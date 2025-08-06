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
                'motivation_triggers': ['novelty', 'social', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 25, 'specifics': 'Clear workspace, close unnecessary tabs'},
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min focused work'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take short walk, stretch exercises'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 15, 'specifics': 'Break task into 3 smaller achievable goals'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define specific reward for completion'},
                    {'type': 'accountability', 'duration': 10, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['progress', 'feedback', 'social_proof']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 1.2, 'afternoon': 1.0, 'evening': 0.8},
            'energy_level': {'high': 1.2, 'medium': 1.0, 'low': 0.8},
            'task_complexity': {'high': 0.8, 'medium': 1.0, 'low': 1.2}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized coaching intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Calculate optimal intervention timing
        timing_multiplier = self._calculate_timing_multiplier(context)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(context['triggers'], personality_config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], personality_config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavioral_principles(actions, user_profile)
        
        return {
            'timing': timing_multiplier,
            'actions': enhanced_actions,
            'follow_up': template['follow_up']
        }

    def _calculate_timing_multiplier(self, context):
        """Calculate optimal timing for intervention delivery"""
        time_factor = self.context_factors['time_of_day'][context['time_of_day']]
        energy_factor = self.context_factors['energy_level'][context['energy_level']]
        complexity_factor = self.context_factors['task_complexity'][context['task_complexity']]
        
        return time_factor * energy_factor * complexity_factor

    def _select_intervention_template(self, triggers, personality_config):
        """Select most appropriate intervention template based on triggers and personality"""
        matching_templates = []
        for template_name, template in self.intervention_templates.items():
            match_score = len(set(triggers) & set(template['triggers']))
            if match_score > 0:
                matching_templates.append((template_name, template, match_score))
        
        return max(matching_templates, key=lambda x: x[2])[1]

    def _personalize_actions(self, actions, personality_config):
        """Personalize action steps based on personality configuration"""
        personalized_actions = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality_config['communication_pref']
            modified_action['learning_approach'] = personality_config['learning_style']
            personalized_actions.append(modified_action)
        return personalized_actions

    def _apply_behavioral_principles(self, actions, user_profile):
        """Enhance actions with behavioral psychology principles"""
        enhanced_actions = []
        for action in actions:
            enhanced_action = action.copy()
            # Add motivation triggers
            enhanced_action['motivation_elements'] = [
                trigger for trigger in self.behavior_triggers['motivation']
                if trigger in user_profile['motivation_preferences']
            ]
            # Add habit formation elements
            enhanced_action['habit_elements'] = self.behavior_triggers['habit_formation']
            enhanced_actions.append(enhanced_action)
        return enhanced_actions

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking intervention outcomes
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation for updating user model
        pass