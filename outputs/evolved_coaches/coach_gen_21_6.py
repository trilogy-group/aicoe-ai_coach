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
            'response_history': [],
            'context_preferences': {}
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
            'optimal_timing': self._determine_optimal_timing(user_id, context_data),
            'receptivity': self._calculate_receptivity(user_id, context_data)
        }

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        user_state = self.assess_context(user_id, context)
        
        if not self._should_intervene(user_id, user_state):
            return None
            
        intervention_type = self._select_intervention_type(user_state)
        content = self._generate_content(user_id, intervention_type, user_state)
        timing = self._optimize_timing(user_id, user_state)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': timing,
            'intensity': self._calculate_intensity(user_state),
            'action_steps': self._generate_action_steps(content)
        }

    def _calculate_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        base_load = context.get('task_complexity', 0.5)
        environmental_load = context.get('distractions', 0.0)
        temporal_load = context.get('time_pressure', 0.0)
        
        return min(1.0, base_load + environmental_load + temporal_load)

    def _assess_time_pressure(self, context):
        """Evaluate time pressure and deadlines"""
        return min(1.0, context.get('urgency', 0.0) + context.get('deadline_proximity', 0.0))

    def _evaluate_task_complexity(self, context):
        """Assess complexity of current task"""
        return context.get('task_complexity', 0.5)

    def _determine_optimal_timing(self, user_id, context):
        """Calculate optimal intervention timing"""
        user_patterns = self.behavioral_patterns.get(user_id, {})
        current_load = self._calculate_cognitive_load(context)
        time_of_day = context.get('time_of_day')
        
        return self._optimize_timing_window(user_patterns, current_load, time_of_day)

    def _calculate_receptivity(self, user_id, context):
        """Estimate user's receptivity to coaching"""
        base_receptivity = self.user_profiles[user_id]['receptivity']
        cognitive_load = self._calculate_cognitive_load(context)
        stress_level = self.user_profiles[user_id]['stress_level']
        
        return max(0.0, base_receptivity - cognitive_load - stress_level)

    def _should_intervene(self, user_id, state):
        """Determine if intervention is appropriate"""
        if state['cognitive_load'] > 0.8:
            return False
        if state['time_pressure'] > 0.9:
            return False
        if state['receptivity'] < 0.3:
            return False
            
        return True

    def _select_intervention_type(self, state):
        """Choose appropriate intervention type"""
        if state['cognitive_load'] > 0.6:
            return 'micro_action'
        if state['time_pressure'] > 0.7:
            return 'quick_tip'
        
        return 'full_coaching'

    def _generate_content(self, user_id, intervention_type, state):
        """Generate personalized intervention content"""
        user_profile = self.user_profiles[user_id]
        content_template = self._get_content_template(intervention_type)
        
        return self._personalize_content(content_template, user_profile, state)

    def _optimize_timing(self, user_id, state):
        """Optimize intervention timing"""
        user_patterns = self.behavioral_patterns.get(user_id, {})
        return self._calculate_optimal_delivery(user_patterns, state)

    def _calculate_intensity(self, state):
        """Calculate appropriate intervention intensity"""
        return min(1.0, 1.0 - state['cognitive_load'])

    def _generate_action_steps(self, content):
        """Generate specific actionable steps"""
        return self._break_down_actions(content)

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction"""
        profile = self.user_profiles[user_id]
        profile['response_history'].append(interaction_data)
        
        self._update_learning_patterns(user_id, interaction_data)
        self._adjust_receptivity(user_id, interaction_data)
        self._refine_context_preferences(user_id, interaction_data)

    def _update_learning_patterns(self, user_id, data):
        """Update user learning patterns"""
        profile = self.user_profiles[user_id]
        profile['learning_patterns'].append(data['learning_outcome'])
        
        if len(profile['learning_patterns']) > 10:
            profile['learning_patterns'] = profile['learning_patterns'][-10:]

    def _adjust_receptivity(self, user_id, data):
        """Adjust receptivity based on response"""
        profile = self.user_profiles[user_id]
        response_quality = data.get('response_quality', 0.5)
        
        profile['receptivity'] = (profile['receptivity'] * 0.8 + response_quality * 0.2)

    def _refine_context_preferences(self, user_id, data):
        """Refine understanding of context preferences"""
        profile = self.user_profiles[user_id]
        context = data.get('context', {})
        response = data.get('response_quality', 0.5)
        
        for key, value in context.items():
            if key not in profile['context_preferences']:
                profile['context_preferences'][key] = []
            profile['context_preferences'][key].append((value, response))