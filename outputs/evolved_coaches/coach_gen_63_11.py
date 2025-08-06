import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
import random

@dataclass
class UserContext:
    user_id: str
    current_activity: str
    energy_level: float 
    stress_level: float
    time_of_day: datetime.time
    recent_interactions: List[str]
    response_history: Dict[str, float]
    goals: List[str]
    preferences: Dict[str, any]

class AICoach:
    def __init__(self):
        self.behavioral_models = {
            'motivation': ['autonomy', 'competence', 'relatedness'],
            'stages_of_change': ['precontemplation', 'contemplation', 'preparation', 'action', 'maintenance'],
            'cognitive_load': ['intrinsic', 'extraneous', 'germane']
        }
        
        self.intervention_types = {
            'micro_nudge': {'duration': 1, 'cognitive_load': 0.2},
            'quick_tip': {'duration': 2, 'cognitive_load': 0.3},
            'mini_exercise': {'duration': 5, 'cognitive_load': 0.5},
            'detailed_guidance': {'duration': 10, 'cognitive_load': 0.8}
        }

    def generate_coaching_intervention(self, user_context: UserContext) -> Dict:
        # Analyze context and select optimal intervention
        intervention_type = self._select_intervention_type(user_context)
        behavioral_model = self._select_behavioral_model(user_context)
        
        # Generate personalized content
        content = self._generate_content(user_context, intervention_type, behavioral_model)
        
        # Add actionability components
        action_steps = self._create_action_steps(content, user_context)
        success_metrics = self._define_success_metrics(content)
        follow_up = self._schedule_follow_up(user_context)

        return {
            'type': intervention_type,
            'content': content,
            'action_steps': action_steps,
            'metrics': success_metrics,
            'follow_up': follow_up,
            'cognitive_load': self.intervention_types[intervention_type]['cognitive_load'],
            'estimated_duration': self.intervention_types[intervention_type]['duration']
        }

    def _select_intervention_type(self, context: UserContext) -> str:
        # Consider energy, stress, time available
        available_cognitive_capacity = 1.0 - (context.stress_level * 0.5)
        available_cognitive_capacity *= context.energy_level

        # Select intervention that fits available capacity
        suitable_types = [
            t for t, props in self.intervention_types.items() 
            if props['cognitive_load'] <= available_cognitive_capacity
        ]
        
        return random.choice(suitable_types) if suitable_types else 'micro_nudge'

    def _select_behavioral_model(self, context: UserContext) -> str:
        # Analyze user history and current state
        response_effectiveness = self._analyze_response_history(context.response_history)
        current_stage = self._determine_stage_of_change(context)
        
        # Select most appropriate model
        if current_stage in ['precontemplation', 'contemplation']:
            return 'motivation'
        elif context.stress_level > 0.7:
            return 'cognitive_load'
        else:
            return 'stages_of_change'

    def _generate_content(self, context: UserContext, 
                         intervention_type: str, 
                         behavioral_model: str) -> str:
        # Template-based content generation with personalization
        templates = self._get_content_templates(intervention_type, behavioral_model)
        selected_template = self._select_best_template(templates, context)
        
        # Personalize content
        personalized = self._personalize_content(selected_template, context)
        
        return personalized

    def _create_action_steps(self, content: str, context: UserContext) -> List[Dict]:
        # Generate specific, measurable steps
        steps = []
        
        # Break down into smaller achievable actions
        sub_tasks = self._break_down_task(content)
        
        for i, task in enumerate(sub_tasks):
            steps.append({
                'step_number': i + 1,
                'description': task,
                'estimated_duration': self._estimate_duration(task),
                'difficulty': self._assess_difficulty(task, context),
                'prerequisites': self._identify_prerequisites(task),
                'verification': self._create_verification_method(task)
            })
            
        return steps

    def _define_success_metrics(self, content: str) -> Dict:
        return {
            'completion': {'type': 'boolean', 'target': True},
            'time_spent': {'type': 'duration', 'target': 'estimated_duration'},
            'perceived_value': {'type': 'scale', 'range': [1,5], 'target': 4},
            'implementation_success': {'type': 'scale', 'range': [1,5], 'target': 4}
        }

    def _schedule_follow_up(self, context: UserContext) -> Dict:
        # Schedule based on user patterns and intervention type
        optimal_time = self._calculate_optimal_time(context)
        
        return {
            'time': optimal_time,
            'type': 'check_in',
            'duration': 2,
            'method': 'notification'
        }

    def _analyze_response_history(self, history: Dict[str, float]) -> float:
        if not history:
            return 0.5
        return sum(history.values()) / len(history)

    def _determine_stage_of_change(self, context: UserContext) -> str:
        # Analyze user behavior patterns
        recent_actions = len([g for g in context.goals if g in context.recent_interactions])
        if recent_actions == 0:
            return 'precontemplation'
        elif recent_actions < 2:
            return 'contemplation'
        else:
            return 'action'

    def _calculate_optimal_time(self, context: UserContext) -> datetime.time:
        # Consider user's typical active hours and energy patterns
        current_time = context.time_of_day
        hours_offset = 2 if context.energy_level > 0.7 else 4
        
        return (datetime.datetime.combine(datetime.date.today(), current_time) + 
                datetime.timedelta(hours=hours_offset)).time()

    def update_user_model(self, user_context: UserContext, 
                         intervention_result: Dict) -> UserContext:
        # Update user model based on intervention results
        user_context.response_history[intervention_result['type']] = intervention_result['success_rate']
        user_context.recent_interactions.append(intervention_result['type'])
        
        return user_context