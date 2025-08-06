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
                'motivation_triggers': ['novelty', 'social_connection', 'creativity'],
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
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min focused work'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take short walk, stretch exercises'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller achievable steps'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define concrete reward for completion'},
                    {'type': 'accountability', 'duration': 15, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_change_strategies = {
            'habit_formation': {
                'cue': None,
                'routine': None,
                'reward': None,
                'tracking_period': 21,
                'reinforcement_schedule': 'variable_ratio'
            },
            'motivation': {
                'intrinsic_factors': ['autonomy', 'mastery', 'purpose'],
                'extrinsic_factors': ['rewards', 'deadlines', 'accountability'],
                'balance_ratio': 0.7  # Favor intrinsic motivation
            }
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized coaching nudge"""
        
        # Get personality-specific configurations
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current context
        cognitive_load = self._assess_cognitive_load(user_context)
        optimal_timing = self._calculate_intervention_timing(user_context)
        current_triggers = self._identify_active_triggers(user_context)

        # Select appropriate intervention
        intervention = self._select_intervention(current_triggers, cognitive_load)
        
        # Personalize actions based on user preferences
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config['learning_style'],
            user_config['communication_pref']
        )

        # Build structured nudge
        nudge = {
            'timing': optimal_timing,
            'message': self._format_message(personalized_actions, user_config),
            'actions': personalized_actions,
            'follow_up': intervention['follow_up'],
            'success_metrics': self._define_success_metrics(intervention),
            'adaptation_data': {
                'cognitive_load': cognitive_load,
                'context': user_context,
                'personality': personality_type
            }
        }

        return nudge

    def _assess_cognitive_load(self, context):
        """Evaluate current cognitive load based on context"""
        factors = {
            'active_tasks': len(context.get('active_tasks', [])) * 0.2,
            'time_pressure': context.get('deadline_proximity', 0) * 0.3,
            'interruptions': context.get('interruption_frequency', 0) * 0.15,
            'task_complexity': context.get('task_complexity', 0) * 0.35
        }
        return sum(factors.values())

    def _calculate_intervention_timing(self, context):
        """Determine optimal intervention timing"""
        current_load = self._assess_cognitive_load(context)
        task_urgency = context.get('task_urgency', 0)
        focus_state = context.get('focus_level', 0)
        
        if current_load > 0.8:
            return 'defer'
        elif task_urgency > 0.7:
            return 'immediate'
        else:
            return 'next_break'

    def _identify_active_triggers(self, context):
        """Identify relevant intervention triggers from context"""
        triggers = []
        if context.get('focus_level', 1) < 0.6:
            triggers.append('distraction')
        if context.get('task_switches', 0) > 5:
            triggers.append('task_switching')
        if context.get('productivity_rate', 1) < 0.7:
            triggers.append('low_productivity')
        return triggers

    def _personalize_actions(self, actions, learning_style, communication_pref):
        """Customize intervention actions based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            if learning_style == 'systematic':
                modified_action['specifics'] = self._add_structure(action['specifics'])
            if communication_pref == 'direct':
                modified_action['specifics'] = self._make_concise(action['specifics'])
            personalized.append(modified_action)
        return personalized

    def _define_success_metrics(self, intervention):
        """Define measurable success metrics for intervention"""
        return {
            'primary_metric': 'task_completion_rate',
            'secondary_metrics': ['focus_duration', 'interruption_reduction'],
            'measurement_period': 60,  # minutes
            'target_values': {
                'task_completion_rate': 0.8,
                'focus_duration': 45,
                'interruption_reduction': 0.5
            }
        }

    def _format_message(self, actions, user_config):
        """Format coaching message according to user preferences"""
        style = user_config['communication_pref']
        message = f"Based on your current context, here's a {style} recommendation:\n"
        for action in actions:
            message += f"- {action['specifics']} ({action['duration']}min)\n"
        return message