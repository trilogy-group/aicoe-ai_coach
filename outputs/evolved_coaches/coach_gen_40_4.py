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
        self.behavioral_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'flow_state': {'challenge': 0.0, 'skill': 0.0},
            'engagement': {'interest': 0.0, 'commitment': 0.0}
        }

        # Personalization tracking
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'success_metrics': {},
            'preference_weights': {},
            'intervention_effectiveness': {}
        }

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {'duration': 2, 'frequency': 45},
            'deep_work': {'duration': 25, 'frequency': 90},
            'reflection': {'duration': 5, 'frequency': 120},
            'skill_building': {'duration': 15, 'frequency': 180}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context and environment"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy_level(user_state),
            'focus_state': self._determine_focus_state(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('context'),
            'interruption_cost': self._calculate_interruption_cost()
        })
        return self.context_tracker

    def generate_intervention(self, context=None):
        """Create personalized intervention based on context"""
        if not context:
            context = self.context_tracker

        # Select optimal intervention type
        intervention_type = self._select_intervention_type(context)
        
        # Personalize content and delivery
        content = self._personalize_content(intervention_type)
        timing = self._optimize_timing(context)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': timing,
            'duration': self.intervention_types[intervention_type]['duration'],
            'delivery_method': self._select_delivery_method(context)
        }

    def update_user_model(self, interaction_data):
        """Update user model based on interaction data"""
        self.user_profile['response_history'].append(interaction_data)
        self._update_effectiveness_metrics(interaction_data)
        self._adjust_intervention_parameters(interaction_data)
        self._update_learning_patterns(interaction_data)

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load"""
        factors = ['task_complexity', 'time_pressure', 'interruptions', 'fatigue']
        weights = [0.4, 0.3, 0.2, 0.1]
        load = sum(user_state.get(f, 0) * w for f, w in zip(factors, weights))
        return min(max(load, 0.0), 1.0)

    def _estimate_energy_level(self, user_state):
        """Estimate user energy level"""
        factors = ['time_active', 'break_frequency', 'task_intensity', 'time_of_day']
        weights = [0.3, 0.2, 0.3, 0.2]
        energy = sum(user_state.get(f, 0) * w for f, w in zip(factors, weights))
        return min(max(energy, 0.0), 1.0)

    def _determine_focus_state(self, user_state):
        """Determine user's current focus state"""
        if user_state.get('deep_work_signal', 0) > 0.7:
            return 'flow'
        elif user_state.get('distraction_level', 0) > 0.6:
            return 'distracted'
        return 'neutral'

    def _select_intervention_type(self, context):
        """Select most appropriate intervention type"""
        if context['cognitive_load'] > 0.8:
            return 'micro_break'
        elif context['focus_state'] == 'flow':
            return 'deep_work'
        elif context['energy_level'] < 0.3:
            return 'reflection'
        return 'skill_building'

    def _personalize_content(self, intervention_type):
        """Generate personalized intervention content"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        return {
            'message': self._generate_message(intervention_type, config),
            'difficulty': self._adjust_difficulty(intervention_type),
            'framing': config.get('communication_pref', 'neutral'),
            'supporting_materials': self._select_materials(intervention_type)
        }

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        if context['focus_state'] == 'flow':
            return 'defer'
        elif context['cognitive_load'] > 0.7:
            return 'immediate'
        return 'next_break'

    def _select_delivery_method(self, context):
        """Select appropriate delivery method"""
        if context['interruption_cost'] > 0.8:
            return 'passive'
        elif context['focus_state'] == 'distracted':
            return 'active'
        return 'ambient'

    def _update_effectiveness_metrics(self, interaction_data):
        """Update intervention effectiveness tracking"""
        intervention_type = interaction_data.get('type')
        success = interaction_data.get('success', 0)
        
        if intervention_type in self.user_profile['intervention_effectiveness']:
            current = self.user_profile['intervention_effectiveness'][intervention_type]
            self.user_profile['intervention_effectiveness'][intervention_type] = \
                (current * 0.9) + (success * 0.1)
        else:
            self.user_profile['intervention_effectiveness'][intervention_type] = success

    def _adjust_intervention_parameters(self, interaction_data):
        """Adjust intervention parameters based on effectiveness"""
        intervention_type = interaction_data.get('type')
        if intervention_type in self.intervention_types:
            effectiveness = self.user_profile['intervention_effectiveness'].get(intervention_type, 0.5)
            self.intervention_types[intervention_type]['frequency'] = \
                max(30, min(180, int(self.intervention_types[intervention_type]['frequency'] * (1 + (effectiveness - 0.5)))))