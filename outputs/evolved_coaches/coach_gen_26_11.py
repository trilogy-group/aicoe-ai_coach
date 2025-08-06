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
            'time_of_day': None,
            'work_context': None,
            'interruption_cost': 0.0
        }
        
        # Behavioral psychology components
        self.behavioral_patterns = {
            'habit_triggers': {},
            'response_history': [],
            'intervention_effectiveness': {},
            'reinforcement_schedule': {}
        }
        
        # User personalization data
        self.user_profile = {
            'personality_type': None,
            'learning_preferences': {},
            'peak_performance_times': [],
            'stress_indicators': {},
            'motivation_factors': [],
            'progress_metrics': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy_level(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity'),
            'interruption_cost': self._calculate_interruption_cost()
        })
        return self.context_tracker

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if not self._should_intervene(context):
            return None
            
        intervention_type = self._select_intervention_type(context, user_profile)
        
        intervention = {
            'content': self._generate_content(intervention_type, user_profile),
            'timing': self._optimize_timing(context),
            'delivery_style': self._personalize_delivery(user_profile),
            'action_steps': self._create_action_steps(intervention_type),
            'follow_up': self._plan_follow_up(intervention_type)
        }
        
        return intervention

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'context_switches': user_state.get('context_switches', 0),
            'time_pressure': user_state.get('time_pressure', 0)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_energy_level(self, user_state):
        """Estimate user energy level based on various factors"""
        return user_state.get('energy_level', 0.5)

    def _calculate_interruption_cost(self):
        """Calculate cost of interrupting current user activity"""
        return (self.context_tracker['cognitive_load'] * 0.6 + 
                (1 - self.context_tracker['energy_level']) * 0.4)

    def _should_intervene(self, context):
        """Determine if intervention is appropriate now"""
        return (context['interruption_cost'] < 0.7 and
                context['cognitive_load'] < 0.8 and
                context['energy_level'] > 0.3)

    def _select_intervention_type(self, context, user_profile):
        """Choose most appropriate intervention type"""
        options = ['micro_learning', 'habit_reminder', 'reflection_prompt', 
                  'goal_check', 'skill_practice']
        
        # Score each option based on context and user profile
        scores = {option: self._score_intervention(option, context, user_profile) 
                 for option in options}
        
        return max(scores, key=scores.get)

    def _generate_content(self, intervention_type, user_profile):
        """Generate personalized intervention content"""
        content_templates = {
            'micro_learning': "Here's a quick tip for {topic} based on {style}...",
            'habit_reminder': "Time to practice {habit} - remember your goal of {goal}...",
            'reflection_prompt': "Consider how {focus_area} affected your {outcome}...",
            'goal_check': "You're making progress on {goal}. Next step: {action}...",
            'skill_practice': "Let's strengthen your {skill} with this {duration} exercise..."
        }
        
        return self._personalize_template(
            content_templates[intervention_type], 
            user_profile
        )

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        return {
            'preferred_time': self._get_optimal_time(context),
            'max_delay': self._calculate_max_delay(context),
            'reminder_frequency': self._get_reminder_frequency(context)
        }

    def _personalize_delivery(self, user_profile):
        """Personalize intervention delivery style"""
        style = self.personality_type_configs.get(
            user_profile['personality_type'],
            {'communication_pref': 'neutral'}
        )
        
        return {
            'tone': style['communication_pref'],
            'format': user_profile['learning_preferences'].get('format', 'text'),
            'length': self._calculate_optimal_length(user_profile)
        }

    def _create_action_steps(self, intervention_type):
        """Generate specific, actionable steps"""
        return [
            {'step': 1, 'action': 'Specific action description', 'duration': '5m'},
            {'step': 2, 'action': 'Next specific action', 'duration': '10m'},
            {'step': 3, 'action': 'Final specific action', 'duration': '5m'}
        ]

    def _plan_follow_up(self, intervention_type):
        """Plan intervention follow-up"""
        return {
            'check_in_time': '+1h',
            'success_metrics': ['completion', 'effectiveness', 'satisfaction'],
            'adaptation_triggers': ['struggle', 'success', 'skip']
        }

    def update_effectiveness(self, intervention_id, feedback):
        """Update intervention effectiveness tracking"""
        self.behavioral_patterns['intervention_effectiveness'][intervention_id] = feedback
        self._adapt_strategies(feedback)

    def _adapt_strategies(self, feedback):
        """Adapt coaching strategies based on feedback"""
        if feedback['effectiveness'] < 0.5:
            self._adjust_intervention_parameters(feedback)