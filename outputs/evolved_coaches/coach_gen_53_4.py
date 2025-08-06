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
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Put phone away']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer', 'Work in focused sprint', 'Take short break']}
                ],
                'follow_up': {'timing': 30, 'type': 'check_completion'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Break into smaller steps', 'Set mini-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['Quick exercise', 'Power pose', 'Positive visualization']}
                ],
                'follow_up': {'timing': 15, 'type': 'progress_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_change_strategies = {
            'habit_formation': {
                'cue': None,
                'routine': None,
                'reward': None,
                'tracking_period': 21,
                'reinforcement_schedule': 'variable'
            },
            'motivation': {
                'intrinsic_factors': ['autonomy', 'mastery', 'purpose'],
                'extrinsic_factors': ['accountability', 'rewards', 'deadlines']
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

        # User state tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'focus_level': 0.0,
            'motivation_level': 0.0,
            'stress_level': 0.0,
            'progress_metrics': {}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant coaching intervention"""
        
        # Update context awareness
        self._update_context(user_context)
        
        # Get personality-specific config
        user_config = self.personality_type_configs[personality_type]
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(user_context, user_config)
        
        # Personalize intervention
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config,
            self.user_state
        )
        
        return {
            'message': self._format_message(personalized_actions, user_config),
            'actions': personalized_actions,
            'follow_up': intervention['follow_up']
        }

    def _update_context(self, context):
        """Update context awareness parameters"""
        self.context_factors.update(context)
        self._recalculate_user_state()

    def _recalculate_user_state(self):
        """Update user state based on context"""
        # Calculate cognitive load
        self.user_state['cognitive_load'] = self._calculate_cognitive_load()
        
        # Update other state metrics
        self.user_state['focus_level'] = self._calculate_focus_level()
        self.user_state['motivation_level'] = self._calculate_motivation_level()
        self.user_state['stress_level'] = self._calculate_stress_level()

    def _select_intervention(self, context, user_config):
        """Select most appropriate intervention based on context"""
        # Score each intervention type
        intervention_scores = {}
        for intervention_type, template in self.intervention_templates.items():
            score = self._calculate_intervention_fit(
                template, 
                context,
                user_config
            )
            intervention_scores[intervention_type] = score
            
        # Select highest scoring intervention
        best_type = max(intervention_scores.items(), key=lambda x: x[1])[0]
        return self.intervention_templates[best_type]

    def _personalize_actions(self, actions, user_config, state):
        """Customize actions based on user preferences and state"""
        personalized = []
        for action in actions:
            # Adjust duration based on cognitive load
            adjusted_duration = self._adjust_duration(
                action['duration'],
                state['cognitive_load']
            )
            
            # Modify steps based on learning style
            adjusted_steps = self._adjust_steps(
                action['steps'],
                user_config['learning_style']
            )
            
            personalized.append({
                **action,
                'duration': adjusted_duration,
                'steps': adjusted_steps
            })
            
        return personalized

    def _format_message(self, actions, user_config):
        """Format coaching message according to communication preferences"""
        style = user_config['communication_pref']
        
        if style == 'direct':
            return self._format_direct_message(actions)
        elif style == 'enthusiastic':
            return self._format_enthusiastic_message(actions)
        
        return self._format_default_message(actions)

    def track_progress(self, user_id, metric, value):
        """Track user progress on specific metrics"""
        if user_id not in self.user_state['progress_metrics']:
            self.user_state['progress_metrics'][user_id] = {}
            
        self.user_state['progress_metrics'][user_id][metric] = value

    def get_progress_report(self, user_id):
        """Generate progress report with actionable insights"""
        metrics = self.user_state['progress_metrics'].get(user_id, {})
        
        return {
            'metrics': metrics,
            'trends': self._calculate_trends(metrics),
            'recommendations': self._generate_recommendations(metrics)
        }