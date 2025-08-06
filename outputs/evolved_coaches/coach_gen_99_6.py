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
            'energy_level': 0.0,
            'focus_state': 'neutral',
            'stress_level': 0.0,
            'receptivity': 0.0
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'time_based': {},
            'context_based': {},
            'state_based': {}
        }

        # Intervention strategies
        self.coaching_strategies = {
            'micro_nudges': self._generate_micro_nudges,
            'deep_insights': self._generate_deep_insights,
            'habit_formation': self._generate_habit_interventions,
            'flow_protection': self._protect_flow_state
        }

    def update_user_state(self, context_data):
        """Update user state based on real-time context"""
        self.user_state['cognitive_load'] = self._assess_cognitive_load(context_data)
        self.user_state['energy_level'] = self._assess_energy_level(context_data)
        self.user_state['focus_state'] = self._detect_focus_state(context_data)
        self.user_state['stress_level'] = self._assess_stress_level(context_data)
        self.user_state['receptivity'] = self._calculate_receptivity()

    def generate_coaching_intervention(self, user_profile, context):
        """Generate personalized coaching intervention"""
        if not self._should_intervene():
            return None

        strategy = self._select_optimal_strategy()
        intervention = self.coaching_strategies[strategy](user_profile, context)
        
        return self._personalize_intervention(intervention, user_profile)

    def _assess_cognitive_load(self, context_data):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': 0.3,
            'time_pressure': 0.2,
            'interruption_frequency': 0.2,
            'task_switching': 0.3
        }
        
        load = sum(factors[f] * context_data.get(f, 0) for f in factors)
        return min(load, 1.0)

    def _detect_focus_state(self, context_data):
        """Detect user's current focus state"""
        if context_data.get('deep_work_signals', 0) > 0.7:
            return 'flow'
        elif context_data.get('distraction_signals', 0) > 0.5:
            return 'distracted'
        return 'neutral'

    def _calculate_receptivity(self):
        """Calculate user's receptivity to coaching"""
        weights = {
            'cognitive_load': -0.3,
            'energy_level': 0.2,
            'stress_level': -0.2
        }
        
        receptivity = sum(weights[k] * self.user_state[k] for k in weights)
        return max(0.0, min(1.0, receptivity + 0.5))

    def _should_intervene(self):
        """Determine if intervention is appropriate"""
        if self.user_state['focus_state'] == 'flow':
            return False
        if self.user_state['cognitive_load'] > 0.8:
            return False
        if self.user_state['receptivity'] < 0.3:
            return False
        return True

    def _select_optimal_strategy(self):
        """Select best coaching strategy for current state"""
        if self.user_state['cognitive_load'] > 0.6:
            return 'micro_nudges'
        if self.user_state['focus_state'] == 'distracted':
            return 'flow_protection'
        if self.user_state['receptivity'] > 0.7:
            return 'deep_insights'
        return 'habit_formation'

    def _generate_micro_nudges(self, user_profile, context):
        """Generate minimal-disruption nudges"""
        return {
            'type': 'micro_nudge',
            'content': self._get_personalized_nudge(user_profile),
            'delivery': 'subtle',
            'timing': self._optimize_timing(context)
        }

    def _generate_deep_insights(self, user_profile, context):
        """Generate comprehensive coaching insights"""
        return {
            'type': 'insight',
            'content': self._get_personalized_insight(user_profile),
            'supporting_data': self._gather_relevant_data(context),
            'action_steps': self._generate_action_steps(user_profile)
        }

    def _generate_habit_interventions(self, user_profile, context):
        """Generate habit-forming interventions"""
        return {
            'type': 'habit_builder',
            'trigger': self._identify_habit_trigger(context),
            'desired_action': self._get_target_behavior(user_profile),
            'reward': self._design_reward(user_profile)
        }

    def _protect_flow_state(self, user_profile, context):
        """Generate flow state protection interventions"""
        return {
            'type': 'flow_protection',
            'barrier': self._identify_disruption_sources(context),
            'protection_strategy': self._get_protection_strategy(user_profile),
            'duration': self._calculate_optimal_duration(context)
        }

    def _personalize_intervention(self, intervention, user_profile):
        """Personalize intervention based on user profile"""
        personality_config = self.personality_type_configs.get(
            user_profile.get('personality_type', 'INTJ')
        )
        
        intervention['style'] = personality_config['communication_pref']
        intervention['pacing'] = personality_config['learning_style']
        intervention['timing'] = self._optimize_timing(personality_config['work_pattern'])
        
        return intervention

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        return {
            'preferred_time': self._calculate_optimal_time(context),
            'frequency': self._calculate_optimal_frequency(context),
            'duration': self._calculate_optimal_duration(context)
        }