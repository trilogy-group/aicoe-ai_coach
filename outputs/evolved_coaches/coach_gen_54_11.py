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
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a short walk, stretch exercises'}
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
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        complexity_factor = self.context_factors['task_complexity'][context['task_complexity']]
        
        return time_factor * energy_factor * complexity_factor

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        current_triggers = self._identify_triggers(context)
        
        best_template = None
        best_match = 0
        
        for template_name, template in self.intervention_templates.items():
            match_score = len(set(template['triggers']) & set(current_triggers))
            if match_score > best_match:
                best_match = match_score
                best_template = template
                
        return best_template

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = config['learning_style']
            modified_action['communication'] = config['communication_pref']
            personalized.append(modified_action)
        return personalized

    def _apply_behavioral_principles(self, actions, motivation_triggers):
        """Enhance actions with behavioral psychology principles"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['triggers'] = self._select_motivation_triggers(motivation_triggers)
            enhanced_action['reinforcement'] = self._generate_reinforcement_strategy()
            enhanced.append(enhanced_action)
        return enhanced

    def _identify_triggers(self, context):
        """Identify relevant behavioral triggers from context"""
        triggers = []
        if context['focus_score'] < 0.6:
            triggers.append('distraction')
        if context['task_switches'] > 5:
            triggers.append('task_switching')
        if context['productivity_score'] < 0.7:
            triggers.append('low_productivity')
        return triggers

    def _select_motivation_triggers(self, available_triggers):
        """Select appropriate motivation triggers"""
        return available_triggers[:2]  # Select top 2 triggers

    def _generate_reinforcement_strategy(self):
        """Generate appropriate reinforcement strategy"""
        return {
            'type': 'positive',
            'schedule': 'variable-ratio',
            'feedback_timing': 'immediate'
        }

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking effectiveness
        pass

    def update_user_model(self, user_id, intervention_results):
        """Update user model based on intervention results"""
        # Implementation for updating user model
        pass