class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced context tracking
        self.context_tracker = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': 'neutral',
            'time_of_day': None,
            'work_context': None,
            'interruption_cost': 0.0
        }

        # Behavioral psychology components
        self.behavioral_patterns = {
            'habit_strength': {},
            'motivation_factors': {},
            'resistance_points': {},
            'success_triggers': {}
        }

        # Personalization metrics
        self.user_profile = {
            'learning_history': [],
            'response_patterns': {},
            'preference_weights': {},
            'intervention_effectiveness': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        focus_impact = self._assess_focus_impact(environment_data)
        timing_score = self._evaluate_timing_appropriateness(user_state)
        
        return {
            'intervention_appropriate': cognitive_load < 0.7 and focus_impact < 0.5,
            'optimal_timing': timing_score > 0.8,
            'suggested_intensity': self._calculate_intensity(cognitive_load)
        }

    def generate_intervention(self, user_context, behavioral_goal):
        """Create personalized coaching intervention"""
        # Select intervention type based on user profile and context
        intervention_type = self._select_intervention_type(user_context)
        
        # Generate specific actionable recommendation
        recommendation = self._create_actionable_recommendation(
            intervention_type,
            behavioral_goal,
            self.user_profile['learning_history']
        )

        # Personalize communication style
        formatted_message = self._personalize_communication(
            recommendation,
            self.user_profile['preference_weights']
        )

        return {
            'message': formatted_message,
            'action_steps': self._generate_action_steps(behavioral_goal),
            'follow_up': self._schedule_follow_up(intervention_type)
        }

    def update_effectiveness(self, intervention_id, user_response):
        """Track and update intervention effectiveness"""
        self.user_profile['intervention_effectiveness'][intervention_id] = user_response
        self._update_learning_patterns(intervention_id, user_response)
        self._adjust_strategy_weights(user_response)

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'time_pressure': user_state.get('time_pressure', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'mental_fatigue': user_state.get('fatigue_level', 0.4)
        }
        
        return sum(factors.values()) / len(factors)

    def _assess_focus_impact(self, environment_data):
        """Evaluate potential impact on user's focus"""
        return min(
            environment_data.get('task_urgency', 0.5),
            1 - environment_data.get('focus_depth', 0.5)
        )

    def _create_actionable_recommendation(self, intervention_type, goal, history):
        """Generate specific, actionable recommendations"""
        base_recommendations = {
            'habit_formation': self._generate_habit_steps(goal),
            'productivity': self._generate_productivity_tactics(goal),
            'learning': self._generate_learning_strategies(goal)
        }
        
        return self._enhance_with_context(
            base_recommendations[intervention_type],
            history
        )

    def _generate_action_steps(self, goal):
        """Create specific, measurable action steps"""
        return [
            {
                'step': f"Step {i+1}",
                'timeframe': f"{5*(i+1)} minutes",
                'success_criteria': f"Completion criteria {i+1}"
            }
            for i in range(3)
        ]

    def _personalize_communication(self, message, preferences):
        """Adapt communication style to user preferences"""
        tone = preferences.get('communication_tone', 'neutral')
        detail_level = preferences.get('detail_preference', 'medium')
        
        return self._format_message(message, tone, detail_level)

    def _update_learning_patterns(self, intervention_id, response):
        """Update user learning patterns based on intervention response"""
        self.user_profile['learning_history'].append({
            'intervention_id': intervention_id,
            'response': response,
            'timestamp': self._get_current_timestamp(),
            'context': self.context_tracker.copy()
        })

    def _adjust_strategy_weights(self, response):
        """Adjust intervention strategy weights based on effectiveness"""
        effectiveness = response.get('effectiveness', 0.5)
        strategy = response.get('strategy_type')
        
        current_weight = self.user_profile['preference_weights'].get(strategy, 1.0)
        self.user_profile['preference_weights'][strategy] = (
            current_weight * 0.8 + effectiveness * 0.2
        )

    def _schedule_follow_up(self, intervention_type):
        """Determine optimal follow-up timing"""
        return {
            'timing': self._calculate_optimal_timing(),
            'type': self._select_follow_up_type(intervention_type),
            'intensity': self._calculate_follow_up_intensity()
        }