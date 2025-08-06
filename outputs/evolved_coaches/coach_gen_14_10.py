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

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context and environment"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._assess_energy_level(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('context')
        })
        return self.context_tracker

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if self._should_intervene(context):
            intervention_type = self._select_intervention_type(context, user_profile)
            content = self._personalize_content(intervention_type, user_profile)
            timing = self._optimize_timing(context)
            
            return {
                'type': intervention_type,
                'content': content,
                'timing': timing,
                'action_steps': self._generate_action_steps(content)
            }
        return None

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'interruption_frequency': user_state.get('interruptions', 0),
            'focus_duration': user_state.get('focus_time', 0)
        }
        return sum(factors.values()) / len(factors)

    def _assess_energy_level(self, user_state):
        """Calculate user energy level"""
        return user_state.get('energy_level', 0.5)

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        if context['cognitive_load'] > 0.8:
            return False
        if any(i['time'] > (time.time() - 1800) for i in self.context_tracker['recent_interventions']):
            return False
        return True

    def _select_intervention_type(self, context, user_profile):
        """Choose most appropriate intervention type"""
        personality = self.personality_type_configs.get(user_profile['personality_type'])
        if context['cognitive_load'] > 0.6:
            return 'micro_intervention'
        if context['energy_level'] < 0.3:
            return 'energy_boost'
        return 'standard_coaching'

    def _personalize_content(self, intervention_type, user_profile):
        """Generate personalized intervention content"""
        personality = self.personality_type_configs[user_profile['personality_type']]
        learning_style = personality['learning_style']
        communication_pref = personality['communication_pref']
        
        content_templates = {
            'micro_intervention': self._get_micro_templates(),
            'energy_boost': self._get_energy_templates(),
            'standard_coaching': self._get_standard_templates()
        }
        
        template = self._select_template(content_templates[intervention_type], learning_style)
        return self._adapt_communication(template, communication_pref)

    def _optimize_timing(self, context):
        """Determine optimal intervention timing"""
        if context['flow_state']['current']:
            return 'defer'
        if context['cognitive_load'] > 0.7:
            return 'wait_for_break'
        return 'immediate'

    def _generate_action_steps(self, content):
        """Create specific, actionable steps"""
        return [
            {'step': 1, 'action': 'Specific action 1', 'timeframe': '5 min'},
            {'step': 2, 'action': 'Specific action 2', 'timeframe': '10 min'},
            {'step': 3, 'action': 'Specific action 3', 'timeframe': '15 min'}
        ]

    def update_effectiveness(self, intervention_id, user_feedback):
        """Track and update intervention effectiveness"""
        self.user_profile['effectiveness_metrics'][intervention_id] = user_feedback
        self._adjust_strategies(user_feedback)

    def _adjust_strategies(self, feedback):
        """Adapt coaching strategies based on feedback"""
        if feedback['satisfaction'] < 0.5:
            self._recalibrate_personalization()
        if feedback['actionability'] < 0.5:
            self._enhance_action_steps()

    def get_performance_metrics(self):
        """Return current performance metrics"""
        return {
            'nudge_quality': self._calculate_nudge_quality(),
            'behavioral_change': self._measure_behavior_change(),
            'user_satisfaction': self._get_satisfaction_score(),
            'relevance': self._calculate_relevance(),
            'actionability': self._measure_actionability()
        }