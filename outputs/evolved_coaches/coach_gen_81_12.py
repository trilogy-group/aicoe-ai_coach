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
                'motivation_triggers': ['novelty', 'connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'type': 'environment', 'duration': 5, 'priority': 1,
                     'description': 'Clear visible distractions from workspace',
                     'success_metric': 'Workspace organization score'},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'description': 'Use Pomodoro technique: 25 min focus + 5 min break',
                     'success_metric': 'Complete focus sessions'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'productivity': {
                'triggers': ['procrastination', 'overwhelm'],
                'actions': [
                    {'type': 'planning', 'duration': 10, 'priority': 1,
                     'description': 'Break task into sub-tasks under 30 minutes each',
                     'success_metric': 'Task completion rate'},
                    {'type': 'motivation', 'duration': 5, 'priority': 2,
                     'description': 'Identify and write down task purpose/impact',
                     'success_metric': 'Motivation score'}
                ],
                'follow_up': {'timing': 60, 'type': 'outcome_review'}
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': {
                'positive': ['achievement_celebration', 'progress_visualization'],
                'negative': ['obstacle_removal', 'friction_reduction']
            },
            'habit_formation': {
                'cue': ['context_triggers', 'time_triggers'],
                'routine': ['action_specificity', 'environment_design'],
                'reward': ['immediate_feedback', 'progress_tracking']
            }
        }

        # Cognitive load management
        self.cognitive_thresholds = {
            'max_simultaneous_tasks': 3,
            'max_decision_points': 5,
            'recovery_time': 15,
            'context_switch_cost': 0.2
        }

    def generate_personalized_intervention(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current cognitive load
        cognitive_load = self._assess_cognitive_load(user_context)
        
        if cognitive_load > user_config['cognitive_load_threshold']:
            return self._generate_recovery_intervention(user_context)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(user_context)
        
        # Personalize actions based on user traits
        personalized_actions = self._personalize_actions(
            template['actions'],
            user_config
        )
        
        return {
            'intervention_type': template['triggers'][0],
            'actions': personalized_actions,
            'follow_up': template['follow_up'],
            'motivation_hooks': self._get_motivation_hooks(user_config)
        }

    def _assess_cognitive_load(self, context):
        """Calculate current cognitive load based on context"""
        load = 0
        load += len(context['active_tasks']) / self.cognitive_thresholds['max_simultaneous_tasks']
        load += context['context_switches'] * self.cognitive_thresholds['context_switch_cost']
        return min(load, 1.0)

    def _select_intervention_template(self, context):
        """Select most relevant intervention template for context"""
        # Implementation of template selection logic
        return self.intervention_templates['focus']  # Simplified for example

    def _personalize_actions(self, actions, user_config):
        """Customize actions based on user's personality configuration"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = user_config['communication_pref']
            modified_action['learning_approach'] = user_config['learning_style']
            personalized.append(modified_action)
        return personalized

    def _get_motivation_hooks(self, user_config):
        """Generate motivation hooks based on user's triggers"""
        return [
            {'trigger': trigger, 'principle': self._get_behavior_principle(trigger)}
            for trigger in user_config['motivation_triggers']
        ]

    def _get_behavior_principle(self, trigger):
        """Map motivation trigger to behavioral psychology principle"""
        # Implementation of behavior principle mapping
        return self.behavior_principles['reinforcement']['positive'][0]

    def _generate_recovery_intervention(self, context):
        """Generate intervention for cognitive load recovery"""
        return {
            'intervention_type': 'recovery',
            'actions': [
                {'type': 'break', 'duration': self.cognitive_thresholds['recovery_time'],
                 'description': 'Take a brief mental reset break',
                 'success_metric': 'Perceived mental clarity'}
            ],
            'follow_up': {'timing': 15, 'type': 'load_check'}
        }