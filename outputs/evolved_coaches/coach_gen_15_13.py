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
                'follow_up_timing': 45
            }
            # Additional intervention types
        }

        self.behavioral_metrics = {
            'engagement': 0.0,
            'completion_rate': 0.0,
            'satisfaction': 0.0,
            'behavioral_change': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized coaching nudge"""
        
        # Get user-specific configurations
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current context
        cognitive_load = self._assess_cognitive_load(user_context)
        optimal_timing = self._determine_intervention_timing(user_context)
        relevant_triggers = self._identify_active_triggers(user_context)

        # Select most appropriate intervention
        intervention = self._select_intervention(
            relevant_triggers,
            cognitive_load,
            user_config
        )

        # Personalize the intervention
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config['learning_style'],
            user_config['communication_pref']
        )

        return {
            'timing': optimal_timing,
            'actions': personalized_actions,
            'motivation_hooks': self._generate_motivation_hooks(user_config),
            'success_metrics': intervention['success_metrics'],
            'follow_up': intervention['follow_up_timing']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'active_tasks': len(context.get('active_tasks', [])) * 0.2,
            'time_pressure': context.get('deadline_proximity', 0) * 0.3,
            'interruptions': context.get('interruption_frequency', 0) * 0.2,
            'task_complexity': context.get('task_complexity', 0) * 0.3
        }
        return sum(factors.values())

    def _determine_intervention_timing(self, context):
        """Determine optimal intervention timing"""
        current_focus = context.get('focus_level', 0)
        task_urgency = context.get('task_urgency', 0)
        last_intervention = context.get('time_since_last_intervention', float('inf'))
        
        if current_focus > 0.8 and task_urgency < 0.7:
            return 'defer'
        if last_intervention < 30 and task_urgency < 0.9:
            return 'defer'
        return 'immediate'

    def _identify_active_triggers(self, context):
        """Identify relevant behavioral triggers"""
        triggers = []
        if context.get('focus_level', 1.0) < 0.6:
            triggers.append('distraction')
        if context.get('task_progress', 1.0) < 0.3:
            triggers.append('procrastination')
        if context.get('energy_level', 1.0) < 0.5:
            triggers.append('low_energy')
        return triggers

    def _select_intervention(self, triggers, cognitive_load, user_config):
        """Select most appropriate intervention based on context"""
        matching_interventions = []
        for name, intervention in self.intervention_templates.items():
            if any(trigger in intervention['triggers'] for trigger in triggers):
                matching_interventions.append(intervention)
        
        # Select intervention with appropriate complexity for current cognitive load
        return min(matching_interventions, 
                  key=lambda x: len(x['actions']) * cognitive_load)

    def _personalize_actions(self, actions, learning_style, communication_style):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_step = self._adapt_communication(
                action['step'],
                communication_style
            )
            personalized.append({
                'step': modified_step,
                'time_est': action['time_est'],
                'format': self._adapt_format(learning_style)
            })
        return personalized

    def _generate_motivation_hooks(self, user_config):
        """Generate personalized motivation triggers"""
        return {
            'primary': user_config['motivation_triggers'][0],
            'secondary': user_config['motivation_triggers'][1],
            'reinforcement_interval': 15 # minutes
        }

    def _adapt_communication(self, message, style):
        """Adapt message to user's communication preference"""
        if style == 'direct':
            return message
        elif style == 'enthusiastic':
            return f"{message} 🎯 You've got this!"
        return message

    def _adapt_format(self, learning_style):
        """Adapt content format to learning style"""
        formats = {
            'systematic': 'checklist',
            'exploratory': 'mindmap',
            'visual': 'diagram',
            'practical': 'example'
        }
        return formats.get(learning_style, 'checklist')

    def track_effectiveness(self, user_response):
        """Track intervention effectiveness metrics"""
        self.behavioral_metrics['engagement'] = (
            self.behavioral_metrics['engagement'] * 0.7 +
            user_response.get('engagement', 0) * 0.3
        )
        self.behavioral_metrics['completion_rate'] = (
            self.behavioral_metrics['completion_rate'] * 0.7 +
            user_response.get('completion', 0) * 0.3
        )
        self.behavioral_metrics['satisfaction'] = (
            self.behavioral_metrics['satisfaction'] * 0.7 +
            user_response.get('satisfaction', 0) * 0.3
        )
        self.behavioral_metrics['behavioral_change'] = (
            self.behavioral_metrics['behavioral_change'] * 0.8 +
            user_response.get('behavior_shift', 0) * 0.2
        )