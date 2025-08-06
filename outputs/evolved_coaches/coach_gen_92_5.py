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
            'resistance': {'current': 0.0, 'threshold': 0.7}
        }

        # User profile and adaptation
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'success_metrics': {},
            'preference_weights': {}
        }

        # Intervention strategies
        self.intervention_types = {
            'micro_nudge': {'duration': 30, 'cognitive_load': 0.1},
            'quick_reflection': {'duration': 120, 'cognitive_load': 0.3},
            'deep_insight': {'duration': 300, 'cognitive_load': 0.7}
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

        intervention_type = self._select_intervention_type()
        
        intervention = {
            'content': self._generate_content(intervention_type),
            'timing': self._optimize_timing(),
            'format': self._personalize_format(user_profile),
            'action_steps': self._create_action_steps(),
            'follow_up': self._plan_follow_up()
        }
        
        return intervention

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'context_switches': user_state.get('context_switches', 0),
            'time_pressure': user_state.get('time_pressure', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_energy_level(self, user_state):
        """Estimate user energy level"""
        factors = {
            'time_since_break': user_state.get('time_since_break', 0),
            'task_intensity': user_state.get('task_intensity', 0.5),
            'biorhythm': self._calculate_biorhythm()
        }
        return sum(factors.values()) / len(factors)

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (
            self.context_tracker['cognitive_load'] < 0.8 and
            self.context_tracker['interruption_cost'] < 0.6 and
            self.behavioral_models['resistance']['current'] < 
            self.behavioral_models['resistance']['threshold']
        )

    def _select_intervention_type(self):
        """Choose appropriate intervention type based on context"""
        if self.context_tracker['cognitive_load'] > 0.6:
            return 'micro_nudge'
        elif self.context_tracker['energy_level'] > 0.7:
            return 'deep_insight'
        return 'quick_reflection'

    def _generate_content(self, intervention_type):
        """Generate personalized intervention content"""
        template = self._get_content_template(intervention_type)
        return self._personalize_content(template)

    def _optimize_timing(self):
        """Optimize intervention timing"""
        return {
            'delay': self._calculate_optimal_delay(),
            'duration': self.intervention_types[self._select_intervention_type()]['duration'],
            'follow_up_interval': self._calculate_follow_up_interval()
        }

    def _personalize_format(self, user_profile):
        """Personalize intervention format"""
        ptype = user_profile['personality_type']
        return {
            'style': self.personality_type_configs[ptype]['communication_pref'],
            'complexity': self._adapt_complexity(),
            'medium': self._select_medium(ptype)
        }

    def _create_action_steps(self):
        """Generate specific actionable steps"""
        return {
            'immediate': self._generate_immediate_action(),
            'short_term': self._generate_short_term_actions(),
            'long_term': self._generate_long_term_actions()
        }

    def update_user_profile(self, interaction_data):
        """Update user profile based on interaction"""
        self.user_profile['response_history'].append(interaction_data)
        self._update_success_metrics(interaction_data)
        self._adapt_preferences(interaction_data)
        self._update_learning_patterns(interaction_data)

    def _update_success_metrics(self, interaction_data):
        """Update intervention success metrics"""
        metrics = self.user_profile['success_metrics']
        metrics['engagement'] = self._calculate_engagement(interaction_data)
        metrics['effectiveness'] = self._calculate_effectiveness(interaction_data)
        metrics['satisfaction'] = self._calculate_satisfaction(interaction_data)

    def get_performance_metrics(self):
        """Return current performance metrics"""
        return {
            'user_satisfaction': self._calculate_satisfaction_score(),
            'behavioral_change': self._calculate_behavior_change(),
            'intervention_relevance': self._calculate_relevance(),
            'actionability': self._calculate_actionability()
        }