class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced behavioral psychology components
        self.behavioral_models = {
            'motivation': {
                'intrinsic': ['autonomy', 'mastery', 'purpose'],
                'extrinsic': ['rewards', 'accountability', 'social_proof']
            },
            'habit_formation': {
                'cue': ['context', 'time', 'emotion', 'location'],
                'routine': ['micro_steps', 'implementation_intentions'],
                'reward': ['immediate', 'delayed', 'compound']
            }
        }

        # Cognitive load and attention management
        self.cognitive_states = {
            'flow': {'threshold': 0.8, 'protection_time': 45},
            'fatigue': {'threshold': 0.3, 'recovery_time': 15},
            'optimal_challenge': {'min': 0.6, 'max': 0.85}
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'work_context': None,
            'recent_activity': [],
            'environment': None
        }

        # User profile and adaptation tracking
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'achievement_metrics': {},
            'preference_weights': {}
        }

    def assess_user_state(self, user_data):
        """Evaluate current user cognitive and emotional state"""
        cognitive_load = self._calculate_cognitive_load(user_data)
        energy_level = self._assess_energy_level(user_data)
        context = self._detect_work_context(user_data)
        
        return {
            'cognitive_load': cognitive_load,
            'energy_level': energy_level,
            'context': context
        }

    def generate_intervention(self, user_state, goals):
        """Create personalized coaching intervention"""
        if not self._should_intervene(user_state):
            return None

        intervention_type = self._select_intervention_type(user_state, goals)
        content = self._generate_content(intervention_type, user_state, goals)
        timing = self._optimize_timing(user_state)

        return {
            'type': intervention_type,
            'content': content,
            'timing': timing,
            'context': user_state['context']
        }

    def _calculate_cognitive_load(self, user_data):
        """Assess current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': self._assess_task_complexity(user_data),
            'context_switches': len(user_data.get('recent_activities', [])),
            'time_pressure': user_data.get('deadline_proximity', 0),
            'interruption_frequency': user_data.get('interruptions', 0)
        }
        
        weights = {'task_complexity': 0.4, 'context_switches': 0.2,
                  'time_pressure': 0.2, 'interruption_frequency': 0.2}
        
        return sum(factor * weights[key] for key, factor in factors.items())

    def _select_intervention_type(self, user_state, goals):
        """Choose most appropriate intervention based on state and goals"""
        if user_state['cognitive_load'] > self.cognitive_states['flow']['threshold']:
            return 'protection'
        elif user_state['energy_level'] < self.cognitive_states['fatigue']['threshold']:
            return 'recovery'
        else:
            return 'enhancement'

    def _generate_content(self, intervention_type, user_state, goals):
        """Create specific, actionable recommendation content"""
        if intervention_type == 'protection':
            return self._generate_protection_nudge(user_state)
        elif intervention_type == 'recovery':
            return self._generate_recovery_suggestion(user_state)
        else:
            return self._generate_enhancement_recommendation(user_state, goals)

    def _optimize_timing(self, user_state):
        """Determine optimal intervention timing"""
        if user_state['cognitive_load'] > self.cognitive_states['flow']['threshold']:
            return 'defer'
        
        current_context = user_state['context']
        if current_context == 'meeting':
            return 'after_meeting'
        elif current_context == 'focused_work':
            return 'next_break'
        else:
            return 'immediate'

    def update_user_profile(self, interaction_data):
        """Update user profile based on interaction outcomes"""
        self.user_profile['response_history'].append(interaction_data)
        self._update_learning_patterns(interaction_data)
        self._adjust_preference_weights(interaction_data)
        self._update_achievement_metrics(interaction_data)

    def _should_intervene(self, user_state):
        """Determine if intervention is appropriate"""
        return (
            not self._is_in_flow(user_state) and
            self._has_attention_capacity(user_state) and
            self._sufficient_time_elapsed()
        )

    def _generate_protection_nudge(self, user_state):
        """Create flow state protection intervention"""
        return {
            'message': 'You\'re in a productive flow. Want to enable focus mode?',
            'actions': ['Enable focus mode', 'Remind me later'],
            'duration': self.cognitive_states['flow']['protection_time']
        }

    def _generate_recovery_suggestion(self, user_state):
        """Create recovery intervention"""
        return {
            'message': 'Time for a quick recharge. Here\'s a 5-minute mindfulness exercise.',
            'actions': ['Start exercise', 'Skip'],
            'duration': self.cognitive_states['fatigue']['recovery_time']
        }

    def _generate_enhancement_recommendation(self, user_state, goals):
        """Create growth-oriented intervention"""
        return {
            'message': f'Ready to tackle your {goals[0]}? Here\'s a specific next step.',
            'actions': ['Start now', 'Modify', 'Later'],
            'duration': 30
        }