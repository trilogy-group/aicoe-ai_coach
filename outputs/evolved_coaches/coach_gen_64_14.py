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
                    {'step': 'Write your next specific task', 'time_est': '2 min'}
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
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_rewards'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof']
        }

        self.user_context = {}
        self.intervention_history = []
        self.success_metrics = {}

    def analyze_user_context(self, user_data):
        """Analyzes user context and current state"""
        context = {
            'personality_type': user_data.get('personality_type'),
            'current_task': user_data.get('current_task'),
            'energy_level': user_data.get('energy_level', 0.0),
            'focus_level': user_data.get('focus_level', 0.0),
            'cognitive_load': user_data.get('cognitive_load', 0.0),
            'time_of_day': user_data.get('time_of_day'),
            'recent_activity': user_data.get('recent_activity', [])
        }
        
        self.user_context = context
        return context

    def generate_personalized_intervention(self):
        """Generates personalized coaching intervention"""
        personality_config = self.personality_type_configs.get(
            self.user_context['personality_type']
        )
        
        # Select appropriate intervention based on context
        intervention_type = self._select_intervention_type()
        template = self.intervention_templates[intervention_type]
        
        # Personalize intervention
        personalized_actions = self._personalize_actions(
            template['actions'], 
            personality_config
        )
        
        intervention = {
            'type': intervention_type,
            'actions': personalized_actions,
            'timing': self._optimize_timing(),
            'motivation_elements': self._add_motivation_elements(personality_config),
            'success_metrics': template['success_metrics'],
            'follow_up': template['follow_up_timing']
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _select_intervention_type(self):
        """Selects most appropriate intervention type based on context"""
        context = self.user_context
        
        if context['focus_level'] < 0.6:
            return 'focus'
        elif context['energy_level'] < 0.5:
            return 'motivation'
        # Additional selection logic
        
        return 'focus'  # default

    def _personalize_actions(self, actions, personality_config):
        """Personalizes action steps based on user's personality and preferences"""
        personalized = []
        
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality_config['communication_pref']
            modified_action['complexity'] = self._adjust_complexity(
                personality_config['cognitive_load_threshold']
            )
            personalized.append(modified_action)
            
        return personalized

    def _optimize_timing(self):
        """Optimizes intervention timing based on user context"""
        context = self.user_context
        
        # Consider time of day, recent activity, and cognitive load
        optimal_time = self._calculate_optimal_time(
            context['time_of_day'],
            context['recent_activity'],
            context['cognitive_load']
        )
        
        return optimal_time

    def _add_motivation_elements(self, personality_config):
        """Adds personalized motivation elements"""
        return {
            'triggers': personality_config['motivation_triggers'],
            'reinforcement_type': self._select_reinforcement_type(personality_config),
            'framing': self._personalize_framing(personality_config)
        }

    def track_intervention_success(self, intervention_id, metrics):
        """Tracks success metrics for interventions"""
        self.success_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion_rate', 0.0),
            'user_satisfaction': metrics.get('user_satisfaction', 0.0),
            'behavior_change': metrics.get('behavior_change', 0.0),
            'timestamp': metrics.get('timestamp')
        }

    def adapt_strategy(self):
        """Adapts coaching strategy based on success metrics"""
        recent_metrics = self._analyze_recent_metrics()
        
        # Adjust intervention parameters based on success patterns
        self._update_intervention_templates(recent_metrics)
        self._adjust_timing_patterns(recent_metrics)
        self._refine_motivation_strategies(recent_metrics)

    def _calculate_optimal_time(self, time_of_day, recent_activity, cognitive_load):
        """Helper method to calculate optimal intervention timing"""
        # Implementation of timing optimization logic
        pass

    def _adjust_complexity(self, threshold):
        """Helper method to adjust action complexity"""
        # Implementation of complexity adjustment logic
        pass