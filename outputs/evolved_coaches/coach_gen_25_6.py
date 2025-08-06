class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced cognitive state tracking
        self.cognitive_state_model = {
            'attention_level': 0.0,
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'stress_level': 0.0,
            'flow_state': False
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'time_based': {},
            'context_based': {},
            'state_based': {},
            'pattern_based': {}
        }

        # Intervention configuration
        self.intervention_settings = {
            'min_time_between': 30,  # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'adaptivity_rate': 0.1
        }

        # User profile tracking
        self.user_profile = {
            'preferences': {},
            'response_history': [],
            'effectiveness_metrics': {},
            'learning_patterns': {},
            'behavioral_trends': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention appropriateness"""
        context_score = 0.0
        
        # Cognitive load assessment
        cognitive_load = self._calculate_cognitive_load(user_state)
        if cognitive_load > 0.8:
            return False  # Too high cognitive load for intervention
            
        # Time-of-day optimization
        if not self._is_optimal_timing(environment_data['time']):
            return False
            
        # Flow state protection
        if self._detect_flow_state(user_state):
            return False
            
        return True

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        user_profile = self.user_profile
        personality_type = user_profile['preferences'].get('personality_type')
        
        # Select intervention type based on context and history
        intervention_type = self._select_intervention_type(context)
        
        # Personalize content
        content = self._personalize_content(
            intervention_type,
            personality_type,
            user_profile['learning_patterns']
        )
        
        # Apply behavioral psychology principles
        content = self._enhance_with_behavioral_science(content)
        
        return {
            'content': content,
            'timing': self._optimize_timing(),
            'delivery_method': self._select_delivery_method(user_profile),
            'intensity': self._calculate_intensity(context)
        }

    def track_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        self.user_profile['response_history'].append({
            'intervention_id': intervention_id,
            'response': user_response,
            'timestamp': time.time(),
            'context': self.cognitive_state_model.copy()
        })
        
        self._update_effectiveness_metrics(intervention_id, user_response)
        self._adapt_intervention_parameters()

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on multiple factors"""
        factors = [
            user_state['task_complexity'] * 0.3,
            user_state['multitasking_level'] * 0.2,
            user_state['time_pressure'] * 0.2,
            user_state['interruption_frequency'] * 0.15,
            user_state['emotional_state'] * 0.15
        ]
        return sum(factors)

    def _detect_flow_state(self, user_state):
        """Detect if user is in flow state to avoid interruption"""
        flow_indicators = [
            user_state['focus_duration'] > 25,
            user_state['task_engagement'] > 0.8,
            user_state['productivity_level'] > 0.7,
            user_state['interruption_frequency'] < 0.2
        ]
        return sum(flow_indicators) >= 3

    def _personalize_content(self, intervention_type, personality_type, learning_patterns):
        """Create personalized intervention content"""
        base_content = self._get_base_content(intervention_type)
        
        if personality_type in self.personality_type_configs:
            config = self.personality_type_configs[personality_type]
            base_content = self._adapt_to_learning_style(base_content, config['learning_style'])
            base_content = self._adapt_communication_style(base_content, config['communication_pref'])
            
        return self._enhance_actionability(base_content)

    def _enhance_with_behavioral_science(self, content):
        """Apply behavioral psychology principles to content"""
        content = self._add_social_proof(content)
        content = self._incorporate_loss_aversion(content)
        content = self._add_commitment_mechanism(content)
        return self._optimize_choice_architecture(content)

    def _adapt_intervention_parameters(self):
        """Adjust intervention parameters based on effectiveness"""
        recent_responses = self.user_profile['response_history'][-10:]
        effectiveness = sum(r['response']['effectiveness'] for r in recent_responses) / len(recent_responses)
        
        self.intervention_settings['intensity_level'] *= (1 + self.intervention_settings['adaptivity_rate'] * (effectiveness - 0.5))
        self.intervention_settings['intensity_level'] = max(0.1, min(1.0, self.intervention_settings['intensity_level']))

    def _optimize_timing(self):
        """Optimize intervention timing based on user patterns"""
        current_time = time.time()
        last_intervention = self.user_profile['response_history'][-1]['timestamp'] if self.user_profile['response_history'] else 0
        
        if current_time - last_intervention < self.intervention_settings['min_time_between'] * 60:
            return False
            
        return self._calculate_optimal_time()