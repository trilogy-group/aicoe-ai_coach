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
            'context_preferences': {},
            'peak_performance_times': []
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate current user context for coaching opportunities"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        time_relevance = self._assess_timing_relevance(user_id, context_data)
        attention_availability = self._evaluate_attention(context_data)
        stress_indicators = self._detect_stress_patterns(context_data)
        
        return {
            'cognitive_load': cognitive_load,
            'timing_score': time_relevance,
            'attention_score': attention_availability,
            'stress_level': stress_indicators,
            'receptivity_score': self._calculate_receptivity(user_id, context_data)
        }

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        context_assessment = self.assess_context(user_id, context)
        
        if not self._should_intervene(context_assessment):
            return None
            
        intervention_type = self._select_intervention_type(user_id, context_assessment)
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(user_id, intervention_type, context),
            'timing': self._optimize_timing(user_id, context),
            'intensity': self._calibrate_intensity(user_id, context_assessment),
            'action_steps': self._generate_action_steps(intervention_type, context),
            'follow_up': self._plan_follow_up(user_id, intervention_type)
        }
        
        self._record_intervention(user_id, intervention)
        return intervention

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        profile = self.user_profiles[user_id]
        
        # Update cognitive state
        profile['cognitive_state'] = self._assess_cognitive_state(interaction_data)
        
        # Update learning patterns
        profile['learning_patterns'].append(self._extract_learning_pattern(interaction_data))
        
        # Update response history
        profile['response_history'].append({
            'timestamp': interaction_data['timestamp'],
            'intervention_type': interaction_data['intervention_type'],
            'effectiveness': interaction_data['effectiveness'],
            'engagement': interaction_data['engagement']
        })
        
        # Recalibrate user preferences
        self._recalibrate_preferences(user_id, interaction_data)

    def _calculate_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        task_complexity = context_data.get('task_complexity', 0.5)
        concurrent_tasks = len(context_data.get('active_tasks', []))
        time_pressure = context_data.get('time_pressure', 0.5)
        
        return (task_complexity * 0.4 + 
                min(concurrent_tasks / 5, 1.0) * 0.3 + 
                time_pressure * 0.3)

    def _assess_timing_relevance(self, user_id, context_data):
        """Evaluate optimal timing for intervention"""
        current_time = context_data['timestamp']
        peak_times = self.user_profiles[user_id]['peak_performance_times']
        
        timing_score = self._calculate_timing_alignment(current_time, peak_times)
        return timing_score * (1 - self._calculate_cognitive_load(context_data))

    def _generate_action_steps(self, intervention_type, context):
        """Generate specific, actionable steps"""
        action_templates = {
            'focus': [
                'Close distracting applications',
                'Set a timer for 25 minutes',
                'Work on single task exclusively'
            ],
            'break': [
                'Stand up and stretch',
                'Take a 5-minute walk',
                'Practice deep breathing'
            ],
            'planning': [
                'List top 3 priorities',
                'Break large task into subtasks',
                'Schedule focused work blocks'
            ]
        }
        
        base_steps = action_templates.get(intervention_type, [])
        return self._personalize_action_steps(base_steps, context)

    def _calculate_receptivity(self, user_id, context_data):
        """Calculate user's likely receptivity to coaching"""
        profile = self.user_profiles[user_id]
        
        base_receptivity = profile['receptivity']
        cognitive_load = self._calculate_cognitive_load(context_data)
        stress_level = profile['stress_level']
        
        return base_receptivity * (1 - cognitive_load) * (1 - stress_level)

    def _should_intervene(self, context_assessment):
        """Determine if intervention is appropriate"""
        return (context_assessment['receptivity_score'] > 0.6 and
                context_assessment['cognitive_load'] < 0.8 and
                context_assessment['attention_score'] > 0.4)

    def _optimize_timing(self, user_id, context):
        """Optimize intervention timing"""
        current_load = self._calculate_cognitive_load(context)
        user_patterns = self.behavioral_patterns.get(user_id, {})
        
        optimal_delay = self._calculate_optimal_delay(
            current_load,
            user_patterns,
            context
        )
        
        return {
            'delay': optimal_delay,
            'expiration': optimal_delay + 300,  # 5-minute validity
            'reminder_interval': self._calculate_reminder_interval(user_id)
        }

    def _calibrate_intensity(self, user_id, context_assessment):
        """Calibrate intervention intensity"""
        base_intensity = 0.5
        receptivity = context_assessment['receptivity_score']
        stress = context_assessment['stress_level']
        
        return min(base_intensity * (1 + receptivity) * (1 - stress), 1.0)