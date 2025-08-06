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
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Enable do-not-disturb']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer', 'Work in focused sprint', 'Take 5min break']}
                ],
                'follow_up': {'timing': '+30min', 'metric': 'focus_score'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Break into smaller steps', 'Set micro-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['Quick exercise', 'Power pose', 'Success visualization']}
                ],
                'follow_up': {'timing': '+15min', 'metric': 'task_progress'}
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 1.2, 'afternoon': 1.0, 'evening': 0.8},
            'energy_level': {'high': 1.2, 'medium': 1.0, 'low': 0.8},
            'task_complexity': {'high': 0.8, 'medium': 1.0, 'low': 1.2},
            'deadline_pressure': {'high': 1.2, 'medium': 1.0, 'low': 0.8}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Calculate context-adjusted intervention timing
        timing_multiplier = self._calculate_context_multiplier(context)
        
        # Select most relevant intervention template
        template = self._select_intervention_template(context['triggers'])
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], personality_config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavioral_principles(actions, user_profile)
        
        return {
            'timing': timing_multiplier,
            'actions': enhanced_actions,
            'follow_up': template['follow_up']
        }

    def _calculate_context_multiplier(self, context):
        """Calculate timing multiplier based on context factors"""
        multiplier = 1.0
        for factor, value in context.items():
            if factor in self.context_factors:
                multiplier *= self.context_factors[factor].get(value, 1.0)
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
                modified_action['steps'] = [f"Creative: {step}" for step in action['steps']]
            personalized.append(modified_action)
        return personalized

    def _apply_behavioral_principles(self, actions, user_profile):
        """Apply behavioral psychology principles to enhance effectiveness"""
        enhanced = []
        for action in actions:
            modified_action = action.copy()
            # Add motivation triggers
            modified_action['motivation'] = self._get_motivation_triggers(user_profile)
            # Add progress tracking
            modified_action['progress_check'] = {
                'timing': f"+{action['duration']}min",
                'metric': 'completion_rate'
            }
            # Add reinforcement
            modified_action['reinforcement'] = {
                'type': 'positive',
                'message': self._generate_reinforcement_message(user_profile)
            }
            enhanced.append(modified_action)
        return enhanced

    def _get_motivation_triggers(self, user_profile):
        """Get personalized motivation triggers"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        return personality_config['motivation_triggers']

    def _generate_reinforcement_message(self, user_profile):
        """Generate personalized reinforcement message"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        if personality_config['communication_pref'] == 'direct':
            return "You've made measurable progress. Keep going."
        else:
            return "Amazing work! You're getting closer to your goals!"