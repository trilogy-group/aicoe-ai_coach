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
            'recent_interactions': [],
            'pending_tasks': []
        }

        # Intervention configuration
        self.intervention_config = {
            'min_interval': 30,  # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'adaptivity_rate': 0.1
        }

    def assess_user_state(self, user_data):
        """Evaluate current user cognitive and emotional state"""
        self.user_state['cognitive_load'] = self._calculate_cognitive_load(user_data)
        self.user_state['energy_level'] = self._estimate_energy_level(user_data)
        self.user_state['focus_state'] = self._detect_flow_state(user_data)
        self.user_state['stress_level'] = self._analyze_stress_indicators(user_data)
        self.user_state['receptivity'] = self._calculate_receptivity()

    def generate_intervention(self, user_context):
        """Create personalized coaching intervention"""
        if not self._should_intervene():
            return None

        intervention = {
            'type': self._select_intervention_type(),
            'content': self._generate_content(),
            'timing': self._optimize_timing(),
            'delivery_method': self._select_delivery_method(),
            'intensity': self._calibrate_intensity()
        }

        return self._personalize_intervention(intervention, user_context)

    def update_behavior_patterns(self, user_response):
        """Update behavior tracking based on user response"""
        self.behavior_patterns['success_patterns'].append({
            'intervention': user_response['intervention'],
            'outcome': user_response['outcome'],
            'context': self.context.copy()
        })
        
        self._update_motivation_model(user_response)
        self._refine_resistance_points(user_response)
        self._adjust_intervention_params(user_response)

    def _calculate_cognitive_load(self, user_data):
        """Estimate current cognitive load using multiple indicators"""
        task_complexity = self._analyze_task_complexity(user_data['current_task'])
        context_switches = len(user_data['recent_task_switches'])
        time_pressure = user_data['deadline_proximity']
        
        return (0.4 * task_complexity + 
                0.3 * context_switches + 
                0.3 * time_pressure)

    def _detect_flow_state(self, user_data):
        """Identify if user is in flow state"""
        productivity = user_data['productivity_metrics']
        focus_duration = user_data['focus_duration']
        interruption_rate = user_data['interruption_rate']
        
        if (productivity > 0.8 and 
            focus_duration > 25 and 
            interruption_rate < 0.2):
            return 'flow'
        return 'neutral'

    def _calculate_receptivity(self):
        """Determine user's likely receptivity to coaching"""
        return (0.4 * (1 - self.user_state['cognitive_load']) +
                0.3 * self.user_state['energy_level'] +
                0.3 * (1 - self.user_state['stress_level']))

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (self.user_state['receptivity'] > 0.6 and
                self._check_intervention_timing() and
                self.user_state['focus_state'] != 'flow')

    def _personalize_intervention(self, intervention, user_context):
        """Customize intervention based on user context and patterns"""
        personality_config = self.personality_type_configs[user_context['personality_type']]
        
        intervention['content'] = self._adapt_to_learning_style(
            intervention['content'], 
            personality_config['learning_style']
        )
        
        intervention['delivery_method'] = self._adapt_to_communication_pref(
            intervention['delivery_method'],
            personality_config['communication_pref']
        )
        
        return intervention

    def _calibrate_intensity(self):
        """Adjust intervention intensity based on user state and patterns"""
        base_intensity = self.intervention_config['intensity_level']
        receptivity_factor = self.user_state['receptivity']
        stress_adjustment = 1 - self.user_state['stress_level']
        
        return base_intensity * receptivity_factor * stress_adjustment

    def _optimize_timing(self):
        """Determine optimal intervention timing"""
        current_load = self.user_state['cognitive_load']
        energy_level = self.user_state['energy_level']
        task_urgency = self.context['pending_tasks'][0]['urgency'] if self.context['pending_tasks'] else 0
        
        return {
            'delay': self._calculate_optimal_delay(current_load, energy_level, task_urgency),
            'duration': self._calculate_intervention_duration(),
            'frequency': self._adjust_frequency()
        }

    def _update_motivation_model(self, user_response):
        """Update understanding of user motivation patterns"""
        if user_response['outcome'] > 0.7:
            self.behavior_patterns['motivation_drivers'].add(
                user_response['intervention']['type']
            )

    def _refine_resistance_points(self, user_response):
        """Identify and update resistance patterns"""
        if user_response['outcome'] < 0.3:
            self.behavior_patterns['resistance_points'].add(
                user_response['intervention']['type']
            )