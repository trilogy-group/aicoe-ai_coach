class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral factors
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'autonomy', 'achievement'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'social_connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'priority': 1,
                     'steps': ['Clear desk', 'Close unnecessary apps', 'Set timer']},
                    {'type': 'cognitive', 'duration': 5, 'priority': 2, 
                     'steps': ['Deep breath', 'State intention', 'Visualize completion']}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'overwhelm'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'priority': 1,
                     'steps': ['Break task down', 'Set mini-milestone', 'Reward plan']},
                    {'type': 'energy_management', 'duration': 5, 'priority': 2,
                     'steps': ['Stand up', 'Quick exercise', 'Water break']}
                ],
                'follow_up': {'timing': 20, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'interruption_frequency': None,
            'deadline_pressure': None
        }

        # Behavioral tracking
        self.user_metrics = {
            'intervention_response_rate': 0.0,
            'completion_rate': 0.0,
            'satisfaction_score': 0.0,
            'behavioral_change_index': 0.0
        }

    def analyze_user_context(self, context_data):
        """Analyzes current user context for intervention timing"""
        self.context_factors.update(context_data)
        
        cognitive_load = self._calculate_cognitive_load()
        attention_capacity = self._estimate_attention_capacity()
        
        return {
            'cognitive_load': cognitive_load,
            'attention_capacity': attention_capacity,
            'intervention_timing': self._optimal_intervention_timing()
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generates contextually relevant and personalized intervention"""
        personality_config = self.personality_type_configs[user_profile['type']]
        context_analysis = self.analyze_user_context(current_context)
        
        # Select optimal intervention based on context
        intervention = self._select_intervention(
            personality_config,
            context_analysis,
            current_context
        )
        
        # Personalize delivery style
        formatted_intervention = self._format_intervention(
            intervention,
            personality_config['communication_pref']
        )
        
        # Add behavioral reinforcement
        enhanced_intervention = self._add_behavioral_elements(
            formatted_intervention,
            personality_config['motivation_triggers']
        )
        
        return enhanced_intervention

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Tracks and updates intervention effectiveness metrics"""
        self.user_metrics['intervention_response_rate'] = \
            (self.user_metrics['intervention_response_rate'] + metrics['response']) / 2
        self.user_metrics['completion_rate'] = \
            (self.user_metrics['completion_rate'] + metrics['completion']) / 2
        self.user_metrics['satisfaction_score'] = \
            (self.user_metrics['satisfaction_score'] + metrics['satisfaction']) / 2
        self.user_metrics['behavioral_change_index'] = \
            (self.user_metrics['behavioral_change_index'] + metrics['behavior_change']) / 2

    def _calculate_cognitive_load(self):
        """Estimates current cognitive load based on context factors"""
        load_factors = {
            'task_complexity': 0.4,
            'interruption_frequency': 0.3,
            'deadline_pressure': 0.3
        }
        
        cognitive_load = sum(
            self.context_factors[factor] * weight 
            for factor, weight in load_factors.items()
        )
        
        return min(cognitive_load, 1.0)

    def _estimate_attention_capacity(self):
        """Estimates user's current attention capacity"""
        energy_weight = 0.4
        time_weight = 0.3
        context_weight = 0.3
        
        attention_score = (
            self.context_factors['energy_level'] * energy_weight +
            self._get_time_factor() * time_weight +
            (1 - self.context_factors['interruption_frequency']) * context_weight
        )
        
        return min(attention_score, 1.0)

    def _optimal_intervention_timing(self):
        """Determines optimal timing for intervention delivery"""
        cognitive_load = self._calculate_cognitive_load()
        attention_capacity = self._estimate_attention_capacity()
        
        if cognitive_load > 0.8 or attention_capacity < 0.3:
            return 'defer'
        elif cognitive_load < 0.4 and attention_capacity > 0.7:
            return 'immediate'
        else:
            return 'next_break'

    def _select_intervention(self, personality_config, context_analysis, current_context):
        """Selects most appropriate intervention based on context and personality"""
        relevant_templates = [
            template for template in self.intervention_templates.values()
            if any(trigger in current_context['triggers'] 
                  for trigger in template['triggers'])
        ]
        
        if not relevant_templates:
            return self._generate_fallback_intervention()
            
        return max(
            relevant_templates,
            key=lambda x: self._calculate_intervention_fit(
                x, personality_config, context_analysis
            )
        )

    def _format_intervention(self, intervention, communication_style):
        """Formats intervention according to user's preferred communication style"""
        if communication_style == 'direct':
            return self._format_direct(intervention)
        elif communication_style == 'enthusiastic':
            return self._format_enthusiastic(intervention)
        # Additional styles...

    def _add_behavioral_elements(self, intervention, motivation_triggers):
        """Enhances intervention with behavioral psychology elements"""
        enhanced = intervention.copy()
        
        # Add motivation aligned with triggers
        enhanced['motivation'] = self._generate_motivation_prompt(motivation_triggers)
        
        # Add commitment mechanism
        enhanced['commitment'] = self._generate_commitment_prompt()
        
        # Add progress tracking
        enhanced['progress'] = self._generate_progress_tracking()
        
        return enhanced

    def _get_time_factor(self):
        """Calculates time-based attention factor"""
        # Implementation for time-based attention calculation
        pass