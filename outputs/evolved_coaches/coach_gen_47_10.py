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
                'temptation_bundling': True,
                'environmental_design': True,
                'social_accountability': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'available_time': None,
            'priority_tasks': [],
            'recent_progress': {},
            'environmental_conditions': {}
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': {},
            'response_patterns': {},
            'engagement_metrics': {},
            'circadian_preferences': {}
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate highly personalized coaching intervention"""
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile, current_context)
        
        # Generate specific actionable recommendation
        nudge = self.craft_nudge(strategy, user_profile, current_context)
        
        # Optimize timing
        delivery_time = self.optimize_delivery_timing(user_profile, current_context)
        
        return {
            'content': nudge,
            'delivery_time': delivery_time,
            'follow_up_actions': self.generate_follow_up_plan(strategy)
        }

    def analyze_context(self, context):
        """Analyze user context for intervention relevance"""
        analyzed_context = {
            'cognitive_load': self.estimate_cognitive_load(context),
            'attention_capacity': self.estimate_attention_capacity(context),
            'motivation_state': self.assess_motivation_state(context),
            'environmental_factors': self.analyze_environment(context)
        }
        return analyzed_context

    def select_intervention_strategy(self, user_profile, context):
        """Select most effective intervention strategy based on user and context"""
        strategy_scores = {}
        
        for strategy in self.intervention_strategies:
            score = self.calculate_strategy_fit(
                strategy, 
                user_profile,
                context
            )
            strategy_scores[strategy] = score
            
        return max(strategy_scores, key=strategy_scores.get)

    def craft_nudge(self, strategy, user_profile, context):
        """Create specific, actionable coaching recommendation"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        nudge = {
            'message': self.generate_message(strategy, personality_config),
            'action_steps': self.generate_action_steps(strategy, context),
            'motivation_hook': self.create_motivation_hook(personality_config),
            'follow_up_trigger': self.set_follow_up_trigger(strategy)
        }
        
        return nudge

    def optimize_delivery_timing(self, user_profile, context):
        """Optimize intervention timing for maximum effectiveness"""
        optimal_time = self.timing_optimizer['optimal_intervals'].get(
            user_profile['id'],
            self.calculate_optimal_time(user_profile, context)
        )
        
        return optimal_time

    def generate_follow_up_plan(self, strategy):
        """Create follow-up plan to reinforce intervention"""
        return {
            'check_in_schedule': self.create_check_in_schedule(strategy),
            'progress_metrics': self.define_progress_metrics(strategy),
            'adjustment_triggers': self.set_adjustment_triggers(strategy)
        }

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        effectiveness_metrics = {
            'engagement_level': self.calculate_engagement(user_response),
            'behavior_change': self.measure_behavior_change(user_response),
            'user_satisfaction': self.assess_satisfaction(user_response)
        }
        
        self.update_strategy_weights(intervention_id, effectiveness_metrics)
        return effectiveness_metrics

    def adapt_to_feedback(self, user_id, feedback):
        """Adapt coaching approach based on user feedback"""
        self.update_user_profile(user_id, feedback)
        self.refine_intervention_strategies(feedback)
        self.adjust_timing_parameters(user_id, feedback)