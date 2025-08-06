class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_response': 'analytical',
                'energy_management': 'recharge_alone'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'social',
                'energy_management': 'recharge_socially'
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
                'confidence_building': True,
                'obstacle_planning': True
            },
            'behavioral_change': {
                'tiny_habits': True,
                'implementation_intentions': True,
                'environmental_design': True,
                'social_accountability': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'current_goals': [],
            'recent_progress': {},
            'environmental_conditions': {}
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_times': [],
            'do_not_disturb': [],
            'frequency_caps': {},
            'response_rates': {}
        }

    def generate_personalized_nudge(self, user_id, context):
        """
        Generate highly personalized behavioral nudge based on user context
        """
        # Get user profile and preferences
        user_profile = self._get_user_profile(user_id)
        personality_config = self.personality_type_configs[user_profile['personality_type']]

        # Analyze current context
        current_context = self._analyze_context(context)
        
        # Select optimal intervention strategy
        strategy = self._select_intervention_strategy(
            personality_config,
            current_context,
            user_profile['goals']
        )

        # Generate specific actionable recommendation
        nudge = self._create_targeted_nudge(
            strategy,
            personality_config,
            current_context
        )

        return nudge

    def _analyze_context(self, context):
        """
        Analyze user context for optimal intervention timing and content
        """
        analyzed_context = {
            'cognitive_load': self._estimate_cognitive_load(context),
            'attention_availability': self._check_attention_availability(context),
            'emotional_state': self._detect_emotional_state(context),
            'environmental_factors': self._assess_environment(context),
            'progress_status': self._evaluate_progress(context)
        }
        return analyzed_context

    def _select_intervention_strategy(self, personality_config, context, goals):
        """
        Select the most appropriate intervention strategy based on multiple factors
        """
        strategy = {
            'approach': self._match_to_personality(personality_config),
            'timing': self._optimize_timing(context),
            'intensity': self._calibrate_intensity(context),
            'framing': self._personalize_framing(personality_config),
            'reinforcement': self._design_reinforcement(goals)
        }
        return strategy

    def _create_targeted_nudge(self, strategy, personality_config, context):
        """
        Create specific, actionable nudge with clear next steps
        """
        nudge = {
            'message': self._generate_message(strategy, personality_config),
            'action_steps': self._specify_actions(strategy, context),
            'timing': self._get_optimal_timing(context),
            'delivery_method': self._select_delivery_method(personality_config),
            'follow_up': self._plan_follow_up(strategy)
        }
        return nudge

    def update_intervention_effectiveness(self, user_id, nudge_id, response_data):
        """
        Update intervention effectiveness based on user response
        """
        # Update response tracking
        self._track_response(user_id, nudge_id, response_data)
        
        # Adjust strategies based on effectiveness
        self._optimize_strategies(user_id, response_data)
        
        # Update timing parameters
        self._refine_timing(user_id, response_data)

    def _optimize_strategies(self, user_id, response_data):
        """
        Optimize intervention strategies based on response data
        """
        effectiveness = self._calculate_effectiveness(response_data)
        self._update_strategy_weights(user_id, effectiveness)
        self._adjust_intensity_levels(user_id, response_data)
        self._refine_personalization(user_id, response_data)

    def _refine_timing(self, user_id, response_data):
        """
        Refine intervention timing based on user responsiveness
        """
        optimal_times = self._analyze_response_patterns(response_data)
        self.timing_optimizer['optimal_times'] = optimal_times
        self._update_frequency_caps(user_id, response_data)
        self._adjust_do_not_disturb(user_id, response_data)