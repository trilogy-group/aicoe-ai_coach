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
                'motivation_triggers': ['novelty', 'social', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'type': 'environment', 'duration': 5, 'priority': 1,
                     'description': 'Clear visible distractions from workspace'},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'description': 'Use Pomodoro technique: 25 min focus + 5 min break'}
                ],
                'follow_up': {'timing': 30, 'type': 'check_completion'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy'],
                'actions': [
                    {'type': 'reframe', 'duration': 2, 'priority': 1,
                     'description': 'Break task into smaller 15-minute chunks'},
                    {'type': 'energize', 'duration': 5, 'priority': 2,
                     'description': 'Take a brief walk to boost energy'}
                ],
                'follow_up': {'timing': 20, 'type': 'progress_check'}
            }
            # Additional templates...
        }

        self.behavioral_metrics = {
            'engagement': 0.0,
            'completion_rate': 0.0,
            'satisfaction': 0.0,
            'behavioral_change': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant coaching nudge"""
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate cognitive load and attention state
        current_load = self._assess_cognitive_load(user_context)
        attention_capacity = self._evaluate_attention_state(user_context)

        # Select appropriate intervention based on context
        intervention = self._select_intervention(
            user_context, 
            current_load,
            attention_capacity,
            user_config
        )

        # Personalize intervention style
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config['learning_style'],
            user_config['communication_pref']
        )

        return {
            'message': self._format_message(personalized_actions, user_config),
            'actions': personalized_actions,
            'follow_up': intervention['follow_up'],
            'metrics': self._generate_success_metrics(personalized_actions)
        }

    def _assess_cognitive_load(self, context):
        """Evaluate current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3),
            'task_familiarity': context.get('familiarity', 0.7)
        }
        return sum(factors.values()) / len(factors)

    def _evaluate_attention_state(self, context):
        """Assess current attention capacity"""
        factors = {
            'time_of_day': context.get('time_factor', 0.8),
            'energy_level': context.get('energy', 0.7),
            'environment': context.get('environment_focus', 0.6)
        }
        return sum(factors.values()) / len(factors)

    def _select_intervention(self, context, cognitive_load, attention, user_config):
        """Select most appropriate intervention based on context"""
        if cognitive_load > user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        elif attention < 0.5:
            return self.intervention_templates['motivation']
        # Additional selection logic...
        return self.intervention_templates['focus']

    def _personalize_actions(self, actions, learning_style, comm_pref):
        """Customize actions based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            if learning_style == 'systematic':
                modified_action['description'] = f"Step-by-step: {action['description']}"
            elif learning_style == 'exploratory':
                modified_action['description'] = f"Try this: {action['description']}"
            
            if comm_pref == 'direct':
                modified_action['tone'] = 'precise'
            elif comm_pref == 'enthusiastic':
                modified_action['tone'] = 'encouraging'
                
            personalized.append(modified_action)
        return personalized

    def _format_message(self, actions, user_config):
        """Format coaching message based on user preferences"""
        message_parts = []
        for action in actions:
            if user_config['communication_pref'] == 'direct':
                message_parts.append(f"- {action['description']} ({action['duration']} min)")
            else:
                message_parts.append(f"💡 {action['description']} (~{action['duration']} min)")
        
        return "\n".join(message_parts)

    def _generate_success_metrics(self, actions):
        """Define measurable success metrics for interventions"""
        return {
            'completion_target': len(actions),
            'time_estimate': sum(a['duration'] for a in actions),
            'priority_actions': len([a for a in actions if a['priority'] == 1])
        }

    def update_metrics(self, user_response):
        """Update behavioral metrics based on user response"""
        self.behavioral_metrics['engagement'] = (
            self.behavioral_metrics['engagement'] * 0.7 + 
            user_response.get('engagement', 0) * 0.3
        )
        # Update other metrics similarly...