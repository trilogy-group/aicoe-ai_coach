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
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 25, 'specifics': 'Clear workspace, close unnecessary tabs'},
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min work blocks'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a short walk, stretch exercises'}
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
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 1.2, 'afternoon': 1.0, 'evening': 0.8},
            'energy_level': {'high': 1.3, 'medium': 1.0, 'low': 0.7},
            'task_complexity': {'high': 0.8, 'medium': 1.0, 'low': 1.2}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_factor = self._calculate_timing_factor(user_context)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(user_context, config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavioral_principles(actions, config['motivation_triggers'])
        
        return {
            'timing': timing_factor,
            'actions': enhanced_actions,
            'follow_up': template['follow_up']
        }

    def _calculate_timing_factor(self, context):
        """Calculate optimal intervention timing based on context"""
        time_factor = self.context_factors['time_of_day'][context['time_of_day']]
        energy_factor = self.context_factors['energy_level'][context['energy_level']]
        complexity_factor = self.context_factors['task_complexity'][context['task_complexity']]
        
        return time_factor * energy_factor * complexity_factor

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        # Match context triggers with template triggers
        matched_templates = []
        for template_name, template in self.intervention_templates.items():
            match_score = sum(1 for trigger in template['triggers'] if trigger in context['triggers'])
            matched_templates.append((template_name, match_score, template))
        
        # Return best matching template
        return max(matched_templates, key=lambda x: x[1])[2]

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            # Adjust action parameters based on user configuration
            modified_action = action.copy()
            modified_action['duration'] *= self._get_duration_modifier(config)
            modified_action['specifics'] = self._adapt_specifics(action['specifics'], config)
            personalized.append(modified_action)
        return personalized

    def _apply_behavioral_principles(self, actions, motivation_triggers):
        """Enhance actions with behavioral psychology principles"""
        enhanced = []
        for action in actions:
            # Add motivation triggers
            action['motivation_cues'] = [
                trigger for trigger in motivation_triggers 
                if self._is_relevant_trigger(trigger, action)
            ]
            
            # Add habit formation elements
            action['habit_elements'] = {
                'cue': self._generate_cue(action),
                'routine': action['specifics'],
                'reward': self._generate_reward(action)
            }
            
            enhanced.append(action)
        return enhanced

    def _get_duration_modifier(self, config):
        """Calculate duration modifier based on user preferences"""
        if config['work_pattern'] == 'deep_focus':
            return 1.2
        elif config['work_pattern'] == 'flexible':
            return 0.8
        return 1.0

    def _adapt_specifics(self, specifics, config):
        """Adapt action specifics to user preferences"""
        if config['communication_pref'] == 'direct':
            return specifics + " (Focus on key metrics and outcomes)"
        elif config['communication_pref'] == 'enthusiastic':
            return specifics + " (Emphasize growth and achievement)"
        return specifics

    def _is_relevant_trigger(self, trigger, action):
        """Check if motivation trigger is relevant for action"""
        # Implementation specific to action types
        return True

    def _generate_cue(self, action):
        """Generate appropriate cue for habit formation"""
        return f"When {action['type']} is needed, I will..."

    def _generate_reward(self, action):
        """Generate appropriate reward for completion"""
        return f"After completing {action['type']}, reward with brief break"