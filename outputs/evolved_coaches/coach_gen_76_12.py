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
            'response_history': [],
            'cognitive_load': 0.0,
            'engagement_level': 0.0,
            'stress_level': 0.0
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate user's current context and state"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        time_of_day = context_data.get('time')
        current_activity = context_data.get('activity')
        stress_indicators = context_data.get('stress_signals', [])
        
        context_score = {
            'cognitive_load': cognitive_load,
            'receptivity': self._calculate_receptivity(time_of_day, cognitive_load),
            'urgency': self._evaluate_urgency(stress_indicators),
            'activity_compatibility': self._check_activity_compatibility(current_activity)
        }
        
        return context_score

    def generate_intervention(self, user_id, context_score):
        """Create personalized coaching intervention"""
        user_profile = self.user_profiles[user_id]
        
        # Select optimal intervention type
        if context_score['cognitive_load'] > 0.7:
            intervention_type = 'micro_action'
        elif context_score['urgency'] > 0.8:
            intervention_type = 'immediate_support'
        else:
            intervention_type = 'standard_coaching'

        # Personalize content
        content = self._personalize_content(
            user_profile,
            intervention_type,
            context_score
        )

        # Add behavioral psychology elements
        content = self._enhance_with_psychology(content, user_profile)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': self._optimize_timing(context_score),
            'delivery_method': self._select_delivery_method(user_profile)
        }

    def track_response(self, user_id, intervention, response_data):
        """Track and learn from user's response to intervention"""
        self.intervention_history.setdefault(user_id, []).append({
            'intervention': intervention,
            'response': response_data,
            'timestamp': response_data.get('timestamp')
        })
        
        self._update_user_model(user_id, response_data)
        self._adjust_strategies(user_id)

    def _calculate_cognitive_load(self, context_data):
        """Estimate current cognitive load based on context"""
        factors = {
            'task_complexity': context_data.get('task_complexity', 0.5),
            'interruptions': context_data.get('interruption_frequency', 0.3),
            'time_pressure': context_data.get('time_pressure', 0.4),
            'mental_fatigue': context_data.get('fatigue_indicators', 0.4)
        }
        
        return sum(factors.values()) / len(factors)

    def _calculate_receptivity(self, time_of_day, cognitive_load):
        """Calculate user's likely receptivity to coaching"""
        base_receptivity = self._get_time_based_receptivity(time_of_day)
        return base_receptivity * (1 - cognitive_load)

    def _personalize_content(self, user_profile, intervention_type, context):
        """Create personalized intervention content"""
        templates = self._get_intervention_templates(intervention_type)
        selected = self._select_best_template(templates, user_profile)
        
        return self._customize_template(
            selected,
            user_profile['preferences'],
            context
        )

    def _enhance_with_psychology(self, content, user_profile):
        """Add psychological elements to increase effectiveness"""
        motivation_type = user_profile.get('motivation_factors', ['achievement'])[0]
        
        enhancers = {
            'achievement': self._add_achievement_framing,
            'social': self._add_social_proof,
            'growth': self._add_growth_mindset,
            'autonomy': self._add_choice_architecture
        }
        
        return enhancers.get(motivation_type, lambda x: x)(content)

    def _optimize_timing(self, context_score):
        """Determine optimal delivery timing"""
        if context_score['urgency'] > 0.8:
            return 'immediate'
        elif context_score['cognitive_load'] > 0.7:
            return 'next_break'
        else:
            return 'optimal_window'

    def _select_delivery_method(self, user_profile):
        """Choose best delivery method based on user preferences"""
        preferences = user_profile.get('preferences', {})
        return preferences.get('preferred_channel', 'notification')

    def _update_user_model(self, user_id, response_data):
        """Update user model based on intervention response"""
        effectiveness = response_data.get('effectiveness', 0.0)
        engagement = response_data.get('engagement', 0.0)
        
        profile = self.user_profiles[user_id]
        profile['response_history'].append({
            'effectiveness': effectiveness,
            'engagement': engagement,
            'timestamp': response_data.get('timestamp')
        })
        
        self._update_learning_model(user_id, response_data)

    def _adjust_strategies(self, user_id):
        """Adjust coaching strategies based on accumulated data"""
        history = self.intervention_history[user_id]
        if len(history) >= 5:
            successful_patterns = self._analyze_success_patterns(history)
            self.behavioral_patterns[user_id] = successful_patterns