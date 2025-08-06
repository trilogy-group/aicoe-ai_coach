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
            'flow_state': {'current': False, 'duration': 0},
            'burnout_risk': 0.0
        }

        # Personalization tracking
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preferred_times': [],
            'intervention_sensitivity': 0.0
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy_level(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity'),
            'interruption_cost': self._calculate_interruption_cost()
        })
        return self.context_tracker

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if not self._should_intervene():
            return None

        intervention = {
            'type': self._select_intervention_type(),
            'content': self._generate_content(),
            'timing': self._optimize_timing(),
            'delivery_style': self._personalize_delivery(user_profile),
            'action_steps': self._create_action_steps()
        }

        return self._enhance_intervention(intervention)

    def track_effectiveness(self, intervention_id, user_response):
        """Monitor and learn from intervention outcomes"""
        self.user_profile['response_history'].append({
            'intervention_id': intervention_id,
            'response': user_response,
            'context': self.context_tracker.copy(),
            'effectiveness': self._calculate_effectiveness(user_response)
        })
        self._update_learning_patterns()

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'multitasking_level': user_state.get('concurrent_tasks', 0),
            'time_pressure': user_state.get('deadline_proximity', 0),
            'mental_fatigue': user_state.get('hours_worked', 0)
        }
        return sum(factors.values()) / len(factors)

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (
            self.context_tracker['cognitive_load'] < 0.7 and
            self.context_tracker['interruption_cost'] < 0.5 and
            not self.behavioral_models['flow_state']['current']
        )

    def _select_intervention_type(self):
        """Choose most appropriate intervention type"""
        options = ['micro_lesson', 'reflection_prompt', 'action_nudge', 'habit_cue']
        return self._rank_options(options)[0]

    def _generate_content(self):
        """Create intervention content based on context"""
        template = self._select_content_template()
        return self._fill_template(template)

    def _personalize_delivery(self, user_profile):
        """Customize intervention delivery style"""
        style = self.personality_type_configs[user_profile['personality_type']]
        return {
            'tone': style['communication_pref'],
            'complexity': self._adapt_complexity(),
            'format': self._select_format(style['learning_style'])
        }

    def _create_action_steps(self):
        """Generate specific, actionable recommendations"""
        return {
            'immediate': self._generate_immediate_action(),
            'short_term': self._generate_short_term_actions(),
            'follow_up': self._generate_follow_up()
        }

    def _enhance_intervention(self, intervention):
        """Apply final enhancements to intervention"""
        return {
            **intervention,
            'motivation_hooks': self._add_motivation_elements(),
            'context_relevance': self._ensure_relevance(),
            'timing_optimization': self._fine_tune_timing()
        }

    def _update_learning_patterns(self):
        """Update user learning patterns based on response history"""
        recent_responses = self.user_profile['response_history'][-10:]
        self.user_profile['learning_patterns'] = self._analyze_patterns(recent_responses)

    def _calculate_effectiveness(self, response):
        """Measure intervention effectiveness"""
        metrics = {
            'engagement': response.get('engagement_level', 0),
            'action_taken': response.get('action_completed', False),
            'reported_value': response.get('user_rating', 0),
            'behavioral_change': response.get('behavior_delta', 0)
        }
        return sum(metrics.values()) / len(metrics)