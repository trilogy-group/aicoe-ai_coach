import datetime
from typing import Dict, List, Optional
from enum import Enum
import random

class InterventionType(Enum):
    NUDGE = "nudge"
    RECOMMENDATION = "recommendation" 
    CHALLENGE = "challenge"
    REFLECTION = "reflection"

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
        
    def analyze_context(self, user_data: Dict) -> Dict:
        """Analyzes user context and current state"""
        context = {
            'cognitive_load': self._estimate_cognitive_load(user_data),
            'energy_level': self._estimate_energy_level(user_data),
            'time_of_day': datetime.datetime.now().hour,
            'recent_activity': user_data.get('recent_activity', []),
            'goals': user_data.get('goals', []),
            'preferences': self.user_preferences
        }
        return context

    def generate_intervention(self, context: Dict) -> Dict:
        """Generates personalized intervention based on context"""
        intervention_type = self._select_intervention_type(context)
        principle = self._select_psychological_principle(context)
        
        intervention = {
            'type': intervention_type,
            'principle': principle,
            'content': self._generate_content(intervention_type, principle, context),
            'priority': self._determine_priority(context),
            'timing': self._optimize_timing(context),
            'action_steps': self._generate_action_steps(context),
            'metrics': self._define_success_metrics(context),
            'alternatives': self._generate_alternatives(context),
            'follow_up': self._create_follow_up_plan(context)
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _estimate_cognitive_load(self, data: Dict) -> float:
        """Estimates current cognitive load (0-1)"""
        factors = {
            'task_complexity': data.get('task_complexity', 0.5),
            'interruptions': len(data.get('recent_interruptions', [])) * 0.1,
            'time_pressure': data.get('deadline_proximity', 0.5),
            'fatigue': 1 - data.get('energy_level', 0.5)
        }
        return min(1.0, sum(factors.values()) / len(factors))

    def _estimate_energy_level(self, data: Dict) -> float:
        """Estimates current energy level (0-1)"""
        time = datetime.datetime.now().hour
        base_energy = math.sin((time - 6) * math.pi / 12) * 0.5 + 0.5
        modifiers = {
            'sleep_quality': data.get('sleep_quality', 0.5),
            'stress_level': 1 - data.get('stress_level', 0.5),
            'exercise': data.get('exercise_today', False) * 0.2
        }
        return min(1.0, base_energy + sum(modifiers.values()) / len(modifiers))

    def _select_intervention_type(self, context: Dict) -> InterventionType:
        """Selects optimal intervention type based on context"""
        cognitive_load = context['cognitive_load']
        energy_level = context['energy_level']
        
        if cognitive_load > 0.8:
            return InterventionType.NUDGE
        elif energy_level < 0.3:
            return InterventionType.REFLECTION
        elif random.random() < 0.3:
            return InterventionType.CHALLENGE
        else:
            return InterventionType.RECOMMENDATION

    def _select_psychological_principle(self, context: Dict) -> PsychologicalPrinciple:
        """Selects psychological principle to apply"""
        recent_principles = [i['principle'] for i in self.intervention_history[-3:]]
        available = [p for p in PsychologicalPrinciple if p not in recent_principles]
        
        if not available:
            available = list(PsychologicalPrinciple)
            
        weights = {
            PsychologicalPrinciple.AUTONOMY: context.get('autonomy_need', 1.0),
            PsychologicalPrinciple.COMPETENCE: context.get('competence_need', 1.0),
            PsychologicalPrinciple.RELATEDNESS: context.get('relatedness_need', 1.0),
            PsychologicalPrinciple.FLOW: 1.0 - context['cognitive_load'],
            PsychologicalPrinciple.GROWTH_MINDSET: context.get('growth_mindset_receptivity', 1.0)
        }
        
        return random.choices(available, [weights[p] for p in available])[0]

    def _generate_content(self, type: InterventionType, principle: PsychologicalPrinciple, context: Dict) -> str:
        """Generates intervention content"""
        templates = self._get_content_templates(type, principle)
        selected = random.choice(templates)
        return self._personalize_content(selected, context)

    def _determine_priority(self, context: Dict) -> Priority:
        """Determines intervention priority"""
        urgency = context.get('urgency', 0.5)
        importance = context.get('importance', 0.5)
        score = urgency * importance
        
        if score > 0.66:
            return Priority.HIGH
        elif score > 0.33:
            return Priority.MEDIUM
        else:
            return Priority.LOW

    def _optimize_timing(self, context: Dict) -> Dict:
        """Optimizes intervention timing"""
        return {
            'optimal_time': self._calculate_optimal_time(context),
            'frequency': self._calculate_frequency(context),
            'duration': self._calculate_duration(context)
        }

    def _generate_action_steps(self, context: Dict) -> List[Dict]:
        """Generates specific action steps"""
        return [
            {
                'step': f"Step {i+1}",
                'description': f"Action description {i+1}",
                'time_estimate': f"{random.randint(5,30)} minutes",
                'difficulty': random.choice(['Easy', 'Medium', 'Hard'])
            }
            for i in range(3)
        ]

    def _define_success_metrics(self, context: Dict) -> Dict:
        """Defines concrete success metrics"""
        return {
            'quantitative': ['Metric 1', 'Metric 2'],
            'qualitative': ['Quality indicator 1', 'Quality indicator 2'],
            'timeline': '1 week'
        }

    def _generate_alternatives(self, context: Dict) -> List[Dict]:
        """Generates alternative approaches"""
        return [
            {'approach': 'Alternative 1', 'pros': ['Pro 1'], 'cons': ['Con 1']},
            {'approach': 'Alternative 2', 'pros': ['Pro 1'], 'cons': ['Con 1']}
        ]

    def _create_follow_up_plan(self, context: Dict) -> Dict:
        """Creates follow-up plan"""
        return {
            'check_points': ['+1 day', '+3 days', '+1 week'],
            'evaluation_criteria': ['Criteria 1', 'Criteria 2'],
            'adjustment_triggers': ['Trigger 1', 'Trigger 2']
        }

    def update_user_model(self, feedback: Dict):
        """Updates user model based on intervention feedback"""
        self.user_preferences.update(feedback.get('preferences', {}))
        self.behavioral_patterns.update(feedback.get('patterns', {}))