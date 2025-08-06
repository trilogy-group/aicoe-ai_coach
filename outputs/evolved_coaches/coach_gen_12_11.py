class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced psychological models
        self.cognitive_models = {
            'attention': {'capacity': 0.0, 'fatigue': 0.0, 'recovery_rate': 0.0},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0, 'goal_alignment': 0.0},
            'emotional': {'valence': 0.0, 'arousal': 0.0, 'dominance': 0.0}
        }

        # Context tracking
        self.context_tracker = {
            'time_of_day': None,
            'work_phase': None, 
            'cognitive_load': 0.0,
            'interruption_cost': 0.0,
            'flow_state': False
        }

        # User adaptation parameters
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preference_weights': {}
        }

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {
                'duration': [2, 5],
                'triggers': ['high_cognitive_load', 'extended_focus'],
                'customization': lambda user: self._personalize_break(user)
            },
            'deep_work': {
                'duration': [25, 45], 
                'triggers': ['low_interruption_cost', 'high_motivation'],
                'customization': lambda user: self._personalize_deep_work(user)
            },
            'reflection': {
                'duration': [5, 10],
                'triggers': ['task_completion', 'learning_opportunity'],
                'customization': lambda user: self._personalize_reflection(user)
            }
        }

    def update_user_state(self, metrics):
        """Update user's cognitive and emotional state based on metrics"""
        self.cognitive_models['attention']['capacity'] = metrics.get('attention', 0.0)
        self.cognitive_models['motivation']['intrinsic'] = metrics.get('motivation', 0.0)
        self.cognitive_models['emotional']['valence'] = metrics.get('mood', 0.0)
        self._update_context(metrics)

    def generate_intervention(self, user_context):
        """Generate personalized intervention based on user state and context"""
        if not self._should_intervene():
            return None

        intervention_type = self._select_intervention_type()
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(intervention_type),
            'timing': self._optimize_timing(),
            'delivery': self._personalize_delivery(),
            'follow_up': self._create_follow_up()
        }

        return self._enhance_actionability(intervention)

    def _should_intervene(self):
        """Determine if intervention is appropriate based on context"""
        if self.context_tracker['flow_state']:
            return False
            
        cognitive_load = self.context_tracker['cognitive_load']
        interruption_cost = self.context_tracker['interruption_cost']
        
        return cognitive_load < 0.8 and interruption_cost < 0.6

    def _select_intervention_type(self):
        """Select most appropriate intervention type based on user state"""
        attention = self.cognitive_models['attention']['capacity']
        motivation = self.cognitive_models['motivation']['intrinsic']
        
        if attention < 0.3:
            return 'micro_break'
        elif motivation > 0.7:
            return 'deep_work'
        else:
            return 'reflection'

    def _generate_content(self, intervention_type):
        """Generate personalized content for intervention"""
        user_style = self.personality_type_configs[self.user_profile['personality_type']]
        
        content = {
            'message': self._craft_message(intervention_type, user_style),
            'suggestions': self._generate_suggestions(intervention_type),
            'rationale': self._explain_benefits(intervention_type)
        }
        
        return content

    def _optimize_timing(self):
        """Optimize intervention timing based on user patterns"""
        current_phase = self.context_tracker['work_phase']
        time_of_day = self.context_tracker['time_of_day']
        
        return {
            'optimal_time': self._calculate_optimal_time(current_phase, time_of_day),
            'duration': self._calculate_duration(),
            'flexibility': self._calculate_flexibility()
        }

    def _personalize_delivery(self):
        """Personalize intervention delivery method"""
        user_prefs = self.user_profile['preference_weights']
        
        return {
            'channel': self._select_channel(user_prefs),
            'style': self._adapt_communication_style(),
            'intensity': self._calculate_intensity()
        }

    def _create_follow_up(self):
        """Create follow-up actions and accountability"""
        return {
            'check_in': self._schedule_check_in(),
            'progress_tracking': self._create_progress_metrics(),
            'adaptation': self._create_adaptation_plan()
        }

    def _enhance_actionability(self, intervention):
        """Enhance intervention actionability"""
        intervention['specific_steps'] = self._break_down_steps()
        intervention['success_criteria'] = self._define_success_criteria()
        intervention['contingency_plans'] = self._create_contingency_plans()
        
        return intervention

    def _update_context(self, metrics):
        """Update context tracking based on new metrics"""
        self.context_tracker['cognitive_load'] = self._calculate_cognitive_load(metrics)
        self.context_tracker['flow_state'] = self._detect_flow_state(metrics)
        self.context_tracker['interruption_cost'] = self._calculate_interruption_cost()

    def track_effectiveness(self, intervention_id, outcomes):
        """Track intervention effectiveness and update user profile"""
        self.user_profile['response_history'].append({
            'intervention_id': intervention_id,
            'outcomes': outcomes,
            'context': self.context_tracker.copy()
        })
        
        self._update_effectiveness_metrics(outcomes)
        self._adapt_strategies(outcomes)