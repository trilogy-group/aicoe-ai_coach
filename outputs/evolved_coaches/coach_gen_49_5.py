class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'achievement', 'efficiency'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'creativity', 'social_impact'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'description': 'Enable focus mode for 25 minutes',
                     'time_estimate': 25,
                     'success_metric': 'Completed focused work session',
                     'priority': 'high'
                    },
                    {'description': 'Clear desktop and close unnecessary tabs',
                     'time_estimate': 2,
                     'success_metric': 'Reduced open windows/tabs',
                     'priority': 'medium'
                    }
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus'],
                'actions': [
                    {'description': 'Take a 5 minute walking break',
                     'time_estimate': 5,
                     'success_metric': 'Reduced mental fatigue',
                     'priority': 'high'
                    }
                ],
                'follow_up': {'timing': 7, 'type': 'wellbeing_check'}
            }
            # Additional templates...
        }

        self.behavioral_tracking = {
            'completion_rate': [],
            'engagement_level': [],
            'satisfaction_scores': [],
            'cognitive_load': []
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current context
        cognitive_load = self._assess_cognitive_load(user_context)
        attention_state = self._assess_attention_state(user_context)
        task_urgency = self._assess_task_urgency(user_context)
        
        # Select appropriate intervention
        if cognitive_load > user_config['cognitive_load_threshold']:
            intervention = self.intervention_templates['break']
        elif attention_state == 'scattered':
            intervention = self.intervention_templates['focus']
        
        # Personalize intervention
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config['learning_style'],
            user_config['communication_pref']
        )
        
        # Add motivation elements
        motivation_elements = self._add_motivation_triggers(
            user_config['motivation_triggers']
        )
        
        return {
            'actions': personalized_actions,
            'motivation': motivation_elements,
            'follow_up': intervention['follow_up']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0),
            'time_pressure': context.get('time_pressure', 0),
            'interruption_frequency': context.get('interruptions', 0),
            'task_switching': context.get('task_switches', 0)
        }
        
        weights = {
            'task_complexity': 0.4,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2,
            'task_switching': 0.1
        }
        
        cognitive_load = sum(factors[k] * weights[k] for k in factors)
        return min(cognitive_load, 1.0)

    def _assess_attention_state(self, context):
        """Assess current attention state"""
        focus_signals = {
            'tab_switches': context.get('tab_switches', 0),
            'app_switches': context.get('app_switches', 0),
            'focus_duration': context.get('focus_duration', 0)
        }
        
        if focus_signals['tab_switches'] > 10 or focus_signals['app_switches'] > 5:
            return 'scattered'
        elif focus_signals['focus_duration'] > 45:
            return 'focused'
        return 'neutral'

    def _assess_task_urgency(self, context):
        """Assess task urgency level"""
        deadline = context.get('deadline', None)
        importance = context.get('importance', 0)
        
        if deadline and importance > 0.8:
            return 'high'
        return 'normal'

    def _personalize_actions(self, actions, learning_style, comm_pref):
        """Personalize action steps based on user preferences"""
        personalized = []
        
        for action in actions:
            modified_action = action.copy()
            
            if learning_style == 'systematic':
                modified_action['description'] = f"Step-by-step: {action['description']}"
            elif learning_style == 'exploratory':
                modified_action['description'] = f"Try this: {action['description']}"
                
            if comm_pref == 'direct':
                modified_action['style'] = 'concise'
            elif comm_pref == 'enthusiastic':
                modified_action['style'] = 'encouraging'
                
            personalized.append(modified_action)
            
        return personalized

    def _add_motivation_triggers(self, triggers):
        """Add personalized motivation elements"""
        motivation_messages = {
            'mastery': 'This will help you master your workflow',
            'achievement': 'You're making excellent progress',
            'efficiency': 'This will optimize your productivity',
            'novelty': 'Try this new approach',
            'creativity': 'Here's an innovative solution',
            'social_impact': 'This will help your team succeed'
        }
        
        return [motivation_messages[t] for t in triggers]

    def track_intervention_outcome(self, outcome_data):
        """Track intervention effectiveness"""
        self.behavioral_tracking['completion_rate'].append(
            outcome_data.get('completed', False))
        self.behavioral_tracking['engagement_level'].append(
            outcome_data.get('engagement', 0))
        self.behavioral_tracking['satisfaction_scores'].append(
            outcome_data.get('satisfaction', 0))
        self.behavioral_tracking['cognitive_load'].append(
            outcome_data.get('cognitive_load', 0))