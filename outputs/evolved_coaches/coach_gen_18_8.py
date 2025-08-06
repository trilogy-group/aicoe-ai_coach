class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced user state tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': 'neutral',
            'stress_level': 0.0,
            'receptivity': 0.0
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': [],
            'motivation_factors': [],
            'resistance_patterns': [],
            'success_markers': []
        }

        # Context awareness settings
        self.context_params = {
            'time_of_day': None,
            'work_context': None,
            'environment': None,
            'social_setting': None,
            'priority_level': 0
        }

        # Intervention configuration
        self.intervention_settings = {
            'frequency': 'adaptive',
            'intensity': 'dynamic',
            'style': 'personalized',
            'timing': 'context_aware'
        }

    def assess_user_state(self, user_data):
        """Evaluate current user cognitive and emotional state"""
        self.user_state['cognitive_load'] = self._calculate_cognitive_load(user_data)
        self.user_state['energy_level'] = self._analyze_energy_patterns(user_data)
        self.user_state['focus_state'] = self._determine_focus_state(user_data)
        self.user_state['stress_level'] = self._evaluate_stress_indicators(user_data)
        self.user_state['receptivity'] = self._calculate_receptivity(user_data)
        
        return self.user_state

    def generate_intervention(self, user_context, personality_type):
        """Create personalized coaching intervention"""
        if not self._is_appropriate_timing(user_context):
            return None

        intervention = {
            'type': self._select_intervention_type(user_context),
            'content': self._generate_content(personality_type),
            'delivery_method': self._determine_delivery_method(user_context),
            'urgency': self._calculate_urgency(user_context),
            'actionability': self._ensure_actionability()
        }

        return self._personalize_intervention(intervention, personality_type)

    def update_behavior_model(self, user_response, intervention_data):
        """Update behavioral model based on intervention outcomes"""
        success_rate = self._calculate_success_rate(user_response)
        self.behavior_triggers['success_markers'].append({
            'intervention': intervention_data,
            'response': user_response,
            'success_rate': success_rate
        })
        
        self._adjust_intervention_parameters(success_rate)
        self._update_learning_patterns(user_response)

    def _calculate_cognitive_load(self, user_data):
        """Assess current cognitive load based on multiple factors"""
        task_complexity = user_data.get('task_complexity', 0.5)
        current_activities = user_data.get('current_activities', [])
        time_pressure = user_data.get('time_pressure', 0.5)
        
        return (task_complexity + len(current_activities) * 0.1 + time_pressure) / 3

    def _analyze_energy_patterns(self, user_data):
        """Analyze user energy levels and patterns"""
        time_of_day = user_data.get('time_of_day')
        recent_activity = user_data.get('recent_activity', [])
        rest_periods = user_data.get('rest_periods', [])
        
        return self._calculate_energy_score(time_of_day, recent_activity, rest_periods)

    def _determine_focus_state(self, user_data):
        """Evaluate user's current focus state"""
        activity_duration = user_data.get('activity_duration', 0)
        interruption_frequency = user_data.get('interruption_frequency', 0)
        task_switches = user_data.get('task_switches', 0)
        
        if activity_duration > 45 and interruption_frequency < 0.2:
            return 'flow'
        elif task_switches > 5:
            return 'scattered'
        return 'neutral'

    def _personalize_intervention(self, intervention, personality_type):
        """Customize intervention based on personality type"""
        config = self.personality_type_configs[personality_type]
        
        intervention['content'] = self._adapt_content_style(
            intervention['content'],
            config['communication_pref']
        )
        
        intervention['delivery_method'] = self._adapt_delivery_method(
            intervention['delivery_method'],
            config['learning_style']
        )
        
        return intervention

    def _ensure_actionability(self):
        """Generate specific, actionable recommendations"""
        return {
            'immediate_action': self._generate_immediate_step(),
            'follow_up_steps': self._generate_follow_up_steps(),
            'success_criteria': self._define_success_criteria(),
            'progress_tracking': self._create_tracking_method()
        }

    def _calculate_receptivity(self, user_data):
        """Calculate user's current receptivity to coaching"""
        return (
            self.user_state['energy_level'] * 0.3 +
            (1 - self.user_state['cognitive_load']) * 0.3 +
            (1 - self.user_state['stress_level']) * 0.4
        )

    def _is_appropriate_timing(self, user_context):
        """Determine if current moment is appropriate for intervention"""
        return (
            self.user_state['receptivity'] > 0.6 and
            not self._is_in_flow_state() and
            self._has_attention_capacity(user_context)
        )