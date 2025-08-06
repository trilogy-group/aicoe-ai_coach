class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.context_tracker = ContextTracker()
        self.recommendation_engine = RecommendationEngine()
        self.behavioral_model = BehavioralModel()
        self.intervention_optimizer = InterventionOptimizer()

class ContextTracker:
    def __init__(self):
        self.cognitive_load = 0.0
        self.attention_state = "focused"
        self.time_patterns = {}
        self.work_context = {}
        
    def update_context(self, user_id, context_data):
        self.cognitive_load = self._assess_cognitive_load(context_data)
        self.attention_state = self._detect_attention_state(context_data)
        self.work_context = self._analyze_work_context(context_data)
        self._update_time_patterns(user_id, context_data)

    def _assess_cognitive_load(self, context_data):
        # Enhanced cognitive load assessment using multiple signals
        task_complexity = context_data.get('task_complexity', 0.5)
        time_pressure = context_data.get('time_pressure', 0.5) 
        interruption_frequency = context_data.get('interruptions', 0.3)
        return (task_complexity + time_pressure + interruption_frequency) / 3

class BehavioralModel:
    def __init__(self):
        self.motivation_factors = {}
        self.habit_patterns = {}
        self.response_history = {}
        
    def analyze_behavior(self, user_id, behavior_data):
        motivation = self._assess_motivation(behavior_data)
        habits = self._identify_habits(behavior_data)
        responsiveness = self._calculate_responsiveness(user_id, behavior_data)
        return {
            'motivation_level': motivation,
            'key_habits': habits,
            'intervention_responsiveness': responsiveness
        }

    def _assess_motivation(self, behavior_data):
        # Enhanced motivation assessment using Self-Determination Theory
        autonomy = behavior_data.get('autonomy_indicators', 0.5)
        competence = behavior_data.get('competence_indicators', 0.5)
        relatedness = behavior_data.get('relatedness_indicators', 0.5)
        return (autonomy + competence + relatedness) / 3

class RecommendationEngine:
    def __init__(self):
        self.recommendation_templates = {}
        self.success_metrics = {}
        self.adaptation_rules = {}

    def generate_recommendation(self, user_id, context, behavior):
        recommendation = {
            'action': self._select_action(context, behavior),
            'specifics': self._generate_specifics(context),
            'timeframe': self._suggest_timeframe(context),
            'success_metrics': self._define_metrics(context),
            'priority': self._assign_priority(context),
            'alternatives': self._generate_alternatives(context)
        }
        return self._personalize_recommendation(user_id, recommendation)

    def _select_action(self, context, behavior):
        if context.cognitive_load > 0.7:
            return self._generate_low_effort_action()
        elif behavior['motivation_level'] < 0.3:
            return self._generate_motivation_focused_action()
        else:
            return self._generate_standard_action()

class InterventionOptimizer:
    def __init__(self):
        self.timing_model = {}
        self.effectiveness_scores = {}
        self.adaptation_history = {}

    def optimize_intervention(self, user_id, context, recommendation):
        timing = self._optimize_timing(user_id, context)
        format = self._optimize_format(user_id, context)
        intensity = self._calibrate_intensity(user_id, context)
        
        return {
            'timing': timing,
            'format': format,
            'intensity': intensity,
            'recommendation': recommendation
        }

    def _optimize_timing(self, user_id, context):
        cognitive_load = context.cognitive_load
        attention_state = context.attention_state
        time_patterns = context.time_patterns.get(user_id, {})
        
        if cognitive_load > 0.8 or attention_state == "deep_focus":
            return "defer"
        elif cognitive_load < 0.3 and attention_state == "receptive":
            return "immediate"
        else:
            return "next_break"

    def track_effectiveness(self, user_id, intervention, outcome):
        if user_id not in self.effectiveness_scores:
            self.effectiveness_scores[user_id] = []
        
        score = self._calculate_effectiveness(intervention, outcome)
        self.effectiveness_scores[user_id].append(score)
        self._update_adaptation_rules(user_id, score)

    def _calculate_effectiveness(self, intervention, outcome):
        relevance = outcome.get('relevance', 0.0)
        action_taken = outcome.get('action_taken', 0.0)
        satisfaction = outcome.get('satisfaction', 0.0)
        return (relevance + action_taken + satisfaction) / 3