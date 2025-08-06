#!/usr/bin/env python3
"""
Enhanced AI Coach - Evolved Productivity Coaching System
=====================================================

Combines best elements from parent systems with improved:
- Personalized intervention strategies
- Context-aware coaching
- Evidence-based behavioral psychology
- Cognitive load optimization
- Actionable recommendations

Version: 3.0 (Enhanced Evolution)
"""

import asyncio
import pandas as pd
import numpy as np
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from dataclasses import dataclass
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class UserContext:
    cognitive_load: float  # 0-1 scale
    attention_state: str   # focused, distracted, fatigued
    time_of_day: datetime
    recent_activity: List[str]
    behavioral_patterns: Dict[str, float]
    intervention_history: List[Dict]
    satisfaction_scores: List[float]

class CognitiveLoadTracker:
    def __init__(self):
        self.load_history = []
        self.attention_states = []
        
    def update_load(self, metrics: Dict[str, float]) -> float:
        """Calculate cognitive load based on multiple metrics"""
        # Weighted combination of activity intensity, task switching, time pressure
        load = (0.4 * metrics['activity_intensity'] +
                0.3 * metrics['task_switching_rate'] +
                0.3 * metrics['time_pressure'])
        self.load_history.append(load)
        return load

    def get_attention_state(self) -> str:
        """Determine current attention state"""
        recent_load = self.load_history[-10:]
        if np.mean(recent_load) > 0.8:
            return "fatigued"
        elif np.std(recent_load) > 0.3:
            return "distracted" 
        return "focused"

class BehavioralPsychology:
    def __init__(self):
        self.intervention_strategies = {
            'implementation_intentions': {
                'trigger': 'goal_setting',
                'format': 'if-then planning',
                'effectiveness': 0.85
            },
            'habit_stacking': {
                'trigger': 'routine_detection', 
                'format': 'anchor_behavior',
                'effectiveness': 0.78
            },
            'temptation_bundling': {
                'trigger': 'motivation_low',
                'format': 'pair_activities',
                'effectiveness': 0.72
            }
        }
        
    def select_strategy(self, context: UserContext) -> Dict:
        """Choose optimal intervention strategy based on context"""
        if context.cognitive_load > 0.7:
            return self.intervention_strategies['habit_stacking']
        elif context.attention_state == 'distracted':
            return self.intervention_strategies['implementation_intentions']
        return self.intervention_strategies['temptation_bundling']

class PersonalizedCoach:
    def __init__(self):
        self.cognitive_tracker = CognitiveLoadTracker()
        self.behavior_engine = BehavioralPsychology()
        self.user_contexts: Dict[str, UserContext] = {}
        
    async def update_user_context(self, user_id: str, metrics: Dict[str, float]):
        """Update user context with new metrics"""
        if user_id not in self.user_contexts:
            self.user_contexts[user_id] = UserContext(
                cognitive_load=0.0,
                attention_state="focused",
                time_of_day=datetime.now(),
                recent_activity=[],
                behavioral_patterns={},
                intervention_history=[],
                satisfaction_scores=[]
            )
            
        context = self.user_contexts[user_id]
        context.cognitive_load = self.cognitive_tracker.update_load(metrics)
        context.attention_state = self.cognitive_tracker.get_attention_state()
        context.time_of_day = datetime.now()
        context.recent_activity.append(metrics['current_activity'])
        
    def generate_intervention(self, user_id: str) -> Dict[str, Any]:
        """Generate personalized coaching intervention"""
        context = self.user_contexts[user_id]
        strategy = self.behavior_engine.select_strategy(context)
        
        intervention = {
            'type': strategy['trigger'],
            'format': strategy['format'],
            'timing': self._optimize_timing(context),
            'content': self._generate_content(context, strategy),
            'action_items': self._generate_actions(context, strategy)
        }
        
        context.intervention_history.append(intervention)
        return intervention
    
    def _optimize_timing(self, context: UserContext) -> Dict[str, Any]:
        """Determine optimal intervention timing"""
        return {
            'delay': max(0, 0.7 - context.cognitive_load) * 3600,  # Scale with cognitive load
            'frequency': 'high' if context.attention_state == 'focused' else 'low',
            'preferred_time': self._get_preferred_time(context)
        }
    
    def _generate_content(self, context: UserContext, strategy: Dict) -> str:
        """Generate contextual intervention content"""
        templates = {
            'implementation_intentions': "When {trigger}, I will {action}",
            'habit_stacking': "After {current}, I will {new}",
            'temptation_bundling': "Only {reward} while {task}"
        }
        return templates[strategy['trigger']].format(
            trigger=context.recent_activity[-1],
            action="take focused action",
            current="completing current task",
            new="begin next priority",
            reward="enjoy break",
            task="making progress"
        )
    
    def _generate_actions(self, context: UserContext, strategy: Dict) -> List[str]:
        """Generate specific actionable recommendations"""
        return [
            f"Break down next task into 25-minute focused sessions",
            f"Use {strategy['format']} technique for next activity transition",
            f"Record progress in productivity journal"
        ]
    
    def _get_preferred_time(self, context: UserContext) -> datetime:
        """Calculate preferred intervention time"""
        history = context.intervention_history[-10:]
        successful_times = [
            int.from_timestamp(i['timing']) 
            for i in history 
            if i.get('satisfaction', 0) > 0.7
        ]
        if successful_times:
            return datetime.fromtimestamp(np.mean(successful_times))
        return datetime.now() + timedelta(hours=1)

    async def run_coaching_loop(self, user_id: str):
        """Main coaching loop"""
        while True:
            try:
                metrics = await self._get_user_metrics(user_id)
                await self.update_user_context(user_id, metrics)
                
                if self._should_intervene(user_id):
                    intervention = self.generate_intervention(user_id)
                    await self._deliver_intervention(user_id, intervention)
                
                await asyncio.sleep(60)  # Check every minute
                
            except Exception as e:
                logger.error(f"Error in coaching loop: {e}")
                await asyncio.sleep(300)  # Back off on error

    def _should_intervene(self, user_id: str) -> bool:
        """Determine if intervention is appropriate"""
        context = self.user_contexts[user_id]
        last_intervention = context.intervention_history[-1] if context.intervention_history else None
        
        if not last_intervention:
            return True
            
        time_since = datetime.now() - last_intervention['timing']
        return (time_since.seconds > 3600 and  # At least 1 hour
                context.cognitive_load < 0.8 and  # Not too cognitively loaded
                context.attention_state != 'fatigued')  # Not fatigued

    async def _get_user_metrics(self, user_id: str) -> Dict[str, float]:
        """Get current user metrics"""
        # Placeholder - would integrate with actual metrics collection
        return {
            'activity_intensity': random.random(),
            'task_switching_rate': random.random(),
            'time_pressure': random.random(),
            'current_activity': 'coding'
        }

    async def _deliver_intervention(self, user_id: str, intervention: Dict):
        """Deliver coaching intervention"""
        # Placeholder - would integrate with actual delivery mechanism
        logger.info(f"Delivering intervention to {user_id}: {intervention}")

if __name__ == "__main__":
    coach = PersonalizedCoach()
    asyncio.run(coach.run_coaching_loop("test_user"))