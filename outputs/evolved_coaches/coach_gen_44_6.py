class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_response': 'analytical',
                'decision_style': 'logical'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'adaptive',
                'decision_style': 'intuitive'
            }
            # Additional types configured similarly
        }

        # Evidence-based intervention strategies
        self.intervention_strategies = {
            'habit_formation': {
                'cue_identification': True,
                'routine_design': True,
                'reward_scheduling': True,
                'progress_tracking': True
            },
            'motivation_enhancement': {
                'goal_setting': True,
                'value_alignment': True,
                'self_efficacy': True,
                'social_support': True
            },
            'behavioral_activation': {
                'activity_scheduling': True,
                'graded_tasks': True,
                'success_spirals': True,
                'reinforcement': True
            }
        }

        # Context-aware nudge parameters
        self.nudge_config = {
            'timing': {
                'peak_energy_hours': True,
                'task_complexity': True,
                'current_workload': True,
                'recovery_needs': True
            },
            'frequency': {
                'learning_curve': True,
                'habit_stage': True,
                'engagement_level': True,
                'progress_rate': True
            },
            'modality': {
                'text': True,
                'audio': True,
                'visual': True,
                'interactive': True
            }
        }

        # Cognitive load management
        self.cognitive_parameters = {
            'attention_span': None,
            'mental_energy': None,
            'task_complexity': None,
            'context_switches': None,
            'learning_capacity': None
        }

    def generate_personalized_intervention(self, user_data, context):
        """Generate highly personalized coaching intervention"""
        personality_profile = self._analyze_personality(user_data)
        current_context = self._assess_context(context)
        cognitive_state = self._evaluate_cognitive_load(user_data)

        intervention = {
            'content': self._create_content(personality_profile, current_context),
            'timing': self._optimize_timing(cognitive_state, current_context),
            'format': self._select_format(personality_profile, cognitive_state),
            'action_steps': self._generate_action_steps(current_context)
        }

        return self._validate_and_enhance(intervention)

    def _analyze_personality(self, user_data):
        """Analyze user personality and preferences"""
        personality_type = user_data.get('personality_type')
        base_config = self.personality_type_configs.get(personality_type, {})
        
        return {
            'learning_style': base_config.get('learning_style'),
            'communication_pref': base_config.get('communication_pref'),
            'motivation_drivers': base_config.get('motivation_drivers'),
            'adaptations': self._generate_adaptations(user_data)
        }

    def _assess_context(self, context):
        """Evaluate current user context for relevance"""
        return {
            'time_of_day': context.get('time'),
            'energy_level': context.get('energy'),
            'current_goals': context.get('goals'),
            'recent_progress': context.get('progress'),
            'environmental_factors': context.get('environment')
        }

    def _evaluate_cognitive_load(self, user_data):
        """Assess current cognitive capacity"""
        return {
            'attention_availability': self._calculate_attention(user_data),
            'mental_bandwidth': self._estimate_bandwidth(user_data),
            'optimal_complexity': self._determine_complexity(user_data)
        }

    def _create_content(self, profile, context):
        """Generate personalized coaching content"""
        template = self._select_template(profile)
        customization = self._apply_contextual_customization(template, context)
        return self._enhance_with_psychology(customization)

    def _optimize_timing(self, cognitive_state, context):
        """Determine optimal intervention timing"""
        return {
            'best_time': self._calculate_optimal_time(cognitive_state, context),
            'frequency': self._determine_frequency(cognitive_state),
            'duration': self._calculate_duration(cognitive_state)
        }

    def _select_format(self, profile, cognitive_state):
        """Choose most effective delivery format"""
        return {
            'primary_mode': self._determine_primary_mode(profile),
            'backup_mode': self._determine_backup_mode(profile),
            'complexity_level': self._adjust_complexity(cognitive_state)
        }

    def _generate_action_steps(self, context):
        """Create specific, actionable recommendations"""
        return {
            'immediate_actions': self._identify_immediate_actions(context),
            'short_term_goals': self._set_short_term_goals(context),
            'progress_metrics': self._define_metrics(context)
        }

    def _validate_and_enhance(self, intervention):
        """Validate and optimize final intervention"""
        if not self._meets_quality_standards(intervention):
            intervention = self._enhance_intervention(intervention)
        return intervention

    def update_model(self, feedback_data):
        """Update coaching model based on feedback"""
        self._update_effectiveness_metrics(feedback_data)
        self._refine_strategies(feedback_data)
        self._optimize_parameters(feedback_data)