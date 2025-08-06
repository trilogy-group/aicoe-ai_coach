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
                'techniques': ['implementation_intentions', 'habit_stacking', 'temptation_bundling'],
                'timing': 'context_dependent',
                'frequency': 'variable_ratio'
            },
            'motivation_enhancement': {
                'techniques': ['goal_visualization', 'progress_tracking', 'social_accountability'],
                'timing': 'pre_action',
                'frequency': 'fixed_interval' 
            },
            'stress_management': {
                'techniques': ['mindfulness', 'cognitive_reframing', 'time_boxing'],
                'timing': 'reactive',
                'frequency': 'as_needed'
            }
        }

        # Contextual awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'task_complexity': None,
            'environmental_conditions': None,
            'social_context': None
        }

        # Behavioral psychology components
        self.behavior_drivers = {
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'ability': {'skill_level': 0.0, 'resources': 0.0},
            'prompt': {'salience': 0.0, 'timing': 0.0}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate highly personalized behavioral nudge based on user profile and context"""
        
        # Update context awareness
        self._update_context(current_context)
        
        # Select optimal intervention strategy
        strategy = self._select_intervention_strategy(user_profile)
        
        # Generate specific actionable recommendation
        nudge = self._create_targeted_nudge(strategy, user_profile)
        
        # Enhance with behavioral drivers
        enhanced_nudge = self._enhance_with_behavioral_science(nudge)
        
        return enhanced_nudge

    def _update_context(self, current_context):
        """Update contextual awareness based on current situation"""
        for factor, value in current_context.items():
            if factor in self.context_factors:
                self.context_factors[factor] = value
        
        self._recalibrate_intervention_timing()

    def _select_intervention_strategy(self, user_profile):
        """Select most appropriate intervention strategy based on user profile and context"""
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        # Match strategy to user's traits and current context
        optimal_strategy = {
            'technique': self._match_technique_to_profile(config),
            'timing': self._optimize_timing(config),
            'intensity': self._calculate_optimal_intensity()
        }
        
        return optimal_strategy

    def _create_targeted_nudge(self, strategy, user_profile):
        """Create specific, actionable recommendation"""
        nudge = {
            'content': self._generate_personalized_content(strategy, user_profile),
            'delivery_method': self._determine_delivery_method(user_profile),
            'action_steps': self._create_action_steps(strategy),
            'follow_up': self._plan_follow_up(strategy)
        }
        
        return nudge

    def _enhance_with_behavioral_science(self, nudge):
        """Apply behavioral psychology principles to enhance effectiveness"""
        
        # Update behavioral drivers
        self._update_behavior_drivers()
        
        # Apply motivation techniques
        nudge = self._apply_motivation_techniques(nudge)
        
        # Enhance with social proof
        nudge = self._add_social_proof(nudge)
        
        # Add commitment mechanism
        nudge = self._add_commitment_device(nudge)
        
        return nudge

    def _update_behavior_drivers(self):
        """Update behavior driver metrics based on context and user state"""
        self.behavior_drivers['motivation']['intrinsic'] = self._calculate_intrinsic_motivation()
        self.behavior_drivers['motivation']['extrinsic'] = self._calculate_extrinsic_motivation()
        self.behavior_drivers['ability']['skill_level'] = self._assess_current_ability()
        self.behavior_drivers['prompt']['timing'] = self._optimize_prompt_timing()

    def evaluate_effectiveness(self, user_response):
        """Evaluate and adapt based on intervention effectiveness"""
        metrics = {
            'engagement': self._calculate_engagement(user_response),
            'behavior_change': self._measure_behavior_change(user_response),
            'satisfaction': self._assess_satisfaction(user_response)
        }
        
        self._adapt_strategies(metrics)
        return metrics

    def _adapt_strategies(self, effectiveness_metrics):
        """Adapt intervention strategies based on effectiveness metrics"""
        if effectiveness_metrics['engagement'] < 0.7:
            self._adjust_engagement_approach()
        
        if effectiveness_metrics['behavior_change'] < 0.6:
            self._strengthen_behavior_triggers()
            
        if effectiveness_metrics['satisfaction'] < 0.8:
            self._improve_personalization()