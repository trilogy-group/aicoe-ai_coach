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
            'recent_interventions': []
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
            'preferences': {},
            'goals': []
        }

    def assess_context(self, user_state, environment):
        """Evaluate current user context and environment"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._assess_energy_level(user_state),
            'time_of_day': environment.get('time'),
            'work_context': environment.get('context')
        })
        return self.context_tracker

    def generate_intervention(self, user_state):
        """Generate personalized coaching intervention"""
        if self._should_intervene():
            intervention = {
                'type': self._select_intervention_type(),
                'content': self._personalize_content(),
                'timing': self._optimize_timing(),
                'intensity': self._calibrate_intensity()
            }
            self._track_intervention(intervention)
            return intervention
        return None

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'time_pressure': user_state.get('deadline_pressure', 0.4)
        }
        return sum(factors.values()) / len(factors)

    def _assess_energy_level(self, user_state):
        """Calculate user energy level"""
        factors = {
            'time_since_break': user_state.get('time_since_break', 0),
            'task_duration': user_state.get('continuous_work_time', 0),
            'reported_fatigue': user_state.get('fatigue_level', 0)
        }
        return self._normalize_energy_score(factors)

    def _should_intervene(self):
        """Determine if intervention is appropriate"""
        return (
            self.context_tracker['cognitive_load'] < 0.8 and
            self._enough_time_since_last_intervention() and
            not self.behavioral_models['flow_state']['current']
        )

    def _select_intervention_type(self):
        """Choose most appropriate intervention type"""
        options = ['nudge', 'reminder', 'suggestion', 'challenge']
        return self._rank_interventions(options)

    def _personalize_content(self):
        """Generate personalized intervention content"""
        personality = self.user_profile['personality_type']
        learning_style = self.personality_type_configs[personality]['learning_style']
        
        return {
            'message': self._generate_message(learning_style),
            'format': self._select_format(learning_style),
            'difficulty': self._adjust_difficulty(),
            'actionability': self._ensure_actionable()
        }

    def _optimize_timing(self):
        """Optimize intervention timing"""
        return {
            'delay': self._calculate_optimal_delay(),
            'duration': self._determine_duration(),
            'frequency': self._adjust_frequency()
        }

    def _calibrate_intensity(self):
        """Calibrate intervention intensity"""
        return min(
            self.context_tracker['cognitive_load'],
            1 - self.behavioral_models['burnout_risk']
        )

    def _track_intervention(self, intervention):
        """Track intervention for effectiveness analysis"""
        self.context_tracker['recent_interventions'].append({
            'timestamp': self._get_timestamp(),
            'intervention': intervention,
            'context': self.context_tracker.copy()
        })

    def update_user_profile(self, feedback):
        """Update user profile based on intervention feedback"""
        self.user_profile['response_history'].append(feedback)
        self._update_effectiveness_metrics(feedback)
        self._adjust_personalization(feedback)

    def _update_effectiveness_metrics(self, feedback):
        """Update intervention effectiveness metrics"""
        metrics = self.user_profile['effectiveness_metrics']
        metrics['response_rate'] = self._calculate_response_rate()
        metrics['behavior_change'] = self._measure_behavior_change()
        metrics['satisfaction'] = self._analyze_satisfaction(feedback)

    def _adjust_personalization(self, feedback):
        """Refine personalization based on feedback"""
        self.user_profile['preferences'].update(
            self._extract_preferences(feedback)
        )
        self._update_learning_patterns(feedback)

    def get_optimization_metrics(self):
        """Return current optimization metrics"""
        return {
            'nudge_quality': self._calculate_nudge_quality(),
            'behavioral_change': self._measure_behavior_change(),
            'user_satisfaction': self._get_satisfaction_score(),
            'relevance': self._calculate_relevance(),
            'actionability': self._measure_actionability()
        }