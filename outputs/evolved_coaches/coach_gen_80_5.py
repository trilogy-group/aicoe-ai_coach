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
        self.update_context(context)
        
        # Select optimal intervention timing
        if not self.is_optimal_timing(user_profile):
            return None

        # Get personality-aligned strategy
        strategy = self.get_matched_strategy(user_profile)
        
        # Generate specific actionable recommendation
        nudge = self.create_targeted_nudge(strategy, user_profile)
        
        # Enhance with behavioral psychology
        nudge = self.apply_behavioral_science(nudge)
        
        return nudge

    def update_context(self, context):
        """
        Update contextual awareness factors
        """
        for factor in context:
            if factor in self.context_factors:
                self.context_factors[factor] = context[factor]
        
        self.update_timing_model()

    def is_optimal_timing(self, user_profile):
        """
        Determine if current moment is optimal for intervention
        """
        current_load = self.assess_cognitive_load()
        engagement_likelihood = self.predict_engagement(user_profile)
        return current_load < 0.7 and engagement_likelihood > 0.6

    def get_matched_strategy(self, user_profile):
        """
        Match intervention strategy to personality and context
        """
        personality_type = user_profile['personality_type']
        config = self.personality_type_configs[personality_type]
        
        return {
            'communication_style': config['communication_pref'],
            'motivation_approach': self.select_motivation_approach(config),
            'learning_method': config['learning_style']
        }

    def create_targeted_nudge(self, strategy, user_profile):
        """
        Generate specific, actionable recommendation
        """
        nudge = {
            'content': self.generate_content(strategy),
            'action_steps': self.create_action_steps(),
            'support_resources': self.get_relevant_resources(user_profile),
            'follow_up': self.design_follow_up()
        }
        return nudge

    def apply_behavioral_science(self, nudge):
        """
        Enhance nudge with behavioral psychology principles
        """
        nudge.update({
            'social_proof': self.add_social_proof(),
            'commitment': self.create_commitment_device(),
            'implementation_intention': self.form_implementation_intention(),
            'progress_tracking': self.design_progress_tracking()
        })
        return nudge

    def assess_cognitive_load(self):
        """
        Estimate current cognitive load
        """
        factors = [
            self.context_factors['workload'],
            self.context_factors['stress_level'],
            self.timing_optimizer['cognitive_load']
        ]
        return sum(filter(None, factors)) / len(factors)

    def predict_engagement(self, user_profile):
        """
        Predict likelihood of engagement
        """
        historical_engagement = self.timing_optimizer['engagement_patterns'].get(
            user_profile['id'], 0.5
        )
        context_score = self.calculate_context_score()
        return (historical_engagement + context_score) / 2

    def update_timing_model(self):
        """
        Update intervention timing model based on new data
        """
        self.timing_optimizer['cognitive_load'] = self.assess_cognitive_load()
        # Additional timing optimization logic

    def calculate_context_score(self):
        """
        Calculate conduciveness of current context
        """
        weights = {
            'time_of_day': 0.2,
            'energy_level': 0.3,
            'stress_level': 0.3,
            'workload': 0.2
        }
        
        score = 0
        for factor, weight in weights.items():
            if self.context_factors[factor]:
                score += self.context_factors[factor] * weight
        
        return score