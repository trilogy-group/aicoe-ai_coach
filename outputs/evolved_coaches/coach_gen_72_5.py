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
                    {'type': 'environment', 'duration': 15, 'specifics': 'Clear workspace of distractions'},
                    {'type': 'technique', 'duration': 25, 'specifics': 'Use Pomodoro timer'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful pause'}
                ],
                'follow_up': {'timing': 30, 'metric': 'focus_duration'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller steps'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define meaningful completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'metric': 'task_completion'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze context
        context_score = self._evaluate_context(user_context)
        
        # Select appropriate intervention
        intervention = self._select_intervention(context_score, user_config)
        
        # Personalize actions
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config,
            context_score
        )

        return {
            'nudge_type': intervention['type'],
            'actions': personalized_actions,
            'timing': self._optimize_timing(user_context),
            'follow_up': intervention['follow_up']
        }

    def _evaluate_context(self, context):
        """Evaluate user context for intervention optimization"""
        score = 0.0
        
        # Weight different context factors
        if context['time_of_day'] in self.context_factors['time_of_day']:
            score += self.context_factors['time_of_day'][context['time_of_day']]
            
        if context['energy'] in self.context_factors['energy_level']:
            score += self.context_factors['energy_level'][context['energy']]
            
        if context['task_complexity'] in self.context_factors['task_complexity']:
            score += self.context_factors['task_complexity'][context['task_complexity']]

        return score / 3.0

    def _select_intervention(self, context_score, user_config):
        """Select most appropriate intervention based on context and user"""
        
        # Match intervention to user's cognitive load threshold
        if context_score > user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        else:
            return self.intervention_templates['motivation']

    def _personalize_actions(self, actions, user_config, context_score):
        """Personalize intervention actions for user"""
        personalized = []
        
        for action in actions:
            # Adjust duration based on context
            adjusted_duration = action['duration'] * context_score
            
            # Modify specifics based on learning style
            modified_specifics = self._adapt_to_style(
                action['specifics'], 
                user_config['learning_style']
            )
            
            personalized.append({
                'type': action['type'],
                'duration': adjusted_duration,
                'specifics': modified_specifics,
                'motivation_hook': self._add_motivation_hook(user_config['motivation_triggers'])
            })
            
        return personalized

    def _optimize_timing(self, context):
        """Optimize intervention timing based on context"""
        base_delay = 15  # minutes
        
        # Adjust for time of day
        tod_factor = self.context_factors['time_of_day'][context['time_of_day']]
        
        # Adjust for energy level
        energy_factor = self.context_factors['energy_level'][context['energy']]
        
        return base_delay * tod_factor * energy_factor

    def _adapt_to_style(self, content, learning_style):
        """Adapt content to user's learning style"""
        if learning_style == 'systematic':
            return f"Step-by-step: {content}"
        else:
            return f"Try this: {content}"

    def _add_motivation_hook(self, triggers):
        """Add motivation hook based on user's triggers"""
        return f"This will help you achieve {triggers[0]} and {triggers[1]}"

    def track_effectiveness(self, nudge_id, user_response):
        """Track effectiveness of interventions"""
        # Implementation for tracking and adapting based on user response
        pass