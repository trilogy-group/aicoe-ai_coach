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
            'burnout_risk': 0.0
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'activity_cycles': {},
            'productivity_patterns': {},
            'engagement_levels': {},
            'response_rates': {}
        }
        
        self.cognitive_models[user_id] = {
            'attention_span': None,
            'cognitive_load': 0.5,
            'flow_state': False,
            'stress_level': 0.0,
            'energy_level': 1.0
        }

    def assess_context(self, user_id, current_context):
        """Evaluate user's current context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_id, current_context)
        attention_availability = self._assess_attention(user_id, current_context)
        optimal_timing = self._check_optimal_timing(user_id, current_context)
        
        context_score = (cognitive_load * 0.4 + 
                        attention_availability * 0.3 +
                        optimal_timing * 0.3)
                        
        return context_score > 0.7

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        if not self.assess_context(user_id, context):
            return None
            
        user_profile = self.user_profiles[user_id]
        cognitive_state = self.cognitive_models[user_id]
        
        # Select intervention type based on user state
        if cognitive_state['flow_state']:
            return self._generate_minimal_nudge(user_id)
        elif cognitive_state['stress_level'] > 0.7:
            return self._generate_calming_intervention(user_id)
        elif cognitive_state['energy_level'] < 0.3:
            return self._generate_energizing_intervention(user_id)
        else:
            return self._generate_standard_intervention(user_id)

    def _generate_standard_intervention(self, user_id):
        """Generate main coaching intervention"""
        profile = self.user_profiles[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        intervention = {
            'type': 'standard',
            'content': self._personalize_content(user_id),
            'timing': self._optimize_timing(user_id),
            'intensity': self._calculate_intensity(user_id),
            'action_items': self._generate_action_items(user_id),
            'follow_up': self._plan_follow_up(user_id)
        }
        
        return intervention

    def _personalize_content(self, user_id):
        """Create personalized intervention content"""
        profile = self.user_profiles[user_id]
        
        content = {
            'message': self._generate_message(profile),
            'examples': self._find_relevant_examples(profile),
            'motivation': self._identify_motivation_hooks(profile),
            'difficulty': self._adjust_difficulty(profile)
        }
        
        return content

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction"""
        profile = self.user_profiles[user_id]
        cognitive = self.cognitive_models[user_id]
        
        # Update various user model components
        self._update_preferences(user_id, interaction_data)
        self._update_cognitive_model(user_id, interaction_data)
        self._update_behavioral_patterns(user_id, interaction_data)
        self._optimize_timing_model(user_id, interaction_data)
        
        # Recalculate risk factors
        profile['burnout_risk'] = self._calculate_burnout_risk(user_id)
        cognitive['stress_level'] = self._calculate_stress_level(user_id)

    def _calculate_cognitive_load(self, user_id, context):
        """Estimate current cognitive load"""
        base_load = self.cognitive_models[user_id]['cognitive_load']
        context_load = self._assess_context_difficulty(context)
        temporal_load = self._assess_temporal_factors(user_id)
        
        total_load = (base_load * 0.4 + 
                     context_load * 0.4 +
                     temporal_load * 0.2)
                     
        return min(total_load, 1.0)

    def _generate_action_items(self, user_id):
        """Create specific actionable recommendations"""
        profile = self.user_profiles[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        actions = []
        
        # Generate contextual action items
        if patterns['productivity_patterns']:
            actions.extend(self._productivity_recommendations(user_id))
            
        if patterns['engagement_levels']:
            actions.extend(self._engagement_recommendations(user_id))
            
        # Prioritize and limit actions
        actions = self._prioritize_actions(actions)
        return actions[:3]  # Limit to top 3 most relevant actions

    def _plan_follow_up(self, user_id):
        """Plan follow-up engagement"""
        profile = self.user_profiles[user_id]
        history = self.intervention_history[user_id]
        
        follow_up = {
            'timing': self._calculate_follow_up_timing(user_id),
            'type': self._determine_follow_up_type(user_id),
            'success_metrics': self._define_success_metrics(user_id)
        }
        
        return follow_up

    def evaluate_effectiveness(self, user_id, intervention_id):
        """Evaluate intervention effectiveness"""
        intervention = self.intervention_history[user_id][-1]
        response = self._get_user_response(user_id, intervention_id)
        
        metrics = {
            'engagement': self._calculate_engagement(response),
            'behavior_change': self._measure_behavior_change(user_id),
            'satisfaction': self._measure_satisfaction(response),
            'relevance': self._assess_relevance(response),
            'actionability': self._assess_actionability(response)
        }
        
        self._update_effectiveness_models(user_id, metrics)
        return metrics