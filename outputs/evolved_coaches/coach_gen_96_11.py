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
        return 1.0 - self._estimate_cognitive_load(context)

    def _assess_motivation(self, context: Dict) -> float:
        """Assesses current motivation level"""
        factors = {
            'recent_progress': context.get('recent_progress', 0.5),
            'goal_alignment': context.get('goal_alignment', 0.5),
            'perceived_value': context.get('perceived_value', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _assess_readiness(self, context: Dict) -> float:
        """Assesses readiness for behavioral change"""
        factors = {
            'past_success': context.get('past_success', 0.5),
            'current_capacity': context.get('current_capacity', 0.5),
            'environmental_support': context.get('environmental_support', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _select_intervention_type(self, context: Dict) -> InterventionType:
        """Selects optimal intervention type based on context"""
        cognitive_load = self._estimate_cognitive_load(context)
        motivation = self._assess_motivation(context)
        
        if cognitive_load > 0.7:
            return InterventionType.NUDGE
        elif motivation < 0.3:
            return InterventionType.CHALLENGE
        elif 0.3 <= motivation <= 0.7:
            return InterventionType.RECOMMENDATION
        else:
            return InterventionType.REFLECTION

    def _select_psychological_principle(self, context: Dict) -> PsychologicalPrinciple:
        """Selects psychological principle to apply"""
        motivation = self._assess_motivation(context)
        readiness = self._assess_readiness(context)
        
        if motivation < 0.3:
            return PsychologicalPrinciple.AUTONOMY
        elif readiness < 0.3:
            return PsychologicalPrinciple.COMPETENCE
        elif 0.3 <= motivation <= 0.7:
            return PsychologicalPrinciple.GROWTH_MINDSET
        else:
            return PsychologicalPrinciple.FLOW

    def _generate_content(self, 
                         intervention_type: InterventionType,
                         principle: PsychologicalPrinciple, 
                         context: Dict) -> Dict:
        """Generates intervention content applying psychological principles"""
        templates = self._get_content_templates(intervention_type, principle)
        selected_template = self._personalize_template(templates, context)
        
        return {
            'message': selected_template['message'],
            'rationale': selected_template['rationale'],
            'expected_outcome': selected_template['expected_outcome']
        }

    def _optimize_timing(self, context: Dict) -> Dict:
        """Optimizes intervention timing"""
        return {
            'optimal_time': self._calculate_optimal_time(context),
            'frequency': self._determine_frequency(context),
            'duration': self._determine_duration(context)
        }

    def _determine_priority(self, context: Dict) -> Priority:
        """Determines intervention priority"""
        urgency = context.get('urgency', 0.5)
        importance = context.get('importance', 0.5)
        
        priority_score = (urgency + importance) / 2
        
        if priority_score > 0.7:
            return Priority.HIGH
        elif priority_score > 0.4:
            return Priority.MEDIUM
        else:
            return Priority.LOW

    def _generate_action_steps(self, context: Dict) -> List[Dict]:
        """Generates specific, actionable steps"""
        return [
            {
                'step': f"Step {i+1}",
                'description': f"Action description {i+1}",
                'time_estimate': f"{random.randint(5,30)} minutes",
                'difficulty': random.random(),
                'resources_needed': []
            }
            for i in range(3)
        ]

    def _define_success_metrics(self, context: Dict) -> List[Dict]:
        """Defines concrete success metrics"""
        return [
            {
                'metric': 'completion_rate',
                'target': '80%',
                'measurement': 'percentage'
            },
            {
                'metric': 'satisfaction_score',
                'target': '4.0/5.0',
                'measurement': 'rating'
            }
        ]

    def _schedule_follow_up(self, context: Dict) -> Dict:
        """Schedules intervention follow-up"""
        return {
            'timing': datetime.datetime.now() + datetime.timedelta(days=1),
            'type': 'check_in',
            'metrics_to_review': ['completion_rate', 'satisfaction_score']
        }

    def update_user_model(self, feedback: Dict) -> None:
        """Updates user model based on intervention feedback"""
        self.user_preferences.update(feedback.get('preferences', {}))
        self.behavioral_patterns.update(feedback.get('behaviors', {}))