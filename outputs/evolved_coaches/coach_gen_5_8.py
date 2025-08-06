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
            'effectiveness_metrics': {},
            'preferred_times': [],
            'attention_spans': []
        }

        # Intervention strategies
        self.strategies = {
            'micro_breaks': self._generate_micro_break,
            'deep_work': self._generate_deep_work_prompt,
            'habit_building': self._generate_habit_prompt,
            'flow_protection': self._protect_flow_state
        }

    def update_context(self, context_data):
        """Update context based on real-time user data"""
        self.context_tracker.update(context_data)
        self._assess_intervention_timing()
        self._update_behavioral_models()

    def generate_intervention(self):
        """Generate personalized coaching intervention"""
        if not self._should_intervene():
            return None

        strategy = self._select_best_strategy()
        intervention = self.strategies[strategy]()
        
        return self._personalize_intervention(intervention)

    def _assess_intervention_timing(self):
        """Determine optimal intervention timing"""
        cognitive_load = self.context_tracker['cognitive_load']
        energy_level = self.context_tracker['energy_level']
        flow_state = self.behavioral_models['flow_state']['depth']

        return (cognitive_load < 0.7 and 
                energy_level > 0.3 and 
                flow_state < 0.8)

    def _select_best_strategy(self):
        """Choose most effective intervention strategy"""
        context = self.context_tracker
        user = self.user_profile
        
        if context['cognitive_load'] > 0.8:
            return 'micro_breaks'
        elif context['work_context'] == 'focused':
            return 'deep_work'
        elif self._is_habit_building_opportunity():
            return 'habit_building'
        else:
            return 'flow_protection'

    def _personalize_intervention(self, intervention):
        """Customize intervention based on user profile"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs[personality]

        intervention.update({
            'tone': config['communication_pref'],
            'complexity': self._adjust_complexity(),
            'timing': self._optimize_timing(),
            'format': config['learning_style']
        })

        return intervention

    def _generate_micro_break(self):
        """Generate context-aware micro break suggestion"""
        return {
            'type': 'micro_break',
            'duration': self._calculate_optimal_break_duration(),
            'activity': self._select_break_activity(),
            'urgency': self._calculate_break_urgency()
        }

    def _generate_deep_work_prompt(self):
        """Generate deep work session guidance"""
        return {
            'type': 'deep_work',
            'duration': self._calculate_optimal_session_length(),
            'preparation': self._generate_preparation_steps(),
            'environment': self._suggest_environment_optimization()
        }

    def _generate_habit_prompt(self):
        """Generate habit building intervention"""
        return {
            'type': 'habit_building',
            'cue': self._identify_habit_cue(),
            'action': self._suggest_habit_action(),
            'reward': self._suggest_habit_reward(),
            'tracking': self._generate_tracking_method()
        }

    def _protect_flow_state(self):
        """Generate flow state protection intervention"""
        return {
            'type': 'flow_protection',
            'barriers': self._identify_flow_barriers(),
            'environment': self._optimize_flow_environment(),
            'duration': self._suggest_flow_duration()
        }

    def _should_intervene(self):
        """Determine if intervention is appropriate"""
        return (self._assess_intervention_timing() and
                not self._is_in_deep_flow() and
                self._sufficient_time_since_last())

    def _update_behavioral_models(self):
        """Update behavioral tracking models"""
        self.behavioral_models['motivation'] = self._assess_motivation()
        self.behavioral_models['flow_state'] = self._assess_flow()
        self.behavioral_models['resistance'] = self._assess_resistance()

    def record_feedback(self, feedback):
        """Record and process intervention feedback"""
        self.user_profile['response_history'].append(feedback)
        self._update_effectiveness_metrics(feedback)
        self._adapt_strategies(feedback)

    def _adapt_strategies(self, feedback):
        """Adapt intervention strategies based on feedback"""
        if feedback['effectiveness'] < 0.5:
            self._adjust_approach()
        self._update_timing_preferences(feedback)
        self._refine_personalization(feedback)