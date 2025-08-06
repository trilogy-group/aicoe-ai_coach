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
                     'steps': ['Identify barrier', 'Break into smaller steps', 'Set mini-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['Quick exercise', 'Review progress', 'Visualize outcome']}
                ],
                'follow_up': {'timing': 15, 'type': 'check_progress'}
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
        """Generate personalized intervention based on context and personality"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.6:
            return None  # Skip if poor timing
            
        # Select relevant intervention template
        template = self._select_intervention(user_context, config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(actions, config)
        
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

    def _select_intervention(self, context, config):
        """Select most appropriate intervention template"""
        # Match context triggers to templates
        matching_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                matching_templates.append((template_name, template))
                
        # Select best match based on learning style and current context
        return max(matching_templates, 
                  key=lambda x: self._calculate_template_fit(x[1], config, context))[1]

    def _personalize_actions(self, actions, config):
        """Customize actions based on personality preferences"""
        personalized = []
        for action in actions:
            # Adjust action parameters based on preferences
            modified_action = action.copy()
            modified_action['duration'] *= self._get_duration_modifier(config)
            modified_action['steps'] = self._adapt_steps(action['steps'], config)
            personalized.append(modified_action)
        return personalized

    def _apply_behavior_principles(self, actions, config):
        """Enhance actions with behavioral psychology principles"""
        enhanced = []
        for action in actions:
            # Add motivation triggers
            action['motivation'] = [
                trigger for trigger in config['motivation_triggers']
                if self._is_trigger_relevant(trigger, action)
            ]
            
            # Add habit formation elements
            action['habit_elements'] = {
                'cue': self._generate_cue(action),
                'routine': action['steps'],
                'reward': self._generate_reward(action, config)
            }
            
            enhanced.append(action)
        return enhanced

    def _get_duration_modifier(self, config):
        """Calculate duration modifier based on work pattern"""
        modifiers = {
            'deep_focus': 1.2,
            'flexible': 0.8
        }
        return modifiers.get(config['work_pattern'], 1.0)

    def _adapt_steps(self, steps, config):
        """Adapt action steps to learning style"""
        if config['learning_style'] == 'systematic':
            return [f"Step {i+1}: {step}" for i, step in enumerate(steps)]
        return steps

    def _is_trigger_relevant(self, trigger, action):
        """Check if motivation trigger is relevant for action"""
        return True  # Simplified - implement actual relevance logic

    def _generate_cue(self, action):
        """Generate context-appropriate cue for habit formation"""
        return f"When starting {action['type']}"  # Simplified

    def _generate_reward(self, action, config):
        """Generate personality-appropriate reward"""
        return f"Acknowledge progress in {config['communication_pref']} style"  # Simplified

    def _calculate_template_fit(self, template, config, context):
        """Calculate how well template matches user preferences and context"""
        return 0.8  # Simplified - implement actual scoring logic