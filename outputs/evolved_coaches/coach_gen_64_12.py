class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral factors
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
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'difficulty': 'easy'},
                    {'step': 'Enable focus mode for 25 minutes',
                     'time_estimate': '25 min', 
                     'difficulty': 'medium'},
                    {'step': 'Take a 5 minute break',
                     'time_estimate': '5 min',
                     'difficulty': 'easy'}
                ],
                'success_metrics': ['focused_time', 'task_completion'],
                'follow_up_interval': 30 # minutes
            },
            'productivity': {
                'triggers': ['procrastination', 'overwhelm', 'missed_deadlines'],
                'actions': [
                    {'step': 'Break task into smaller subtasks',
                     'time_estimate': '5 min',
                     'difficulty': 'medium'},
                    {'step': 'Prioritize top 3 subtasks',
                     'time_estimate': '3 min',
                     'difficulty': 'easy'},
                    {'step': 'Schedule focused work blocks',
                     'time_estimate': '5 min',
                     'difficulty': 'medium'}
                ],
                'success_metrics': ['tasks_completed', 'on_time_delivery'],
                'follow_up_interval': 60
            }
            # Additional intervention types
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'autonomy': ['choice', 'control', 'ownership'],
            'competence': ['progress', 'mastery', 'achievement'],
            'relatedness': ['connection', 'collaboration', 'recognition']
        }

        # Cognitive load management
        self.cognitive_thresholds = {
            'morning': 0.8,
            'afternoon': 0.7,
            'evening': 0.6
        }

    def generate_personalized_nudge(self, user_context):
        """Generate personalized intervention based on user context"""
        personality = user_context.get('personality_type')
        current_state = user_context.get('current_state')
        time_of_day = user_context.get('time_of_day')
        
        # Get personality-specific config
        user_config = self.personality_type_configs[personality]
        
        # Check cognitive load threshold
        if self._check_cognitive_capacity(time_of_day, current_state):
            # Select appropriate intervention
            intervention = self._select_intervention(current_state, user_config)
            
            # Personalize actions based on user preferences
            personalized_actions = self._personalize_actions(
                intervention['actions'],
                user_config
            )
            
            # Add behavioral psychology elements
            motivation_elements = self._add_motivation_triggers(
                user_config['motivation_triggers']
            )
            
            return {
                'nudge_type': intervention['type'],
                'actions': personalized_actions,
                'motivation': motivation_elements,
                'follow_up': intervention['follow_up_interval']
            }
        else:
            return self._generate_lightweight_nudge()

    def _check_cognitive_capacity(self, time_of_day, current_state):
        """Check if user has cognitive capacity for intervention"""
        threshold = self.cognitive_thresholds[time_of_day]
        current_load = current_state.get('cognitive_load', 0.5)
        return current_load <= threshold

    def _select_intervention(self, current_state, user_config):
        """Select most appropriate intervention based on state and user preferences"""
        # Implementation of intervention selection logic
        pass

    def _personalize_actions(self, actions, user_config):
        """Customize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = user_config['communication_pref']
            modified_action['format'] = user_config['learning_style']
            personalized.append(modified_action)
        return personalized

    def _add_motivation_triggers(self, trigger_types):
        """Add motivation elements based on behavioral psychology"""
        motivation_elements = []
        for trigger in trigger_types:
            if trigger in self.behavior_triggers:
                motivation_elements.extend(self.behavior_triggers[trigger])
        return motivation_elements

    def _generate_lightweight_nudge(self):
        """Generate minimal intervention for high cognitive load periods"""
        return {
            'nudge_type': 'micro',
            'actions': [{'step': 'Take a 2 minute breather',
                        'time_estimate': '2 min',
                        'difficulty': 'easy'}],
            'follow_up': 15
        }

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Track and analyze intervention effectiveness"""
        # Implementation of effectiveness tracking
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation of user model updates
        pass