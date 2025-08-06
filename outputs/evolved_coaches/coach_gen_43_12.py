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
            'focus_state': 'neutral',
            'time_of_day': None,
            'work_context': None,
            'interruption_cost': 0.0
        }

        # Behavioral psychology components
        self.behavior_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'self_efficacy': 0.0,
            'commitment': 0.0
        }

        # Personalization tracking
        self.user_profile = {
            'preferences': {},
            'response_history': [],
            'learning_patterns': {},
            'intervention_effectiveness': {},
            'peak_performance_times': [],
            'stress_indicators': {}
        }

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {'duration': 2, 'frequency': 'high', 'cognitive_load': 'low'},
            'deep_work': {'duration': 45, 'frequency': 'medium', 'cognitive_load': 'high'},
            'reflection': {'duration': 10, 'frequency': 'low', 'cognitive_load': 'medium'},
            'skill_building': {'duration': 20, 'frequency': 'medium', 'cognitive_load': 'high'}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        focus_state = self._detect_flow_state(user_state)
        interruption_cost = self._estimate_interruption_cost(focus_state, cognitive_load)

        self.context_tracker.update({
            'cognitive_load': cognitive_load,
            'focus_state': focus_state,
            'interruption_cost': interruption_cost,
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity')
        })

        return self.context_tracker

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        user_profile = self.user_profile
        current_context = self.assess_context(context['user_state'], context['environment'])

        # Select optimal intervention type
        intervention_type = self._select_intervention_type(current_context, user_profile)
        
        # Personalize content and delivery
        intervention = self._personalize_intervention(
            intervention_type,
            user_profile,
            current_context
        )

        # Add behavioral reinforcement
        intervention = self._add_behavioral_elements(intervention, user_profile)

        return intervention

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'time_pressure': user_state.get('time_pressure', 0.5),
            'interruptions': user_state.get('interruption_frequency', 0.3),
            'fatigue': user_state.get('fatigue_level', 0.4)
        }
        
        return sum(factors.values()) / len(factors)

    def _detect_flow_state(self, user_state):
        """Detect if user is in flow state"""
        engagement = user_state.get('engagement', 0.0)
        challenge = user_state.get('task_difficulty', 0.0)
        skill = user_state.get('skill_level', 0.0)

        if 0.7 <= engagement <= 1.0 and abs(challenge - skill) < 0.2:
            return 'flow'
        return 'neutral'

    def _estimate_interruption_cost(self, focus_state, cognitive_load):
        """Calculate cost of interrupting user"""
        base_cost = 0.3
        if focus_state == 'flow':
            base_cost *= 2
        return base_cost * (1 + cognitive_load)

    def _select_intervention_type(self, context, user_profile):
        """Choose most appropriate intervention type"""
        if context['cognitive_load'] > 0.8:
            return 'micro_break'
        elif context['focus_state'] == 'flow':
            return 'deep_work'
        elif context['interruption_cost'] < 0.4:
            return 'skill_building'
        return 'reflection'

    def _personalize_intervention(self, intervention_type, user_profile, context):
        """Customize intervention based on user profile and context"""
        intervention = self.intervention_types[intervention_type].copy()
        
        # Adjust for user preferences
        if user_profile['preferences'].get('duration_modifier'):
            intervention['duration'] *= user_profile['preferences']['duration_modifier']

        # Add personalized content
        intervention.update({
            'content': self._generate_content(intervention_type, user_profile),
            'delivery_style': user_profile['preferences'].get('communication_style', 'neutral'),
            'timing': self._optimize_timing(context)
        })

        return intervention

    def _add_behavioral_elements(self, intervention, user_profile):
        """Add behavioral psychology elements to intervention"""
        intervention.update({
            'cue': self._identify_trigger(user_profile),
            'reward': self._select_reward(user_profile),
            'commitment_device': self._create_commitment_device(intervention['content']),
            'social_proof': self._get_social_proof(intervention['content'])
        })
        return intervention

    def update_user_profile(self, user_id, intervention_result):
        """Update user profile based on intervention effectiveness"""
        self.user_profile['response_history'].append(intervention_result)
        self._update_effectiveness_metrics(intervention_result)
        self._adjust_user_preferences(intervention_result)

    def _update_effectiveness_metrics(self, result):
        """Update intervention effectiveness tracking"""
        intervention_type = result['intervention_type']
        effectiveness = result['effectiveness']
        
        if intervention_type in self.user_profile['intervention_effectiveness']:
            current = self.user_profile['intervention_effectiveness'][intervention_type]
            self.user_profile['intervention_effectiveness'][intervention_type] = \
                (current * 0.7) + (effectiveness * 0.3)
        else:
            self.user_profile['intervention_effectiveness'][intervention_type] = effectiveness

    def _adjust_user_preferences(self, result):
        """Adjust user preferences based on intervention results"""
        if result['user_feedback']:
            self.user_profile['preferences'].update(result['user_feedback'])