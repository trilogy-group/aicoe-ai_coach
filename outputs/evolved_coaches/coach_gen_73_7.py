class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning patterns
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'autonomy', 'achievement'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'social_connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types configured similarly
        }

        # Enhanced intervention templates with behavioral psychology
        self.intervention_templates = {
            'habit_formation': {
                'cue': lambda context: self._identify_behavioral_trigger(context),
                'routine': lambda goal: self._generate_micro_steps(goal),
                'reward': lambda achievement: self._create_reward_schedule(achievement),
                'difficulty': lambda user: self._adapt_challenge_level(user),
                'followup': lambda progress: self._schedule_accountability_check(progress)
            },
            'focus_enhancement': {
                'environment': lambda context: self._optimize_work_environment(context),
                'timeblock': lambda schedule: self._create_focused_intervals(schedule),
                'breaks': lambda energy: self._schedule_recovery_periods(energy),
                'distractions': lambda triggers: self._minimize_interruptions(triggers)
            }
        }

        # Contextual awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environmental_conditions': None,
            'recent_performance': None,
            'stress_indicators': None
        }

        # Action tracking and metrics
        self.progress_metrics = {
            'completed_actions': [],
            'behavior_changes': {},
            'satisfaction_scores': [],
            'engagement_level': 0.0,
            'effectiveness_rating': 0.0
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate highly personalized coaching intervention"""
        personality_config = self.personality_type_configs[user_profile['type']]
        
        # Analyze current context
        context_score = self._evaluate_context_fitness(context)
        
        # Select optimal intervention timing
        if not self._is_optimal_timing(context_score):
            return None

        # Generate intervention based on personality and context
        intervention = self._create_targeted_intervention(
            personality_config,
            context,
            user_profile['goals']
        )

        # Add specific actionable steps
        intervention['action_steps'] = self._generate_action_steps(
            intervention['type'],
            personality_config['learning_style']
        )

        # Include progress tracking
        intervention['metrics'] = self._define_success_metrics(intervention['type'])
        
        return intervention

    def _evaluate_context_fitness(self, context):
        """Evaluate if current context is suitable for intervention"""
        context_weights = {
            'time_of_day': 0.3,
            'energy_level': 0.2,
            'task_complexity': 0.2,
            'environmental_conditions': 0.15,
            'recent_performance': 0.15
        }
        
        fitness_score = sum(
            context_weights[factor] * self._normalize_factor(context[factor])
            for factor in context_weights
        )
        
        return fitness_score

    def _create_targeted_intervention(self, personality_config, context, goals):
        """Create personalized intervention matching user traits and context"""
        intervention_type = self._select_intervention_type(
            personality_config['motivation_triggers'],
            context['task_complexity']
        )
        
        return {
            'type': intervention_type,
            'style': personality_config['communication_pref'],
            'intensity': self._calculate_intensity(
                personality_config['cognitive_load_threshold'],
                context['energy_level']
            ),
            'timing': self._optimize_timing(context['time_of_day']),
            'format': self._select_format(personality_config['learning_style'])
        }

    def _generate_action_steps(self, intervention_type, learning_style):
        """Generate specific, actionable steps"""
        base_steps = self.intervention_templates[intervention_type]
        
        return {
            'immediate': self._adapt_to_style(base_steps['cue'], learning_style),
            'short_term': self._adapt_to_style(base_steps['routine'], learning_style),
            'reinforcement': self._adapt_to_style(base_steps['reward'], learning_style),
            'timeline': self._create_timeline(intervention_type),
            'alternatives': self._generate_alternatives(intervention_type)
        }

    def _define_success_metrics(self, intervention_type):
        """Define concrete success metrics for intervention"""
        return {
            'behavioral_indicators': self._identify_behavior_metrics(intervention_type),
            'satisfaction_measures': self._define_satisfaction_metrics(),
            'progress_tracking': self._create_progress_markers(),
            'verification_method': self._select_verification_approach()
        }

    def update_progress(self, user_id, action_results):
        """Update progress tracking and adjust future interventions"""
        self.progress_metrics['completed_actions'].append(action_results)
        self._update_effectiveness_metrics(action_results)
        self._adjust_intervention_parameters(user_id, action_results)

    def get_performance_stats(self):
        """Return current performance statistics"""
        return {
            'engagement_rate': self._calculate_engagement(),
            'behavior_change_rate': self._calculate_behavior_change(),
            'satisfaction_score': self._calculate_satisfaction(),
            'effectiveness_rating': self.progress_metrics['effectiveness_rating']
        }