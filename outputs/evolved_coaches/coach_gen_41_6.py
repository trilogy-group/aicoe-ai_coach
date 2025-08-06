class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.behavioral_patterns = {}
        self.intervention_history = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'cognitive_load': 0.0,
            'attention_span': 1.0,
            'motivation_level': 0.5,
            'stress_level': 0.0,
            'flow_state': False,
            'learning_style': None,
            'peak_performance_times': [],
            'intervention_responsiveness': {}
        }
        
        self.behavioral_patterns[user_id] = {
            'daily_routines': {},
            'productivity_cycles': [],
            'break_patterns': [],
            'task_completion_rates': {}
        }
        
        self.intervention_history[user_id] = []
        
    def assess_cognitive_state(self, user_id, context_data):
        """Analyze current cognitive state based on context"""
        profile = self.user_profiles[user_id]
        
        # Update cognitive load based on task complexity and time
        profile['cognitive_load'] = self._calculate_cognitive_load(context_data)
        
        # Check for flow state
        profile['flow_state'] = self._detect_flow_state(context_data)
        
        # Update stress and attention metrics
        profile['stress_level'] = self._assess_stress_indicators(context_data)
        profile['attention_span'] = self._calculate_attention_capacity(context_data)
        
        return profile

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        profile = self.user_profiles[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        if profile['flow_state']:
            return self._create_minimal_intervention()
            
        intervention_type = self._select_intervention_type(profile, patterns)
        timing = self._optimize_intervention_timing(profile, patterns)
        content = self._generate_intervention_content(intervention_type, profile)
        
        intervention = {
            'type': intervention_type,
            'timing': timing,
            'content': content,
            'intensity': self._calculate_intensity(profile),
            'actionable_steps': self._generate_action_steps(profile, context)
        }
        
        self.intervention_history[user_id].append(intervention)
        return intervention

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on intervention outcomes"""
        profile = self.user_profiles[user_id]
        patterns = self.behavioral_patterns[user_id]
        
        # Update intervention responsiveness
        effectiveness = self._calculate_intervention_effectiveness(interaction_data)
        intervention_type = interaction_data['intervention_type']
        profile['intervention_responsiveness'][intervention_type] = effectiveness
        
        # Update behavioral patterns
        self._update_behavioral_patterns(patterns, interaction_data)
        
        # Adjust motivation modeling
        profile['motivation_level'] = self._recalculate_motivation(interaction_data)
        
        # Update learning style if needed
        if interaction_data.get('learning_indicators'):
            profile['learning_style'] = self._analyze_learning_style(interaction_data)

    def _calculate_cognitive_load(self, context_data):
        """Estimate current cognitive load"""
        base_load = context_data.get('task_complexity', 0.5)
        time_factor = self._get_time_pressure_factor(context_data)
        context_factor = self._analyze_environment_load(context_data)
        return min(1.0, base_load * time_factor * context_factor)

    def _detect_flow_state(self, context_data):
        """Determine if user is in flow state"""
        engagement = context_data.get('engagement_metrics', 0.0)
        focus_duration = context_data.get('focus_duration', 0.0)
        productivity = context_data.get('productivity_rate', 0.0)
        
        return (engagement > 0.8 and 
                focus_duration > 25 and 
                productivity > 0.7)

    def _select_intervention_type(self, profile, patterns):
        """Choose most effective intervention type"""
        if profile['cognitive_load'] > 0.8:
            return 'stress_reduction'
        elif profile['motivation_level'] < 0.3:
            return 'motivation_boost'
        elif profile['attention_span'] < 0.4:
            return 'focus_enhancement'
        return 'productivity_optimization'

    def _generate_action_steps(self, profile, context):
        """Create specific actionable recommendations"""
        intervention_type = self._select_intervention_type(profile, {})
        
        action_steps = {
            'stress_reduction': [
                'Take a 5-minute breathing break',
                'Stand up and stretch',
                'Review and prioritize your task list'
            ],
            'motivation_boost': [
                'Break current task into smaller chunks',
                'Set a 25-minute focused work period',
                'Identify and note your next milestone'
            ],
            'focus_enhancement': [
                'Clear workspace of distractions',
                'Enable do-not-disturb mode',
                'Set a clear goal for next 30 minutes'
            ],
            'productivity_optimization': [
                'Review and update task priorities',
                'Schedule your next break',
                'Identify potential blockers'
            ]
        }
        
        return action_steps[intervention_type]

    def _calculate_intensity(self, profile):
        """Determine appropriate intervention intensity"""
        base_intensity = 0.5
        if profile['stress_level'] > 0.7:
            base_intensity *= 0.6
        if profile['motivation_level'] < 0.3:
            base_intensity *= 1.3
        return min(1.0, base_intensity)

    def _optimize_intervention_timing(self, profile, patterns):
        """Calculate optimal intervention timing"""
        current_load = profile['cognitive_load']
        time_since_last = self._get_time_since_last_intervention()
        
        if current_load > 0.8 or profile['flow_state']:
            return 'defer'
        elif time_since_last < 30:
            return 'wait'
        return 'immediate'

    def get_performance_metrics(self, user_id):
        """Return key performance indicators"""
        return {
            'intervention_effectiveness': self._calculate_effectiveness_metrics(user_id),
            'behavioral_changes': self._analyze_behavior_changes(user_id),
            'user_satisfaction': self._calculate_satisfaction_metrics(user_id),
            'engagement_rate': self._calculate_engagement_rate(user_id)
        }