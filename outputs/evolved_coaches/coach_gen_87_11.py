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
            'interruption_cost': 0.0
        }

        # Behavioral psychology components
        self.behavioral_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'flow_state': {'current': False, 'duration': 0},
            'burnout_risk': 0.0
        }

        # Personalization tracking
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preferred_times': [],
            'attention_spans': []
        }

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {'duration': 2, 'frequency': 'high'},
            'deep_work': {'duration': 45, 'frequency': 'medium'},
            'reflection': {'duration': 10, 'frequency': 'low'},
            'skill_building': {'duration': 15, 'frequency': 'medium'}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy_level(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity'),
            'interruption_cost': self._calculate_interruption_cost()
        })
        return self.context_tracker

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if not self._should_intervene():
            return None

        intervention_type = self._select_intervention_type()
        personalized_content = self._personalize_content(intervention_type, user_profile)
        
        return {
            'type': intervention_type,
            'content': personalized_content,
            'timing': self._optimize_timing(),
            'duration': self.intervention_types[intervention_type]['duration'],
            'action_steps': self._generate_action_steps()
        }

    def update_user_model(self, interaction_result):
        """Update user model based on intervention results"""
        self.user_profile['response_history'].append(interaction_result)
        self._update_effectiveness_metrics(interaction_result)
        self._adjust_intervention_parameters()
        self._update_learning_patterns()

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0),
            'context_switches': user_state.get('context_switches', 0),
            'time_pressure': user_state.get('time_pressure', 0)
        }
        return sum(factors.values()) / len(factors)

    def _should_intervene(self):
        """Determine if intervention is appropriate"""
        return (
            self.context_tracker['cognitive_load'] < 0.8 and
            self.context_tracker['interruption_cost'] < 0.6 and
            not self.behavioral_models['flow_state']['current']
        )

    def _select_intervention_type(self):
        """Choose appropriate intervention based on context"""
        if self.context_tracker['cognitive_load'] > 0.6:
            return 'micro_break'
        elif self.context_tracker['energy_level'] < 0.4:
            return 'deep_work'
        else:
            return 'skill_building'

    def _personalize_content(self, intervention_type, user_profile):
        """Create personalized intervention content"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        return {
            'style': personality_config['communication_pref'],
            'complexity': self._adapt_complexity(),
            'framing': self._optimize_framing(personality_config),
            'examples': self._generate_relevant_examples()
        }

    def _generate_action_steps(self):
        """Create specific, actionable recommendations"""
        return [
            {'step': 1, 'action': 'Specific action', 'duration': '5m'},
            {'step': 2, 'action': 'Next action', 'duration': '10m'},
            {'step': 3, 'action': 'Final action', 'duration': '5m'}
        ]

    def _optimize_timing(self):
        """Optimize intervention timing"""
        return {
            'preferred_time': self._get_optimal_time(),
            'max_duration': self._calculate_available_time(),
            'urgency': self._assess_urgency()
        }

    def _update_effectiveness_metrics(self, result):
        """Update intervention effectiveness tracking"""
        metrics = self.user_profile['effectiveness_metrics']
        metrics['engagement'] = (metrics.get('engagement', 0) * 0.9) + (result['engagement'] * 0.1)
        metrics['completion'] = (metrics.get('completion', 0) * 0.9) + (result['completion'] * 0.1)
        metrics['satisfaction'] = (metrics.get('satisfaction', 0) * 0.9) + (result['satisfaction'] * 0.1)

    def _adjust_intervention_parameters(self):
        """Adapt intervention parameters based on effectiveness"""
        for intervention in self.intervention_types:
            self._optimize_intervention_frequency(intervention)
            self._adjust_intervention_duration(intervention)

    def _update_learning_patterns(self):
        """Update user learning pattern analysis"""
        recent_patterns = self._analyze_recent_responses()
        self.user_profile['learning_patterns'].append(recent_patterns)
        self._prune_old_patterns()