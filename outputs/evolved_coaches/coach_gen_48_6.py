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
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro with 25min focused work'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a short walk, stretch'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller milestones'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define concrete reward for completion'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'type': 'milestone_check'}
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
            return None  # Skip if timing isn't optimal

        # Select appropriate intervention template
        template = self._select_intervention_template(user_context, config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._enhance_with_psychology(actions, config['motivation_triggers'])
        
        return {
            'timing': timing_score,
            'actions': enhanced_actions,
            'follow_up': template['follow_up'],
            'success_metrics': self._define_success_metrics(enhanced_actions)
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        task_factor = self.context_factors['task_complexity'][context['task']]
        
        return (time_factor + energy_factor + task_factor) / 3

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        relevant_triggers = [t for t in self.intervention_templates 
                           if any(trigger in context['triggers'] 
                           for trigger in self.intervention_templates[t]['triggers'])]
        
        if not relevant_triggers:
            return self.intervention_templates['focus']  # Default template
            
        return self.intervention_templates[relevant_triggers[0]]

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = config['learning_style']
            modified_action['communication'] = config['communication_pref']
            personalized.append(modified_action)
        return personalized

    def _enhance_with_psychology(self, actions, motivation_triggers):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['motivation'] = {
                'trigger': motivation_triggers[0],
                'reinforcement': self.behavior_triggers['habit_formation'],
                'engagement': self.behavior_triggers['engagement']
            }
            enhanced.append(enhanced_action)
        return enhanced

    def _define_success_metrics(self, actions):
        """Define concrete success metrics for actions"""
        return {
            'completion_rate': {'target': 0.8, 'measure': 'action_steps_completed'},
            'engagement': {'target': 0.7, 'measure': 'time_spent_on_tasks'},
            'effectiveness': {'target': 0.75, 'measure': 'self_reported_progress'}
        }

    def track_intervention_effectiveness(self, intervention_id, user_feedback):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking and analyzing results
        pass

    def adapt_recommendations(self, historical_data):
        """Adapt future recommendations based on historical effectiveness"""
        # Implementation for recommendation adaptation
        pass