class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.context_models = {}
        self.behavioral_patterns = {}
        self.intervention_history = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'cognitive_state': None,
            'attention_capacity': 1.0,
            'motivation_level': 1.0,
            'stress_level': 0.0,
            'learning_patterns': [],
            'response_history': [],
            'success_metrics': {}
        }
        
    def assess_context(self, user_id, context_data):
        """Analyze current user context and state"""
        context = {
            'cognitive_load': self._calculate_cognitive_load(context_data),
            'time_of_day': context_data.get('time'),
            'task_complexity': context_data.get('complexity', 0.5),
            'environment': context_data.get('environment', 'neutral'),
            'recent_activity': context_data.get('recent_activity', [])
        }
        self.context_models[user_id] = context
        return context

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        user = self.user_profiles[user_id]
        current_context = self.context_models[user_id]

        # Select optimal intervention type based on state
        if current_context['cognitive_load'] > 0.8:
            return self._generate_minimal_intervention(user, context)
        elif user['motivation_level'] < 0.4:
            return self._generate_motivation_boost(user, context)
        else:
            return self._generate_standard_intervention(user, context)

    def _generate_standard_intervention(self, user, context):
        """Generate detailed coaching intervention"""
        intervention = {
            'type': 'standard',
            'priority': self._calculate_priority(context),
            'recommendations': self._get_specific_recommendations(context),
            'action_steps': self._generate_action_steps(context),
            'success_metrics': self._define_success_metrics(context),
            'time_estimates': self._estimate_completion_time(context),
            'alternatives': self._generate_alternatives(context),
            'follow_up': self._schedule_follow_up(context)
        }
        return intervention

    def _generate_minimal_intervention(self, user, context):
        """Generate lightweight intervention for high cognitive load"""
        return {
            'type': 'minimal',
            'priority': 'low',
            'message': self._get_minimal_message(context),
            'action': self._get_single_action(context)
        }

    def _generate_motivation_boost(self, user, context):
        """Generate motivation-focused intervention"""
        return {
            'type': 'motivation',
            'priority': 'high',
            'message': self._get_motivation_message(context),
            'quick_wins': self._get_quick_wins(context),
            'reinforcement': self._get_reinforcement_strategy(context)
        }

    def track_response(self, user_id, intervention_id, response_data):
        """Track user response to intervention"""
        if user_id not in self.intervention_history:
            self.intervention_history[user_id] = []
            
        response = {
            'intervention_id': intervention_id,
            'timestamp': response_data['timestamp'],
            'completion_rate': response_data.get('completion_rate', 0),
            'satisfaction': response_data.get('satisfaction', 0),
            'difficulty': response_data.get('difficulty', 0),
            'effectiveness': response_data.get('effectiveness', 0)
        }
        
        self.intervention_history[user_id].append(response)
        self._update_user_profile(user_id, response)

    def _update_user_profile(self, user_id, response):
        """Update user profile based on intervention response"""
        user = self.user_profiles[user_id]
        user['response_history'].append(response)
        
        # Update learning patterns
        user['learning_patterns'].append({
            'intervention_type': response['intervention_id'],
            'effectiveness': response['effectiveness']
        })
        
        # Adjust motivation and attention metrics
        user['motivation_level'] = self._recalculate_motivation(user, response)
        user['attention_capacity'] = self._recalculate_attention(user, response)

    def _calculate_cognitive_load(self, context_data):
        """Calculate current cognitive load"""
        base_load = context_data.get('base_load', 0.5)
        task_complexity = context_data.get('complexity', 0.5)
        time_pressure = context_data.get('time_pressure', 0.5)
        
        return min(1.0, (base_load + task_complexity + time_pressure) / 3)

    def _get_specific_recommendations(self, context):
        """Generate specific, actionable recommendations"""
        task_type = context.get('task_type')
        recommendations = []
        
        if task_type == 'focus':
            recommendations.extend([
                {'action': 'Enable Do Not Disturb mode', 'duration': '25 mins'},
                {'action': 'Clear desktop of distractions', 'duration': '2 mins'},
                {'action': 'Set specific task goal', 'duration': '3 mins'}
            ])
        # Add more task-specific recommendations
        
        return recommendations

    def _define_success_metrics(self, context):
        """Define measurable success metrics"""
        return {
            'completion_rate': 'Complete 80% of recommended actions',
            'time_saved': 'Reduce task time by 20%',
            'quality_improvement': 'Reduce errors by 30%',
            'satisfaction': 'Maintain satisfaction score above 4/5'
        }

    def _schedule_follow_up(self, context):
        """Schedule appropriate follow-up checks"""
        return {
            'timing': self._calculate_optimal_timing(context),
            'type': self._determine_follow_up_type(context),
            'metrics': self._get_follow_up_metrics(context)
        }

    def get_optimization_metrics(self):
        """Return system optimization metrics"""
        return {
            'avg_completion_rate': self._calculate_avg_completion(),
            'avg_satisfaction': self._calculate_avg_satisfaction(),
            'behavioral_change': self._calculate_behavioral_change(),
            'intervention_effectiveness': self._calculate_effectiveness()
        }