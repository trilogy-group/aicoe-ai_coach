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
            'energy_level': self._estimate_energy(user_data),
            'time_of_day': datetime.datetime.now().hour,
            'recent_activity': user_data.get('recent_activity', []),
            'goals': user_data.get('goals', [])
        }
        return context

    def generate_intervention(self, context: Dict) -> Dict:
        """Generates personalized coaching intervention"""
        intervention_type = self._select_intervention_type(context)
        principle = self._select_psychological_principle(context)
        
        intervention = {
            'type': intervention_type,
            'principle': principle,
            'priority': self._determine_priority(context),
            'content': self._generate_content(intervention_type, principle, context),
            'action_steps': self._generate_action_steps(intervention_type, context),
            'metrics': self._define_success_metrics(intervention_type),
            'timing': self._optimize_timing(context),
            'alternatives': self._generate_alternatives(context)
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _estimate_cognitive_load(self, data: Dict) -> float:
        """Estimates current cognitive load (0-1)"""
        factors = {
            'task_complexity': data.get('task_complexity', 0.5),
            'interruptions': len(data.get('recent_interruptions', [])) * 0.1,
            'time_pressure': data.get('deadline_proximity', 0.5)
        }
        return min(1.0, sum(factors.values()) / len(factors))

    def _estimate_energy(self, data: Dict) -> float:
        """Estimates user energy level (0-1)"""
        factors = {
            'time_since_break': data.get('time_since_break', 0) / 120,
            'task_duration': data.get('continuous_work_time', 0) / 180,
            'reported_fatigue': data.get('fatigue_level', 0.5)
        }
        return 1.0 - (sum(factors.values()) / len(factors))

    def _select_intervention_type(self, context: Dict) -> InterventionType:
        """Selects optimal intervention type based on context"""
        cognitive_load = context['cognitive_load']
        energy = context['energy_level']
        
        if cognitive_load > 0.8:
            return InterventionType.NUDGE
        elif energy < 0.3:
            return InterventionType.REFLECTION
        elif random.random() < 0.3:
            return InterventionType.CHALLENGE
        else:
            return InterventionType.RECOMMENDATION

    def _select_psychological_principle(self, context: Dict) -> PsychologicalPrinciple:
        """Selects psychological principle to apply"""
        if context['cognitive_load'] > 0.7:
            return PsychologicalPrinciple.FLOW
        elif context['energy_level'] < 0.4:
            return PsychologicalPrinciple.COMPETENCE
        else:
            return random.choice([
                PsychologicalPrinciple.AUTONOMY,
                PsychologicalPrinciple.GROWTH_MINDSET,
                PsychologicalPrinciple.RELATEDNESS
            ])

    def _determine_priority(self, context: Dict) -> Priority:
        """Determines intervention priority"""
        urgency = context.get('deadline_proximity', 0.5)
        importance = context.get('goal_alignment', 0.5)
        
        priority_score = urgency * 0.6 + importance * 0.4
        
        if priority_score > 0.7:
            return Priority.HIGH
        elif priority_score > 0.4:
            return Priority.MEDIUM
        else:
            return Priority.LOW

    def _generate_content(self, type: InterventionType, 
                         principle: PsychologicalPrinciple,
                         context: Dict) -> str:
        """Generates intervention content"""
        templates = {
            InterventionType.NUDGE: {
                PsychologicalPrinciple.AUTONOMY: "Consider taking a moment to {action}",
                PsychologicalPrinciple.COMPETENCE: "You've made great progress. Ready to {action}?",
                PsychologicalPrinciple.FLOW: "Stay focused and {action}"
            },
            InterventionType.RECOMMENDATION: {
                PsychologicalPrinciple.GROWTH_MINDSET: "Try this new approach: {action}",
                PsychologicalPrinciple.COMPETENCE: "Based on your skills, you could {action}"
            }
        }
        
        return templates.get(type, {}).get(principle, "").format(
            action=self._get_contextual_action(context)
        )

    def _generate_action_steps(self, type: InterventionType, context: Dict) -> List[Dict]:
        """Generates specific action steps"""
        return [{
            'step': f"Step {i+1}",
            'description': f"Action description {i+1}",
            'duration': random.randint(5, 30),
            'difficulty': random.random()
        } for i in range(3)]

    def _define_success_metrics(self, type: InterventionType) -> Dict:
        """Defines measurable success metrics"""
        return {
            'completion_rate': 0.0,
            'satisfaction_score': 0.0,
            'time_to_complete': 0,
            'behavioral_change': 0.0
        }

    def _optimize_timing(self, context: Dict) -> Dict:
        """Optimizes intervention timing"""
        return {
            'best_time': datetime.datetime.now(),
            'frequency': 'daily',
            'duration': 15
        }

    def _generate_alternatives(self, context: Dict) -> List[Dict]:
        """Generates alternative recommendations"""
        return [{
            'title': f"Alternative {i+1}",
            'description': f"Alternative approach {i+1}",
            'effort_required': random.random()
        } for i in range(2)]

    def _get_contextual_action(self, context: Dict) -> str:
        """Gets context-appropriate action suggestion"""
        actions = [
            "break down this task into smaller steps",
            "review your progress",
            "try a different approach",
            "take a short break",
            "connect with a teammate"
        ]
        return random.choice(actions)

    def update_user_model(self, feedback: Dict):
        """Updates user model based on intervention feedback"""
        self.user_preferences.update(feedback.get('preferences', {}))
        self.behavioral_patterns.update(feedback.get('behaviors', {}))