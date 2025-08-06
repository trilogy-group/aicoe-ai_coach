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
                     'steps': ['Clear desk', 'Put phone on DND', 'Close unnecessary tabs']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer for 25 min', 'Work on single task', 'Take 5 min break']}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify specific barrier', 'Break task into smaller steps', 'Set micro-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['2-min movement break', 'Deep breathing', 'Review task purpose']}
                ],
                'follow_up': {'timing': 15, 'type': 'motivation_check'}
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 1.2, 'afternoon': 1.0, 'evening': 0.8},
            'energy_level': {'high': 1.2, 'medium': 1.0, 'low': 0.8},
            'task_complexity': {'high': 0.8, 'medium': 1.0, 'low': 1.2},
            'interruption_frequency': {'high': 0.7, 'medium': 1.0, 'low': 1.3}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Calculate context-adjusted intervention timing
        timing_multiplier = self._calculate_context_multiplier(context)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(context['triggers'])
        
        # Personalize actions based on user profile
        actions = self._personalize_actions(template['actions'], personality_config)
        
        # Apply cognitive load adjustments
        adjusted_actions = self._adjust_for_cognitive_load(
            actions,
            context['current_load'],
            personality_config['cognitive_load_threshold']
        )

        return {
            'timing': timing_multiplier,
            'actions': adjusted_actions,
            'follow_up': template['follow_up'],
            'motivation_hooks': self._get_motivation_hooks(personality_config)
        }

    def _calculate_context_multiplier(self, context):
        """Calculate timing multiplier based on context factors"""
        multiplier = 1.0
        for factor, value in context.items():
            if factor in self.context_factors:
                multiplier *= self.context_factors[factor][value]
        return multiplier

    def _select_intervention_template(self, triggers):
        """Select most appropriate intervention template based on triggers"""
        for template_name, template in self.intervention_templates.items():
            if any(trigger in template['triggers'] for trigger in triggers):
                return template
        return self.intervention_templates['focus']  # Default template

    def _personalize_actions(self, actions, personality_config):
        """Personalize action steps based on personality configuration"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            if personality_config['learning_style'] == 'systematic':
                modified_action['steps'] = [f"Detailed: {step}" for step in action['steps']]
            elif personality_config['learning_style'] == 'exploratory':
                modified_action['steps'] = [f"Flexible: {step}" for step in action['steps']]
            personalized.append(modified_action)
        return personalized

    def _adjust_for_cognitive_load(self, actions, current_load, threshold):
        """Adjust actions based on cognitive load considerations"""
        if current_load > threshold:
            # Simplify and reduce actions when cognitive load is high
            return [action for action in actions if action['priority'] == 1]
        return actions

    def _get_motivation_hooks(self, personality_config):
        """Generate motivation hooks based on personality triggers"""
        return [
            {'trigger': trigger, 'intensity': 0.8}
            for trigger in personality_config['motivation_triggers']
        ]

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking and analyzing intervention outcomes
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation for updating user model
        pass