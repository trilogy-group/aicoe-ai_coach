class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning patterns
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
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'priority': 1,
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Enable do not disturb']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer', 'Use pomodoro method', 'Take structured breaks']}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframing', 'duration': 10, 'priority': 1,
                     'steps': ['Identify barriers', 'Break down task', 'Set micro-goals']},
                    {'type': 'reward_system', 'duration': 5, 'priority': 2,
                     'steps': ['Define reward', 'Set achievement criteria', 'Schedule reward']}
                ],
                'follow_up': {'timing': 60, 'type': 'satisfaction_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['progress', 'feedback', 'social_proof']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized coaching intervention based on user context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        current_context = self._evaluate_context(context)
        
        # Select optimal intervention based on context
        intervention = self._select_intervention(personality_config, current_context)
        
        # Personalize action steps
        actions = self._personalize_actions(intervention['actions'], personality_config)
        
        return {
            'message': self._format_message(actions, personality_config),
            'actions': actions,
            'follow_up': intervention['follow_up']
        }

    def _evaluate_context(self, context):
        """Evaluate current user context for intervention timing"""
        context_score = (
            self.context_factors['time_of_day'][context['time']] *
            self.context_factors['energy_level'][context['energy']] *
            self.context_factors['task_complexity'][context['task_type']]
        )
        
        return {
            'optimal_timing': context_score > 0.6,
            'cognitive_capacity': context_score,
            'intervention_type': 'active' if context_score > 0.7 else 'passive'
        }

    def _select_intervention(self, personality_config, context):
        """Select most appropriate intervention based on personality and context"""
        if context['cognitive_capacity'] < personality_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        return self.intervention_templates['motivation']

    def _personalize_actions(self, actions, personality_config):
        """Customize action steps based on personality preferences"""
        personalized_actions = []
        for action in actions:
            modified_action = action.copy()
            modified_action['steps'] = self._adapt_steps(
                action['steps'],
                personality_config['learning_style'],
                personality_config['communication_pref']
            )
            personalized_actions.append(modified_action)
        return personalized_actions

    def _adapt_steps(self, steps, learning_style, communication_pref):
        """Adapt action steps to user's learning style and communication preferences"""
        adapted_steps = []
        for step in steps:
            if learning_style == 'systematic':
                step = f"Step {len(adapted_steps)+1}: {step}"
            elif learning_style == 'exploratory':
                step = f"Try this: {step}"
                
            if communication_pref == 'direct':
                step = step.replace('Try', 'Do')
            elif communication_pref == 'enthusiastic':
                step = f"{step} 💪"
                
            adapted_steps.append(step)
        return adapted_steps

    def _format_message(self, actions, personality_config):
        """Format coaching message according to personality preferences"""
        message_parts = []
        for action in actions:
            if personality_config['communication_pref'] == 'direct':
                message_parts.append(f"Complete these {len(action['steps'])} steps in {action['duration']} minutes:")
            else:
                message_parts.append(f"Here's a {action['duration']}-minute activity to boost your progress:")
            message_parts.extend(action['steps'])
        
        return "\n".join(message_parts)

    def track_intervention_effectiveness(self, user_id, intervention_id, metrics):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking intervention results
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction patterns"""
        # Implementation for updating user model
        pass