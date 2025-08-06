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
            'intervention_success_rate': {}
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'daily_rhythm': {},
            'task_preferences': {},
            'response_patterns': {}
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate current user context for intervention timing"""
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
        if not self._should_intervene(user_id, context):
            return None
            
        user_state = self._get_user_state(user_id)
        intervention_type = self._select_intervention_type(user_state, context)
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(user_id, intervention_type),
            'timing': self._optimize_timing(user_id, context),
            'intensity': self._calculate_intensity(user_state),
            'action_steps': self._generate_action_steps(intervention_type)
        }
        
        self._record_intervention(user_id, intervention)
        return intervention

    def update_user_model(self, user_id, feedback_data):
        """Update user model based on intervention feedback"""
        success_rate = self._calculate_success_rate(feedback_data)
        self.user_profiles[user_id]['intervention_success_rate'].update(success_rate)
        
        self._update_behavioral_patterns(user_id, feedback_data)
        self._adjust_receptivity_model(user_id, feedback_data)
        self._refine_timing_model(user_id, feedback_data)

    def _calculate_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        task_load = context_data.get('task_complexity', 0.5)
        environmental_load = context_data.get('distractions', 0.3)
        temporal_load = context_data.get('time_pressure', 0.4)
        
        return (0.4 * task_load + 0.3 * environmental_load + 0.3 * temporal_load)

    def _select_intervention_type(self, user_state, context):
        """Select most appropriate intervention type"""
        if user_state['stress_level'] > 0.7:
            return 'stress_management'
        elif user_state['energy_level'] < 0.3:
            return 'energy_boost'
        elif context['cognitive_load'] > 0.8:
            return 'focus_enhancement'
        else:
            return 'productivity_optimization'

    def _generate_content(self, user_id, intervention_type):
        """Generate personalized intervention content"""
        user_patterns = self.behavioral_patterns[user_id]
        success_history = self.user_profiles[user_id]['intervention_success_rate']
        
        content = {
            'message': self._craft_message(intervention_type, user_patterns),
            'techniques': self._select_techniques(intervention_type, success_history),
            'examples': self._generate_examples(user_patterns),
            'reinforcement': self._select_reinforcement_strategy(user_id)
        }
        
        return content

    def _generate_action_steps(self, intervention_type):
        """Generate specific actionable steps"""
        action_library = {
            'stress_management': [
                'Take 3 deep breaths',
                'Stand up and stretch',
                'Do a 2-minute mindfulness exercise'
            ],
            'energy_boost': [
                'Take a 5-minute walk',
                'Drink water',
                'Do 10 jumping jacks'
            ],
            'focus_enhancement': [
                'Clear desk of distractions',
                'Set a 25-minute timer',
                'Write down current task goal'
            ],
            'productivity_optimization': [
                'Break task into smaller steps',
                'Set specific completion criteria',
                'Schedule next break time'
            ]
        }
        
        return action_library.get(intervention_type, [])

    def _optimize_timing(self, user_id, context):
        """Optimize intervention timing"""
        daily_rhythm = self.behavioral_patterns[user_id]['daily_rhythm']
        current_load = context['cognitive_load']
        
        optimal_time = self._calculate_optimal_time(daily_rhythm, current_load)
        return optimal_time

    def _calculate_receptivity(self, user_id, context):
        """Calculate user receptivity to interventions"""
        base_receptivity = self.user_profiles[user_id]['receptivity']
        context_modifier = self._get_context_modifier(context)
        time_modifier = self._get_time_modifier(user_id)
        
        return base_receptivity * context_modifier * time_modifier

    def _should_intervene(self, user_id, context):
        """Determine if intervention is appropriate"""
        receptivity = self._calculate_receptivity(user_id, context)
        last_intervention = self._get_last_intervention_time(user_id)
        cognitive_load = context['cognitive_load']
        
        return (receptivity > 0.6 and 
                cognitive_load < 0.8 and 
                self._sufficient_time_elapsed(last_intervention))

    def _record_intervention(self, user_id, intervention):
        """Record intervention for tracking"""
        self.intervention_history[user_id].append({
            'timestamp': self._get_current_time(),
            'intervention': intervention,
            'context': self._get_current_context(user_id)
        })