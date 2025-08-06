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

    def _assess_cognitive_load(self, context_data):
        # Enhanced cognitive load assessment using multiple signals
        task_complexity = context_data.get('task_complexity', 0.5)
        time_pressure = context_data.get('time_pressure', 0.5) 
        interruption_frequency = context_data.get('interruptions', 0.3)
        return (0.4 * task_complexity + 0.4 * time_pressure + 0.2 * interruption_frequency)

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
            'specifics': self._generate_specifics(context),
            'timeframe': self._suggest_timeframe(context),
            'success_metrics': self._define_metrics(),
            'alternatives': self._generate_alternatives(),
            'priority': self._assign_priority(context)
        }
        return self._personalize_recommendation(recommendation, user_id)

    def _select_action(self, context, behavior):
        if context.cognitive_load > 0.7:
            return self._generate_low_effort_action()
        elif behavior['motivation_level'] < 0.4:
            return self._generate_motivation_focused_action()
        else:
            return self._generate_standard_action()

class InterventionManager:
    def __init__(self):
        self.intervention_schedule = {}
        self.effectiveness_tracker = {}
        self.adaptation_rules = {}

    def schedule_intervention(self, user_id, recommendation, context):
        timing = self._optimize_timing(user_id, context)
        format = self._select_format(context)
        intensity = self._calibrate_intensity(user_id)
        
        return {
            'timing': timing,
            'format': format,
            'intensity': intensity,
            'content': recommendation,
            'follow_up': self._schedule_followup(timing)
        }

    def _optimize_timing(self, user_id, context):
        cognitive_load = context.cognitive_load
        attention_state = context.attention_state
        work_patterns = context.time_patterns.get(user_id, {})
        
        optimal_time = self._calculate_optimal_time(
            cognitive_load,
            attention_state,
            work_patterns
        )
        return optimal_time

class AICoachSystem:
    def __init__(self):
        self.context_tracker = ContextTracker()
        self.behavioral_model = BehavioralModel()
        self.recommendation_engine = RecommendationEngine()
        self.intervention_manager = InterventionManager()

    def generate_coaching_intervention(self, user_id, context_data, behavior_data):
        # Update context understanding
        self.context_tracker.update_context(user_id, context_data)
        
        # Analyze behavioral patterns
        behavior_analysis = self.behavioral_model.analyze_behavior(
            user_id, 
            behavior_data
        )

        # Generate personalized recommendation
        recommendation = self.recommendation_engine.generate_recommendation(
            user_id,
            self.context_tracker,
            behavior_analysis
        )

        # Schedule and format intervention
        intervention = self.intervention_manager.schedule_intervention(
            user_id,
            recommendation,
            self.context_tracker
        )

        return intervention

    def track_intervention_effectiveness(self, user_id, intervention_id, metrics):
        self.intervention_manager.effectiveness_tracker[intervention_id] = metrics
        self._adapt_strategies(user_id, metrics)

    def _adapt_strategies(self, user_id, effectiveness_metrics):
        if effectiveness_metrics['engagement'] < 0.5:
            self.recommendation_engine.adaptation_rules[user_id]['engagement_focus'] = True
        if effectiveness_metrics['completion'] < 0.4:
            self.recommendation_engine.adaptation_rules[user_id]['simplify_actions'] = True