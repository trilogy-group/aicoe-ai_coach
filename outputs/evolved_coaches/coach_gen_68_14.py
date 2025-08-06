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
        self.behavioral_patterns = {}
        
    def update_context(self, user_id, context_data):
        self.cognitive_load = self._assess_cognitive_load(context_data)
        self.attention_state = self._detect_attention_state(context_data)
        self.work_context = self._analyze_work_context(context_data)
        self._update_patterns(user_id, context_data)

    def _assess_cognitive_load(self, context_data):
        # Enhanced cognitive load assessment using multiple signals
        task_complexity = context_data.get('task_complexity', 0)
        time_pressure = context_data.get('time_pressure', 0)
        interruption_frequency = context_data.get('interruptions', 0)
        return (0.4 * task_complexity + 0.3 * time_pressure + 0.3 * interruption_frequency)

class RecommendationEngine:
    def __init__(self):
        self.action_templates = {}
        self.success_metrics = {}
        self.implementation_guides = {}
        
    def generate_recommendation(self, user_profile, context):
        recommendation = {
            'action': self._select_action(context),
            'specifics': self._generate_specifics(context),
            'timeframe': self._estimate_timeframe(),
            'success_metrics': self._define_metrics(),
            'priority': self._assess_priority(context),
            'alternatives': self._generate_alternatives()
        }
        return self._personalize_recommendation(recommendation, user_profile)

    def _select_action(self, context):
        if context.cognitive_load > 0.8:
            return self.action_templates['high_load']
        elif context.attention_state == 'flow':
            return self.action_templates['protect_flow']
        return self.action_templates['default']

class BehavioralModel:
    def __init__(self):
        self.motivation_factors = {}
        self.habit_patterns = {}
        self.response_history = {}
        
    def analyze_behavior(self, user_id, behavioral_data):
        motivation = self._assess_motivation(behavioral_data)
        habit_strength = self._evaluate_habits(behavioral_data)
        response_pattern = self._analyze_responses(user_id, behavioral_data)
        
        return {
            'motivation_level': motivation,
            'habit_strength': habit_strength,
            'response_pattern': response_pattern,
            'intervention_receptivity': self._calculate_receptivity(motivation, habit_strength)
        }

    def _assess_motivation(self, data):
        autonomy = data.get('autonomy_indicators', 0)
        competence = data.get('competence_indicators', 0)
        relatedness = data.get('relatedness_indicators', 0)
        return (autonomy + competence + relatedness) / 3

class InterventionOptimizer:
    def __init__(self):
        self.timing_models = {}
        self.effectiveness_scores = {}
        self.adaptation_rules = {}
        
    def optimize_intervention(self, user_profile, context, behavioral_data):
        timing = self._optimize_timing(user_profile, context)
        intensity = self._calibrate_intensity(behavioral_data)
        format = self._select_format(user_profile, context)
        
        return {
            'optimal_time': timing,
            'intensity_level': intensity,
            'delivery_format': format,
            'customization': self._personalize_delivery(user_profile)
        }

    def _optimize_timing(self, user_profile, context):
        if context.attention_state == 'flow':
            return 'defer'
        if context.cognitive_load > 0.7:
            return 'wait_for_break'
        return 'immediate'

    def _calibrate_intensity(self, behavioral_data):
        motivation = behavioral_data['motivation_level']
        receptivity = behavioral_data['intervention_receptivity']
        return min(motivation * receptivity * 1.2, 1.0)

class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {}
        self.learning_patterns = {}
        self.response_history = {}
        self.effectiveness_metrics = {}
        
    def update_profile(self, interaction_data):
        self._update_preferences(interaction_data)
        self._update_learning_patterns(interaction_data)
        self._update_response_history(interaction_data)
        self._recalculate_effectiveness()

    def get_personalization_factors(self):
        return {
            'preferred_times': self.preferences.get('timing', []),
            'communication_style': self.preferences.get('style', 'neutral'),
            'intervention_frequency': self.preferences.get('frequency', 'medium'),
            'success_patterns': self._analyze_success_patterns()
        }