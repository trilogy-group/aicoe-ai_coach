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
                    {'type': 'environment', 'duration': 5, 'priority': 1,
                     'description': 'Clear visible distractions from workspace'},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'description': 'Use Pomodoro technique: 25 min focus + 5 min break'}
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy'],
                'actions': [
                    {'type': 'reframe', 'duration': 2, 'priority': 1,
                     'description': 'Break task into smaller 15-minute segments'},
                    {'type': 'reward', 'duration': 1, 'priority': 2,
                     'description': 'Define specific reward for completion'}
                ],
                'follow_up': {'timing': 15, 'type': 'progress_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # Performance tracking
        self.user_metrics = {
            'intervention_success': [],
            'behavioral_changes': [],
            'satisfaction_scores': [],
            'completion_rates': []
        }

    def generate_personalized_intervention(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        
        # Get personality-specific configurations
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze cognitive load and attention state
        cognitive_load = self._assess_cognitive_load(user_context)
        attention_state = self._analyze_attention_patterns(user_context)

        # Select appropriate intervention template
        template = self._select_intervention_template(
            cognitive_load,
            attention_state,
            user_config
        )

        # Personalize actions based on user preferences
        personalized_actions = self._personalize_actions(
            template['actions'],
            user_config,
            user_context
        )

        # Add behavioral psychology elements
        enhanced_intervention = self._enhance_with_behavioral_science(
            personalized_actions,
            user_config['motivation_triggers']
        )

        return enhanced_intervention

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        # Implementation of cognitive load assessment
        load_factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3)
        }
        return sum(load_factors.values()) / len(load_factors)

    def _analyze_attention_patterns(self, context):
        """Analyze user attention patterns"""
        # Implementation of attention pattern analysis
        return {
            'focus_duration': context.get('focus_duration', 0),
            'distraction_frequency': context.get('distraction_frequency', 0),
            'task_switching_rate': context.get('task_switching_rate', 0)
        }

    def _select_intervention_template(self, cognitive_load, attention_state, user_config):
        """Select appropriate intervention template based on state"""
        if cognitive_load > user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        return self.intervention_templates['motivation']

    def _personalize_actions(self, actions, user_config, context):
        """Personalize intervention actions"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = user_config['communication_pref']
            modified_action['learning_approach'] = user_config['learning_style']
            modified_action['timing'] = self._optimize_timing(context)
            personalized.append(modified_action)
        return personalized

    def _enhance_with_behavioral_science(self, actions, motivation_triggers):
        """Add behavioral psychology elements to intervention"""
        enhanced = {
            'actions': actions,
            'behavioral_elements': {
                'motivation_hooks': motivation_triggers,
                'habit_formation': self.behavioral_triggers['habit_formation'],
                'engagement_factors': self.behavioral_triggers['engagement']
            },
            'success_metrics': {
                'completion': 'binary',
                'effort': 'scale_1_5',
                'satisfaction': 'scale_1_10'
            }
        }
        return enhanced

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        # Implementation of timing optimization
        return {
            'preferred_time': context.get('peak_productivity_time'),
            'frequency': context.get('intervention_frequency'),
            'duration': context.get('optimal_duration')
        }

    def track_intervention_success(self, intervention_id, metrics):
        """Track success of interventions"""
        self.user_metrics['intervention_success'].append({
            'id': intervention_id,
            'metrics': metrics
        })

    def update_user_profile(self, user_id, new_metrics):
        """Update user profile with new performance metrics"""
        # Implementation of user profile updates
        pass