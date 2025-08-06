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
            'intervention_sensitivity': 0.0
        }

    def assess_context(self, user_state, environment_data):
        """Evaluates current user context for intervention timing"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy_level(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity')
        })
        return self._should_intervene()

    def generate_intervention(self, context):
        """Creates personalized coaching intervention"""
        if not self._is_appropriate_timing():
            return None
            
        intervention_type = self._select_intervention_type()
        content = self._personalize_content(intervention_type)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': self._optimize_timing(),
            'action_steps': self._generate_action_steps()
        }

    def update_user_model(self, interaction_data):
        """Updates user model based on intervention responses"""
        self.user_profile['response_history'].append(interaction_data)
        self._update_effectiveness_metrics(interaction_data)
        self._adjust_intervention_parameters()
        self._update_learning_patterns()

    def _calculate_cognitive_load(self, user_state):
        """Estimates current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'interruption_frequency': user_state.get('interruptions', 0),
            'focus_duration': user_state.get('focus_time', 0)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_energy_level(self, user_state):
        """Estimates user energy level for optimal intervention"""
        return user_state.get('energy_level', 0.5)

    def _should_intervene(self):
        """Determines if intervention is appropriate"""
        if self.behavioral_models['flow_state']['current']:
            return False
            
        return (
            self.context_tracker['cognitive_load'] < 0.7 and
            self.context_tracker['energy_level'] > 0.3 and
            self._check_intervention_spacing()
        )

    def _select_intervention_type(self):
        """Selects most appropriate intervention type"""
        user_state = self._get_current_state()
        if user_state['needs_motivation']:
            return 'motivation_boost'
        elif user_state['needs_focus']:
            return 'focus_enhancement'
        return 'progress_check'

    def _personalize_content(self, intervention_type):
        """Personalizes intervention content"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        return self._generate_content_template(
            intervention_type,
            config['communication_pref'],
            config['learning_style']
        )

    def _optimize_timing(self):
        """Optimizes intervention timing"""
        preferred_times = self.user_profile['preferred_times']
        current_time = self.context_tracker['time_of_day']
        return self._find_optimal_time(preferred_times, current_time)

    def _generate_action_steps(self):
        """Generates specific actionable steps"""
        return [
            {
                'step': 'specific_action',
                'timeframe': 'immediate',
                'difficulty': 'achievable',
                'measurement': 'trackable_metric'
            }
        ]

    def _update_effectiveness_metrics(self, interaction_data):
        """Updates intervention effectiveness tracking"""
        metrics = self.user_profile['effectiveness_metrics']
        metrics['response_rate'] = self._calculate_response_rate()
        metrics['behavior_change'] = self._measure_behavior_change()
        metrics['satisfaction'] = interaction_data.get('satisfaction', 0)

    def _adjust_intervention_parameters(self):
        """Adjusts intervention parameters based on effectiveness"""
        effectiveness = self.user_profile['effectiveness_metrics']
        self.user_profile['intervention_sensitivity'] = self._calibrate_sensitivity(effectiveness)

    def _update_learning_patterns(self):
        """Updates user learning patterns"""
        recent_responses = self.user_profile['response_history'][-10:]
        self.user_profile['learning_patterns'] = self._analyze_learning_patterns(recent_responses)

    def _check_intervention_spacing(self):
        """Ensures appropriate spacing between interventions"""
        recent = self.context_tracker['recent_interventions']
        if not recent:
            return True
        return (time.time() - recent[-1]) > self._get_minimum_spacing()