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
            'energy_level': 1.0,
            'focus_state': 'optimal',
            'stress_level': 0.0,
            'receptivity': 1.0
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'time_based': {},
            'context_based': {},
            'state_based': {}
        }

        # Intervention strategies
        self.intervention_types = {
            'micro_break': {'duration': 2, 'intensity': 0.2},
            'deep_work': {'duration': 45, 'intensity': 0.8},
            'reflection': {'duration': 5, 'intensity': 0.4},
            'skill_building': {'duration': 15, 'intensity': 0.6}
        }

    def assess_user_state(self, user_data):
        """
        Analyzes user's current cognitive and emotional state
        """
        cognitive_load = self._calculate_cognitive_load(user_data)
        energy_level = self._assess_energy_level(user_data)
        focus_state = self._determine_focus_state(user_data)
        stress_level = self._measure_stress_indicators(user_data)
        
        self.user_state.update({
            'cognitive_load': cognitive_load,
            'energy_level': energy_level,
            'focus_state': focus_state,
            'stress_level': stress_level
        })
        
        return self.user_state

    def generate_personalized_intervention(self, user_context):
        """
        Creates targeted coaching intervention based on user state and context
        """
        if not self._is_appropriate_timing(user_context):
            return None

        intervention = {
            'type': self._select_intervention_type(),
            'content': self._generate_content(),
            'timing': self._optimize_timing(),
            'delivery_method': self._select_delivery_method(),
            'intensity': self._calibrate_intensity()
        }

        return self._format_intervention(intervention)

    def _calculate_cognitive_load(self, user_data):
        """
        Estimates current cognitive load based on work patterns and indicators
        """
        task_complexity = user_data.get('task_complexity', 0.5)
        context_switches = user_data.get('context_switches', 0)
        time_pressure = user_data.get('time_pressure', 0.5)
        
        cognitive_load = (task_complexity * 0.4 + 
                         min(context_switches * 0.1, 0.4) +
                         time_pressure * 0.2)
        
        return min(cognitive_load, 1.0)

    def _assess_energy_level(self, user_data):
        """
        Determines user's current energy and fatigue levels
        """
        time_active = user_data.get('time_active', 0)
        break_frequency = user_data.get('break_frequency', 0)
        activity_intensity = user_data.get('activity_intensity', 0.5)
        
        energy_level = 1.0 - (time_active * 0.1) + (break_frequency * 0.2)
        return max(min(energy_level, 1.0), 0.0)

    def _determine_focus_state(self, user_data):
        """
        Analyzes current focus and flow state
        """
        productivity_markers = user_data.get('productivity_markers', [])
        distraction_count = user_data.get('distraction_count', 0)
        work_continuity = user_data.get('work_continuity', 0.5)

        if work_continuity > 0.8 and distraction_count < 2:
            return 'flow'
        elif work_continuity > 0.5:
            return 'focused'
        else:
            return 'distracted'

    def _is_appropriate_timing(self, user_context):
        """
        Determines if intervention timing is optimal
        """
        if self.user_state['focus_state'] == 'flow':
            return False
            
        if self.user_state['cognitive_load'] > 0.8:
            return False
            
        return True

    def _select_intervention_type(self):
        """
        Chooses most appropriate intervention based on user state
        """
        if self.user_state['energy_level'] < 0.3:
            return 'micro_break'
        elif self.user_state['focus_state'] == 'distracted':
            return 'deep_work'
        elif self.user_state['stress_level'] > 0.7:
            return 'reflection'
        else:
            return 'skill_building'

    def _generate_content(self):
        """
        Creates personalized coaching content
        """
        selected_type = self._select_intervention_type()
        
        content_templates = {
            'micro_break': "Take a 2-minute break to stretch and reset",
            'deep_work': "Let's focus on {task} for the next 45 minutes",
            'reflection': "Reflect on your main accomplishment today",
            'skill_building': "Practice {skill} for 15 minutes"
        }
        
        return content_templates[selected_type]

    def _optimize_timing(self):
        """
        Optimizes intervention timing based on user patterns
        """
        return {
            'delay': self._calculate_optimal_delay(),
            'duration': self.intervention_types[self._select_intervention_type()]['duration'],
            'frequency': self._calculate_frequency()
        }

    def _select_delivery_method(self):
        """
        Selects optimal delivery method based on user preferences and context
        """
        if self.user_state['cognitive_load'] > 0.7:
            return 'minimal_visual'
        elif self.user_state['focus_state'] == 'distracted':
            return 'prominent_notification'
        else:
            return 'standard_notification'

    def _calibrate_intensity(self):
        """
        Calibrates intervention intensity based on user state
        """
        base_intensity = self.intervention_types[self._select_intervention_type()]['intensity']
        
        modifiers = {
            'cognitive_load': -0.2 if self.user_state['cognitive_load'] > 0.6 else 0,
            'stress_level': -0.3 if self.user_state['stress_level'] > 0.7 else 0,
            'receptivity': 0.2 if self.user_state['receptivity'] > 0.8 else 0
        }
        
        return max(min(base_intensity + sum(modifiers.values()), 1.0), 0.1)

    def _format_intervention(self, intervention):
        """
        Formats intervention for delivery
        """
        return {
            'type': intervention['type'],
            'content': intervention['content'],
            'timing': intervention['timing'],
            'delivery_method': intervention['delivery_method'],
            'intensity': intervention['intensity'],
            'metadata': {
                'user_state': self.user_state,
                'timestamp': self._get_timestamp()
            }
        }