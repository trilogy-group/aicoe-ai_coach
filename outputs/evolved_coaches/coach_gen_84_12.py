class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.cognitive_models = {}
        self.behavioral_patterns = {}
        
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
        
        # Check cognitive readiness
        if not self._is_receptive(user):
            return None
            
        # Select optimal intervention type
        intervention_type = self._select_intervention(
            user['cognitive_state'],
            user['learning_patterns'],
            context
        )
        
        # Personalize content
        content = self._personalize_content(
            intervention_type,
            user,
            context
        )
        
        # Add behavioral psychology elements
        enhanced_content = self._apply_behavioral_psychology(content, user)
        
        return {
            'type': intervention_type,
            'content': enhanced_content,
            'timing': self._optimize_timing(user),
            'action_steps': self._generate_action_steps(enhanced_content)
        }

    def track_response(self, user_id, nudge_id, response_data):
        """Track user response to intervention"""
        user = self.user_profiles[user_id]
        user['response_history'].append({
            'nudge_id': nudge_id,
            'response': response_data,
            'timestamp': response_data['timestamp'],
            'effectiveness': response_data['effectiveness']
        })
        
        self._update_learning_patterns(user_id, response_data)

    def _is_receptive(self, user):
        """Check if user is in receptive state for coaching"""
        return (user['cognitive_state'] < 0.8 and 
                user['stress_level'] < 0.7 and
                user['attention_capacity'] > 0.3)

    def _select_intervention(self, cognitive_state, learning_patterns, context):
        """Select most effective intervention type based on user state"""
        if cognitive_state > 0.7:
            return 'micro_action'
        elif context.get('time_pressure', 0) > 0.8:
            return 'quick_tip'
        elif len(learning_patterns) > 5:
            return 'pattern_based'
        return 'standard'

    def _personalize_content(self, intervention_type, user, context):
        """Personalize intervention content"""
        base_content = self._get_base_content(intervention_type)
        
        # Adapt to user preferences
        content = self._adapt_to_preferences(base_content, user['context_preferences'])
        
        # Consider temporal context
        content = self._adapt_to_timing(content, user['peak_performance_times'])
        
        # Add user-specific elements
        content = self._add_personal_relevance(content, user['learning_patterns'])
        
        return content

    def _apply_behavioral_psychology(self, content, user):
        """Apply behavioral psychology principles"""
        enhanced = content.copy()
        
        # Add social proof elements
        enhanced['social_proof'] = self._generate_social_proof(user)
        
        # Include commitment devices
        enhanced['commitment_mechanism'] = self._create_commitment_device(user)
        
        # Add progress visualization
        enhanced['progress_markers'] = self._generate_progress_indicators(user)
        
        return enhanced

    def _generate_action_steps(self, content):
        """Generate specific, actionable steps"""
        return [{
            'step': i+1,
            'action': action,
            'timeframe': timeframe,
            'difficulty': difficulty,
            'expected_outcome': outcome
        } for i, (action, timeframe, difficulty, outcome) in 
        enumerate(self._break_down_actions(content))]

    def _optimize_timing(self, user):
        """Optimize intervention timing"""
        return {
            'preferred_time': self._get_peak_times(user),
            'frequency': self._calculate_optimal_frequency(user),
            'spacing': self._calculate_optimal_spacing(user)
        }

    def _update_learning_patterns(self, user_id, response_data):
        """Update user learning patterns based on response"""
        user = self.user_profiles[user_id]
        
        # Update effectiveness tracking
        self._update_effectiveness_metrics(user, response_data)
        
        # Adjust intervention preferences
        self._adjust_preferences(user, response_data)
        
        # Update timing optimization
        self._update_timing_model(user, response_data)

    def _calculate_cognitive_load(self, indicators):
        """Calculate cognitive load score"""
        weights = {
            'task_complexity': 0.3,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2,
            'focus_duration': 0.2
        }
        return sum(indicator * weights[key] 
                  for key, indicator in indicators.items())