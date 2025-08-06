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
            'energy_level': 1.0,
            'receptivity': 1.0,
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
            'task_switching': context_data.get('task_switches', 0.2)
        }
        
        cognitive_load = sum(cognitive_indicators.values()) / len(cognitive_indicators)
        attention_capacity = max(0.1, 1.0 - cognitive_load)
        
        self.user_profiles[user_id]['cognitive_state'] = cognitive_load
        self.user_profiles[user_id]['attention_capacity'] = attention_capacity
        
        return cognitive_load, attention_capacity

    def evaluate_intervention_timing(self, user_id, context):
        """Determine optimal timing for intervention"""
        user = self.user_profiles[user_id]
        
        # Check cognitive load and attention
        if user['cognitive_state'] > 0.8:
            return False # Too high cognitive load
            
        # Check for flow state
        if self.detect_flow_state(user_id):
            return False # Don't interrupt flow
            
        # Check time-based patterns
        if not self.is_optimal_time(user_id, context):
            return False
            
        return True

    def generate_personalized_nudge(self, user_id, context):
        """Create highly personalized intervention"""
        user = self.user_profiles[user_id]
        
        if not self.evaluate_intervention_timing(user_id, context):
            return None
            
        # Select intervention type based on user state
        intervention_type = self.select_intervention_type(user, context)
        
        # Generate specific actionable recommendation
        recommendation = self.generate_recommendation(
            user_id,
            intervention_type,
            context
        )
        
        # Adjust delivery style based on user preferences
        styled_message = self.style_message(
            recommendation,
            user['context_preferences']
        )
        
        return styled_message

    def select_intervention_type(self, user, context):
        """Choose most appropriate intervention approach"""
        if user['stress_level'] > 0.7:
            return 'stress_management'
        elif user['energy_level'] < 0.3:
            return 'energy_boost'
        elif context.get('task_complexity', 0) > 0.8:
            return 'task_breakdown'
        else:
            return 'productivity_enhancement'

    def generate_recommendation(self, user_id, intervention_type, context):
        """Create specific, actionable recommendation"""
        recommendations = {
            'stress_management': [
                "Take 3 deep breaths and scan your body for tension",
                "Step away for a 2-minute walking break",
                "Do a quick progressive muscle relaxation exercise"
            ],
            'energy_boost': [
                "Stand up and do 10 jumping jacks",
                "Drink a glass of water and stretch",
                "Take a 5-minute break in natural light"
            ],
            'task_breakdown': [
                "Break this task into 3 smaller subtasks",
                "Focus on just the next 15-minute chunk",
                "Write down your next 3 concrete action steps"
            ],
            'productivity_enhancement': [
                "Clear your workspace of distractions",
                "Set a specific goal for the next 30 minutes",
                "Use the Pomodoro technique for this task"
            ]
        }
        
        user_history = self.intervention_history.get(user_id, [])
        
        # Select least recently used recommendation
        valid_recommendations = recommendations[intervention_type]
        for rec in valid_recommendations:
            if rec not in user_history[-3:]:
                return rec
                
        return valid_recommendations[0]

    def detect_flow_state(self, user_id):
        """Detect if user is in flow state"""
        user = self.user_profiles[user_id]
        
        flow_indicators = [
            user['cognitive_state'] > 0.5,
            user['attention_capacity'] > 0.7,
            user['stress_level'] < 0.3
        ]
        
        return sum(flow_indicators) >= 2

    def is_optimal_time(self, user_id, context):
        """Check if current time is optimal for intervention"""
        user = self.user_profiles[user_id]
        
        current_time = context.get('time_of_day')
        if not current_time:
            return True
            
        peak_times = user['peak_performance_times']
        if not peak_times:
            return True
            
        time_diff = min(abs(t - current_time) for t in peak_times)
        return time_diff < 1.0 # Within 1 hour of peak time

    def style_message(self, message, preferences):
        """Adjust message style to user preferences"""
        style = preferences.get('communication_style', 'neutral')
        
        styled_messages = {
            'direct': f"Action needed: {message}",
            'encouraging': f"You've got this! Try to {message}",
            'analytical': f"Research suggests: {message}",
            'neutral': message
        }
        
        return styled_messages.get(style, message)

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction"""
        user = self.user_profiles[user_id]
        
        # Update response history
        user['response_history'].append(interaction_data)
        
        # Update learning patterns
        if len(user['response_history']) >= 3:
            self.analyze_patterns(user_id)
            
        # Update context preferences
        context = interaction_data.get('context', {})
        if context:
            self.update_context_preferences(user_id, context)

    def analyze_patterns(self, user_id):
        """Analyze user response patterns"""
        user = self.user_profiles[user_id]
        recent_responses = user['response_history'][-3:]
        
        # Analyze effectiveness patterns
        effectiveness_scores = [r.get('effectiveness', 0) for r in recent_responses]
        avg_effectiveness = sum(effectiveness_scores) / len(effectiveness_scores)
        
        # Update user model based on patterns
        if avg_effectiveness > 0.7:
            self.reinforce_successful_patterns(user_id)
        else:
            self.adjust_intervention_strategy(user_id)

    def update_context_preferences(self, user_id, context):
        """Update tracked context preferences"""
        user = self.user_profiles[user_id]
        
        for key, value in context.items():
            if key not in user['context_preferences']:
                user['context_preferences'][key] = []
            user['context_preferences'][key].append(value)
            
            # Keep only recent history
            user['context_preferences'][key] = user['context_preferences'][key][-10:]