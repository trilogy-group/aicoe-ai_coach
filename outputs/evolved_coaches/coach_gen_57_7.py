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
        """Analyzes current user state using multiple data points"""
        cognitive_load = self._calculate_cognitive_load(user_data)
        energy_level = self._assess_energy_level(user_data)
        focus_state = self._determine_focus_state(user_data)
        
        self.user_state.update({
            'cognitive_load': cognitive_load,
            'energy_level': energy_level,
            'focus_state': focus_state
        })
        
        return self.user_state

    def generate_personalized_intervention(self, user_context):
        """Creates highly personalized coaching intervention"""
        if not self._is_appropriate_time(user_context):
            return None

        user_state = self.assess_user_state(user_context)
        
        intervention = {
            'type': self._select_intervention_type(user_state),
            'content': self._generate_content(user_state),
            'timing': self._optimize_timing(user_state),
            'delivery_method': self._select_delivery_method(user_state)
        }

        return self._enhance_intervention(intervention, user_context)

    def _calculate_cognitive_load(self, user_data):
        """Estimates current cognitive load based on multiple factors"""
        base_load = user_data.get('task_complexity', 0.5)
        context_load = user_data.get('context_demands', 0.3)
        temporal_load = user_data.get('time_pressure', 0.2)
        
        return min(1.0, base_load + context_load + temporal_load)

    def _assess_energy_level(self, user_data):
        """Determines user energy level using biological and contextual markers"""
        time_of_day_factor = self._get_circadian_factor(user_data['timestamp'])
        activity_drain = user_data.get('recent_activity_intensity', 0.0)
        rest_quality = user_data.get('rest_quality', 1.0)
        
        return max(0.0, min(1.0, (time_of_day_factor * rest_quality) - activity_drain))

    def _determine_focus_state(self, user_data):
        """Analyzes current focus state and flow potential"""
        if self.user_state['cognitive_load'] > 0.8:
            return 'overloaded'
        elif 0.3 <= self.user_state['cognitive_load'] <= 0.7:
            return 'optimal'
        else:
            return 'underutilized'

    def _select_intervention_type(self, user_state):
        """Chooses most appropriate intervention based on user state"""
        if user_state['cognitive_load'] > 0.7:
            return 'micro_break'
        elif user_state['energy_level'] < 0.3:
            return 'reflection'
        elif user_state['focus_state'] == 'optimal':
            return 'deep_work'
        else:
            return 'skill_building'

    def _generate_content(self, user_state):
        """Creates specific, actionable content for intervention"""
        intervention_type = self._select_intervention_type(user_state)
        
        content_templates = {
            'micro_break': "Take a 2-minute break to stretch and breathe deeply",
            'deep_work': "Block out the next 45 minutes for focused work on {task}",
            'reflection': "Reflect on your top 3 priorities for the next hour",
            'skill_building': "Practice {skill} for 15 minutes using {technique}"
        }
        
        return self._personalize_content(content_templates[intervention_type], user_state)

    def _optimize_timing(self, user_state):
        """Determines optimal timing for intervention delivery"""
        if user_state['cognitive_load'] > 0.8:
            return 'immediate'
        elif user_state['focus_state'] == 'optimal':
            return 'next_break'
        else:
            return 'within_30_mins'

    def _select_delivery_method(self, user_state):
        """Chooses appropriate delivery method based on user state"""
        if user_state['cognitive_load'] > 0.7:
            return 'minimal_visual'
        elif user_state['focus_state'] == 'optimal':
            return 'non_intrusive'
        else:
            return 'interactive'

    def _enhance_intervention(self, intervention, user_context):
        """Adds psychological sophistication to intervention"""
        personality_type = user_context.get('personality_type', 'INTJ')
        config = self.personality_type_configs[personality_type]
        
        intervention.update({
            'learning_style': config['learning_style'],
            'communication_style': config['communication_pref'],
            'work_pattern_alignment': config['work_pattern']
        })
        
        return intervention

    def _is_appropriate_time(self, user_context):
        """Checks if current time is appropriate for intervention"""
        return (user_context.get('available', True) and 
                not user_context.get('in_meeting', False) and
                self.user_state['receptivity'] > 0.4)

    def _get_circadian_factor(self, timestamp):
        """Calculates circadian rhythm factor for energy estimation"""
        hour = timestamp.hour
        if 9 <= hour <= 11:
            return 1.0
        elif 14 <= hour <= 16:
            return 0.8
        elif 4 <= hour <= 6:
            return 0.4
        else:
            return 0.6

    def _personalize_content(self, template, user_state):
        """Personalizes content template based on user state"""
        # Add personalization logic here
        return template