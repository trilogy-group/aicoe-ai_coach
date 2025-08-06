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
                    {'type': 'environment', 'duration': 25, 'specifics': 'Clear workspace, close unnecessary tabs'},
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min work blocks'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a brief walk, stretch exercises'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 achievable sub-goals'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define specific reward for completion'},
                    {'type': 'accountability', 'duration': 15, 'specifics': 'Share goals with accountability partner'}
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
        """Generate personalized intervention based on context and personality"""
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
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        complexity_factor = self.context_factors['task_complexity'][context['task_complexity']]
        
        return time_factor * energy_factor * complexity_factor

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        # Match context triggers to templates
        matching_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                matching_templates.append((template_name, template))
        
        # Select best match based on learning style and cognitive load
        return self._rank_templates(matching_templates, config)[0][1]

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = config['communication_pref']
            modified_action['pacing'] = config['work_pattern']
            personalized.append(modified_action)
        return personalized

    def _apply_behavioral_principles(self, actions, motivation_triggers):
        """Enhance actions with behavioral psychology principles"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['triggers'] = self._select_motivation_triggers(action, motivation_triggers)
            enhanced_action['reinforcement'] = self._generate_reinforcement_strategy(action)
            enhanced.append(enhanced_action)
        return enhanced

    def _select_motivation_triggers(self, action, preferred_triggers):
        """Select appropriate motivation triggers for action"""
        return [trigger for trigger in preferred_triggers 
                if self._is_trigger_relevant(trigger, action)]

    def _generate_reinforcement_strategy(self, action):
        """Generate appropriate reinforcement strategy"""
        return {
            'immediate': f"Acknowledge completion of {action['type']}",
            'delayed': f"Track progress towards {action['type']} mastery",
            'social': f"Share {action['type']} achievement with peers"
        }

    def _rank_templates(self, templates, config):
        """Rank intervention templates by suitability"""
        ranked = []
        for name, template in templates:
            score = self._calculate_template_score(template, config)
            ranked.append((score, template))
        return sorted(ranked, reverse=True)

    def _calculate_template_score(self, template, config):
        """Calculate template suitability score"""
        base_score = 1.0
        if template['actions'][0]['type'] == config['learning_style']:
            base_score *= 1.2
        if len(template['actions']) <= config['cognitive_load_threshold'] * 10:
            base_score *= 1.1
        return base_score