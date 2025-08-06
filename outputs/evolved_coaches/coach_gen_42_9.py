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
            'interruption_count': 0
        }

        # Behavioral psychology components
        self.behavioral_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'flow_state': {'duration': 0, 'depth': 0.0},
            'resistance_patterns': []
        }

        # User profile and progress tracking
        self.user_profile = {
            'personality_type': None,
            'learning_history': [],
            'response_patterns': {},
            'achievement_metrics': {},
            'preference_weights': {}
        }

        # Intervention strategies
        self.intervention_library = {
            'micro_breaks': self._generate_micro_break_suggestions,
            'deep_work': self._generate_focus_interventions,
            'habit_building': self._generate_habit_interventions,
            'energy_management': self._generate_energy_interventions
        }

    def update_context(self, context_data):
        """Update current user context based on real-time data"""
        self.context_tracker.update(context_data)
        self._assess_cognitive_load()
        self._update_behavioral_patterns()

    def generate_coaching_intervention(self):
        """Generate personalized coaching intervention based on current context"""
        if not self._should_intervene():
            return None

        intervention_type = self._select_intervention_type()
        base_intervention = self.intervention_library[intervention_type]()
        
        personalized_intervention = self._personalize_intervention(base_intervention)
        return self._format_intervention(personalized_intervention)

    def _assess_cognitive_load(self):
        """Analyze current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': self.context_tracker['work_context'].get('complexity', 0),
            'interruption_frequency': self.context_tracker['interruption_count'],
            'time_pressure': self.context_tracker['work_context'].get('deadline_proximity', 0),
            'energy_level': self.context_tracker['energy_level']
        }
        
        self.context_tracker['cognitive_load'] = sum(factors.values()) / len(factors)

    def _should_intervene(self):
        """Determine if intervention is appropriate based on context"""
        if self.context_tracker['cognitive_load'] > 0.8:
            return False  # Don't interrupt during high cognitive load
            
        if self._check_flow_state():
            return False  # Don't interrupt flow state
            
        return True

    def _select_intervention_type(self):
        """Select most appropriate intervention type based on context"""
        context = self.context_tracker
        if context['energy_level'] < 0.3:
            return 'energy_management'
        elif context['cognitive_load'] > 0.6:
            return 'micro_breaks'
        elif self._is_habit_building_opportunity():
            return 'habit_building'
        return 'deep_work'

    def _personalize_intervention(self, intervention):
        """Customize intervention based on user profile and preferences"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs[personality]
        
        intervention.update({
            'tone': config['communication_pref'],
            'complexity': self._adjust_complexity(),
            'timing': self._optimize_timing(),
            'format': self._select_format()
        })
        
        return intervention

    def _generate_micro_break_suggestions(self):
        """Generate context-aware micro-break recommendations"""
        return {
            'type': 'micro_break',
            'duration': self._calculate_optimal_break_duration(),
            'activity': self._select_break_activity(),
            'expected_benefit': self._calculate_expected_benefit()
        }

    def _generate_focus_interventions(self):
        """Generate deep work optimization suggestions"""
        return {
            'type': 'focus_optimization',
            'duration': self._calculate_focus_session_length(),
            'environment': self._suggest_environment_optimizations(),
            'preparation': self._generate_preparation_steps()
        }

    def _generate_habit_interventions(self):
        """Generate habit formation suggestions"""
        return {
            'type': 'habit_building',
            'cue': self._identify_habit_cue(),
            'routine': self._suggest_habit_routine(),
            'reward': self._suggest_habit_reward(),
            'tracking': self._generate_tracking_method()
        }

    def _generate_energy_interventions(self):
        """Generate energy management suggestions"""
        return {
            'type': 'energy_management',
            'activity': self._suggest_energy_activity(),
            'duration': self._calculate_recovery_duration(),
            'expected_impact': self._calculate_energy_impact()
        }

    def _format_intervention(self, intervention):
        """Format intervention for delivery"""
        return {
            'message': self._generate_message(intervention),
            'action_items': self._extract_action_items(intervention),
            'timing': intervention['timing'],
            'priority': self._calculate_priority(intervention),
            'delivery_method': self._select_delivery_method(intervention)
        }

    def update_user_profile(self, feedback_data):
        """Update user profile based on intervention feedback"""
        self.user_profile['learning_history'].append(feedback_data)
        self._update_preference_weights(feedback_data)
        self._refine_response_patterns(feedback_data)