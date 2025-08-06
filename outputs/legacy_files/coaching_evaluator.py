"""
AI Coaching Evaluator - Real Performance Measurement System
Measures actual coaching effectiveness and drives iterative improvement
"""

import os
import sys
import json
import time
import logging
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple
import importlib.util
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CoachingEvaluator:
    def __init__(self):
        # Initialize clients only if available and keys are set
        self.openai_client = None
        self.anthropic_client = None
        
        if OPENAI_AVAILABLE and os.getenv('OPENAI_API_KEY'):
            try:
                self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            except Exception as e:
                logger.warning(f"Failed to initialize OpenAI client: {e}")
        
        if ANTHROPIC_AVAILABLE and os.getenv('ANTHROPIC_API_KEY'):
            try:
                self.anthropic_client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
            except Exception as e:
                logger.warning(f"Failed to initialize Anthropic client: {e}")
        
    def load_coach_module(self, coach_path: str):
        """Load AI coach module dynamically"""
        spec = importlib.util.spec_from_file_location("ai_coach", coach_path)
        coach_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(coach_module)
        return coach_module.AICoach()
    
    def generate_realistic_telemetry(self, user_profile: Dict, days: int = 30) -> pd.DataFrame:
        """Generate realistic user telemetry data for testing"""
        data = []
        base_time = datetime.now() - timedelta(days=days)
        
        for day in range(days):
            # Simulate workday patterns
            if day % 7 < 5:  # Weekdays
                for hour in range(9, 18):  # Work hours
                    # Create realistic behavioral patterns
                    cognitive_load = np.random.beta(2, 5)  # More low-medium loads
                    tab_count = max(3, int(np.random.gamma(2, 3)))  # Realistic tab counts
                    
                    # Simulate inefficiency patterns
                    inefficiencies = []
                    if tab_count > 15:
                        inefficiencies.append({"type": "high_tabs", "severity": min(1.0, tab_count/20)})
                    if cognitive_load > 0.7:
                        inefficiencies.append({"type": "cognitive_overload", "severity": cognitive_load})
                    
                    data.append({
                        'timestamp': base_time + timedelta(days=day, hours=hour),
                        'user_id': user_profile['user_id'],
                        'tab_count': tab_count,
                        'cognitive_load_score': cognitive_load,
                        'inefficiencies': inefficiencies,
                        'persona_type': user_profile['persona_type'],
                        'focus_score': max(0, 1 - cognitive_load - (tab_count - 5) * 0.05),
                        'productivity_baseline': user_profile.get('productivity_baseline', 0.7)
                    })
        
        return pd.DataFrame(data)
    
    def measure_coaching_impact(self, coach, telemetry_data: pd.DataFrame, user_profile: Dict) -> Dict[str, float]:
        """Measure actual coaching effectiveness using behavioral change metrics"""
        
        results = []
        behavioral_changes = []
        user_satisfaction_scores = []
        
        for i, row in telemetry_data.iterrows():
            try:
                # Get coaching recommendation (handle async)
                try:
                    coaching_result = coach.analyze_and_coach(
                        data=pd.DataFrame([row]), 
                        user_id=row['user_id']
                    )
                    # If it's a coroutine, we need to run it synchronously for testing
                    if hasattr(coaching_result, '__await__'):
                        import asyncio
                        coaching_result = asyncio.run(coaching_result)
                except Exception as async_error:
                    logger.error(f"Async coaching error: {async_error}")
                    continue
                
                if not coaching_result or 'nudge_text' not in coaching_result:
                    continue
                
                # Simulate user response to coaching
                user_response = self.simulate_user_response(
                    coaching_result, row, user_profile
                )
                
                results.append({
                    'nudge_quality': user_response['nudge_quality'],
                    'behavioral_change': user_response['behavioral_change'],
                    'user_satisfaction': user_response['user_satisfaction'],
                    'relevance_score': user_response['relevance_score'],
                    'actionability': user_response['actionability']
                })
                
                behavioral_changes.append(user_response['behavioral_change'])
                user_satisfaction_scores.append(user_response['user_satisfaction'])
                
            except Exception as e:
                logger.error(f"Error processing coaching for row {i}: {e}")
                continue
        
        if not results:
            return self.get_penalty_metrics()
        
        # Calculate comprehensive performance metrics
        metrics = {
            'avg_nudge_quality': np.mean([r['nudge_quality'] for r in results]),
            'avg_behavioral_change': np.mean(behavioral_changes),
            'avg_user_satisfaction': np.mean(user_satisfaction_scores),
            'avg_relevance': np.mean([r['relevance_score'] for r in results]),
            'avg_actionability': np.mean([r['actionability'] for r in results]),
            'total_interactions': len(results),
            'effectiveness_consistency': 1 - np.std(behavioral_changes),  # Lower std = more consistent
            'user_retention_score': self.calculate_retention_score(user_satisfaction_scores)
        }
        
        # Calculate composite fitness score
        metrics['composite_fitness'] = (
            metrics['avg_behavioral_change'] * 0.3 +
            metrics['avg_user_satisfaction'] * 0.25 +
            metrics['avg_nudge_quality'] * 0.2 +
            metrics['avg_relevance'] * 0.15 +
            metrics['avg_actionability'] * 0.1
        )
        
        return metrics
    
    def simulate_user_response(self, coaching_result: Dict, telemetry_row: pd.Series, user_profile: Dict) -> Dict[str, float]:
        """Simulate realistic user response to coaching using psychological models"""
        
        nudge_text = coaching_result.get('nudge_text', '')
        nudge_type = coaching_result.get('nudge_type', 'unknown')
        
        # Base scores influenced by persona and situation
        persona_type = user_profile.get('persona_type', 'developer')
        cognitive_load = telemetry_row.get('cognitive_load_score', 0.5)
        
        # Persona-specific response patterns
        persona_modifiers = {
            'developer': {'relevance': 0.1, 'quality': 0.15, 'actionability': 0.2},
            'analyst': {'relevance': 0.15, 'quality': 0.1, 'actionability': 0.1},
            'manager': {'relevance': 0.05, 'quality': 0.2, 'actionability': 0.15},
            'designer': {'relevance': 0.2, 'quality': 0.05, 'actionability': 0.1},
            'support': {'relevance': 0.1, 'quality': 0.1, 'actionability': 0.05}
        }
        
        base_modifier = persona_modifiers.get(persona_type, {'relevance': 0.1, 'quality': 0.1, 'actionability': 0.1})
        
        # Evaluate nudge quality (psychological sophistication)
        quality_indicators = [
            'research shows' in nudge_text.lower(),
            'cognitive' in nudge_text.lower() or 'psychology' in nudge_text.lower(),
            len(nudge_text) > 100,  # Detailed explanations
            'consider:' in nudge_text.lower() or 'try:' in nudge_text.lower(),
            any(word in nudge_text.lower() for word in ['flow', 'focus', 'attention', 'efficiency'])
        ]
        
        nudge_quality = 0.3 + sum(quality_indicators) * 0.14 + base_modifier['quality']
        nudge_quality = min(1.0, nudge_quality + np.random.normal(0, 0.1))
        
        # Evaluate relevance to current situation
        relevance_score = 0.4 + base_modifier['relevance']
        if telemetry_row.get('tab_count', 0) > 10 and 'tab' in nudge_text.lower():
            relevance_score += 0.3
        if cognitive_load > 0.7 and any(word in nudge_text.lower() for word in ['overload', 'stress', 'cognitive']):
            relevance_score += 0.3
        
        relevance_score = min(1.0, relevance_score + np.random.normal(0, 0.1))
        
        # Evaluate actionability
        actionability = 0.3 + base_modifier['actionability']
        action_indicators = [
            'close' in nudge_text.lower(),
            'try' in nudge_text.lower(),
            'consider' in nudge_text.lower(),
            '?' in nudge_text  # Questions prompt action
        ]
        actionability += sum(action_indicators) * 0.15
        actionability = min(1.0, actionability + np.random.normal(0, 0.1))
        
        # Calculate behavioral change probability (depends on all factors)
        behavioral_change = (
            nudge_quality * 0.4 +
            relevance_score * 0.35 +
            actionability * 0.25
        ) * (1 - cognitive_load * 0.3)  # High cognitive load reduces action likelihood
        
        # User satisfaction (composite of quality and relevance)
        user_satisfaction = (nudge_quality * 0.6 + relevance_score * 0.4) * np.random.uniform(0.8, 1.2)
        user_satisfaction = max(0, min(1.0, user_satisfaction))
        
        return {
            'nudge_quality': max(0, min(1.0, nudge_quality)),
            'behavioral_change': max(0, min(1.0, behavioral_change)),
            'user_satisfaction': user_satisfaction,
            'relevance_score': max(0, min(1.0, relevance_score)),
            'actionability': max(0, min(1.0, actionability))
        }
    
    def calculate_retention_score(self, satisfaction_scores: List[float]) -> float:
        """Calculate user retention probability based on satisfaction patterns"""
        if not satisfaction_scores:
            return 0.0
        
        avg_satisfaction = np.mean(satisfaction_scores)
        consistency = 1 - np.std(satisfaction_scores)  # Lower variance = more consistent
        
        # Users are more likely to continue using if satisfaction is high and consistent
        retention_score = avg_satisfaction * 0.7 + consistency * 0.3
        return max(0, min(1.0, retention_score))
    
    def get_penalty_metrics(self) -> Dict[str, float]:
        """Return penalty metrics for failed evaluations"""
        return {
            'avg_nudge_quality': 0.0,
            'avg_behavioral_change': 0.0,
            'avg_user_satisfaction': 0.0,
            'avg_relevance': 0.0,
            'avg_actionability': 0.0,
            'total_interactions': 0,
            'effectiveness_consistency': 0.0,
            'user_retention_score': 0.0,
            'composite_fitness': -1.0  # Penalty score
        }
    
    def evaluate_coach(self, coach_path: str, test_scenarios: List[Dict] = None) -> Dict[str, Any]:
        """Comprehensive evaluation of AI coach effectiveness"""
        start_time = time.time()
        
        try:
            logger.info(f"Evaluating coach: {coach_path}")
            
            # Load coach module
            coach = self.load_coach_module(coach_path)
            
            # Generate test scenarios if not provided
            if not test_scenarios:
                test_scenarios = self.generate_test_scenarios()
            
            all_metrics = []
            
            # Test across different user profiles and scenarios
            for scenario in test_scenarios:
                user_profile = scenario['user_profile']
                telemetry = self.generate_realistic_telemetry(user_profile, days=scenario.get('days', 7))
                
                metrics = self.measure_coaching_impact(coach, telemetry, user_profile)
                metrics['scenario'] = scenario['name']
                metrics['persona_type'] = user_profile['persona_type']
                
                all_metrics.append(metrics)
            
            # Aggregate results across all scenarios
            aggregated_metrics = self.aggregate_metrics(all_metrics)
            
            execution_time = time.time() - start_time
            aggregated_metrics['execution_time'] = execution_time
            aggregated_metrics['error'] = ""
            
            # Log results
            self.log_evaluation_results(coach_path, aggregated_metrics)
            
            logger.info(f"Evaluation completed. Composite fitness: {aggregated_metrics['composite_fitness']:.4f}")
            
            return aggregated_metrics
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Evaluation error: {error_msg}")
            
            result = self.get_penalty_metrics()
            result['execution_time'] = time.time() - start_time
            result['error'] = error_msg
            
            self.log_evaluation_results(coach_path, result)
            return result
    
    def generate_test_scenarios(self) -> List[Dict]:
        """Generate diverse test scenarios for comprehensive evaluation"""
        scenarios = [
            {
                'name': 'high_productivity_developer',
                'user_profile': {
                    'user_id': 1,
                    'persona_type': 'developer',
                    'productivity_baseline': 0.8,
                    'focus_preference': 'deep_work'
                },
                'days': 7
            },
            {
                'name': 'distracted_analyst',
                'user_profile': {
                    'user_id': 2,
                    'persona_type': 'analyst',
                    'productivity_baseline': 0.6,
                    'focus_preference': 'structured'
                },
                'days': 7
            },
            {
                'name': 'overloaded_manager',
                'user_profile': {
                    'user_id': 3,
                    'persona_type': 'manager',
                    'productivity_baseline': 0.5,
                    'focus_preference': 'multitask'
                },
                'days': 7
            },
            {
                'name': 'creative_designer',
                'user_profile': {
                    'user_id': 4,
                    'persona_type': 'designer',
                    'productivity_baseline': 0.7,
                    'focus_preference': 'inspiration_driven'
                },
                'days': 7
            },
            {
                'name': 'stressed_support',
                'user_profile': {
                    'user_id': 5,
                    'persona_type': 'support',
                    'productivity_baseline': 0.6,
                    'focus_preference': 'reactive'
                },
                'days': 7
            }
        ]
        return scenarios
    
    def aggregate_metrics(self, metrics_list: List[Dict]) -> Dict[str, float]:
        """Aggregate metrics across all test scenarios"""
        if not metrics_list:
            return self.get_penalty_metrics()
        
        # Calculate weighted averages across scenarios
        aggregated = {}
        
        numeric_keys = [
            'avg_nudge_quality', 'avg_behavioral_change', 'avg_user_satisfaction',
            'avg_relevance', 'avg_actionability', 'effectiveness_consistency',
            'user_retention_score', 'composite_fitness'
        ]
        
        for key in numeric_keys:
            values = [m[key] for m in metrics_list if key in m]
            aggregated[key] = np.mean(values) if values else 0.0
        
        # Total interactions across all scenarios
        aggregated['total_interactions'] = sum(m.get('total_interactions', 0) for m in metrics_list)
        
        # Scenario-specific breakdowns
        aggregated['scenario_results'] = {m['scenario']: m['composite_fitness'] for m in metrics_list}
        
        return aggregated
    
    def log_evaluation_results(self, coach_path: str, metrics: Dict[str, Any]):
        """Log evaluation results to file"""
        results_file = "/Users/stanhus/Documents/work/ai_coach/outputs/coaching_evaluation_results.json"
        
        result_entry = {
            'timestamp': datetime.now().isoformat(),
            'coach_path': os.path.basename(coach_path),
            'metrics': metrics
        }
        
        # Load existing results or create new
        try:
            with open(results_file, 'r') as f:
                results = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            results = []
        
        results.append(result_entry)
        
        # Save updated results
        os.makedirs(os.path.dirname(results_file), exist_ok=True)
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Results logged to {results_file}")


def evaluate_coach(coach_path: str) -> Dict[str, Any]:
    """Main evaluation function"""
    evaluator = CoachingEvaluator()
    return evaluator.evaluate_coach(coach_path)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        coach_path = sys.argv[1]
    else:
        coach_path = "/Users/stanhus/Documents/work/ai_coach/ai_coach.py"
    
    print("Testing coaching evaluator...")
    result = evaluate_coach(coach_path)
    print(f"Evaluation result: {json.dumps(result, indent=2)}")