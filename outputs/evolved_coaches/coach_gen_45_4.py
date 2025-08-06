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

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {
                'duration': 2,
                'frequency': 45,
                'cognitive_load_threshold': 0.7
            },
            'deep_work': {
                'duration': 25,
                'frequency': 90,
                'energy_threshold': 0.6
            },
            'reflection': {
                'duration': 5,
                'frequency': 120,
                'stress_threshold': 0.8
            }
        }

    def assess_user_state(self, user_data):
        """
        Analyzes user's current cognitive and emotional state
        """
        current_state = {
            'cognitive_load': self._calculate_cognitive_load(user_data),
            'energy_level': self._assess_energy(user_data),
            'focus_state': self._determine_focus_state(user_data),
            'stress_level': self._measure_stress(user_data),
            'receptivity': self._calculate_receptivity(user_data)
        }
        self.user_state.update(current_state)
        return current_state

    def generate_intervention(self, user_context):
        """
        Creates personalized coaching intervention based on user state and context
        """
        if not self._is_appropriate_timing(user_context):
            return None

        intervention_type = self._select_intervention_type()
        
        return {
            'type': intervention_type,
            'content': self._generate_content(intervention_type),
            'timing': self._optimize_timing(user_context),
            'delivery_method': self._select_delivery_method(),
            'intensity': self._calculate_intensity()
        }

    def _calculate_cognitive_load(self, user_data):
        """
        Estimates current cognitive load based on work patterns and signals
        """
        base_load = user_data.get('task_complexity', 0.5)
        time_pressure = user_data.get('deadline_proximity', 0.3)
        context_switches = user_data.get('context_switches', 0.2)
        
        return min(1.0, base_load + time_pressure + context_switches)

    def _assess_energy(self, user_data):
        """
        Evaluates user's current energy level
        """
        time_active = user_data.get('time_active', 0)
        break_frequency = user_data.get('breaks_taken', 0)
        work_intensity = user_data.get('work_intensity', 0.5)
        
        energy = 1.0 - (time_active * 0.1) + (break_frequency * 0.2)
        return max(0.0, min(1.0, energy))

    def _determine_focus_state(self, user_data):
        """
        Analyzes current focus level and flow state
        """
        productivity = user_data.get('productivity_signals', 0.5)
        distractions = user_data.get('distraction_count', 0)
        deep_work_time = user_data.get('focus_duration', 0)

        if productivity > 0.8 and distractions < 2 and deep_work_time > 20:
            return 'flow'
        elif productivity > 0.6:
            return 'focused'
        else:
            return 'distracted'

    def _is_appropriate_timing(self, user_context):
        """
        Determines if intervention timing is appropriate
        """
        if user_context.get('in_meeting', False):
            return False
        if self.user_state['focus_state'] == 'flow':
            return False
        if self.user_state['cognitive_load'] > 0.9:
            return False
        return True

    def _select_intervention_type(self):
        """
        Chooses most appropriate intervention based on user state
        """
        if self.user_state['cognitive_load'] > 0.7:
            return 'micro_break'
        elif self.user_state['energy_level'] < 0.4:
            return 'deep_work'
        elif self.user_state['stress_level'] > 0.7:
            return 'reflection'
        return 'standard'

    def _generate_content(self, intervention_type):
        """
        Creates specific, actionable content for the intervention
        """
        content_templates = {
            'micro_break': "Take a 2-minute break to stretch and breathe deeply",
            'deep_work': "Block the next 25 minutes for focused work on {task}",
            'reflection': "Reflect on your top accomplishment today and plan your next step",
            'standard': "Review your current task priority and adjust if needed"
        }
        return content_templates.get(intervention_type, "")

    def _optimize_timing(self, user_context):
        """
        Optimizes intervention timing based on user context
        """
        current_time = user_context.get('timestamp')
        next_meeting = user_context.get('next_meeting_time')
        
        if next_meeting and (next_meeting - current_time).minutes < 15:
            return current_time + timedelta(minutes=1)
        
        return current_time + timedelta(minutes=5)

    def _select_delivery_method(self):
        """
        Selects appropriate delivery method based on user state
        """
        if self.user_state['cognitive_load'] > 0.8:
            return 'minimal_visual'
        elif self.user_state['focus_state'] == 'distracted':
            return 'prominent_notification'
        return 'standard_notification'

    def _calculate_intensity(self):
        """
        Determines intervention intensity based on user receptivity
        """
        base_intensity = 0.5
        receptivity_factor = self.user_state['receptivity']
        stress_adjustment = 1 - self.user_state['stress_level']
        
        return base_intensity * receptivity_factor * stress_adjustment