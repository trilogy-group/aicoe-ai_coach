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
            'motivation_drivers': set(),
            'resistance_points': set(),
            'success_patterns': []
        }

        # Context awareness parameters
        self.context = {
            'time_of_day': None,
            'work_context': None,
            'environment': None,
            'recent_activities': [],
            'upcoming_events': []
        }

        # Intervention configuration
        self.intervention_config = {
            'min_interval': 30,  # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'adaptivity_rate': 0.1
        }

    def assess_user_state(self, metrics):
        """
        Enhanced user state assessment incorporating multiple factors
        """
        self.user_state['cognitive_load'] = self._calculate_cognitive_load(metrics)
        self.user_state['energy_level'] = self._estimate_energy_level(metrics)
        self.user_state['focus_state'] = self._determine_focus_state(metrics)
        self.user_state['stress_level'] = self._analyze_stress_indicators(metrics)
        self.user_state['receptivity'] = self._calculate_receptivity()

    def generate_intervention(self, user_context):
        """
        Creates personalized, context-aware coaching interventions
        """
        if not self._should_intervene():
            return None

        intervention_type = self._select_intervention_type()
        content = self._personalize_content(intervention_type, user_context)
        timing = self._optimize_timing()
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': timing,
            'intensity': self._calculate_intensity(),
            'follow_up': self._plan_follow_up()
        }

    def update_behavior_patterns(self, user_response):
        """
        Updates behavior pattern tracking based on user response
        """
        success = self._evaluate_response_success(user_response)
        self.behavior_patterns['success_patterns'].append({
            'context': self.context.copy(),
            'intervention': self.last_intervention,
            'success': success
        })
        self._adapt_intervention_strategy(success)

    def _calculate_cognitive_load(self, metrics):
        """
        Sophisticated cognitive load estimation
        """
        factors = {
            'task_complexity': metrics.get('task_complexity', 0.5),
            'time_pressure': metrics.get('time_pressure', 0.5),
            'interruption_frequency': metrics.get('interruptions', 0.3),
            'task_familiarity': metrics.get('familiarity', 0.7)
        }
        return sum(v * k for k, v in factors.items()) / len(factors)

    def _optimize_timing(self):
        """
        Determines optimal intervention timing
        """
        current_load = self.user_state['cognitive_load']
        energy_level = self.user_state['energy_level']
        focus_state = self.user_state['focus_state']
        
        if focus_state == 'flow':
            return self._delay_intervention()
        
        return self._calculate_optimal_time(current_load, energy_level)

    def _personalize_content(self, intervention_type, user_context):
        """
        Creates highly personalized intervention content
        """
        personality_config = self.personality_type_configs[user_context['personality_type']]
        
        return {
            'message': self._generate_message(personality_config),
            'action_items': self._generate_action_items(intervention_type),
            'difficulty': self._adjust_difficulty(user_context),
            'support_resources': self._compile_resources(intervention_type)
        }

    def _should_intervene(self):
        """
        Determines if intervention is appropriate
        """
        return (
            self.user_state['receptivity'] > 0.6 and
            self.user_state['cognitive_load'] < 0.8 and
            self._check_intervention_timing()
        )

    def _adapt_intervention_strategy(self, success):
        """
        Adapts intervention strategy based on success
        """
        self.intervention_config['intensity_level'] += (
            self.intervention_config['adaptivity_rate'] if success 
            else -self.intervention_config['adaptivity_rate']
        )
        self.intervention_config['intensity_level'] = max(0.1, min(1.0, self.intervention_config['intensity_level']))

    def _calculate_intensity(self):
        """
        Calculates appropriate intervention intensity
        """
        base_intensity = self.intervention_config['intensity_level']
        modifiers = {
            'cognitive_load': -0.3,
            'stress_level': -0.2,
            'receptivity': 0.2
        }
        
        return base_intensity * sum(v * self.user_state[k] for k, v in modifiers.items())

    def _plan_follow_up(self):
        """
        Plans follow-up interventions
        """
        return {
            'timing': self._calculate_follow_up_timing(),
            'type': self._select_follow_up_type(),
            'success_criteria': self._define_success_criteria()
        }

    def get_effectiveness_metrics(self):
        """
        Returns intervention effectiveness metrics
        """
        return {
            'success_rate': self._calculate_success_rate(),
            'user_engagement': self._measure_engagement(),
            'behavior_change': self._measure_behavior_change(),
            'user_satisfaction': self._measure_satisfaction()
        }