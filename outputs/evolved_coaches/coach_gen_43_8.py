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
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_levels': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.6:
            return None  # Skip if timing isn't optimal

        # Select appropriate intervention template
        template = self._select_intervention_template(user_context, config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavioral_principles(actions, config)
        
        return {
            'timing': timing_score,
            'actions': enhanced_actions,
            'follow_up': template['follow_up'],
            'motivation_triggers': self._get_motivation_triggers(config)
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_levels'][context['energy']]
        task_factor = self.context_factors['task_complexity'][context['task']]
        
        return (time_factor * 0.4 + energy_factor * 0.4 + task_factor * 0.2)

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        if 'distraction' in context['challenges']:
            return self.intervention_templates['focus']
        elif 'motivation' in context['challenges']:
            return self.intervention_templates['motivation']
        return self.intervention_templates['focus']  # Default

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = config['learning_style']
            modified_action['communication'] = config['communication_pref']
            personalized.append(modified_action)
        return personalized

    def _apply_behavioral_principles(self, actions, config):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['triggers'] = self.behavior_triggers['habit_formation']
            enhanced_action['motivation_elements'] = self.behavior_triggers['motivation']
            enhanced_action['engagement_factors'] = self.behavior_triggers['engagement']
            enhanced.append(enhanced_action)
        return enhanced

    def _get_motivation_triggers(self, config):
        """Get personalized motivation triggers"""
        return config['motivation_triggers']

    def track_intervention_effectiveness(self, intervention_id, user_feedback):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking effectiveness
        pass

    def adapt_strategies(self, effectiveness_data):
        """Adapt coaching strategies based on effectiveness data"""
        # Implementation for strategy adaptation
        pass