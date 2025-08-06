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
            'response_patterns': {},
            'cognitive_load_baseline': 0.5,
            'optimal_times': [],
            'flow_states': []
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'activity_cycles': {},
            'productivity_patterns': {},
            'engagement_levels': {},
            'success_metrics': {}
        }
        
    def assess_context(self, user_id, current_state):
        """Evaluate user's current context for intervention timing"""
        cognitive_load = self._measure_cognitive_load(current_state)
        time_relevance = self._check_timing_appropriateness(user_id)
        attention_availability = self._assess_attention(current_state)
        
        context_score = (cognitive_load * 0.4 + 
                        time_relevance * 0.3 +
                        attention_availability * 0.3)
                        
        return context_score > 0.7

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        if not self.assess_context(user_id, context):
            return None
            
        user_profile = self.user_profiles[user_id]
        behavioral_data = self.behavioral_patterns[user_id]
        
        # Select optimal intervention type
        intervention_type = self._select_intervention_type(
            user_profile,
            behavioral_data,
            context
        )
        
        # Generate specific actionable recommendation
        recommendation = self._create_actionable_recommendation(
            intervention_type,
            user_profile,
            context
        )
        
        # Personalize delivery approach
        delivery = self._personalize_delivery(
            user_profile,
            intervention_type,
            context
        )
        
        return {
            'type': intervention_type,
            'content': recommendation,
            'delivery': delivery,
            'timing': self._optimize_timing(user_id)
        }

    def _measure_cognitive_load(self, state):
        """Assess current cognitive load level"""
        factors = {
            'task_complexity': self._evaluate_complexity(state),
            'context_switches': self._count_context_switches(state),
            'time_pressure': self._assess_time_pressure(state),
            'interruption_frequency': self._measure_interruptions(state)
        }
        
        weights = {
            'task_complexity': 0.4,
            'context_switches': 0.2, 
            'time_pressure': 0.2,
            'interruption_frequency': 0.2
        }
        
        return sum(factors[k] * weights[k] for k in factors)

    def _create_actionable_recommendation(self, intervention_type, profile, context):
        """Generate specific, actionable coaching advice"""
        recommendations = {
            'focus': self._generate_focus_recommendation(profile, context),
            'break': self._generate_break_recommendation(profile, context),
            'planning': self._generate_planning_recommendation(profile, context),
            'reflection': self._generate_reflection_recommendation(profile, context)
        }
        
        return recommendations[intervention_type]

    def _personalize_delivery(self, profile, intervention_type, context):
        """Customize intervention delivery style"""
        tone = self._select_communication_tone(profile)
        format = self._select_message_format(profile, context)
        urgency = self._determine_urgency(context)
        
        return {
            'tone': tone,
            'format': format,
            'urgency': urgency
        }

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction"""
        profile = self.user_profiles[user_id]
        
        # Update learning patterns
        profile['learning_style'] = self._refine_learning_style(
            profile['learning_style'],
            interaction_data
        )
        
        # Update response patterns
        profile['response_patterns'] = self._update_response_patterns(
            profile['response_patterns'],
            interaction_data
        )
        
        # Update behavioral patterns
        self.behavioral_patterns[user_id] = self._update_behavioral_patterns(
            self.behavioral_patterns[user_id],
            interaction_data
        )
        
        # Record intervention outcome
        self.intervention_history[user_id].append({
            'intervention': interaction_data['intervention'],
            'response': interaction_data['response'],
            'outcome': interaction_data['outcome'],
            'timestamp': interaction_data['timestamp']
        })

    def _optimize_timing(self, user_id):
        """Determine optimal intervention timing"""
        profile = self.user_profiles[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        optimal_times = self._analyze_productive_periods(patterns)
        attention_spans = self._analyze_attention_cycles(patterns)
        
        return self._select_optimal_window(
            optimal_times,
            attention_spans,
            profile['cognitive_load_baseline']
        )

    def get_intervention_effectiveness(self, user_id):
        """Measure intervention effectiveness"""
        history = self.intervention_history[user_id]
        
        if not history:
            return 0.0
            
        success_rate = sum(1 for i in history if i['outcome'] > 0.7) / len(history)
        behavior_change = self._measure_behavior_change(user_id)
        satisfaction = self._measure_user_satisfaction(user_id)
        
        return (success_rate * 0.4 + 
                behavior_change * 0.4 +
                satisfaction * 0.2)