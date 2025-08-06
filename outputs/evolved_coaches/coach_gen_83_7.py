class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'cognitive_style': 'analytical',
                'stress_response': 'problem_solving'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'cognitive_style': 'intuitive',
                'stress_response': 'reframing'
            }
            # Additional types...
        }

        # Evidence-based intervention strategies
        self.intervention_strategies = {
            'habit_formation': {
                'techniques': ['implementation_intentions', 'habit_stacking', 'temptation_bundling'],
                'timing': 'context_dependent',
                'frequency': 'adaptive'
            },
            'motivation_enhancement': {
                'techniques': ['goal_visualization', 'progress_tracking', 'reward_scheduling'],
                'timing': 'energy_dependent',
                'frequency': 'variable_ratio'
            },
            'behavioral_activation': {
                'techniques': ['graded_tasks', 'success_spirals', 'momentum_building'],
                'timing': 'mood_dependent',
                'frequency': 'increasing_intervals'
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'current_goals': [],
            'recent_progress': {},
            'environmental_factors': {}
        }

        # Cognitive load management
        self.cognitive_load_manager = {
            'attention_threshold': 0.7,
            'complexity_ceiling': 3,
            'context_switches': 0,
            'recovery_periods': []
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate highly personalized behavioral nudge"""
        
        # Update context awareness
        self._update_context(current_context)
        
        # Select optimal intervention strategy
        strategy = self._select_intervention_strategy(user_profile)
        
        # Generate specific actionable recommendation
        nudge = self._craft_nudge(strategy, user_profile)
        
        # Validate and optimize timing
        if not self._is_optimal_timing(nudge):
            return self._defer_nudge(nudge)
            
        return nudge

    def _update_context(self, current_context):
        """Update context awareness based on current user state"""
        self.context_factors.update(current_context)
        self._assess_cognitive_load()
        self._track_progress_markers()

    def _select_intervention_strategy(self, user_profile):
        """Select most appropriate intervention based on user profile and context"""
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy_weights = {
            'habit_formation': self._calculate_strategy_weight('habit_formation', config),
            'motivation_enhancement': self._calculate_strategy_weight('motivation_enhancement', config),
            'behavioral_activation': self._calculate_strategy_weight('behavioral_activation', config)
        }
        
        return max(strategy_weights.items(), key=lambda x: x[1])[0]

    def _craft_nudge(self, strategy, user_profile):
        """Create specific, actionable recommendation"""
        selected_technique = self._select_technique(strategy)
        
        return {
            'content': self._generate_content(selected_technique, user_profile),
            'timing': self._optimize_timing(user_profile),
            'format': self._determine_format(user_profile),
            'action_steps': self._generate_action_steps(selected_technique),
            'follow_up': self._plan_follow_up(selected_technique)
        }

    def _calculate_strategy_weight(self, strategy, config):
        """Calculate effectiveness weight for intervention strategy"""
        base_weight = 1.0
        
        # Apply contextual modifiers
        context_modifier = self._get_context_modifier(strategy)
        personality_modifier = self._get_personality_modifier(strategy, config)
        progress_modifier = self._get_progress_modifier(strategy)
        
        return base_weight * context_modifier * personality_modifier * progress_modifier

    def _assess_cognitive_load(self):
        """Monitor and manage cognitive load"""
        current_load = self._calculate_cognitive_load()
        
        if current_load > self.cognitive_load_manager['attention_threshold']:
            self._initiate_recovery_period()
            
        self.cognitive_load_manager['context_switches'] += 1

    def _track_progress_markers(self):
        """Track behavioral change indicators"""
        for goal in self.context_factors['current_goals']:
            progress = self._measure_goal_progress(goal)
            self.context_factors['recent_progress'][goal] = progress

    def _is_optimal_timing(self, nudge):
        """Determine if timing is optimal for intervention"""
        energy_sufficient = self.context_factors['energy_level'] > 0.5
        stress_manageable = self.context_factors['stress_level'] < 0.7
        cognitive_capacity = self._has_cognitive_capacity()
        
        return all([energy_sufficient, stress_manageable, cognitive_capacity])

    def _generate_action_steps(self, technique):
        """Generate specific, achievable action steps"""
        return [
            {
                'step': f"Implement {technique}",
                'timeframe': 'immediate',
                'difficulty': 'manageable',
                'success_criteria': 'measurable_outcome'
            }
        ]

    def _plan_follow_up(self, technique):
        """Plan appropriate follow-up and reinforcement"""
        return {
            'timing': self._calculate_optimal_follow_up(),
            'type': self._determine_follow_up_type(technique),
            'success_metrics': self._define_success_metrics()
        }