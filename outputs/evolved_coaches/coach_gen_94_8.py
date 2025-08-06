class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_responses': ['analysis', 'withdrawal', 'planning'],
                'energy_management': ['scheduled_breaks', 'quiet_time', 'deep_work']
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'variety'],
                'stress_responses': ['distraction', 'socializing', 'reframing'],
                'energy_management': ['movement', 'social_breaks', 'novelty']
            }
            # Additional types...
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
            'behavior_change': {
                'implementation_intentions': True,
                'commitment_devices': True,
                'environmental_design': True,
                'accountability': True
            }
        }

        # Context-aware intervention timing
        self.timing_parameters = {
            'optimal_times': [],
            'frequency_caps': {},
            'recovery_periods': {},
            'attention_cycles': [],
            'energy_patterns': {}
        }

        # Personalization factors
        self.user_context = {
            'goals': [],
            'preferences': {},
            'constraints': {},
            'progress': {},
            'engagement_history': []
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate highly personalized behavioral nudge"""
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile, current_context)
        
        # Generate specific actionable recommendation
        nudge = self.craft_nudge(strategy, user_profile, current_context)
        
        # Optimize timing and delivery
        delivery_params = self.optimize_delivery(user_profile, current_context)
        
        return {
            'nudge_content': nudge,
            'delivery_timing': delivery_params,
            'follow_up_actions': self.generate_follow_up(strategy)
        }

    def analyze_context(self, context):
        """Analyze user context for relevance"""
        return {
            'attention_level': self.estimate_attention(context),
            'energy_state': self.assess_energy_state(context),
            'receptivity': self.calculate_receptivity(context),
            'environmental_factors': self.analyze_environment(context),
            'recent_behaviors': self.get_behavior_history(context)
        }

    def select_intervention_strategy(self, user_profile, context):
        """Select most effective intervention strategy"""
        strategies = []
        for strategy, params in self.intervention_strategies.items():
            score = self.score_strategy_fit(strategy, user_profile, context)
            strategies.append((score, strategy))
        
        return max(strategies, key=lambda x: x[0])[1]

    def craft_nudge(self, strategy, profile, context):
        """Create specific, actionable recommendation"""
        template = self.get_strategy_template(strategy)
        personalized = self.personalize_content(template, profile)
        actionable = self.add_specific_actions(personalized, context)
        
        return {
            'message': actionable,
            'suggested_actions': self.break_down_steps(actionable),
            'support_resources': self.get_relevant_resources(strategy)
        }

    def optimize_delivery(self, profile, context):
        """Optimize intervention timing and delivery"""
        return {
            'optimal_time': self.calculate_optimal_time(profile, context),
            'delivery_channel': self.select_channel(profile),
            'frequency': self.determine_frequency(profile),
            'follow_up_schedule': self.create_follow_up_schedule()
        }

    def track_effectiveness(self, nudge_id, user_response):
        """Track and analyze intervention effectiveness"""
        return {
            'engagement': self.measure_engagement(user_response),
            'behavior_change': self.assess_behavior_change(user_response),
            'satisfaction': self.calculate_satisfaction(user_response),
            'learning': self.update_learning_model(nudge_id, user_response)
        }

    def adapt_strategy(self, effectiveness_data):
        """Adapt intervention strategy based on effectiveness"""
        self.update_timing_parameters(effectiveness_data)
        self.refine_personalization(effectiveness_data)
        self.optimize_strategies(effectiveness_data)
        return self.get_updated_parameters()