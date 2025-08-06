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
            'environment': None,
            'recent_activity': None,
            'upcoming_commitments': None
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
        Generate highly personalized behavioral nudges based on user profile and context
        """
        # Update context awareness
        self._update_context(context)
        
        # Select optimal intervention strategy
        strategy = self._select_intervention_strategy(user_profile)
        
        # Generate customized content
        content = self._create_intervention_content(strategy, user_profile)
        
        # Optimize timing
        timing = self._optimize_intervention_timing(user_profile)
        
        return {
            'content': content,
            'timing': timing,
            'strategy': strategy,
            'context_factors': self.context_factors
        }

    def _update_context(self, context):
        """
        Update context awareness based on current user situation
        """
        for factor in context:
            if factor in self.context_factors:
                self.context_factors[factor] = context[factor]
        
        self._analyze_cognitive_load()
        self._assess_receptivity()

    def _select_intervention_strategy(self, user_profile):
        """
        Select the most appropriate intervention strategy based on user profile and context
        """
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy = {
            'type': self._match_strategy_to_personality(config),
            'intensity': self._calculate_intervention_intensity(),
            'framing': self._determine_message_framing(config),
            'social_proof': self._incorporate_social_elements(config)
        }
        
        return strategy

    def _create_intervention_content(self, strategy, user_profile):
        """
        Create specific, actionable intervention content
        """
        content = {
            'message': self._generate_message(strategy, user_profile),
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
            'spacing': self._optimize_spacing(),
            'urgency': self._assess_urgency()
        }
        
        return timing

    def _analyze_cognitive_load(self):
        """
        Analyze current cognitive load to optimize intervention delivery
        """
        factors = {
            'task_complexity': self._assess_task_complexity(),
            'mental_fatigue': self._estimate_mental_fatigue(),
            'attention_resources': self._evaluate_attention_resources()
        }
        
        self.timing_optimizer['cognitive_load'] = factors

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """
        Track and analyze intervention effectiveness
        """
        effectiveness = {
            'engagement': metrics.get('engagement'),
            'completion': metrics.get('completion'),
            'satisfaction': metrics.get('satisfaction'),
            'behavioral_change': metrics.get('behavioral_change')
        }
        
        self._update_strategy_weights(effectiveness)
        self._refine_timing_model(effectiveness)
        
        return effectiveness

    def adapt_to_feedback(self, feedback_data):
        """
        Adapt coaching strategies based on feedback
        """
        self._update_intervention_strategies(feedback_data)
        self._refine_personality_models(feedback_data)
        self._optimize_timing_parameters(feedback_data)
        self._enhance_context_awareness(feedback_data)