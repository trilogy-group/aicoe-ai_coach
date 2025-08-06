class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning patterns
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
                    {'type': 'environment', 'duration': 15, 'priority': 1,
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Put phone away']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer', 'Work in focused sprint', 'Take short break']}
                ],
                'follow_up': {'timing': 30, 'type': 'check_completion'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Challenge assumption', 'Find smaller step']},
                    {'type': 'reward', 'duration': 2, 'priority': 2,
                     'steps': ['Define milestone', 'Choose reward', 'Set timeline']}
                ],
                'follow_up': {'timing': 15, 'type': 'progress_check'}
            }
        }

        # Behavioral psychology components
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
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.6:
            return None  # Skip if poor timing
            
        # Select relevant intervention template
        template = self._select_intervention(user_context, user_config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], user_config)
        
        # Add behavioral psychology elements
        enhanced_actions = self._enhance_with_psychology(actions, user_config)
        
        return {
            'timing': timing_score,
            'actions': enhanced_actions,
            'follow_up': template['follow_up'],
            'motivation_hooks': self._get_motivation_hooks(user_config)
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        task_factor = self.context_factors['task_complexity'][context['task']]
        
        return (time_factor * 0.4 + energy_factor * 0.4 + task_factor * 0.2)

    def _select_intervention(self, context, user_config):
        """Select most appropriate intervention template"""
        # Match context triggers to templates
        matching_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                matching_templates.append((template_name, template))
                
        # Select best match based on user preferences
        return max(matching_templates, 
                  key=lambda x: self._calculate_template_fit(x[1], user_config))[1]

    def _personalize_actions(self, actions, user_config):
        """Customize actions based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = user_config['communication_pref']
            modified_action['pace'] = user_config['work_pattern']
            modified_action['complexity'] = min(action['priority'], 
                                             user_config['cognitive_load_threshold'])
            personalized.append(modified_action)
        return personalized

    def _enhance_with_psychology(self, actions, user_config):
        """Add behavioral psychology elements to actions"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['triggers'] = self._get_behavior_triggers(user_config)
            enhanced_action['reinforcement'] = self._get_reinforcement_strategy(action, user_config)
            enhanced.append(enhanced_action)
        return enhanced

    def _get_motivation_hooks(self, user_config):
        """Generate motivation hooks based on user preferences"""
        return [trigger for trigger in user_config['motivation_triggers']
                if trigger in self.behavior_triggers['motivation']]

    def _get_behavior_triggers(self, user_config):
        """Select appropriate behavioral triggers"""
        return [trigger for trigger in self.behavior_triggers['habit_formation']
                if self._matches_user_style(trigger, user_config)]

    def _get_reinforcement_strategy(self, action, user_config):
        """Define reinforcement strategy for action"""
        return {
            'type': 'immediate' if action['priority'] == 1 else 'delayed',
            'feedback_style': user_config['communication_pref'],
            'reward_alignment': user_config['motivation_triggers'][0]
        }

    def _matches_user_style(self, trigger, user_config):
        """Check if trigger matches user's preferred style"""
        return (trigger in user_config['motivation_triggers'] or
                trigger in self.behavior_triggers['engagement'])