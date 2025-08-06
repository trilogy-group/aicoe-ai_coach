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

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_celebration'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy_support', 'competence_building', 'relatedness']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_activity': None
        }

        # User state tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'focus_duration': 0,
            'break_timing': 0,
            'task_completion_rate': 0.0,
            'intervention_response': {}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        
        # Update context awareness
        self.update_context(current_context)
        
        # Calculate cognitive load
        cognitive_load = self.estimate_cognitive_load()
        
        # Select appropriate intervention
        intervention = self.select_intervention(user_profile, cognitive_load)
        
        # Personalize the intervention
        personalized_actions = self.personalize_actions(
            intervention, 
            user_profile['personality_type'],
            cognitive_load
        )
        
        return self.format_nudge(personalized_actions)

    def update_context(self, current_context):
        """Update context awareness parameters"""
        for factor, value in current_context.items():
            if factor in self.context_factors:
                self.context_factors[factor] = value

    def estimate_cognitive_load(self):
        """Calculate current cognitive load based on context and user state"""
        factors = {
            'task_complexity': 0.3,
            'focus_duration': 0.2,
            'environment_distractions': 0.2,
            'energy_level': 0.3
        }
        
        load = sum(
            factors[factor] * self.context_factors.get(factor, 0.5) 
            for factor in factors
        )
        
        return min(load, 1.0)

    def select_intervention(self, user_profile, cognitive_load):
        """Select most appropriate intervention based on user state"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        if cognitive_load > personality_config['cognitive_load_threshold']:
            return self.intervention_templates['break']
        else:
            return self.intervention_templates['focus']

    def personalize_actions(self, intervention, personality_type, cognitive_load):
        """Customize intervention actions based on personality and state"""
        config = self.personality_type_configs[personality_type]
        
        personalized = {
            'actions': [],
            'communication_style': config['communication_pref'],
            'timing': self.optimize_timing(config['work_pattern']),
            'motivation_hooks': self.select_motivation_triggers(config['motivation_triggers'])
        }

        # Adjust action complexity based on cognitive load
        for action in intervention['actions']:
            if cognitive_load > 0.7:
                # Simplify actions when cognitive load is high
                action['time_estimate'] = min(int(action['time_estimate'].split()[0]) * 1.5, 5)
            personalized['actions'].append(action)

        return personalized

    def optimize_timing(self, work_pattern):
        """Optimize intervention timing based on work pattern"""
        timing_map = {
            'deep_focus': {'interval': 45, 'duration': 5},
            'flexible': {'interval': 25, 'duration': 3}
        }
        return timing_map.get(work_pattern, {'interval': 30, 'duration': 4})

    def select_motivation_triggers(self, triggers):
        """Select appropriate motivation hooks based on user profile"""
        return [
            principle for principle in self.behavior_principles['motivation']
            if any(trigger in principle for trigger in triggers)
        ]

    def format_nudge(self, personalized_intervention):
        """Format the intervention for delivery"""
        return {
            'actions': personalized_intervention['actions'],
            'style': personalized_intervention['communication_style'],
            'timing': personalized_intervention['timing'],
            'motivation': personalized_intervention['motivation_hooks'],
            'priority': 'high' if self.user_state['cognitive_load'] > 0.7 else 'medium'
        }

    def track_intervention_response(self, intervention_id, user_response):
        """Track and analyze user response to interventions"""
        self.user_state['intervention_response'][intervention_id] = user_response
        self.adapt_intervention_strategy(user_response)

    def adapt_intervention_strategy(self, response_data):
        """Adapt intervention strategy based on user response patterns"""
        if response_data['completed']:
            self.user_state['task_completion_rate'] += 0.1
        else:
            self.user_state['task_completion_rate'] -= 0.05
            
        self.user_state['task_completion_rate'] = max(0.0, min(1.0, self.user_state['task_completion_rate']))