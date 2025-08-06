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
                'motivation_triggers': ['novelty', 'social', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Enable focus mode', 'time_est': '1 min'},
                    {'step': 'Set timer for focused work', 'time_est': '1 min'}
                ],
                'success_metrics': ['time_on_task', 'task_completion'],
                'follow_up_interval': 30 # minutes
            },
            'productivity': {
                'triggers': ['procrastination', 'low_output'],
                'actions': [
                    {'step': 'Break task into smaller chunks', 'time_est': '5 min'},
                    {'step': 'Set SMART goals', 'time_est': '10 min'},
                    {'step': 'Schedule focused work blocks', 'time_est': '5 min'}
                ],
                'success_metrics': ['tasks_completed', 'quality_score'],
                'follow_up_interval': 60
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['positive', 'negative', 'intermittent'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose']
        }

        self.user_context = {}
        self.intervention_history = []
        self.progress_metrics = {}

    def analyze_user_context(self, user_data):
        """Analyze user context and state for personalized interventions"""
        context = {
            'personality_type': user_data.get('personality_type'),
            'current_task': user_data.get('current_task'),
            'cognitive_load': self._estimate_cognitive_load(user_data),
            'energy_level': self._estimate_energy_level(user_data),
            'time_of_day': user_data.get('timestamp').hour,
            'recent_activity': user_data.get('recent_activity', [])
        }
        self.user_context.update(context)
        return context

    def generate_intervention(self, context_data):
        """Generate personalized intervention based on context"""
        personality_config = self.personality_type_configs[context_data['personality_type']]
        
        # Select appropriate intervention based on context
        intervention_type = self._select_intervention_type(context_data)
        template = self.intervention_templates[intervention_type]
        
        # Personalize intervention
        personalized_actions = self._personalize_actions(
            template['actions'],
            personality_config,
            context_data
        )

        # Apply behavioral principles
        motivation_elements = self._apply_behavioral_principles(
            personality_config['motivation_triggers']
        )

        intervention = {
            'type': intervention_type,
            'actions': personalized_actions,
            'motivation': motivation_elements,
            'timing': self._optimize_timing(context_data),
            'success_metrics': template['success_metrics'],
            'follow_up': template['follow_up_interval']
        }

        self.intervention_history.append(intervention)
        return intervention

    def track_progress(self, intervention_id, metrics):
        """Track intervention effectiveness and user progress"""
        self.progress_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion_rate', 0),
            'satisfaction': metrics.get('satisfaction', 0),
            'behavior_change': metrics.get('behavior_change', 0),
            'timestamp': metrics.get('timestamp')
        }
        
        return self._adjust_intervention_strategy(intervention_id)

    def _estimate_cognitive_load(self, user_data):
        """Estimate current cognitive load based on user activity"""
        factors = {
            'task_complexity': user_data.get('task_complexity', 0.5),
            'interruption_frequency': user_data.get('interruptions', 0.3),
            'time_pressure': user_data.get('deadline_proximity', 0.4)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_energy_level(self, user_data):
        """Estimate user energy level based on activity patterns"""
        factors = {
            'time_active': user_data.get('time_active', 0),
            'task_intensity': user_data.get('task_intensity', 0.5),
            'break_frequency': user_data.get('breaks_taken', 0)
        }
        return self._calculate_energy_score(factors)

    def _personalize_actions(self, actions, personality_config, context):
        """Personalize action steps based on user preferences and context"""
        personalized = []
        for action in actions:
            modified_action = {
                'step': self._adapt_language(
                    action['step'], 
                    personality_config['communication_pref']
                ),
                'time_est': self._adjust_time_estimate(
                    action['time_est'],
                    personality_config['work_pattern']
                ),
                'difficulty': self._calculate_difficulty(action, context)
            }
            personalized.append(modified_action)
        return personalized

    def _apply_behavioral_principles(self, motivation_triggers):
        """Apply behavioral psychology principles to intervention"""
        return {
            'reinforcement_type': self._select_reinforcement(motivation_triggers),
            'habit_elements': self._identify_habit_components(),
            'motivation_factors': self._align_motivation_factors(motivation_triggers)
        }

    def _optimize_timing(self, context):
        """Optimize intervention timing based on user context"""
        return {
            'suggested_time': self._calculate_optimal_time(context),
            'frequency': self._determine_frequency(context),
            'duration': self._calculate_duration(context)
        }

    def _adjust_intervention_strategy(self, intervention_id):
        """Adjust intervention strategy based on progress metrics"""
        metrics = self.progress_metrics[intervention_id]
        
        adjustments = {
            'difficulty': self._adjust_difficulty(metrics),
            'frequency': self._adjust_frequency(metrics),
            'approach': self._adjust_approach(metrics)
        }
        
        return adjustments