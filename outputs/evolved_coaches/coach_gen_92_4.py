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
            'context_preferences': {},
            'peak_performance_times': []
        }
        
    def assess_cognitive_load(self, user_id, context_data):
        """Evaluate current cognitive load and attention capacity"""
        cognitive_indicators = {
            'task_complexity': context_data.get('task_complexity', 0.5),
            'time_pressure': context_data.get('time_pressure', 0.5),
            'interruption_frequency': context_data.get('interruptions', 0.3),
            'fatigue_level': context_data.get('fatigue', 0.2)
        }
        
        cognitive_load = sum(cognitive_indicators.values()) / len(cognitive_indicators)
        return min(cognitive_load, 1.0)

    def generate_personalized_nudge(self, user_id, context):
        """Create highly personalized behavioral nudge"""
        user = self.user_profiles[user_id]
        cognitive_load = self.assess_cognitive_load(user_id, context)
        
        if cognitive_load > 0.8:
            return self.generate_stress_management_intervention(user_id)
        elif cognitive_load < 0.3:
            return self.generate_engagement_boost(user_id)
        else:
            return self.generate_optimal_performance_nudge(user_id)

    def generate_stress_management_intervention(self, user_id):
        """Generate stress-reduction focused intervention"""
        interventions = {
            'high_stress': [
                "Take a 2-minute breathing break: Inhale for 4 counts, hold for 4, exhale for 4",
                "Step away from your desk and stretch for 1 minute",
                "Write down your top 3 priorities for the next hour"
            ],
            'moderate_stress': [
                "Take a brief walk to reset your focus",
                "Do a quick mindfulness check-in",
                "Review and adjust your task list"
            ]
        }
        
        stress_level = self.user_profiles[user_id]['stress_level']
        intervention_type = 'high_stress' if stress_level > 0.7 else 'moderate_stress'
        
        return {
            'type': 'stress_management',
            'content': random.choice(interventions[intervention_type]),
            'urgency': 'high' if stress_level > 0.8 else 'medium',
            'duration': '2-5 minutes'
        }

    def generate_engagement_boost(self, user_id):
        """Generate engagement-focused intervention"""
        return {
            'type': 'engagement',
            'content': self.get_personalized_engagement_prompt(user_id),
            'urgency': 'low',
            'duration': '5-10 minutes'
        }

    def generate_optimal_performance_nudge(self, user_id):
        """Generate performance optimization intervention"""
        user = self.user_profiles[user_id]
        
        return {
            'type': 'performance_optimization',
            'content': self.get_flow_state_prompt(user),
            'urgency': 'medium',
            'duration': '3-7 minutes'
        }

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        user = self.user_profiles[user_id]
        
        # Update cognitive state
        user['cognitive_state'] = self.calculate_cognitive_state(interaction_data)
        
        # Update stress and engagement levels
        user['stress_level'] = self.calculate_stress_level(interaction_data)
        user['engagement_level'] = self.calculate_engagement_level(interaction_data)
        
        # Update learning patterns
        user['learning_patterns'].append({
            'timestamp': interaction_data['timestamp'],
            'response': interaction_data['response'],
            'effectiveness': interaction_data['effectiveness']
        })
        
        # Prune old data
        if len(user['learning_patterns']) > 100:
            user['learning_patterns'] = user['learning_patterns'][-100:]

    def calculate_cognitive_state(self, interaction_data):
        """Calculate current cognitive state"""
        factors = {
            'response_time': interaction_data.get('response_time', 0.5),
            'error_rate': interaction_data.get('error_rate', 0.3),
            'task_completion': interaction_data.get('task_completion', 0.7),
            'focus_duration': interaction_data.get('focus_duration', 0.6)
        }
        
        return sum(factors.values()) / len(factors)

    def calculate_stress_level(self, interaction_data):
        """Calculate current stress level"""
        indicators = {
            'typing_speed': interaction_data.get('typing_speed_variance', 0.3),
            'mouse_movement': interaction_data.get('mouse_jitter', 0.2),
            'task_switching': interaction_data.get('task_switching_rate', 0.4),
            'break_frequency': interaction_data.get('break_frequency', 0.5)
        }
        
        return sum(indicators.values()) / len(indicators)

    def calculate_engagement_level(self, interaction_data):
        """Calculate current engagement level"""
        metrics = {
            'active_time': interaction_data.get('active_time', 0.6),
            'interaction_depth': interaction_data.get('interaction_depth', 0.5),
            'response_quality': interaction_data.get('response_quality', 0.7),
            'initiative_taken': interaction_data.get('initiative_taken', 0.4)
        }
        
        return sum(metrics.values()) / len(metrics)

    def get_personalized_engagement_prompt(self, user_id):
        """Generate personalized engagement prompt"""
        user = self.user_profiles[user_id]
        
        prompts = [
            f"Set a specific goal to accomplish in the next {random.randint(25,45)} minutes",
            "Break your current task into smaller, manageable chunks",
            "Identify one challenging aspect of your work and create a plan to address it",
            "Review your progress and celebrate small wins from today"
        ]
        
        return random.choice(prompts)

    def get_flow_state_prompt(self, user):
        """Generate flow state optimization prompt"""
        prompts = [
            "Minimize distractions and focus deeply for the next 25 minutes",
            "Set a clear intention for your next work session",
            "Create an environment that supports your peak performance",
            "Challenge yourself with a slightly stretched goal for this session"
        ]
        
        return random.choice(prompts)