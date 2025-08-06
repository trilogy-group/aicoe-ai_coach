class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'preferences': {},
            'learning_style': None,
            'motivation_factors': [],
            'cognitive_load': 0.0,
            'engagement_patterns': {},
            'success_metrics': {}
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'daily_rhythms': {},
            'response_rates': {},
            'completion_patterns': {}
        }
        
    def assess_cognitive_state(self, user_id, context_data):
        """Evaluate user's current cognitive capacity and state"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        attention_level = self._estimate_attention(context_data)
        stress_level = self._analyze_stress_indicators(context_data)
        
        return {
            'cognitive_load': cognitive_load,
            'attention': attention_level,
            'stress': stress_level,
            'receptivity': self._calculate_receptivity(cognitive_load, stress_level)
        }

    def generate_personalized_intervention(self, user_id, context):
        """Create tailored coaching intervention based on user state and context"""
        user_state = self.assess_cognitive_state(user_id, context)
        
        if not self._is_appropriate_timing(user_id, context):
            return None
            
        intervention_type = self._select_intervention_type(user_state)
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(user_id, intervention_type),
            'intensity': self._calculate_intensity(user_state),
            'timing': self._optimize_timing(user_id, context),
            'action_steps': self._generate_action_steps(intervention_type),
            'follow_up': self._plan_follow_up(user_id)
        }
        
        return self._format_intervention(intervention)

    def track_intervention_outcome(self, user_id, intervention_id, outcome_data):
        """Record and analyze intervention effectiveness"""
        self.intervention_history[user_id].append({
            'intervention_id': intervention_id,
            'outcome': outcome_data,
            'context': self._capture_context(),
            'user_state': self.assess_cognitive_state(user_id, outcome_data)
        })
        
        self._update_user_model(user_id, outcome_data)
        self._optimize_strategies(user_id)

    def _calculate_cognitive_load(self, context):
        """Estimate current cognitive load based on context signals"""
        task_complexity = self._assess_task_complexity(context)
        environmental_load = self._assess_environment(context)
        temporal_pressure = self._assess_time_pressure(context)
        
        return (task_complexity + environmental_load + temporal_pressure) / 3.0

    def _estimate_attention(self, context):
        """Estimate user's current attention capacity"""
        focus_signals = self._analyze_focus_signals(context)
        distraction_level = self._assess_distractions(context)
        time_on_task = context.get('time_on_task', 0)
        
        return self._calculate_attention_score(focus_signals, distraction_level, time_on_task)

    def _select_intervention_type(self, user_state):
        """Choose most appropriate intervention based on user state"""
        if user_state['cognitive_load'] > 0.8:
            return 'micro_break'
        elif user_state['stress'] > 0.7:
            return 'stress_reduction'
        elif user_state['attention'] < 0.4:
            return 'focus_enhancement'
        else:
            return 'progress_check'

    def _generate_action_steps(self, intervention_type):
        """Create specific, actionable steps based on intervention type"""
        action_templates = {
            'micro_break': [
                'Take 3 deep breaths',
                'Stand and stretch for 1 minute',
                'Look at something 20 feet away for 20 seconds'
            ],
            'stress_reduction': [
                'Complete 2-minute mindfulness exercise',
                'List top 3 priorities for next hour',
                'Take a 5-minute walking break'
            ],
            'focus_enhancement': [
                'Clear desk of non-essential items',
                'Set timer for 25-minute focused work',
                'Turn off notifications temporarily'
            ]
        }
        
        return action_templates.get(intervention_type, [])

    def _optimize_timing(self, user_id, context):
        """Determine optimal intervention timing"""
        user_patterns = self.behavioral_patterns[user_id]
        current_load = self._calculate_cognitive_load(context)
        time_since_last = self._time_since_last_intervention(user_id)
        
        return self._calculate_optimal_timing(user_patterns, current_load, time_since_last)

    def _update_user_model(self, user_id, outcome_data):
        """Update user model based on intervention outcomes"""
        success_rate = outcome_data.get('success_rate', 0)
        engagement_level = outcome_data.get('engagement', 0)
        
        self.user_profiles[user_id]['success_metrics'] = {
            'success_rate': success_rate,
            'engagement': engagement_level,
            'trend': self._calculate_improvement_trend(user_id)
        }
        
        self._adapt_strategies(user_id, outcome_data)

    def _format_intervention(self, intervention):
        """Format intervention for delivery"""
        return {
            'title': self._generate_title(intervention['type']),
            'message': self._generate_message(intervention),
            'actions': intervention['action_steps'],
            'timing': intervention['timing'],
            'intensity': intervention['intensity'],
            'follow_up': intervention['follow_up']
        }