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
                    {'type': 'environment', 'duration': 25, 'specifics': 'Clear workspace, close unnecessary tabs'},
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min work blocks'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful break with stretching'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 achievable sub-goals'},
                    {'type': 'reward', 'duration': 30, 'specifics': 'Define concrete reward for completion'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 120, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 1.2, 'afternoon': 1.0, 'evening': 0.8},
            'energy_level': {'high': 1.3, 'medium': 1.0, 'low': 0.7},
            'task_complexity': {'high': 0.8, 'medium': 1.0, 'low': 1.2}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze context and select appropriate intervention
        context_score = self._evaluate_context(user_context)
        optimal_intervention = self._select_intervention(context_score, user_config)
        
        # Personalize intervention based on user preferences
        personalized_actions = self._personalize_actions(
            optimal_intervention['actions'],
            user_config
        )

        return {
            'intervention_type': optimal_intervention['type'],
            'actions': personalized_actions,
            'timing': self._calculate_optimal_timing(user_context),
            'follow_up': optimal_intervention['follow_up']
        }

    def _evaluate_context(self, context):
        """Evaluate user context for intervention selection"""
        context_score = 1.0
        
        for factor, value in context.items():
            if factor in self.context_factors:
                context_score *= self.context_factors[factor][value]
                
        return context_score

    def _select_intervention(self, context_score, user_config):
        """Select most appropriate intervention based on context and user config"""
        
        # Consider cognitive load threshold
        if context_score < user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
            
        # Check motivation triggers
        if any(trigger in user_config['motivation_triggers'] for trigger in ['mastery', 'achievement']):
            return self.intervention_templates['motivation']
            
        return self.intervention_templates['focus']

    def _personalize_actions(self, actions, user_config):
        """Personalize intervention actions based on user preferences"""
        personalized = []
        
        for action in actions:
            # Adjust communication style
            action['specifics'] = self._adapt_communication(
                action['specifics'], 
                user_config['communication_pref']
            )
            
            # Adjust to learning style
            action['duration'] = self._adapt_duration(
                action['duration'],
                user_config['learning_style']
            )
            
            personalized.append(action)
            
        return personalized

    def _calculate_optimal_timing(self, context):
        """Calculate optimal timing for intervention delivery"""
        base_timing = 30  # Base timing in minutes
        
        # Adjust for time of day
        timing_factor = self.context_factors['time_of_day'][context['time_of_day']]
        
        # Adjust for energy level
        energy_factor = self.context_factors['energy_level'][context['energy_level']]
        
        return int(base_timing * timing_factor * energy_factor)

    def _adapt_communication(self, message, style):
        """Adapt communication style of message"""
        if style == 'direct':
            return message.strip().rstrip('.')  # More concise
        elif style == 'enthusiastic':
            return message + '!'  # More energetic
        return message

    def _adapt_duration(self, duration, learning_style):
        """Adapt duration based on learning style"""
        if learning_style == 'systematic':
            return int(duration * 1.2)  # More time for thorough approach
        elif learning_style == 'exploratory':
            return int(duration * 0.8)  # Less time for flexible approach
        return duration