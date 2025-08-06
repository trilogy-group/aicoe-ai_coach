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

        # Personalization engine
        self.user_profile = {
            'personality_type': None,
            'learning_history': [],
            'response_patterns': {},
            'peak_performance_times': [],
            'intervention_preferences': {}
        }

        # Intervention optimization
        self.intervention_config = {
            'min_time_between': 30,  # minutes
            'max_daily_interventions': 8,
            'intensity_levels': ['subtle', 'moderate', 'strong'],
            'delivery_methods': ['notification', 'email', 'in-app']
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        interruption_cost = self._estimate_interruption_cost(user_state)
        
        self.context_tracker.update({
            'cognitive_load': cognitive_load,
            'energy_level': user_state.get('energy', 0.0),
            'focus_state': self._detect_flow_state(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity'),
            'interruption_cost': interruption_cost
        })
        
        return self.context_tracker

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        user_profile = self.user_profile
        current_context = self.assess_context(context['user_state'], context['environment'])

        if not self._should_intervene(current_context):
            return None

        intervention_type = self._select_intervention_type(user_profile, current_context)
        content = self._generate_content(intervention_type, user_profile, current_context)
        delivery = self._optimize_delivery(content, current_context)

        return {
            'type': intervention_type,
            'content': content,
            'delivery_method': delivery,
            'timing': self._optimize_timing(current_context),
            'intensity': self._calculate_intensity(current_context)
        }

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction feedback"""
        response = interaction_data.get('response')
        effectiveness = interaction_data.get('effectiveness')
        
        self.user_profile['learning_history'].append(interaction_data)
        self.user_profile['response_patterns'][response.type] = effectiveness
        
        self._update_behavioral_patterns(interaction_data)
        self._refine_intervention_preferences(interaction_data)

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on user state"""
        task_complexity = user_state.get('task_complexity', 0.5)
        context_switches = user_state.get('context_switches', 0)
        time_pressure = user_state.get('time_pressure', 0.5)
        
        return (task_complexity * 0.4 + 
                min(context_switches / 10, 1.0) * 0.3 + 
                time_pressure * 0.3)

    def _detect_flow_state(self, user_state):
        """Detect if user is in flow state"""
        focus_duration = user_state.get('focus_duration', 0)
        productivity = user_state.get('productivity', 0.0)
        interruptions = user_state.get('interruptions', 0)

        if (focus_duration > 25 and 
            productivity > 0.7 and 
            interruptions < 2):
            return 'flow'
        return 'neutral'

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        if (context['focus_state'] == 'flow' or
            context['cognitive_load'] > 0.8 or
            context['interruption_cost'] > 0.7):
            return False
        return True

    def _select_intervention_type(self, user_profile, context):
        """Select most appropriate intervention type"""
        personality = user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        if context['energy_level'] < 0.3:
            return 'energy_management'
        elif context['cognitive_load'] > 0.6:
            return 'focus_enhancement'
        return 'productivity_optimization'

    def _generate_content(self, intervention_type, user_profile, context):
        """Generate personalized intervention content"""
        templates = self._get_content_templates(intervention_type)
        selected = self._personalize_template(
            templates, 
            user_profile['personality_type'],
            context
        )
        return self._fill_template(selected, context)

    def _optimize_delivery(self, content, context):
        """Optimize intervention delivery method"""
        if context['cognitive_load'] > 0.6:
            return 'notification'
        elif len(content) > 100:
            return 'email'
        return 'in-app'

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        if context['time_of_day'] in self.user_profile['peak_performance_times']:
            return 'immediate'
        return 'next_break'

    def _calculate_intensity(self, context):
        """Calculate appropriate intervention intensity"""
        if context['cognitive_load'] < 0.3:
            return 'strong'
        elif context['cognitive_load'] < 0.6:
            return 'moderate'
        return 'subtle'

    def _update_behavioral_patterns(self, interaction_data):
        """Update tracked behavioral patterns"""
        behavior = interaction_data.get('behavior')
        success = interaction_data.get('success', False)
        
        if behavior:
            current_strength = self.behavioral_patterns['habit_strength'].get(behavior, 0)
            self.behavioral_patterns['habit_strength'][behavior] = current_strength + (0.1 if success else -0.05)

    def _refine_intervention_preferences(self, interaction_data):
        """Refine intervention preferences based on feedback"""
        method = interaction_data.get('delivery_method')
        success = interaction_data.get('success', False)
        
        if method:
            current_pref = self.user_profile['intervention_preferences'].get(method, 0.5)
            self.user_profile['intervention_preferences'][method] = current_pref + (0.1 if success else -0.05)