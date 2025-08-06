class EnhancedAICoach:
    def __init__(self):
        # Personality and learning profiles
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
        
        # Personalization engine
        self.user_profile = {
            'preferences': {},
            'response_history': [],
            'learning_patterns': {},
            'intervention_effectiveness': {}
        }

    def assess_context(self, user_state):
        """Evaluate current user context and state"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._assess_energy_level(user_state),
            'time_of_day': user_state.get('time'),
            'work_context': user_state.get('activity')
        })
        return self.context_tracker

    def generate_intervention(self, user_state):
        """Generate personalized coaching intervention"""
        context = self.assess_context(user_state)
        
        # Check intervention timing
        if not self._is_good_intervention_time():
            return None
            
        # Select intervention type based on context
        intervention_type = self._select_intervention_type(context)
        
        # Personalize content
        content = self._personalize_content(intervention_type, user_state)
        
        # Add behavioral reinforcement
        content = self._add_behavioral_elements(content)
        
        return {
            'type': intervention_type,
            'content': content,
            'timing': self._get_optimal_timing(),
            'action_steps': self._generate_action_steps(content)
        }

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'time_pressure': user_state.get('deadline_pressure', 0.4)
        }
        return sum(factors.values()) / len(factors)

    def _assess_energy_level(self, user_state):
        """Calculate user energy level"""
        factors = {
            'time_since_break': user_state.get('time_since_break', 0),
            'task_duration': user_state.get('continuous_work_time', 0),
            'daily_activity': user_state.get('activity_level', 0.5)
        }
        return self._normalize_energy_score(factors)

    def _is_good_intervention_time(self):
        """Determine if current moment is optimal for intervention"""
        if self.behavioral_models['flow_state']['current']:
            return False
        
        recent_interventions = len(self.context_tracker['recent_interventions'])
        if recent_interventions > 3:
            return False
            
        return True

    def _select_intervention_type(self, context):
        """Choose appropriate intervention type based on context"""
        if context['cognitive_load'] > 0.7:
            return 'micro_break'
        elif context['energy_level'] < 0.3:
            return 'energy_boost'
        else:
            return 'growth_prompt'

    def _personalize_content(self, intervention_type, user_state):
        """Create personalized intervention content"""
        personality_type = user_state.get('personality_type')
        config = self.personality_type_configs.get(personality_type, {})
        
        content = {
            'style': config.get('communication_pref', 'neutral'),
            'complexity': self._adjust_complexity(context['cognitive_load']),
            'duration': self._calculate_optimal_duration(),
            'tone': self._select_tone(user_state)
        }
        
        return content

    def _add_behavioral_elements(self, content):
        """Add behavioral psychology elements to intervention"""
        content.update({
            'reinforcement': self._select_reinforcement_type(),
            'habit_trigger': self._identify_habit_trigger(),
            'motivation_elements': self._add_motivation_factors()
        })
        return content

    def _generate_action_steps(self, content):
        """Create specific, actionable steps"""
        return {
            'immediate_action': self._create_immediate_step(),
            'follow_up': self._create_follow_up_steps(),
            'measurement': self._create_progress_metrics()
        }

    def update_effectiveness(self, intervention_id, user_feedback):
        """Update intervention effectiveness tracking"""
        self.user_profile['intervention_effectiveness'][intervention_id] = user_feedback
        self._update_learning_patterns(intervention_id, user_feedback)

    def _update_learning_patterns(self, intervention_id, feedback):
        """Update user learning patterns based on feedback"""
        pattern = {
            'intervention_id': intervention_id,
            'feedback': feedback,
            'context': self.context_tracker.copy(),
            'timestamp': self._get_current_timestamp()
        }
        self.user_profile['learning_patterns'][intervention_id] = pattern