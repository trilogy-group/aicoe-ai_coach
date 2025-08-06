class EnhancedAICoach:
    def __init__(self):
        # Personality and cognitive profiles
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
            'interruption_cost': 0.0
        }
        
        # Behavioral psychology components
        self.behavioral_patterns = {
            'habit_triggers': {},
            'response_history': [],
            'reinforcement_schedule': {},
            'progress_markers': {}
        }
        
        # Personalization engine
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': {},
            'response_preferences': {},
            'peak_performance_times': [],
            'burnout_indicators': [],
            'motivation_factors': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._assess_energy_level(user_state),
            'focus_state': self._detect_flow_state(user_state),
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
        content = self._personalize_content(intervention_type, user_profile)
        timing = self._optimize_timing(context)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': timing,
            'delivery_method': self._get_preferred_delivery(user_profile)
        }

    def track_effectiveness(self, intervention, user_response):
        """Monitor and learn from intervention outcomes"""
        self.behavioral_patterns['response_history'].append({
            'intervention': intervention,
            'response': user_response,
            'context': self.context_tracker.copy(),
            'timestamp': self._get_timestamp()
        })
        
        self._update_reinforcement_schedule(user_response)
        self._adjust_personalization(user_response)

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive demands"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'concurrent_tasks': len(user_state.get('active_tasks', [])),
            'time_pressure': user_state.get('deadline_proximity', 0),
            'interruption_frequency': user_state.get('interruption_count', 0)
        }
        return sum(factors.values()) / len(factors)

    def _detect_flow_state(self, user_state):
        """Identify if user is in flow state"""
        indicators = {
            'focus_duration': user_state.get('focus_duration', 0),
            'task_engagement': user_state.get('engagement_level', 0),
            'productivity_rate': user_state.get('productivity_rate', 0)
        }
        return 'flow' if all(v > 0.7 for v in indicators.values()) else 'normal'

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        return (
            context['cognitive_load'] < 0.7 and
            context['focus_state'] != 'flow' and
            context['interruption_cost'] < 0.5
        )

    def _select_intervention_type(self, context, user_profile):
        """Choose most appropriate intervention"""
        options = {
            'micro_break': context['energy_level'] < 0.3,
            'focus_boost': context['cognitive_load'] > 0.6,
            'progress_check': self._is_milestone_due(),
            'habit_reminder': self._check_habit_triggers()
        }
        return max(options.items(), key=lambda x: x[1])[0]

    def _personalize_content(self, intervention_type, user_profile):
        """Customize intervention content"""
        base_content = self._get_base_content(intervention_type)
        personality_adjustments = self.personality_type_configs[user_profile['personality_type']]
        
        return self._adapt_content(
            base_content,
            personality_adjustments,
            user_profile['learning_patterns']
        )

    def _optimize_timing(self, context):
        """Determine optimal delivery timing"""
        if context['focus_state'] == 'flow':
            return 'defer'
        
        return {
            'immediate': context['interruption_cost'] < 0.3,
            'next_break': 0.3 <= context['interruption_cost'] < 0.7,
            'end_of_session': context['interruption_cost'] >= 0.7
        }

    def _update_reinforcement_schedule(self, response):
        """Adjust reinforcement patterns based on response"""
        effectiveness = response.get('effectiveness', 0)
        current_schedule = self.behavioral_patterns['reinforcement_schedule']
        
        if effectiveness > 0.7:
            current_schedule['frequency'] *= 1.1
        elif effectiveness < 0.3:
            current_schedule['frequency'] *= 0.9

    def _adjust_personalization(self, response):
        """Refine personalization based on feedback"""
        self.user_profile['learning_patterns'].update({
            'response_speed': response.get('response_time'),
            'completion_rate': response.get('completion'),
            'satisfaction': response.get('satisfaction')
        })