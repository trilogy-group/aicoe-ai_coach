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
                'motivation_triggers': ['novelty', 'connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types configured similarly
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
                'triggers': ['high_cognitive_load', 'extended_focus_time'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Hydrate',
                     'time_estimate': '1 min',
                     'success_metric': 'Water consumed'},
                    {'step': 'Brief mindfulness exercise',
                     'time_estimate': '3 min',
                     'success_metric': 'Exercise completed'}
                ],
                'follow_up_interval': 5,
                'priority_level': 'medium'
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['progress', 'feedback', 'social']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_activity': [],
            'productivity_metrics': {}
        }

        # User adaptation tracking
        self.user_profile = {
            'personality_type': None,
            'preferred_times': [],
            'effective_interventions': [],
            'completion_rates': {},
            'satisfaction_scores': {},
            'behavioral_changes': {}
        }

    def generate_nudge(self, context, user_state):
        """Generate personalized intervention based on context and user state"""
        
        # Update context awareness
        self.update_context(context)
        
        # Calculate cognitive load
        cognitive_load = self.estimate_cognitive_load(user_state)
        
        # Select appropriate intervention
        intervention = self.select_intervention(cognitive_load, user_state)
        
        # Personalize based on user profile
        personalized_actions = self.personalize_actions(intervention)
        
        # Apply behavioral psychology principles
        enhanced_nudge = self.apply_behavioral_principles(personalized_actions)
        
        return enhanced_nudge

    def update_context(self, context):
        """Update context awareness parameters"""
        self.context_factors.update(context)
        self.analyze_patterns()

    def estimate_cognitive_load(self, user_state):
        """Calculate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'time_pressure': user_state.get('time_pressure', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'task_switching': user_state.get('task_switches', 0.4)
        }
        
        weights = {
            'task_complexity': 0.4,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2,
            'task_switching': 0.1
        }
        
        cognitive_load = sum(factors[k] * weights[k] for k in factors)
        return cognitive_load

    def select_intervention(self, cognitive_load, user_state):
        """Select most appropriate intervention based on current state"""
        if cognitive_load > self.user_profile['personality_type']['cognitive_load_threshold']:
            return self.intervention_templates['break']
        return self.intervention_templates['focus']

    def personalize_actions(self, intervention):
        """Customize intervention actions based on user profile"""
        personalized = intervention.copy()
        
        # Adjust based on user preferences and history
        personalized['actions'] = [
            self.customize_action(action) 
            for action in intervention['actions']
        ]
        
        # Add user-specific motivation triggers
        personalized['motivation'] = [
            trigger for trigger in self.user_profile['personality_type']['motivation_triggers']
        ]
        
        return personalized

    def customize_action(self, action):
        """Customize individual action steps"""
        custom = action.copy()
        
        # Adjust time estimates based on user history
        if action['step'] in self.user_profile['completion_rates']:
            custom['time_estimate'] = self.calculate_personalized_time(action['step'])
            
        # Add alternative approaches based on user preferences
        custom['alternatives'] = self.generate_alternatives(action['step'])
        
        return custom

    def apply_behavioral_principles(self, intervention):
        """Apply behavioral psychology principles to intervention"""
        enhanced = intervention.copy()
        
        # Add habit formation elements
        enhanced['habit_cue'] = self.identify_habit_cue()
        enhanced['habit_reward'] = self.select_reward()
        
        # Add motivation elements
        enhanced['motivation_strategy'] = self.select_motivation_strategy()
        
        # Add engagement elements
        enhanced['engagement_hooks'] = self.generate_engagement_hooks()
        
        return enhanced

    def track_effectiveness(self, intervention_id, metrics):
        """Track intervention effectiveness and update user profile"""
        self.user_profile['completion_rates'][intervention_id] = metrics['completion']
        self.user_profile['satisfaction_scores'][intervention_id] = metrics['satisfaction']
        self.user_profile['behavioral_changes'][intervention_id] = metrics['behavior_change']
        
        self.optimize_interventions()

    def optimize_interventions(self):
        """Optimize intervention strategies based on tracked effectiveness"""
        # Implementation of optimization logic
        pass