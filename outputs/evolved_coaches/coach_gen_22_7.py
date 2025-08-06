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
        time_relevance = self._evaluate_timing(user_id, context_data['timestamp'])
        attention_availability = self._assess_attention(user_id, context_data)
        
        return {
            'cognitive_load': cognitive_load,
            'timing_score': time_relevance,
            'attention_score': attention_availability,
            'receptivity': self.user_profiles[user_id]['receptivity']
        }

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        context_assessment = self.assess_context(user_id, context)
        
        if not self._should_intervene(context_assessment):
            return None
            
        intervention_type = self._select_intervention_type(user_id, context)
        
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

    def update_user_model(self, user_id, feedback_data):
        """Update user model based on intervention feedback"""
        profile = self.user_profiles[user_id]
        
        # Update receptivity based on response
        profile['receptivity'] = self._recalculate_receptivity(
            profile['receptivity'], 
            feedback_data['response_quality']
        )
        
        # Update learning patterns
        profile['learning_patterns'].append({
            'intervention_type': feedback_data['intervention_type'],
            'effectiveness': feedback_data['effectiveness'],
            'context': feedback_data['context']
        })
        
        # Update behavioral patterns
        self._update_behavioral_patterns(user_id, feedback_data)
        
        # Adjust cognitive model
        self._refine_cognitive_model(user_id, feedback_data)

    def _calculate_cognitive_load(self, context_data):
        """Estimate current cognitive load based on context"""
        base_load = context_data.get('task_complexity', 0.5)
        environmental_load = context_data.get('distractions', 0.0)
        temporal_load = context_data.get('time_pressure', 0.0)
        
        return min(1.0, base_load + 0.3 * environmental_load + 0.2 * temporal_load)

    def _evaluate_timing(self, user_id, timestamp):
        """Evaluate optimal timing for intervention"""
        profile = self.user_profiles[user_id]
        peak_times = profile['peak_performance_times']
        
        timing_score = self._calculate_timing_alignment(timestamp, peak_times)
        return timing_score * profile['receptivity']

    def _assess_attention(self, user_id, context):
        """Assess user's current attention availability"""
        profile = self.user_profiles[user_id]
        base_attention = profile['attention_capacity']
        
        modifiers = {
            'stress': -0.2 * profile['stress_level'],
            'energy': 0.3 * profile['energy_level'],
            'task_focus': -0.1 * context.get('task_focus', 0.0)
        }
        
        return max(0.0, min(1.0, base_attention + sum(modifiers.values())))

    def _should_intervene(self, context_assessment):
        """Determine if intervention is appropriate"""
        threshold = 0.6
        
        intervention_score = (
            0.3 * (1 - context_assessment['cognitive_load']) +
            0.3 * context_assessment['attention_score'] +
            0.2 * context_assessment['timing_score'] +
            0.2 * context_assessment['receptivity']
        )
        
        return intervention_score > threshold

    def _select_intervention_type(self, user_id, context):
        """Select most appropriate intervention type"""
        profile = self.user_profiles[user_id]
        
        # Analyze past effectiveness
        type_effectiveness = self._analyze_intervention_history(user_id)
        
        # Consider current context
        context_weights = self._get_context_weights(context)
        
        # Select optimal intervention type
        return self._optimize_intervention_selection(
            type_effectiveness,
            context_weights,
            profile['learning_patterns']
        )

    def _generate_content(self, user_id, intervention_type, context):
        """Generate personalized intervention content"""
        profile = self.user_profiles[user_id]
        
        content_template = self._get_content_template(intervention_type)
        personalized_content = self._personalize_content(
            content_template,
            profile,
            context
        )
        
        return self._enhance_actionability(personalized_content)

    def _optimize_timing(self, user_id, context):
        """Optimize intervention timing"""
        profile = self.user_profiles[user_id]
        
        current_load = self._calculate_cognitive_load(context)
        energy_cycle = self._get_energy_cycle(profile)
        
        return self._compute_optimal_timing(
            current_load,
            energy_cycle,
            profile['peak_performance_times']
        )

    def _calibrate_intensity(self, user_id, context_assessment):
        """Calibrate intervention intensity"""
        base_intensity = 0.7
        
        modifiers = {
            'cognitive_load': -0.3 * context_assessment['cognitive_load'],
            'receptivity': 0.2 * context_assessment['receptivity'],
            'attention': 0.1 * context_assessment['attention_score']
        }
        
        return max(0.1, min(1.0, base_intensity + sum(modifiers.values())))

    def _generate_action_steps(self, intervention_type, context):
        """Generate specific actionable steps"""
        base_steps = self._get_base_action_steps(intervention_type)
        
        contextualized_steps = self._contextualize_steps(base_steps, context)
        prioritized_steps = self._prioritize_steps(contextualized_steps)
        
        return self._enhance_step_clarity(prioritized_steps)

    def _plan_follow_up(self, user_id, intervention_type):
        """Plan follow-up engagement"""
        profile = self.user_profiles[user_id]
        
        optimal_timing = self._calculate_follow_up_timing(profile)
        follow_up_type = self._select_follow_up_type(intervention_type)
        
        return {
            'timing': optimal_timing,
            'type': follow_up_type,
            'intensity': self._calculate_follow_up_intensity(profile)
        }