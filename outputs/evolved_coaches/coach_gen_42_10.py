class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced cognitive state tracking
        self.cognitive_state = {
            'attention_level': 0.0,
            'energy_level': 0.0,
            'stress_level': 0.0,
            'flow_state': False,
            'cognitive_load': 0.0
        }

        # Behavioral psychology components
        self.behavioral_patterns = {
            'work_sessions': [],
            'break_patterns': [],
            'productivity_peaks': [],
            'distraction_triggers': []
        }

        # Intervention configuration
        self.intervention_settings = {
            'min_time_between': 30, # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'nudge_style': 'adaptive'
        }

    def analyze_user_context(self, user_data):
        """Analyzes current user context for optimal intervention"""
        context = {
            'time_of_day': user_data.get('timestamp'),
            'current_task': user_data.get('task'),
            'energy_level': self._estimate_energy_level(user_data),
            'focus_state': self._assess_focus_state(user_data),
            'workload': self._calculate_workload(user_data)
        }
        return self._evaluate_intervention_timing(context)

    def generate_personalized_nudge(self, user_profile, context):
        """Generates personalized coaching intervention"""
        if not self._should_intervene(context):
            return None

        intervention_type = self._select_intervention_type(user_profile, context)
        
        nudge = {
            'content': self._generate_content(intervention_type, user_profile),
            'timing': self._optimize_timing(context),
            'intensity': self._calibrate_intensity(user_profile),
            'delivery_method': self._select_delivery_method(user_profile)
        }

        return self._format_nudge(nudge)

    def update_user_model(self, user_id, interaction_data):
        """Updates user model based on interaction data"""
        self.behavioral_patterns['work_sessions'].append(interaction_data)
        self._update_cognitive_state(interaction_data)
        self._refine_intervention_params(interaction_data)

    def _estimate_energy_level(self, user_data):
        """Estimates user energy level based on activity patterns"""
        recent_activity = user_data.get('recent_activity', [])
        time_of_day = user_data.get('timestamp').hour
        
        base_energy = self._calculate_circadian_energy(time_of_day)
        activity_impact = sum(a.get('intensity', 0) for a in recent_activity) / len(recent_activity)
        
        return min(1.0, base_energy * (1 - activity_impact))

    def _assess_focus_state(self, user_data):
        """Assesses user's current focus state"""
        recent_switches = len(user_data.get('task_switches', []))
        active_duration = user_data.get('active_duration', 0)
        
        focus_score = 1.0
        if recent_switches > 3:
            focus_score *= 0.7
        if active_duration > 90:
            focus_score *= 0.8
            
        return focus_score

    def _calculate_workload(self, user_data):
        """Calculates current cognitive workload"""
        task_complexity = user_data.get('task_complexity', 0.5)
        context_switches = len(user_data.get('context_switches', []))
        pending_tasks = len(user_data.get('pending_tasks', []))
        
        workload = (task_complexity + (context_switches * 0.1) + (pending_tasks * 0.05))
        return min(1.0, workload)

    def _select_intervention_type(self, user_profile, context):
        """Selects appropriate intervention type based on context"""
        if context['focus_state'] > 0.8:
            return 'flow_protection'
        elif context['workload'] > 0.7:
            return 'workload_management'
        elif context['energy_level'] < 0.3:
            return 'energy_boost'
        else:
            return 'general_productivity'

    def _generate_content(self, intervention_type, user_profile):
        """Generates specific intervention content"""
        content_templates = {
            'flow_protection': "Maintaining your excellent focus. Consider setting a timer for {duration} minutes.",
            'workload_management': "High workload detected. Let's break this down into smaller tasks.",
            'energy_boost': "Energy levels are low. A 5-minute movement break could help.",
            'general_productivity': "Good time to review your priorities for the next hour."
        }
        
        return content_templates[intervention_type].format(
            duration=self._calculate_optimal_duration(user_profile)
        )

    def _optimize_timing(self, context):
        """Optimizes intervention timing"""
        if context['focus_state'] > 0.8:
            return 'defer'
        elif context['workload'] > 0.9:
            return 'urgent'
        else:
            return 'normal'

    def _calibrate_intensity(self, user_profile):
        """Calibrates intervention intensity"""
        base_intensity = self.intervention_settings['intensity_level']
        personality_modifier = self._get_personality_modifier(user_profile)
        return base_intensity * personality_modifier

    def _format_nudge(self, nudge):
        """Formats final nudge for delivery"""
        return {
            'message': nudge['content'],
            'timing': nudge['timing'],
            'intensity': nudge['intensity'],
            'delivery': nudge['delivery_method'],
            'timestamp': self._get_timestamp()
        }

    def _should_intervene(self, context):
        """Determines if intervention is appropriate"""
        return (
            context['focus_state'] < 0.9 and
            context['workload'] < 0.95 and
            self._check_intervention_spacing()
        )

    def _update_cognitive_state(self, interaction_data):
        """Updates cognitive state tracking"""
        self.cognitive_state['attention_level'] = interaction_data.get('attention', self.cognitive_state['attention_level'])
        self.cognitive_state['energy_level'] = interaction_data.get('energy', self.cognitive_state['energy_level'])
        self.cognitive_state['stress_level'] = interaction_data.get('stress', self.cognitive_state['stress_level'])
        self.cognitive_state['flow_state'] = interaction_data.get('flow', self.cognitive_state['flow_state'])