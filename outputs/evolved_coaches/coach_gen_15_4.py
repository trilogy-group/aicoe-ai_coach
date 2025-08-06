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
        
        profile['cognitive_state'] = self._update_cognitive_model(
            profile['cognitive_state'], 
            interaction_data
        )
        
        profile['learning_patterns'].append(interaction_data)
        profile['response_history'].append(interaction_data['response'])
        
        self._update_timing_model(user_id, interaction_data)
        self._update_context_preferences(user_id, interaction_data)
        
    def _calculate_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        base_load = context_data.get('task_complexity', 0.5)
        environmental_load = context_data.get('distractions', 0.0)
        temporal_load = context_data.get('time_pressure', 0.0)
        
        return min(1.0, base_load + 0.3 * environmental_load + 0.2 * temporal_load)

    def _assess_timing_relevance(self, user_id, context_data):
        """Evaluate optimal timing for intervention"""
        current_time = context_data['timestamp']
        profile = self.user_profiles[user_id]
        
        time_relevance = self._compare_peak_times(current_time, profile['peak_performance_times'])
        context_relevance = self._evaluate_context_timing(context_data)
        
        return 0.7 * time_relevance + 0.3 * context_relevance

    def _generate_action_steps(self, intervention_type, context):
        """Generate specific, actionable recommendations"""
        action_templates = {
            'focus': [
                'Close distracting applications',
                'Set a timer for 25 minutes of focused work',
                'Take a 5 minute break after completion'
            ],
            'stress': [
                'Take 3 deep breaths',
                'Stand up and stretch for 2 minutes',
                'Review and prioritize your task list'
            ],
            'energy': [
                'Take a short walk',
                'Drink water',
                'Do 5 minutes of energizing exercises'
            ]
        }
        
        base_actions = action_templates.get(intervention_type, [])
        return self._personalize_actions(base_actions, context)

    def _should_intervene(self, context_assessment):
        """Determine if intervention is appropriate"""
        if context_assessment['cognitive_load'] > 0.8:
            return False
            
        if context_assessment['stress_level'] > 0.9:
            return False
            
        return (context_assessment['receptivity_score'] > 0.6 and
                context_assessment['attention_score'] > 0.4)

    def _calculate_receptivity(self, user_id, context_data):
        """Calculate user's likely receptivity to coaching"""
        profile = self.user_profiles[user_id]
        
        base_receptivity = profile['receptivity']
        time_factor = self._get_time_receptivity(context_data)
        context_factor = self._get_context_receptivity(context_data)
        
        return min(1.0, base_receptivity * time_factor * context_factor)

    def _record_intervention(self, user_id, intervention):
        """Record intervention for learning and adaptation"""
        if user_id not in self.intervention_history:
            self.intervention_history[user_id] = []
            
        self.intervention_history[user_id].append({
            'timestamp': intervention['timing'],
            'type': intervention['type'],
            'context': intervention['content'],
            'intensity': intervention['intensity']
        })

    def _personalize_actions(self, base_actions, context):
        """Customize action steps based on context"""
        personalized = []
        for action in base_actions:
            modified_action = self._adapt_to_context(action, context)
            if modified_action:
                personalized.append(modified_action)
        return personalized