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
                'decision_style': 'logical'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'adaptive',
                'decision_style': 'intuitive'
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
            'cognitive_reframing': {
                'thought_awareness': True,
                'belief_examination': True,
                'perspective_shifting': True
            },
            'motivation_enhancement': {
                'goal_setting': True,
                'value_alignment': True,
                'self_efficacy': True
            }
        }

        # Context-aware nudge parameters
        self.nudge_config = {
            'timing': {
                'peak_energy_hours': True,
                'task_complexity': True,
                'current_cognitive_load': True
            },
            'frequency': {
                'optimal_spacing': True,
                'habituation_prevention': True,
                'urgency_adjustment': True
            },
            'format': {
                'communication_style': True,
                'media_type': True,
                'length': True
            }
        }

    def generate_personalized_intervention(self, user_data, context):
        """
        Generate highly personalized coaching intervention based on user data and context
        """
        personality_profile = self._analyze_personality(user_data)
        current_context = self._evaluate_context(context)
        optimal_strategy = self._select_intervention_strategy(personality_profile, current_context)
        
        return self._craft_intervention(optimal_strategy, personality_profile, current_context)

    def _analyze_personality(self, user_data):
        """
        Analyze user personality traits and preferences
        """
        personality_type = user_data.get('personality_type')
        base_profile = self.personality_type_configs.get(personality_type, {})
        
        # Enhance with behavioral analysis
        behavioral_patterns = self._analyze_behavioral_patterns(user_data)
        learning_preferences = self._determine_learning_style(user_data)
        
        return {
            **base_profile,
            'behavioral_patterns': behavioral_patterns,
            'learning_preferences': learning_preferences
        }

    def _evaluate_context(self, context):
        """
        Evaluate current user context for optimal intervention
        """
        return {
            'cognitive_load': self._assess_cognitive_load(context),
            'energy_level': self._estimate_energy_level(context),
            'time_pressure': self._calculate_time_pressure(context),
            'environmental_factors': self._analyze_environment(context),
            'recent_progress': self._evaluate_progress(context)
        }

    def _select_intervention_strategy(self, personality_profile, context):
        """
        Select most effective intervention strategy based on personality and context
        """
        strategy_scores = {}
        
        for strategy in self.intervention_strategies:
            score = self._calculate_strategy_fit(
                strategy,
                personality_profile,
                context
            )
            strategy_scores[strategy] = score
            
        return max(strategy_scores.items(), key=lambda x: x[1])[0]

    def _craft_intervention(self, strategy, profile, context):
        """
        Craft specific, actionable intervention using selected strategy
        """
        intervention = {
            'content': self._generate_content(strategy, profile),
            'delivery_method': self._optimize_delivery(profile, context),
            'timing': self._determine_optimal_timing(context),
            'action_steps': self._create_action_steps(strategy, profile),
            'follow_up': self._design_follow_up(strategy, profile)
        }
        
        return self._personalize_messaging(intervention, profile)

    def _calculate_strategy_fit(self, strategy, profile, context):
        """
        Calculate how well a strategy fits current user and context
        """
        personality_fit = self._assess_personality_fit(strategy, profile)
        context_fit = self._assess_context_fit(strategy, context)
        historical_success = self._analyze_historical_effectiveness(strategy, profile)
        
        return (0.4 * personality_fit + 
                0.4 * context_fit + 
                0.2 * historical_success)

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """
        Track and analyze intervention effectiveness
        """
        return {
            'behavioral_change': self._measure_behavior_change(metrics),
            'user_satisfaction': self._analyze_satisfaction(metrics),
            'engagement_level': self._calculate_engagement(metrics),
            'goal_progress': self._evaluate_goal_progress(metrics)
        }

    def adapt_strategy(self, effectiveness_data):
        """
        Adapt intervention strategies based on effectiveness data
        """
        self._update_strategy_weights(effectiveness_data)
        self._refine_personalization_models(effectiveness_data)
        self._optimize_timing_patterns(effectiveness_data)