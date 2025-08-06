class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral factors
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
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'priority': 1,
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Enable do-not-disturb']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer for 25 min', 'Work on single task', 'Take 5 min break']}
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframing', 'duration': 10, 'priority': 1,
                     'steps': ['Identify specific barrier', 'Break into smaller steps', 'Set micro-goal']},
                    {'type': 'reward', 'duration': 5, 'priority': 2,
                     'steps': ['Define completion criteria', 'Choose meaningful reward', 'Schedule reward time']}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['implementation_intention', 'habit_stacking', 'environmental_design'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof'],
            'focus': ['attention_management', 'cognitive_load', 'context_switching']
        }

        # User context tracking
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Update context tracking
        self.context_factors.update(context)
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(personality_config, context)
        
        # Personalize action steps
        personalized_actions = self._personalize_actions(intervention['actions'], 
                                                       personality_config,
                                                       context)
        
        return {
            'message': self._format_message(personality_config, intervention),
            'actions': personalized_actions,
            'follow_up': intervention['follow_up']
        }

    def _select_intervention(self, personality_config, context):
        """Select most appropriate intervention based on user context"""
        # Calculate intervention scores based on context match
        intervention_scores = {}
        for name, template in self.intervention_templates.items():
            score = self._calculate_relevance_score(template, context)
            intervention_scores[name] = score
            
        # Select highest scoring intervention
        best_intervention = max(intervention_scores.items(), key=lambda x: x[1])[0]
        return self.intervention_templates[best_intervention]

    def _personalize_actions(self, actions, personality_config, context):
        """Customize action steps based on personality and context"""
        personalized = []
        for action in actions:
            # Adjust duration based on cognitive load threshold
            adjusted_duration = action['duration'] * (1/personality_config['cognitive_load_threshold'])
            
            # Add motivation elements based on personality triggers
            motivation_elements = [
                trigger for trigger in personality_config['motivation_triggers']
                if trigger in self.behavior_triggers['motivation']
            ]
            
            personalized.append({
                **action,
                'duration': adjusted_duration,
                'motivation_elements': motivation_elements,
                'communication_style': personality_config['communication_pref']
            })
            
        return personalized

    def _calculate_relevance_score(self, template, context):
        """Calculate how relevant an intervention is to current context"""
        score = 0
        
        # Check trigger matches
        for trigger in template['triggers']:
            if trigger in context.values():
                score += 1
                
        # Consider time of day appropriateness
        if context['time_of_day'] in self._get_optimal_times(template):
            score += 0.5
            
        # Consider energy level match
        if context['energy_level'] >= self._get_required_energy(template):
            score += 0.5
            
        return score

    def _format_message(self, personality_config, intervention):
        """Format intervention message according to personality preferences"""
        style = personality_config['communication_pref']
        
        templates = {
            'direct': "To improve {focus_area}, complete these specific steps:",
            'enthusiastic': "Ready for a breakthrough in {focus_area}? Let's try these exciting steps!",
            # Additional templates...
        }
        
        return templates[style].format(focus_area=intervention['triggers'][0])

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for effectiveness tracking
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation for user model updates
        pass