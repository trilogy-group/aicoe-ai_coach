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
        self.behavioral_patterns = {
            'response_history': [],
            'intervention_effectiveness': {},
            'habit_formation_progress': {},
            'motivation_triggers': set(),
            'resistance_patterns': []
        }

        # Personalization engine
        self.user_profile = {
            'personality_type': None,
            'learning_preferences': [],
            'peak_performance_times': [],
            'productivity_patterns': {},
            'feedback_responses': [],
            'goal_progress': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        temporal_context = self._analyze_temporal_patterns(environment_data)
        work_phase = self._detect_work_phase(user_state)

        return {
            'receptivity_score': self._calculate_receptivity(cognitive_load, temporal_context),
            'intervention_timing': self._optimize_timing(work_phase),
            'context_appropriateness': self._evaluate_context_fit(environment_data)
        }

    def generate_intervention(self, context_assessment, user_profile):
        """Create personalized coaching intervention"""
        intervention_type = self._select_intervention_type(context_assessment)
        content = self._personalize_content(intervention_type, user_profile)
        delivery = self._optimize_delivery_method(user_profile)

        return {
            'content': content,
            'timing': self._get_optimal_timing(),
            'format': delivery,
            'intensity': self._calculate_intensity(context_assessment),
            'follow_up': self._plan_follow_up(intervention_type)
        }

    def track_effectiveness(self, intervention, user_response):
        """Monitor and analyze intervention effectiveness"""
        self.behavioral_patterns['response_history'].append({
            'intervention': intervention,
            'response': user_response,
            'context': self.context_tracker.copy(),
            'timestamp': self._get_timestamp()
        })

        self._update_effectiveness_metrics(intervention, user_response)
        self._adjust_strategies(user_response)

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'time_pressure': user_state.get('time_pressure', 0),
            'interruption_frequency': self.context_tracker['interruption_count'],
            'focus_duration': self.context_tracker['focus_duration']
        }
        
        return sum(factors.values()) / len(factors)

    def _personalize_content(self, intervention_type, user_profile):
        """Create highly personalized intervention content"""
        personality_config = self.personality_type_configs.get(
            user_profile['personality_type'], 
            self.personality_type_configs['INTJ']  # Default fallback
        )

        return {
            'message': self._generate_message(personality_config),
            'tone': personality_config['communication_pref'],
            'complexity': self._adjust_complexity(personality_config['learning_style']),
            'examples': self._get_relevant_examples(user_profile),
            'action_steps': self._generate_action_steps(intervention_type)
        }

    def _optimize_timing(self, work_phase):
        """Determine optimal intervention timing"""
        return {
            'immediate_receptivity': self._calculate_immediate_receptivity(),
            'optimal_delay': self._calculate_optimal_delay(work_phase),
            'frequency_limit': self._get_frequency_limit(),
            'do_not_disturb': self._check_dnd_conditions()
        }

    def _adjust_strategies(self, user_response):
        """Adapt coaching strategies based on user response"""
        effectiveness = self._calculate_response_effectiveness(user_response)
        
        if effectiveness < 0.5:
            self._modify_approach()
            self._update_user_preferences()
        
        self._reinforce_successful_patterns(effectiveness)

    def _generate_action_steps(self, intervention_type):
        """Create specific, actionable recommendations"""
        return {
            'immediate_action': self._get_immediate_action(intervention_type),
            'short_term_steps': self._get_short_term_steps(),
            'long_term_strategy': self._get_long_term_strategy(),
            'progress_metrics': self._define_progress_metrics()
        }

    def _calculate_receptivity(self, cognitive_load, temporal_context):
        """Calculate user receptivity to interventions"""
        factors = {
            'cognitive_bandwidth': 1 - cognitive_load,
            'temporal_appropriateness': temporal_context.get('appropriateness', 0),
            'energy_level': self.context_tracker['energy_level'],
            'recent_intervention_count': len(self.behavioral_patterns['response_history'][-5:])
        }
        
        return sum(factors.values()) / len(factors)

    def update_user_profile(self, new_data):
        """Update user profile with new behavioral data"""
        self.user_profile.update(new_data)
        self._recalibrate_personalization()
        self._update_effectiveness_metrics()