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
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Focus timer started'},
                    {'step': 'Clear workspace',
                     'time_estimate': '3 min', 
                     'success_metric': 'Workspace organized'}
                ],
                'follow_up_interval': 30 # minutes
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus_time'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Hydrate',
                     'time_estimate': '1 min',
                     'success_metric': 'Water consumed'},
                    {'step': 'Deep breathing',
                     'time_estimate': '1 min',
                     'success_metric': 'Breathing exercise done'}
                ],
                'follow_up_interval': 15
            }
            # Additional intervention types
        }

        self.behavioral_metrics = {
            'focus_duration': [],
            'task_completion': [],
            'intervention_response': [],
            'cognitive_load': [],
            'satisfaction_scores': []
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant coaching intervention"""
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate cognitive load and attention state
        current_load = self._assess_cognitive_load(user_context)
        attention_state = self._evaluate_attention_state(user_context)
        
        # Select appropriate intervention based on state
        if current_load > user_config['cognitive_load_threshold']:
            intervention = self.intervention_templates['break']
        elif attention_state == 'scattered':
            intervention = self.intervention_templates['focus']
        
        # Personalize intervention style
        personalized_actions = self._adapt_to_learning_style(
            intervention['actions'],
            user_config['learning_style']
        )
        
        # Format communication style
        message = self._format_message(
            personalized_actions,
            user_config['communication_pref']
        )
        
        return {
            'message': message,
            'actions': personalized_actions,
            'follow_up': intervention['follow_up_interval']
        }

    def track_intervention_effectiveness(self, user_id, intervention_id, metrics):
        """Track and analyze intervention outcomes"""
        for metric, value in metrics.items():
            self.behavioral_metrics[metric].append({
                'user_id': user_id,
                'intervention_id': intervention_id,
                'value': value,
                'timestamp': time.time()
            })
        
        # Analyze effectiveness
        effectiveness = self._calculate_effectiveness(intervention_id)
        
        # Adapt future interventions based on effectiveness
        self._update_intervention_models(effectiveness)
        
        return effectiveness

    def _assess_cognitive_load(self, context):
        """Evaluate current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3),
            'task_switching': context.get('task_switches', 0.4)
        }
        
        weighted_load = sum(factors.values()) / len(factors)
        return min(weighted_load, 1.0)

    def _evaluate_attention_state(self, context):
        """Analyze current attention state"""
        focus_signals = {
            'app_switches': context.get('app_switches', 0),
            'idle_time': context.get('idle_time', 0),
            'active_windows': context.get('active_windows', 1)
        }
        
        if focus_signals['app_switches'] > 10 or \
           focus_signals['idle_time'] > 300 or \
           focus_signals['active_windows'] > 5:
            return 'scattered'
        return 'focused'

    def _adapt_to_learning_style(self, actions, style):
        """Adapt intervention to user's learning style"""
        if style == 'systematic':
            return [self._add_structured_details(action) for action in actions]
        elif style == 'exploratory':
            return [self._add_discovery_elements(action) for action in actions]
        return actions

    def _format_message(self, actions, comm_style):
        """Format intervention message based on communication preference"""
        if comm_style == 'direct':
            return self._create_concise_message(actions)
        elif comm_style == 'enthusiastic':
            return self._create_motivational_message(actions)
        return self._create_default_message(actions)

    def _calculate_effectiveness(self, intervention_id):
        """Calculate intervention effectiveness score"""
        relevant_metrics = [m for m in self.behavioral_metrics['intervention_response'] 
                          if m['intervention_id'] == intervention_id]
        
        if not relevant_metrics:
            return 0.0
            
        completion_rate = sum(m['value'] for m in relevant_metrics) / len(relevant_metrics)
        satisfaction = sum(m['value'] for m in self.behavioral_metrics['satisfaction_scores'][-5:]) / 5
        
        return (completion_rate * 0.7 + satisfaction * 0.3)

    def _update_intervention_models(self, effectiveness):
        """Update intervention models based on effectiveness"""
        if effectiveness < 0.5:
            self._adjust_intervention_parameters()