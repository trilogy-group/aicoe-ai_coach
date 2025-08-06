class EnhancedAICoach:
    def __init__(self):
        # Personality and learning profiles
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }
        
        # Enhanced context tracking
        self.context_tracker = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': None,
            'time_of_day': None,
            'work_context': None,
            'interruption_count': 0
        }
        
        # Behavioral psychology components
        self.behavioral_patterns = {
            'response_history': [],
            'intervention_effectiveness': {},
            'habit_formation_progress': {},
            'motivation_triggers': set()
        }
        
        # User state modeling
        self.user_state = {
            'stress_level': 0.0,
            'receptivity': 0.0,
            'goal_progress': {},
            'learning_velocity': 0.0,
            'engagement_level': 0.0
        }
        
        # Intervention configurations
        self.intervention_types = {
            'micro_nudge': {'duration': 30, 'cognitive_load': 0.1},
            'quick_tip': {'duration': 60, 'cognitive_load': 0.2},
            'mini_lesson': {'duration': 300, 'cognitive_load': 0.4},
            'deep_dive': {'duration': 900, 'cognitive_load': 0.8}
        }

    def assess_context(self, user_data):
        """Evaluate current user context for intervention timing"""
        context_score = 0.0
        
        # Cognitive load assessment
        current_load = self._calculate_cognitive_load(user_data)
        self.context_tracker['cognitive_load'] = current_load
        
        # Time and schedule optimization
        time_appropriateness = self._evaluate_timing(user_data['time'])
        
        # Work context evaluation
        context_alignment = self._assess_work_context(user_data['activity'])
        
        # Calculate overall context score
        context_score = (current_load * 0.4 + 
                        time_appropriateness * 0.3 +
                        context_alignment * 0.3)
        
        return context_score

    def generate_intervention(self, user_profile, context_score):
        """Create personalized coaching intervention"""
        if context_score < 0.3:
            return None # Context not suitable
            
        # Select intervention type
        intervention_type = self._select_intervention_type(context_score)
        
        # Personalize content
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Generate specific actionable recommendation
        recommendation = self._create_recommendation(
            intervention_type,
            personality_config,
            self.user_state
        )
        
        return {
            'type': intervention_type,
            'content': recommendation,
            'expected_duration': self.intervention_types[intervention_type]['duration'],
            'cognitive_load': self.intervention_types[intervention_type]['cognitive_load']
        }

    def update_effectiveness(self, intervention_id, user_response):
        """Track and update intervention effectiveness"""
        self.behavioral_patterns['response_history'].append({
            'intervention_id': intervention_id,
            'response': user_response,
            'context': self.context_tracker.copy(),
            'user_state': self.user_state.copy()
        })
        
        # Update effectiveness metrics
        self._update_intervention_metrics(intervention_id, user_response)
        
        # Adjust future recommendations
        self._optimize_recommendation_engine()

    def _calculate_cognitive_load(self, user_data):
        """Assess current cognitive load based on multiple factors"""
        base_load = user_data.get('activity_complexity', 0.5)
        fatigue_factor = self._calculate_fatigue(user_data)
        interruption_impact = self.context_tracker['interruption_count'] * 0.1
        
        cognitive_load = min(1.0, base_load + fatigue_factor + interruption_impact)
        return cognitive_load

    def _evaluate_timing(self, time_data):
        """Optimize intervention timing"""
        # Consider circadian rhythms
        hour = time_data.hour
        if 9 <= hour <= 11 or 14 <= hour <= 16:
            timing_score = 0.8
        elif 12 <= hour <= 13:
            timing_score = 0.4  # Lunch period
        else:
            timing_score = 0.6
            
        return timing_score

    def _assess_work_context(self, activity):
        """Evaluate work context appropriateness"""
        context_scores = {
            'deep_work': 0.2,  # Minimize interruptions
            'meetings': 0.1,   # Avoid interrupting
            'email': 0.7,      # Good time for quick tips
            'planning': 0.9,   # Ideal for coaching
            'break': 0.8       # Good for longer interventions
        }
        return context_scores.get(activity, 0.5)

    def _create_recommendation(self, intervention_type, personality_config, user_state):
        """Generate specific, actionable recommendations"""
        recommendation_templates = {
            'micro_nudge': "Take a 2-minute break to stretch and reset your focus",
            'quick_tip': "Try the Pomodoro technique: 25 minutes focused work, then 5 minutes break",
            'mini_lesson': "Let's improve your task prioritization using the Eisenhower Matrix...",
            'deep_dive': "Complete this guided productivity assessment and create an action plan..."
        }
        
        # Personalize based on personality and learning style
        base_recommendation = recommendation_templates[intervention_type]
        personalized_recommendation = self._personalize_content(
            base_recommendation,
            personality_config,
            user_state
        )
        
        return personalized_recommendation

    def _personalize_content(self, content, personality_config, user_state):
        """Customize content delivery based on user preferences"""
        style = personality_config['communication_pref']
        if style == 'direct':
            return f"Action required: {content}"
        elif style == 'enthusiastic':
            return f"Ready for a positive change? {content}!"
        return content

    def _optimize_recommendation_engine(self):
        """Improve recommendation system based on historical effectiveness"""
        if len(self.behavioral_patterns['response_history']) > 10:
            # Analyze patterns and adjust strategies
            successful_patterns = self._analyze_success_patterns()
            self._update_intervention_strategies(successful_patterns)