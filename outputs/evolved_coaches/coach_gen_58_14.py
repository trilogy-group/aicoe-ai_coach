class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced context tracking
        self.context_tracker = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'time_of_day': None,
            'work_context': None,
            'interruption_count': 0,
            'focus_duration': 0,
            'stress_indicators': []
        }

        # Behavioral psychology components
        self.behavioral_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation_factors': {'autonomy': 0, 'mastery': 0, 'purpose': 0},
            'cognitive_biases': [],
            'resistance_patterns': []
        }

        # Personalization engine
        self.user_profile = {
            'personality_type': None,
            'learning_history': [],
            'response_patterns': {},
            'preference_weights': {},
            'achievement_metrics': {},
            'engagement_scores': {}
        }

        # Intervention strategies
        self.coaching_strategies = {
            'nudge': self._create_nudge_strategy(),
            'direct': self._create_direct_strategy(),
            'supportive': self._create_supportive_strategy(),
            'challenge': self._create_challenge_strategy()
        }

    def _create_nudge_strategy(self):
        return {
            'timing_rules': {
                'optimal_intervals': [30, 60, 90],
                'cognitive_load_threshold': 0.7,
                'recovery_period': 15
            },
            'delivery_methods': ['notification', 'inline_prompt', 'ambient_signal'],
            'intensity_levels': range(1, 6),
            'contextual_triggers': ['task_switch', 'idle_period', 'stress_spike']
        }

    def analyze_context(self, user_state, environment_data):
        """Analyze current user context and environment"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        work_context = self._detect_work_pattern(environment_data)
        energy_level = self._estimate_energy_level(user_state)

        self.context_tracker.update({
            'cognitive_load': cognitive_load,
            'work_context': work_context,
            'energy_level': energy_level,
            'time_of_day': environment_data.get('time')
        })

        return self.context_tracker

    def generate_intervention(self, context, user_profile):
        """Generate personalized coaching intervention"""
        strategy = self._select_optimal_strategy(context, user_profile)
        timing = self._optimize_timing(context)
        content = self._generate_content(strategy, user_profile)
        
        return {
            'type': strategy,
            'timing': timing,
            'content': content,
            'intensity': self._calculate_intensity(context),
            'delivery_method': self._select_delivery_method(user_profile)
        }

    def _select_optimal_strategy(self, context, user_profile):
        """Select best coaching strategy based on context and user profile"""
        if context['cognitive_load'] > 0.8:
            return 'supportive'
        elif context['energy_level'] < 0.3:
            return 'nudge'
        elif self._check_growth_opportunity(context):
            return 'challenge'
        return 'direct'

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        if context['cognitive_load'] > 0.7:
            return 'defer'
        if context['work_context'] == 'deep_focus':
            return 'wait_for_break'
        return 'immediate'

    def _generate_content(self, strategy, user_profile):
        """Generate personalized coaching content"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        learning_style = personality_config['learning_style']
        communication_pref = personality_config['communication_pref']

        return {
            'message': self._craft_message(strategy, learning_style, communication_pref),
            'action_items': self._generate_action_items(strategy),
            'supporting_resources': self._get_resources(learning_style)
        }

    def update_user_model(self, interaction_data):
        """Update user model based on interaction data"""
        self.user_profile['learning_history'].append(interaction_data)
        self._update_response_patterns(interaction_data)
        self._adjust_preference_weights(interaction_data)
        self._update_achievement_metrics(interaction_data)

    def _calculate_effectiveness(self):
        """Calculate intervention effectiveness"""
        return {
            'behavioral_change': self._measure_behavior_change(),
            'user_satisfaction': self._calculate_satisfaction(),
            'engagement_level': self._measure_engagement(),
            'goal_progress': self._track_goal_progress()
        }

    def _adapt_strategy(self, effectiveness_metrics):
        """Adapt coaching strategy based on effectiveness metrics"""
        if effectiveness_metrics['behavioral_change'] < 0.5:
            self._adjust_intervention_intensity()
        if effectiveness_metrics['user_satisfaction'] < 0.7:
            self._modify_communication_style()
        if effectiveness_metrics['engagement_level'] < 0.6:
            self._enhance_personalization()

    def get_performance_metrics(self):
        """Return current performance metrics"""
        return {
            'nudge_quality': self._calculate_nudge_quality(),
            'behavioral_change': self._measure_behavior_change(),
            'user_satisfaction': self._calculate_satisfaction(),
            'relevance': self._measure_relevance(),
            'actionability': self._measure_actionability()
        }