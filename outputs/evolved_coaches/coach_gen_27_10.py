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
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Break into smaller steps', 'Set micro-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['Quick exercise', 'Power pose', 'Success visualization']}
                ],
                'follow_up': {'timing': 15, 'type': 'progress_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_reward', 'progress_tracking', 'streak_maintenance'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3},
            'interruption_frequency': {'high': 0.3, 'medium': 0.6, 'low': 0.9}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(context)
        if timing_score < 0.6:
            return None  # Skip if timing isn't appropriate

        # Select relevant intervention template
        template = self._select_intervention_template(context, personality_config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], personality_config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(actions, user_profile)
        
        return {
            'type': template['type'],
            'actions': enhanced_actions,
            'timing': timing_score,
            'follow_up': template['follow_up']
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time_of_day']]
        energy_factor = self.context_factors['energy_level'][context['energy_level']]
        complexity_factor = self.context_factors['task_complexity'][context['task_complexity']]
        interruption_factor = self.context_factors['interruption_frequency'][context['interruption_frequency']]
        
        return (time_factor + energy_factor + complexity_factor + interruption_factor) / 4

    def _select_intervention_template(self, context, personality_config):
        """Select most appropriate intervention template"""
        relevant_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                relevance_score = self._calculate_template_relevance(template, context, personality_config)
                relevant_templates.append((template_name, relevance_score))
        
        best_template = max(relevant_templates, key=lambda x: x[1])
        return self.intervention_templates[best_template[0]]

    def _personalize_actions(self, actions, personality_config):
        """Personalize action steps based on user preferences"""
        personalized_actions = []
        for action in actions:
            modified_action = action.copy()
            modified_action['steps'] = self._adapt_steps_to_style(
                action['steps'],
                personality_config['learning_style'],
                personality_config['communication_pref']
            )
            personalized_actions.append(modified_action)
        return personalized_actions

    def _apply_behavior_principles(self, actions, user_profile):
        """Apply behavioral psychology principles to enhance effectiveness"""
        enhanced_actions = []
        for action in actions:
            enhanced_action = action.copy()
            # Add immediate rewards
            enhanced_action['reward'] = self._generate_reward(user_profile)
            # Add progress tracking
            enhanced_action['progress_markers'] = self._create_progress_markers(action)
            # Add social proof elements
            enhanced_action['social_proof'] = self._add_social_proof(action, user_profile)
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