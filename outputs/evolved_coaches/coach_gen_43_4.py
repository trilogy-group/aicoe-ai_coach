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
                'motivation_triggers': ['novelty', 'social', 'creativity'],
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
                'follow_up_interval': 25 # minutes
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines'],
                'actions': [
                    {'step': 'Break down project into tasks', 'time_est': '10 min'},
                    {'step': 'Prioritize tasks (1-3)', 'time_est': '5 min'},
                    {'step': 'Schedule work blocks', 'time_est': '5 min'}
                ],
                'success_metrics': ['tasks_scheduled', 'deadlines_met'],
                'follow_up_interval': 60
            }
            # Additional templates...
        }

        self.behavioral_techniques = {
            'habit_formation': ['implementation_intentions', 'habit_stacking', 'temptation_bundling'],
            'motivation': ['goal_setting', 'progress_tracking', 'reward_scheduling'],
            'focus': ['pomodoro', 'timeboxing', 'deep_work']
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant coaching intervention"""
        user_config = self.personality_type_configs[personality_type]
        
        # Assess cognitive load and attention state
        cognitive_load = self._assess_cognitive_load(user_context)
        attention_state = self._assess_attention_state(user_context)
        
        # Select appropriate intervention based on context
        if cognitive_load > user_config['cognitive_load_threshold']:
            intervention = self._generate_load_reduction_intervention()
        else:
            intervention = self._select_optimal_intervention(user_context, user_config)

        # Personalize communication style
        intervention = self._personalize_communication(intervention, user_config['communication_pref'])
        
        return intervention

    def _assess_cognitive_load(self, context):
        """Estimate current cognitive load based on context"""
        load_factors = {
            'num_open_apps': 0.1,
            'task_complexity': 0.3,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2,
            'fatigue_level': 0.1
        }
        
        cognitive_load = sum(load_factors[factor] * context.get(factor, 0) for factor in load_factors)
        return min(cognitive_load, 1.0)

    def _assess_attention_state(self, context):
        """Determine current attention state and focus level"""
        attention_metrics = {
            'time_on_task': context.get('time_on_task', 0),
            'task_switches': context.get('task_switches', 0),
            'focus_duration': context.get('focus_duration', 0)
        }
        
        return self._calculate_attention_score(attention_metrics)

    def _select_optimal_intervention(self, context, user_config):
        """Select most appropriate intervention based on context and user preferences"""
        relevant_templates = self._filter_relevant_templates(context)
        scored_templates = self._score_templates(relevant_templates, user_config)
        
        return max(scored_templates, key=lambda x: x['score'])

    def _generate_load_reduction_intervention(self):
        """Create intervention to reduce cognitive load"""
        return {
            'type': 'load_reduction',
            'actions': [
                {'step': 'Close unnecessary applications', 'time_est': '2 min'},
                {'step': 'Take a 5-minute break', 'time_est': '5 min'},
                {'step': 'Review and reprioritize tasks', 'time_est': '3 min'}
            ],
            'priority': 'high'
        }

    def _personalize_communication(self, intervention, comm_style):
        """Adapt intervention language to user's preferred communication style"""
        style_templates = {
            'direct': {'prefix': '', 'tone': 'straightforward'},
            'enthusiastic': {'prefix': "Let's", 'tone': 'energetic'},
            'supportive': {'prefix': 'Consider', 'tone': 'encouraging'}
        }
        
        template = style_templates[comm_style]
        intervention['tone'] = template['tone']
        intervention['message'] = f"{template['prefix']} {intervention['message']}"
        
        return intervention

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        metrics = {
            'user_engagement': user_response.get('engagement_level', 0),
            'action_completion': user_response.get('completed_actions', 0),
            'perceived_value': user_response.get('satisfaction', 0)
        }
        
        self._update_intervention_stats(intervention_id, metrics)
        return self._generate_effectiveness_report(metrics)

    def adapt_to_feedback(self, feedback_data):
        """Adapt coaching strategies based on feedback"""
        for metric, value in feedback_data.items():
            if value < 0.6:  # Threshold for adaptation
                self._adjust_strategy(metric)