class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'cognitive_load': 0.0,
            'engagement_level': 0.0,
            'stress_level': 0.0,
            'learning_style': None,
            'intervention_preferences': {},
            'peak_performance_times': [],
            'behavioral_triggers': {},
            'success_patterns': []
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate user's current context and state"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        time_of_day = context_data.get('time')
        current_activity = context_data.get('activity')
        stress_indicators = context_data.get('stress_signals', [])
        
        context_score = {
            'cognitive_capacity': self._assess_cognitive_capacity(cognitive_load),
            'timing_optimality': self._evaluate_timing(time_of_day, user_id),
            'activity_compatibility': self._check_activity_compatibility(current_activity),
            'stress_level': self._analyze_stress_indicators(stress_indicators)
        }
        
        return context_score

    def generate_intervention(self, user_id, context_score):
        """Create personalized coaching intervention"""
        if not self._should_intervene(user_id, context_score):
            return None
            
        user_profile = self.user_profiles[user_id]
        
        # Select optimal intervention type
        intervention_type = self._select_intervention_type(
            user_profile,
            context_score
        )
        
        # Generate personalized content
        content = self._generate_content(
            intervention_type,
            user_profile,
            context_score
        )
        
        # Add specific actionable steps
        action_steps = self._create_action_steps(content, user_profile)
        
        return {
            'type': intervention_type,
            'content': content,
            'action_steps': action_steps,
            'timing': self._optimize_timing(user_profile),
            'delivery_method': self._select_delivery_method(user_profile)
        }

    def track_response(self, user_id, intervention, response_data):
        """Track and learn from user's response to intervention"""
        effectiveness = self._calculate_effectiveness(response_data)
        self._update_user_profile(user_id, effectiveness)
        self._update_intervention_history(user_id, intervention, effectiveness)
        self._refine_behavioral_patterns(user_id, response_data)

    def _calculate_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        task_complexity = context_data.get('task_complexity', 0)
        distractions = len(context_data.get('distractions', []))
        time_pressure = context_data.get('time_pressure', 0)
        
        return (0.4 * task_complexity + 
                0.3 * distractions +
                0.3 * time_pressure)

    def _assess_cognitive_capacity(self, cognitive_load):
        """Determine available cognitive capacity"""
        base_capacity = 100
        return max(0, base_capacity - cognitive_load)

    def _evaluate_timing(self, time_of_day, user_id):
        """Evaluate optimal timing for intervention"""
        user_peaks = self.user_profiles[user_id]['peak_performance_times']
        current_time = self._convert_to_minutes(time_of_day)
        
        timing_score = 0
        for peak in user_peaks:
            distance = abs(current_time - peak)
            timing_score += max(0, 1 - (distance / 120))
            
        return min(1.0, timing_score)

    def _select_intervention_type(self, user_profile, context_score):
        """Choose most effective intervention type"""
        if context_score['cognitive_capacity'] < 30:
            return 'micro_intervention'
        elif context_score['stress_level'] > 0.7:
            return 'stress_reduction'
        elif context_score['timing_optimality'] > 0.8:
            return 'deep_learning'
        else:
            return 'standard_coaching'

    def _generate_content(self, intervention_type, user_profile, context_score):
        """Generate personalized intervention content"""
        content_templates = {
            'micro_intervention': "Quick focus tip: {action}",
            'stress_reduction': "Let's take a moment to {technique}",
            'deep_learning': "Consider this approach: {strategy}",
            'standard_coaching': "Try this: {recommendation}"
        }
        
        return self._personalize_content(
            content_templates[intervention_type],
            user_profile
        )

    def _create_action_steps(self, content, user_profile):
        """Generate specific, actionable steps"""
        return [
            {
                'step': i + 1,
                'action': action,
                'timeframe': timeframe,
                'success_metric': metric
            }
            for i, (action, timeframe, metric) 
            in enumerate(self._generate_step_sequence(content, user_profile))
        ]

    def _optimize_timing(self, user_profile):
        """Determine optimal delivery timing"""
        return {
            'preferred_time': user_profile['peak_performance_times'][0],
            'frequency': self._calculate_optimal_frequency(user_profile),
            'spacing': self._calculate_optimal_spacing(user_profile)
        }

    def _select_delivery_method(self, user_profile):
        """Choose best delivery method based on user preferences"""
        preferences = user_profile['intervention_preferences']
        return max(preferences.items(), key=lambda x: x[1])[0]

    def _should_intervene(self, user_id, context_score):
        """Determine if intervention is appropriate"""
        return (context_score['cognitive_capacity'] > 20 and
                context_score['timing_optimality'] > 0.4 and
                context_score['stress_level'] < 0.9)

    def _update_user_profile(self, user_id, effectiveness):
        """Update user profile based on intervention effectiveness"""
        profile = self.user_profiles[user_id]
        profile['success_patterns'].append(effectiveness)
        self._refine_learning_style(profile, effectiveness)
        self._update_peak_times(profile, effectiveness)

    def _refine_behavioral_patterns(self, user_id, response_data):
        """Update behavioral pattern recognition"""
        patterns = self.behavioral_patterns.get(user_id, [])
        patterns.append(response_data)
        self.behavioral_patterns[user_id] = patterns[-100:]  # Keep last 100 responses