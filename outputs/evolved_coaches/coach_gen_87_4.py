class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning and communication preferences
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types omitted for brevity
        }

        # Enhanced behavioral psychology principles
        self.behavior_principles = {
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'cognitive_load': ['attention', 'processing', 'retention'],
            'emotional_intelligence': ['self_awareness', 'regulation', 'empathy']
        }

        # Action recommendation templates with improved specificity
        self.action_templates = {
            'task_focus': {
                'template': "Focus on {task} for {duration} minutes using {technique}",
                'metrics': ['completion_rate', 'quality_score'],
                'priority_levels': ['critical', 'high', 'medium', 'low'],
                'time_estimates': {'short': 15, 'medium': 30, 'long': 60}
            },
            'skill_development': {
                'template': "Practice {skill} through {exercise} for {duration} minutes",
                'success_criteria': ['proficiency_level', 'consistency'],
                'difficulty_levels': ['beginner', 'intermediate', 'advanced']
            }
        }

        # Enhanced contextual awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

        # User engagement tracking
        self.user_metrics = {
            'recommendation_adherence': 0.0,
            'behavior_change_rate': 0.0,
            'satisfaction_score': 0.0,
            'progress_markers': []
        }

    def generate_personalized_nudge(self, user_profile, context):
        """
        Generate highly personalized coaching nudges based on user profile and context
        """
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Update context awareness
        self.update_context_factors(context)
        
        # Select optimal intervention based on multiple factors
        intervention = self.select_intervention(
            personality_config,
            self.context_factors,
            user_profile['goals']
        )
        
        return self.format_nudge(intervention, personality_config)

    def update_context_factors(self, context):
        """
        Update contextual awareness based on current situation
        """
        self.context_factors.update({
            'time_of_day': context.get('time'),
            'energy_level': self.assess_energy_level(context),
            'task_complexity': context.get('task_complexity'),
            'environment': context.get('environment'),
            'recent_performance': context.get('performance_history')
        })

    def select_intervention(self, personality_config, context, goals):
        """
        Select the most appropriate intervention based on multiple factors
        """
        intervention = {
            'type': self.determine_intervention_type(context, goals),
            'intensity': self.calculate_intensity(context),
            'timing': self.optimize_timing(context),
            'content': self.generate_content(personality_config, goals)
        }
        
        return intervention

    def determine_intervention_type(self, context, goals):
        """
        Determine the most effective type of intervention for current context
        """
        if context['energy_level'] == 'low':
            return 'micro_action'
        elif context['task_complexity'] == 'high':
            return 'step_by_step_guidance'
        else:
            return 'motivation_boost'

    def calculate_intensity(self, context):
        """
        Calculate appropriate intervention intensity based on context
        """
        factors = {
            'time_pressure': context.get('time_pressure', 0.5),
            'task_importance': context.get('task_importance', 0.5),
            'user_receptivity': context.get('user_receptivity', 0.5)
        }
        
        return sum(factors.values()) / len(factors)

    def optimize_timing(self, context):
        """
        Optimize intervention timing based on user patterns and context
        """
        return {
            'optimal_time': self.predict_optimal_time(context),
            'frequency': self.calculate_frequency(context),
            'duration': self.determine_duration(context)
        }

    def generate_content(self, personality_config, goals):
        """
        Generate personalized content based on personality and goals
        """
        return {
            'message': self.craft_message(personality_config),
            'actions': self.specify_actions(goals),
            'support_material': self.gather_resources(personality_config)
        }

    def format_nudge(self, intervention, personality_config):
        """
        Format the intervention according to user's communication preferences
        """
        style = personality_config['communication_pref']
        
        formatted_nudge = {
            'message': self.apply_communication_style(intervention['content']['message'], style),
            'actions': intervention['content']['actions'],
            'timing': intervention['timing'],
            'intensity': intervention['intensity'],
            'support': intervention['content']['support_material']
        }
        
        return formatted_nudge

    def track_effectiveness(self, nudge_id, user_response):
        """
        Track and analyze the effectiveness of interventions
        """
        self.user_metrics['recommendation_adherence'] = self.calculate_adherence(user_response)
        self.user_metrics['behavior_change_rate'] = self.measure_behavior_change(user_response)
        self.user_metrics['satisfaction_score'] = self.assess_satisfaction(user_response)
        
        self.update_progress_markers(nudge_id, user_response)
        
        return self.user_metrics

    def adapt_strategy(self, effectiveness_metrics):
        """
        Adapt coaching strategy based on effectiveness metrics
        """
        if effectiveness_metrics['satisfaction_score'] < 0.7:
            self.adjust_communication_style()
        if effectiveness_metrics['behavior_change_rate'] < 0.5:
            self.intensify_interventions()
        if effectiveness_metrics['recommendation_adherence'] < 0.6:
            self.simplify_actions()