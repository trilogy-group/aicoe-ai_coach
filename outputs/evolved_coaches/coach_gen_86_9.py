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
                'follow_up': True
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy'],
                'actions': [
                    {'type': 'goal_reminder', 'duration': 2, 'impact': 0.6},
                    {'type': 'small_win', 'duration': 10, 'impact': 0.7},
                    {'type': 'accountability', 'duration': 5, 'impact': 0.8}
                ],
                'follow_up': True
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
        config = self.personality_type_configs[personality_type]
        
        # Calculate cognitive load and attention state
        cognitive_load = self._assess_cognitive_load(user_context)
        attention_state = self._assess_attention_state(user_context)
        
        # Select appropriate intervention
        if cognitive_load > config['cognitive_load_threshold']:
            intervention = self._generate_focus_intervention(config)
        else:
            intervention = self._generate_motivation_intervention(config)
            
        # Personalize based on learning style and communication preferences
        intervention = self._personalize_intervention(intervention, config)
        
        return intervention

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruptions': context.get('interruptions', 0.3),
            'task_switching': context.get('task_switching', 0.4)
        }
        return sum(factors.values()) / len(factors)

    def _assess_attention_state(self, context):
        """Assess current attention state"""
        factors = {
            'focus_duration': context.get('focus_duration', 0),
            'distraction_level': context.get('distraction_level', 0.5),
            'energy_level': context.get('energy_level', 0.7)
        }
        return sum(factors.values()) / len(factors)

    def _generate_focus_intervention(self, config):
        """Generate focus-oriented intervention"""
        template = self.intervention_templates['focus']
        intervention = {
            'type': 'focus',
            'actions': self._select_actions(template['actions'], config),
            'duration': 25,
            'success_metrics': {
                'focus_time': '25 minutes uninterrupted',
                'task_completion': 'Complete 1 defined task',
                'distraction_count': 'Max 2 interruptions'
            }
        }
        return intervention

    def _generate_motivation_intervention(self, config):
        """Generate motivation-oriented intervention"""
        template = self.intervention_templates['motivation']
        intervention = {
            'type': 'motivation',
            'actions': self._select_actions(template['actions'], config),
            'duration': 15,
            'success_metrics': {
                'task_initiation': 'Start within 5 minutes',
                'progress': 'Complete 25% of task',
                'engagement': 'Maintain focus for 15 minutes'
            }
        }
        return intervention

    def _select_actions(self, available_actions, config):
        """Select appropriate actions based on user configuration"""
        selected = []
        for action in available_actions:
            if action['impact'] > 0.6:
                selected.append({
                    'step': action['type'],
                    'duration': action['duration'],
                    'expected_impact': action['impact'],
                    'adaptation': self._adapt_to_style(action['type'], config)
                })
        return selected

    def _adapt_to_style(self, action_type, config):
        """Adapt action to user's learning and communication style"""
        style_adaptations = {
            'systematic': {'detail_level': 'high', 'structure': 'sequential'},
            'exploratory': {'detail_level': 'moderate', 'structure': 'flexible'}
        }
        return style_adaptations[config['learning_style']]

    def _personalize_intervention(self, intervention, config):
        """Add personal touches based on user preferences"""
        intervention['communication_style'] = config['communication_pref']
        intervention['pacing'] = config['work_pattern']
        intervention['motivation_hooks'] = config['motivation_triggers']
        return intervention

    def track_effectiveness(self, intervention_id, metrics):
        """Track intervention effectiveness"""
        self.behavioral_metrics['engagement'] = metrics.get('engagement', 0)
        self.behavioral_metrics['completion_rate'] = metrics.get('completion_rate', 0)
        self.behavioral_metrics['satisfaction'] = metrics.get('satisfaction', 0)
        self.behavioral_metrics['behavioral_change'] = metrics.get('behavioral_change', 0)
        return self.behavioral_metrics