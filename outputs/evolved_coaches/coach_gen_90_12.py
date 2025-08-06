class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
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
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Focus timer started'},
                    {'step': 'Clear workspace',
                     'time_estimate': '3 min', 
                     'success_metric': 'Desk organized'}
                ],
                'follow_up_interval': 30 # minutes
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus', 'stress'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Deep breathing exercise',
                     'time_estimate': '3 min',
                     'success_metric': 'Breathing cycles done'},
                    {'step': 'Hydrate',
                     'time_estimate': '1 min',
                     'success_metric': 'Water consumed'}
                ],
                'follow_up_interval': 15
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
        """Generate contextually relevant and personalized coaching nudge"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate cognitive load and attention state
        cognitive_load = self._assess_cognitive_load(user_context)
        attention_state = self._analyze_attention_patterns(user_context)
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(
            cognitive_load,
            attention_state,
            config['work_pattern'],
            user_context['current_activity']
        )

        # Personalize communication style
        message = self._format_message(
            intervention,
            config['communication_pref'],
            config['motivation_triggers']
        )

        return {
            'message': message,
            'actions': intervention['actions'],
            'follow_up': intervention['follow_up_interval']
        }

    def _assess_cognitive_load(self, context):
        """Analyze user's current cognitive load"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3),
            'task_switching': context.get('task_switches', 0.4)
        }
        
        weights = {
            'task_complexity': 0.4,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2,
            'task_switching': 0.1
        }

        cognitive_load = sum(factors[k] * weights[k] for k in factors)
        return min(cognitive_load, 1.0)

    def _analyze_attention_patterns(self, context):
        """Analyze user's attention patterns and focus state"""
        focus_signals = {
            'app_switches': context.get('app_switches', 0),
            'focus_duration': context.get('focus_duration', 0),
            'idle_time': context.get('idle_time', 0)
        }
        
        # Calculate attention score
        attention_score = (
            (1 - focus_signals['app_switches']/100) * 0.4 +
            (focus_signals['focus_duration']/3600) * 0.4 +
            (1 - focus_signals['idle_time']/300) * 0.2
        )
        
        return {
            'score': attention_score,
            'state': 'focused' if attention_score > 0.7 else 'distracted'
        }

    def _select_intervention(self, cognitive_load, attention_state, work_pattern, activity):
        """Select most appropriate intervention based on context"""
        if cognitive_load > 0.7:
            return self.intervention_templates['break']
        elif attention_state['state'] == 'distracted':
            return self.intervention_templates['focus']
        # Additional intervention selection logic...
        
        return self.intervention_templates['focus']

    def _format_message(self, intervention, comm_style, motivation_triggers):
        """Format intervention message according to user preferences"""
        templates = {
            'direct': "{action}. This will {benefit}.",
            'enthusiastic': "Ready to level up? Let's {action} and {benefit}!",
            'supportive': "Consider {action} - it could help you {benefit}."
        }
        
        action = intervention['actions'][0]['step']
        benefit = "improve your focus and productivity"
        
        return templates[comm_style].format(
            action=action,
            benefit=benefit
        )

    def track_effectiveness(self, user_response):
        """Track and update intervention effectiveness metrics"""
        self.behavioral_metrics['engagement'] = (
            self.behavioral_metrics['engagement'] * 0.9 +
            user_response['engagement'] * 0.1
        )
        self.behavioral_metrics['completion_rate'] = (
            self.behavioral_metrics['completion_rate'] * 0.9 +
            user_response['completed'] * 0.1
        )
        # Update other metrics...