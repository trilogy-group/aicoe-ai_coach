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
                     'success_metric': 'Reduced open windows'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Focus timer started'},
                    {'step': 'Set clear next action',
                     'time_estimate': '3 min', 
                     'success_metric': 'Written task goal'}
                ],
                'follow_up_interval': 30 # minutes
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus', 'stress_signals'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Hydration break',
                     'time_estimate': '3 min',
                     'success_metric': 'Water consumed'},
                    {'step': 'Brief mindfulness exercise',
                     'time_estimate': '5 min',
                     'success_metric': 'Reduced stress markers'}
                ],
                'follow_up_interval': 15
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'competence', 'relatedness'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # User state tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'focus_duration': 0,
            'task_switches': 0,
            'break_intervals': [],
            'productivity_score': 0.0,
            'intervention_responses': {}
        }

    def generate_personalized_intervention(self, user_context, personality_type):
        """Generate contextually relevant intervention based on user state"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current cognitive load
        current_load = self._assess_cognitive_load(user_context)
        
        # Select appropriate intervention
        if current_load > user_config['cognitive_load_threshold']:
            intervention = self._create_break_intervention(user_config)
        else:
            intervention = self._create_focus_intervention(user_config)
            
        # Personalize based on learning style and communication preferences
        intervention = self._personalize_intervention(intervention, user_config)
        
        return intervention

    def _assess_cognitive_load(self, context):
        """Evaluate user's current cognitive load"""
        load_factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruptions': context.get('interruption_frequency', 0.3),
            'task_switching': self.user_state['task_switches'] / 100
        }
        
        return sum(load_factors.values()) / len(load_factors)

    def _create_break_intervention(self, user_config):
        """Generate break recommendation based on user preferences"""
        template = self.intervention_templates['break']
        
        intervention = {
            'type': 'break',
            'urgency': 'high' if self.user_state['focus_duration'] > 90 else 'medium',
            'actions': template['actions'],
            'motivation_hook': self._select_motivation_trigger(user_config),
            'follow_up': template['follow_up_interval']
        }
        
        return intervention

    def _create_focus_intervention(self, user_config):
        """Generate focus enhancement recommendation"""
        template = self.intervention_templates['focus']
        
        intervention = {
            'type': 'focus',
            'urgency': 'high' if self.user_state['task_switches'] > 5 else 'medium',
            'actions': template['actions'],
            'motivation_hook': self._select_motivation_trigger(user_config),
            'follow_up': template['follow_up_interval']
        }
        
        return intervention

    def _select_motivation_trigger(self, user_config):
        """Select appropriate motivation trigger based on user profile"""
        return random.choice(user_config['motivation_triggers'])

    def _personalize_intervention(self, intervention, user_config):
        """Customize intervention delivery based on user preferences"""
        
        # Adjust communication style
        if user_config['communication_pref'] == 'direct':
            intervention['tone'] = 'concise'
            intervention['format'] = 'checklist'
        else:
            intervention['tone'] = 'encouraging'
            intervention['format'] = 'narrative'
            
        # Adapt to learning style
        if user_config['learning_style'] == 'systematic':
            intervention['structure'] = 'sequential'
            intervention['detail_level'] = 'high'
        else:
            intervention['structure'] = 'flexible'
            intervention['detail_level'] = 'moderate'
            
        return intervention

    def update_user_state(self, new_state):
        """Update tracking of user state and intervention effectiveness"""
        self.user_state.update(new_state)
        
        # Analyze intervention effectiveness
        if 'last_intervention' in new_state:
            self.user_state['intervention_responses'][new_state['last_intervention']] = {
                'completion_rate': new_state.get('completion_rate', 0),
                'satisfaction': new_state.get('satisfaction', 0),
                'productivity_impact': new_state.get('productivity_delta', 0)
            }