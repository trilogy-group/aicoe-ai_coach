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
            'burnout_risk': 0.0
        }

        # Personalization parameters
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preferred_times': [],
            'sensitivity_threshold': 0.7
        }

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {'duration': 2, 'frequency': 45},
            'deep_work': {'duration': 25, 'frequency': 90},
            'reflection': {'duration': 5, 'frequency': 120},
            'skill_building': {'duration': 15, 'frequency': 240}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention appropriateness"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        interruption_cost = self._estimate_interruption_cost(user_state)
        timing_score = self._evaluate_timing(environment_data)

        return {
            'cognitive_load': cognitive_load,
            'interruption_cost': interruption_cost,
            'timing_score': timing_score,
            'intervention_appropriate': timing_score > self.user_profile['sensitivity_threshold']
        }

    def generate_intervention(self, context_assessment):
        """Create personalized coaching intervention"""
        if not context_assessment['intervention_appropriate']:
            return None

        intervention_type = self._select_intervention_type(context_assessment)
        personalized_content = self._personalize_content(intervention_type)
        
        return {
            'type': intervention_type,
            'content': personalized_content,
            'timing': self._optimize_timing(),
            'duration': self.intervention_types[intervention_type]['duration'],
            'follow_up': self._create_follow_up_plan()
        }

    def update_effectiveness(self, intervention_result):
        """Update intervention effectiveness metrics"""
        self.user_profile['response_history'].append(intervention_result)
        self._update_learning_patterns(intervention_result)
        self._adjust_sensitivity_threshold(intervention_result)
        self._optimize_intervention_params(intervention_result)

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'time_pressure': user_state.get('time_pressure', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'fatigue_level': user_state.get('fatigue', 0.4)
        }
        
        return sum(factors.values()) / len(factors)

    def _estimate_interruption_cost(self, user_state):
        """Calculate cost of interrupting current work"""
        flow_state = self.behavioral_models['flow_state']['depth']
        task_importance = user_state.get('task_importance', 0.5)
        deadline_pressure = user_state.get('deadline_pressure', 0.5)
        
        return (flow_state * 0.4 + task_importance * 0.3 + deadline_pressure * 0.3)

    def _evaluate_timing(self, environment_data):
        """Determine optimal timing for intervention"""
        time_factors = {
            'time_since_last': environment_data.get('time_since_last_intervention', 0),
            'time_of_day_score': self._get_time_of_day_score(),
            'energy_level': self.context_tracker['energy_level'],
            'scheduled_meetings': environment_data.get('upcoming_meetings', [])
        }
        
        return self._calculate_timing_score(time_factors)

    def _select_intervention_type(self, context):
        """Choose most appropriate intervention type"""
        if context['cognitive_load'] > 0.8:
            return 'micro_break'
        elif context['timing_score'] > 0.9:
            return 'deep_work'
        elif context['cognitive_load'] < 0.3:
            return 'skill_building'
        else:
            return 'reflection'

    def _personalize_content(self, intervention_type):
        """Create personalized intervention content"""
        personality = self.user_profile['personality_type']
        learning_style = self.personality_type_configs[personality]['learning_style']
        comm_pref = self.personality_type_configs[personality]['communication_pref']
        
        return self._generate_content(intervention_type, learning_style, comm_pref)

    def _optimize_timing(self):
        """Optimize intervention timing"""
        preferred_times = self.user_profile['preferred_times']
        current_load = self.context_tracker['cognitive_load']
        energy_level = self.context_tracker['energy_level']
        
        return self._calculate_optimal_time(preferred_times, current_load, energy_level)

    def _create_follow_up_plan(self):
        """Generate follow-up actions and measurements"""
        return {
            'check_points': [15, 30, 60],
            'success_metrics': ['task_completion', 'energy_level', 'satisfaction'],
            'adjustment_triggers': {'low_response': 'increase_frequency', 'high_stress': 'reduce_intensity'}
        }

    def _update_learning_patterns(self, result):
        """Update user learning and response patterns"""
        self.user_profile['learning_patterns'].append({
            'intervention_type': result['type'],
            'effectiveness': result['effectiveness'],
            'context': self.context_tracker.copy()
        })

    def _adjust_sensitivity_threshold(self, result):
        """Dynamically adjust intervention sensitivity"""
        if result['effectiveness'] < 0.5:
            self.user_profile['sensitivity_threshold'] *= 1.1
        else:
            self.user_profile['sensitivity_threshold'] *= 0.9
        
        self.user_profile['sensitivity_threshold'] = max(0.3, min(0.9, self.user_profile['sensitivity_threshold']))