class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
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
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'type': 'environment', 'duration': 5, 'impact': 0.7},
                    {'type': 'timeblock', 'duration': 25, 'impact': 0.8},
                    {'type': 'mindfulness', 'duration': 3, 'impact': 0.6}
                ],
                'follow_up': {'timing': 30, 'type': 'check_progress'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy'],
                'actions': [
                    {'type': 'goal_reminder', 'duration': 2, 'impact': 0.6},
                    {'type': 'small_win', 'duration': 10, 'impact': 0.7},
                    {'type': 'accountability', 'duration': 5, 'impact': 0.8}
                ],
                'follow_up': {'timing': 15, 'type': 'reinforcement'}
            }
            # Additional templates...
        }

        self.behavioral_metrics = {
            'engagement': 0.0,
            'completion_rate': 0.0,
            'satisfaction': 0.0,
            'behavioral_change': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current cognitive load
        cognitive_load = self._assess_cognitive_load(user_context)
        
        # Select appropriate intervention
        if cognitive_load > user_config['cognitive_load_threshold']:
            intervention = self._generate_light_intervention(user_context)
        else:
            intervention = self._generate_full_intervention(user_context, user_config)

        # Enhance with personality-specific motivators
        intervention = self._add_motivation_elements(intervention, user_config['motivation_triggers'])
        
        return self._format_intervention(intervention, user_config['communication_pref'])

    def _assess_cognitive_load(self, context):
        """Evaluate current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3),
            'fatigue_level': context.get('fatigue', 0.4)
        }
        return sum(factors.values()) / len(factors)

    def _generate_light_intervention(self, context):
        """Generate minimal intervention for high cognitive load"""
        return {
            'type': 'micro_break',
            'duration': 2,
            'action': 'Take a deep breath and reset',
            'expected_impact': 0.4
        }

    def _generate_full_intervention(self, context, user_config):
        """Generate complete intervention based on context"""
        
        # Select most relevant template
        template = self._select_best_template(context)
        
        # Customize actions based on user preferences
        actions = self._customize_actions(template['actions'], user_config)
        
        return {
            'type': template['type'],
            'actions': actions,
            'duration': sum(a['duration'] for a in actions),
            'expected_impact': max(a['impact'] for a in actions),
            'follow_up': template['follow_up']
        }

    def _add_motivation_elements(self, intervention, motivation_triggers):
        """Add personalized motivation elements"""
        motivation_enhancers = {
            'mastery': {'type': 'progress_tracking', 'impact': 0.3},
            'autonomy': {'type': 'choice_provision', 'impact': 0.4},
            'social_connection': {'type': 'peer_comparison', 'impact': 0.3},
            'achievement': {'type': 'milestone_celebration', 'impact': 0.4}
        }
        
        selected_enhancers = [motivation_enhancers[t] for t in motivation_triggers if t in motivation_enhancers]
        intervention['motivation_elements'] = selected_enhancers
        
        return intervention

    def _format_intervention(self, intervention, communication_style):
        """Format intervention according to communication preference"""
        
        style_formats = {
            'direct': {'prefix': '', 'suffix': ''},
            'enthusiastic': {'prefix': '💪 ', 'suffix': ' 🎯'},
            'supportive': {'prefix': 'Consider ', 'suffix': ' 😊'}
        }
        
        format_style = style_formats.get(communication_style, style_formats['direct'])
        
        return {
            **intervention,
            'message': f"{format_style['prefix']}{intervention['action']}{format_style['suffix']}"
        }

    def track_effectiveness(self, intervention_id, user_response):
        """Track and update intervention effectiveness"""
        self.behavioral_metrics['engagement'] = (
            self.behavioral_metrics['engagement'] * 0.9 + user_response['engagement'] * 0.1
        )
        self.behavioral_metrics['completion_rate'] = (
            self.behavioral_metrics['completion_rate'] * 0.9 + user_response['completed'] * 0.1
        )
        self.behavioral_metrics['satisfaction'] = (
            self.behavioral_metrics['satisfaction'] * 0.9 + user_response['satisfaction'] * 0.1
        )
        self.behavioral_metrics['behavioral_change'] = (
            self.behavioral_metrics['behavioral_change'] * 0.9 + user_response['behavior_change'] * 0.1
        )

        return self.behavioral_metrics