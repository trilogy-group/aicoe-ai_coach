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
            'motivation_drivers': [],
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
            'stress_level': 0.0,
            'energy_level': 1.0,
            'flow_state': False
        }

    def assess_context(self, user_id, context_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        attention_availability = self._assess_attention(context_data)
        time_appropriateness = self._check_timing_optimality(user_id, context_data)
        
        context_score = (cognitive_load * 0.4 + 
                        attention_availability * 0.3 +
                        time_appropriateness * 0.3)
                        
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
            
        if cognitive_state['stress_level'] > 0.7:
            return self._generate_stress_intervention(user_id)
            
        if cognitive_state['energy_level'] < 0.3:
            return self._generate_energy_intervention(user_id)
            
        return self._generate_standard_intervention(user_id)

    def _generate_standard_intervention(self, user_id):
        """Generate standard personalized coaching intervention"""
        profile = self.user_profiles[user_id]
        
        intervention = {
            'type': 'standard',
            'content': self._personalize_content(user_id),
            'timing': self._optimize_timing(user_id),
            'intensity': self._calculate_intensity(user_id),
            'action_steps': self._generate_action_steps(user_id),
            'follow_up': self._plan_follow_up(user_id)
        }
        
        self.intervention_history[user_id].append(intervention)
        return intervention

    def _personalize_content(self, user_id):
        """Generate personalized content based on user profile"""
        profile = self.user_profiles[user_id]
        
        content = {
            'message': self._craft_message(profile),
            'tone': self._determine_tone(profile),
            'examples': self._find_relevant_examples(profile),
            'motivation_hooks': self._identify_motivation_drivers(profile)
        }
        
        return content

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Update behavioral patterns
        self.behavioral_patterns[user_id]['response_rates'].update(
            interaction_data['response_patterns']
        )
        
        # Update cognitive model
        self.cognitive_models[user_id].update({
            'attention_span': interaction_data.get('attention_metrics'),
            'cognitive_load': interaction_data.get('cognitive_load'),
            'stress_level': interaction_data.get('stress_indicators')
        })
        
        # Update user preferences
        self.user_profiles[user_id]['preferences'].update(
            interaction_data['preference_updates']
        )
        
        # Recalibrate intervention parameters
        self._recalibrate_intervention_params(user_id)

    def _calculate_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': 0.3,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2,
            'task_switching': 0.2
        }
        
        load = sum(context_data.get(k, 0) * v for k, v in factors.items())
        return min(load, 1.0)

    def _assess_attention(self, context_data):
        """Evaluate current attention availability"""
        attention_signals = {
            'focus_duration': 0.4,
            'context_switches': -0.2,
            'active_applications': -0.2,
            'idle_time': 0.2
        }
        
        attention = sum(context_data.get(k, 0) * v for k, v in attention_signals.items())
        return max(min(attention, 1.0), 0.0)

    def _generate_action_steps(self, user_id):
        """Generate specific, actionable recommendations"""
        profile = self.user_profiles[user_id]
        cognitive_state = self.cognitive_models[user_id]
        
        steps = []
        if cognitive_state['stress_level'] > 0.6:
            steps.extend(self._get_stress_management_steps())
        
        if cognitive_state['energy_level'] < 0.4:
            steps.extend(self._get_energy_management_steps())
            
        steps.extend(self._get_personalized_productivity_steps(profile))
        
        return steps[:3]  # Limit to top 3 most relevant steps

    def _recalibrate_intervention_params(self, user_id):
        """Recalibrate intervention parameters based on user response patterns"""
        response_data = self.behavioral_patterns[user_id]['response_rates']
        
        # Update timing preferences
        self.user_profiles[user_id]['optimal_times'] = self._calculate_optimal_times(response_data)
        
        # Update intensity calibration
        self.user_profiles[user_id]['intensity_preference'] = self._calculate_intensity_preference(response_data)
        
        # Update content preferences
        self.user_profiles[user_id]['content_preferences'] = self._analyze_content_effectiveness(response_data)