class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'preferences': {},
            'learning_style': None,
            'motivation_factors': [],
            'cognitive_load_baseline': 0,
            'response_patterns': {},
            'context_sensitivity': {}
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'daily_rhythms': {},
            'work_patterns': {},
            'stress_indicators': {},
            'engagement_levels': {}
        }
        
    def assess_context(self, user_id, current_context):
        """Evaluate user's current context for intervention timing"""
        cognitive_load = self._estimate_cognitive_load(user_id, current_context)
        time_sensitivity = self._check_temporal_factors(user_id, current_context)
        attention_availability = self._assess_attention(user_id, current_context)
        
        return {
            'cognitive_load': cognitive_load,
            'time_sensitivity': time_sensitivity,
            'attention': attention_availability,
            'receptivity_score': self._calculate_receptivity(cognitive_load, time_sensitivity, attention_availability)
        }

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        context_assessment = self.assess_context(user_id, context)
        
        if not self._is_appropriate_timing(context_assessment):
            return None
            
        intervention_type = self._select_intervention_type(user_id, context_assessment)
        content = self._generate_content(user_id, intervention_type, context)
        
        return self._format_intervention(content, context_assessment)

    def _estimate_cognitive_load(self, user_id, context):
        """Estimate current cognitive load based on context and patterns"""
        base_load = self.user_profiles[user_id]['cognitive_load_baseline']
        context_load = self._analyze_context_complexity(context)
        temporal_load = self._get_temporal_load_factor(user_id)
        
        return self._combine_load_factors(base_load, context_load, temporal_load)

    def _check_temporal_factors(self, user_id, context):
        """Check time-based factors affecting intervention effectiveness"""
        daily_pattern = self.behavioral_patterns[user_id]['daily_rhythms']
        work_pattern = self.behavioral_patterns[user_id]['work_patterns']
        
        return self._calculate_timing_score(daily_pattern, work_pattern, context)

    def _assess_attention(self, user_id, context):
        """Assess user's current attention availability"""
        flow_state = self._detect_flow_state(user_id, context)
        interruption_cost = self._calculate_interruption_cost(user_id, context)
        focus_level = self._estimate_focus_level(user_id, context)
        
        return self._combine_attention_factors(flow_state, interruption_cost, focus_level)

    def _select_intervention_type(self, user_id, context_assessment):
        """Select most appropriate intervention type based on context"""
        user_preferences = self.user_profiles[user_id]['preferences']
        effectiveness_history = self._analyze_past_effectiveness(user_id)
        
        return self._optimize_intervention_selection(user_preferences, effectiveness_history, context_assessment)

    def _generate_content(self, user_id, intervention_type, context):
        """Generate personalized intervention content"""
        motivation_factors = self.user_profiles[user_id]['motivation_factors']
        learning_style = self.user_profiles[user_id]['learning_style']
        
        content = self._create_base_content(intervention_type)
        content = self._personalize_content(content, motivation_factors, learning_style)
        content = self._add_actionable_steps(content, context)
        
        return content

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        self._update_preferences(user_id, interaction_data)
        self._update_behavioral_patterns(user_id, interaction_data)
        self._update_effectiveness_metrics(user_id, interaction_data)
        self._refine_cognitive_model(user_id, interaction_data)

    def _calculate_receptivity(self, cognitive_load, time_sensitivity, attention):
        """Calculate overall receptivity score for intervention"""
        weights = {'cognitive': 0.4, 'temporal': 0.3, 'attention': 0.3}
        
        return (weights['cognitive'] * (1 - cognitive_load) +
                weights['temporal'] * time_sensitivity +
                weights['attention'] * attention)

    def _is_appropriate_timing(self, context_assessment):
        """Determine if current moment is appropriate for intervention"""
        return context_assessment['receptivity_score'] > 0.6

    def _format_intervention(self, content, context_assessment):
        """Format intervention based on context and user state"""
        return {
            'content': content,
            'delivery_style': self._select_delivery_style(context_assessment),
            'urgency': self._calculate_urgency(context_assessment),
            'actionable_steps': content['action_items'],
            'follow_up': self._generate_follow_up_plan(content)
        }

    def get_effectiveness_metrics(self, user_id):
        """Return effectiveness metrics for user interventions"""
        return {
            'engagement_rate': self._calculate_engagement_rate(user_id),
            'behavior_change': self._measure_behavior_change(user_id),
            'satisfaction_score': self._calculate_satisfaction(user_id),
            'action_completion': self._get_action_completion_rate(user_id)
        }