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
        }

        # Behavioral psychology components
        self.behavior_triggers = {
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
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_factor = self._calculate_timing_factor(user_context)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(user_context, config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(actions, config['motivation_triggers'])
        
        return {
            'timing': timing_factor,
            'actions': enhanced_actions,
            'follow_up': template['follow_up']
        }

    def _calculate_timing_factor(self, context):
        """Calculate optimal intervention timing based on context"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        complexity_factor = self.context_factors['task_complexity'][context['task_complexity']]
        
        return time_factor * energy_factor * complexity_factor

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        # Match context triggers to template triggers
        matching_templates = []
        for template_name, template in self.intervention_templates.items():
            match_score = sum(1 for trigger in template['triggers'] if trigger in context['triggers'])
            matching_templates.append((template_name, match_score))
        
        # Select best matching template
        best_match = max(matching_templates, key=lambda x: x[1])
        return self.intervention_templates[best_match[0]]

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            # Adjust action based on learning style
            if config['learning_style'] == 'systematic':
                action['specifics'] = self._add_structure(action['specifics'])
            elif config['learning_style'] == 'exploratory':
                action['specifics'] = self._add_flexibility(action['specifics'])
                
            # Adjust communication style
            action['message'] = self._adapt_communication(
                action['specifics'],
                config['communication_pref']
            )
            
            personalized.append(action)
        return personalized

    def _apply_behavior_principles(self, actions, motivation_triggers):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            # Add motivation elements
            action['motivation'] = {
                'trigger': random.choice(motivation_triggers),
                'reinforcement': self._generate_reinforcement(action['type'])
            }
            
            # Add habit formation elements
            action['habit_elements'] = {
                'cue': self._generate_cue(action['type']),
                'routine': action['specifics'],
                'reward': self._generate_reward(action['type'])
            }
            
            enhanced.append(action)
        return enhanced

    def _add_structure(self, specifics):
        """Add structured elements to action specifics"""
        return f"1. {specifics}\n2. Track progress\n3. Review completion"

    def _add_flexibility(self, specifics):
        """Add flexible elements to action specifics"""
        return f"{specifics} (adapt as needed based on your preferences)"

    def _adapt_communication(self, message, style):
        """Adapt communication style of message"""
        if style == 'direct':
            return f"Action required: {message}"
        elif style == 'enthusiastic':
            return f"Exciting opportunity: {message}!"
        return message

    def _generate_reinforcement(self, action_type):
        """Generate appropriate reinforcement strategy"""
        reinforcements = {
            'environment': 'Notice improved focus in organized space',
            'technique': 'Track productivity improvements',
            'break': 'Feel refreshed and energized'
        }
        return reinforcements.get(action_type, 'Observe positive changes')

    def _generate_cue(self, action_type):
        """Generate context-appropriate cue"""
        cues = {
            'environment': 'Starting new task',
            'technique': 'Feeling scattered',
            'break': 'Timer completion'
        }
        return cues.get(action_type, 'Regular check-in')

    def _generate_reward(self, action_type):
        """Generate appropriate reward"""
        rewards = {
            'environment': 'Satisfaction of organized space',
            'technique': 'Improved performance metrics',
            'break': 'Renewed energy'
        }
        return rewards.get(action_type, 'Sense of accomplishment')