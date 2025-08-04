#!/usr/bin/env python3
"""
AI COACH - Complete System
==========================

This is the complete AI coaching system that combines all learned intelligence,
adaptive algorithms, persona-specific optimizations, and real-time learning
capabilities into a single comprehensive file.

FEATURES:
- Intelligent persona-specific coaching (Manager, Analyst, Developer, Designer)
- Adaptive learning from user interactions with OpenEvolve-inspired algorithms
- Smart timing and frequency management based on learned patterns
- Specialized templates for Excel/PowerBI/VSCode optimization
- Real-time confidence threshold tuning and mid-session adaptation
- Comprehensive telemetry analysis across multiple dimensions
- Persistent learning state with cross-session improvement
- JSON-serialized interaction logging for continuous learning

INTEGRATION: Ready for WorkSmart platform integration
"""

import asyncio
import json
import logging
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Union
from collections import defaultdict, Counter
from pathlib import Path
import re
import random
import time
import argparse
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('outputs/ai_coach.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

class AICoach:
    """
    Complete AI Coach System with all learned intelligence and adaptive capabilities.
    
    This class represents the culmination of iterative learning and optimization
    based on synthetic user interaction data and OpenEvolve-inspired algorithms.
    Combines all functionality from main.py, ai_coach_analyzer.py, iterative_learning.py,
    and intelligent_improvements.py into a single comprehensive system.
    """
    
    def __init__(self, anthropic_client=None, config: Dict = None):
        """Initialize the AI Coach with all learned intelligence."""
        self.claude = anthropic_client
        self.config = config or {}
        
        # Ensure outputs directory exists
        Path("outputs").mkdir(exist_ok=True)
        
        # Core intelligence parameters (learned from 37+ synthetic interactions)
        self.confidence_threshold = 0.8  # Optimized from 0.7 based on acceptance vs effectiveness
        self.daily_nudge_limits = {'manager': 3, 'analyst': 5, 'developer': 4, 'designer': 4}
        self.nudge_history = []
        self.interaction_history = []
        
        # Session metrics tracking
        self.session_metrics = {
            'nudges_generated': 0,
            'nudges_accepted': 0,
            'total_productivity_lift': 0.0,
            'total_satisfaction_lift': 0.0,
            'evaluation_time_seconds': [],
            'nudge_generation_time_seconds': [],
            'api_errors': 0,
            'json_parse_errors': 0,
            'start_time': datetime.now()
        }
        
        # PERSONA-SPECIFIC INTELLIGENCE (Learned from 37+ interactions)
        self.persona_intelligence = {
            'manager': {
                'language_style': 'consultative',
                'prefixes': [
                    "When you have a moment, consider",
                    "At your convenience, you might",
                    "If it helps, you could try",
                    "You might find it useful to"
                ],
                'avoid_words': ['Want to try', 'You should', 'Need to'],
                'confidence_override': 0.85,  # Higher bar for managers (57% acceptance rate)
                'nudge_interval_minutes': 60,  # Less frequent due to "busy" dismissals
                'optimal_hours': [9, 10, 14, 15],  # Avoid early morning/end of day
                'common_dismissal_reasons': ['busy', 'in_meeting'],
                'acceptance_rate': 0.571,  # Learned from synthetic data
                'avg_effectiveness': 0.27
            },
            'analyst': {
                'language_style': 'technical_helpful',
                'excel_shortcuts': [
                    "Try Ctrl+Arrow keys to navigate data regions - saves ~30 seconds per task",
                    "Use Alt+Tab to switch between Excel sheets - saves 15+ clicks per hour",
                    "Consider Ctrl+Shift+L for instant filters - saves ~2 minutes per dataset",
                    "Want to try some Excel shortcuts? Using Ctrl+Arrow keys to navigate between data regions can save up to 30% of your clicking time."
                ],
                'powerbi_templates': [
                    "Create PowerBI templates now - could save 5+ hours next week",
                    "Try DAX shortcuts with CALCULATE functions - speeds up reports by 40%",
                    "Set up automatic data refresh - eliminates manual updates",
                    "Want to try blocking out 90 minutes for focused PowerBI work? Creating report templates now could save you 5+ hours next week."
                ],
                'data_focus': [
                    "Perfect time for deep data analysis - your environment looks optimized",
                    "Want to block 90 minutes for report creation? Your focus patterns show this is your peak time"
                ],
                'confidence_override': 0.6,  # Lower bar - they accept more (87.5% rate)
                'nudge_interval_minutes': 30,
                'specialization_triggers': ['Excel', 'PowerBI', 'data', 'analysis'],
                'acceptance_rate': 0.875,  # Highest performing persona
                'avg_effectiveness': 0.43
            },
            'developer': {
                'language_style': 'technical_direct',
                'vscode_optimizations': [
                    "Want to try grouping your VSCode tabs into workspaces? It could cut your context switching by 50% and help you stay in flow.",
                    "Use Cmd+Shift+P for quick commands - saves navigation time",
                    "Try workspace-specific settings - improves focus by 30%",
                    "Want to try organizing your browser tabs into dedicated workspaces? Research shows this can cut context-switching time by 30%."
                ],
                'confidence_override': 0.75,
                'nudge_interval_minutes': 45,  # Longer intervals due to frequency complaints
                'quiet_hours': [9, 10, 11, 14, 15, 16],  # Peak coding hours - minimal interruptions
                'flow_state_protection': True,
                'common_dismissal_reasons': ['too_frequent', 'in_flow'],
                'acceptance_rate': 0.778,  # Good acceptance with flow protection
                'avg_effectiveness': 0.38
            },
            'designer': {
                'language_style': 'creative_supportive',
                'confidence_override': 0.7,
                'nudge_interval_minutes': 35,
                'acceptance_rate': 1.0,  # 100% from limited data
                'avg_effectiveness': 0.47
            }
        }
        
        # SMART TIMING ENGINE (Learned from "busy" dismissal patterns)
        self.smart_timing = {
            'avoid_first_hour': True,      # Don't nudge before 9 AM
            'avoid_last_30min': True,      # Don't nudge after 5 PM
            'lunch_break_awareness': True,  # Avoid 12-1 PM
            'meeting_detection': True,      # Learn meeting patterns
            'optimal_hours': [9, 10, 11, 14, 15, 16],  # Peak productivity hours
            'busy_dismissal_threshold': 2,   # Adapt timing after 2 "busy" responses
            'flow_state_detection': True,    # Don't interrupt long focus periods
            'respect_focus_sessions': True   # Honor user focus time
        }
        
        # LEARNING METRICS AND ADAPTATION
        self.learning_metrics = {
            'total_interactions': 0,
            'acceptance_rate': 0.0,
            'avg_effectiveness': 0.0,
            'persona_performance': defaultdict(dict),
            'evolution_history': [],
            'adaptation_count': 0
        }
        
        # NUDGE TEMPLATES (Enhanced with learned patterns)
        self.nudge_templates = {
            'focus': {
                'high_switches': "Lots of context switching detected. Want to try closing {tab_count} tabs for a focused sprint?",
                'no_deep_work': "It's been 2 hours without deep focus time. Ready for a distraction-free session?",
                'cognitive_overload': "Your cognitive load is peaking. How about a 5-minute break to reset?",
                'tab_management': "Want to try consolidating those {tab_count} browser tabs into 2-3? Research shows it could help you stay more focused."
            },
            'wellbeing': {
                'long_streak': "You've been at it for {hours} hours straight. Time to stretch and hydrate?",
                'no_breaks': "No breaks detected today. A quick walk could boost your afternoon productivity.",
                'late_hours': "Working late again? Consider wrapping up to maintain tomorrow's performance.",
                'cognitive_load': "Want to try a 5-minute break to reset? Your cognitive load suggests it could help."
            },
            'value_creation': {
                'low_core_work': "Only {core_percentage}% on core tasks today. Want to block time for important work?",
                'automation_opportunity': "I notice repetitive tasks. Want to try automating {task_type}?",
                'high_value_focus': "Perfect time for high-value work. Want to try a focused 90-minute session?",
                'email_batching': "Want to try email batching? Checking email just 3x daily could free up 90 minutes for your core work."
            },
            'productivity': {
                'window_switching': "High window switching detected. Want to try focus mode for better flow?",
                'interruption_management': "Multiple interruptions detected. Want to try blocking focus time?",
                'time_blocking': "Want to try time-blocking? Setting aside 30 minutes for {task_type} could help reduce context switching."
            }
        }
        
        # Load previous learning state if available
        self._load_learning_state()
        
        logger.info("AI Coach initialized with complete learned intelligence")
    
    async def analyze_and_coach(self, telemetry_data: pd.DataFrame, user_id: int) -> Optional[Dict]:
        """
        Main coaching analysis method - the complete intelligence engine.
        Combines all analysis capabilities from the original system.
        
        Args:
            telemetry_data: Real-time user telemetry data
            user_id: Unique user identifier
            
        Returns:
            Coaching nudge dict or None if no action needed
        """
        try:
            start_time = time.time()
            
            # Extract user context and persona
            user_context = self._extract_user_context(telemetry_data)
            user_persona = telemetry_data['persona_type'].iloc[0] if 'persona_type' in telemetry_data.columns else 'analyst'
            
            # Pre-flight checks using learned intelligence
            if not self._should_send_nudge(user_id, user_persona, user_context):
                return None
            
            # Multi-dimensional analysis (from ai_coach_analyzer.py)
            analysis_results = await self._run_comprehensive_analysis(telemetry_data, user_context)
            
            # Generate intelligent nudge with persona optimization
            nudge = await self._generate_intelligent_nudge(analysis_results, user_context, user_persona)
            
            analysis_time = time.time() - start_time
            self.session_metrics['evaluation_time_seconds'].append(analysis_time)
            
            if nudge and nudge.get('confidence', 0) >= self._get_persona_confidence_threshold(user_persona):
                # Apply persona-specific customizations
                nudge = self._customize_nudge_for_persona(nudge, user_persona, user_context)
                
                # Log for continuous learning
                self._log_nudge_generation(user_id, user_persona, nudge, user_context)
                return nudge
                
            return None
            
        except Exception as e:
            logger.error(f"Coaching analysis failed: {str(e)}")
            self.session_metrics['api_errors'] += 1
            return None
    
    def _extract_user_context(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Extract comprehensive user context from telemetry data."""
        try:
            latest = data.iloc[-1]
            
            context = {
                'timestamp': latest.get('timestamp', datetime.now().isoformat()),
                'current_hour': datetime.fromisoformat(latest.get('timestamp', datetime.now().isoformat())).hour,
                'tab_count': int(latest.get('tab_count', 3)),
                'window_switches': int(data['window_switches_15min'].sum()) if 'window_switches_15min' in data.columns else 5,
                'focus_duration': int(latest.get('focus_session_duration', 15)),
                'cognitive_load': float(latest.get('cognitive_load_score', 0.5)),
                'app_active': latest.get('app_active', 'Browser'),
                'task_category': latest.get('task_category', 'support'),
                'keystrokes_per_min': float(latest.get('keystrokes_per_min', 60)),
                'break_duration': int(data['break_duration_min'].sum()) if 'break_duration_min' in data.columns else 5,
                'interruption_count': int(data['interruption_count'].sum()) if 'interruption_count' in data.columns else 2,
                'core_work_percentage': float(latest.get('core_work_percentage', 0.3)),
                'value_score': float(latest.get('value_score', 0.5)),
                'productivity_score': float(latest.get('productivity_score', 0.6)),
                'meeting_duration': int(data['meeting_duration_min'].sum()) if 'meeting_duration_min' in data.columns else 0
            }
            
            # Contextual flags for intelligent decision making
            context['flags'] = []
            if context['tab_count'] > 5:
                context['flags'].append('high_tab_count')
            if context['window_switches'] > 10:
                context['flags'].append('frequent_switching')
            if context['focus_duration'] > 45:
                context['flags'].append('good_focus')
            elif context['focus_duration'] < 15:
                context['flags'].append('short_focus')
            if context['cognitive_load'] > 0.8:
                context['flags'].append('cognitive_overload')
            if context['core_work_percentage'] < 0.3:
                context['flags'].append('low_core_work')
            if context['current_hour'] > 16:
                context['flags'].append('end_of_day')
            if context['interruption_count'] > 5:
                context['flags'].append('high_interruptions')
            if context['meeting_duration'] > 240:
                context['flags'].append('meeting_heavy_day')
            if context['break_duration'] < 5:
                context['flags'].append('no_breaks')
                
            return context
            
        except Exception as e:
            logger.error(f"Context extraction failed: {str(e)}")
            return {'flags': [], 'current_hour': 12, 'tab_count': 3}
    
    def _should_send_nudge(self, user_id: int, persona: str, context: Dict) -> bool:
        """Comprehensive pre-flight check using all learned patterns."""
        try:
            # Check timing intelligence
            if not self._is_optimal_timing(persona, context):
                return False
            
            # Check frequency limits with persona-specific intervals
            if self._exceeds_frequency_limit(user_id, persona):
                return False
            
            # Check recent dismissal patterns
            if self._has_recent_dismissals(user_id, persona):
                return False
            
            # Check daily nudge limits
            daily_key = f"{user_id}_{datetime.now().strftime('%Y-%m-%d')}"
            daily_count = sum(1 for h in self.nudge_history if h.get('daily_key') == daily_key)
            if daily_count >= self.daily_nudge_limits.get(persona, 4):
                return False
            
            # Check for flow state protection (especially for developers)
            if persona == 'developer' and self._is_in_flow_state(context):
                return False
                
            return True
            
        except Exception:
            return True  # Default to allowing nudge
    
    def _is_optimal_timing(self, persona: str, context: Dict) -> bool:
        """Check if current timing is optimal based on learned patterns."""
        current_hour = context.get('current_hour', datetime.now().hour)
        
        # Apply global smart timing rules
        if self.smart_timing['avoid_first_hour'] and current_hour <= 8:
            return False
        if self.smart_timing['avoid_last_30min'] and current_hour >= 17:
            return False
        if self.smart_timing['lunch_break_awareness'] and 12 <= current_hour <= 13:
            return False
        
        # Apply persona-specific timing
        persona_config = self.persona_intelligence.get(persona, {})
        
        # Check quiet hours (especially important for developers)
        if 'quiet_hours' in persona_config and current_hour in persona_config['quiet_hours']:
            # Allow exceptions for very high urgency situations
            if context.get('cognitive_load', 0) < 0.9 and not any(flag in context.get('flags', []) for flag in ['cognitive_overload', 'high_interruptions']):
                return False
        
        # Check optimal hours preference
        if 'optimal_hours' in persona_config and current_hour not in persona_config['optimal_hours']:
            # Only strict for managers (who have the most "busy" dismissals)
            if persona == 'manager':
                return False
            
        return True
    
    def _exceeds_frequency_limit(self, user_id: int, persona: str) -> bool:
        """Check frequency limits with persona-specific intervals."""
        persona_config = self.persona_intelligence.get(persona, {})
        interval_minutes = persona_config.get('nudge_interval_minutes', 30)
        
        recent_cutoff = datetime.now() - timedelta(minutes=interval_minutes)
        recent_nudges = [
            n for n in self.nudge_history 
            if n.get('user_id') == user_id and 
            datetime.fromisoformat(n.get('timestamp', '1900-01-01')) > recent_cutoff
        ]
        
        return len(recent_nudges) > 0
    
    def _has_recent_dismissals(self, user_id: int, persona: str) -> bool:
        """Check for recent dismissal patterns suggesting we should back off."""
        recent_interactions = [
            i for i in self.interaction_history[-10:]  # Last 10 interactions
            if i.get('user_id') == user_id and not i.get('outcome', {}).get('accepted', False)
        ]
        
        # Be more sensitive for personas with known dismissal issues
        threshold = 1 if persona == 'manager' else 2  # Managers dismiss more often
        return len(recent_interactions) >= threshold
    
    def _is_in_flow_state(self, context: Dict) -> bool:
        """Detect if user is in flow state (especially important for developers)."""
        # Flow state indicators
        long_focus = context.get('focus_duration', 0) > 30
        low_switches = context.get('window_switches', 10) < 5
        active_coding = context.get('app_active', '') in ['VSCode', 'IntelliJ', 'PyCharm', 'Sublime']
        high_keystrokes = context.get('keystrokes_per_min', 0) > 80
        
        # Require multiple indicators for flow state
        flow_indicators = sum([long_focus, low_switches, active_coding, high_keystrokes])
        return flow_indicators >= 2
    
    async def _run_comprehensive_analysis(self, data: pd.DataFrame, context: Dict) -> Dict[str, Any]:
        """Run comprehensive multi-dimensional analysis combining all original capabilities."""
        
        # Prepare data summary for analysis
        data_summary = self._prepare_data_summary(data)
        
        analysis = {
            'focus_analysis': self._analyze_focus_patterns(data, context),
            'productivity_analysis': self._analyze_productivity_patterns(data, context),
            'wellbeing_analysis': self._analyze_wellbeing_patterns(data, context),
            'value_creation_analysis': self._analyze_value_creation(data, context),
            'automation_opportunities': self._identify_automation_opportunities(data, context),
            'context_switching_analysis': self._analyze_context_switching(data, context),
            'time_management_analysis': self._analyze_time_management(data, context)
        }
        
        # Calculate overall urgency and priority scores
        urgency_scores = []
        for dimension, result in analysis.items():
            if isinstance(result, dict) and 'urgency_score' in result:
                urgency_scores.append(result['urgency_score'])
        
        analysis['overall_urgency'] = np.mean(urgency_scores) if urgency_scores else 0.5
        analysis['data_summary'] = data_summary
        
        return analysis
    
    def _prepare_data_summary(self, data_chunk: pd.DataFrame) -> Dict:
        """Prepare comprehensive data summary with proper JSON serialization."""
        import numpy as np
        
        def convert_numpy_types(obj):
            """Convert numpy types to native Python types for JSON serialization."""
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {key: convert_numpy_types(value) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [convert_numpy_types(item) for item in obj]
            return obj
        
        try:
            summary = {
                'record_count': len(data_chunk),
                'time_range': {
                    'start': str(data_chunk['timestamp'].min()) if 'timestamp' in data_chunk.columns else str(datetime.now()),
                    'end': str(data_chunk['timestamp'].max()) if 'timestamp' in data_chunk.columns else str(datetime.now())
                },
                'user_metrics': {
                    'avg_keystrokes': float(data_chunk['keystrokes_per_min'].mean()) if 'keystrokes_per_min' in data_chunk.columns else 60.0,
                    'total_window_switches': int(data_chunk['window_switches_15min'].sum()) if 'window_switches_15min' in data_chunk.columns else 5,
                    'avg_cognitive_load': float(data_chunk['cognitive_load_score'].mean()) if 'cognitive_load_score' in data_chunk.columns else 0.5,
                    'max_focus_duration': int(data_chunk['focus_session_duration'].max()) if 'focus_session_duration' in data_chunk.columns else 15,
                    'break_time': int(data_chunk['break_duration_min'].sum()) if 'break_duration_min' in data_chunk.columns else 5,
                    'tab_count': float(data_chunk['tab_count'].mean()) if 'tab_count' in data_chunk.columns else 3.0
                },
                'app_usage': convert_numpy_types(data_chunk['app_active'].value_counts().to_dict()) if 'app_active' in data_chunk.columns else {'Browser': 1},
                'task_distribution': convert_numpy_types(data_chunk['task_category'].value_counts().to_dict()) if 'task_category' in data_chunk.columns else {'support': 1},
                'recent_activities': convert_numpy_types(data_chunk[['timestamp', 'app_active', 'task_category'] if all(col in data_chunk.columns for col in ['timestamp', 'app_active', 'task_category']) else data_chunk.columns[:3]].tail(5).to_dict('records'))
            }
            
            return summary
        except Exception as e:
            logger.error(f"Data summary preparation failed: {str(e)}")
            return {'record_count': 0, 'user_metrics': {}}
    
    def _analyze_focus_patterns(self, data: pd.DataFrame, context: Dict) -> Dict:
        """Analyze focus and attention patterns."""
        focus_score = 0.8 - (context['window_switches'] / 20)  # More switches = lower focus
        focus_score = max(0.1, min(1.0, focus_score))
        
        issues = []
        recommendations = []
        
        if context['tab_count'] > 5:
            issues.append(f"High tab count ({context['tab_count']})")
            recommendations.append("Close unused tabs or organize into workspaces")
        if context['window_switches'] > 10:
            issues.append(f"Frequent window switching ({context['window_switches']})")
            recommendations.append("Try focus mode or dedicated work blocks")
        if context['focus_duration'] < 15:
            issues.append(f"Short focus sessions ({context['focus_duration']}min)")
            recommendations.append("Set up 25-minute focused work periods")
        
        return {
            'focus_score': focus_score,
            'urgency_score': 1.0 - focus_score,
            'issues': issues,
            'recommendations': recommendations,
            'analysis_type': 'focus'
        }
    
    def _analyze_productivity_patterns(self, data: pd.DataFrame, context: Dict) -> Dict:
        """Analyze productivity patterns and bottlenecks."""
        productivity_score = (context['keystrokes_per_min'] / 100) * 0.4 + context['value_score'] * 0.6
        productivity_score = max(0.1, min(1.0, productivity_score))
        
        issues = []
        recommendations = []
        
        if context['core_work_percentage'] < 0.3:
            issues.append(f"Low core work time ({context['core_work_percentage']:.1%})")
            recommendations.append("Block time for core work activities")
        if context['interruption_count'] > 5:
            issues.append(f"High interruption count ({context['interruption_count']})")
            recommendations.append("Enable focus mode to reduce interruptions")
        
        return {
            'productivity_score': productivity_score,
            'urgency_score': 1.0 - productivity_score,
            'issues': issues,
            'recommendations': recommendations,
            'analysis_type': 'productivity'
        }
    
    def _analyze_wellbeing_patterns(self, data: pd.DataFrame, context: Dict) -> Dict:
        """Analyze wellbeing and stress indicators."""
        wellbeing_score = 1.0 - context['cognitive_load']
        if context['break_duration'] < 10:
            wellbeing_score *= 0.8  # Penalize lack of breaks
        
        issues = []
        recommendations = []
        
        if context['cognitive_load'] > 0.8:
            issues.append("High cognitive load detected")
            recommendations.append("Take a 5-minute break to reset")
        if context['break_duration'] < 5:
            issues.append("No breaks taken recently")
            recommendations.append("Schedule regular 5-minute breaks")
        
        return {
            'wellbeing_score': wellbeing_score,
            'urgency_score': 1.0 - wellbeing_score,
            'issues': issues,
            'recommendations': recommendations,
            'analysis_type': 'wellbeing'
        }
    
    def _analyze_value_creation(self, data: pd.DataFrame, context: Dict) -> Dict:
        """Analyze value creation patterns."""
        value_score = context['value_score']
        
        issues = []
        recommendations = []
        
        if value_score < 0.4:
            issues.append(f"Low value creation score ({value_score:.1f})")
            recommendations.append("Focus on high-value activities")
        if context['task_category'] == 'support' and context['core_work_percentage'] < 0.2:
            issues.append("Too much reactive support work")
            recommendations.append("Batch support tasks into dedicated blocks")
        
        return {
            'value_score': value_score,
            'urgency_score': 1.0 - value_score,
            'issues': issues,
            'recommendations': recommendations,
            'analysis_type': 'value_creation'
        }
    
    def _identify_automation_opportunities(self, data: pd.DataFrame, context: Dict) -> Dict:
        """Identify opportunities for automation and optimization."""
        opportunities = []
        automation_score = 0.3  # Base score
        
        app_active = context.get('app_active', '')
        
        if 'Excel' in app_active and context['window_switches'] > 5:
            opportunities.append("Excel keyboard shortcuts could reduce navigation time")
            automation_score += 0.3
        
        if 'PowerBI' in app_active or 'Power BI' in app_active:
            opportunities.append("PowerBI templates could save hours per week")
            automation_score += 0.4
        
        if context['tab_count'] > 6:
            opportunities.append("Browser workspace organization could improve focus")
            automation_score += 0.2
        
        if 'VSCode' in app_active or 'Visual Studio' in app_active:
            opportunities.append("VSCode workspace optimization could reduce context switching")
            automation_score += 0.3
        
        return {
            'opportunities': opportunities,
            'urgency_score': min(1.0, automation_score),
            'automation_potential': automation_score,
            'analysis_type': 'automation'
        }
    
    def _analyze_context_switching(self, data: pd.DataFrame, context: Dict) -> Dict:
        """Analyze context switching patterns."""
        switching_score = max(0.1, 1.0 - (context['window_switches'] / 15))
        
        issues = []
        if context['window_switches'] > 15:
            issues.append("Excessive context switching detected")
        if context['tab_count'] > 8:
            issues.append("High tab count contributing to switching")
        
        return {
            'switching_score': switching_score,
            'urgency_score': 1.0 - switching_score,
            'issues': issues,
            'analysis_type': 'context_switching'
        }
    
    def _analyze_time_management(self, data: pd.DataFrame, context: Dict) -> Dict:
        """Analyze time management patterns."""
        time_score = context['core_work_percentage']
        
        issues = []
        if context['meeting_duration'] > 240:
            issues.append("Meeting-heavy day detected")
        if context['core_work_percentage'] < 0.3:
            issues.append("Low core work percentage")
        
        return {
            'time_score': time_score,
            'urgency_score': 1.0 - time_score,
            'issues': issues,
            'analysis_type': 'time_management'
        }
    
    async def _generate_intelligent_nudge(self, analysis: Dict, context: Dict, persona: str) -> Optional[Dict]:
        """Generate intelligent nudge using all learned patterns and analysis."""
        try:
            # Get the most urgent dimension
            urgency_scores = {
                dim: result.get('urgency_score', 0)
                for dim, result in analysis.items()
                if isinstance(result, dict) and 'urgency_score' in result
            }
            
            if not urgency_scores:
                return None
                
            most_urgent = max(urgency_scores.items(), key=lambda x: x[1])
            urgency_dimension, urgency_score = most_urgent
            
            if urgency_score < 0.3:  # Not urgent enough
                return None
            
            # Generate persona-specific nudge text
            nudge_text = self._generate_persona_nudge_text(urgency_dimension, analysis, context, persona)
            
            if not nudge_text:
                return None
            
            # Calculate confidence based on multiple factors
            confidence = self._calculate_nudge_confidence(analysis, context, persona)
            
            return {
                'nudge_text': nudge_text,
                'nudge_type': 'value_creation',  # Primary type based on learning
                'confidence': confidence,
                'urgency_score': urgency_score,
                'trigger_dimension': urgency_dimension,
                'expected_outcome': self._generate_expected_outcome(urgency_dimension, analysis, context),
                'trigger_reason': self._generate_trigger_reason(analysis, context),
                'snooze_options': ['15min', '1hour', 'rest-of-day'],
                'persona_optimized': True,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Nudge generation failed: {str(e)}")
            return None
    
    def _generate_persona_nudge_text(self, urgency_dimension: str, analysis: Dict, context: Dict, persona: str) -> str:
        """Generate persona-optimized nudge text using all learned templates."""
        persona_config = self.persona_intelligence.get(persona, {})
        
        # Check for specialized templates first (especially for analysts)
        if persona == 'analyst':
            specialized_text = self._get_analyst_specialized_text(context)
            if specialized_text:
                return specialized_text
        
        # Check for developer-specific templates
        elif persona == 'developer':
            dev_text = self._get_developer_specialized_text(context)
            if dev_text:
                return dev_text
        
        # Generate base nudge text based on urgency dimension
        base_text = self._generate_base_nudge_text(urgency_dimension, analysis, context)
        
        # Apply persona-specific language styling
        if persona_config.get('language_style') == 'consultative':
            # Manager style - softer, less pushy
            base_text = self._apply_consultative_tone(base_text, persona_config)
        elif persona_config.get('language_style') == 'technical_direct':
            # Developer style - technical and direct
            base_text = self._apply_technical_tone(base_text, context)
        
        return base_text
    
    def _get_analyst_specialized_text(self, context: Dict) -> Optional[str]:
        """Get specialized text for analysts based on app usage (87.5% acceptance rate)."""
        app_active = context.get('app_active', '')
        analyst_config = self.persona_intelligence['analyst']
        
        if 'Excel' in app_active:
            return random.choice(analyst_config['excel_shortcuts'])
        elif 'PowerBI' in app_active or 'Power BI' in app_active:
            return random.choice(analyst_config['powerbi_templates'])
        elif context.get('focus_duration', 0) > 20:
            return random.choice(analyst_config['data_focus'])
        
        return None
    
    def _get_developer_specialized_text(self, context: Dict) -> Optional[str]:
        """Get specialized text for developers based on app usage."""
        app_active = context.get('app_active', '')
        developer_config = self.persona_intelligence['developer']
        
        if 'VSCode' in app_active or 'Visual Studio' in app_active:
            return random.choice(developer_config['vscode_optimizations'])
        
        return None
    
    def _generate_base_nudge_text(self, urgency_dimension: str, analysis: Dict, context: Dict) -> str:
        """Generate base nudge text based on urgency dimension using learned templates."""
        dimension_result = analysis.get(urgency_dimension, {})
        
        if urgency_dimension == 'focus_analysis':
            if context['tab_count'] > 5:
                template = self.nudge_templates['focus']['tab_management']
                return template.format(tab_count=context['tab_count'])
            elif context['window_switches'] > 10:
                return self.nudge_templates['focus']['high_switches'].format(tab_count=max(3, context['tab_count'] - 3))
            else:
                return self.nudge_templates['focus']['no_deep_work']
        
        elif urgency_dimension == 'productivity_analysis':
            if context['core_work_percentage'] < 0.3:
                return self.nudge_templates['productivity']['time_blocking'].format(task_type='core work')
            else:
                return self.nudge_templates['productivity']['interruption_management']
        
        elif urgency_dimension == 'value_creation_analysis':
            if context['value_score'] < 0.4:
                template = self.nudge_templates['value_creation']['low_core_work']
                return template.format(core_percentage=int(context['core_work_percentage'] * 100))
            else:
                return self.nudge_templates['value_creation']['high_value_focus']
        
        elif urgency_dimension == 'wellbeing_analysis':
            if context['cognitive_load'] > 0.8:
                return self.nudge_templates['wellbeing']['cognitive_load']
            elif context['break_duration'] < 5:
                return self.nudge_templates['wellbeing']['no_breaks']
            else:
                return self.nudge_templates['wellbeing']['long_streak'].format(hours=2)
        
        elif urgency_dimension == 'automation_opportunities':
            opportunities = dimension_result.get('opportunities', [])
            if opportunities:
                return f"Want to try {opportunities[0].lower()}? It could significantly improve your workflow efficiency."
        
        # Fallback
        return "Want to try a focused 25-minute work session? It could help boost your productivity and focus."
    
    def _apply_consultative_tone(self, text: str, persona_config: Dict) -> str:
        """Apply consultative tone for managers (learned from 57% acceptance rate)."""
        avoid_words = persona_config.get('avoid_words', [])
        prefixes = persona_config.get('prefixes', [])
        
        # Replace direct language with softer alternatives
        for avoid_word in avoid_words:
            if avoid_word in text:
                prefix = random.choice(prefixes)
                text = text.replace(avoid_word, prefix, 1)
        
        # Remove emojis for professional tone
        text = re.sub(r'[🎯🚀💡🔧⚡️✨🤔💻📊🎨]', '', text).strip()
        
        return text
    
    def _apply_technical_tone(self, text: str, context: Dict) -> str:
        """Apply technical tone for developers."""
        app_active = context.get('app_active', '')
        
        # Add technical specificity
        if 'VSCode' in app_active or 'Visual Studio' in app_active:
            if 'tabs' in text and 'VSCode' not in text:
                text = text.replace('tabs', 'VSCode tabs')
            if 'workspace' not in text.lower() and 'organization' in text:
                text += " You could group them into workspaces for better organization."
        
        return text
    
    def _calculate_nudge_confidence(self, analysis: Dict, context: Dict, persona: str) -> float:
        """Calculate nudge confidence using all learned patterns."""
        base_confidence = 0.7
        
        # Adjust based on persona success rates (learned from synthetic data)
        persona_config = self.persona_intelligence.get(persona, {})
        if 'acceptance_rate' in persona_config:
            acceptance_rate = persona_config['acceptance_rate']
            # Boost confidence for high-accepting personas
            base_confidence += (acceptance_rate - 0.5) * 0.3
        
        # Adjust based on urgency
        overall_urgency = analysis.get('overall_urgency', 0.5)
        base_confidence += (overall_urgency - 0.5) * 0.3
        
        # Adjust based on context clarity (more flags = clearer situation)
        flag_count = len(context.get('flags', []))
        if flag_count > 2:
            base_confidence += 0.1
        elif flag_count < 1:
            base_confidence -= 0.1
        
        # Adjust based on specialization triggers
        if persona == 'analyst' and any(trigger in context.get('app_active', '') for trigger in ['Excel', 'PowerBI']):
            base_confidence += 0.15  # High confidence for analyst specializations
        
        return max(0.1, min(0.95, base_confidence))
    
    def _get_persona_confidence_threshold(self, persona: str) -> float:
        """Get persona-specific confidence threshold (learned optimization)."""
        persona_config = self.persona_intelligence.get(persona, {})
        return persona_config.get('confidence_override', self.confidence_threshold)
    
    def _customize_nudge_for_persona(self, nudge: Dict, persona: str, context: Dict) -> Dict:
        """Apply final persona-specific customizations to the nudge."""
        persona_config = self.persona_intelligence.get(persona, {})
        
        # Apply language style customizations
        if persona_config.get('language_style') == 'consultative':
            # Ensure professional tone for managers
            nudge['nudge_text'] = re.sub(r'[🎯🚀💡🔧⚡️✨]', '', nudge['nudge_text']).strip()
        
        # Add persona-specific expected outcomes
        if persona == 'analyst' and any(app in context.get('app_active', '') for app in ['Excel', 'PowerBI']):
            nudge['expected_outcome'] += " with specialized tool optimization"
        elif persona == 'developer' and 'VSCode' in context.get('app_active', ''):
            nudge['expected_outcome'] += " through development environment optimization"
        
        return nudge
    
    def _generate_expected_outcome(self, urgency_dimension: str, analysis: Dict, context: Dict) -> str:
        """Generate detailed expected outcome description."""
        base_outcomes = {
            'focus_analysis': "Improved focus and reduced context switching leading to higher productivity",
            'productivity_analysis': "Increased core work completion and better time allocation",
            'value_creation_analysis': "Higher value output and more meaningful work accomplishment",
            'wellbeing_analysis': "Reduced stress and improved work-life balance",
            'automation_opportunities': "Streamlined workflow and reduced manual effort",
            'context_switching_analysis': "Reduced cognitive load and improved task completion",
            'time_management_analysis': "Better time allocation and increased efficiency"
        }
        
        return base_outcomes.get(urgency_dimension, "Enhanced workflow efficiency and better work experience")
    
    def _generate_trigger_reason(self, analysis: Dict, context: Dict) -> str:
        """Generate detailed trigger reason explanation."""
        reasons = []
        
        if context['tab_count'] > 5:
            reasons.append(f"High tab count ({context['tab_count']})")
        if context['window_switches'] > 10:
            reasons.append(f"Frequent context switching ({context['window_switches']} switches)")
        if context['core_work_percentage'] < 0.3:
            reasons.append(f"Low core work percentage ({context['core_work_percentage']:.1%})")
        if context['cognitive_load'] > 0.8:
            reasons.append("High cognitive load detected")
        if context['interruption_count'] > 5:
            reasons.append(f"High interruption count ({context['interruption_count']})")
        if context['focus_duration'] < 15:
            reasons.append(f"Short focus sessions ({context['focus_duration']}min)")
        
        return "; ".join(reasons) if reasons else "Optimization opportunity identified"
    
    def _log_nudge_generation(self, user_id: int, persona: str, nudge: Dict, context: Dict):
        """Log nudge generation for learning and analysis."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'persona': persona,
            'nudge': nudge,
            'context_flags': context.get('flags', []),
            'confidence_threshold_used': self._get_persona_confidence_threshold(persona),
            'generation_source': 'ai_coach_comprehensive'
        }
        
        self.nudge_history.append({
            'timestamp': nudge['timestamp'],
            'user_id': user_id,
            'persona': persona,
            'nudge_type': nudge['nudge_type'],
            'confidence': nudge['confidence'],
            'daily_key': f"{user_id}_{datetime.now().strftime('%Y-%m-%d')}"
        })
        
        # Save to persistent log
        try:
            with open('outputs/nudge_generation_log.jsonl', 'a') as f:
                f.write(json.dumps(log_entry, default=str) + '\n')
        except Exception as e:
            logger.error(f"Failed to log nudge generation: {str(e)}")
    
    def record_user_interaction(self, user_id: int, persona: str, nudge: Dict, outcome: Dict):
        """Record user interaction for continuous learning and adaptation."""
        # Convert numpy types for JSON serialization
        def convert_for_json(obj):
            if isinstance(obj, (np.integer, np.int64)):
                return int(obj)
            elif isinstance(obj, (np.floating, np.float64)):
                return float(obj)
            elif isinstance(obj, dict):
                return {key: convert_for_json(value) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [convert_for_json(item) for item in obj]
            return obj
        
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'persona': persona,
            'nudge': nudge,
            'outcome': outcome,
            'effectiveness_score': self._calculate_effectiveness_score(nudge, outcome)
        }
        
        self.interaction_history.append(interaction)
        self._update_learning_metrics(interaction)
        self._adapt_based_on_interaction(interaction)
        
        # Update session metrics
        self.session_metrics['nudges_generated'] += 1
        if outcome.get('accepted', False):
            self.session_metrics['nudges_accepted'] += 1
            self.session_metrics['total_productivity_lift'] += outcome.get('productivity_impact', 0)
            self.session_metrics['total_satisfaction_lift'] += outcome.get('satisfaction_impact', 0)
        
        # Log interaction
        self._log_coaching_interaction(user_id, persona, nudge, outcome)
        
        # Save to persistent storage
        try:
            with open('outputs/coaching_interactions.jsonl', 'a') as f:
                f.write(json.dumps(convert_for_json(interaction)) + '\n')
        except Exception as e:
            logger.error(f"Failed to save interaction: {str(e)}")
    
    def _calculate_effectiveness_score(self, nudge: Dict, outcome: Dict) -> float:
        """Calculate comprehensive effectiveness score."""
        if not outcome.get('accepted', False):
            return 0.0
        
        # Weight different factors
        confidence_weight = nudge.get('confidence', 0.7) * 0.3
        impact_weight = (
            outcome.get('productivity_impact', 0) + 
            outcome.get('satisfaction_impact', 0)
        ) * 0.5
        response_time_weight = min(0.2, 30 / max(1, outcome.get('response_time_seconds', 30))) # Faster response = higher score
        
        return min(1.0, confidence_weight + impact_weight + response_time_weight)
    
    def _update_learning_metrics(self, interaction: Dict):
        """Update comprehensive learning metrics."""
        self.learning_metrics['total_interactions'] += 1
        
        # Update acceptance rate
        accepted_count = sum(1 for i in self.interaction_history if i['outcome'].get('accepted', False))
        self.learning_metrics['acceptance_rate'] = accepted_count / len(self.interaction_history)
        
        # Update effectiveness
        effectiveness_scores = [i['effectiveness_score'] for i in self.interaction_history]
        self.learning_metrics['avg_effectiveness'] = np.mean(effectiveness_scores)
        
        # Update persona-specific metrics
        persona = interaction['persona']
        persona_interactions = [i for i in self.interaction_history if i['persona'] == persona]
        
        self.learning_metrics['persona_performance'][persona] = {
            'total_interactions': len(persona_interactions),
            'acceptance_rate': np.mean([i['outcome'].get('accepted', False) for i in persona_interactions]),
            'avg_effectiveness': np.mean([i['effectiveness_score'] for i in persona_interactions]),
            'common_dismissal_reasons': Counter([
                i['outcome'].get('dismissal_reason', 'unknown') 
                for i in persona_interactions 
                if not i['outcome'].get('accepted', False)
            ]).most_common(3)
        }
    
    def _adapt_based_on_interaction(self, interaction: Dict):
        """Adapt coaching strategy based on interaction outcome (OpenEvolve-inspired)."""
        persona = interaction['persona']
        outcome = interaction['outcome']
        nudge = interaction['nudge']
        
        self.learning_metrics['adaptation_count'] += 1
        
        # Record adaptation in evolution history
        adaptation = {
            'timestamp': datetime.now().isoformat(),
            'persona': persona,
            'trigger': 'interaction_feedback',
            'adaptation_type': None,
            'old_value': None,
            'new_value': None
        }
        
        # If dismissed, analyze reason and adapt
        if not outcome.get('accepted', False):
            dismissal_reason = outcome.get('dismissal_reason', 'unknown')
            
            if dismissal_reason == 'too_frequent':
                # Increase interval for this persona
                current_interval = self.persona_intelligence.get(persona, {}).get('nudge_interval_minutes', 30)
                new_interval = min(120, current_interval + 15)  # Max 2 hours
                
                if persona not in self.persona_intelligence:
                    self.persona_intelligence[persona] = {}
                
                adaptation.update({
                    'adaptation_type': 'frequency_increase',
                    'old_value': current_interval,
                    'new_value': new_interval
                })
                
                self.persona_intelligence[persona]['nudge_interval_minutes'] = new_interval
                logger.info(f"Increased {persona} nudge interval to {new_interval} minutes")
            
            elif dismissal_reason == 'busy':
                # Adjust timing for this persona
                current_hour = datetime.now().hour
                persona_config = self.persona_intelligence.setdefault(persona, {})
                avoid_hours = persona_config.setdefault('avoid_hours', [])
                
                if current_hour not in avoid_hours:
                    avoid_hours.append(current_hour)
                    adaptation.update({
                        'adaptation_type': 'timing_adjustment',
                        'old_value': avoid_hours[:-1],
                        'new_value': avoid_hours
                    })
                    logger.info(f"Added {current_hour}:00 to {persona} avoid hours")
            
            elif dismissal_reason in ['not_relevant', 'unclear']:
                # Increase confidence threshold for this persona
                current_threshold = self.persona_intelligence.get(persona, {}).get('confidence_override', self.confidence_threshold)
                new_threshold = min(0.95, current_threshold + 0.05)
                
                self.persona_intelligence.setdefault(persona, {})['confidence_override'] = new_threshold
                adaptation.update({
                    'adaptation_type': 'confidence_increase',
                    'old_value': current_threshold,
                    'new_value': new_threshold
                })
                logger.info(f"Increased {persona} confidence threshold to {new_threshold:.2f}")
        
        # If accepted with high effectiveness, reinforce strategy
        elif interaction['effectiveness_score'] > 0.7:
            # Lower confidence threshold slightly for this persona (more aggressive)
            current_threshold = self.persona_intelligence.get(persona, {}).get('confidence_override', self.confidence_threshold)
            new_threshold = max(0.5, current_threshold - 0.02)
            
            self.persona_intelligence.setdefault(persona, {})['confidence_override'] = new_threshold
            adaptation.update({
                'adaptation_type': 'confidence_decrease',
                'old_value': current_threshold,
                'new_value': new_threshold
            })
            logger.info(f"Lowered {persona} confidence threshold to {new_threshold:.2f} (reinforcing success)")
        
        # Record adaptation
        if adaptation['adaptation_type']:
            self.learning_metrics['evolution_history'].append(adaptation)
    
    def _log_coaching_interaction(self, user_id: int, persona: str, nudge: Dict, outcome: Dict):
        """Log coaching interaction with structured output."""
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'persona': persona,
            'nudge': nudge,
            'outcome': outcome,
            'effectiveness_score': self._calculate_effectiveness_score(nudge, outcome)
        }
        
        # Console output
        print(f"💬 NUDGE for User {user_id} ({persona}):")
        print(f"   Text: {nudge['nudge_text']}")
        print(f"   Type: {nudge['nudge_type']} | Confidence: {nudge['confidence']:.2f}")
        print(f"   Accepted: {'✅' if outcome['accepted'] else '❌'}")
        
        if outcome['accepted']:
            productivity_impact = outcome.get('productivity_impact', 0)
            satisfaction_impact = outcome.get('satisfaction_impact', 0)
            print(f"   Impact: +{productivity_impact:.1%} productivity, +{satisfaction_impact:.1%} satisfaction")
        else:
            dismissal_reason = outcome.get('dismissal_reason', 'unknown')
            print(f"   Dismissal Reason: {dismissal_reason}")
    
    def _load_learning_state(self):
        """Load previous learning state for continuous improvement."""
        try:
            state_file = Path("outputs/ai_coach_learning_state.json")
            if state_file.exists():
                with open(state_file, 'r') as f:
                    state = json.load(f)
                
                # Restore learned parameters
                if 'confidence_threshold' in state:
                    self.confidence_threshold = state['confidence_threshold']
                
                if 'persona_intelligence' in state:
                    # Merge with default intelligence
                    for persona, config in state['persona_intelligence'].items():
                        if persona in self.persona_intelligence:
                            self.persona_intelligence[persona].update(config)
                        else:
                            self.persona_intelligence[persona] = config
                
                if 'learning_metrics' in state:
                    self.learning_metrics.update(state['learning_metrics'])
                
                if 'smart_timing' in state:
                    self.smart_timing.update(state['smart_timing'])
                
                logger.info(f"Loaded learning state from {state.get('timestamp', 'unknown time')}")
                
        except Exception as e:
            logger.info("No previous learning state found - starting fresh")
    
    def save_learning_state(self):
        """Save current learning state for persistence."""
        try:
            state = {
                'timestamp': datetime.now().isoformat(),
                'confidence_threshold': self.confidence_threshold,
                'persona_intelligence': self.persona_intelligence,
                'learning_metrics': dict(self.learning_metrics),
                'smart_timing': self.smart_timing,
                'total_interactions': len(self.interaction_history),
                'session_metrics': self.session_metrics
            }
            
            with open("outputs/ai_coach_learning_state.json", 'w') as f:
                json.dump(state, f, indent=2, default=str)
                
            logger.info("Learning state saved successfully")
            
        except Exception as e:
            logger.error(f"Failed to save learning state: {str(e)}")
    
    async def run_coaching_session(self, telemetry_generator, duration_minutes: int = 60, adaptive_learning: bool = True):
        """Run a complete coaching session with real-time adaptation."""
        print(f"🎯 Starting {duration_minutes}-minute coaching session...")
        
        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=duration_minutes)
        
        # Generate continuous data stream
        data_stream = telemetry_generator.generate_real_time_stream()
        
        chunk_count = 0
        learning_check_interval = max(5, duration_minutes // 4)  # Learn every 1/4 of session
        
        async for data_chunk in data_stream:
            if datetime.now() >= end_time:
                break
            
            chunk_count += 1
            await self._process_data_chunk(data_chunk, chunk_count)
            
            # Adaptive learning during session
            if adaptive_learning and chunk_count % learning_check_interval == 0:
                await self._mid_session_learning_update(chunk_count)
            
            # Simulate real-time delay
            await asyncio.sleep(1)  # Accelerated for demo
        
        # Final learning update and metrics
        if adaptive_learning:
            await self._final_learning_update()
        
        self._print_comprehensive_summary()
    
    async def _process_data_chunk(self, data_chunk: pd.DataFrame, chunk_id: int):
        """Process a chunk of telemetry data and generate coaching suggestions."""
        print(f"\n📊 Processing chunk {chunk_id} ({len(data_chunk)} records)")
        
        # Group by user for individual analysis
        for user_id in data_chunk['user_id'].unique():
            user_data = data_chunk[data_chunk['user_id'] == user_id]
            
            # Analyze with AI Coach
            start_time = time.time()
            nudge = await self.analyze_and_coach(user_data, user_id)
            analysis_time = time.time() - start_time
            
            if nudge:
                # Generate user response simulation
                user_persona = user_data['persona_type'].iloc[0] if 'persona_type' in user_data.columns else 'analyst'
                outcome = self._simulate_user_response(user_persona, nudge)
                
                # Record the interaction for learning
                self.record_user_interaction(user_id, user_persona, nudge, outcome)
    
    def _simulate_user_response(self, persona: str, nudge: Dict) -> Dict:
        """Simulate realistic user response based on learned patterns."""
        # Use learned acceptance rates
        persona_config = self.persona_intelligence.get(persona, {})
        base_acceptance_rate = persona_config.get('acceptance_rate', 0.7)
        
        # Adjust based on nudge confidence
        confidence_boost = (nudge['confidence'] - 0.5) * 0.3
        final_acceptance_rate = min(0.95, base_acceptance_rate + confidence_boost)
        
        accepted = random.random() < final_acceptance_rate
        
        if accepted:
            return {
                'accepted': True,
                'response_time_seconds': random.uniform(5, 30),
                'productivity_impact': random.uniform(0.08, 0.20),
                'satisfaction_impact': random.uniform(0.10, 0.16),
                'follow_through_probability': 0.84,
                'user_feedback': random.choice([
                    "Will block time for important work",
                    "Good point about automation", 
                    "Restructuring my priorities"
                ])
            }
        else:
            # Use learned dismissal reasons
            common_dismissals = persona_config.get('common_dismissal_reasons', ['busy', 'not_relevant'])
            dismissal_reason = random.choice(common_dismissals)
            
            return {
                'accepted': False,
                'dismissal_reason': dismissal_reason,
                'productivity_impact': 0.0,
                'satisfaction_impact': -0.02,
                'response_time_seconds': random.uniform(1, 5),
                'user_feedback': random.choice([
                    "Not now", "Too busy", "Not helpful", "In the middle of something"
                ])
            }
    
    async def _mid_session_learning_update(self, chunk_id: int):
        """Perform mid-session learning adjustments."""
        try:
            if not self.interaction_history:
                return
            
            recent_interactions = self.interaction_history[-10:]  # Last 10 interactions
            recent_acceptance = np.mean([i['outcome'].get('accepted', False) for i in recent_interactions])
            
            # Quick adjustments based on current session performance
            if recent_acceptance < 0.5:
                # Lower confidence threshold for more nudges
                old_threshold = self.confidence_threshold
                self.confidence_threshold = max(0.6, old_threshold - 0.05)
                print(f"🔧 Mid-session: Lowered confidence threshold ({old_threshold:.2f} → {self.confidence_threshold:.2f})")
                
            elif recent_acceptance > 0.9:
                # Raise confidence threshold for quality
                old_threshold = self.confidence_threshold
                self.confidence_threshold = min(0.9, old_threshold + 0.05)
                print(f"🔧 Mid-session: Raised confidence threshold ({old_threshold:.2f} → {self.confidence_threshold:.2f})")
            
            print(f"📊 Mid-session check (chunk {chunk_id}): {recent_acceptance:.1%} acceptance rate")
                
        except Exception as e:
            logger.error(f"Mid-session learning failed: {str(e)}")
    
    async def _final_learning_update(self):
        """Perform final learning update after session."""
        try:
            print("\n🧠 Performing final learning update...")
            
            # Apply any new improvements discovered during session
            adaptation_count = len(self.learning_metrics.get('evolution_history', []))
            
            if adaptation_count > 0:
                print(f"✅ Applied {adaptation_count} adaptations during session")
                
                # Show latest adaptations
                recent_adaptations = self.learning_metrics['evolution_history'][-3:]
                for adaptation in recent_adaptations:
                    print(f"   • {adaptation['adaptation_type']} for {adaptation['persona']}")
            else:
                print("ℹ️ No new adaptations needed")
            
            # Save learning state for next session
            self.save_learning_state()
            print("💾 Learning state saved for next session")
            
        except Exception as e:
            logger.error(f"Final learning update failed: {str(e)}")
    
    def _print_comprehensive_summary(self):
        """Print comprehensive session summary with all metrics."""
        metrics = self.session_metrics
        
        print("\n" + "="*60)
        print("📈 AI COACH SESSION SUMMARY")
        print("="*60)
        
        # Basic counts
        acceptance_rate = (metrics['nudges_accepted'] / max(1, metrics['nudges_generated'])) * 100
        print(f"Nudges Generated: {metrics['nudges_generated']}")
        print(f"Nudges Accepted: {metrics['nudges_accepted']} ({acceptance_rate:.1f}%)")
        
        # Performance metrics
        if metrics['evaluation_time_seconds']:
            avg_eval_time = sum(metrics['evaluation_time_seconds']) / len(metrics['evaluation_time_seconds'])
            print(f"Average Evaluation Time: {avg_eval_time:.2f} seconds")
        else:
            avg_eval_time = 0
        
        # Impact metrics
        if metrics['nudges_accepted'] > 0:
            avg_productivity_lift = metrics['total_productivity_lift'] / metrics['nudges_accepted']
            avg_satisfaction_lift = metrics['total_satisfaction_lift'] / metrics['nudges_accepted']
        else:
            avg_productivity_lift = 0
            avg_satisfaction_lift = 0
        
        print(f"Average Productivity Lift: +{avg_productivity_lift:.1%}")
        print(f"Average Satisfaction Lift: +{avg_satisfaction_lift:.1%}")
        
        # ROI calculation
        total_productivity_lift = metrics['total_productivity_lift']
        simulated_roi = total_productivity_lift * 50 * 40 * 83 * 13  # 50 users, 40hrs/week, $83/hr, 13 weeks
        
        print(f"Simulated Quarterly ROI: ${simulated_roi:,.0f}")
        
        # Target comparisons
        print("\n🎯 TARGET COMPARISONS:")
        print(f"Acceptance Rate: {acceptance_rate:.1f}% (Target: >65%) {'✅' if acceptance_rate > 65 else '❌'}")
        print(f"Avg Productivity Lift: +{avg_productivity_lift:.1%} (Target: >12%) {'✅' if avg_productivity_lift > 0.12 else '❌'}")
        print(f"Response Time: {avg_eval_time:.1f}s (Target: <5s) {'✅' if avg_eval_time < 5 else '❌'}")
        
        # Intelligence status
        self._print_intelligence_summary()
    
    def _print_intelligence_summary(self):
        """Print current intelligence and learning status."""
        print(f"\n🧠 INTELLIGENCE STATUS:")
        print(f"   Current Confidence Threshold: {self.confidence_threshold:.2f}")
        print(f"   Total Learning Interactions: {self.learning_metrics['total_interactions']}")
        print(f"   Overall Acceptance Rate: {self.learning_metrics['acceptance_rate']:.1%}")
        print(f"   Overall Effectiveness: {self.learning_metrics['avg_effectiveness']:.2f}")
        
        # Show persona adaptations
        active_adaptations = []
        for persona, config in self.persona_intelligence.items():
            if 'confidence_override' in config:
                active_adaptations.append(f"Confidence tuning for {persona}")
            if 'nudge_interval_minutes' in config:
                active_adaptations.append(f"Frequency control for {persona}")
            if 'avoid_hours' in config:
                active_adaptations.append(f"Timing optimization for {persona}")
        
        if active_adaptations:
            print(f"   Active Adaptations:")
            for adaptation in active_adaptations[:5]:  # Show top 5
                print(f"     • {adaptation}")
        
        # Learning status
        total_interactions = self.learning_metrics['total_interactions']
        status = '🟢 Active' if total_interactions > 10 else '🟡 Building' if total_interactions > 0 else '🔴 Starting'
        print(f"   Learning Status: {status}")
    
    def get_intelligence_summary(self) -> Dict[str, Any]:
        """Get comprehensive summary of current intelligence and learning status."""
        return {
            'version': '1.0-complete',
            'learning_status': {
                'total_interactions': self.learning_metrics['total_interactions'],
                'acceptance_rate': self.learning_metrics['acceptance_rate'],
                'avg_effectiveness': self.learning_metrics['avg_effectiveness'],
                'adaptation_count': self.learning_metrics['adaptation_count'],
                'status': 'Active' if self.learning_metrics['total_interactions'] > 10 else 'Building'
            },
            'persona_intelligence': {
                persona: {
                    'confidence_threshold': config.get('confidence_override', self.confidence_threshold),
                    'nudge_interval': config.get('nudge_interval_minutes', 30),
                    'acceptance_rate': config.get('acceptance_rate', 0.7),
                    'specializations': len(config.get('excel_shortcuts', [])) + len(config.get('powerbi_templates', [])) + len(config.get('vscode_optimizations', [])),
                    'performance': self.learning_metrics['persona_performance'].get(persona, {})
                }
                for persona, config in self.persona_intelligence.items()
            },
            'smart_timing': self.smart_timing,
            'session_metrics': self.session_metrics,
            'optimization_features': [
                'Persona-specific language adaptation',
                'Smart timing and frequency management', 
                'Specialized analyst templates (Excel/PowerBI)',
                'Developer flow-state protection',
                'Adaptive confidence thresholds',
                'Real-time learning and adjustment',
                'Context-aware nudge generation',
                'Multi-dimensional telemetry analysis',
                'OpenEvolve-inspired strategy evolution',
                'Comprehensive interaction logging'
            ]
        }

# WORKMART INTEGRATION FUNCTIONS
def create_workmart_ai_coach(anthropic_api_key: str, config: Dict = None) -> AICoach:
    """
    Factory function to create WorkSmart-ready AI Coach instance.
    
    Args:
        anthropic_api_key: Anthropic Claude API key
        config: Optional configuration dictionary
        
    Returns:
        Configured AICoach instance ready for integration
    """
    try:
        # Import Anthropic client - replace with actual implementation
        # from anthropic import Anthropic
        # client = Anthropic(api_key=anthropic_api_key)
        
        # For now, using None for demo purposes
        client = None
        
        return AICoach(client, config)
        
    except ImportError:
        logger.warning("Anthropic client not available - using mock for testing")
        return AICoach(None, config)

async def process_workmart_telemetry(coach: AICoach, telemetry_data: Dict, user_id: int) -> Optional[Dict]:
    """
    Process WorkSmart telemetry data and return coaching recommendation.
    
    Args:
        coach: AICoach instance
        telemetry_data: Real-time telemetry from WorkSmart platform
        user_id: WorkSmart user identifier
        
    Returns:
        Coaching nudge dictionary or None
    """
    try:
        # Convert WorkSmart telemetry to DataFrame format
        df = pd.DataFrame([telemetry_data])
        
        # Generate coaching recommendation
        nudge = await coach.analyze_and_coach(df, user_id)
        
        return nudge
        
    except Exception as e:
        logger.error(f"WorkSmart telemetry processing failed: {str(e)}")
        return None

def record_workmart_interaction(coach: AICoach, user_id: int, persona: str, nudge: Dict, user_response: Dict):
    """
    Record WorkSmart user interaction with coaching system.
    
    Args:
        coach: AICoach instance
        user_id: WorkSmart user identifier
        persona: User persona type
        nudge: Original coaching nudge
        user_response: User's response to the nudge
    """
    coach.record_user_interaction(user_id, persona, nudge, user_response)

# MAIN EXECUTION
async def main():
    """Main entry point for the AI Coach system."""
    parser = argparse.ArgumentParser(description='AI Coach Complete System')
    parser.add_argument('--mode', choices=['demo', 'test', 'session'], default='demo',
                       help='Run mode: demo (show capabilities), test (run tests), session (full coaching)')
    parser.add_argument('--duration', type=int, default=5,
                       help='Duration for session mode in minutes')
    parser.add_argument('--users', type=int, default=6,
                       help='Number of synthetic users for session mode')
    parser.add_argument('--adaptive', action='store_true', default=True,
                       help='Enable adaptive learning during session')
    
    args = parser.parse_args()
    
    print("🧠 AI COACH - COMPLETE SYSTEM")
    print("="*50)
    
    # Initialize AI Coach
    coach = AICoach(None)  # Mock client for demo
    
    if args.mode == 'demo':
        # Show intelligence summary
        summary = coach.get_intelligence_summary()
        print(f"Learning Status: {summary['learning_status']['status']}")
        print(f"Total Features: {len(summary['optimization_features'])}")
        print(f"Persona Profiles: {len(summary['persona_intelligence'])}")
        
        print(f"\n💡 OPTIMIZATION FEATURES:")
        for feature in summary['optimization_features']:
            print(f"   • {feature}")
            
        print(f"\n🎯 Ready for WorkSmart integration!")
        
    elif args.mode == 'test':
        # Run basic functionality tests
        print("🧪 Running system tests...")
        
        # Test telemetry processing
        test_telemetry = pd.DataFrame([{
            'timestamp': datetime.now().isoformat(),
            'persona_type': 'analyst',
            'tab_count': 8,
            'window_switches_15min': 12,
            'focus_session_duration': 20,
            'cognitive_load_score': 0.7,
            'app_active': 'Excel',
            'task_category': 'analysis',
            'keystrokes_per_min': 85,
            'break_duration_min': 5,
            'interruption_count': 3,
            'core_work_percentage': 0.4,
            'value_score': 0.5
        }])
        
        nudge = await coach.analyze_and_coach(test_telemetry, user_id=999)
        
        if nudge:
            print(f"✅ System test passed:")
            print(f"   Generated nudge with {nudge['confidence']:.2f} confidence")
            print(f"   Persona optimized: {nudge.get('persona_optimized', False)}")
        else:
            print(f"❌ System test failed - no nudge generated")
            
    elif args.mode == 'session':
        # Run full coaching session (requires telemetry generator)
        print(f"⚠️ Session mode requires telemetry generator")
        print(f"   Use synthetic_data_generator.py to create telemetry data")
        
    return coach

if __name__ == "__main__":
    asyncio.run(main())