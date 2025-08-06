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
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Set timer for focused work', 'time_est': '25 min'},
                    {'step': 'Take structured break', 'time_est': '5 min'}
                ],
                'success_metrics': ['focused_time', 'task_completion'],
                'priority': 'high'
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into smaller chunks', 'time_est': '5 min'},
                    {'step': 'Set specific mini-goals', 'time_est': '3 min'},
                    {'step': 'Schedule rewards for completion', 'time_est': '2 min'}
                ],
                'success_metrics': ['task_initiation', 'goal_achievement'],
                'priority': 'medium'
            }
            # Additional intervention types
        }

        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_score': 1.0,
            'recent_interventions': [],
            'intervention_outcomes': {}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        
        # Get personality-specific configurations
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Analyze current context
        cognitive_load = self._assess_cognitive_load(current_context)
        optimal_timing = self._check_intervention_timing()
        
        if not optimal_timing or cognitive_load > personality_config['cognitive_load_threshold']:
            return None

        # Select most relevant intervention
        intervention = self._select_intervention(
            personality_config,
            current_context,
            self.user_context
        )

        # Personalize intervention content
        personalized_content = self._personalize_content(
            intervention,
            personality_config,
            user_profile
        )

        # Track intervention
        self._log_intervention(intervention, current_context)

        return personalized_content

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'open_tasks': min(context.get('open_tasks', 0) / 10, 1.0),
            'interruptions': min(context.get('interruptions_per_hour', 0) / 20, 1.0),
            'time_pressure': context.get('deadline_proximity', 0.0)
        }
        return sum(factors.values()) / len(factors)

    def _check_intervention_timing(self):
        """Check if timing is appropriate for intervention"""
        recent_interventions = self.user_context['recent_interventions']
        if len(recent_interventions) > 0:
            time_since_last = time.time() - recent_interventions[-1]
            if time_since_last < 1800:  # 30 minutes
                return False
        return True

    def _select_intervention(self, personality_config, current_context, user_context):
        """Select most appropriate intervention based on context and history"""
        
        # Score each intervention type
        intervention_scores = {}
        for intervention_type, template in self.intervention_templates.items():
            score = self._calculate_intervention_score(
                template,
                personality_config,
                current_context,
                user_context
            )
            intervention_scores[intervention_type] = score

        # Return highest scoring intervention
        return max(intervention_scores.items(), key=lambda x: x[1])[0]

    def _calculate_intervention_score(self, template, personality_config, current_context, user_context):
        """Calculate appropriateness score for an intervention"""
        
        relevance_score = sum(1 for trigger in template['triggers'] 
                            if current_context.get(trigger, False))
        
        effectiveness_score = self._get_historical_effectiveness(
            template,
            user_context['intervention_outcomes']
        )

        personality_match = self._calculate_personality_match(
            template,
            personality_config
        )

        return (relevance_score * 0.4 + 
                effectiveness_score * 0.3 + 
                personality_match * 0.3)

    def _personalize_content(self, intervention, personality_config, user_profile):
        """Personalize intervention content for user"""
        template = self.intervention_templates[intervention]
        
        # Adjust language style
        communication_style = personality_config['communication_pref']
        
        # Build personalized content
        content = {
            'title': self._adapt_text(template['title'], communication_style),
            'actions': [
                {
                    'step': self._adapt_text(action['step'], communication_style),
                    'time_est': action['time_est']
                }
                for action in template['actions']
            ],
            'motivation': self._generate_motivation_message(
                personality_config['motivation_triggers']
            ),
            'success_metrics': template['success_metrics'],
            'priority': template['priority']
        }

        return content

    def _log_intervention(self, intervention, context):
        """Log intervention for tracking"""
        self.user_context['recent_interventions'].append(time.time())
        
        # Maintain rolling window of last 10 interventions
        if len(self.user_context['recent_interventions']) > 10:
            self.user_context['recent_interventions'].pop(0)

    def update_intervention_outcome(self, intervention_id, outcome_metrics):
        """Update intervention effectiveness tracking"""
        self.user_context['intervention_outcomes'][intervention_id] = {
            'timestamp': time.time(),
            'metrics': outcome_metrics
        }