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

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate', 'intermittent', 'social'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose']
        }

        self.user_context = {}
        self.intervention_history = []
        self.success_metrics = {}

    def analyze_user_context(self, user_data):
        """Analyze user context and state for personalized interventions"""
        context = {
            'personality_type': user_data.get('personality_type'),
            'current_task': user_data.get('current_task'),
            'energy_level': user_data.get('energy_level', 0.5),
            'focus_score': user_data.get('focus_score', 0.5),
            'cognitive_load': user_data.get('cognitive_load', 0.5),
            'time_of_day': user_data.get('time_of_day'),
            'recent_achievements': user_data.get('recent_achievements', [])
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
        
        template = self.intervention_templates[intervention_type]
        
        # Personalize actions based on personality
        actions = self._personalize_actions(template['actions'], personality)
        
        intervention = {
            'type': intervention_type,
            'actions': actions,
            'timing': self._optimize_timing(context_data),
            'motivation_hooks': self._get_motivation_hooks(personality),
            'follow_up_schedule': self._create_follow_up_schedule()
        }

        self.intervention_history.append(intervention)
        return intervention

    def _personalize_actions(self, actions, personality):
        """Customize actions based on personality preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality['communication_pref']
            modified_action['pace'] = personality['work_pattern']
            modified_action['format'] = personality['learning_style']
            personalized.append(modified_action)
        return personalized

    def _optimize_timing(self, context):
        """Optimize intervention timing based on context"""
        return {
            'optimal_time': context['time_of_day'],
            'frequency': 'adaptive',
            'spacing': self._calculate_optimal_spacing(context)
        }

    def _get_motivation_hooks(self, personality):
        """Generate motivation hooks based on personality"""
        return {
            'primary_trigger': personality['motivation_triggers'][0],
            'secondary_triggers': personality['motivation_triggers'][1:],
            'reinforcement_type': self._select_reinforcement_type(personality)
        }

    def _create_follow_up_schedule(self):
        """Create follow-up schedule for intervention"""
        return {
            'check_points': [1, 3, 7],  # Days
            'metrics': ['completion', 'effectiveness', 'satisfaction'],
            'adjustment_threshold': 0.7
        }

    def track_effectiveness(self, intervention_id, metrics):
        """Track intervention effectiveness"""
        self.success_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion_rate', 0),
            'behavior_change': metrics.get('behavior_change', 0),
            'user_satisfaction': metrics.get('user_satisfaction', 0),
            'long_term_impact': metrics.get('long_term_impact', 0)
        }
        
        return self._calculate_effectiveness_score(metrics)

    def adapt_strategy(self, effectiveness_data):
        """Adapt intervention strategy based on effectiveness"""
        if effectiveness_data['score'] < 0.7:
            self._adjust_intervention_parameters(effectiveness_data)
        return self._get_updated_strategy()

    def _calculate_effectiveness_score(self, metrics):
        """Calculate overall effectiveness score"""
        weights = {'completion_rate': 0.3, 'behavior_change': 0.3,
                  'user_satisfaction': 0.2, 'long_term_impact': 0.2}
        
        score = sum(metrics[k] * weights[k] for k in weights.keys())
        return {'score': score, 'areas_for_improvement': self._identify_improvement_areas(metrics)}