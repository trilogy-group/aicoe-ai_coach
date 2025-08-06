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
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 25, 'specific': 'Clear workspace of distractions'},
                    {'type': 'technique', 'duration': 45, 'specific': 'Use Pomodoro method'},
                    {'type': 'break', 'duration': 5, 'specific': 'Take mindful micro-break'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specific': 'Break task into 3 smaller chunks'},
                    {'type': 'reward', 'duration': 30, 'specific': 'Define meaningful completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specific': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 120, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_change_techniques = {
            'habit_formation': ['implementation_intentions', 'habit_stacking', 'environmental_design'],
            'motivation_enhancement': ['autonomy_support', 'competence_building', 'relatedness'],
            'cognitive_strategies': ['reframing', 'mental_contrasting', 'if_then_planning']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_levels': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze context and cognitive load
        current_load = self._assess_cognitive_load(user_context)
        if current_load > user_config['cognitive_load_threshold']:
            return self._generate_simplified_nudge(user_context)

        # Select appropriate intervention template
        template = self._select_intervention_template(user_context)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], user_config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_techniques(actions, user_config['motivation_triggers'])
        
        return {
            'nudge_type': template['triggers'][0],
            'actions': enhanced_actions,
            'follow_up': template['follow_up'],
            'motivation_elements': self._get_motivation_elements(user_config)
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        load_score = 0.0
        
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_levels'][context['energy']]
        complexity_factor = self.context_factors['task_complexity'][context['task_type']]
        
        load_score = 1 - ((time_factor + energy_factor + complexity_factor) / 3)
        return load_score

    def _select_intervention_template(self, context):
        """Select most appropriate intervention template based on context"""
        for template_name, template in self.intervention_templates.items():
            if context['trigger'] in template['triggers']:
                return template
        return self.intervention_templates['focus']  # Default template

    def _personalize_actions(self, actions, user_config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = user_config['communication_pref']
            modified_action['learning_approach'] = user_config['learning_style']
            personalized.append(modified_action)
        return personalized

    def _apply_behavior_techniques(self, actions, motivation_triggers):
        """Apply behavioral psychology techniques to enhance effectiveness"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['implementation_intention'] = self._generate_implementation_intention(action)
            enhanced_action['motivation_hook'] = self._select_motivation_hook(motivation_triggers)
            enhanced.append(enhanced_action)
        return enhanced

    def _generate_implementation_intention(self, action):
        """Generate specific implementation intention for action"""
        return f"When I {action['trigger']}, I will {action['specific']}"

    def _select_motivation_hook(self, triggers):
        """Select appropriate motivation hook based on user triggers"""
        return {
            'type': triggers[0],
            'message': f"This will help you achieve {triggers[0]}"
        }

    def _get_motivation_elements(self, user_config):
        """Get motivation elements based on user configuration"""
        return {
            'primary_driver': user_config['motivation_triggers'][0],
            'reinforcement_type': user_config['communication_pref'],
            'work_style_alignment': user_config['work_pattern']
        }

    def _generate_simplified_nudge(self, context):
        """Generate simplified nudge for high cognitive load situations"""
        return {
            'nudge_type': 'minimal',
            'actions': [{'type': 'break', 'duration': 5, 'specific': 'Take a short break'}],
            'follow_up': {'timing': 15, 'type': 'quick_check'}
        }