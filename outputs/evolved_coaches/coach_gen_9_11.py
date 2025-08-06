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

        # Personalization tracking
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preference_weights': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy_level(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity'),
            'interruption_cost': self._calculate_interruption_cost()
        })
        return self.context_tracker

    def generate_intervention(self, user_context):
        """Create personalized coaching intervention"""
        if not self._should_intervene():
            return None

        intervention = {
            'type': self._select_intervention_type(),
            'content': self._generate_content(),
            'timing': self._optimize_timing(),
            'delivery_style': self._personalize_delivery()
        }

        return self._enhance_actionability(intervention)

    def track_effectiveness(self, intervention_id, user_response):
        """Monitor and learn from intervention outcomes"""
        self.user_profile['response_history'].append({
            'intervention_id': intervention_id,
            'response': user_response,
            'context': self.context_tracker.copy(),
            'effectiveness': self._calculate_effectiveness(user_response)
        })
        self._update_learning_patterns()

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.0),
            'context_switches': user_state.get('context_switches', 0),
            'time_pressure': user_state.get('time_pressure', 0.0)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_energy_level(self, user_state):
        """Calculate user energy level considering multiple factors"""
        return user_state.get('energy_level', 0.5)

    def _calculate_interruption_cost(self):
        """Determine cost of interrupting current user activity"""
        flow_state = self.behavioral_models['flow_state']
        return flow_state['depth'] * flow_state['duration']

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (self.context_tracker['cognitive_load'] < 0.7 and
                self.context_tracker['interruption_cost'] < 0.5)

    def _select_intervention_type(self):
        """Choose most appropriate intervention type"""
        user_prefs = self.user_profile['preference_weights']
        context = self.context_tracker
        
        intervention_types = {
            'micro_break': self._score_intervention('micro_break'),
            'reflection': self._score_intervention('reflection'),
            'skill_building': self._score_intervention('skill_building'),
            'habit_reinforcement': self._score_intervention('habit_reinforcement')
        }
        
        return max(intervention_types.items(), key=lambda x: x[1])[0]

    def _generate_content(self):
        """Create personalized intervention content"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        return {
            'message': self._craft_message(config),
            'action_items': self._generate_action_items(),
            'supporting_resources': self._collect_resources()
        }

    def _optimize_timing(self):
        """Determine optimal delivery timing"""
        return {
            'preferred_time': self._calculate_preferred_time(),
            'urgency': self._calculate_urgency(),
            'expiration': self._set_expiration()
        }

    def _personalize_delivery(self):
        """Customize intervention delivery style"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        return {
            'tone': config.get('communication_pref', 'neutral'),
            'format': self._select_format(),
            'intensity': self._calculate_intensity()
        }

    def _enhance_actionability(self, intervention):
        """Make intervention more specific and actionable"""
        intervention['content']['action_items'] = [
            self._make_specific(item) for item in intervention['content']['action_items']
        ]
        intervention['content']['success_metrics'] = self._define_success_metrics()
        return intervention

    def _update_learning_patterns(self):
        """Update user learning patterns based on response history"""
        recent_responses = self.user_profile['response_history'][-10:]
        
        effectiveness_by_type = {}
        for response in recent_responses:
            intervention_type = response['intervention_id'].split('_')[0]
            effectiveness = response['effectiveness']
            
            if intervention_type not in effectiveness_by_type:
                effectiveness_by_type[intervention_type] = []
            effectiveness_by_type[intervention_type].append(effectiveness)

        self.user_profile['effectiveness_metrics'] = {
            t: sum(v)/len(v) for t, v in effectiveness_by_type.items()
        }