class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced context tracking
        self.context_tracker = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': 'neutral',
            'time_of_day': None,
            'work_context': None,
            'interruption_cost': 0.0
        }

        # Behavioral psychology components
        self.behavioral_patterns = {
            'habit_strength': {},
            'motivation_factors': {},
            'resistance_points': {},
            'success_triggers': {}
        }

        # Personalization metrics
        self.user_profile = {
            'learning_history': [],
            'response_patterns': {},
            'preference_weights': {},
            'intervention_effectiveness': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        focus_impact = self._assess_focus_impact(environment_data)
        timing_score = self._evaluate_timing_appropriateness(user_state)
        
        return {
            'intervention_appropriate': cognitive_load < 0.7 and focus_impact < 0.5,
            'optimal_timing': timing_score > 0.8,
            'suggested_intensity': self._calculate_intensity(cognitive_load)
        }

    def generate_intervention(self, user_context, behavioral_goal):
        """Create personalized coaching intervention"""
        # Select intervention type based on user profile and context
        intervention_type = self._select_intervention_type(user_context)
        
        # Generate personalized content
        content = self._generate_content(
            intervention_type,
            behavioral_goal,
            self.user_profile['learning_history']
        )
        
        # Optimize delivery approach
        delivery = self._optimize_delivery(
            content,
            self.user_profile['preference_weights']
        )
        
        return {
            'content': content,
            'delivery_method': delivery,
            'timing': self._get_optimal_timing(),
            'intensity': self._calculate_intensity(self.context_tracker['cognitive_load'])
        }

    def track_effectiveness(self, intervention_id, user_response):
        """Monitor and adapt to intervention effectiveness"""
        # Update effectiveness metrics
        self.user_profile['intervention_effectiveness'][intervention_id] = user_response
        
        # Adjust future interventions based on response
        self._update_learning_patterns(intervention_id, user_response)
        self._adjust_preference_weights(user_response)
        
        # Optimize future selections
        self._refine_intervention_strategy()

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive load based on multiple factors"""
        task_complexity = user_state.get('task_complexity', 0.5)
        current_focus = user_state.get('focus_level', 0.5)
        environmental_stress = user_state.get('stress_level', 0.3)
        
        return (task_complexity * 0.4 + 
                (1 - current_focus) * 0.4 + 
                environmental_stress * 0.2)

    def _select_intervention_type(self, user_context):
        """Choose most appropriate intervention type"""
        personality_type = user_context.get('personality_type')
        current_state = user_context.get('current_state')
        
        if personality_type in self.personality_type_configs:
            config = self.personality_type_configs[personality_type]
            return self._match_intervention_to_style(config, current_state)
        
        return 'default_intervention'

    def _generate_content(self, intervention_type, goal, history):
        """Create personalized intervention content"""
        template = self._get_intervention_template(intervention_type)
        personalization = self._apply_personal_preferences(history)
        
        content = template.format(
            goal=goal,
            personal_elements=personalization,
            action_steps=self._generate_action_steps(goal)
        )
        
        return content

    def _optimize_delivery(self, content, preferences):
        """Optimize intervention delivery method"""
        return {
            'channel': self._select_optimal_channel(preferences),
            'format': self._select_optimal_format(content, preferences),
            'timing': self._calculate_optimal_timing(preferences)
        }

    def _update_learning_patterns(self, intervention_id, response):
        """Update user learning patterns based on intervention response"""
        self.user_profile['learning_history'].append({
            'intervention_id': intervention_id,
            'response': response,
            'context': self.context_tracker.copy(),
            'timestamp': self._get_current_timestamp()
        })

    def _refine_intervention_strategy(self):
        """Refine intervention strategy based on accumulated data"""
        effectiveness_data = self.user_profile['intervention_effectiveness']
        learning_patterns = self._analyze_learning_patterns()
        
        self.behavioral_patterns['success_triggers'].update(
            self._extract_success_patterns(effectiveness_data)
        )
        
        self._update_intervention_weights(learning_patterns)

    def _get_optimal_timing(self):
        """Calculate optimal intervention timing"""
        current_load = self.context_tracker['cognitive_load']
        time_patterns = self._analyze_time_patterns()
        
        return self._calculate_next_intervention_time(
            current_load,
            time_patterns
        )