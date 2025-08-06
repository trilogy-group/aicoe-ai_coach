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

        # User profile and personalization
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preferred_times': [],
            'intervention_sensitivity': 0.0
        }

        # Intervention strategies
        self.strategies = {
            'micro_breaks': self._generate_micro_break,
            'deep_work': self._generate_deep_work_advice,
            'habit_building': self._generate_habit_advice,
            'energy_management': self._generate_energy_advice
        }

    def update_context(self, context_data):
        """Update current user context based on real-time data"""
        self.context_tracker.update(context_data)
        self._assess_intervention_timing()
        self._update_behavioral_models()

    def generate_coaching_intervention(self):
        """Generate personalized coaching intervention based on context"""
        if not self._should_intervene():
            return None

        intervention_type = self._select_intervention_type()
        base_intervention = self.strategies[intervention_type]()
        
        personalized_intervention = self._personalize_intervention(base_intervention)
        actionable_steps = self._generate_actionable_steps(personalized_intervention)
        
        return {
            'message': personalized_intervention,
            'action_steps': actionable_steps,
            'context_relevance': self._calculate_relevance(),
            'timing_score': self._calculate_timing_score()
        }

    def _assess_intervention_timing(self):
        """Determine optimal intervention timing"""
        cognitive_load = self.context_tracker['cognitive_load']
        energy_level = self.context_tracker['energy_level']
        flow_state = self.behavioral_models['flow_state']['current']
        
        timing_score = (
            (1 - cognitive_load) * 0.4 +
            energy_level * 0.3 +
            (not flow_state) * 0.3
        )
        
        return timing_score > 0.7

    def _update_behavioral_models(self):
        """Update behavioral psychology models based on user data"""
        # Update habit formation tracking
        self.behavioral_models['habit_formation'] = self._analyze_habit_patterns()
        
        # Update motivation levels
        self.behavioral_models['motivation'] = self._assess_motivation()
        
        # Update flow state detection
        self.behavioral_models['flow_state'] = self._detect_flow_state()
        
        # Update burnout risk assessment
        self.behavioral_models['burnout_risk'] = self._calculate_burnout_risk()

    def _personalize_intervention(self, intervention):
        """Personalize intervention based on user profile"""
        personality_type = self.user_profile['personality_type']
        config = self.personality_type_configs[personality_type]
        
        return self._adapt_to_style(intervention, config['communication_pref'])

    def _generate_actionable_steps(self, intervention):
        """Generate specific, actionable steps from intervention"""
        return [
            {
                'step': f"Step {i+1}",
                'action': action,
                'timeframe': timeframe,
                'success_metric': metric
            }
            for i, (action, timeframe, metric) in enumerate(
                self._break_down_intervention(intervention)
            )
        ]

    def _should_intervene(self):
        """Determine if intervention is appropriate"""
        return (
            self._assess_intervention_timing() and
            not self.behavioral_models['flow_state']['current'] and
            self.context_tracker['interruption_cost'] < 0.7
        )

    def _calculate_relevance(self):
        """Calculate contextual relevance score"""
        context_match = self._assess_context_match()
        user_needs = self._assess_user_needs()
        timing = self._calculate_timing_score()
        
        return (context_match * 0.4 + user_needs * 0.4 + timing * 0.2)

    def _generate_micro_break(self):
        """Generate personalized micro-break suggestion"""
        energy_level = self.context_tracker['energy_level']
        cognitive_load = self.context_tracker['cognitive_load']
        
        return self._select_break_activity(energy_level, cognitive_load)

    def _generate_deep_work_advice(self):
        """Generate deep work optimization advice"""
        work_pattern = self.user_profile['personality_type']
        current_context = self.context_tracker['work_context']
        
        return self._optimize_deep_work(work_pattern, current_context)

    def _generate_habit_advice(self):
        """Generate habit formation guidance"""
        current_habits = self.behavioral_models['habit_formation']
        motivation = self.behavioral_models['motivation']
        
        return self._create_habit_strategy(current_habits, motivation)

    def _generate_energy_advice(self):
        """Generate energy management recommendations"""
        energy_pattern = self._analyze_energy_pattern()
        work_demands = self._assess_work_demands()
        
        return self._create_energy_strategy(energy_pattern, work_demands)