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
                     'success_metric': 'Workspace organization score'},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'description': 'Use Pomodoro technique: 25 min focus + 5 min break',
                     'success_metric': 'Complete focus sessions'}
                ]
            },
            'productivity': {
                'triggers': ['procrastination', 'low_output'],
                'actions': [
                    {'type': 'planning', 'duration': 10, 'priority': 1,
                     'description': 'Break task into smaller 30-min chunks',
                     'success_metric': 'Task completion rate'},
                    {'type': 'accountability', 'duration': 5, 'priority': 2,
                     'description': 'Share progress with accountability partner',
                     'success_metric': 'Regular check-ins completed'}
                ]
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_rewards'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof']
        }

        self.user_context = {}
        self.intervention_history = []
        self.success_metrics = {}

    def analyze_user_context(self, user_data):
        """Analyze user context and current state"""
        context = {
            'personality_type': user_data.get('personality_type'),
            'current_task': user_data.get('current_task'),
            'energy_level': user_data.get('energy_level', 0.0),
            'focus_level': user_data.get('focus_level', 0.0),
            'cognitive_load': user_data.get('cognitive_load', 0.0),
            'time_of_day': user_data.get('time_of_day'),
            'environment': user_data.get('environment', {})
        }
        
        self.user_context = context
        return context

    def generate_intervention(self, context):
        """Generate personalized intervention based on context"""
        personality_config = self.personality_type_configs.get(
            context['personality_type'], self.personality_type_configs['INTJ']
        )

        # Select appropriate intervention based on context
        if context['cognitive_load'] > personality_config['cognitive_load_threshold']:
            intervention_type = 'focus'
        elif context['energy_level'] < 0.4:
            intervention_type = 'productivity'
        
        intervention = self.intervention_templates[intervention_type]
        
        # Personalize actions based on personality and context
        personalized_actions = []
        for action in intervention['actions']:
            personalized_action = self._personalize_action(
                action, personality_config, context
            )
            personalized_actions.append(personalized_action)

        return {
            'type': intervention_type,
            'actions': personalized_actions,
            'timing': self._optimize_timing(context),
            'motivation_elements': self._add_motivation_elements(personality_config)
        }

    def _personalize_action(self, action, personality_config, context):
        """Personalize action based on user characteristics"""
        personalized = action.copy()
        
        # Adjust duration based on energy level
        if context['energy_level'] < 0.5:
            personalized['duration'] *= 0.8
            
        # Modify description based on communication preference
        if personality_config['communication_pref'] == 'direct':
            personalized['description'] = f"ACTION REQUIRED: {action['description']}"
        
        # Add learning style specific elements
        if personality_config['learning_style'] == 'systematic':
            personalized['steps'] = self._break_into_steps(action['description'])
            
        return personalized

    def _optimize_timing(self, context):
        """Optimize intervention timing"""
        return {
            'optimal_time': self._calculate_optimal_time(context),
            'frequency': self._calculate_frequency(context),
            'duration': self._calculate_duration(context)
        }

    def _add_motivation_elements(self, personality_config):
        """Add personalized motivation elements"""
        return {
            'triggers': personality_config['motivation_triggers'],
            'reinforcement': self.behavior_principles['reinforcement'],
            'social_proof': self._generate_social_proof()
        }

    def track_intervention_success(self, intervention_id, metrics):
        """Track success metrics for interventions"""
        self.success_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion_rate', 0.0),
            'user_satisfaction': metrics.get('user_satisfaction', 0.0),
            'behavior_change': metrics.get('behavior_change', 0.0),
            'timestamp': metrics.get('timestamp')
        }

    def adapt_strategy(self):
        """Adapt coaching strategy based on success metrics"""
        if self.success_metrics:
            avg_completion = sum(m['completion_rate'] for m in self.success_metrics.values()) / len(self.success_metrics)
            if avg_completion < 0.5:
                self._adjust_difficulty_level('decrease')
            elif avg_completion > 0.8:
                self._adjust_difficulty_level('increase')

    def _break_into_steps(self, description):
        """Break action into detailed steps"""
        # Implementation for breaking down actions
        pass

    def _calculate_optimal_time(self, context):
        """Calculate optimal intervention timing"""
        # Implementation for timing optimization
        pass

    def _calculate_frequency(self, context):
        """Calculate optimal intervention frequency"""
        # Implementation for frequency calculation
        pass

    def _calculate_duration(self, context):
        """Calculate optimal intervention duration"""
        # Implementation for duration calculation
        pass

    def _generate_social_proof(self):
        """Generate relevant social proof examples"""
        # Implementation for social proof generation
        pass

    def _adjust_difficulty_level(self, direction):
        """Adjust intervention difficulty"""
        # Implementation for difficulty adjustment
        pass