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

    def assess_context(self, user_state, environment):
        """Evaluate current user context for intervention timing"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy_level(user_state),
            'time_of_day': environment.get('time'),
            'work_context': environment.get('activity'),
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
            'delivery_style': self._personalize_delivery(),
            'action_steps': self._create_action_steps()
        }

        return self._enhance_relevance(intervention)

    def track_effectiveness(self, intervention_id, outcomes):
        """Monitor and analyze intervention effectiveness"""
        self.user_profile['effectiveness_metrics'][intervention_id] = {
            'behavioral_change': outcomes.get('behavior_delta', 0.0),
            'user_satisfaction': outcomes.get('satisfaction', 0.0),
            'completion_rate': outcomes.get('completion', 0.0)
        }
        self._update_learning_patterns(outcomes)

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.0),
            'context_switches': user_state.get('context_switches', 0),
            'time_pressure': user_state.get('deadline_proximity', 0.0)
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
        options = ['micro_learning', 'habit_trigger', 'reflection_prompt', 'action_nudge']
        return self._rank_options(options)[0]

    def _generate_content(self):
        """Create personalized intervention content"""
        template = self._get_content_template()
        return self._personalize_content(template)

    def _optimize_timing(self):
        """Determine optimal intervention timing"""
        return {
            'preferred_time': self._get_optimal_time(),
            'frequency': self._calculate_frequency(),
            'duration': self._estimate_duration()
        }

    def _personalize_delivery(self):
        """Customize delivery based on user preferences"""
        style = self.personality_type_configs[self.user_profile['personality_type']]
        return {
            'tone': style['communication_pref'],
            'format': style['learning_style'],
            'complexity': self._adapt_complexity()
        }

    def _create_action_steps(self):
        """Generate specific, actionable recommendations"""
        return {
            'immediate': self._generate_immediate_action(),
            'short_term': self._generate_short_term_actions(),
            'long_term': self._generate_long_term_actions()
        }

    def _enhance_relevance(self, intervention):
        """Improve intervention relevance and actionability"""
        intervention['context_markers'] = self._identify_context_markers()
        intervention['success_metrics'] = self._define_success_metrics()
        intervention['adaptation_rules'] = self._create_adaptation_rules()
        return intervention

    def _update_learning_patterns(self, outcomes):
        """Update user learning and response patterns"""
        self.user_profile['learning_patterns'].append({
            'context': self.context_tracker.copy(),
            'outcome': outcomes,
            'timestamp': self._get_timestamp()
        })
        self._optimize_future_interventions()

    def _optimize_future_interventions(self):
        """Improve future intervention effectiveness"""
        self.user_profile['intervention_sensitivity'] = self._calculate_sensitivity()
        self._update_preferred_times()
        self._adjust_delivery_parameters()