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
            'flow_states': []
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'activity_cycles': {},
            'response_rates': {},
            'completion_patterns': {},
            'engagement_levels': {}
        }
        
    def assess_context(self, user_id, current_state):
        """Evaluate user's current context for intervention timing"""
        cognitive_load = self._estimate_cognitive_load(user_id, current_state)
        attention_availability = self._check_attention_availability(current_state)
        time_appropriateness = self._evaluate_timing(user_id, current_state)
        
        context_score = (cognitive_load * 0.4 + 
                        attention_availability * 0.3 +
                        time_appropriateness * 0.3)
                        
        return context_score > 0.7

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        if not self.assess_context(user_id, context):
            return None
            
        user_profile = self.user_profiles[user_id]
        behavioral_pattern = self.behavioral_patterns[user_id]
        
        # Select intervention type based on user patterns
        intervention_type = self._select_intervention_type(
            user_profile, 
            behavioral_pattern,
            context
        )
        
        # Generate specific actionable recommendation
        recommendation = self._generate_recommendation(
            intervention_type,
            user_profile,
            context
        )
        
        # Personalize delivery style
        delivery = self._personalize_delivery(
            recommendation,
            user_profile['preferences']
        )
        
        return {
            'type': intervention_type,
            'content': recommendation,
            'delivery': delivery,
            'timing': self._optimize_timing(user_id, context)
        }

    def track_response(self, user_id, intervention, response):
        """Track and learn from user's response to intervention"""
        self.intervention_history[user_id].append({
            'intervention': intervention,
            'response': response,
            'timestamp': response['timestamp'],
            'effectiveness': response['effectiveness']
        })
        
        self._update_user_profile(user_id, intervention, response)
        self._update_behavioral_patterns(user_id, response)
        self._optimize_future_interventions(user_id)

    def _estimate_cognitive_load(self, user_id, state):
        """Estimate current cognitive load based on user state"""
        baseline = self.user_profiles[user_id]['cognitive_load_baseline']
        activity_intensity = state.get('activity_level', 0.5)
        time_pressure = state.get('time_pressure', 0.5)
        task_complexity = state.get('task_complexity', 0.5)
        
        cognitive_load = (baseline * 0.2 +
                         activity_intensity * 0.3 +
                         time_pressure * 0.25 +
                         task_complexity * 0.25)
                         
        return min(cognitive_load, 1.0)

    def _check_attention_availability(self, state):
        """Determine if user is available for intervention"""
        focus_level = state.get('focus_level', 0.5)
        interruption_cost = state.get('interruption_cost', 0.5)
        task_urgency = state.get('task_urgency', 0.5)
        
        availability = (1 - focus_level) * 0.4 + \
                      (1 - interruption_cost) * 0.3 + \
                      (1 - task_urgency) * 0.3
                      
        return availability

    def _select_intervention_type(self, profile, patterns, context):
        """Select most appropriate intervention type"""
        effectiveness_weights = self._analyze_historical_effectiveness(patterns)
        context_weights = self._analyze_context_fit(context)
        user_preferences = profile['preferences']
        
        intervention_scores = {}
        for intervention_type in ['nudge', 'suggestion', 'reminder', 'challenge']:
            score = (effectiveness_weights.get(intervention_type, 0.5) * 0.4 +
                    context_weights.get(intervention_type, 0.5) * 0.4 +
                    user_preferences.get(intervention_type, 0.5) * 0.2)
            intervention_scores[intervention_type] = score
            
        return max(intervention_scores, key=intervention_scores.get)

    def _generate_recommendation(self, intervention_type, profile, context):
        """Generate specific actionable recommendation"""
        if intervention_type == 'nudge':
            return self._generate_nudge(profile, context)
        elif intervention_type == 'suggestion':
            return self._generate_suggestion(profile, context)
        elif intervention_type == 'reminder':
            return self._generate_reminder(profile, context)
        else:
            return self._generate_challenge(profile, context)

    def _personalize_delivery(self, content, preferences):
        """Personalize intervention delivery style"""
        tone = preferences.get('communication_tone', 'neutral')
        detail_level = preferences.get('detail_level', 'medium')
        
        personalized_content = self._adjust_tone(content, tone)
        final_content = self._adjust_detail(personalized_content, detail_level)
        
        return final_content

    def _optimize_timing(self, user_id, context):
        """Optimize intervention timing"""
        optimal_times = self.user_profiles[user_id]['optimal_times']
        current_time = context.get('timestamp')
        
        timing_score = self._calculate_timing_score(
            optimal_times, 
            current_time,
            context
        )
        
        return {
            'optimal_time': timing_score > 0.8,
            'delay_minutes': self._calculate_delay(timing_score)
        }

    def _update_user_profile(self, user_id, intervention, response):
        """Update user profile based on intervention response"""
        profile = self.user_profiles[user_id]
        
        profile['preferences'] = self._update_preferences(
            profile['preferences'],
            intervention,
            response
        )
        
        profile['response_patterns'] = self._update_response_patterns(
            profile['response_patterns'],
            intervention,
            response
        )

    def _optimize_future_interventions(self, user_id):
        """Optimize future interventions based on historical data"""
        history = self.intervention_history[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        self._update_timing_models(user_id, history)
        self._update_effectiveness_models(user_id, history)
        self._update_engagement_patterns(user_id, patterns)