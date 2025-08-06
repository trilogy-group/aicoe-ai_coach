class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['novelty', 'social'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Enable focus mode', 'time_est': '1 min'},
                    {'step': 'Set clear work block duration', 'time_est': '1 min'}
                ],
                'success_metrics': ['focused_time', 'task_completion'],
                'follow_up_interval': 30 # minutes
            },
            'productivity': {
                'triggers': ['low_output', 'procrastination'],
                'actions': [
                    {'step': 'Break task into smaller chunks', 'time_est': '5 min'},
                    {'step': 'Set SMART goals for each chunk', 'time_est': '5 min'},
                    {'step': 'Schedule specific work blocks', 'time_est': '3 min'}
                ],
                'success_metrics': ['tasks_completed', 'time_to_completion'],
                'follow_up_interval': 60
            }
            # Additional templates...
        }

        self.behavioral_triggers = {
            'cognitive_load': {
                'threshold': 0.7,
                'indicators': ['task_switching_rate', 'error_rate'],
                'interventions': ['simplify', 'break', 'delegate']
            },
            'motivation': {
                'threshold': 0.5,
                'indicators': ['task_completion_rate', 'engagement_time'],
                'interventions': ['goal_reminder', 'progress_highlight', 'reward']
            }
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Assess current cognitive load
        cognitive_load = self._calculate_cognitive_load(user_context)
        
        # Select appropriate intervention based on load and personality
        if cognitive_load > config['cognitive_load_threshold']:
            intervention = self._get_load_reduction_intervention(config)
        else:
            intervention = self._get_optimization_intervention(config)

        # Personalize delivery style
        intervention = self._personalize_communication(intervention, config)
        
        return self._format_actionable_nudge(intervention)

    def _calculate_cognitive_load(self, context):
        """Estimate current cognitive load from context signals"""
        load_signals = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_rate': context.get('interruption_rate', 0.3),
            'task_switching': context.get('task_switching_rate', 0.4)
        }
        
        # Weighted average of load signals
        weights = {'task_complexity': 0.4, 'time_pressure': 0.3, 
                  'interruption_rate': 0.2, 'task_switching': 0.1}
        
        return sum(load_signals[k] * weights[k] for k in weights)

    def _get_load_reduction_intervention(self, config):
        """Generate intervention to reduce cognitive load"""
        interventions = {
            'systematic': {
                'action': 'Break current task into smaller chunks',
                'rationale': 'Reduce complexity while maintaining systematic approach',
                'steps': ['List subtasks', 'Estimate time for each', 'Prioritize']
            },
            'exploratory': {
                'action': 'Take a strategic break',
                'rationale': 'Reset focus while allowing creative incubation',
                'steps': ['5 min break', 'Quick physical activity', 'Return with fresh perspective']
            }
        }
        return interventions[config['learning_style']]

    def _get_optimization_intervention(self, config):
        """Generate intervention to optimize performance"""
        return {
            'action': self._select_motivation_strategy(config['motivation_drivers']),
            'steps': self._generate_action_steps(config['work_pattern']),
            'metrics': self._define_success_metrics(config['learning_style'])
        }

    def _personalize_communication(self, intervention, config):
        """Adjust intervention language and style to match preferences"""
        style = config['communication_pref']
        if style == 'direct':
            intervention['tone'] = 'clear and concise'
        elif style == 'enthusiastic':
            intervention['tone'] = 'energetic and encouraging'
        
        return intervention

    def _format_actionable_nudge(self, intervention):
        """Format intervention as specific, actionable nudge"""
        return {
            'message': self._construct_message(intervention),
            'action_steps': intervention['steps'],
            'time_estimate': self._calculate_time_estimate(intervention['steps']),
            'success_metrics': intervention.get('metrics', []),
            'follow_up': self._schedule_follow_up(intervention)
        }

    def _select_motivation_strategy(self, drivers):
        """Select motivation strategy based on key drivers"""
        strategies = {
            'mastery': 'Focus on skill development and expertise',
            'autonomy': 'Provide choice and control in approach',
            'novelty': 'Introduce new challenges or techniques',
            'social': 'Incorporate collaborative elements'
        }
        return [strategies[d] for d in drivers]

    def track_intervention_effectiveness(self, nudge, user_response):
        """Track and analyze intervention effectiveness"""
        return {
            'engagement': self._calculate_engagement(user_response),
            'completion': self._verify_action_completion(nudge, user_response),
            'satisfaction': self._measure_satisfaction(user_response),
            'behavioral_change': self._assess_behavior_change(user_response)
        }