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
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Set a 25-minute focus timer', 'time_est': '1 min'},
                    {'step': 'Write your next subtask', 'time_est': '3 min'}
                ],
                'success_metrics': ['focused_time', 'task_completion'],
                'follow_up_timing': 30 # minutes
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into 15-minute chunks', 'time_est': '5 min'},
                    {'step': 'Set 3 mini-milestones', 'time_est': '3 min'},
                    {'step': 'Schedule reward after completion', 'time_est': '2 min'}
                ],
                'success_metrics': ['task_initiation', 'milestone_completion'],
                'follow_up_timing': 45
            }
            # Additional intervention types
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_celebration'],
            'habit_formation': ['implementation_intentions', 'habit_stacking', 'environmental_design'],
            'motivation': ['autonomy_support', 'competence_building', 'relatedness']
        }

        self.user_context = {}
        self.intervention_history = []
        self.effectiveness_metrics = {}

    def analyze_user_context(self, user_data):
        """Analyzes user context for personalized interventions"""
        context = {
            'personality_type': user_data.get('personality_type'),
            'current_task': user_data.get('current_task'),
            'energy_level': user_data.get('energy_level', 0.5),
            'focus_level': user_data.get('focus_level', 0.5),
            'cognitive_load': user_data.get('cognitive_load', 0.0),
            'time_of_day': user_data.get('time_of_day'),
            'recent_activity': user_data.get('recent_activity', [])
        }
        
        self.user_context = context
        return context

    def generate_intervention(self, context_data):
        """Generates personalized intervention based on context"""
        personality = self.personality_type_configs[context_data['personality_type']]
        
        # Select appropriate intervention based on context
        if context_data['cognitive_load'] > personality['cognitive_load_threshold']:
            intervention_type = 'focus'
        elif context_data['energy_level'] < 0.4:
            intervention_type = 'motivation'
        
        intervention = self.intervention_templates[intervention_type].copy()
        
        # Personalize based on personality
        intervention['communication_style'] = personality['communication_pref']
        intervention['learning_approach'] = personality['learning_style']
        
        # Add behavioral principles
        intervention['psychological_elements'] = {
            'reinforcement': self._select_reinforcement(personality),
            'habit_support': self._select_habit_support(context_data),
            'motivation_alignment': self._align_motivation(personality)
        }
        
        return intervention

    def track_effectiveness(self, intervention_id, metrics):
        """Tracks intervention effectiveness"""
        self.effectiveness_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion_rate', 0.0),
            'user_satisfaction': metrics.get('user_satisfaction', 0.0),
            'behavior_change': metrics.get('behavior_change', 0.0),
            'time_to_action': metrics.get('time_to_action', 0.0)
        }

    def _select_reinforcement(self, personality):
        """Selects appropriate reinforcement strategies"""
        if personality['communication_pref'] == 'direct':
            return ['progress_metrics', 'achievement_badges', 'streak_tracking']
        return ['social_recognition', 'positive_feedback', 'celebration_moments']

    def _select_habit_support(self, context):
        """Selects context-appropriate habit formation support"""
        time_of_day = context['time_of_day']
        recent_activity = context['recent_activity']
        
        supports = []
        if 'morning' in time_of_day:
            supports.append('morning_routine_integration')
        if len(recent_activity) > 0:
            supports.append('activity_chaining')
            
        return supports

    def _align_motivation(self, personality):
        """Aligns motivation strategies with personality"""
        return [trigger for trigger in personality['motivation_triggers']]

    def schedule_follow_up(self, intervention):
        """Schedules follow-up check for intervention"""
        return {
            'timing': intervention['follow_up_timing'],
            'check_points': ['completion', 'obstacles', 'adjustments_needed'],
            'metrics_to_track': intervention['success_metrics']
        }

    def adapt_to_feedback(self, feedback_data):
        """Adapts intervention strategies based on feedback"""
        if feedback_data['effectiveness'] < 0.5:
            self._adjust_intervention_parameters(feedback_data)
        self._update_effectiveness_models(feedback_data)

    def _adjust_intervention_parameters(self, feedback):
        """Adjusts intervention parameters based on feedback"""
        pass

    def _update_effectiveness_models(self, feedback):
        """Updates effectiveness prediction models"""
        pass