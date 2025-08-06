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
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'specifics': 'Clear workspace of distractions'},
                    {'type': 'technique', 'duration': 25, 'specifics': 'Use Pomodoro timer'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful pause'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into smaller chunks'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'type': 'achievement_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

        # User adaptation tracking
        self.user_profile = {
            'intervention_response': {},
            'success_patterns': {},
            'challenge_areas': {},
            'progress_metrics': {},
            'preference_learning': {}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized coaching nudge"""
        
        # Update context awareness
        self.update_context(user_context)
        
        # Select appropriate intervention based on context
        intervention = self.select_intervention(personality_type)
        
        # Personalize based on user profile
        personalized_actions = self.personalize_actions(intervention, personality_type)
        
        # Apply behavioral psychology principles
        enhanced_nudge = self.apply_behavioral_principles(personalized_actions)
        
        # Add specific metrics and success criteria
        actionable_nudge = self.add_actionability(enhanced_nudge)
        
        return actionable_nudge

    def update_context(self, user_context):
        """Update context awareness parameters"""
        for factor in self.context_factors:
            if factor in user_context:
                self.context_factors[factor] = user_context[factor]

    def select_intervention(self, personality_type):
        """Select most appropriate intervention template"""
        user_config = self.personality_type_configs[personality_type]
        
        # Match intervention to user's current context and preferences
        best_intervention = None
        max_score = 0
        
        for template_name, template in self.intervention_templates.items():
            score = self.calculate_intervention_fit(template, user_config)
            if score > max_score:
                max_score = score
                best_intervention = template
                
        return best_intervention

    def personalize_actions(self, intervention, personality_type):
        """Customize intervention actions for user"""
        user_config = self.personality_type_configs[personality_type]
        
        personalized = {
            'actions': [],
            'timing': intervention['follow_up']['timing'],
            'style': user_config['communication_pref']
        }
        
        for action in intervention['actions']:
            modified_action = self.adapt_action_to_user(action, user_config)
            personalized['actions'].append(modified_action)
            
        return personalized

    def apply_behavioral_principles(self, intervention):
        """Apply psychological principles to strengthen intervention"""
        enhanced = intervention.copy()
        
        # Add motivation triggers
        enhanced['motivation_elements'] = self.select_motivation_triggers()
        
        # Add habit formation elements
        enhanced['habit_elements'] = self.create_habit_loop()
        
        # Add engagement mechanics
        enhanced['engagement_elements'] = self.add_engagement_features()
        
        return enhanced

    def add_actionability(self, intervention):
        """Add specific metrics and success criteria"""
        actionable = intervention.copy()
        
        for action in actionable['actions']:
            action['success_metrics'] = self.define_success_metrics(action)
            action['implementation_steps'] = self.create_implementation_steps(action)
            action['progress_tracking'] = self.setup_progress_tracking(action)
            
        return actionable

    def calculate_intervention_fit(self, template, user_config):
        """Calculate how well an intervention matches user needs"""
        fit_score = 0
        
        # Consider learning style match
        if template['type'] == user_config['learning_style']:
            fit_score += 1
            
        # Consider cognitive load
        if self.estimate_cognitive_load(template) <= user_config['cognitive_load_threshold']:
            fit_score += 1
            
        # Consider timing appropriateness
        if self.is_timing_appropriate(template):
            fit_score += 1
            
        return fit_score

    def adapt_action_to_user(self, action, user_config):
        """Customize action based on user preferences"""
        adapted = action.copy()
        
        # Adjust communication style
        adapted['presentation'] = user_config['communication_pref']
        
        # Modify duration based on work pattern
        adapted['duration'] = self.adjust_duration(action['duration'], user_config['work_pattern'])
        
        # Add personalized motivation elements
        adapted['motivation'] = self.select_motivation_triggers(user_config['motivation_triggers'])
        
        return adapted

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        if intervention_id not in self.user_profile['intervention_response']:
            self.user_profile['intervention_response'][intervention_id] = []
            
        self.user_profile['intervention_response'][intervention_id].append(user_response)
        
        # Update success patterns
        self.update_success_patterns(intervention_id, user_response)
        
        # Adjust user profile based on response
        self.adapt_user_profile(user_response)