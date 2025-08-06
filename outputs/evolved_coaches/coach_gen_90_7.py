class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'cognitive_state': None,
            'attention_capacity': 1.0,
            'stress_level': 0.0,
            'energy_level': 1.0,
            'receptivity': 1.0,
            'learning_patterns': [],
            'intervention_response': {},
            'context_preferences': {},
            'peak_performance_times': []
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate user's current context and state"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        time_pressure = self._assess_time_pressure(context_data)
        task_complexity = self._evaluate_task_complexity(context_data)
        
        return {
            'cognitive_load': cognitive_load,
            'time_pressure': time_pressure, 
            'task_complexity': task_complexity,
            'receptivity': self._calculate_receptivity(user_id, context_data)
        }

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        user_state = self.assess_context(user_id, context)
        
        if not self._should_intervene(user_id, user_state):
            return None
            
        intervention_type = self._select_intervention_type(user_state)
        content = self._generate_content(user_id, intervention_type)
        timing = self._optimize_timing(user_id, context)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': timing,
            'intensity': self._calculate_intensity(user_state),
            'action_steps': self._generate_action_steps(content)
        }

    def track_response(self, user_id, intervention_id, response_data):
        """Track and analyze user response to intervention"""
        self.intervention_history[user_id].append({
            'intervention_id': intervention_id,
            'response': response_data,
            'context': self.user_profiles[user_id]['cognitive_state'],
            'effectiveness': self._calculate_effectiveness(response_data)
        })
        
        self._update_user_model(user_id, response_data)

    def _calculate_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        task_load = context_data.get('task_complexity', 0.5)
        time_pressure = context_data.get('time_pressure', 0.5)
        interruption_frequency = context_data.get('interruptions', 0.3)
        
        return (0.4 * task_load + 0.4 * time_pressure + 0.2 * interruption_frequency)

    def _calculate_receptivity(self, user_id, context):
        """Calculate user's receptivity to coaching"""
        base_receptivity = self.user_profiles[user_id]['receptivity']
        cognitive_load = self._calculate_cognitive_load(context)
        time_of_day_factor = self._get_time_optimization(context)
        
        return base_receptivity * (1 - cognitive_load) * time_of_day_factor

    def _select_intervention_type(self, user_state):
        """Select most appropriate intervention type"""
        if user_state['cognitive_load'] > 0.8:
            return 'micro_intervention'
        elif user_state['time_pressure'] > 0.7:
            return 'quick_tip'
        else:
            return 'full_coaching'

    def _generate_content(self, user_id, intervention_type):
        """Generate personalized intervention content"""
        user_patterns = self.behavioral_patterns.get(user_id, {})
        learning_style = self.user_profiles[user_id]['learning_patterns']
        
        content = self._get_base_content(intervention_type)
        return self._personalize_content(content, user_patterns, learning_style)

    def _generate_action_steps(self, content):
        """Generate specific, actionable steps"""
        return [
            {
                'step': i + 1,
                'action': action,
                'timeframe': self._suggest_timeframe(action),
                'success_criteria': self._define_success_criteria(action)
            }
            for i, action in enumerate(self._break_down_actions(content))
        ]

    def _optimize_timing(self, user_id, context):
        """Optimize intervention timing"""
        peak_times = self.user_profiles[user_id]['peak_performance_times']
        current_load = self._calculate_cognitive_load(context)
        
        return self._find_optimal_window(peak_times, current_load)

    def _calculate_intensity(self, user_state):
        """Calculate appropriate intervention intensity"""
        base_intensity = 0.7
        cognitive_load = user_state['cognitive_load']
        receptivity = user_state['receptivity']
        
        return base_intensity * (1 - cognitive_load) * receptivity

    def _should_intervene(self, user_id, user_state):
        """Determine if intervention is appropriate"""
        last_intervention = self.intervention_history.get(user_id, [])[-1] if self.intervention_history.get(user_id) else None
        
        if last_intervention:
            time_since_last = self._calculate_time_elapsed(last_intervention)
            if time_since_last < self._get_minimum_interval(user_state):
                return False
                
        return user_state['receptivity'] > 0.4 and user_state['cognitive_load'] < 0.9

    def _update_user_model(self, user_id, response_data):
        """Update user model based on intervention response"""
        effectiveness = self._calculate_effectiveness(response_data)
        self.user_profiles[user_id]['receptivity'] *= (0.8 + 0.2 * effectiveness)
        self._update_learning_patterns(user_id, response_data)
        self._update_behavioral_patterns(user_id, response_data)