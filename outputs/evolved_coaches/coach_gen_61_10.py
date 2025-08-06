import datetime
from typing import Dict, List, Optional
from enum import Enum
import random

class InterventionType(Enum):
    NUDGE = "nudge"
    RECOMMENDATION = "recommendation" 
    REFLECTION = "reflection"
    CHALLENGE = "challenge"

class PsychologicalPrinciple(Enum):
    AUTONOMY = "autonomy"
    COMPETENCE = "competence"
    RELATEDNESS = "relatedness"
    FLOW = "flow"
    GROWTH_MINDSET = "growth_mindset"

class Priority(Enum):
    HIGH = 3
    MEDIUM = 2 
    LOW = 1

class AICoach:
    def __init__(self):
        self.user_context = {}
        self.intervention_history = []
        self.user_preferences = {}
        self.behavioral_patterns = {}
        
    def analyze_user_context(self, context_data: Dict) -> Dict:
        """Analyzes user context to determine optimal intervention strategy"""
        analyzed_context = {
            'cognitive_load': self._estimate_cognitive_load(context_data),
            'attention_capacity': self._estimate_attention_capacity(context_data),
            'motivation_level': self._assess_motivation(context_data),
            'readiness_for_change': self._assess_readiness(context_data),
            'optimal_intervention_type': self._determine_intervention_type(context_data)
        }
        return analyzed_context

    def generate_intervention(self, context: Dict) -> Dict:
        """Generates personalized intervention based on user context"""
        intervention_type = self._select_intervention_type(context)
        psychological_principle = self._select_psychological_principle(context)
        
        intervention = {
            'type': intervention_type,
            'principle': psychological_principle,
            'content': self._generate_content(intervention_type, psychological_principle, context),
            'timing': self._optimize_timing(context),
            'priority': self._determine_priority(context),
            'action_steps': self._generate_action_steps(context),
            'success_metrics': self._define_success_metrics(context),
            'follow_up': self._schedule_follow_up(context)
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _estimate_cognitive_load(self, context: Dict) -> float:
        """Estimates current cognitive load based on context factors"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'distractions': context.get('distractions', 0.5),
            'fatigue': context.get('fatigue', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_attention_capacity(self, context: Dict) -> float:
        """Estimates available attention capacity"""
        time_of_day = datetime.datetime.now().hour
        energy_level = context.get('energy_level', 0.5)
        recent_breaks = context.get('time_since_break', 60)
        
        capacity = energy_level * (1 - (recent_breaks / 240))
        return max(0.1, min(capacity, 1.0))

    def _assess_motivation(self, context: Dict) -> float:
        """Assesses current motivation level"""
        factors = {
            'goal_progress': context.get('goal_progress', 0.5),
            'recent_successes': context.get('recent_successes', 0.5),
            'social_support': context.get('social_support', 0.5),
            'intrinsic_motivation': context.get('intrinsic_motivation', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _assess_readiness(self, context: Dict) -> float:
        """Assesses readiness for behavioral change"""
        stages = {
            'precontemplation': 0.2,
            'contemplation': 0.4,
            'preparation': 0.6,
            'action': 0.8,
            'maintenance': 1.0
        }
        current_stage = context.get('change_stage', 'contemplation')
        return stages[current_stage]

    def _select_intervention_type(self, context: Dict) -> InterventionType:
        """Selects optimal intervention type based on context"""
        cognitive_load = self._estimate_cognitive_load(context)
        attention = self._estimate_attention_capacity(context)
        
        if cognitive_load > 0.8:
            return InterventionType.NUDGE
        elif attention < 0.3:
            return InterventionType.NUDGE
        elif context.get('goal_progress', 0) > 0.7:
            return InterventionType.REFLECTION
        else:
            return InterventionType.RECOMMENDATION

    def _select_psychological_principle(self, context: Dict) -> PsychologicalPrinciple:
        """Selects psychological principle to apply"""
        motivation = self._assess_motivation(context)
        readiness = self._assess_readiness(context)
        
        if motivation < 0.3:
            return PsychologicalPrinciple.AUTONOMY
        elif readiness < 0.5:
            return PsychologicalPrinciple.GROWTH_MINDSET
        else:
            return PsychologicalPrinciple.FLOW

    def _generate_content(self, intervention_type: InterventionType, 
                         principle: PsychologicalPrinciple, context: Dict) -> str:
        """Generates intervention content applying psychological principles"""
        templates = self._get_content_templates(intervention_type, principle)
        selected_template = random.choice(templates)
        return self._personalize_content(selected_template, context)

    def _optimize_timing(self, context: Dict) -> Dict:
        """Optimizes intervention timing"""
        return {
            'optimal_time': self._calculate_optimal_time(context),
            'frequency': self._calculate_frequency(context),
            'duration': self._calculate_duration(context)
        }

    def _generate_action_steps(self, context: Dict) -> List[Dict]:
        """Generates specific, measurable action steps"""
        return [
            {
                'step': 'Specific action description',
                'time_estimate': '10 mins',
                'difficulty': 'medium',
                'resources_needed': ['resource1', 'resource2'],
                'completion_criteria': 'Measurable outcome'
            }
        ]

    def _define_success_metrics(self, context: Dict) -> Dict:
        """Defines concrete success metrics"""
        return {
            'behavioral_indicators': ['indicator1', 'indicator2'],
            'measurement_method': 'method description',
            'target_values': {'metric1': 'value1'},
            'timeline': 'timeline description'
        }

    def _schedule_follow_up(self, context: Dict) -> Dict:
        """Schedules follow-up checks"""
        return {
            'timing': 'follow up timing',
            'method': 'follow up method',
            'assessment_criteria': ['criteria1', 'criteria2']
        }

    def update_user_model(self, feedback: Dict) -> None:
        """Updates user model based on intervention feedback"""
        self.user_preferences.update(feedback.get('preferences', {}))
        self.behavioral_patterns.update(feedback.get('patterns', {}))