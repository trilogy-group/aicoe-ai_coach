class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced cognitive and behavioral tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_state': 'optimal',
            'stress_level': 0.0,
            'receptivity': 1.0
        }

        # Intervention configuration
        self.intervention_settings = {
            'min_time_between': 30, # minutes
            'max_daily': 8,
            'intensity_factor': 0.7
        }

        # Behavioral psychology components
        self.behavior_drivers = {
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

    def assess_user_state(self, context_data):
        """Evaluate current user cognitive and emotional state"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        energy_level = self._assess_energy(context_data)
        focus_state = self._determine_focus_state(context_data)
        stress_level = self._evaluate_stress(context_data)
        receptivity = self._calculate_receptivity(cognitive_load, energy_level, stress_level)

        self.user_state.update({
            'cognitive_load': cognitive_load,
            'energy_level': energy_level,
            'focus_state': focus_state,
            'stress_level': stress_level,
            'receptivity': receptivity
        })

        return self.user_state

    def generate_intervention(self, user_profile, context):
        """Create personalized coaching intervention"""
        if not self._should_intervene():
            return None

        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        intervention = {
            'type': self._select_intervention_type(context),
            'content': self._generate_content(personality_config, context),
            'timing': self._optimize_timing(context),
            'intensity': self._calculate_intensity(),
            'action_steps': self._create_action_steps(context)
        }

        return self._personalize_intervention(intervention, user_profile)

    def _calculate_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        base_load = context.get('task_complexity', 0.5)
        environmental_load = context.get('distractions', 0.0)
        temporal_load = context.get('time_pressure', 0.0)
        
        return min(1.0, base_load + environmental_load + temporal_load)

    def _assess_energy(self, context):
        """Evaluate user energy levels"""
        time_of_day = context.get('time_of_day', 12)
        recent_breaks = context.get('breaks_taken', 0)
        work_duration = context.get('continuous_work_time', 0)
        
        energy = 1.0 - (work_duration / 480) + (recent_breaks * 0.1)
        return max(0.0, min(1.0, energy))

    def _determine_focus_state(self, context):
        """Assess current focus state"""
        if self.user_state['cognitive_load'] < 0.3:
            return 'under_stimulated'
        elif self.user_state['cognitive_load'] > 0.8:
            return 'overwhelmed'
        return 'optimal'

    def _evaluate_stress(self, context):
        """Calculate current stress levels"""
        deadline_pressure = context.get('deadline_proximity', 0.0)
        task_difficulty = context.get('task_difficulty', 0.0)
        external_pressure = context.get('external_pressure', 0.0)
        
        return min(1.0, (deadline_pressure + task_difficulty + external_pressure) / 3)

    def _calculate_receptivity(self, cognitive_load, energy, stress):
        """Determine user receptivity to coaching"""
        return max(0.0, 1.0 - (cognitive_load + stress) * (1 - energy))

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (self.user_state['receptivity'] > 0.4 and 
                self.user_state['cognitive_load'] < 0.8)

    def _select_intervention_type(self, context):
        """Choose appropriate intervention type"""
        if self.user_state['focus_state'] == 'overwhelmed':
            return 'stress_reduction'
        elif self.user_state['energy_level'] < 0.3:
            return 'energy_management'
        return 'productivity_enhancement'

    def _generate_content(self, personality_config, context):
        """Create personalized intervention content"""
        communication_style = personality_config['communication_pref']
        learning_style = personality_config['learning_style']
        
        return {
            'message': self._craft_message(communication_style),
            'supporting_material': self._get_learning_resources(learning_style),
            'reinforcement': self._create_reinforcement_strategy(context)
        }

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        current_task = context.get('current_task', {})
        return {
            'delay': self._calculate_optimal_delay(current_task),
            'duration': self._determine_intervention_duration(),
            'frequency': self._calculate_frequency()
        }

    def _calculate_intensity(self):
        """Determine appropriate intervention intensity"""
        return min(1.0, self.intervention_settings['intensity_factor'] * 
                  self.user_state['receptivity'])

    def _create_action_steps(self, context):
        """Generate specific, actionable recommendations"""
        return {
            'immediate': self._generate_immediate_actions(context),
            'short_term': self._generate_short_term_actions(context),
            'long_term': self._generate_long_term_actions(context)
        }

    def _personalize_intervention(self, intervention, user_profile):
        """Apply final personalization to intervention"""
        intervention['style'] = user_profile.get('preferred_style', 'neutral')
        intervention['complexity'] = self._adjust_complexity(user_profile)
        intervention['format'] = user_profile.get('preferred_format', 'text')
        
        return intervention