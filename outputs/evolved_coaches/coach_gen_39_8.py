class EvolutionaryAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types omitted for brevity
        }

        # Enhanced behavioral psychology principles
        self.behavioral_principles = {
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'habit_formation': ['cue', 'routine', 'reward'],
            'cognitive_load': ['attention', 'processing', 'retention'],
            'emotional_intelligence': ['self_awareness', 'regulation', 'empathy']
        }

        # Action recommendation templates with improved specificity
        self.action_templates = {
            'task_focus': {
                'template': "Focus on {task} for {duration} minutes using {technique}",
                'metrics': ['completion_rate', 'quality_score'],
                'priority_levels': ['critical', 'high', 'medium', 'low'],
                'time_estimates': {'quick': 15, 'medium': 30, 'extended': 60}
            },
            'skill_development': {
                'template': "Practice {skill} through {exercise} for {duration} minutes",
                'success_criteria': ['proficiency_level', 'consistency'],
                'difficulty_levels': ['beginner', 'intermediate', 'advanced']
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized coaching intervention based on user profile and context"""
        
        # Update context awareness
        self.context_factors.update(context)
        
        # Get personality-specific configurations
        personality_config = self.personality_type_configs.get(user_profile['personality_type'])
        
        # Select appropriate behavioral principles
        selected_principles = self._select_behavioral_principles(user_profile, context)
        
        # Generate specific action recommendation
        action = self._create_action_recommendation(
            personality_config,
            selected_principles,
            context
        )
        
        return self._format_nudge(action, personality_config)

    def _select_behavioral_principles(self, user_profile, context):
        """Select relevant behavioral psychology principles based on user and context"""
        principles = []
        
        # Analyze cognitive load
        if context['task_complexity'] == 'high':
            principles.extend(self.behavioral_principles['cognitive_load'])
            
        # Add motivation elements
        if context['energy_level'] == 'low':
            principles.extend(self.behavioral_principles['motivation'])
            
        # Include habit formation for recurring tasks
        if context.get('task_frequency') == 'recurring':
            principles.extend(self.behavioral_principles['habit_formation'])
            
        return principles

    def _create_action_recommendation(self, personality_config, principles, context):
        """Create specific, actionable recommendations"""
        
        action = {
            'type': self._determine_action_type(context),
            'duration': self._calculate_optimal_duration(context),
            'technique': self._select_technique(personality_config, principles),
            'success_metrics': self._define_success_metrics(context),
            'priority': self._assess_priority(context),
            'follow_up': self._create_follow_up_plan(context)
        }
        
        return action

    def _determine_action_type(self, context):
        """Determine most appropriate type of action based on context"""
        if context['task_complexity'] == 'high':
            return 'task_focus'
        return 'skill_development'

    def _calculate_optimal_duration(self, context):
        """Calculate optimal duration based on context factors"""
        base_duration = self.action_templates['task_focus']['time_estimates']['medium']
        
        # Adjust for energy level
        if context['energy_level'] == 'low':
            base_duration *= 0.7
        elif context['energy_level'] == 'high':
            base_duration *= 1.3
            
        return round(base_duration)

    def _select_technique(self, personality_config, principles):
        """Select appropriate technique based on personality and principles"""
        if personality_config['learning_style'] == 'systematic':
            return 'structured_approach'
        return 'flexible_approach'

    def _define_success_metrics(self, context):
        """Define specific, measurable success metrics"""
        return {
            'completion_rate': 'percentage',
            'quality_score': 'scale_1_10',
            'time_efficiency': 'minutes_saved'
        }

    def _assess_priority(self, context):
        """Assess priority level of recommendation"""
        if context['task_complexity'] == 'high' and context['time_of_day'] == 'peak':
            return 'critical'
        return 'medium'

    def _create_follow_up_plan(self, context):
        """Create specific follow-up plan"""
        return {
            'timing': 'end_of_session',
            'metrics_to_check': ['completion_rate', 'quality_score'],
            'adjustment_threshold': 0.8
        }

    def _format_nudge(self, action, personality_config):
        """Format nudge according to user's communication preferences"""
        template = self.action_templates[action['type']]['template']
        
        return {
            'message': template.format(
                task=action['type'],
                duration=action['duration'],
                technique=action['technique']
            ),
            'style': personality_config['communication_pref'],
            'metrics': action['success_metrics'],
            'priority': action['priority'],
            'follow_up': action['follow_up']
        }

    def update_effectiveness(self, feedback):
        """Update system effectiveness based on feedback"""
        # Implementation for updating based on feedback
        pass