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
            'work_load': None,
            'social_context': None,
            'environmental_factors': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_frequency': None,
            'user_receptivity': None,
            'context_appropriateness': None,
            'intervention_spacing': None
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """
        Generate highly personalized behavioral nudges based on user profile and context
        """
        # Update context awareness
        self.update_context(current_context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile)
        
        # Generate customized content
        content = self.create_intervention_content(strategy, user_profile)
        
        # Optimize timing
        timing = self.optimize_intervention_timing()
        
        return {
            'content': content,
            'timing': timing,
            'strategy': strategy
        }

    def update_context(self, current_context):
        """
        Update context awareness based on current user situation
        """
        for factor in self.context_factors:
            if factor in current_context:
                self.context_factors[factor] = current_context[factor]

    def select_intervention_strategy(self, user_profile):
        """
        Select the most appropriate intervention strategy based on user profile and context
        """
        personality_type = user_profile['personality_type']
        config = self.personality_type_configs[personality_type]
        
        # Match strategy to user characteristics and context
        strategy = {
            'type': self.match_strategy_to_profile(config),
            'intensity': self.calculate_intervention_intensity(),
            'framing': self.determine_message_framing(config)
        }
        
        return strategy

    def create_intervention_content(self, strategy, user_profile):
        """
        Create specific, actionable intervention content
        """
        content = {
            'message': self.generate_message(strategy, user_profile),
            'action_steps': self.generate_action_steps(strategy),
            'support_resources': self.compile_resources(strategy),
            'progress_metrics': self.define_progress_metrics(strategy)
        }
        
        return content

    def optimize_intervention_timing(self):
        """
        Optimize intervention timing based on user receptivity and context
        """
        timing = {
            'optimal_time': self.calculate_optimal_time(),
            'frequency': self.determine_frequency(),
            'spacing': self.calculate_intervention_spacing()
        }
        
        return timing

    def calculate_intervention_intensity(self):
        """
        Calculate appropriate intervention intensity based on context
        """
        stress_level = self.context_factors['stress_level']
        workload = self.context_factors['work_load']
        energy = self.context_factors['energy_level']
        
        # Algorithm to balance intensity with current capacity
        return self.balance_intensity(stress_level, workload, energy)

    def determine_message_framing(self, user_config):
        """
        Determine optimal message framing based on user preferences
        """
        return {
            'tone': user_config['communication_pref'],
            'complexity': self.adapt_to_cognitive_load(),
            'focus': user_config['motivation_drivers'][0]
        }

    def adapt_to_cognitive_load(self):
        """
        Adapt content complexity based on current cognitive load indicators
        """
        workload = self.context_factors['work_load']
        stress = self.context_factors['stress_level']
        
        return self.calculate_optimal_complexity(workload, stress)

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """
        Track and analyze intervention effectiveness
        """
        effectiveness_metrics = {
            'user_engagement': self.measure_engagement(user_response),
            'behavior_change': self.measure_behavior_change(user_response),
            'satisfaction': self.measure_satisfaction(user_response)
        }
        
        self.update_strategy_weights(effectiveness_metrics)
        return effectiveness_metrics