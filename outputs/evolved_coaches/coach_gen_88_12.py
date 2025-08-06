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
        self.update_context(context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile)
        
        # Generate specific actionable recommendation
        nudge = self.craft_nudge(strategy, user_profile)
        
        # Optimize timing
        timing = self.optimize_timing(user_profile)
        
        return {
            'nudge': nudge,
            'timing': timing,
            'context_relevance': self.assess_relevance(context),
            'expected_impact': self.predict_impact(user_profile, nudge)
        }

    def update_context(self, context):
        """
        Update context awareness based on latest user data
        """
        for factor in self.context_factors:
            if factor in context:
                self.context_factors[factor] = context[factor]
        
        self.analyze_cognitive_load(context)
        self.update_engagement_patterns(context)

    def select_intervention_strategy(self, user_profile):
        """
        Select the most appropriate intervention strategy based on user profile
        """
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy = {
            'type': self.match_strategy_to_profile(config),
            'intensity': self.calculate_optimal_intensity(user_profile),
            'framing': self.determine_message_framing(config)
        }
        
        return strategy

    def craft_nudge(self, strategy, user_profile):
        """
        Create specific, actionable recommendation using selected strategy
        """
        return {
            'message': self.generate_message(strategy, user_profile),
            'action_steps': self.generate_action_steps(strategy),
            'support_resources': self.compile_resources(strategy),
            'follow_up': self.design_follow_up(strategy)
        }

    def optimize_timing(self, user_profile):
        """
        Determine optimal timing for intervention delivery
        """
        patterns = self.timing_optimizer['engagement_patterns']
        cognitive_load = self.timing_optimizer['cognitive_load']
        
        return {
            'optimal_time': self.calculate_optimal_time(patterns),
            'frequency': self.determine_frequency(cognitive_load),
            'spacing': self.calculate_optimal_spacing(user_profile)
        }

    def assess_relevance(self, context):
        """
        Evaluate contextual relevance of intervention
        """
        relevance_score = self.calculate_relevance_score(context)
        context_match = self.evaluate_context_match(context)
        
        return {
            'score': relevance_score,
            'context_match': context_match,
            'adjustment_needed': relevance_score < 0.8
        }

    def predict_impact(self, user_profile, nudge):
        """
        Predict likely effectiveness of intervention
        """
        return {
            'behavior_change_probability': self.calculate_change_probability(user_profile, nudge),
            'expected_engagement': self.predict_engagement(user_profile),
            'potential_barriers': self.identify_barriers(user_profile)
        }

    def analyze_cognitive_load(self, context):
        """
        Assess current cognitive load to optimize intervention delivery
        """
        self.timing_optimizer['cognitive_load'] = {
            'current_load': self.estimate_cognitive_load(context),
            'capacity': self.estimate_capacity(context),
            'optimal_complexity': self.calculate_optimal_complexity(context)
        }

    def update_engagement_patterns(self, context):
        """
        Update user engagement pattern analysis
        """
        self.timing_optimizer['engagement_patterns'].update({
            'peak_times': self.identify_peak_times(context),
            'response_patterns': self.analyze_response_patterns(context),
            'attention_spans': self.calculate_attention_spans(context)
        })