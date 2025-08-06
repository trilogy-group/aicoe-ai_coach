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
            # Additional types...
        }

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Mode activated'},
                    {'step': 'Set timer for focused work block',
                     'time_estimate': '1 min', 
                     'success_metric': 'Timer started'}
                ],
                'follow_up_window': 25,
                'cognitive_load': 0.3
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines', 'task_confusion'],
                'actions': [
                    {'step': 'Brain dump all tasks',
                     'time_estimate': '5 min',
                     'success_metric': 'Tasks listed'},
                    {'step': 'Prioritize top 3 tasks',
                     'time_estimate': '3 min',
                     'success_metric': 'Priorities set'},
                    {'step': 'Schedule focused blocks',
                     'time_estimate': '5 min',
                     'success_metric': 'Calendar blocked'}
                ],
                'follow_up_window': 60,
                'cognitive_load': 0.5
            }
            # Additional templates...
        }

        self.behavioral_triggers = {
            'time_of_day': ['morning', 'afternoon', 'evening'],
            'energy_level': ['high', 'medium', 'low'],
            'context': ['work', 'learning', 'creative', 'admin'],
            'cognitive_state': ['fresh', 'fatigued', 'overwhelmed']
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Calculate cognitive load and attention capacity
        current_load = self._assess_cognitive_load(context)
        attention_capacity = personality_config['cognitive_load_threshold'] - current_load

        # Select appropriate intervention based on context and capacity
        if attention_capacity < 0.2:
            return self._generate_minimal_intervention(context)
        
        relevant_template = self._select_intervention_template(context, personality_config)
        
        # Personalize intervention based on user preferences
        personalized_actions = self._personalize_actions(
            relevant_template['actions'],
            personality_config,
            user_profile['past_responses']
        )

        return {
            'nudge_type': relevant_template['triggers'][0],
            'actions': personalized_actions,
            'timing': self._optimize_timing(context),
            'follow_up': relevant_template['follow_up_window'],
            'motivation_hooks': self._select_motivation_triggers(personality_config)
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        base_load = 0.4  # Default baseline
        
        load_factors = {
            'task_complexity': context.get('task_complexity', 0.3),
            'time_pressure': context.get('time_pressure', 0.2),
            'interruptions': context.get('interruption_frequency', 0.1),
            'task_switching': context.get('task_switching_rate', 0.2)
        }
        
        return min(sum(load_factors.values()) + base_load, 1.0)

    def _select_intervention_template(self, context, personality_config):
        """Select most appropriate intervention template"""
        relevant_templates = []
        
        for template_name, template in self.intervention_templates.items():
            relevance_score = self._calculate_template_relevance(
                template, context, personality_config
            )
            relevant_templates.append((template_name, template, relevance_score))
            
        return max(relevant_templates, key=lambda x: x[2])[1]

    def _personalize_actions(self, actions, personality_config, past_responses):
        """Personalize action steps based on user preferences and history"""
        personalized = []
        
        for action in actions:
            modified_action = action.copy()
            
            # Adjust language style
            modified_action['step'] = self._adjust_communication_style(
                action['step'], 
                personality_config['communication_pref']
            )
            
            # Adjust time estimates based on past performance
            modified_action['time_estimate'] = self._adjust_time_estimate(
                action['time_estimate'],
                past_responses
            )
            
            personalized.append(modified_action)
            
        return personalized

    def _optimize_timing(self, context):
        """Optimize intervention timing based on context"""
        time_factors = {
            'time_of_day': context.get('time_of_day'),
            'energy_level': context.get('energy_level'),
            'task_urgency': context.get('task_urgency'),
            'last_intervention': context.get('time_since_last_intervention')
        }
        
        return self._calculate_optimal_timing(time_factors)

    def _select_motivation_triggers(self, personality_config):
        """Select appropriate motivation triggers"""
        return [
            trigger for trigger in personality_config['motivation_triggers']
            if self._is_trigger_relevant(trigger)
        ]

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking and analyzing intervention results
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on new interaction data"""
        # Implementation for updating user model
        pass