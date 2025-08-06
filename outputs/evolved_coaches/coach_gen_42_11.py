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
            'task_complexity': 0.0
        }

        # Behavioral psychology components
        self.behavioral_patterns = {
            'response_history': [],
            'intervention_effectiveness': {},
            'habit_formation_progress': {},
            'motivation_triggers': set(),
            'resistance_patterns': {}
        }

        # User profile and personalization
        self.user_profile = {
            'personality_type': None,
            'learning_preferences': {},
            'peak_performance_times': [],
            'stress_indicators': [],
            'success_patterns': {},
            'challenge_areas': set()
        }

        # Intervention strategies
        self.intervention_library = {
            'micro_breaks': self._generate_micro_break_suggestions,
            'focus_enhancement': self._generate_focus_interventions,
            'stress_management': self._generate_stress_interventions,
            'productivity_optimization': self._generate_productivity_nudges,
            'habit_building': self._generate_habit_interventions
        }

    def update_context(self, context_data):
        """Update current user context based on real-time data"""
        self.context_tracker.update(context_data)
        self._analyze_cognitive_load()
        self._update_intervention_timing()

    def generate_coaching_intervention(self):
        """Generate personalized coaching intervention based on context"""
        if not self._should_intervene():
            return None

        intervention_type = self._select_intervention_type()
        intervention = self.intervention_library[intervention_type]()
        
        return self._personalize_intervention(intervention)

    def _analyze_cognitive_load(self):
        """Analyze current cognitive load and adjust intervention threshold"""
        factors = [
            self.context_tracker['task_complexity'],
            self.context_tracker['interruption_count'],
            self.context_tracker['focus_duration']
        ]
        self.context_tracker['cognitive_load'] = sum(factors) / len(factors)

    def _should_intervene(self):
        """Determine if intervention is appropriate based on context"""
        return (
            self.context_tracker['cognitive_load'] < 0.8 and
            self._check_timing_appropriate() and
            self._check_user_receptivity()
        )

    def _select_intervention_type(self):
        """Select most appropriate intervention type based on context"""
        if self.context_tracker['cognitive_load'] > 0.6:
            return 'stress_management'
        elif self.context_tracker['focus_duration'] > 90:
            return 'micro_breaks'
        elif self._check_habit_opportunity():
            return 'habit_building'
        return 'productivity_optimization'

    def _personalize_intervention(self, intervention):
        """Customize intervention based on user profile and preferences"""
        personality_config = self.personality_type_configs.get(
            self.user_profile['personality_type']
        )
        
        return {
            'content': intervention,
            'style': personality_config['communication_pref'],
            'timing': self._optimize_timing(),
            'format': self._select_delivery_format(),
            'intensity': self._calculate_intensity()
        }

    def _generate_micro_break_suggestions(self):
        """Generate context-aware break suggestions"""
        return {
            'type': 'micro_break',
            'duration': self._calculate_optimal_break_duration(),
            'activity': self._select_break_activity(),
            'rationale': 'Maintain focus and energy levels'
        }

    def _generate_focus_interventions(self):
        """Generate focus-enhancing interventions"""
        return {
            'type': 'focus_enhancement',
            'technique': self._select_focus_technique(),
            'duration': self._calculate_focus_session_length(),
            'preparation': self._generate_focus_prep_steps()
        }

    def _generate_stress_interventions(self):
        """Generate stress management interventions"""
        return {
            'type': 'stress_management',
            'technique': self._select_stress_technique(),
            'duration': self._calculate_stress_intervention_duration(),
            'follow_up': self._generate_stress_follow_up()
        }

    def _generate_productivity_nudges(self):
        """Generate productivity optimization suggestions"""
        return {
            'type': 'productivity',
            'action': self._select_productivity_action(),
            'expected_impact': self._calculate_productivity_impact(),
            'implementation': self._generate_implementation_steps()
        }

    def _generate_habit_interventions(self):
        """Generate habit-building interventions"""
        return {
            'type': 'habit_building',
            'target_habit': self._select_habit_focus(),
            'next_step': self._generate_habit_step(),
            'reinforcement': self._select_reinforcement_strategy()
        }

    def update_effectiveness(self, intervention_id, effectiveness_score):
        """Update intervention effectiveness tracking"""
        self.behavioral_patterns['intervention_effectiveness'][intervention_id] = effectiveness_score
        self._update_learning_model(intervention_id, effectiveness_score)

    def _update_learning_model(self, intervention_id, effectiveness):
        """Update the learning model based on intervention effectiveness"""
        self.behavioral_patterns['response_history'].append({
            'intervention_id': intervention_id,
            'effectiveness': effectiveness,
            'context': self.context_tracker.copy(),
            'timestamp': self._get_current_timestamp()
        })