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
        """Analyzes user context to determine optimal intervention approach"""
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
            "success_metrics": self._define_success_metrics(intervention_type),
            "follow_up": self._create_follow_up_plan(intervention_type)
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
        time_of_day = context.get("time_of_day")
        recent_breaks = context.get("time_since_break", 0)
        
        attention_score = sum(focus_signals) / len(focus_signals) if focus_signals else 0.5
        attention_score *= self._time_of_day_modifier(time_of_day)
        attention_score *= max(0.2, 1 - (recent_breaks / 120))
        
        return min(1.0, max(0.1, attention_score))

    def _gauge_motivation(self, context: Dict) -> float:
        """Assesses current motivation level"""
        progress = context.get("progress", 0)
        setbacks = context.get("setbacks", 0)
        achievements = context.get("recent_achievements", [])
        
        motivation = 0.5
        motivation += 0.1 * progress
        motivation -= 0.05 * setbacks
        motivation += 0.1 * len(achievements)
        
        return min(1.0, max(0.1, motivation))

    def _select_intervention_type(self, analysis: Dict) -> InterventionType:
        """Selects most appropriate intervention type based on analysis"""
        if analysis["cognitive_load"] == CognitiveLoad.HIGH:
            return InterventionType.NUDGE
        elif analysis["motivation_level"] < 0.4:
            return InterventionType.CHALLENGE
        elif analysis["attention_capacity"] > 0.7:
            return InterventionType.RECOMMENDATION
        return InterventionType.REFLECTION

    def _select_psychological_principle(self, analysis: Dict) -> PsychologicalPrinciple:
        """Selects psychological principle to apply based on analysis"""
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
            "difficulty": selected_template["difficulty"],
            "duration": selected_template["duration"],
            "rationale": selected_template["rationale"]
        }

    def _generate_action_steps(self, intervention_type: InterventionType, 
                             analysis: Dict) -> List[Dict]:
        """Generates specific, actionable steps"""
        steps = []
        if intervention_type == InterventionType.RECOMMENDATION:
            steps = self._generate_detailed_steps(analysis)
        elif intervention_type == InterventionType.CHALLENGE:
            steps = self._generate_challenge_steps(analysis)
        else:
            steps = self._generate_quick_steps(analysis)
            
        return [self._add_step_metadata(step) for step in steps]

    def _define_success_metrics(self, intervention_type: InterventionType) -> Dict:
        """Defines concrete success metrics for the intervention"""
        return {
            "completion_criteria": self._get_completion_criteria(intervention_type),
            "progress_indicators": self._get_progress_indicators(intervention_type),
            "measurement_frequency": self._get_measurement_frequency(intervention_type)
        }

    def _create_follow_up_plan(self, intervention_type: InterventionType) -> Dict:
        """Creates follow-up schedule and check-in plan"""
        return {
            "check_points": self._generate_checkpoints(intervention_type),
            "adjustment_triggers": self._define_adjustment_triggers(),
            "reinforcement_schedule": self._create_reinforcement_schedule()
        }

    def update_user_response(self, intervention_id: str, response_data: Dict) -> None:
        """Updates user response data and adjusts future interventions"""
        self._log_response(intervention_id, response_data)
        self._update_effectiveness_metrics(response_data)
        self._adjust_intervention_parameters(response_data)
        self._update_behavioral_patterns(response_data)

    def get_intervention_effectiveness(self) -> Dict:
        """Returns effectiveness metrics for past interventions"""
        return {
            "completion_rate": self._calculate_completion_rate(),
            "behavior_change": self._measure_behavior_change(),
            "user_satisfaction": self._calculate_satisfaction(),
            "engagement_trend": self._analyze_engagement_trend()
        }