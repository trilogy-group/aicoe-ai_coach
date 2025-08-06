class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced user state tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_state': 'optimal',
            'stress_level': 0.0,
            'receptivity': 1.0
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'time_based': {},
            'context_based': {},
            'state_based': {}
        }

        # Intervention configuration
        self.intervention_settings = {
            'min_interval': 30,  # minutes
            'max_daily': 8,
            'intensity_level': 0.5
        }

    def analyze_user_context(self, user_data):
        """Analyzes user context to determine optimal coaching approach"""
        context = {
            'time_of_day': user_data.get('time'),
            'current_task': user_data.get('task'),
            'location': user_data.get('location'),
            'device': user_data.get('device'),
            'recent_activity': user_data.get('activity_history', [])
        }
        
        return self._evaluate_intervention_timing(context)

    def _evaluate_intervention_timing(self, context):
        """Determines if intervention timing is appropriate"""
        cognitive_load = self._assess_cognitive_load(context)
        receptivity = self._calculate_receptivity(context)
        
        return cognitive_load < 0.7 and receptivity > 0.6

    def generate_personalized_nudge(self, user_profile, context):
        """Generates personalized coaching intervention"""
        personality_config = self.personality_type_configs.get(
            user_profile['personality_type'], 
            self.personality_type_configs['INTJ']
        )

        nudge = {
            'content': self._generate_content(personality_config, context),
            'style': personality_config['communication_pref'],
            'timing': self._optimize_timing(context),
            'intensity': self._calculate_intensity(user_profile),
            'action_steps': self._generate_action_steps(context)
        }

        return self._format_nudge(nudge)

    def _assess_cognitive_load(self, context):
        """Evaluates current cognitive load based on context"""
        factors = {
            'task_complexity': self._evaluate_task_complexity(context['current_task']),
            'time_pressure': self._evaluate_time_pressure(context),
            'interruption_frequency': self._calculate_interruption_rate(context),
            'focus_duration': self._get_focus_duration(context)
        }
        
        return sum(factors.values()) / len(factors)

    def _calculate_receptivity(self, context):
        """Calculates user's likely receptivity to coaching"""
        factors = {
            'time_appropriateness': self._evaluate_time_appropriateness(context['time_of_day']),
            'task_interruptibility': self._evaluate_task_interruptibility(context['current_task']),
            'recent_engagement': self._evaluate_recent_engagement(context['recent_activity'])
        }
        
        return sum(factors.values()) / len(factors)

    def _generate_content(self, personality_config, context):
        """Generates personalized coaching content"""
        learning_style = personality_config['learning_style']
        work_pattern = personality_config['work_pattern']
        
        content_templates = self._get_content_templates(learning_style)
        return self._customize_content(content_templates, work_pattern, context)

    def _generate_action_steps(self, context):
        """Creates specific, actionable recommendations"""
        return [
            {
                'step': 'specific_action',
                'timeframe': 'immediate',
                'effort_level': 'low',
                'expected_outcome': 'measurable_result'
            }
        ]

    def _optimize_timing(self, context):
        """Optimizes intervention timing"""
        return {
            'optimal_time': self._calculate_optimal_time(context),
            'valid_duration': self._calculate_validity_window(context),
            'priority_level': self._calculate_priority(context)
        }

    def _calculate_intensity(self, user_profile):
        """Calculates appropriate intervention intensity"""
        base_intensity = self.intervention_settings['intensity_level']
        user_sensitivity = user_profile.get('coaching_sensitivity', 0.5)
        return min(base_intensity * user_sensitivity, 1.0)

    def _format_nudge(self, nudge):
        """Formats coaching intervention for delivery"""
        return {
            'message': nudge['content'],
            'delivery_style': nudge['style'],
            'timing': nudge['timing'],
            'intensity': nudge['intensity'],
            'actions': nudge['action_steps'],
            'metadata': {
                'version': '2.0',
                'type': 'enhanced_coaching_intervention'
            }
        }

    def update_user_state(self, interaction_data):
        """Updates user state based on interaction data"""
        self.user_state.update({
            'cognitive_load': self._recalculate_cognitive_load(interaction_data),
            'energy_level': self._recalculate_energy(interaction_data),
            'focus_state': self._evaluate_focus_state(interaction_data),
            'stress_level': self._evaluate_stress(interaction_data),
            'receptivity': self._recalculate_receptivity(interaction_data)
        })

    def adapt_strategy(self, performance_metrics):
        """Adapts coaching strategy based on performance"""
        self.intervention_settings.update({
            'intensity_level': self._adjust_intensity(performance_metrics),
            'min_interval': self._adjust_interval(performance_metrics),
            'max_daily': self._adjust_frequency(performance_metrics)
        })