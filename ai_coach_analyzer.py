"""
AI Coach Analyzer with Claude Integration
Processes telemetry data and generates contextual coaching nudges.
"""

import json
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List
import pandas as pd
import re

# Import robust JSON parser
try:
    from json_parser import parse_llm_json
except ImportError:
    # Fallback if robust parser not available
    def parse_llm_json(response: str, expected_type: str) -> Optional[Dict[str, Any]]:
        try:
            return json.loads(response)
        except:
            return None

logger = logging.getLogger(__name__)

class AICoachAnalyzer:
    """Main analyzer that processes telemetry and generates nudges."""
    
    def __init__(self, claude_client, evolved_prompts: Dict[str, str]):
        self.claude = claude_client
        self.prompts = evolved_prompts
        self.daily_nudge_count = {}
        self.confidence_threshold = 0.7
        self.nudge_history = []  # Track recent nudges to avoid repetition
        
        # Nudge templates for fallback
        self.nudge_templates = {
            'focus': {
                'high_switches': "Lots of context switching detected. Want to try closing {tab_count} tabs for a focused sprint?",
                'no_deep_work': "It's been 2 hours without deep focus time. Ready for a distraction-free session?",
                'cognitive_overload': "Your cognitive load is peaking. How about a 5-minute break to reset?"
            },
            'wellbeing': {
                'long_streak': "You've been at it for {hours} hours straight. Time to stretch and hydrate?",
                'no_breaks': "No breaks detected today. A quick walk could boost your afternoon productivity.",
                'late_hours': "Working late again? Consider wrapping up to maintain tomorrow's performance."
            },
            'value_creation': {
                'low_core_work': "Only {core_percentage}% on core tasks today. Want to block time for important work?",
                'repetitive_task': "This task takes {time_spent} weekly. Interested in a 5-minute automation guide?",
                'meeting_overload': "Meetings consuming {meeting_percentage}% of your day. Time to decline some invites?"
            }
        }
    
    async def analyze_telemetry_chunk(self, data_chunk: pd.DataFrame, user_id: int) -> Optional[Dict]:
        """Analyze telemetry data and generate nudge if appropriate."""
        # Check daily nudge limit
        today = datetime.now().strftime('%Y-%m-%d')
        daily_key = f"{user_id}_{today}"
        
        if self.daily_nudge_count.get(daily_key, 0) >= 3:
            return None
        
        # Check if enough time has passed since last nudge (minimum 30 minutes)
        if self._too_soon_for_nudge(user_id):
            return None
        
        # Run all evaluators in parallel
        evaluation_tasks = []
        for evaluator_name, prompt_template in self.prompts.items():
            task = self._run_evaluator(evaluator_name, prompt_template, data_chunk)
            evaluation_tasks.append(task)
        
        evaluations_list = await asyncio.gather(*evaluation_tasks)
        
        # Convert to dict
        evaluations = {}
        for i, evaluator_name in enumerate(self.prompts.keys()):
            evaluations[evaluator_name] = evaluations_list[i]
        
        # Generate nudge based on evaluations
        nudge = await self._generate_nudge(evaluations, data_chunk, user_id)
        
        if nudge and nudge.get('confidence', 0) >= self.confidence_threshold:
            # Update counters
            self.daily_nudge_count[daily_key] = self.daily_nudge_count.get(daily_key, 0) + 1
            self.nudge_history.append({
                'user_id': user_id,
                'timestamp': datetime.now(),
                'nudge_type': nudge.get('nudge_type')
            })
            
            return nudge
        
        return None
    
    def _too_soon_for_nudge(self, user_id: int) -> bool:
        """Check if it's too soon to send another nudge to this user."""
        recent_nudges = [n for n in self.nudge_history 
                        if n['user_id'] == user_id 
                        and n['timestamp'] > datetime.now() - timedelta(minutes=30)]
        return len(recent_nudges) > 0
    
    async def _run_evaluator(self, evaluator_name: str, prompt_template: str, 
                           data_chunk: pd.DataFrame) -> Dict:
        """Run a single evaluator on the data."""
        # Prepare data summary for the prompt
        data_summary = self._prepare_data_summary(data_chunk)
        
        # Format prompt
        try:
            filled_prompt = prompt_template.format(telemetry_chunk=json.dumps(data_summary))
        except:
            # Fallback formatting
            filled_prompt = prompt_template.replace("{telemetry_chunk}", json.dumps(data_summary))
        
        # Add context
        enhanced_prompt = f"""
{filled_prompt}

Additional context:
- Current time: {datetime.now().strftime('%Y-%m-%d %H:%M')}
- Data represents the last 15 minutes of activity
- User has received {self.daily_nudge_count.get(f"{data_chunk['user_id'].iloc[0]}_{datetime.now().strftime('%Y-%m-%d')}", 0)} nudges today

Respond with valid JSON only. No additional text or explanation.
"""
        
        try:
            response = await self.claude.generate(
                enhanced_prompt,
                max_tokens=500,
                temperature=0.3
            )
            
            # Use robust JSON parser
            parsed_result = parse_llm_json(response, evaluator_name)
            
            if parsed_result is None:
                logger.warning(f"Failed to parse JSON from {evaluator_name}")
                return {"error": "JSON parsing failed", "raw_response": response[:200]}
            
            return parsed_result
            
        except Exception as e:
            logger.error(f"Evaluator {evaluator_name} failed: {str(e)}")
            return {"error": str(e), "evaluator": evaluator_name}
    
    def _prepare_data_summary(self, data_chunk: pd.DataFrame) -> Dict:
        """Prepare a summary of the data chunk for analysis."""
        summary = {
            'record_count': len(data_chunk),
            'time_range': {
                'start': data_chunk['timestamp'].min(),
                'end': data_chunk['timestamp'].max()
            },
            'user_metrics': {
                'avg_keystrokes': data_chunk['keystrokes_per_min'].mean(),
                'total_window_switches': data_chunk['window_switches_15min'].sum(),
                'avg_cognitive_load': data_chunk['cognitive_load_score'].mean(),
                'max_focus_duration': data_chunk['focus_session_duration'].max(),
                'break_time': data_chunk['break_duration_min'].sum(),
                'tab_count': data_chunk['tab_count'].mean()
            },
            'app_usage': data_chunk['app_active'].value_counts().to_dict(),
            'task_distribution': data_chunk['task_category'].value_counts().to_dict(),
            'recent_activities': data_chunk[['timestamp', 'app_active', 'task_category']].tail(5).to_dict('records')
        }
        
        return summary
    
    async def _generate_nudge(self, evaluations: Dict, data_chunk: pd.DataFrame, 
                            user_id: int) -> Optional[Dict]:
        """Generate appropriate nudge based on evaluations."""
        # Calculate urgency scores
        urgency_scores = {}
        
        for eval_name, eval_result in evaluations.items():
            if 'error' in eval_result:
                continue
                
            # Extract scores
            if 'focus_score' in eval_result:
                urgency_scores['focus'] = 100 - eval_result.get('focus_score', 50)
            elif 'wellbeing_score' in eval_result:
                urgency_scores['wellbeing'] = 100 - eval_result.get('wellbeing_score', 50)
            elif 'value_score' in eval_result:
                urgency_scores['value_creation'] = 100 - eval_result.get('value_score', 50)
        
        if not urgency_scores:
            return None
        
        # Find highest priority issue
        primary_concern = max(urgency_scores.items(), key=lambda x: x[1])
        concern_type, concern_score = primary_concern
        
        # Only nudge if score indicates real issue (>30 urgency)
        if concern_score < 30:
            return None
        
        # Get relevant evaluation
        relevant_eval = None
        for eval_name, eval_result in evaluations.items():
            if concern_type in eval_name:
                relevant_eval = eval_result
                break
        
        if not relevant_eval:
            return None
        
        # Generate contextual nudge
        nudge_data = {
            'concern_type': concern_type,
            'concern_score': concern_score,
            'evaluation': relevant_eval,
            'data_chunk': data_chunk
        }
        
        return await self._create_contextual_nudge(nudge_data)
    
    async def _create_contextual_nudge(self, nudge_data: Dict) -> Dict:
        """Create a contextual nudge with Claude."""
        concern_type = nudge_data['concern_type']
        evaluation = nudge_data['evaluation']
        data_chunk = nudge_data['data_chunk']
        
        # Extract relevant metrics
        latest_data = data_chunk.iloc[-1]
        
        nudge_prompt = f"""
Generate a helpful, friendly nudge for a {concern_type} issue in workplace productivity.

Context:
- Issue type: {concern_type}
- Severity: {nudge_data['concern_score']}/100
- Current app: {latest_data['app_active']}
- Tab count: {latest_data['tab_count']}
- Recent switches: {latest_data['window_switches_15min']}
- Evaluation details: {json.dumps(evaluation)}

Requirements:
1. Be friendly and supportive, not commanding
2. Make it specific and actionable
3. Use "Want to try..." or "How about..." phrasing
4. Keep it under 40 words
5. Include a specific metric or number when relevant
6. Focus on the immediate benefit

Output as JSON:
{{
    "nudge_text": "Your friendly suggestion here",
    "nudge_type": "{concern_type}",
    "confidence": 0.0-1.0,
    "expected_outcome": "Brief description of expected benefit",
    "trigger_reason": "What triggered this nudge",
    "snooze_options": ["15min", "1hour", "rest-of-day"]
}}
"""
        
        try:
            response = await self.claude.generate(
                nudge_prompt,
                max_tokens=300,
                temperature=0.7
            )
            
            nudge = json.loads(response)
            
            # Validate nudge
            if self._validate_nudge(nudge):
                return nudge
            else:
                # Fallback to template
                return self._generate_template_nudge(concern_type, latest_data)
                
        except Exception as e:
            print(f"⚠️ Nudge generation failed: {e}")
            # Fallback to template
            return self._generate_template_nudge(concern_type, latest_data)
    
    def _validate_nudge(self, nudge: Dict) -> bool:
        """Validate nudge has required fields and appropriate content."""
        required_fields = ['nudge_text', 'nudge_type', 'confidence', 'expected_outcome']
        
        # Check fields
        if not all(field in nudge for field in required_fields):
            return False
        
        # Check nudge text length
        if len(nudge['nudge_text'].split()) > 50:
            return False
        
        # Check confidence is valid
        if not isinstance(nudge.get('confidence', 0), (int, float)):
            return False
        
        if not 0 <= nudge.get('confidence', 0) <= 1:
            return False
        
        return True
    
    def _generate_template_nudge(self, concern_type: str, latest_data: pd.Series) -> Dict:
        """Generate nudge from templates as fallback."""
        templates = self.nudge_templates.get(concern_type, self.nudge_templates['focus'])
        
        # Select appropriate template
        if concern_type == 'focus':
            if latest_data['window_switches_15min'] > 18:
                template = templates['high_switches']
                nudge_text = template.format(tab_count=int(latest_data['tab_count']))
                trigger = "high_context_switching"
            else:
                template = templates['no_deep_work']
                nudge_text = template
                trigger = "no_deep_work"
        
        elif concern_type == 'wellbeing':
            if latest_data['focus_session_duration'] > 120:
                template = templates['long_streak']
                nudge_text = template.format(hours=round(latest_data['focus_session_duration'] / 60, 1))
                trigger = "long_work_streak"
            else:
                template = templates['no_breaks']
                nudge_text = template
                trigger = "no_breaks"
        
        else:  # value_creation
            template = templates['low_core_work']
            nudge_text = template.format(core_percentage=30)  # Default value
            trigger = "low_core_work"
        
        return {
            'nudge_text': nudge_text,
            'nudge_type': concern_type,
            'confidence': 0.8,  # High confidence for template nudges
            'expected_outcome': f"Improved {concern_type.replace('_', ' ')}",
            'trigger_reason': trigger,
            'snooze_options': ['15min', '1hour', 'rest-of-day']
        }
    
    def get_analytics(self) -> Dict:
        """Get analytics on nudge generation."""
        total_nudges = sum(self.daily_nudge_count.values())
        
        nudge_types = {}
        for nudge in self.nudge_history:
            nudge_type = nudge.get('nudge_type', 'unknown')
            nudge_types[nudge_type] = nudge_types.get(nudge_type, 0) + 1
        
        return {
            'total_nudges': total_nudges,
            'nudges_by_type': nudge_types,
            'users_reached': len(set(n['user_id'] for n in self.nudge_history)),
            'avg_daily_nudges': total_nudges / max(1, len(set(
                n['timestamp'].date() for n in self.nudge_history
            )))
        }