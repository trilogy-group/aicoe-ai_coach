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
            'interruption_cost': 0.0
        }

        # Behavioral psychology components
        self.behavioral_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'flow_state': {'depth': 0.0, 'duration': 0},
            'resistance': {'barriers': [], 'mitigation_strategies': {}}
        }

        # User profile and personalization
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'success_metrics': {},
            'preferred_times': [],
            'attention_span': 0,
            'productivity_peaks': []
        }

    def assess_context(self, user_state, environment):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        interruption_cost = self._estimate_interruption_cost(user_state)
        work_context = self._analyze_work_context(environment)

        self.context_tracker.update({
            'cognitive_load': cognitive_load,
            'work_context': work_context,
            'interruption_cost': interruption_cost
        })

        return self._should_intervene()

    def generate_intervention(self, context):
        """Create personalized coaching intervention"""
        if not self._is_appropriate_timing():
            return None

        intervention = {
            'type': self._select_intervention_type(context),
            'content': self._generate_content(context),
            'delivery_style': self._personalize_delivery(),
            'action_steps': self._create_action_steps(context),
            'follow_up': self._plan_follow_up()
        }

        return self._optimize_intervention(intervention)

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'time_pressure': user_state.get('time_pressure', 0),
            'interruptions': user_state.get('interruption_frequency', 0),
            'fatigue': user_state.get('energy_level', 0)
        }
        
        return sum(factors.values()) / len(factors)

    def _personalize_delivery(self):
        """Customize intervention delivery based on user preferences"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        return {
            'style': config.get('communication_pref', 'neutral'),
            'format': self._determine_best_format(),
            'timing': self._optimize_timing()
        }

    def _create_action_steps(self, context):
        """Generate specific, actionable recommendations"""
        return {
            'immediate': self._generate_immediate_actions(context),
            'short_term': self._generate_short_term_plan(),
            'long_term': self._generate_long_term_strategy(),
            'metrics': self._define_success_metrics()
        }

    def update_user_model(self, interaction_data):
        """Update user model based on interaction outcomes"""
        self.user_profile['response_history'].append(interaction_data)
        self._update_learning_patterns(interaction_data)
        self._adjust_intervention_strategies()
        self._refine_timing_model()

    def _optimize_intervention(self, intervention):
        """Optimize intervention for maximum impact"""
        intervention['content'] = self._enhance_relevance(intervention['content'])
        intervention['action_steps'] = self._ensure_actionability(intervention['action_steps'])
        intervention['motivation'] = self._add_motivation_elements()
        
        return intervention

    def _enhance_relevance(self, content):
        """Improve content relevance based on user context"""
        return {
            'core_message': content,
            'context_links': self._generate_context_connections(),
            'personalized_examples': self._generate_examples(),
            'anticipated_obstacles': self._identify_obstacles()
        }

    def _ensure_actionability(self, steps):
        """Make recommendations more specific and actionable"""
        return {
            'micro_steps': self._break_down_steps(steps),
            'success_criteria': self._define_success_metrics(),
            'progress_tracking': self._create_tracking_mechanism(),
            'contingency_plans': self._generate_contingencies()
        }

    def _add_motivation_elements(self):
        """Add psychological motivation enhancers"""
        return {
            'intrinsic_motivators': self._identify_personal_motivators(),
            'progress_visualization': self._create_progress_markers(),
            'social_proof': self._gather_relevant_examples(),
            'commitment_devices': self._generate_commitment_strategies()
        }

    def get_performance_metrics(self):
        """Return current performance metrics"""
        return {
            'intervention_success_rate': self._calculate_success_rate(),
            'user_engagement': self._measure_engagement(),
            'behavior_change': self._measure_behavior_change(),
            'user_satisfaction': self._measure_satisfaction()
        }