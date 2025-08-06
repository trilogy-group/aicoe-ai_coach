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
            'recent_progress': self._analyze_progress(user_data),
            'current_challenges': self._identify_challenges(user_data)
        }
        return context

    def generate_intervention(self, context: Dict) -> Dict:
        """Generates personalized coaching intervention"""
        
        # Select optimal intervention type based on context
        intervention_type = self._select_intervention_type(context)
        
        # Choose psychological principles to apply
        principles = self._select_psychological_principles(context)
        
        # Generate specific content
        content = self._generate_content(intervention_type, principles, context)
        
        # Add actionability components
        action_steps = self._create_action_steps(content, context)
        metrics = self._define_success_metrics(content)
        
        intervention = {
            'type': intervention_type,
            'principles': principles,
            'content': content,
            'action_steps': action_steps,
            'metrics': metrics,
            'priority': self._assign_priority(context),
            'timing': self._optimize_timing(context),
            'difficulty': self._adapt_difficulty(context)
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _estimate_cognitive_load(self, data: Dict) -> float:
        """Estimates current cognitive load (0-1)"""
        factors = [
            data.get('task_complexity', 0.5),
            data.get('multitasking_level', 0.5),
            data.get('time_pressure', 0.5),
            data.get('interruption_frequency', 0.5)
        ]
        return sum(factors) / len(factors)

    def _estimate_energy(self, data: Dict) -> float:
        """Estimates energy level (0-1)"""
        factors = [
            data.get('hours_slept', 7) / 9,
            1 - (data.get('stress_level', 0.5)),
            data.get('motivation', 0.5)
        ]
        return sum(factors) / len(factors)

    def _analyze_progress(self, data: Dict) -> Dict:
        """Analyzes recent progress and patterns"""
        return {
            'completion_rate': data.get('task_completion_rate', 0.0),
            'consistency': data.get('habit_consistency', 0.0),
            'improvement': data.get('skill_improvement', 0.0)
        }

    def _identify_challenges(self, data: Dict) -> List[str]:
        """Identifies current challenges"""
        challenges = []
        thresholds = {
            'task_completion_rate': 0.7,
            'habit_consistency': 0.8,
            'focus_duration': 45
        }
        
        for metric, threshold in thresholds.items():
            if data.get(metric, 0) < threshold:
                challenges.append(metric)
        
        return challenges

    def _select_intervention_type(self, context: Dict) -> InterventionType:
        """Selects optimal intervention type based on context"""
        cognitive_load = context['cognitive_load']
        energy = context['energy_level']
        
        if cognitive_load > 0.8:
            return InterventionType.NUDGE
        elif energy < 0.3:
            return InterventionType.REFLECTION
        elif context['recent_progress']['improvement'] < 0.5:
            return InterventionType.CHALLENGE
        else:
            return InterventionType.RECOMMENDATION

    def _select_psychological_principles(self, context: Dict) -> List[PsychologicalPrinciple]:
        """Selects relevant psychological principles"""
        principles = []
        
        if context['cognitive_load'] < 0.7:
            principles.append(PsychologicalPrinciple.FLOW)
        
        if context['recent_progress']['improvement'] < 0.3:
            principles.append(PsychologicalPrinciple.GROWTH_MINDSET)
            
        if len(context['current_challenges']) > 2:
            principles.append(PsychologicalPrinciple.COMPETENCE)
            
        if random.random() < 0.3:
            principles.append(PsychologicalPrinciple.AUTONOMY)
            
        return principles[:2]  # Limit to 2 principles

    def _generate_content(self, type: InterventionType, 
                         principles: List[PsychologicalPrinciple],
                         context: Dict) -> str:
        """Generates intervention content"""
        templates = {
            InterventionType.NUDGE: [
                "Quick win: Take 2 minutes to {action}",
                "Remember: {principle} leads to {benefit}"
            ],
            InterventionType.RECOMMENDATION: [
                "To improve {area}, try: {specific_action}",
                "Research shows {evidence} leads to {outcome}"
            ],
            InterventionType.CHALLENGE: [
                "Ready to level up? Complete {challenge} today",
                "Push your limits: {stretch_goal}"
            ],
            InterventionType.REFLECTION: [
                "Reflect: What made {success} possible today?",
                "Consider: How could {challenge} become easier?"
            ]
        }
        
        template = random.choice(templates[type])
        # Additional logic to fill template based on context
        return template

    def _create_action_steps(self, content: str, context: Dict) -> List[Dict]:
        """Creates specific action steps"""
        steps = []
        # Generate 2-3 concrete action steps based on content and context
        return steps

    def _define_success_metrics(self, content: str) -> Dict:
        """Defines measurable success metrics"""
        return {
            'completion': 'Binary yes/no',
            'quality': 'Scale 1-5',
            'time_spent': 'Minutes',
            'difficulty': 'Scale 1-5'
        }

    def _assign_priority(self, context: Dict) -> Priority:
        """Assigns priority level"""
        if context['cognitive_load'] > 0.8:
            return Priority.LOW
        elif len(context['current_challenges']) > 2:
            return Priority.HIGH
        else:
            return Priority.MEDIUM

    def _optimize_timing(self, context: Dict) -> Dict:
        """Optimizes intervention timing"""
        return {
            'best_time': self._calculate_optimal_time(context),
            'frequency': self._calculate_frequency(context),
            'duration': self._calculate_duration(context)
        }

    def _adapt_difficulty(self, context: Dict) -> float:
        """Adapts intervention difficulty (0-1)"""
        base_difficulty = 0.5
        modifiers = {
            'energy': context['energy_level'] * 0.2,
            'cognitive_load': -context['cognitive_load'] * 0.2,
            'progress': context['recent_progress']['improvement'] * 0.1
        }
        return min(1.0, max(0.1, base_difficulty + sum(modifiers.values())))

    def update_user_model(self, feedback: Dict):
        """Updates user model based on intervention feedback"""
        self.user_preferences.update(feedback.get('preferences', {}))
        self.behavioral_patterns.update(feedback.get('patterns', {}))