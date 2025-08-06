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

        # Behavioral psychology patterns
        self.behavior_patterns = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation_drivers': [],
            'resistance_points': [],
            'success_patterns': []
        }

        # Context awareness settings
        self.context = {
            'time_of_day': None,
            'work_context': None,
            'environment': None,
            'recent_interactions': [],
            'task_complexity': 0.0
        }

        # Intervention configurations
        self.intervention_config = {
            'min_interval': 30,  # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'adaptation_rate': 0.1
        }

    def assess_user_state(self, user_data):
        """Evaluate current user cognitive and emotional state"""
        self.user_state['cognitive_load'] = self._calculate_cognitive_load(user_data)
        self.user_state['energy_level'] = self._analyze_energy_patterns(user_data)
        self.user_state['focus_state'] = self._detect_flow_state(user_data)
        self.user_state['stress_level'] = self._evaluate_stress_indicators(user_data)
        self.user_state['receptivity'] = self._calculate_receptivity(user_data)
        
        return self.user_state

    def generate_intervention(self, user_context):
        """Create personalized coaching intervention"""
        if not self._should_intervene(user_context):
            return None

        intervention_type = self._select_intervention_type()
        content = self._generate_content(intervention_type)
        timing = self._optimize_timing(user_context)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': timing,
            'intensity': self._calculate_intensity(),
            'action_steps': self._generate_action_steps()
        }

    def update_behavior_patterns(self, user_response):
        """Update behavior tracking based on user response"""
        self.behavior_patterns['success_patterns'].append(user_response)
        self._adapt_intervention_strategy(user_response)
        self._update_effectiveness_metrics(user_response)

    def _calculate_cognitive_load(self, data):
        """Assess current cognitive load based on multiple factors"""
        task_complexity = data.get('task_complexity', 0.5)
        context_switches = data.get('context_switches', 0)
        time_pressure = data.get('time_pressure', 0.5)
        
        return (task_complexity + context_switches * 0.1 + time_pressure) / 3

    def _analyze_energy_patterns(self, data):
        """Analyze user energy levels and patterns"""
        time_of_day = data.get('time_of_day')
        recent_activity = data.get('recent_activity', [])
        rest_periods = data.get('rest_periods', [])
        
        return self._calculate_energy_score(time_of_day, recent_activity, rest_periods)

    def _detect_flow_state(self, data):
        """Detect if user is in flow state"""
        focus_duration = data.get('focus_duration', 0)
        task_engagement = data.get('task_engagement', 0)
        interruption_rate = data.get('interruption_rate', 0)
        
        if focus_duration > 25 and task_engagement > 0.8 and interruption_rate < 0.2:
            return 'flow'
        return 'neutral'

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        last_intervention = context.get('last_intervention_time')
        current_state = self.assess_user_state(context)
        
        return (
            self._check_timing_appropriate(last_intervention) and
            current_state['receptivity'] > 0.6 and
            not self._is_in_flow_state()
        )

    def _generate_content(self, intervention_type):
        """Generate personalized intervention content"""
        templates = self._get_content_templates(intervention_type)
        selected_template = self._select_best_template(templates)
        
        return self._personalize_content(selected_template)

    def _generate_action_steps(self):
        """Create specific, actionable steps"""
        return [
            {
                'step': 'specific_action',
                'timeframe': 'immediate',
                'difficulty': 'achievable',
                'expected_outcome': 'measurable_result'
            }
        ]

    def _calculate_intensity(self):
        """Calculate appropriate intervention intensity"""
        base_intensity = self.intervention_config['intensity_level']
        user_receptivity = self.user_state['receptivity']
        stress_factor = 1 - self.user_state['stress_level']
        
        return base_intensity * user_receptivity * stress_factor

    def _adapt_intervention_strategy(self, response):
        """Adapt intervention strategy based on user response"""
        success_rate = response.get('success_rate', 0)
        engagement_level = response.get('engagement', 0)
        
        self.intervention_config['intensity_level'] *= (1 + self.intervention_config['adaptation_rate'] * (success_rate - 0.5))
        self.intervention_config['adaptation_rate'] = max(0.05, min(0.2, self.intervention_config['adaptation_rate'] * engagement_level))

    def _update_effectiveness_metrics(self, response):
        """Update intervention effectiveness tracking"""
        self.behavior_patterns['success_patterns'] = self.behavior_patterns['success_patterns'][-50:]  # Keep last 50 responses
        self._calculate_success_rate()
        self._update_resistance_points(response)