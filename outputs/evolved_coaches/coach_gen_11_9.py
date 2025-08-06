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
            'priority_tasks': [],
            'environmental_conditions': {},
            'social_context': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': [],
            'user_receptivity': {},
            'context_weights': {},
            'engagement_history': []
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """
        Generate highly personalized coaching interventions based on user profile and context
        """
        # Get personality-specific configurations
        personality_config = self.personality_type_configs.get(user_profile['personality_type'])
        
        # Analyze current context
        context_assessment = self.assess_context(current_context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(
            personality_config,
            context_assessment,
            user_profile['goals']
        )

        # Generate specific actionable recommendation
        nudge = self.craft_intervention(
            strategy,
            personality_config,
            context_assessment
        )

        return nudge

    def assess_context(self, context_data):
        """
        Sophisticated context analysis considering multiple factors
        """
        self.context_factors.update({
            'time_of_day': context_data.get('time'),
            'energy_level': self.estimate_energy_level(context_data),
            'stress_level': self.analyze_stress_indicators(context_data),
            'priority_tasks': self.prioritize_tasks(context_data.get('tasks')),
            'environmental_conditions': context_data.get('environment'),
            'social_context': context_data.get('social_setting')
        })
        
        return self.context_factors

    def select_intervention_strategy(self, personality_config, context, goals):
        """
        Select the most appropriate intervention strategy based on multiple factors
        """
        strategy_scores = {}
        
        for strategy, components in self.intervention_strategies.items():
            score = self.calculate_strategy_fit(
                strategy,
                components,
                personality_config,
                context,
                goals
            )
            strategy_scores[strategy] = score
            
        return max(strategy_scores.items(), key=lambda x: x[1])[0]

    def craft_intervention(self, strategy, personality_config, context):
        """
        Create specific, actionable recommendations using selected strategy
        """
        intervention = {
            'message': self.generate_message(strategy, personality_config),
            'action_steps': self.generate_action_steps(strategy, context),
            'timing': self.optimize_timing(context),
            'follow_up': self.design_follow_up(strategy),
            'reinforcement': self.create_reinforcement_plan(personality_config)
        }
        
        return intervention

    def calculate_strategy_fit(self, strategy, components, personality, context, goals):
        """
        Calculate how well a strategy fits current situation
        """
        weights = {
            'personality_alignment': 0.3,
            'context_suitability': 0.25,
            'goal_relevance': 0.25,
            'historical_effectiveness': 0.2
        }
        
        scores = {
            'personality_alignment': self.assess_personality_fit(strategy, personality),
            'context_suitability': self.assess_context_fit(strategy, context),
            'goal_relevance': self.assess_goal_alignment(strategy, goals),
            'historical_effectiveness': self.get_historical_effectiveness(strategy)
        }
        
        return sum(weight * scores[factor] for factor, weight in weights.items())

    def optimize_timing(self, context):
        """
        Optimize intervention timing based on user receptivity and context
        """
        timing_factors = {
            'user_energy': context['energy_level'],
            'stress_level': context['stress_level'],
            'task_load': len(context['priority_tasks']),
            'time_of_day': context['time_of_day']
        }
        
        optimal_time = self.calculate_optimal_timing(timing_factors)
        self.timing_optimizer['optimal_intervals'].append(optimal_time)
        
        return optimal_time

    def track_effectiveness(self, intervention_id, user_response):
        """
        Track and analyze intervention effectiveness
        """
        effectiveness_metrics = {
            'user_engagement': user_response.get('engagement_level'),
            'action_completion': user_response.get('action_completed'),
            'satisfaction': user_response.get('satisfaction_score'),
            'behavioral_change': user_response.get('behavior_modified')
        }
        
        self.update_strategy_effectiveness(intervention_id, effectiveness_metrics)
        self.adjust_future_interventions(effectiveness_metrics)

    def update_strategy_effectiveness(self, intervention_id, metrics):
        """
        Update effectiveness ratings for intervention strategies
        """
        strategy = self.get_intervention_strategy(intervention_id)
        current_effectiveness = self.intervention_strategies[strategy]
        
        # Update effectiveness ratings based on new data
        updated_effectiveness = self.calculate_updated_effectiveness(
            current_effectiveness,
            metrics
        )
        
        self.intervention_strategies[strategy] = updated_effectiveness