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
        enhanced_actions = self._apply_behavioral_principles(actions, config)
        
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
            # Adjust action based on learning style
            if config['learning_style'] == 'systematic':
                action['specifics'] = self._add_structured_steps(action['specifics'])
            elif config['learning_style'] == 'exploratory':
                action['specifics'] = self._add_discovery_options(action['specifics'])
                
            # Adjust communication style
            action['message'] = self._format_message(action['specifics'], config['communication_pref'])
            
            personalized.append(action)
        return personalized

    def _apply_behavioral_principles(self, actions, config):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            # Add motivation triggers
            action['motivation'] = [
                trigger for trigger in config['motivation_triggers']
                if trigger in self.behavior_triggers['motivation']
            ]
            
            # Add habit formation elements
            action['habit_elements'] = {
                'cue': self._generate_cue(action),
                'routine': action['specifics'],
                'reward': self._generate_reward(action, config)
            }
            
            # Adjust for cognitive load
            action['complexity'] = self._assess_complexity(action)
            if action['complexity'] > config['cognitive_load_threshold']:
                action = self._simplify_action(action)
                
            enhanced.append(action)
        return enhanced

    def _add_structured_steps(self, specifics):
        """Add structured steps to action specifics"""
        return f"1. {specifics}\n2. Track progress\n3. Review and adjust"

    def _add_discovery_options(self, specifics):
        """Add exploratory options to action specifics"""
        return f"{specifics} (Try different approaches: A, B, or create your own)"

    def _format_message(self, content, style):
        """Format message according to communication preference"""
        if style == 'direct':
            return f"Action required: {content}"
        return f"Consider trying: {content}"

    def _generate_cue(self, action):
        """Generate environmental or contextual cue"""
        return f"When {action['type']} occurs, initiate the action"

    def _generate_reward(self, action, config):
        """Generate appropriate reward based on user preferences"""
        return f"Reward completion with {config['work_pattern']} appropriate break"

    def _assess_complexity(self, action):
        """Assess cognitive complexity of action"""
        return len(action['specifics'].split()) / 50  # Simple complexity metric

    def _simplify_action(self, action):
        """Simplify action if too complex"""
        action['specifics'] = ' '.join(action['specifics'].split()[:25])
        return action