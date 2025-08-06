class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }
        
        # Enhanced context tracking
        self.context_tracker = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'time_of_day': None,
            'work_context': None,
            'recent_interventions': []
        }
        
        # Behavioral psychology components
        self.behavioral_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'flow_state': {'current': False, 'duration': 0},
            'burnout_risk': 0.0
        }
        
        # User profile and personalization
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preferences': {},
            'goals': []
        }

    def assess_context(self, user_state, environment):
        """Evaluate current user context and environment"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._assess_energy_level(user_state),
            'time_of_day': environment.get('time'),
            'work_context': environment.get('context')
        })
        return self.context_tracker

    def generate_intervention(self, user_state):
        """Create personalized coaching intervention"""
        if self._check_flow_state():
            return self._protect_flow_state()
            
        context = self.assess_context(user_state, user_state.get('environment'))
        
        if self._should_intervene(context):
            intervention = {
                'type': self._select_intervention_type(context),
                'content': self._generate_content(context),
                'timing': self._optimize_timing(context),
                'delivery_style': self._personalize_delivery()
            }
            
            self._track_intervention(intervention)
            return intervention
        return None

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'time_pressure': user_state.get('time_pressure', 0.4)
        }
        return sum(factors.values()) / len(factors)

    def _assess_energy_level(self, user_state):
        """Calculate user energy level"""
        factors = {
            'time_since_break': user_state.get('time_since_break', 0),
            'task_duration': user_state.get('continuous_work_time', 0),
            'daily_activity': user_state.get('activity_level', 0.5)
        }
        return max(0, 1 - (sum(factors.values()) / len(factors)))

    def _check_flow_state(self):
        """Detect if user is in flow state"""
        return self.behavioral_models['flow_state']['current']

    def _protect_flow_state(self):
        """Minimize interruptions during flow state"""
        return {'type': 'flow_protection', 'action': 'defer_interruptions'}

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        return (
            context['cognitive_load'] < 0.8 and
            context['energy_level'] > 0.3 and
            self._check_intervention_timing()
        )

    def _select_intervention_type(self, context):
        """Choose most appropriate intervention type"""
        options = ['nudge', 'suggestion', 'reminder', 'break_prompt']
        weights = self._calculate_intervention_weights(context)
        return max(options, key=lambda x: weights[x])

    def _generate_content(self, context):
        """Create personalized intervention content"""
        template = self._select_content_template(context)
        return self._personalize_content(template, self.user_profile)

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        return {
            'immediate': context['cognitive_load'] < 0.5,
            'defer_minutes': self._calculate_defer_time(context),
            'optimal_window': self._find_optimal_window()
        }

    def _personalize_delivery(self):
        """Customize delivery based on user preferences"""
        style = self.personality_type_configs.get(
            self.user_profile['personality_type'],
            {'communication_pref': 'neutral'}
        )
        return style['communication_pref']

    def _track_intervention(self, intervention):
        """Record intervention for analysis"""
        self.context_tracker['recent_interventions'].append({
            'timestamp': self._get_timestamp(),
            'intervention': intervention,
            'context': self.context_tracker.copy()
        })

    def update_user_profile(self, feedback):
        """Update user profile based on intervention feedback"""
        self.user_profile['response_history'].append(feedback)
        self._update_effectiveness_metrics(feedback)
        self._adjust_personalization(feedback)

    def _update_effectiveness_metrics(self, feedback):
        """Update intervention effectiveness tracking"""
        metrics = self.user_profile['effectiveness_metrics']
        metrics['response_rate'] = self._calculate_response_rate()
        metrics['behavior_change'] = self._assess_behavior_change()
        metrics['satisfaction'] = self._calculate_satisfaction()

    def _adjust_personalization(self, feedback):
        """Refine personalization based on feedback"""
        self.user_profile['preferences'] = self._update_preferences(feedback)
        self.behavioral_models = self._update_behavioral_models(feedback)