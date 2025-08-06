class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced psychological models
        self.cognitive_models = {
            'attention': {'capacity': 0.0, 'fatigue': 0.0, 'recovery_rate': 0.0},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0, 'self_efficacy': 0.0},
            'emotional': {'valence': 0.0, 'arousal': 0.0, 'dominance': 0.0}
        }

        # Context tracking
        self.context_tracker = {
            'time_of_day': None,
            'work_phase': None, 
            'cognitive_load': 0.0,
            'interruption_cost': 0.0,
            'flow_state': False
        }

        # Behavioral intervention settings
        self.intervention_config = {
            'min_interval': 30,  # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'adaptation_rate': 0.1
        }

        # User profile and history
        self.user_profile = {
            'personality_type': None,
            'preferred_times': [],
            'response_history': [],
            'success_patterns': {},
            'learning_curve': {}
        }

    def update_cognitive_state(self, metrics):
        """Update cognitive and emotional state based on user metrics"""
        self.cognitive_models['attention']['capacity'] = metrics.get('focus_level', 0.5)
        self.cognitive_models['motivation']['intrinsic'] = metrics.get('engagement', 0.5)
        self.cognitive_models['emotional']['valence'] = metrics.get('mood', 0.0)
        
        # Update context
        self.context_tracker['cognitive_load'] = self._calculate_cognitive_load(metrics)
        self.context_tracker['flow_state'] = self._detect_flow_state(metrics)

    def generate_intervention(self, context):
        """Generate personalized coaching intervention"""
        if not self._should_intervene():
            return None

        intervention_type = self._select_intervention_type()
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(intervention_type),
            'timing': self._optimize_timing(),
            'intensity': self._calculate_intensity(),
            'action_steps': self._generate_action_steps()
        }

        return self._personalize_intervention(intervention)

    def _calculate_cognitive_load(self, metrics):
        """Estimate current cognitive load"""
        task_complexity = metrics.get('task_complexity', 0.5)
        time_pressure = metrics.get('time_pressure', 0.5)
        context_switches = metrics.get('context_switches', 0)
        
        return (0.4 * task_complexity + 
                0.3 * time_pressure + 
                0.3 * min(context_switches / 10, 1.0))

    def _detect_flow_state(self, metrics):
        """Detect if user is in flow state"""
        focus_duration = metrics.get('focus_duration', 0)
        task_progress = metrics.get('task_progress', 0.0)
        interruption_rate = metrics.get('interruption_rate', 0.0)
        
        return (focus_duration > 25 and
                task_progress > 0.3 and
                interruption_rate < 0.2)

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        if self.context_tracker['flow_state']:
            return False
            
        time_since_last = self._get_time_since_last_intervention()
        if time_since_last < self.intervention_config['min_interval']:
            return False
            
        return (self.context_tracker['cognitive_load'] < 0.8 and
                self._get_daily_intervention_count() < self.intervention_config['max_daily'])

    def _select_intervention_type(self):
        """Select most appropriate intervention type"""
        options = ['motivation', 'focus', 'planning', 'reflection', 'skill_building']
        
        # Choose based on current state and history
        if self.cognitive_models['motivation']['intrinsic'] < 0.3:
            return 'motivation'
        elif self.cognitive_models['attention']['capacity'] < 0.3:
            return 'focus'
        
        return self._get_most_effective_type()

    def _generate_content(self, intervention_type):
        """Generate intervention content"""
        templates = self._get_intervention_templates(intervention_type)
        selected = self._select_best_template(templates)
        
        return self._fill_template(selected, {
            'user_name': self.user_profile.get('name'),
            'context': self.context_tracker['work_phase'],
            'specific_goal': self._get_current_goal()
        })

    def _generate_action_steps(self):
        """Generate specific actionable steps"""
        return [
            {
                'step': 1,
                'action': 'Specific action description',
                'timeframe': '5 minutes',
                'difficulty': 'easy',
                'expected_outcome': 'Measurable result'
            },
            # Additional steps...
        ]

    def _personalize_intervention(self, intervention):
        """Personalize intervention based on user profile"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        return {
            **intervention,
            'tone': config.get('communication_pref', 'neutral'),
            'format': config.get('learning_style', 'balanced'),
            'timing': self._adjust_timing(intervention['timing']),
            'intensity': self._adjust_intensity(intervention['intensity'])
        }

    def update_effectiveness(self, feedback):
        """Update intervention effectiveness metrics"""
        self.user_profile['response_history'].append(feedback)
        self._update_success_patterns(feedback)
        self._adjust_intervention_params(feedback)
        
    def _update_success_patterns(self, feedback):
        """Update patterns of successful interventions"""
        if feedback.get('effectiveness', 0) > 0.7:
            context = self._get_context_signature()
            self.user_profile['success_patterns'][context] = {
                'intervention_type': feedback['type'],
                'timing': feedback['timing'],
                'intensity': feedback['intensity']
            }