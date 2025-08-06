class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
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
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Set a 25-minute focus timer', 'time_est': '1 min'},
                    {'step': 'Write your next specific task', 'time_est': '2 min'}
                ],
                'success_metrics': ['focus_duration', 'task_completion'],
                'follow_up_timing': 30 # minutes
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into 15-minute chunks', 'time_est': '5 min'},
                    {'step': 'Set 3 mini-milestones', 'time_est': '3 min'},
                    {'step': 'Schedule reward after completion', 'time_est': '2 min'}
                ],
                'success_metrics': ['task_initiation', 'milestone_completion'],
                'follow_up_timing': 60
            }
            # Additional intervention types
        }

        self.behavioral_principles = {
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'attention': ['focus_duration', 'context_switching', 'cognitive_load'],
            'learning': ['spaced_repetition', 'active_recall', 'elaboration']
        }

    def generate_personalized_intervention(self, user_context, personality_type):
        """Generate personalized coaching intervention based on user context and type"""
        
        user_config = self.personality_type_configs[personality_type]
        current_cognitive_load = self._assess_cognitive_load(user_context)
        
        # Select appropriate intervention based on context and load
        if current_cognitive_load > user_config['cognitive_load_threshold']:
            intervention = self._generate_load_reduction_intervention()
        else:
            intervention = self._select_optimal_intervention(user_context, user_config)

        # Personalize communication style
        intervention = self._adapt_communication_style(
            intervention, 
            user_config['communication_pref']
        )

        return intervention

    def _assess_cognitive_load(self, user_context):
        """Assess current cognitive load based on context factors"""
        load_factors = {
            'active_tasks': 0.2 * user_context.get('num_active_tasks', 0),
            'time_pressure': 0.3 * user_context.get('deadline_proximity', 0),
            'complexity': 0.3 * user_context.get('task_complexity', 0),
            'interruptions': 0.2 * user_context.get('interruption_frequency', 0)
        }
        return sum(load_factors.values())

    def _generate_load_reduction_intervention(self):
        """Generate intervention to reduce cognitive load"""
        return {
            'type': 'load_reduction',
            'priority': 'high',
            'actions': [
                {'step': 'Identify most critical task', 'time_est': '2 min'},
                {'step': 'Defer non-urgent items', 'time_est': '5 min'},
                {'step': 'Create focused work block', 'time_est': '3 min'}
            ],
            'success_metrics': ['perceived_load', 'task_focus']
        }

    def _select_optimal_intervention(self, user_context, user_config):
        """Select best intervention based on context and user preferences"""
        relevant_templates = self._filter_relevant_templates(
            user_context, 
            user_config['learning_style']
        )
        
        return self._prioritize_interventions(
            relevant_templates,
            user_config['motivation_triggers']
        )

    def _adapt_communication_style(self, intervention, comm_style):
        """Adapt intervention language to user's preferred communication style"""
        style_modifiers = {
            'direct': {
                'tone': 'straightforward',
                'detail_level': 'high',
                'emotion_level': 'low'
            },
            'enthusiastic': {
                'tone': 'energetic', 
                'detail_level': 'moderate',
                'emotion_level': 'high'
            }
        }
        
        modifier = style_modifiers[comm_style]
        intervention['communication'] = modifier
        return intervention

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Track and analyze intervention effectiveness"""
        success_metrics = {
            'completion_rate': metrics.get('completed_actions', 0) / metrics.get('total_actions', 1),
            'satisfaction': metrics.get('user_satisfaction', 0),
            'behavior_change': metrics.get('behavior_delta', 0)
        }
        
        self._update_intervention_models(intervention_id, success_metrics)
        return success_metrics

    def _update_intervention_models(self, intervention_id, metrics):
        """Update intervention effectiveness models based on feedback"""
        # Implementation for updating ML models based on intervention outcomes
        pass