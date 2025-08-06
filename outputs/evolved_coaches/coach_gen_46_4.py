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
            'engagement_level': 0.5,
            'learning_patterns': [],
            'response_history': [],
            'context_preferences': {},
            'peak_performance_times': []
        }
        
    def assess_cognitive_state(self, user_id, context_data):
        """Evaluate user's current cognitive state and capacity"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        attention_score = self._measure_attention_availability(context_data)
        stress_indicators = self._detect_stress_signals(context_data)
        
        return {
            'cognitive_load': cognitive_load,
            'attention': attention_score,
            'stress': stress_indicators,
            'receptivity': self._calculate_receptivity(cognitive_load, attention_score)
        }

    def generate_personalized_intervention(self, user_id, context):
        """Create tailored coaching intervention based on user state and context"""
        user_state = self.assess_cognitive_state(user_id, context)
        
        if not self._is_appropriate_time(user_id, context):
            return None
            
        intervention_type = self._select_intervention_type(user_state)
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(user_id, intervention_type),
            'intensity': self._calculate_intensity(user_state),
            'timing': self._optimize_timing(user_id, context),
            'action_steps': self._generate_action_steps(intervention_type),
            'follow_up': self._plan_follow_up(user_id)
        }
        
        return self._format_intervention(intervention)

    def track_response(self, user_id, intervention_id, response_data):
        """Record and analyze user response to intervention"""
        self.intervention_history[user_id].append({
            'intervention_id': intervention_id,
            'response': response_data,
            'effectiveness': self._calculate_effectiveness(response_data),
            'timestamp': response_data['timestamp']
        })
        
        self._update_user_model(user_id, response_data)

    def _calculate_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        task_complexity = context_data.get('task_complexity', 0.5)
        concurrent_tasks = len(context_data.get('active_tasks', []))
        time_pressure = context_data.get('deadline_proximity', 0.0)
        
        return (task_complexity * 0.4 + 
                min(concurrent_tasks / 5, 1.0) * 0.3 + 
                time_pressure * 0.3)

    def _measure_attention_availability(self, context_data):
        """Evaluate user's current attention capacity"""
        focus_indicators = context_data.get('focus_metrics', {})
        interruption_frequency = context_data.get('interruptions_per_hour', 0)
        deep_work_state = context_data.get('deep_work_duration', 0)
        
        return self._calculate_attention_score(
            focus_indicators, 
            interruption_frequency,
            deep_work_state
        )

    def _select_intervention_type(self, user_state):
        """Choose appropriate intervention based on user state"""
        if user_state['cognitive_load'] > 0.8:
            return 'stress_management'
        elif user_state['attention'] < 0.4:
            return 'focus_enhancement'
        elif user_state['stress'] > 0.7:
            return 'wellbeing_support'
        else:
            return 'performance_optimization'

    def _generate_action_steps(self, intervention_type):
        """Create specific, actionable recommendations"""
        action_templates = {
            'stress_management': [
                'Take a 5-minute breathing break',
                'Do a quick stretching routine',
                'Write down your top concerns'
            ],
            'focus_enhancement': [
                'Clear your workspace',
                'Set a 25-minute focus timer',
                'Turn off notifications'
            ],
            'wellbeing_support': [
                'Take a short walk',
                'Drink water',
                'Do a quick meditation'
            ],
            'performance_optimization': [
                'Review your priorities',
                'Break task into smaller steps',
                'Schedule focused work blocks'
            ]
        }
        
        return action_templates.get(intervention_type, [])

    def _optimize_timing(self, user_id, context):
        """Determine optimal intervention timing"""
        user_patterns = self.behavioral_patterns.get(user_id, {})
        current_load = self._calculate_cognitive_load(context)
        time_of_day = context.get('time_of_day')
        
        return self._calculate_optimal_timing(
            user_patterns,
            current_load,
            time_of_day
        )

    def _calculate_effectiveness(self, response_data):
        """Measure intervention effectiveness"""
        engagement = response_data.get('engagement_level', 0)
        completion = response_data.get('action_completion', 0)
        sentiment = response_data.get('response_sentiment', 0)
        
        return (engagement * 0.4 + completion * 0.4 + sentiment * 0.2)

    def _update_user_model(self, user_id, response_data):
        """Update user model based on intervention response"""
        effectiveness = self._calculate_effectiveness(response_data)
        
        self.user_profiles[user_id]['learning_patterns'].append({
            'intervention_type': response_data['intervention_type'],
            'effectiveness': effectiveness,
            'context': response_data['context']
        })
        
        self._refine_personalization(user_id)

    def _refine_personalization(self, user_id):
        """Improve personalization based on accumulated data"""
        learning_patterns = self.user_profiles[user_id]['learning_patterns']
        
        if len(learning_patterns) >= 5:
            self._update_intervention_preferences(user_id, learning_patterns)
            self._update_timing_preferences(user_id, learning_patterns)
            self._update_content_preferences(user_id, learning_patterns)