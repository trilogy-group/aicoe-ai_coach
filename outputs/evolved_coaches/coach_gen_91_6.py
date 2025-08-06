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
                    {'description': 'Enable focus mode for 25 minutes',
                     'duration': 25,
                     'success_metric': 'continuous_focus_time'},
                    {'description': 'Clear desktop and close unnecessary tabs',
                     'duration': 5,
                     'success_metric': 'reduced_open_windows'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'productivity': {
                'triggers': ['low_output', 'procrastination'],
                'actions': [
                    {'description': 'Break task into 15-minute segments',
                     'duration': 5,
                     'success_metric': 'task_completion_rate'},
                    {'description': 'Set 3 specific mini-goals',
                     'duration': 10,
                     'success_metric': 'goals_achieved'}
                ],
                'follow_up': {'timing': 60, 'type': 'achievement_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_state': 'fresh',
            'recent_interventions': [],
            'success_metrics': {}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized coaching intervention based on user profile and context"""
        
        # Get personality-specific configurations
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Assess current cognitive load and attention state
        cognitive_load = self._assess_cognitive_load(current_context)
        attention_capacity = self._calculate_attention_capacity(
            cognitive_load, 
            personality_config['cognitive_load_threshold']
        )

        # Select appropriate intervention based on context
        intervention = self._select_intervention(
            current_context,
            personality_config,
            attention_capacity
        )

        # Personalize action steps
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            personality_config,
            user_profile['skill_level']
        )

        # Generate motivational framing
        motivation_frame = self._create_motivation_frame(
            personality_config['motivation_triggers'],
            user_profile['goals']
        )

        return {
            'nudge_type': intervention['type'],
            'message': self._format_message(
                intervention,
                personality_config['communication_pref']
            ),
            'actions': personalized_actions,
            'motivation': motivation_frame,
            'follow_up': intervention['follow_up']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruptions': context.get('interruption_frequency', 0.3),
            'task_switching': context.get('task_switching_rate', 0.4)
        }
        return sum(factors.values()) / len(factors)

    def _calculate_attention_capacity(self, cognitive_load, threshold):
        """Calculate available attention capacity"""
        return max(0, threshold - cognitive_load)

    def _select_intervention(self, context, personality_config, attention_capacity):
        """Select most appropriate intervention based on context and capacity"""
        available_interventions = [
            template for template in self.intervention_templates.values()
            if any(trigger in context['triggers'] for trigger in template['triggers'])
        ]
        
        # Filter by attention capacity requirements
        suitable_interventions = [
            intervention for intervention in available_interventions
            if sum(action['duration'] for action in intervention['actions']) <= attention_capacity * 60
        ]

        return max(suitable_interventions, 
                  key=lambda x: self._calculate_intervention_fit(x, personality_config))

    def _personalize_actions(self, actions, personality_config, skill_level):
        """Personalize action steps based on user profile"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['difficulty'] = self._adjust_difficulty(
                action, skill_level
            )
            modified_action['style'] = self._adapt_to_learning_style(
                action, personality_config['learning_style']
            )
            personalized.append(modified_action)
        return personalized

    def _create_motivation_frame(self, triggers, user_goals):
        """Create motivational framing based on psychological triggers"""
        return {
            'primary_trigger': max(triggers, key=lambda t: self._calculate_trigger_relevance(t, user_goals)),
            'reinforcement_type': 'positive' if random.random() > 0.3 else 'negative',
            'goal_alignment': self._align_with_goals(user_goals)
        }

    def _format_message(self, intervention, communication_pref):
        """Format intervention message according to communication preference"""
        templates = {
            'direct': "{action}. Expected outcome: {outcome}",
            'enthusiastic': "Ready to {action}? You'll feel great when {outcome}!",
            'supportive': "Consider {action} - this could help you {outcome}"
        }
        return templates[communication_pref].format(
            action=intervention['description'],
            outcome=intervention['success_metric']
        )

    def update_user_context(self, new_context_data):
        """Update user context with new data"""
        self.user_context.update(new_context_data)
        self._prune_old_interventions()
        self._update_success_metrics()

    def _prune_old_interventions(self):
        """Remove old interventions from tracking"""
        current_time = time.time()
        self.user_context['recent_interventions'] = [
            i for i in self.user_context['recent_interventions']
            if current_time - i['timestamp'] < 3600
        ]

    def _update_success_metrics(self):
        """Update intervention success metrics"""
        for metric in self.user_context['success_metrics']:
            if metric['check_time'] <= time.time():
                self._evaluate_metric_success(metric)