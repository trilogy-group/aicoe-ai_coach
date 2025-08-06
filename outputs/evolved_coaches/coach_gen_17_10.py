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
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 25, 'specifics': 'Clear workspace, close unnecessary tabs'},
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro with 25min focused work'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a short walk, stretch'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller achievable goals'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define specific reward for completion'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'type': 'achievement_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_intervention(self, user_data, context):
        """Generate personalized coaching intervention based on user data and context"""
        personality_config = self.personality_type_configs[user_data['personality_type']]
        current_context = self._evaluate_context(context)
        
        # Select optimal intervention based on context and personality
        intervention = self._select_intervention(personality_config, current_context)
        
        # Personalize action steps
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            personality_config,
            current_context
        )

        return {
            'intervention_type': intervention['type'],
            'actions': personalized_actions,
            'timing': self._calculate_optimal_timing(current_context),
            'follow_up': intervention['follow_up']
        }

    def _evaluate_context(self, context):
        """Evaluate current context factors for intervention optimization"""
        context_score = {
            'cognitive_load': min(
                context['active_tasks'] * 0.2,
                context['interruptions'] * 0.1,
                1.0
            ),
            'time_pressure': context['deadline_proximity'] * 0.8,
            'environment': context['distraction_level'] * 0.6
        }
        
        return context_score

    def _select_intervention(self, personality_config, context):
        """Select most appropriate intervention based on personality and context"""
        if context['cognitive_load'] > personality_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        elif context['time_pressure'] > 0.7:
            return self.intervention_templates['motivation']
        
        return self._get_default_intervention(personality_config)

    def _personalize_actions(self, actions, personality_config, context):
        """Personalize action steps based on user preferences and context"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            
            # Adjust duration based on cognitive load
            modified_action['duration'] *= (1 - context['cognitive_load'])
            
            # Add personality-specific instructions
            modified_action['specifics'] = self._adapt_instructions(
                action['specifics'],
                personality_config['communication_pref']
            )
            
            personalized.append(modified_action)
            
        return personalized

    def _calculate_optimal_timing(self, context):
        """Calculate optimal timing for intervention delivery"""
        base_delay = 15  # minutes
        
        # Adjust timing based on context
        cognitive_load_factor = 1 + (context['cognitive_load'] * 0.5)
        time_pressure_factor = 1 - (context['time_pressure'] * 0.3)
        
        return int(base_delay * cognitive_load_factor * time_pressure_factor)

    def _adapt_instructions(self, instructions, communication_style):
        """Adapt instruction language based on communication preference"""
        if communication_style == 'direct':
            return instructions  # Already direct format
        elif communication_style == 'enthusiastic':
            return f"Ready for this? {instructions}! You'll do great!"
        
        return instructions

    def _get_default_intervention(self, personality_config):
        """Get default intervention based on personality type"""
        if personality_config['learning_style'] == 'systematic':
            return self.intervention_templates['focus']
        return self.intervention_templates['motivation']

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for effectiveness tracking
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation for user model updates
        pass