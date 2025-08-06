class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning and communication preferences
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types omitted for brevity
        }

        # Enhanced behavioral psychology principles
        self.behavioral_principles = {
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'cognitive_load': ['attention', 'processing', 'retention'],
            'emotional_intelligence': ['self_awareness', 'regulation', 'empathy']
        }

        # Action templates with improved specificity and measurability
        self.action_templates = {
            'habit_building': {
                'structure': {
                    'specific_action': '',
                    'time_estimate': 0,
                    'success_metrics': [],
                    'priority_level': 1,
                    'follow_up_schedule': []
                },
                'alternatives': [],
                'implementation_steps': []
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'user_energy': None,
            'task_complexity': None,
            'environment': None
        }

        # User engagement tracking
        self.user_metrics = {
            'completion_rate': 0.0,
            'satisfaction_score': 0.0,
            'behavioral_change': 0.0,
            'engagement_level': 0.0
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized coaching intervention based on user profile and context"""
        
        # Get personality-based preferences
        personality_config = self.personality_type_configs.get(user_profile['personality_type'])
        
        # Analyze context for optimal timing
        context_score = self._evaluate_context_fitness(context)
        
        # Select appropriate behavioral principles
        selected_principles = self._select_behavioral_principles(user_profile, context)
        
        # Generate specific action recommendation
        action = self._create_action_plan(
            personality_config,
            selected_principles,
            context
        )
        
        return self._format_nudge(action, personality_config)

    def _evaluate_context_fitness(self, context):
        """Evaluate appropriateness of current context for intervention"""
        fitness_score = 0.0
        
        # Update context factors
        self.context_factors.update({
            'time_of_day': context.get('time'),
            'user_energy': context.get('energy_level'),
            'task_complexity': context.get('task_complexity'),
            'environment': context.get('environment')
        })
        
        # Calculate optimal intervention timing
        if self._is_optimal_timing(context):
            fitness_score += 1.0
            
        return fitness_score

    def _select_behavioral_principles(self, user_profile, context):
        """Select appropriate behavioral psychology principles based on user and context"""
        selected = []
        
        # Match principles to user characteristics
        for category, principles in self.behavioral_principles.items():
            relevant = self._match_principles_to_user(
                principles,
                user_profile,
                context
            )
            selected.extend(relevant)
            
        return selected

    def _create_action_plan(self, personality_config, principles, context):
        """Create specific, actionable recommendation"""
        action_plan = self.action_templates['habit_building']['structure'].copy()
        
        # Customize based on personality
        action_plan.update({
            'communication_style': personality_config['communication_pref'],
            'learning_approach': personality_config['learning_style']
        })
        
        # Add implementation steps
        action_plan['implementation_steps'] = self._generate_steps(
            principles,
            context
        )
        
        # Set metrics and follow-up
        action_plan['success_metrics'] = self._define_metrics(action_plan)
        action_plan['follow_up_schedule'] = self._create_follow_up_schedule()
        
        return action_plan

    def _format_nudge(self, action_plan, personality_config):
        """Format coaching intervention based on user preferences"""
        return {
            'message': self._generate_message(action_plan, personality_config),
            'action_steps': action_plan['implementation_steps'],
            'metrics': action_plan['success_metrics'],
            'follow_up': action_plan['follow_up_schedule']
        }

    def track_engagement(self, user_id, interaction_data):
        """Track user engagement and intervention effectiveness"""
        self.user_metrics.update({
            'completion_rate': interaction_data.get('completion_rate', 0.0),
            'satisfaction_score': interaction_data.get('satisfaction', 0.0),
            'behavioral_change': interaction_data.get('behavior_change', 0.0),
            'engagement_level': interaction_data.get('engagement', 0.0)
        })
        
        return self.user_metrics

    def _is_optimal_timing(self, context):
        """Determine if current moment is optimal for intervention"""
        return (
            context.get('user_receptivity', 0) > 0.7 and
            context.get('cognitive_load', 1) < 0.8 and
            not context.get('do_not_disturb', False)
        )

    def _match_principles_to_user(self, principles, user_profile, context):
        """Match behavioral principles to user characteristics"""
        matched = []
        for principle in principles:
            if self._principle_matches_user(principle, user_profile, context):
                matched.append(principle)
        return matched

    def _generate_steps(self, principles, context):
        """Generate specific implementation steps"""
        return [
            {
                'step': f"Implement {principle}",
                'timeframe': '10 minutes',
                'difficulty': 'medium'
            }
            for principle in principles
        ]

    def _define_metrics(self, action_plan):
        """Define specific success metrics"""
        return [
            'Completion rate',
            'Time to implement',
            'Perceived difficulty',
            'Effectiveness rating'
        ]

    def _create_follow_up_schedule(self):
        """Create follow-up check schedule"""
        return [
            {'timing': '1 day', 'type': 'quick_check'},
            {'timing': '1 week', 'type': 'detailed_review'}
        ]

    def _generate_message(self, action_plan, personality_config):
        """Generate personalized message"""
        style = personality_config['communication_pref']
        return f"Based on your {style} communication preference..."