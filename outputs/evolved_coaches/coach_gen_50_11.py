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

        # Personalization tracking
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
            'deep_work': {'duration': 90, 'frequency': 180},
            'reflection': {'duration': 5, 'frequency': 120},
            'skill_building': {'duration': 15, 'frequency': 240}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention appropriateness"""
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
        
        return {
            'type': intervention_type,
            'content': self._personalize_content(intervention_type, user_profile),
            'timing': self._optimize_timing(),
            'duration': self.intervention_types[intervention_type]['duration'],
            'action_steps': self._generate_action_steps()
        }

    def update_user_model(self, interaction_result):
        """Update user model based on intervention effectiveness"""
        self.user_profile['response_history'].append(interaction_result)
        self._update_effectiveness_metrics(interaction_result)
        self._adjust_sensitivity_threshold(interaction_result)
        self._update_learning_patterns(interaction_result)

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
        return user_state.get('energy_level', 0.5)

    def _calculate_interruption_cost(self):
        """Calculate cost of interrupting current activity"""
        return (self.context_tracker['cognitive_load'] * 0.6 + 
                (1 - self.context_tracker['energy_level']) * 0.4)

    def _should_intervene(self):
        """Determine if intervention is appropriate"""
        return (self.context_tracker['interruption_cost'] < 
                self.user_profile['sensitivity_threshold'])

    def _select_intervention_type(self):
        """Select most appropriate intervention type"""
        if self.context_tracker['cognitive_load'] > 0.8:
            return 'micro_break'
        elif self.context_tracker['energy_level'] < 0.3:
            return 'deep_work'
        return 'skill_building'

    def _personalize_content(self, intervention_type, user_profile):
        """Generate personalized intervention content"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        return {
            'style': personality_config['communication_pref'],
            'format': personality_config['learning_style'],
            'intensity': self._calculate_intensity(),
            'framing': self._optimize_framing(personality_config)
        }

    def _optimize_timing(self):
        """Optimize intervention timing"""
        return {
            'suggested_time': self._find_optimal_time(),
            'flexibility': self._calculate_timing_flexibility(),
            'urgency': self._assess_urgency()
        }

    def _generate_action_steps(self):
        """Generate specific actionable recommendations"""
        return {
            'immediate': self._get_immediate_actions(),
            'short_term': self._get_short_term_actions(),
            'follow_up': self._get_follow_up_actions()
        }

    def _update_effectiveness_metrics(self, result):
        """Update intervention effectiveness tracking"""
        self.user_profile['effectiveness_metrics'].update({
            'completion_rate': self._calculate_completion_rate(result),
            'satisfaction': result.get('satisfaction', 0),
            'behavior_change': result.get('behavior_change', 0)
        })

    def _adjust_sensitivity_threshold(self, result):
        """Dynamically adjust intervention sensitivity"""
        effectiveness = result.get('effectiveness', 0)
        self.user_profile['sensitivity_threshold'] *= (1 + (effectiveness - 0.5) * 0.1)