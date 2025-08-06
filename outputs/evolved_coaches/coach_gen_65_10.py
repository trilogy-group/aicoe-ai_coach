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
            'preferred_times': [],
            'sensitivity_threshold': 0.7
        }

    def assess_context(self, user_state, environment_data):
        """Evaluates current user context for intervention appropriateness"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._assess_energy_level(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity')
        })
        
        return self._calculate_intervention_readiness()

    def generate_intervention(self, context_score):
        """Creates personalized coaching intervention"""
        if not self._should_intervene(context_score):
            return None
            
        intervention_type = self._select_intervention_type()
        content = self._personalize_content(intervention_type)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': self._optimize_timing(),
            'action_steps': self._generate_action_steps()
        }

    def _calculate_cognitive_load(self, user_state):
        """Estimates current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'focus_duration': user_state.get('focus_time', 0.0)
        }
        
        return sum(factors.values()) / len(factors)

    def _assess_energy_level(self, user_state):
        """Evaluates user energy level for intervention timing"""
        return user_state.get('energy', 0.5)

    def _calculate_intervention_readiness(self):
        """Determines if user is ready for an intervention"""
        weights = {
            'cognitive_load': 0.3,
            'energy_level': 0.2,
            'time_appropriateness': 0.3,
            'context_relevance': 0.2
        }
        
        scores = {
            'cognitive_load': 1 - self.context_tracker['cognitive_load'],
            'energy_level': self.context_tracker['energy_level'],
            'time_appropriateness': self._evaluate_timing(),
            'context_relevance': self._assess_context_relevance()
        }
        
        return sum(weights[k] * scores[k] for k in weights)

    def _should_intervene(self, context_score):
        """Determines if intervention should be made"""
        return (context_score > self.user_profile['sensitivity_threshold'] and
                not self.behavioral_models['flow_state']['current'])

    def _select_intervention_type(self):
        """Chooses most appropriate intervention type"""
        options = ['micro_learning', 'habit_prompt', 'reflection_exercise', 
                  'goal_reminder', 'break_suggestion']
        
        return self._rank_interventions(options)[0]

    def _personalize_content(self, intervention_type):
        """Personalizes intervention content for user"""
        personality_config = self.personality_type_configs[self.user_profile['personality_type']]
        
        return self._generate_content(intervention_type, personality_config)

    def _optimize_timing(self):
        """Optimizes intervention timing"""
        return {
            'preferred_time': self._get_optimal_time(),
            'frequency': self._calculate_frequency(),
            'duration': self._determine_duration()
        }

    def _generate_action_steps(self):
        """Creates specific actionable steps"""
        return [
            {'step': 1, 'action': 'Specific action description', 'duration': '5m'},
            {'step': 2, 'action': 'Next specific action', 'duration': '10m'},
            {'step': 3, 'action': 'Final specific action', 'duration': '5m'}
        ]

    def update_effectiveness(self, intervention_results):
        """Updates intervention effectiveness metrics"""
        self.user_profile['effectiveness_metrics'].update(intervention_results)
        self._adjust_parameters(intervention_results)

    def _adjust_parameters(self, results):
        """Adjusts coaching parameters based on effectiveness"""
        if results.get('success_rate', 0) < 0.5:
            self.user_profile['sensitivity_threshold'] *= 1.1
        else:
            self.user_profile['sensitivity_threshold'] *= 0.9
            
        self.user_profile['sensitivity_threshold'] = max(0.3, min(0.9, 
            self.user_profile['sensitivity_threshold']))