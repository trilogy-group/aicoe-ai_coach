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
            'motivation': {
                'goal_setting': True,
                'implementation_intentions': True,
                'value_alignment': True,
                'self_efficacy_building': True
            },
            'behavioral_change': {
                'tiny_habits': True,
                'commitment_devices': True,
                'social_proof': True,
                'choice_architecture': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'workload': None,
            'social_context': None,
            'physical_environment': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': [],
            'response_rates': {},
            'engagement_patterns': {},
            'cognitive_load': {}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """
        Generate highly personalized coaching interventions
        """
        # Update context awareness
        self._update_context(context)
        
        # Select optimal intervention strategy
        strategy = self._select_intervention_strategy(user_profile)
        
        # Generate tailored content
        content = self._create_intervention_content(strategy, user_profile)
        
        # Optimize timing
        timing = self._optimize_intervention_timing(user_profile)
        
        return {
            'content': content,
            'timing': timing,
            'strategy': strategy,
            'context': self.context_factors
        }

    def _update_context(self, context):
        """
        Update contextual awareness factors
        """
        for factor, value in context.items():
            if factor in self.context_factors:
                self.context_factors[factor] = value
        
        self._analyze_cognitive_load()
        self._assess_receptivity()

    def _select_intervention_strategy(self, user_profile):
        """
        Select the most effective intervention strategy based on user profile and context
        """
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy = {
            'type': self._match_strategy_to_personality(config),
            'intensity': self._calculate_intervention_intensity(),
            'approach': self._determine_communication_approach(config)
        }
        
        return strategy

    def _create_intervention_content(self, strategy, user_profile):
        """
        Generate specific, actionable intervention content
        """
        content = {
            'message': self._generate_tailored_message(strategy, user_profile),
            'action_steps': self._create_action_steps(),
            'reinforcement': self._design_reinforcement_mechanism(),
            'follow_up': self._plan_follow_up()
        }
        
        return content

    def _optimize_intervention_timing(self, user_profile):
        """
        Optimize intervention timing based on user patterns and context
        """
        timing = {
            'optimal_time': self._calculate_optimal_time(),
            'frequency': self._determine_frequency(),
            'spacing': self._calculate_spacing_interval(),
            'urgency': self._assess_urgency()
        }
        
        return timing

    def _analyze_cognitive_load(self):
        """
        Assess current cognitive load to optimize intervention delivery
        """
        factors = {
            'task_complexity': self.context_factors['workload'],
            'time_pressure': self._calculate_time_pressure(),
            'distractions': self._assess_environment(),
            'fatigue': self.context_factors['energy_level']
        }
        
        self.timing_optimizer['cognitive_load'] = self._calculate_cognitive_load(factors)

    def _assess_receptivity(self):
        """
        Evaluate user receptivity to interventions
        """
        receptivity = {
            'attention_availability': self._check_attention_availability(),
            'emotional_state': self._assess_emotional_state(),
            'motivation_level': self._gauge_motivation(),
            'recent_engagement': self._check_recent_interactions()
        }
        
        return receptivity

    def update_effectiveness_metrics(self, interaction_results):
        """
        Update intervention effectiveness metrics
        """
        self.timing_optimizer['response_rates'].update(interaction_results)
        self._adjust_strategies(interaction_results)
        self._update_engagement_patterns(interaction_results)

    def _adjust_strategies(self, results):
        """
        Adjust intervention strategies based on effectiveness
        """
        for strategy, effectiveness in results.items():
            if strategy in self.intervention_strategies:
                self._refine_strategy_parameters(strategy, effectiveness)

    def get_optimization_metrics(self):
        """
        Return current optimization metrics
        """
        return {
            'response_rates': self.timing_optimizer['response_rates'],
            'engagement_patterns': self.timing_optimizer['engagement_patterns'],
            'strategy_effectiveness': self._calculate_strategy_effectiveness(),
            'context_sensitivity': self._evaluate_context_sensitivity()
        }