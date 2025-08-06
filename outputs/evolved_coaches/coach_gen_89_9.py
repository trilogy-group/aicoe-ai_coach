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

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {'duration': 2, 'frequency': 45},
            'deep_work': {'duration': 90, 'frequency': 180},
            'reflection': {'duration': 5, 'frequency': 120},
            'skill_building': {'duration': 15, 'frequency': 240}
        }

    def update_context(self, context_data):
        """Update context based on real-time user data"""
        self.context_tracker.update(context_data)
        self._assess_cognitive_load()
        self._update_interruption_cost()

    def generate_intervention(self, user_state):
        """Generate personalized coaching intervention"""
        if not self._should_intervene():
            return None

        intervention = self._select_optimal_intervention(user_state)
        return self._personalize_intervention(intervention)

    def _assess_cognitive_load(self):
        """Calculate current cognitive load based on multiple factors"""
        factors = [
            self.context_tracker['work_context'],
            self.context_tracker['time_of_day'],
            self.behavioral_models['flow_state']['depth']
        ]
        self.context_tracker['cognitive_load'] = sum(factors) / len(factors)

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (
            self.context_tracker['cognitive_load'] < 0.7 and
            self.context_tracker['interruption_cost'] < 0.5 and
            not self._in_deep_flow()
        )

    def _select_optimal_intervention(self, user_state):
        """Select best intervention based on current context"""
        intervention_scores = {}
        for int_type, config in self.intervention_types.items():
            score = self._calculate_intervention_score(int_type, user_state)
            intervention_scores[int_type] = score
        
        return max(intervention_scores.items(), key=lambda x: x[1])[0]

    def _personalize_intervention(self, intervention_type):
        """Customize intervention based on user profile"""
        base_intervention = self.intervention_types[intervention_type].copy()
        
        # Apply personality-based modifications
        personality = self.user_profile['personality_type']
        if personality in self.personality_type_configs:
            config = self.personality_type_configs[personality]
            base_intervention.update(self._apply_personality_mods(config))

        # Add contextual elements
        base_intervention['timing'] = self._optimize_timing()
        base_intervention['format'] = self._select_delivery_format()
        
        return base_intervention

    def update_effectiveness(self, intervention_id, metrics):
        """Update intervention effectiveness tracking"""
        self.user_profile['effectiveness_metrics'][intervention_id] = metrics
        self._adapt_intervention_weights(intervention_id, metrics)

    def _in_deep_flow(self):
        """Check if user is in flow state"""
        return (
            self.behavioral_models['flow_state']['depth'] > 0.7 and
            self.behavioral_models['flow_state']['duration'] < 120
        )

    def _calculate_intervention_score(self, int_type, user_state):
        """Score intervention suitability"""
        weights = self.user_profile['preference_weights']
        base_score = weights.get(int_type, 1.0)
        
        relevance = self._assess_relevance(int_type, user_state)
        timing = self._assess_timing_fit(int_type)
        effectiveness = self._get_historical_effectiveness(int_type)
        
        return base_score * relevance * timing * effectiveness

    def _optimize_timing(self):
        """Optimize intervention timing"""
        return {
            'optimal_time': self._calculate_optimal_time(),
            'flexibility': self._calculate_timing_flexibility(),
            'urgency': self._calculate_urgency()
        }

    def _select_delivery_format(self):
        """Select best delivery format based on context"""
        context = self.context_tracker['work_context']
        cognitive_load = self.context_tracker['cognitive_load']
        
        if cognitive_load > 0.8:
            return 'minimal_visual'
        elif context == 'focused_work':
            return 'non_intrusive'
        else:
            return 'interactive'

    def _adapt_intervention_weights(self, intervention_id, metrics):
        """Update intervention weights based on effectiveness"""
        current_weight = self.user_profile['preference_weights'].get(intervention_id, 1.0)
        effectiveness = metrics.get('effectiveness', 0.0)
        
        # Adaptive learning rate
        learning_rate = 0.1 * (1.0 - current_weight)
        new_weight = current_weight + learning_rate * (effectiveness - current_weight)
        
        self.user_profile['preference_weights'][intervention_id] = new_weight