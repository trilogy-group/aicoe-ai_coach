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
            'motivation': 0.5,
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
            'focus_duration': context_data.get('focus_time', 30)
        }
        
        cognitive_load = sum(cognitive_indicators.values()) / len(cognitive_indicators)
        attention_capacity = max(0.1, 1 - cognitive_load)
        
        self.user_profiles[user_id]['cognitive_state'] = cognitive_load
        self.user_profiles[user_id]['attention_capacity'] = attention_capacity
        
        return cognitive_load, attention_capacity

    def generate_personalized_nudge(self, user_id, context):
        """Create highly personalized behavioral nudge"""
        user = self.user_profiles[user_id]
        
        # Check intervention timing
        if not self._is_good_intervention_time(user_id, context):
            return None
            
        # Select intervention type based on user state
        if user['cognitive_state'] > 0.7:
            intervention = self._generate_focus_intervention(user_id)
        elif user['stress_level'] > 0.6:
            intervention = self._generate_wellbeing_intervention(user_id)
        else:
            intervention = self._generate_growth_intervention(user_id)
            
        # Personalize content
        intervention = self._personalize_content(intervention, user)
        
        # Add specific action steps
        intervention['action_steps'] = self._generate_action_steps(intervention['type'], user)
        
        # Track intervention
        self._log_intervention(user_id, intervention)
        
        return intervention

    def _is_good_intervention_time(self, user_id, context):
        """Determine if this is an optimal time to intervene"""
        user = self.user_profiles[user_id]
        
        # Check cognitive load
        if user['cognitive_state'] > 0.8:
            return False
            
        # Check flow state
        if self._is_in_flow_state(user_id):
            return False
            
        # Check intervention frequency
        if self._too_many_recent_interventions(user_id):
            return False
            
        # Check if during peak performance time
        if context['time'] in user['peak_performance_times']:
            return False
            
        return True

    def _generate_focus_intervention(self, user_id):
        """Generate intervention for high cognitive load"""
        return {
            'type': 'focus',
            'title': 'Quick Focus Reset',
            'description': 'Take a 2-minute mindful break to reset your attention',
            'duration': 2,
            'intensity': 'light'
        }

    def _generate_wellbeing_intervention(self, user_id):
        """Generate intervention for high stress"""
        return {
            'type': 'wellbeing', 
            'title': 'Stress Relief',
            'description': 'Practice this quick breathing exercise',
            'duration': 3,
            'intensity': 'medium'
        }

    def _generate_growth_intervention(self, user_id):
        """Generate intervention for skill development"""
        return {
            'type': 'growth',
            'title': 'Skill Building',
            'description': 'Try this technique to enhance your current task',
            'duration': 5,
            'intensity': 'high'
        }

    def _personalize_content(self, intervention, user):
        """Customize intervention content for user"""
        # Adjust language style
        intervention['description'] = self._adapt_language(
            intervention['description'], 
            user['learning_patterns']
        )
        
        # Adjust complexity
        intervention['complexity'] = self._adapt_complexity(
            user['cognitive_state'],
            user['attention_capacity']
        )
        
        # Add personalized examples
        intervention['examples'] = self._generate_relevant_examples(
            intervention['type'],
            user['context_preferences']
        )
        
        return intervention

    def _generate_action_steps(self, intervention_type, user):
        """Generate specific actionable steps"""
        if intervention_type == 'focus':
            return [
                'Close unnecessary browser tabs',
                'Put phone in do-not-disturb mode',
                'Take 3 deep breaths',
                'Set a 25-minute focus timer'
            ]
        elif intervention_type == 'wellbeing':
            return [
                'Stand up and stretch',
                'Drink a glass of water',
                'Do 1 minute of shoulder rolls',
                'Take a brief walk'
            ]
        else:
            return [
                'Break task into smaller steps',
                'Set a specific goal for next 30 minutes',
                'Review your progress',
                'Plan your next action'
            ]

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction"""
        user = self.user_profiles[user_id]
        
        # Update response history
        user['response_history'].append({
            'intervention_type': interaction_data['type'],
            'engagement': interaction_data['engagement'],
            'completion': interaction_data['completion'],
            'feedback': interaction_data['feedback']
        })
        
        # Update learning patterns
        self._update_learning_patterns(user_id, interaction_data)
        
        # Update context preferences
        self._update_context_preferences(user_id, interaction_data)
        
        # Adjust intervention parameters
        self._optimize_intervention_params(user_id)

    def _is_in_flow_state(self, user_id):
        """Detect if user is in flow state"""
        user = self.user_profiles[user_id]
        recent_patterns = self.behavioral_patterns.get(user_id, [])
        
        if len(recent_patterns) < 5:
            return False
            
        focus_indicators = [p['focus_level'] for p in recent_patterns[-5:]]
        return sum(focus_indicators) / len(focus_indicators) > 0.8

    def _too_many_recent_interventions(self, user_id):
        """Check intervention frequency"""
        recent_interventions = self.intervention_history.get(user_id, [])
        if len(recent_interventions) < 3:
            return False
            
        time_diffs = [
            recent_interventions[i+1]['timestamp'] - recent_interventions[i]['timestamp']
            for i in range(len(recent_interventions)-1)
        ]
        return min(time_diffs) < 1800  # 30 minutes