class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.cognitive_models = {}
        self.behavioral_patterns = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'cognitive_state': None,
            'attention_capacity': 1.0,
            'stress_level': 0.0,
            'energy_level': 1.0,
            'receptivity': 1.0,
            'learning_patterns': [],
            'response_history': [],
            'context_preferences': {},
            'peak_performance_times': []
        }
        
    def assess_cognitive_state(self, user_id, context_data):
        """Evaluate user's current cognitive state and capacity"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        attention_level = self._measure_attention_capacity(context_data)
        stress_indicators = self._detect_stress_signals(context_data)
        
        state = {
            'cognitive_load': cognitive_load,
            'attention': attention_level,
            'stress': stress_indicators,
            'time_of_day': context_data.get('time'),
            'task_complexity': context_data.get('task_complexity', 0.5)
        }
        
        self.user_profiles[user_id]['cognitive_state'] = state
        return state

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        user = self.user_profiles[user_id]
        
        # Check intervention timing and frequency
        if not self._is_good_intervention_time(user_id, context):
            return None
            
        # Select intervention type based on user state
        intervention_type = self._select_intervention_type(user)
        
        # Generate specific actionable recommendation
        recommendation = self._generate_recommendation(user, intervention_type, context)
        
        # Personalize delivery style
        delivery = self._personalize_delivery(user, recommendation)
        
        intervention = {
            'type': intervention_type,
            'content': recommendation,
            'delivery': delivery,
            'timing': context['time'],
            'expected_impact': self._predict_impact(user, recommendation)
        }
        
        self._record_intervention(user_id, intervention)
        return intervention

    def _select_intervention_type(self, user):
        """Choose most appropriate intervention type"""
        if user['cognitive_state']['stress'] > 0.7:
            return 'stress_management'
        elif user['cognitive_state']['cognitive_load'] > 0.8:
            return 'focus_enhancement'
        elif user['energy_level'] < 0.3:
            return 'energy_boost'
        else:
            return 'performance_optimization'

    def _generate_recommendation(self, user, intervention_type, context):
        """Generate specific, actionable recommendation"""
        recommendations = {
            'stress_management': [
                {'action': 'Take a 5-minute mindfulness break',
                 'rationale': 'Research shows this reduces cortisol levels by 15%'},
                {'action': 'Do 3 rounds of deep breathing exercises',
                 'rationale': 'Activates parasympathetic nervous system'}
            ],
            'focus_enhancement': [
                {'action': 'Enable do-not-disturb mode for 25 minutes',
                 'rationale': 'Eliminates attention switching costs'},
                {'action': 'Break task into smaller 15-minute segments',
                 'rationale': 'Improves focus and completion rates'}
            ],
            'energy_boost': [
                {'action': 'Take a 5-minute walking break',
                 'rationale': 'Increases blood flow and alertness'},
                {'action': 'Drink water and have a protein-rich snack',
                 'rationale': 'Stabilizes blood sugar and energy levels'}
            ],
            'performance_optimization': [
                {'action': 'Review and prioritize remaining tasks',
                 'rationale': 'Improves work efficiency by 20%'},
                {'action': 'Set a specific goal for next work block',
                 'rationale': 'Increases motivation and focus'}
            ]
        }
        
        return self._select_best_recommendation(recommendations[intervention_type], user, context)

    def _personalize_delivery(self, user, recommendation):
        """Personalize intervention delivery style"""
        tone = 'supportive' if user['stress_level'] > 0.5 else 'motivational'
        urgency = 'high' if user['cognitive_state']['cognitive_load'] > 0.7 else 'normal'
        
        return {
            'tone': tone,
            'urgency': urgency,
            'format': self._get_preferred_format(user),
            'timing_delay': self._calculate_timing_delay(user)
        }

    def process_feedback(self, user_id, intervention_id, feedback):
        """Process user feedback and update models"""
        user = self.user_profiles[user_id]
        intervention = self.intervention_history[user_id][intervention_id]
        
        self._update_effectiveness_model(user, intervention, feedback)
        self._adjust_user_preferences(user, feedback)
        self._refine_timing_model(user, feedback)
        
        return self._generate_adaptation_plan(user, feedback)

    def _calculate_cognitive_load(self, context_data):
        """Estimate current cognitive load"""
        base_load = context_data.get('task_complexity', 0.5)
        distractions = context_data.get('distraction_level', 0.3)
        time_pressure = context_data.get('time_pressure', 0.4)
        
        return min(1.0, base_load + 0.3 * distractions + 0.3 * time_pressure)

    def _is_good_intervention_time(self, user_id, context):
        """Determine if this is a good time to intervene"""
        user = self.user_profiles[user_id]
        
        # Check cognitive load
        if user['cognitive_state']['cognitive_load'] > 0.9:
            return False
            
        # Check flow state
        if self._is_in_flow_state(user):
            return False
            
        # Check intervention frequency
        if self._too_many_recent_interventions(user_id):
            return False
            
        return True

    def _predict_impact(self, user, recommendation):
        """Predict likely impact of intervention"""
        return {
            'behavior_change_probability': 0.7,
            'expected_effectiveness': 0.8,
            'user_receptivity': 0.75
        }

    def _record_intervention(self, user_id, intervention):
        """Record intervention for tracking"""
        if user_id not in self.intervention_history:
            self.intervention_history[user_id] = []
        self.intervention_history[user_id].append(intervention)