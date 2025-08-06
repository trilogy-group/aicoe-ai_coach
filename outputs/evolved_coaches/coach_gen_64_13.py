class EvolutionaryAICoach:
    def __init__(self):
        self.user_profile = {}
        self.intervention_history = []
        self.behavioral_models = {
            'motivation': MotivationModel(),
            'habit_formation': HabitFormationModel(),
            'cognitive_load': CognitiveLoadModel()
        }
        self.personalization_engine = PersonalizationEngine()
        self.recommendation_engine = RecommendationEngine()
        self.metrics_tracker = MetricsTracker()

    def initialize_user(self, user_data):
        """Initialize user profile with baseline data and preferences"""
        self.user_profile = {
            'demographics': user_data.get('demographics', {}),
            'goals': user_data.get('goals', []),
            'preferences': user_data.get('preferences', {}),
            'context': user_data.get('context', {}),
            'behavioral_patterns': {},
            'intervention_response': {}
        }
        self.personalization_engine.initialize(self.user_profile)

    def generate_intervention(self, context):
        """Generate personalized coaching intervention"""
        # Analyze current context and user state
        user_state = self._analyze_user_state(context)
        cognitive_load = self.behavioral_models['cognitive_load'].assess(context)
        
        # Select optimal intervention type and timing
        intervention_type = self._select_intervention_type(user_state, cognitive_load)
        timing = self._optimize_timing(context, cognitive_load)

        # Generate personalized content
        content = self.recommendation_engine.generate(
            intervention_type=intervention_type,
            user_profile=self.user_profile,
            context=context,
            cognitive_load=cognitive_load
        )

        # Add actionability enhancements
        actionable_steps = self._generate_action_steps(content)
        success_metrics = self._define_success_metrics(content)
        
        intervention = {
            'type': intervention_type,
            'timing': timing,
            'content': content,
            'action_steps': actionable_steps,
            'success_metrics': success_metrics,
            'priority': self._calculate_priority(context),
            'follow_up': self._schedule_follow_up(timing)
        }

        self.intervention_history.append(intervention)
        return intervention

    def _analyze_user_state(self, context):
        """Analyze current user state based on context and history"""
        recent_behavior = self.metrics_tracker.get_recent_behavior()
        motivation_level = self.behavioral_models['motivation'].assess(
            context, recent_behavior
        )
        habit_strength = self.behavioral_models['habit_formation'].assess(
            self.intervention_history
        )
        
        return {
            'motivation': motivation_level,
            'habit_strength': habit_strength,
            'engagement': self.metrics_tracker.get_engagement_level(),
            'progress': self.metrics_tracker.get_goal_progress()
        }

    def _select_intervention_type(self, user_state, cognitive_load):
        """Select optimal intervention type based on user state"""
        if cognitive_load > 0.7:
            return 'micro_action'
        elif user_state['motivation'] < 0.4:
            return 'motivation_boost'
        elif user_state['habit_strength'] < 0.3:
            return 'habit_formation'
        else:
            return 'progress_optimization'

    def _optimize_timing(self, context, cognitive_load):
        """Optimize intervention timing based on context"""
        user_schedule = context.get('schedule', {})
        attention_patterns = self.metrics_tracker.get_attention_patterns()
        
        optimal_times = self.personalization_engine.predict_optimal_times(
            user_schedule,
            attention_patterns,
            cognitive_load
        )
        
        return optimal_times[0] if optimal_times else None

    def _generate_action_steps(self, content):
        """Generate specific, measurable action steps"""
        return self.recommendation_engine.break_down_actions(
            content,
            max_steps=3,
            time_estimates=True,
            difficulty_levels=True
        )

    def _define_success_metrics(self, content):
        """Define concrete success metrics for the intervention"""
        return {
            'primary_metric': self.recommendation_engine.get_primary_metric(content),
            'secondary_metrics': self.recommendation_engine.get_secondary_metrics(content),
            'timeframe': self.recommendation_engine.get_measurement_timeframe(content)
        }

    def _calculate_priority(self, context):
        """Calculate intervention priority level"""
        urgency = context.get('urgency', 0.5)
        importance = self.recommendation_engine.assess_importance(context)
        user_receptivity = self.personalization_engine.predict_receptivity(context)
        
        return (urgency + importance + user_receptivity) / 3

    def _schedule_follow_up(self, timing):
        """Schedule follow-up check based on intervention timing"""
        return {
            'time': timing + self.recommendation_engine.get_optimal_follow_up_delay(),
            'type': 'check_progress',
            'metrics': ['completion', 'effectiveness', 'satisfaction']
        }

    def update_metrics(self, intervention_id, metrics):
        """Update intervention effectiveness metrics"""
        self.metrics_tracker.update(intervention_id, metrics)
        self.personalization_engine.update_models(metrics)
        self._adapt_strategies(metrics)

    def _adapt_strategies(self, metrics):
        """Adapt coaching strategies based on effectiveness metrics"""
        if metrics['effectiveness'] < 0.5:
            self.recommendation_engine.adjust_difficulty(-0.1)
            self.personalization_engine.increase_personalization_weight()
        else:
            self.recommendation_engine.adjust_difficulty(0.05)
            self.behavioral_models['habit_formation'].strengthen_pattern(metrics)