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
            'response_history': [],
            'cognitive_load': 0.0,
            'engagement_level': 0.0,
            'stress_level': 0.0
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate user's current context and state"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        time_of_day = context_data.get('time')
        current_activity = context_data.get('activity')
        stress_indicators = context_data.get('stress_signals', [])
        
        context_score = {
            'cognitive_load': cognitive_load,
            'timing_appropriateness': self._evaluate_timing(time_of_day),
            'activity_interruption_cost': self._assess_interruption_cost(current_activity),
            'stress_level': self._analyze_stress(stress_indicators)
        }
        
        return context_score

    def generate_intervention(self, user_id, context_score):
        """Create personalized coaching intervention"""
        user_profile = self.user_profiles[user_id]
        
        if context_score['cognitive_load'] > 0.8:
            return self._generate_stress_management_intervention(user_profile)
            
        if context_score['timing_appropriateness'] < 0.4:
            return self._defer_intervention(user_id)
            
        intervention_type = self._select_intervention_type(user_profile, context_score)
        
        intervention = {
            'type': intervention_type,
            'content': self._personalize_content(user_profile, intervention_type),
            'timing': self._optimize_timing(context_score),
            'intensity': self._calibrate_intensity(user_profile),
            'action_steps': self._generate_action_steps(intervention_type)
        }
        
        return intervention

    def _calculate_cognitive_load(self, context_data):
        """Estimate current cognitive load based on context signals"""
        task_complexity = context_data.get('task_complexity', 0.5)
        interruption_frequency = context_data.get('interruptions', 0.0)
        time_pressure = context_data.get('time_pressure', 0.0)
        
        cognitive_load = (0.4 * task_complexity + 
                         0.3 * interruption_frequency +
                         0.3 * time_pressure)
        return min(cognitive_load, 1.0)

    def _evaluate_timing(self, time_of_day):
        """Determine appropriateness of current timing"""
        # Implementation of timing optimization logic
        return 0.7 # Example score

    def _assess_interruption_cost(self, activity):
        """Calculate cost of interrupting current activity"""
        interruption_costs = {
            'deep_work': 0.9,
            'meeting': 0.7,
            'email': 0.3,
            'break': 0.1
        }
        return interruption_costs.get(activity, 0.5)

    def _analyze_stress(self, stress_indicators):
        """Evaluate stress level from biological and behavioral signals"""
        if not stress_indicators:
            return 0.3
        return sum(stress_indicators) / len(stress_indicators)

    def _select_intervention_type(self, user_profile, context_score):
        """Choose most appropriate intervention type"""
        if context_score['stress_level'] > 0.7:
            return 'stress_reduction'
        if context_score['cognitive_load'] > 0.6:
            return 'focus_enhancement'
        return 'productivity_optimization'

    def _personalize_content(self, user_profile, intervention_type):
        """Customize intervention content for user"""
        content_templates = {
            'stress_reduction': [
                "Take a 2-minute breathing exercise",
                "Step away for a short walk",
                "Practice progressive muscle relaxation"
            ],
            'focus_enhancement': [
                "Clear your workspace of distractions",
                "Set a specific goal for next 25 minutes",
                "Use noise-cancelling headphones"
            ],
            'productivity_optimization': [
                "Break your task into smaller chunks",
                "Set a timer for focused work",
                "Review and prioritize your task list"
            ]
        }
        
        return self._select_best_content(content_templates[intervention_type], user_profile)

    def _optimize_timing(self, context_score):
        """Determine optimal delivery timing"""
        if context_score['timing_appropriateness'] < 0.3:
            return 'defer_15min'
        if context_score['cognitive_load'] > 0.7:
            return 'wait_for_break'
        return 'immediate'

    def _calibrate_intensity(self, user_profile):
        """Adjust intervention intensity based on user preferences"""
        base_intensity = 0.5
        engagement_factor = user_profile['engagement_level']
        stress_factor = user_profile['stress_level']
        
        intensity = base_intensity * (1 + engagement_factor - stress_factor)
        return max(0.2, min(intensity, 0.8))

    def _generate_action_steps(self, intervention_type):
        """Create specific, actionable steps"""
        action_steps = {
            'stress_reduction': [
                {'step': 1, 'action': 'Find quiet space', 'duration': '1 min'},
                {'step': 2, 'action': 'Deep breathing exercise', 'duration': '2 min'},
                {'step': 3, 'action': 'Mindful body scan', 'duration': '2 min'}
            ],
            'focus_enhancement': [
                {'step': 1, 'action': 'Clear desktop', 'duration': '1 min'},
                {'step': 2, 'action': 'Set specific goal', 'duration': '2 min'},
                {'step': 3, 'action': 'Enable do-not-disturb', 'duration': '30 sec'}
            ],
            'productivity_optimization': [
                {'step': 1, 'action': 'List top 3 priorities', 'duration': '2 min'},
                {'step': 2, 'action': 'Break down main task', 'duration': '3 min'},
                {'step': 3, 'action': 'Set timer for first chunk', 'duration': '1 min'}
            ]
        }
        return action_steps[intervention_type]

    def update_user_model(self, user_id, intervention_response):
        """Update user model based on intervention response"""
        if user_id not in self.user_profiles:
            return
            
        profile = self.user_profiles[user_id]
        profile['response_history'].append(intervention_response)
        
        # Update engagement and effectiveness metrics
        profile['engagement_level'] = self._calculate_engagement(profile['response_history'])
        
        # Adjust future interventions based on response
        self._refine_intervention_strategy(profile, intervention_response)