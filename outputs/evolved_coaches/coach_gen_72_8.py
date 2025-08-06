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
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Enable focus mode', 'time_est': '1 min'},
                    {'step': 'Set timer for focused work', 'time_est': '1 min'}
                ],
                'success_metrics': ['time_on_task', 'task_completion'],
                'follow_up_interval': 30 # minutes
            },
            'productivity': {
                'triggers': ['procrastination', 'low_output'],
                'actions': [
                    {'step': 'Break task into smaller chunks', 'time_est': '5 min'},
                    {'step': 'Set SMART goals', 'time_est': '10 min'},
                    {'step': 'Schedule focused work blocks', 'time_est': '5 min'}
                ],
                'success_metrics': ['tasks_completed', 'quality_score'],
                'follow_up_interval': 60
            }
            # Additional templates...
        }

        self.behavioral_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'rewards'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof']
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate cognitive load and attention state
        current_load = self._assess_cognitive_load(user_context)
        attention_capacity = self._evaluate_attention_state(user_context)

        # Select appropriate intervention based on context
        if current_load > config['cognitive_load_threshold']:
            return self._generate_load_reduction_nudge(config)
        
        intervention = self._select_intervention(user_context, config)
        
        # Personalize delivery style
        intervention = self._adapt_communication_style(intervention, config['communication_pref'])
        
        # Add behavioral reinforcement
        intervention = self._add_behavioral_elements(intervention, config['motivation_triggers'])
        
        return intervention

    def _assess_cognitive_load(self, context):
        """Evaluate current cognitive load based on context"""
        load_factors = {
            'active_tasks': context.get('num_active_tasks', 0) * 0.2,
            'time_pressure': context.get('deadline_proximity', 0) * 0.3,
            'task_complexity': context.get('task_difficulty', 0) * 0.3,
            'interruptions': context.get('interruption_frequency', 0) * 0.2
        }
        return sum(load_factors.values())

    def _evaluate_attention_state(self, context):
        """Assess current attention capacity"""
        attention_factors = {
            'time_since_break': context.get('minutes_since_break', 0),
            'focus_duration': context.get('continuous_focus_time', 0),
            'energy_level': context.get('energy_indicator', 0.5)
        }
        return self._calculate_attention_score(attention_factors)

    def _select_intervention(self, context, config):
        """Select most appropriate intervention template"""
        relevant_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                relevance_score = self._calculate_relevance(template, context, config)
                relevant_templates.append((template_name, relevance_score))
        
        best_template = max(relevant_templates, key=lambda x: x[1])[0]
        return self.intervention_templates[best_template]

    def _adapt_communication_style(self, intervention, comm_style):
        """Adapt intervention language and format to user's preferred style"""
        if comm_style == 'direct':
            intervention['tone'] = 'concise'
            intervention['format'] = 'bullet_points'
        elif comm_style == 'enthusiastic':
            intervention['tone'] = 'encouraging'
            intervention['format'] = 'narrative'
        return intervention

    def _add_behavioral_elements(self, intervention, motivation_triggers):
        """Add behavioral psychology elements to intervention"""
        for trigger in motivation_triggers:
            if trigger == 'mastery':
                intervention['progress_tracking'] = True
                intervention['skill_development'] = True
            elif trigger == 'autonomy':
                intervention['choice_options'] = True
                intervention['customization'] = True
            elif trigger == 'social_connection':
                intervention['social_proof'] = True
                intervention['peer_comparison'] = True
        return intervention

    def _calculate_relevance(self, template, context, config):
        """Calculate contextual relevance score"""
        relevance_factors = {
            'trigger_match': 0.4,
            'timing_fit': 0.3,
            'user_preferences': 0.3
        }
        
        scores = {
            'trigger_match': self._score_trigger_match(template, context),
            'timing_fit': self._score_timing_fit(template, context),
            'user_preferences': self._score_preference_match(template, config)
        }
        
        return sum(score * weight for factor, (score, weight) 
                  in zip(scores.keys(), relevance_factors.items()))

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for effectiveness tracking
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation for user model updates
        pass