class EnhancedAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced factors
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_response': 'analytical',
                'optimal_challenge_level': 'high'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'adaptive',
                'optimal_challenge_level': 'moderate'
            }
            # Additional types configured similarly
        }

        # Evidence-based intervention strategies
        self.intervention_strategies = {
            'habit_formation': {
                'cue_identification': True,
                'routine_design': True,
                'reward_scheduling': True,
                'progress_tracking': True
            },
            'motivation': {
                'goal_setting': True,
                'value_alignment': True,
                'self_efficacy': True,
                'social_proof': True
            },
            'behavioral_change': {
                'implementation_intentions': True,
                'commitment_devices': True,
                'environmental_design': True,
                'accountability': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'available_time': None,
            'priority_tasks': [],
            'recent_progress': {},
            'environmental_conditions': {}
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': {},
            'response_patterns': {},
            'engagement_metrics': {},
            'effectiveness_history': {}
        }

    def analyze_user_context(self, user_data):
        """
        Enhanced context analysis incorporating multiple data points
        """
        context = {
            'current_state': self._assess_current_state(user_data),
            'behavioral_patterns': self._analyze_patterns(user_data),
            'readiness_level': self._evaluate_readiness(user_data),
            'intervention_history': self._get_intervention_history(user_data)
        }
        return self._synthesize_context(context)

    def generate_personalized_nudge(self, user_context, personality_type):
        """
        Creates highly personalized behavioral nudges
        """
        config = self.personality_type_configs[personality_type]
        
        # Select optimal intervention strategy
        strategy = self._select_intervention_strategy(user_context, config)
        
        # Generate specific actionable recommendation
        nudge = self._craft_nudge(strategy, config, user_context)
        
        # Optimize delivery parameters
        delivery = self._optimize_delivery(nudge, user_context)
        
        return {
            'content': nudge,
            'timing': delivery['timing'],
            'channel': delivery['channel'],
            'format': delivery['format']
        }

    def track_intervention_effectiveness(self, intervention_data):
        """
        Enhanced effectiveness tracking and optimization
        """
        metrics = {
            'engagement': self._calculate_engagement(intervention_data),
            'behavior_change': self._measure_behavior_change(intervention_data),
            'user_satisfaction': self._assess_satisfaction(intervention_data),
            'long_term_impact': self._evaluate_impact(intervention_data)
        }
        
        self._update_optimization_parameters(metrics)
        return metrics

    def _select_intervention_strategy(self, context, config):
        """
        Selects optimal intervention strategy based on context and configuration
        """
        strategies = []
        for strategy, params in self.intervention_strategies.items():
            score = self._calculate_strategy_fit(strategy, context, config)
            strategies.append((score, strategy))
        
        return max(strategies, key=lambda x: x[0])[1]

    def _craft_nudge(self, strategy, config, context):
        """
        Creates specific, actionable recommendations
        """
        template = self._get_strategy_template(strategy)
        personalization = self._apply_personality_adaptations(template, config)
        contextualization = self._apply_context_factors(personalization, context)
        
        return self._format_nudge(contextualization)

    def _optimize_delivery(self, nudge, context):
        """
        Optimizes intervention delivery parameters
        """
        return {
            'timing': self._calculate_optimal_timing(context),
            'channel': self._select_best_channel(context),
            'format': self._determine_optimal_format(nudge, context)
        }

    def _update_optimization_parameters(self, metrics):
        """
        Updates system parameters based on intervention effectiveness
        """
        self.timing_optimizer['effectiveness_history'].update(metrics)
        self._recalibrate_intervention_parameters()
        self._update_learning_models()

    def adapt_to_feedback(self, feedback_data):
        """
        Adapts coaching approach based on user feedback
        """
        self._update_user_preferences(feedback_data)
        self._adjust_intervention_strategies(feedback_data)
        self._refine_personalization_models(feedback_data)
        
        return self._generate_adaptation_summary()