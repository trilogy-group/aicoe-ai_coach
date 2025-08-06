class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'cognitive_state': None,
            'attention_capacity': 1.0,
            'stress_level': 0.0,
            'engagement_level': 0.5,
            'learning_patterns': [],
            'response_history': [],
            'context_preferences': {},
            'peak_performance_times': []
        }
        
    def assess_cognitive_load(self, user_id, context_data):
        """Evaluate current cognitive load and attention capacity"""
        cognitive_indicators = {
            'task_complexity': context_data.get('task_complexity', 0.5),
            'time_pressure': context_data.get('time_pressure', 0.5),
            'interruption_frequency': context_data.get('interruptions', 0.3),
            'focus_duration': context_data.get('focus_time', 30)
        }
        
        cognitive_load = self._calculate_cognitive_load(cognitive_indicators)
        self.user_profiles[user_id]['cognitive_state'] = cognitive_load
        return cognitive_load

    def generate_personalized_nudge(self, user_id, context):
        """Generate contextually relevant coaching intervention"""
        user = self.user_profiles[user_id]
        
        # Check intervention timing and frequency
        if not self._is_optimal_timing(user_id, context):
            return None
            
        # Select intervention type based on user state
        intervention_type = self._select_intervention_type(user, context)
        
        # Generate specific actionable recommendation
        recommendation = self._generate_recommendation(
            user_id,
            intervention_type,
            context
        )
        
        # Personalize delivery style
        delivery = self._personalize_delivery(user_id, recommendation)
        
        return {
            'message': delivery['content'],
            'urgency': delivery['urgency'],
            'action_items': delivery['actions'],
            'follow_up': delivery['follow_up']
        }

    def track_intervention_response(self, user_id, intervention_id, response_data):
        """Track and analyze user response to intervention"""
        self.intervention_history.setdefault(user_id, []).append({
            'intervention_id': intervention_id,
            'timestamp': response_data['timestamp'],
            'engagement': response_data['engagement'],
            'completion': response_data['completion'],
            'feedback': response_data['feedback']
        })
        
        self._update_user_model(user_id, response_data)

    def _calculate_cognitive_load(self, indicators):
        """Calculate cognitive load score from indicators"""
        weights = {
            'task_complexity': 0.3,
            'time_pressure': 0.25,
            'interruption_frequency': 0.25,
            'focus_duration': 0.2
        }
        
        load_score = sum(
            indicators[k] * weights[k] 
            for k in weights
        )
        
        return min(load_score, 1.0)

    def _is_optimal_timing(self, user_id, context):
        """Determine if current moment is optimal for intervention"""
        user = self.user_profiles[user_id]
        
        # Check cognitive load
        if user['cognitive_state'] > 0.8:
            return False
            
        # Check flow state
        if self._detect_flow_state(user_id):
            return False
            
        # Check time patterns
        if not self._is_preferred_time(user_id, context['timestamp']):
            return False
            
        return True

    def _select_intervention_type(self, user, context):
        """Select most appropriate intervention type"""
        options = {
            'quick_tip': 0.0,
            'deep_insight': 0.0,
            'action_prompt': 0.0,
            'reflection': 0.0
        }
        
        # Score each type based on context
        cognitive_load = user['cognitive_state']
        engagement = user['engagement_level']
        
        options['quick_tip'] = 1.0 if cognitive_load > 0.6 else 0.3
        options['deep_insight'] = 0.8 if cognitive_load < 0.4 else 0.1
        options['action_prompt'] = 0.9 if engagement > 0.7 else 0.4
        options['reflection'] = 0.7 if cognitive_load < 0.3 else 0.2
        
        return max(options.items(), key=lambda x: x[1])[0]

    def _generate_recommendation(self, user_id, intervention_type, context):
        """Generate specific actionable recommendation"""
        user = self.user_profiles[user_id]
        
        if intervention_type == 'quick_tip':
            return self._generate_quick_tip(user, context)
        elif intervention_type == 'deep_insight':
            return self._generate_deep_insight(user, context)
        elif intervention_type == 'action_prompt':
            return self._generate_action_prompt(user, context)
        else:
            return self._generate_reflection(user, context)

    def _personalize_delivery(self, user_id, recommendation):
        """Personalize intervention delivery style"""
        user = self.user_profiles[user_id]
        
        # Adjust language style
        tone = self._determine_tone(user)
        content = self._adjust_language(recommendation, tone)
        
        # Set urgency
        urgency = self._calculate_urgency(user, recommendation)
        
        # Generate specific actions
        actions = self._generate_action_items(recommendation)
        
        # Plan follow-up
        follow_up = self._plan_follow_up(user_id, recommendation)
        
        return {
            'content': content,
            'urgency': urgency,
            'actions': actions,
            'follow_up': follow_up
        }

    def _update_user_model(self, user_id, response_data):
        """Update user model based on intervention response"""
        user = self.user_profiles[user_id]
        
        # Update engagement metrics
        user['engagement_level'] = (
            user['engagement_level'] * 0.7 + 
            response_data['engagement'] * 0.3
        )
        
        # Update learning patterns
        self._update_learning_patterns(user_id, response_data)
        
        # Update context preferences
        self._update_context_preferences(user_id, response_data)
        
        # Update peak performance times
        if response_data['completion'] > 0.8:
            self._update_peak_times(user_id, response_data['timestamp'])