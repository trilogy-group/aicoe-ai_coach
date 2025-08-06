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
                'motivation_triggers': ['novelty', 'social_connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'priority': 1,
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Enable do-not-disturb']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer', 'Use Pomodoro method', 'Take structured breaks']}
                ],
                'success_metrics': ['focus_duration', 'task_completion_rate']
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'priority': 1,
                     'steps': ['Break task into smaller chunks', 'Set SMART goals', 'Visualize outcome']},
                    {'type': 'reward_system', 'duration': 5, 'priority': 2,
                     'steps': ['Define milestone rewards', 'Track progress', 'Celebrate wins']}
                ],
                'success_metrics': ['task_initiation_speed', 'completion_rate']
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.6:
            return None  # Skip intervention if timing isn't optimal

        # Select most relevant intervention
        intervention = self._select_intervention(user_context, config)
        
        # Personalize action steps
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            config['learning_style'],
            user_context['current_capacity']
        )

        return {
            'type': intervention['type'],
            'actions': personalized_actions,
            'timing': self._get_optimal_timing(user_context),
            'success_metrics': intervention['success_metrics'],
            'follow_up': self._generate_follow_up_plan(intervention)
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal timing score based on context factors"""
        time_factor = self.context_factors['time_of_day'][context['time_of_day']]
        energy_factor = self.context_factors['energy_level'][context['energy_level']]
        complexity_factor = self.context_factors['task_complexity'][context['task_complexity']]
        
        return (time_factor + energy_factor + complexity_factor) / 3

    def _select_intervention(self, context, config):
        """Select most appropriate intervention based on context and user config"""
        relevant_interventions = []
        for intervention_type, details in self.intervention_templates.items():
            relevance_score = self._calculate_relevance(context, details['triggers'])
            if relevance_score > 0.7:
                relevant_interventions.append((intervention_type, details, relevance_score))
        
        return max(relevant_interventions, key=lambda x: x[2])[1]

    def _personalize_actions(self, actions, learning_style, capacity):
        """Personalize action steps based on learning style and current capacity"""
        personalized = []
        for action in actions:
            if capacity >= action['priority']:
                modified_action = action.copy()
                modified_action['steps'] = self._adapt_steps(
                    action['steps'],
                    learning_style
                )
                personalized.append(modified_action)
        return personalized

    def _adapt_steps(self, steps, learning_style):
        """Adapt steps based on learning style"""
        if learning_style == 'systematic':
            return [f"Step {i+1}: {step}" for i, step in enumerate(steps)]
        else:
            return [f"Try this: {step}" for step in steps]

    def _get_optimal_timing(self, context):
        """Calculate optimal timing for intervention delivery"""
        return {
            'delay': self._calculate_delay(context),
            'frequency': self._calculate_frequency(context),
            'duration': self._calculate_duration(context)
        }

    def _generate_follow_up_plan(self, intervention):
        """Generate follow-up plan for intervention"""
        return {
            'check_points': [1, 3, 7],  # Days
            'metrics': intervention['success_metrics'],
            'adjustment_triggers': ['completion_rate', 'engagement_level']
        }

    def track_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for effectiveness tracking
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation for user model updates
        pass