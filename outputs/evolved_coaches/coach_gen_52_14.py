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
        
    def assess_cognitive_state(self, user_id, context_data):
        """Evaluate user's current cognitive state and capacity"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        attention_span = self._estimate_attention_span(user_id, context_data)
        stress_indicators = self._detect_stress_signals(context_data)
        
        state = {
            'cognitive_load': cognitive_load,
            'attention_span': attention_span,
            'stress_level': stress_indicators,
            'time_of_day': context_data.get('time'),
            'task_complexity': context_data.get('task_complexity', 0.5)
        }
        
        self.cognitive_models[user_id] = state
        return state

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        if user_id not in self.user_profiles:
            self.initialize_user(user_id)
            
        cognitive_state = self.assess_cognitive_state(user_id, context)
        
        # Select optimal intervention type
        if cognitive_state['cognitive_load'] > 0.8:
            intervention_type = 'micro_break'
        elif cognitive_state['stress_level'] > 0.7:
            intervention_type = 'stress_reduction'
        elif cognitive_state['attention_span'] < 0.3:
            intervention_type = 'focus_enhancement'
        else:
            intervention_type = 'performance_optimization'
            
        # Personalize intervention content
        intervention = self._create_personalized_intervention(
            user_id,
            intervention_type,
            cognitive_state,
            context
        )
        
        # Track intervention
        self._record_intervention(user_id, intervention)
        
        return intervention

    def _create_personalized_intervention(self, user_id, type, state, context):
        """Generate specific intervention content"""
        base_interventions = {
            'micro_break': {
                'title': 'Quick Reset',
                'duration': '2 minutes',
                'actions': ['Stand up', 'Stretch', 'Deep breathing']
            },
            'stress_reduction': {
                'title': 'Stress Relief',
                'duration': '5 minutes', 
                'actions': ['Progressive relaxation', 'Mindful breathing', 'Mental reset']
            },
            'focus_enhancement': {
                'title': 'Focus Boost',
                'duration': '3 minutes',
                'actions': ['Environment check', 'Goal setting', 'Distraction elimination']
            },
            'performance_optimization': {
                'title': 'Peak Performance',
                'duration': '4 minutes',
                'actions': ['Energy check', 'Priority alignment', 'Success visualization']
            }
        }
        
        intervention = base_interventions[type].copy()
        
        # Personalize based on user history
        if user_id in self.intervention_history:
            past_responses = self.user_profiles[user_id]['response_history']
            intervention = self._adapt_to_history(intervention, past_responses)
            
        # Adjust for cognitive state
        intervention = self._adjust_for_cognitive_load(
            intervention,
            state['cognitive_load']
        )
        
        # Add contextual elements
        intervention['context_relevant_tips'] = self._generate_context_tips(context)
        
        return intervention

    def _adjust_for_cognitive_load(self, intervention, cognitive_load):
        """Modify intervention based on cognitive capacity"""
        if cognitive_load > 0.8:
            intervention['actions'] = intervention['actions'][:2]
            intervention['duration'] = '2 minutes'
        elif cognitive_load < 0.3:
            intervention['actions'].extend(['Additional focus exercise', 'Energy boost'])
            intervention['duration'] = '6 minutes'
        return intervention

    def _generate_context_tips(self, context):
        """Generate context-specific recommendations"""
        task_type = context.get('task_type')
        time_of_day = context.get('time_of_day')
        environment = context.get('environment')
        
        tips = []
        if task_type == 'creative':
            tips.append('Set up your space for creative flow')
        elif task_type == 'analytical':
            tips.append('Break complex problems into smaller parts')
            
        if time_of_day == 'morning':
            tips.append('Capitalize on your fresh mental energy')
        elif time_of_day == 'afternoon':
            tips.append('Take an energizing micro-break')
            
        if environment == 'noisy':
            tips.append('Use noise-cancelling techniques')
            
        return tips

    def record_response(self, user_id, intervention_id, response_data):
        """Track user response to intervention"""
        if user_id not in self.intervention_history:
            self.intervention_history[user_id] = []
            
        response = {
            'intervention_id': intervention_id,
            'timestamp': response_data['timestamp'],
            'effectiveness': response_data['effectiveness'],
            'completion': response_data['completion'],
            'mood_impact': response_data['mood_impact']
        }
        
        self.intervention_history[user_id].append(response)
        self._update_user_model(user_id, response)

    def _update_user_model(self, user_id, response):
        """Update user model based on intervention response"""
        profile = self.user_profiles[user_id]
        profile['response_history'].append(response)
        
        # Update effectiveness metrics
        if len(profile['response_history']) > 5:
            recent_responses = profile['response_history'][-5:]
            avg_effectiveness = sum(r['effectiveness'] for r in recent_responses) / 5
            profile['receptivity'] = avg_effectiveness
            
        # Update learning patterns
        self._update_learning_patterns(user_id, response)

    def _update_learning_patterns(self, user_id, response):
        """Update understanding of user learning patterns"""
        profile = self.user_profiles[user_id]
        if response['effectiveness'] > 0.8:
            pattern = {
                'intervention_type': response['intervention_id'],
                'context': self.cognitive_models[user_id],
                'effectiveness': response['effectiveness']
            }
            profile['learning_patterns'].append(pattern)