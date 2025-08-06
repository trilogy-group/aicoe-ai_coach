class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'preferences': {},
            'learning_style': None,
            'motivation_factors': [],
            'response_patterns': {},
            'cognitive_load_baseline': 0.5,
            'optimal_times': [],
            'burnout_risk': 0.0
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'activity_patterns': {},
            'response_rates': {},
            'completion_rates': {},
            'engagement_scores': {}
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._estimate_cognitive_load(context_data)
        time_appropriateness = self._check_timing_appropriateness(user_id, context_data)
        attention_availability = self._assess_attention_capacity(context_data)
        
        return {
            'cognitive_load': cognitive_load,
            'timing_score': time_appropriateness,
            'attention_score': attention_availability,
            'intervention_readiness': (cognitive_load + time_appropriateness + attention_availability) / 3
        }

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        if context['intervention_readiness'] < 0.4:
            return None
            
        user_profile = self.user_profiles[user_id]
        behavioral_data = self.behavioral_patterns[user_id]
        
        intervention_type = self._select_intervention_type(user_profile, context)
        content = self._generate_content(intervention_type, user_profile, context)
        delivery_method = self._optimize_delivery(user_profile, context)
        
        intervention = {
            'type': intervention_type,
            'content': content,
            'delivery': delivery_method,
            'timing': self._get_optimal_timing(user_id, context),
            'expected_impact': self._predict_effectiveness(user_id, content)
        }
        
        self.intervention_history[user_id].append(intervention)
        return intervention

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on intervention response"""
        profile = self.user_profiles[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        # Update response patterns
        self._update_response_patterns(profile, interaction_data)
        
        # Update behavioral patterns
        self._update_behavioral_patterns(patterns, interaction_data)
        
        # Adjust intervention parameters
        self._optimize_parameters(user_id, interaction_data)
        
        # Update cognitive model
        self._update_cognitive_model(user_id, interaction_data)

    def _estimate_cognitive_load(self, context_data):
        """Estimate current cognitive load based on context"""
        factors = {
            'task_complexity': 0.3,
            'time_pressure': 0.2,
            'interruption_frequency': 0.2,
            'focus_state': 0.3
        }
        
        load_score = sum(
            factors[factor] * context_data.get(factor, 0.5) 
            for factor in factors
        )
        return min(1.0, max(0.0, load_score))

    def _check_timing_appropriateness(self, user_id, context):
        """Evaluate appropriateness of current timing"""
        profile = self.user_profiles[user_id]
        current_time = context.get('timestamp')
        
        timing_score = self._calculate_timing_score(profile, current_time)
        return timing_score

    def _assess_attention_capacity(self, context):
        """Assess user's current attention availability"""
        attention_factors = {
            'focus_duration': context.get('focus_duration', 0),
            'interruption_count': context.get('interruption_count', 0),
            'task_switches': context.get('task_switches', 0)
        }
        
        attention_score = self._calculate_attention_score(attention_factors)
        return attention_score

    def _select_intervention_type(self, user_profile, context):
        """Select most appropriate intervention type"""
        options = ['nudge', 'reminder', 'suggestion', 'challenge']
        scores = self._score_intervention_options(options, user_profile, context)
        return max(scores, key=scores.get)

    def _generate_content(self, intervention_type, user_profile, context):
        """Generate personalized intervention content"""
        content_template = self._get_content_template(intervention_type)
        personalized_content = self._personalize_content(
            content_template, 
            user_profile,
            context
        )
        return personalized_content

    def _optimize_delivery(self, user_profile, context):
        """Optimize intervention delivery method"""
        methods = ['notification', 'email', 'in-app', 'calendar']
        return self._select_best_delivery(methods, user_profile, context)

    def _get_optimal_timing(self, user_id, context):
        """Determine optimal delivery timing"""
        profile = self.user_profiles[user_id]
        current_time = context.get('timestamp')
        
        return self._calculate_optimal_time(profile, current_time)

    def _predict_effectiveness(self, user_id, content):
        """Predict intervention effectiveness"""
        history = self.intervention_history[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        return self._calculate_effectiveness_score(content, history, patterns)

    def _update_response_patterns(self, profile, interaction_data):
        """Update user response patterns"""
        response_type = interaction_data.get('response_type')
        response_time = interaction_data.get('response_time')
        
        profile['response_patterns'][response_type] = response_time

    def _update_behavioral_patterns(self, patterns, interaction_data):
        """Update behavioral pattern tracking"""
        behavior_type = interaction_data.get('behavior_type')
        behavior_data = interaction_data.get('behavior_data')
        
        patterns['activity_patterns'][behavior_type] = behavior_data

    def _optimize_parameters(self, user_id, interaction_data):
        """Optimize intervention parameters based on feedback"""
        effectiveness = interaction_data.get('effectiveness', 0)
        timing = interaction_data.get('timing_score', 0)
        
        self._adjust_parameters(user_id, effectiveness, timing)

    def _update_cognitive_model(self, user_id, interaction_data):
        """Update user cognitive model"""
        cognitive_state = interaction_data.get('cognitive_state', {})
        self.cognitive_models[user_id] = self._update_model(
            self.cognitive_models.get(user_id, {}),
            cognitive_state
        )