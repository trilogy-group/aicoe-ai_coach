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
                    {'type': 'environment', 'duration': 5, 'priority': 1,
                     'description': 'Clear visible distractions from workspace',
                     'success_metric': 'Workspace clarity score'},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'description': 'Use Pomodoro technique: 25min focused work',
                     'success_metric': 'Complete Pomodoro cycles'}
                ]
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy'],
                'actions': [
                    {'type': 'reframe', 'duration': 3, 'priority': 1,
                     'description': 'Break task into 3 smaller achievable steps',
                     'success_metric': 'Task completion rate'},
                    {'type': 'energize', 'duration': 5, 'priority': 2,
                     'description': 'Take a brief walk or stretching break',
                     'success_metric': 'Energy level rating'}
                ]
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking'],
            'habit_formation': ['trigger_identification', 'routine_design'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'cognitive_load': ['chunking', 'spacing', 'interleaving']
        }

        self.user_context = {}
        self.intervention_history = []
        self.effectiveness_metrics = {}

    def analyze_user_context(self, user_data):
        """Analyze user context and state for personalized interventions"""
        context = {
            'personality_type': user_data.get('personality_type'),
            'current_task': user_data.get('current_task'),
            'energy_level': user_data.get('energy_level', 0.5),
            'focus_level': user_data.get('focus_level', 0.5),
            'cognitive_load': user_data.get('cognitive_load', 0.0),
            'time_of_day': user_data.get('timestamp').hour,
            'recent_breaks': user_data.get('breaks_taken', []),
            'task_progress': user_data.get('task_progress', 0.0)
        }
        
        self.user_context = context
        return context

    def generate_intervention(self, context_data):
        """Generate personalized intervention based on context"""
        personality = self.personality_type_configs[context_data['personality_type']]
        
        # Select appropriate intervention based on context
        if context_data['cognitive_load'] > personality['cognitive_load_threshold']:
            intervention_type = 'focus'
        elif context_data['energy_level'] < 0.4:
            intervention_type = 'motivation'
        
        # Get base intervention
        intervention = self.intervention_templates[intervention_type].copy()
        
        # Personalize based on personality and context
        intervention['actions'] = self._personalize_actions(
            intervention['actions'],
            personality,
            context_data
        )
        
        # Add behavioral principles
        intervention['principles'] = self._apply_behavior_principles(context_data)
        
        return intervention

    def _personalize_actions(self, actions, personality, context):
        """Personalize action steps based on user traits and context"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            
            # Adjust duration based on cognitive load
            if context['cognitive_load'] > 0.7:
                modified_action['duration'] *= 0.8
            
            # Modify communication style
            modified_action['description'] = self._adapt_communication(
                modified_action['description'],
                personality['communication_pref']
            )
            
            # Add personalized success metrics
            modified_action['success_metric'] = self._personalize_metric(
                modified_action['success_metric'],
                personality['learning_style']
            )
            
            personalized.append(modified_action)
            
        return personalized

    def _apply_behavior_principles(self, context):
        """Apply relevant behavioral psychology principles"""
        principles = []
        
        if context['focus_level'] < 0.5:
            principles.extend(self.behavior_principles['cognitive_load'])
        
        if context['task_progress'] < 0.3:
            principles.extend(self.behavior_principles['motivation'])
            
        return principles

    def _adapt_communication(self, message, style):
        """Adapt communication style based on personality preference"""
        if style == 'direct':
            return message.strip().split(':')[-1]
        elif style == 'enthusiastic':
            return f"Great opportunity: {message}!"
        return message

    def _personalize_metric(self, metric, learning_style):
        """Personalize success metrics based on learning style"""
        if learning_style == 'systematic':
            return f"Quantitative {metric}"
        elif learning_style == 'exploratory':
            return f"Qualitative assessment of {metric}"
        return metric

    def track_effectiveness(self, intervention_id, metrics):
        """Track intervention effectiveness"""
        self.effectiveness_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion_rate', 0.0),
            'satisfaction': metrics.get('satisfaction', 0.0),
            'behavior_change': metrics.get('behavior_change', 0.0),
            'relevance': metrics.get('relevance', 0.0)
        }

    def update_intervention_history(self, intervention):
        """Update intervention history and patterns"""
        self.intervention_history.append({
            'timestamp': intervention.get('timestamp'),
            'type': intervention.get('type'),
            'effectiveness': intervention.get('effectiveness', 0.0)
        })