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
                'motivation_triggers': ['novelty', 'connection', 'creativity'],
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
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min work blocks'},
                    {'type': 'tool', 'duration': 15, 'specifics': 'Enable focus mode in {app_name}'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'task_avoidance', 'low_energy'],
                'actions': [
                    {'type': 'reframe', 'duration': 10, 'specifics': 'Break task into smaller 15min segments'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Set specific reward for completion'},
                    {'type': 'accountability', 'duration': 20, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 30, 'type': 'motivation_check'}
            }
            # Additional intervention types
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
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
        """Generate personalized coaching intervention based on context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        
        # Select appropriate intervention template
        template = self._select_intervention(user_context, user_config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], user_config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavioral_principles(actions, user_config)
        
        return {
            'timing': timing_score,
            'actions': enhanced_actions,
            'follow_up': template['follow_up']
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        task_factor = self.context_factors['task_complexity'][context['task']]
        
        return (time_factor + energy_factor + task_factor) / 3

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
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            # Adjust communication style
            action['specifics'] = self._adjust_communication(
                action['specifics'], 
                user_config['communication_pref']
            )
            
            # Adjust to learning style
            action['duration'] = self._adjust_duration(
                action['duration'],
                user_config['learning_style']
            )
            
            personalized.append(action)
        return personalized

    def _apply_behavioral_principles(self, actions, user_config):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            # Add motivation triggers
            action['motivation'] = [
                trigger for trigger in user_config['motivation_triggers']
                if self._is_trigger_relevant(trigger, action)
            ]
            
            # Add habit formation elements
            action['habit_elements'] = {
                element: self._generate_habit_element(element, action)
                for element in self.behavioral_triggers['habit_formation']
            }
            
            enhanced.append(action)
        return enhanced

    def _adjust_communication(self, message, style):
        """Adjust communication style of message"""
        style_adjustments = {
            'direct': lambda m: m.strip().rstrip('.') + '.',
            'enthusiastic': lambda m: m.strip().rstrip('!') + '!'
        }
        return style_adjustments.get(style, lambda m: m)(message)

    def _adjust_duration(self, duration, style):
        """Adjust duration based on learning style"""
        adjustments = {
            'systematic': lambda d: d * 1.2,
            'exploratory': lambda d: d * 0.8
        }
        return int(adjustments.get(style, lambda d: d)(duration))

    def _is_trigger_relevant(self, trigger, action):
        """Check if motivation trigger is relevant for action"""
        return True  # Simplified - implement actual relevance logic

    def _generate_habit_element(self, element, action):
        """Generate habit formation element for action"""
        return f"{element}_{action['type']}"  # Simplified - implement actual generation

    def _calculate_template_fit(self, template, user_config):
        """Calculate how well template matches user preferences"""
        return 0.8  # Simplified - implement actual scoring logic