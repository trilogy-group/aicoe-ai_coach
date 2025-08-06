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

class CognitiveLoad(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class AICoach:
    def __init__(self):
        self.user_context = {}
        self.intervention_history = []
        self.user_preferences = {}
        self.behavioral_patterns = {}
        
    def analyze_user_context(self, context_data: Dict) -> Dict:
        """Analyzes user context to determine optimal intervention strategy"""
        cognitive_load = self._assess_cognitive_load(context_data)
        attention_capacity = self._evaluate_attention(context_data)
        motivation_level = self._gauge_motivation(context_data)
        
        return {
            "cognitive_load": cognitive_load,
            "attention_capacity": attention_capacity,
            "motivation_level": motivation_level,
            "optimal_timing": self._determine_timing(context_data),
            "receptivity": self._assess_receptivity(context_data)
        }

    def generate_intervention(self, context: Dict) -> Dict:
        """Generates personalized intervention based on user context"""
        analysis = self.analyze_user_context(context)
        
        intervention_type = self._select_intervention_type(analysis)
        psychological_principle = self._select_psychological_principle(analysis)
        
        intervention = {
            "type": intervention_type,
            "principle": psychological_principle,
            "content": self._generate_content(intervention_type, psychological_principle, analysis),
            "timing": analysis["optimal_timing"],
            "action_steps": self._generate_action_steps(intervention_type, analysis),
            "success_metrics": self._define_success_metrics(),
            "follow_up": self._schedule_follow_up(analysis)
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _assess_cognitive_load(self, context: Dict) -> CognitiveLoad:
        """Evaluates current cognitive load based on context signals"""
        task_complexity = context.get("task_complexity", 0)
        time_pressure = context.get("time_pressure", 0)
        distractions = context.get("distractions", 0)
        
        load_score = task_complexity + time_pressure + distractions
        
        if load_score < 3:
            return CognitiveLoad.LOW
        elif load_score < 6:
            return CognitiveLoad.MEDIUM
        return CognitiveLoad.HIGH

    def _evaluate_attention(self, context: Dict) -> float:
        """Estimates current attention capacity"""
        focus_signals = context.get("focus_signals", [])
        time_on_task = context.get("time_on_task", 0)
        breaks_taken = context.get("breaks_taken", 0)
        
        attention_score = sum(focus_signals) / len(focus_signals) if focus_signals else 0.5
        attention_score *= max(0, 1 - (time_on_task / 120))  # Decay after 2 hours
        attention_score += min(0.2, breaks_taken * 0.05)  # Bonus for taking breaks
        
        return min(1.0, attention_score)

    def _gauge_motivation(self, context: Dict) -> float:
        """Assesses current motivation level"""
        progress = context.get("progress", 0)
        setbacks = context.get("setbacks", 0)
        achievements = context.get("achievements", 0)
        
        motivation = 0.5  # Baseline
        motivation += progress * 0.2
        motivation -= setbacks * 0.1
        motivation += achievements * 0.15
        
        return max(0.1, min(1.0, motivation))

    def _select_intervention_type(self, analysis: Dict) -> InterventionType:
        """Selects most appropriate intervention type based on analysis"""
        if analysis["cognitive_load"] == CognitiveLoad.HIGH:
            return InterventionType.NUDGE
        elif analysis["motivation_level"] < 0.4:
            return InterventionType.CHALLENGE
        elif analysis["attention_capacity"] < 0.3:
            return InterventionType.REFLECTION
        return InterventionType.RECOMMENDATION

    def _select_psychological_principle(self, analysis: Dict) -> PsychologicalPrinciple:
        """Selects psychological principle to apply"""
        if analysis["motivation_level"] < 0.4:
            return PsychologicalPrinciple.AUTONOMY
        elif analysis["cognitive_load"] == CognitiveLoad.HIGH:
            return PsychologicalPrinciple.FLOW
        return random.choice([
            PsychologicalPrinciple.COMPETENCE,
            PsychologicalPrinciple.GROWTH_MINDSET,
            PsychologicalPrinciple.RELATEDNESS
        ])

    def _generate_content(self, intervention_type: InterventionType, 
                         principle: PsychologicalPrinciple, 
                         analysis: Dict) -> Dict:
        """Generates intervention content applying psychological principles"""
        templates = self._get_content_templates(intervention_type, principle)
        selected_template = self._personalize_template(
            random.choice(templates),
            analysis
        )
        
        return {
            "message": selected_template["message"],
            "rationale": selected_template["rationale"],
            "difficulty": self._adjust_difficulty(analysis),
            "estimated_time": selected_template["time_estimate"],
            "alternatives": selected_template["alternatives"]
        }

    def _generate_action_steps(self, intervention_type: InterventionType, 
                             analysis: Dict) -> List[Dict]:
        """Generates specific, actionable steps"""
        return [
            {
                "step": f"Step {i+1}",
                "description": f"Action description {i+1}",
                "time_estimate": f"{random.randint(5,30)} minutes",
                "priority": "High" if i == 0 else "Medium",
                "completion_criteria": f"Completion criteria {i+1}"
            }
            for i in range(3)
        ]

    def _define_success_metrics(self) -> Dict:
        """Defines measurable success metrics"""
        return {
            "completion_rate": "100%",
            "time_to_completion": "Within estimated time",
            "quality_threshold": "Meets all criteria",
            "feedback_score": ">=4/5"
        }

    def _schedule_follow_up(self, analysis: Dict) -> Dict:
        """Schedules appropriate follow-up checks"""
        return {
            "timing": datetime.datetime.now() + datetime.timedelta(hours=24),
            "type": "check_in",
            "metrics_to_review": ["progress", "obstacles", "satisfaction"]
        }

    def update_user_model(self, feedback: Dict) -> None:
        """Updates user model based on intervention feedback"""
        self.user_preferences.update(feedback.get("preferences", {}))
        self.behavioral_patterns.update(feedback.get("behaviors", {}))