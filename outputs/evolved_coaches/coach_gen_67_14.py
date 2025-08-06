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
        self.behavior_triggers = {
            'habit_formation': [],
            'motivation_patterns': {},
            'resistance_points': [],
            'success_markers': []
        }

        # Context awareness system
        self.context_tracker = {
            'time_patterns': {},
            'location_context': {},
            'activity_state': '',
            'social_context': '',
            'device_state': {}
        }

    def assess_user_state(self, user_data):
        """Evaluate current user cognitive and emotional state"""
        cognitive_load = self._calculate_cognitive_load(user_data)
        energy_level = self._assess_energy_level(user_data)
        focus_state = self._determine_focus_state(user_data)
        
        self.user_state.update({
            'cognitive_load': cognitive_load,
            'energy_level': energy_level,
            'focus_state': focus_state
        })
        
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
            'intensity': self._calculate_intensity()
        }

    def _calculate_cognitive_load(self, data):
        """Assess current cognitive load based on multiple factors"""
        task_complexity = data.get('task_complexity', 0.5)
        context_switches = data.get('context_switches', 0)
        time_pressure = data.get('time_pressure', 0.5)
        
        return (task_complexity + (context_switches * 0.1) + time_pressure) / 3

    def _assess_energy_level(self, data):
        """Determine user energy level"""
        time_active = data.get('time_active', 0)
        break_frequency = data.get('break_frequency', 0)
        activity_intensity = data.get('activity_intensity', 0.5)
        
        return max(0, 1 - (time_active * 0.1) + (break_frequency * 0.2))

    def _determine_focus_state(self, data):
        """Analyze user focus state"""
        distraction_level = data.get('distractions', 0)
        flow_indicators = data.get('flow_indicators', [])
        recent_progress = data.get('progress_markers', 0)
        
        if len(flow_indicators) > 2 and distraction_level < 0.3:
            return 'flow'
        elif recent_progress > 0.7:
            return 'productive'
        else:
            return 'normal'

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        if self.user_state['cognitive_load'] > 0.8:
            return False
            
        time_since_last = context.get('time_since_last_intervention', 0)
        if time_since_last < self.intervention_settings['min_time_between']:
            return False
            
        return self.user_state['receptivity'] > 0.6

    def _select_intervention_type(self):
        """Choose appropriate intervention type"""
        if self.user_state['energy_level'] < 0.3:
            return 'energy_management'
        elif self.user_state['stress_level'] > 0.7:
            return 'stress_reduction'
        elif self.user_state['focus_state'] == 'flow':
            return 'flow_protection'
        else:
            return 'productivity_enhancement'

    def _generate_content(self, intervention_type):
        """Create specific intervention content"""
        base_templates = {
            'energy_management': "Take a 5 minute break and stretch.",
            'stress_reduction': "Practice 2 minutes of deep breathing.",
            'flow_protection': "Maintain current focus for 25 more minutes.",
            'productivity_enhancement': "Break this task into smaller steps."
        }
        
        content = base_templates[intervention_type]
        return self._personalize_content(content)

    def _personalize_content(self, content):
        """Customize content for user"""
        personality = self.personality_type_configs.get(self.user_state.get('personality_type', 'INTJ'))
        
        if personality['communication_pref'] == 'direct':
            return content
        elif personality['communication_pref'] == 'enthusiastic':
            return f"Great opportunity! {content}"
        
        return content

    def _optimize_timing(self, context):
        """Determine optimal intervention timing"""
        current_time = context.get('time', 0)
        schedule = context.get('schedule', [])
        
        # Find next available time slot
        next_slot = self._find_next_available(current_time, schedule)
        
        return next_slot

    def _calculate_intensity(self):
        """Determine intervention intensity"""
        base_intensity = self.intervention_settings['intensity_factor']
        receptivity = self.user_state['receptivity']
        
        return min(1.0, base_intensity * receptivity)

    def update_effectiveness(self, feedback):
        """Update system based on intervention effectiveness"""
        if feedback.get('was_helpful', False):
            self.intervention_settings['intensity_factor'] *= 1.1
        else:
            self.intervention_settings['intensity_factor'] *= 0.9
            
        self.intervention_settings['intensity_factor'] = min(1.0, 
            max(0.1, self.intervention_settings['intensity_factor']))