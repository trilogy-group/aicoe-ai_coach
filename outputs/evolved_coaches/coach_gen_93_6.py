class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.cognitive_models = {}
        self.behavioral_patterns = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'cognitive_state': None,
            'attention_capacity': 1.0,
            'stress_level': 0.0,
            'engagement_level': 0.5,
            'learning_patterns': [],
            'response_history': [],
            'peak_performance_times': [],
            'intervention_preferences': {}
        }
        
    def assess_cognitive_load(self, user_id, context_data):
        """Evaluate current cognitive load based on context"""
        cognitive_load = 0.0
        
        # Analyze work complexity
        cognitive_load += context_data.get('task_complexity', 0) * 0.3
        
        # Consider time of day fatigue
        time_factor = self._calculate_time_fatigue(context_data['timestamp'])
        cognitive_load += time_factor * 0.2
        
        # Account for recent activity intensity
        activity_load = self._analyze_recent_activity(user_id)
        cognitive_load += activity_load * 0.25
        
        # Factor in reported stress level
        cognitive_load += self.user_profiles[user_id]['stress_level'] * 0.25
        
        return min(cognitive_load, 1.0)

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        if not self._should_intervene(user_id, context):
            return None
            
        user_state = self._analyze_user_state(user_id, context)
        
        intervention = {
            'type': self._select_intervention_type(user_state),
            'content': self._generate_content(user_state),
            'timing': self._optimize_timing(user_id),
            'intensity': self._calculate_intensity(user_state),
            'action_items': self._generate_action_items(user_state)
        }
        
        self._record_intervention(user_id, intervention)
        return intervention

    def _analyze_user_state(self, user_id, context):
        """Comprehensive analysis of user's current state"""
        profile = self.user_profiles[user_id]
        
        return {
            'cognitive_load': self.assess_cognitive_load(user_id, context),
            'attention_capacity': profile['attention_capacity'],
            'stress_level': profile['stress_level'],
            'engagement': profile['engagement_level'],
            'time_of_day': context.get('timestamp'),
            'recent_responses': profile['response_history'][-5:],
            'task_context': context.get('current_task')
        }

    def _should_intervene(self, user_id, context):
        """Determine if intervention is appropriate now"""
        cognitive_load = self.assess_cognitive_load(user_id, context)
        if cognitive_load > 0.8:
            return False
            
        last_intervention = self._get_last_intervention_time(user_id)
        if not self._enough_time_elapsed(last_intervention):
            return False
            
        if self._user_in_flow_state(user_id):
            return False
            
        return True

    def _select_intervention_type(self, user_state):
        """Choose most appropriate intervention type"""
        if user_state['stress_level'] > 0.7:
            return 'stress_management'
        elif user_state['cognitive_load'] > 0.6:
            return 'focus_enhancement'
        elif user_state['engagement'] < 0.4:
            return 'motivation_boost'
        else:
            return 'performance_optimization'

    def _generate_content(self, user_state):
        """Generate personalized intervention content"""
        intervention_type = self._select_intervention_type(user_state)
        
        content_templates = {
            'stress_management': [
                "I notice you might be feeling stressed. Let's take a 2-minute breathing break.",
                "Quick stress relief: Focus on relaxing your shoulders and taking 3 deep breaths."
            ],
            'focus_enhancement': [
                "Your focus may be scattered. Try the Pomodoro technique: 25 minutes of focused work, then a 5-minute break.",
                "Minimize distractions by closing unnecessary browser tabs and putting your phone in another room."
            ],
            'motivation_boost': [
                "Remember your goal: {goal}. You've made great progress so far!",
                "Break your current task into smaller, manageable chunks. What's the next tiny step?"
            ],
            'performance_optimization': [
                "You're in a good flow. Consider capturing your current approach to replicate this state later.",
                "Great energy level! This is an optimal time to tackle your most important task."
            ]
        }
        
        return self._personalize_content(
            content_templates[intervention_type],
            user_state
        )

    def _generate_action_items(self, user_state):
        """Create specific, actionable recommendations"""
        action_items = []
        
        if user_state['cognitive_load'] > 0.6:
            action_items.append({
                'action': 'Take a 5-minute break',
                'timeframe': 'Next 5 minutes',
                'expected_benefit': 'Reduced mental fatigue'
            })
            
        if user_state['stress_level'] > 0.7:
            action_items.append({
                'action': 'Deep breathing exercise: 4 counts in, 4 counts out',
                'timeframe': 'Next 2 minutes',
                'expected_benefit': 'Immediate stress reduction'
            })
            
        return action_items

    def update_user_state(self, user_id, new_data):
        """Update user state with new information"""
        if user_id in self.user_profiles:
            self.user_profiles[user_id].update(new_data)
            self._update_learning_patterns(user_id, new_data)
            self._adjust_intervention_strategy(user_id)

    def record_feedback(self, user_id, intervention_id, feedback):
        """Process user feedback to improve future interventions"""
        if user_id in self.intervention_history:
            self.intervention_history[user_id].append({
                'intervention_id': intervention_id,
                'feedback': feedback,
                'timestamp': feedback['timestamp']
            })
            self._update_intervention_preferences(user_id, feedback)

    def _update_learning_patterns(self, user_id, new_data):
        """Update user learning and response patterns"""
        profile = self.user_profiles[user_id]
        profile['learning_patterns'].append(new_data)
        if len(profile['learning_patterns']) > 100:
            profile['learning_patterns'] = profile['learning_patterns'][-100:]

    def _adjust_intervention_strategy(self, user_id):
        """Adapt intervention strategy based on user patterns"""
        profile = self.user_profiles[user_id]
        recent_responses = profile['response_history'][-20:]
        
        if recent_responses:
            effectiveness = sum(r['effectiveness'] for r in recent_responses) / len(recent_responses)
            if effectiveness < 0.5:
                self._modify_intervention_parameters(user_id)