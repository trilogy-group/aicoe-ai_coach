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
            'effectiveness_history': {}
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate highly personalized coaching intervention"""
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile, current_context)
        
        # Generate specific actionable recommendation
        nudge = self.create_targeted_nudge(strategy, user_profile, current_context)
        
        # Optimize timing and delivery
        delivery_plan = self.optimize_delivery(nudge, user_profile, current_context)
        
        return self.format_intervention(nudge, delivery_plan)

    def analyze_context(self, context):
        """Enhanced context analysis with multiple factors"""
        analyzed_context = {
            'cognitive_load': self.estimate_cognitive_load(context),
            'attention_capacity': self.assess_attention_availability(context),
            'environmental_factors': self.analyze_environment(context),
            'temporal_patterns': self.identify_timing_patterns(context),
            'task_complexity': self.evaluate_task_demands(context)
        }
        return analyzed_context

    def select_intervention_strategy(self, user_profile, context):
        """Choose most effective intervention based on user and context"""
        strategies = []
        
        # Match strategy to personality type
        personality_match = self.match_personality_strategies(user_profile)
        strategies.extend(personality_match)
        
        # Consider contextual factors
        context_match = self.match_context_strategies(context)
        strategies.extend(context_match)
        
        # Evaluate past effectiveness
        effectiveness_weights = self.calculate_strategy_weights(strategies, user_profile)
        
        return self.select_optimal_strategy(strategies, effectiveness_weights)

    def create_targeted_nudge(self, strategy, user_profile, context):
        """Generate specific, actionable recommendation"""
        nudge = {
            'content': self.generate_nudge_content(strategy, user_profile),
            'action_steps': self.create_action_steps(strategy),
            'motivation_hooks': self.identify_motivation_triggers(user_profile),
            'implementation_plan': self.create_implementation_plan(context)
        }
        return nudge

    def optimize_delivery(self, nudge, user_profile, context):
        """Optimize intervention timing and delivery method"""
        delivery_plan = {
            'timing': self.calculate_optimal_timing(context),
            'method': self.select_delivery_method(user_profile),
            'frequency': self.determine_frequency(user_profile, context),
            'follow_up': self.plan_follow_up(nudge)
        }
        return delivery_plan

    def track_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        effectiveness_metrics = {
            'engagement': self.measure_engagement(user_response),
            'behavior_change': self.assess_behavior_change(user_response),
            'user_satisfaction': self.evaluate_satisfaction(user_response),
            'long_term_impact': self.project_long_term_impact(user_response)
        }
        
        self.update_effectiveness_history(intervention_id, effectiveness_metrics)
        self.optimize_future_interventions(effectiveness_metrics)

    def adapt_to_feedback(self, user_id, feedback):
        """Adapt coaching approach based on user feedback"""
        self.update_user_preferences(user_id, feedback)
        self.refine_intervention_strategies(feedback)
        self.adjust_timing_parameters(feedback)
        self.enhance_personalization(user_id, feedback)

    def format_intervention(self, nudge, delivery_plan):
        """Format final intervention for delivery"""
        return {
            'content': nudge['content'],
            'action_steps': nudge['action_steps'],
            'timing': delivery_plan['timing'],
            'delivery_method': delivery_plan['method'],
            'follow_up_plan': delivery_plan['follow_up'],
            'motivation_elements': nudge['motivation_hooks'],
            'implementation_guidance': nudge['implementation_plan']
        }