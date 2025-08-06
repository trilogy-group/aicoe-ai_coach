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
                    {'type': 'environment', 'duration': 15, 'specifics': 'Clear workspace of distractions'},
                    {'type': 'technique', 'duration': 25, 'specifics': 'Use Pomodoro method'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful pause'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into smaller milestones'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

        # User progress tracking
        self.progress_metrics = {
            'completion_rate': 0.0,
            'engagement_level': 0.0,
            'behavior_change': 0.0,
            'satisfaction': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on context and personality"""
        
        # Update context awareness
        self.update_context(user_context)
        
        # Select appropriate intervention template
        template = self.select_intervention_template()
        
        # Personalize based on personality type
        config = self.personality_type_configs[personality_type]
        
        # Apply behavioral psychology principles
        behavioral_elements = self.apply_behavior_principles(template, config)
        
        # Generate specific actionable steps
        action_steps = self.generate_action_steps(behavioral_elements)
        
        return self.format_nudge(action_steps, config)

    def update_context(self, context):
        """Update context awareness parameters"""
        self.context_factors.update(context)
        self.assess_cognitive_load()
        self.check_intervention_timing()

    def select_intervention_template(self):
        """Select most appropriate intervention template based on context"""
        current_needs = self.analyze_user_needs()
        return self.match_template_to_needs(current_needs)

    def apply_behavior_principles(self, template, config):
        """Apply behavioral psychology principles to intervention"""
        motivation_elements = self.behavior_triggers['motivation']
        habit_elements = self.behavior_triggers['habit_formation']
        
        return {
            'motivation_triggers': [t for t in motivation_elements if t in config['motivation_triggers']],
            'habit_formation': habit_elements,
            'engagement_factors': self.behavior_triggers['engagement']
        }

    def generate_action_steps(self, behavioral_elements):
        """Generate specific, actionable steps"""
        steps = []
        for trigger in behavioral_elements['motivation_triggers']:
            step = {
                'action': self.get_specific_action(trigger),
                'duration': self.estimate_duration(trigger),
                'success_metric': self.define_success_metric(trigger),
                'follow_up': self.create_follow_up_plan(trigger)
            }
            steps.append(step)
        return steps

    def format_nudge(self, action_steps, config):
        """Format nudge according to user's communication preferences"""
        return {
            'style': config['communication_pref'],
            'actions': action_steps,
            'timing': self.optimize_timing(),
            'format': self.adapt_to_cognitive_load(),
            'follow_up': self.schedule_follow_up()
        }

    def track_progress(self, user_response):
        """Track user progress and update metrics"""
        self.progress_metrics['completion_rate'] = self.calculate_completion_rate(user_response)
        self.progress_metrics['engagement_level'] = self.measure_engagement(user_response)
        self.progress_metrics['behavior_change'] = self.assess_behavior_change(user_response)
        self.progress_metrics['satisfaction'] = self.measure_satisfaction(user_response)

    def optimize_timing(self):
        """Optimize intervention timing based on user patterns"""
        return {
            'best_time': self.analyze_peak_periods(),
            'frequency': self.calculate_optimal_frequency(),
            'spacing': self.determine_intervention_spacing()
        }

    def adapt_to_cognitive_load(self):
        """Adapt intervention complexity to current cognitive load"""
        current_load = self.assess_cognitive_load()
        return self.adjust_complexity(current_load)

    def schedule_follow_up(self):
        """Create follow-up schedule for intervention"""
        return {
            'timing': self.calculate_follow_up_timing(),
            'type': self.determine_follow_up_type(),
            'metrics': self.define_follow_up_metrics()
        }