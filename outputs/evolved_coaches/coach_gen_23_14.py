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
            'priority_tasks': [],
            'environmental_conditions': {},
            'social_context': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': [],
            'user_receptivity': {},
            'context_weights': {},
            'response_history': []
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """
        Generate highly personalized coaching interventions based on user profile and context
        """
        # Get personality-specific configurations
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Analyze current context
        context_assessment = self.assess_context(current_context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(
            personality_config,
            context_assessment,
            user_profile['goals']
        )

        # Generate specific actionable recommendation
        nudge = self.craft_nudge(
            strategy,
            personality_config['communication_pref'],
            context_assessment['constraints']
        )

        return self.optimize_delivery(nudge, context_assessment)

    def assess_context(self, context):
        """
        Comprehensive context analysis for intervention timing and content
        """
        return {
            'attention_availability': self.estimate_attention_availability(context),
            'cognitive_load': self.assess_cognitive_load(context),
            'environmental_factors': self.analyze_environment(context),
            'timing_appropriateness': self.evaluate_timing(context),
            'constraints': self.identify_constraints(context)
        }

    def select_intervention_strategy(self, personality_config, context, goals):
        """
        Select the most effective intervention strategy based on user characteristics
        """
        strategy_weights = {
            'habit_formation': self.calculate_strategy_fit('habit_formation', personality_config, context),
            'motivation': self.calculate_strategy_fit('motivation', personality_config, context),
            'behavioral_change': self.calculate_strategy_fit('behavioral_change', personality_config, context)
        }
        
        return max(strategy_weights.items(), key=lambda x: x[1])[0]

    def craft_nudge(self, strategy, communication_style, constraints):
        """
        Create specific, actionable recommendations using selected strategy
        """
        return {
            'content': self.generate_content(strategy, communication_style),
            'action_steps': self.generate_action_steps(strategy, constraints),
            'support_resources': self.compile_resources(strategy),
            'follow_up': self.design_follow_up(strategy)
        }

    def optimize_delivery(self, nudge, context):
        """
        Optimize intervention delivery for maximum impact
        """
        return {
            'content': self.adapt_content_to_context(nudge['content'], context),
            'timing': self.determine_optimal_timing(context),
            'format': self.select_delivery_format(context),
            'intensity': self.calibrate_intensity(context)
        }

    def track_effectiveness(self, nudge_id, user_response):
        """
        Track and analyze intervention effectiveness
        """
        self.timing_optimizer['response_history'].append({
            'nudge_id': nudge_id,
            'response': user_response,
            'context': self.context_factors.copy(),
            'timestamp': self.get_current_timestamp()
        })
        
        self.update_optimization_parameters(nudge_id, user_response)

    def update_optimization_parameters(self, nudge_id, response):
        """
        Update internal optimization parameters based on intervention outcomes
        """
        self.timing_optimizer['user_receptivity'].update(self.analyze_response_patterns())
        self.timing_optimizer['optimal_intervals'] = self.recalculate_intervals()
        self.intervention_strategies = self.refine_strategies(response)