class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced attributes
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_response': 'analytical',
                'optimal_challenge_level': 'high'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'adaptive',
                'optimal_challenge_level': 'moderate'
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
            'available_time': None,
            'priority_tasks': [],
            'recent_progress': {},
            'environmental_factors': {}
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': {},
            'response_patterns': {},
            'engagement_metrics': {},
            'effectiveness_history': {}
        }

    def generate_personalized_nudge(self, user_id, context):
        """
        Generate highly personalized coaching interventions based on user context
        """
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        intervention = self.select_optimal_intervention(
            user_profile,
            current_context,
            self.get_historical_effectiveness(user_id)
        )
        
        return self.format_intervention(intervention, user_profile['communication_pref'])

    def analyze_context(self, context):
        """
        Enhanced context analysis incorporating multiple factors
        """
        analyzed_context = {
            'cognitive_load': self.estimate_cognitive_load(context),
            'attention_capacity': self.assess_attention_availability(context),
            'motivation_state': self.evaluate_motivation_level(context),
            'environmental_support': self.assess_environment(context),
            'timing_appropriateness': self.evaluate_timing(context)
        }
        return analyzed_context

    def select_optimal_intervention(self, user_profile, context, history):
        """
        Select the most effective intervention based on multiple factors
        """
        candidate_interventions = self.generate_intervention_candidates(user_profile)
        
        scored_interventions = [
            (intervention, self.score_intervention_fit(
                intervention, 
                user_profile,
                context,
                history
            ))
            for intervention in candidate_interventions
        ]
        
        return max(scored_interventions, key=lambda x: x[1])[0]

    def score_intervention_fit(self, intervention, user_profile, context, history):
        """
        Calculate comprehensive intervention fit score
        """
        return sum([
            self.calculate_psychological_alignment(intervention, user_profile),
            self.calculate_contextual_relevance(intervention, context),
            self.calculate_historical_effectiveness(intervention, history),
            self.calculate_cognitive_load_appropriateness(intervention, context),
            self.calculate_motivation_impact(intervention, user_profile)
        ]) / 5.0

    def format_intervention(self, intervention, communication_style):
        """
        Format intervention according to user's preferred communication style
        """
        formatted = {
            'message': self.adapt_message_style(intervention['content'], communication_style),
            'action_steps': self.generate_specific_actions(intervention['recommendations']),
            'support_resources': self.curate_resources(intervention['topic']),
            'follow_up': self.design_follow_up_plan(intervention['goals'])
        }
        return formatted

    def adapt_message_style(self, content, style):
        """
        Adapt message delivery to user's communication preferences
        """
        style_adaptations = {
            'direct': self.format_direct_style,
            'enthusiastic': self.format_enthusiastic_style,
            'analytical': self.format_analytical_style,
            'supportive': self.format_supportive_style
        }
        return style_adaptations[style](content)

    def generate_specific_actions(self, recommendations):
        """
        Convert recommendations into specific, actionable steps
        """
        return [
            {
                'step': i + 1,
                'action': action,
                'timeframe': self.suggest_timeframe(action),
                'success_criteria': self.define_success_criteria(action),
                'potential_obstacles': self.identify_obstacles(action),
                'mitigation_strategies': self.suggest_mitigations(action)
            }
            for i, action in enumerate(recommendations)
        ]

    def update_effectiveness_metrics(self, user_id, intervention_id, outcomes):
        """
        Update intervention effectiveness metrics based on outcomes
        """
        self.timing_optimizer['effectiveness_history'][intervention_id] = {
            'user_id': user_id,
            'timestamp': self.get_current_timestamp(),
            'outcomes': outcomes,
            'context': self.context_factors.copy()
        }
        
        self.optimize_future_interventions(user_id, outcomes)

    def optimize_future_interventions(self, user_id, outcomes):
        """
        Adjust future intervention strategies based on observed outcomes
        """
        self.update_timing_patterns(user_id, outcomes)
        self.adjust_challenge_levels(user_id, outcomes)
        self.refine_communication_approach(user_id, outcomes)
        self.update_effectiveness_models(user_id, outcomes)