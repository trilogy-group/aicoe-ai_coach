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
        self.work_context = self._analyze_work_patterns(context_data)
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
        receptivity = self._calculate_receptivity(behavior_data)
        return {
            'motivation_level': motivation,
            'habit_strength': habits,
            'intervention_receptivity': receptivity
        }

    def _assess_motivation(self, behavior_data):
        # Enhanced motivation assessment using Self-Determination Theory
        autonomy = behavior_data.get('autonomy', 0.5)
        competence = behavior_data.get('competence', 0.5)
        relatedness = behavior_data.get('relatedness', 0.5)
        return (autonomy + competence + relatedness) / 3

class RecommendationEngine:
    def __init__(self):
        self.recommendation_templates = {}
        self.success_metrics = {}
        self.adaptation_rules = {}

    def generate_recommendation(self, user_id, context, behavior):
        recommendation = {
            'action': self._select_action(context, behavior),
            'timing': self._optimize_timing(context),
            'specificity': self._add_specificity(context),
            'metrics': self._define_success_metrics(),
            'follow_up': self._create_follow_up_plan()
        }
        return self._personalize_recommendation(recommendation, user_id)

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
        self.effectiveness_metrics = {}
        self.adaptation_history = {}

    def optimize_intervention(self, user_id, context, recommendation):
        timing = self._optimize_delivery_timing(context)
        format = self._select_delivery_format(context)
        intensity = self._calibrate_intensity(context)
        
        return {
            'delivery_time': timing,
            'format': format,
            'intensity': intensity,
            'follow_up_schedule': self._create_follow_up_schedule()
        }

    def _optimize_delivery_timing(self, context):
        cognitive_load = context.cognitive_load
        attention_state = context.attention_state
        time_patterns = context.time_patterns
        
        if cognitive_load > 0.8 or attention_state == "deep_focus":
            return "defer"
        elif cognitive_load < 0.3 and attention_state == "receptive":
            return "immediate"
        else:
            return "next_break"

    def track_effectiveness(self, user_id, intervention, outcome):
        if user_id not in self.effectiveness_metrics:
            self.effectiveness_metrics[user_id] = []
        
        self.effectiveness_metrics[user_id].append({
            'intervention': intervention,
            'outcome': outcome,
            'timestamp': time.time()
        })
        
        self._update_adaptation_rules(user_id)

    def _update_adaptation_rules(self, user_id):
        recent_metrics = self.effectiveness_metrics[user_id][-10:]
        success_rate = sum(m['outcome']['success'] for m in recent_metrics) / len(recent_metrics)
        
        if success_rate < 0.5:
            self._adjust_intervention_parameters(user_id)