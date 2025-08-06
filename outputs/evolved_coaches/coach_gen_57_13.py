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
        self.attention_state = None
        self.work_context = None
        self.temporal_patterns = {}
        
    def update_context(self, user_id, context_data):
        self.cognitive_load = self._assess_cognitive_load(context_data)
        self.attention_state = self._detect_attention_state(context_data)
        self.work_context = self._analyze_work_context(context_data)
        self._update_temporal_patterns(user_id, context_data)

    def _assess_cognitive_load(self, context_data):
        # Enhanced cognitive load assessment using multiple signals
        task_complexity = context_data.get('task_complexity', 0)
        time_pressure = context_data.get('time_pressure', 0)
        interruption_frequency = context_data.get('interruptions', 0)
        return (0.4 * task_complexity + 0.3 * time_pressure + 
                0.3 * interruption_frequency)

class RecommendationEngine:
    def __init__(self):
        self.action_templates = self._load_action_templates()
        self.success_metrics = {}
        
    def generate_recommendation(self, user_profile, context):
        recommendation = {
            'action': self._select_action(context),
            'specifics': self._generate_specifics(user_profile),
            'time_estimate': self._estimate_time(),
            'success_metrics': self._define_metrics(),
            'priority': self._assess_priority(context),
            'alternatives': self._generate_alternatives()
        }
        return recommendation

    def _select_action(self, context):
        if context.cognitive_load > 0.7:
            return self.action_templates['high_load']
        elif context.attention_state == 'flow':
            return self.action_templates['protect_flow']
        return self.action_templates['default']

class BehavioralModel:
    def __init__(self):
        self.motivation_factors = {
            'autonomy': 0.0,
            'competence': 0.0,
            'relatedness': 0.0
        }
        self.change_readiness = 0.0
        
    def assess_motivation(self, user_data):
        self.motivation_factors['autonomy'] = self._calc_autonomy(user_data)
        self.motivation_factors['competence'] = self._calc_competence(user_data)
        self.motivation_factors['relatedness'] = self._calc_relatedness(user_data)
        return sum(self.motivation_factors.values()) / 3.0

    def generate_intervention(self, user_profile, context):
        motivation = self.assess_motivation(user_profile)
        readiness = self._assess_change_readiness(user_profile)
        return self._create_targeted_intervention(motivation, readiness)

class InterventionOptimizer:
    def __init__(self):
        self.timing_model = TimingModel()
        self.effectiveness_tracker = EffectivenessTracker()
        
    def optimize_intervention(self, recommendation, context):
        timing = self.timing_model.get_optimal_timing(context)
        intensity = self._calculate_intensity(context)
        format = self._select_format(context)
        
        optimized = {
            'timing': timing,
            'intensity': intensity,
            'format': format,
            'recommendation': recommendation
        }
        return optimized

    def track_effectiveness(self, intervention_id, metrics):
        self.effectiveness_tracker.log_outcome(intervention_id, metrics)
        self.timing_model.update(metrics)

class TimingModel:
    def __init__(self):
        self.user_patterns = {}
        self.global_patterns = {}
        
    def get_optimal_timing(self, context):
        user_timing = self._get_user_optimal_time(context)
        global_timing = self._get_global_optimal_time(context)
        return self._combine_timing_signals(user_timing, global_timing)

class EffectivenessTracker:
    def __init__(self):
        self.intervention_outcomes = {}
        
    def log_outcome(self, intervention_id, metrics):
        self.intervention_outcomes[intervention_id] = {
            'behavioral_change': metrics.get('behavioral_change', 0),
            'user_satisfaction': metrics.get('user_satisfaction', 0),
            'completion_rate': metrics.get('completion_rate', 0),
            'time_to_action': metrics.get('time_to_action', 0)
        }

    def get_effectiveness_stats(self):
        return {
            'avg_behavioral_change': self._calc_avg('behavioral_change'),
            'avg_satisfaction': self._calc_avg('user_satisfaction'),
            'avg_completion': self._calc_avg('completion_rate')
        }