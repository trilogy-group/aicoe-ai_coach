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
        self.success_metrics = {}
        
    def analyze_user_context(self, context_data: Dict) -> Dict:
        """Analyzes user context to determine optimal intervention strategy"""
        current_state = {
            "cognitive_load": self._estimate_cognitive_load(context_data),
            "energy_level": self._estimate_energy_level(context_data),
            "motivation": self._assess_motivation(context_data),
            "progress": self._evaluate_progress(context_data)
        }
        self.user_context.update(current_state)
        return current_state

    def generate_intervention(self, context: Dict) -> Dict:
        """Generates personalized intervention based on user context"""
        intervention_type = self._select_intervention_type(context)
        principle = self._select_psychological_principle(context)
        
        intervention = {
            "type": intervention_type,
            "principle": principle,
            "content": self._generate_content(intervention_type, principle, context),
            "timing": self._optimize_timing(context),
            "priority": self._determine_priority(context),
            "action_steps": self._create_action_steps(context),
            "success_metrics": self._define_success_metrics(context),
            "follow_up": self._schedule_follow_up(context)
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _estimate_cognitive_load(self, context: Dict) -> float:
        """Estimates current cognitive load based on context signals"""
        factors = {
            "task_complexity": context.get("task_complexity", 0.5),
            "time_pressure": context.get("time_pressure", 0.5),
            "interruptions": context.get("interruptions", 0.5),
            "multitasking": context.get("multitasking", 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_energy_level(self, context: Dict) -> float:
        """Estimates user energy level based on context signals"""
        time_of_day = datetime.datetime.now().hour
        activity_level = context.get("activity_level", 0.5)
        recent_breaks = context.get("breaks_taken", 0)
        
        energy = (
            (24 - abs(14 - time_of_day)) / 24 * 0.4 +
            activity_level * 0.4 +
            min(recent_breaks / 3, 1.0) * 0.2
        )
        return energy

    def _assess_motivation(self, context: Dict) -> float:
        """Assesses current motivation level"""
        factors = {
            "goal_progress": context.get("goal_progress", 0.5),
            "recent_wins": context.get("recent_wins", 0.5),
            "task_alignment": context.get("task_alignment", 0.5),
            "social_support": context.get("social_support", 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _evaluate_progress(self, context: Dict) -> float:
        """Evaluates progress toward goals"""
        return context.get("progress", 0.5)

    def _select_intervention_type(self, context: Dict) -> InterventionType:
        """Selects optimal intervention type based on context"""
        cognitive_load = self._estimate_cognitive_load(context)
        motivation = self._assess_motivation(context)
        
        if cognitive_load > 0.7:
            return InterventionType.NUDGE
        elif motivation < 0.3:
            return InterventionType.CHALLENGE
        elif context.get("reflection_opportunity", False):
            return InterventionType.REFLECTION
        else:
            return InterventionType.RECOMMENDATION

    def _select_psychological_principle(self, context: Dict) -> PsychologicalPrinciple:
        """Selects psychological principle to apply"""
        motivation = self._assess_motivation(context)
        progress = self._evaluate_progress(context)
        
        if motivation < 0.3:
            return PsychologicalPrinciple.AUTONOMY
        elif progress < 0.3:
            return PsychologicalPrinciple.COMPETENCE
        elif context.get("social_context", False):
            return PsychologicalPrinciple.RELATEDNESS
        elif 0.3 <= progress <= 0.7:
            return PsychologicalPrinciple.FLOW
        else:
            return PsychologicalPrinciple.GROWTH_MINDSET

    def _generate_content(self, 
                         intervention_type: InterventionType,
                         principle: PsychologicalPrinciple, 
                         context: Dict) -> str:
        """Generates intervention content applying psychological principles"""
        templates = {
            InterventionType.NUDGE: {
                PsychologicalPrinciple.AUTONOMY: "Consider taking a moment to {action}",
                PsychologicalPrinciple.COMPETENCE: "You've mastered {skill} before - apply that here",
                PsychologicalPrinciple.RELATEDNESS: "Others found success by {strategy}",
                PsychologicalPrinciple.FLOW: "Focus fully on {task} for the next 25 minutes",
                PsychologicalPrinciple.GROWTH_MINDSET: "View this challenge as an opportunity to grow"
            }
        }
        
        template = templates[intervention_type][principle]
        return template.format(**context)

    def _optimize_timing(self, context: Dict) -> datetime.datetime:
        """Optimizes intervention timing"""
        now = datetime.datetime.now()
        cognitive_load = self._estimate_cognitive_load(context)
        energy = self._estimate_energy_level(context)
        
        if cognitive_load > 0.7 or energy < 0.3:
            delay = datetime.timedelta(minutes=30)
        else:
            delay = datetime.timedelta(minutes=5)
            
        return now + delay

    def _determine_priority(self, context: Dict) -> Priority:
        """Determines intervention priority"""
        urgency = context.get("urgency", 0.5)
        importance = context.get("importance", 0.5)
        
        priority_score = urgency * 0.6 + importance * 0.4
        
        if priority_score > 0.7:
            return Priority.HIGH
        elif priority_score > 0.4:
            return Priority.MEDIUM
        else:
            return Priority.LOW

    def _create_action_steps(self, context: Dict) -> List[Dict]:
        """Creates specific action steps"""
        return [
            {
                "step": 1,
                "action": "Define specific goal",
                "time_estimate": "5 min",
                "difficulty": "easy"
            },
            {
                "step": 2, 
                "action": "Break down into subtasks",
                "time_estimate": "10 min",
                "difficulty": "medium"
            },
            {
                "step": 3,
                "action": "Complete first subtask",
                "time_estimate": "15 min", 
                "difficulty": "medium"
            }
        ]

    def _define_success_metrics(self, context: Dict) -> Dict:
        """Defines metrics to measure intervention success"""
        return {
            "completion": "Task completed yes/no",
            "time_spent": "Time to completion",
            "quality": "Self-rated quality 1-5",
            "satisfaction": "Self-rated satisfaction 1-5"
        }

    def _schedule_follow_up(self, context: Dict) -> datetime.datetime:
        """Schedules intervention follow-up"""
        now = datetime.datetime.now()
        return now + datetime.timedelta(hours=24)

    def update_user_model(self, feedback: Dict) -> None:
        """Updates user model based on intervention feedback"""
        self.user_preferences.update(feedback.get("preferences", {}))
        self.behavioral_patterns.update(feedback.get("behaviors", {}))
        self.success_metrics.update(feedback.get("metrics", {}))