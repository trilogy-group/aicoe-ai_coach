class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced traits and learning patterns
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

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting applications',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Mode activated'},
                    {'step': 'Set timer for focused work block',
                     'time_estimate': '1 min', 
                     'success_metric': 'Timer started'}
                ],
                'follow_up_interval': 25,
                'priority_level': 'high'
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus_period'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Hydrate and rest eyes',
                     'time_estimate': '3 min',
                     'success_metric': 'Break taken'}
                ],
                'follow_up_interval': 5,
                'priority_level': 'medium'
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['progress', 'feedback', 'social_proof']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'interruption_frequency': None,
            'deadline_pressure': None
        }

        # User state tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'focus_duration': 0,
            'break_needed': False,
            'last_intervention': None,
            'intervention_success_rate': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized coaching nudge"""
        
        # Update context awareness
        self.update_context(user_context)
        
        # Select appropriate intervention based on context
        intervention = self.select_intervention()
        
        # Personalize based on personality type
        config = self.personality_type_configs[personality_type]
        
        # Apply behavioral psychology principles
        triggers = self.behavior_triggers
        
        # Generate specific actionable recommendations
        actions = self.get_actions(intervention, config)
        
        return {
            'message': self.format_message(intervention, config),
            'actions': actions,
            'timing': self.optimize_timing(),
            'follow_up': self.schedule_follow_up(intervention)
        }

    def update_context(self, context):
        """Update context awareness parameters"""
        self.context_factors.update(context)
        self.update_user_state()

    def update_user_state(self):
        """Update user state based on context and previous interventions"""
        # Calculate cognitive load
        self.user_state['cognitive_load'] = self.calculate_cognitive_load()
        
        # Check if break needed
        self.user_state['break_needed'] = (
            self.user_state['focus_duration'] > 50 or 
            self.user_state['cognitive_load'] > 0.7
        )

    def select_intervention(self):
        """Select most appropriate intervention based on context"""
        if self.user_state['break_needed']:
            return self.intervention_templates['break']
        
        # Additional intervention selection logic...
        return self.intervention_templates['focus']

    def get_actions(self, intervention, config):
        """Generate specific actionable steps"""
        actions = intervention['actions']
        
        # Personalize actions based on user config
        personalized_actions = []
        for action in actions:
            personalized_action = action.copy()
            personalized_action['style'] = config['learning_style']
            personalized_actions.append(personalized_action)
            
        return personalized_actions

    def optimize_timing(self):
        """Optimize intervention timing based on context"""
        current_load = self.user_state['cognitive_load']
        last_intervention = self.user_state['last_intervention']
        
        # Calculate optimal timing
        if current_load > 0.8:
            return 'immediate'
        elif current_load > 0.6:
            return 'next_break'
        else:
            return 'scheduled'

    def schedule_follow_up(self, intervention):
        """Schedule follow-up check based on intervention type"""
        return {
            'interval': intervention['follow_up_interval'],
            'type': 'check_completion',
            'metrics': [action['success_metric'] for action in intervention['actions']]
        }

    def calculate_cognitive_load(self):
        """Calculate current cognitive load based on context factors"""
        factors = [
            self.context_factors['task_complexity'],
            self.context_factors['interruption_frequency'],
            self.context_factors['deadline_pressure']
        ]
        return sum(filter(None, factors)) / len(factors)

    def format_message(self, intervention, config):
        """Format coaching message based on personality preferences"""
        style = config['communication_pref']
        if style == 'direct':
            return f"Action needed: {intervention['actions'][0]['step']}"
        else:
            return f"Consider taking a moment to {intervention['actions'][0]['step']}"