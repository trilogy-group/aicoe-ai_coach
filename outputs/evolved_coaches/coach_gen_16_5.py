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
            'flow_state': {'depth': 0.0, 'duration': 0},
            'burnout_risk': 0.0
        }

        # User profile and personalization
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_metrics': {},
            'preferred_times': [],
            'intervention_sensitivity': 0.0
        }

        # Intervention strategies
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
        personalized_content = self._personalize_content(intervention_type)
        
        return {
            'type': intervention_type,
            'content': personalized_content,
            'timing': self._optimize_timing(),
            'duration': self.intervention_types[intervention_type]['duration'],
            'action_steps': self._generate_action_steps()
        }

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on user state"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'context_switches': user_state.get('context_switches', 0),
            'time_pressure': user_state.get('time_pressure', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _estimate_energy_level(self, user_state):
        """Estimate user energy level based on activity patterns"""
        base_energy = user_state.get('base_energy', 0.8)
        time_active = user_state.get('time_active', 0)
        recent_breaks = user_state.get('recent_breaks', [])
        
        energy_decay = 0.1 * (time_active / 3600)  # Decay per hour
        break_recovery = sum([0.1 for b in recent_breaks if b > 10])  # Recovery from breaks
        
        return min(1.0, max(0.0, base_energy - energy_decay + break_recovery))

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (
            self.context_tracker['cognitive_load'] < 0.8 and
            self.context_tracker['interruption_cost'] < 0.6 and
            self._check_timing_appropriate()
        )

    def _select_intervention_type(self):
        """Choose most appropriate intervention type"""
        if self.context_tracker['cognitive_load'] > 0.6:
            return 'micro_break'
        elif self.context_tracker['energy_level'] < 0.4:
            return 'deep_work'
        elif len(self.user_profile['learning_patterns']) > 5:
            return 'skill_building'
        return 'reflection'

    def _personalize_content(self, intervention_type):
        """Create personalized intervention content"""
        personality = self.user_profile['personality_type']
        config = self.personality_type_configs.get(personality, {})
        
        return {
            'style': config.get('communication_pref', 'neutral'),
            'complexity': self._adapt_complexity(),
            'framing': self._optimize_framing(),
            'examples': self._generate_relevant_examples()
        }

    def _generate_action_steps(self):
        """Create specific, actionable recommendations"""
        return [
            {'step': 1, 'action': 'Specific action 1', 'duration': '5m'},
            {'step': 2, 'action': 'Specific action 2', 'duration': '10m'},
            {'step': 3, 'action': 'Specific action 3', 'duration': '5m'}
        ]

    def update_effectiveness(self, intervention_result):
        """Update intervention effectiveness metrics"""
        self.user_profile['effectiveness_metrics'][intervention_result['type']] = {
            'success_rate': intervention_result.get('success_rate', 0.0),
            'engagement': intervention_result.get('engagement', 0.0),
            'impact': intervention_result.get('impact', 0.0)
        }

    def _optimize_timing(self):
        """Optimize intervention timing based on user patterns"""
        return {
            'preferred_time': self._get_optimal_time(),
            'frequency': self._calculate_optimal_frequency(),
            'duration': self._calculate_optimal_duration()
        }

    def _adapt_complexity(self):
        """Adapt content complexity to user state"""
        return min(1.0, 
                  (1 - self.context_tracker['cognitive_load']) * 
                  self.user_profile['intervention_sensitivity'])

    def _calculate_interruption_cost(self):
        """Calculate cost of interrupting current activity"""
        return (self.context_tracker['cognitive_load'] * 0.7 + 
                (1 - self.context_tracker['energy_level']) * 0.3)