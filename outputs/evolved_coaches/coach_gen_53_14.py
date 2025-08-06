class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.context_tracker = ContextTracker()
        self.recommendation_engine = RecommendationEngine()
        self.behavioral_model = BehavioralModel()
        self.intervention_manager = InterventionManager()

class ContextTracker:
    def __init__(self):
        self.cognitive_load = 0.0
        self.attention_state = None
        self.time_patterns = {}
        self.work_context = None
        
    def update_context(self, user_id, context_data):
        self.cognitive_load = self._assess_cognitive_load(context_data)
        self.attention_state = self._detect_attention_state(context_data)
        self.work_context = self._analyze_work_context(context_data)
        self._update_time_patterns(user_id, context_data)

    def is_good_intervention_time(self, user_id):
        return (self.cognitive_load < 0.7 and 
                self.attention_state != "flow" and
                self._check_time_patterns(user_id))

class BehavioralModel:
    def __init__(self):
        self.motivation_factors = {
            "autonomy": 0.0,
            "competence": 0.0,
            "relatedness": 0.0
        }
        self.change_readiness = 0.0
        self.response_history = {}

    def assess_user_state(self, user_id, behavior_data):
        self._update_motivation_factors(behavior_data)
        self.change_readiness = self._calculate_readiness(user_id)
        self._track_response_patterns(user_id, behavior_data)

    def get_optimal_approach(self, user_id):
        return {
            "motivation_type": self._determine_motivation_type(),
            "intensity_level": self._calculate_intensity(),
            "framing_style": self._select_framing_style(user_id)
        }

class RecommendationEngine:
    def __init__(self):
        self.action_templates = self._load_action_templates()
        self.success_metrics = {}
        self.difficulty_levels = {}

    def generate_recommendation(self, user_id, context, behavioral_model):
        base_action = self._select_base_action(context)
        personalized_action = self._personalize_action(
            base_action, 
            user_id,
            behavioral_model
        )
        return self._enhance_actionability(personalized_action)

    def _enhance_actionability(self, action):
        return {
            "steps": self._break_into_steps(action),
            "time_estimate": self._estimate_time(action),
            "success_metrics": self._define_metrics(action),
            "difficulty": self._assess_difficulty(action),
            "alternatives": self._generate_alternatives(action)
        }

class InterventionManager:
    def __init__(self):
        self.intervention_history = {}
        self.effectiveness_metrics = {}
        self.frequency_controller = FrequencyController()

    def create_intervention(self, user_id, context, behavioral_model):
        if not self._should_intervene(user_id, context):
            return None

        recommendation = self.recommendation_engine.generate_recommendation(
            user_id, 
            context,
            behavioral_model
        )

        return self._format_intervention(
            recommendation,
            self._get_optimal_timing(user_id),
            self._get_delivery_style(user_id)
        )

    def track_effectiveness(self, user_id, intervention_id, outcome_data):
        self.effectiveness_metrics[intervention_id] = self._calculate_effectiveness(
            outcome_data
        )
        self._update_user_patterns(user_id, outcome_data)

class FrequencyController:
    def __init__(self):
        self.user_preferences = {}
        self.response_patterns = {}
        self.burnout_prevention = {}

    def get_next_intervention_time(self, user_id, context):
        return self._optimize_timing(
            user_id,
            self._get_user_patterns(user_id),
            context
        )

class EnhancedAICoachSystem:
    def __init__(self):
        self.coach = EnhancedAICoach()
        
    def process_user(self, user_id, context_data, behavior_data):
        # Update context and behavioral models
        self.coach.context_tracker.update_context(user_id, context_data)
        self.coach.behavioral_model.assess_user_state(user_id, behavior_data)

        # Check if intervention is appropriate
        if self.coach.context_tracker.is_good_intervention_time(user_id):
            # Generate personalized intervention
            intervention = self.coach.intervention_manager.create_intervention(
                user_id,
                self.coach.context_tracker,
                self.coach.behavioral_model
            )
            
            if intervention:
                return intervention

        return None

    def track_outcome(self, user_id, intervention_id, outcome_data):
        self.coach.intervention_manager.track_effectiveness(
            user_id, 
            intervention_id,
            outcome_data
        )