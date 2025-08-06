class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning patterns
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
                'motivation_triggers': ['novelty', 'connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'difficulty': 'easy'},
                    {'step': 'Enable focus mode for 25 minutes',
                     'time_estimate': '25 min', 
                     'difficulty': 'medium'},
                    {'step': 'Take a 5 minute break',
                     'time_estimate': '5 min',
                     'difficulty': 'easy'}
                ],
                'success_metrics': ['focused_time', 'task_completion'],
                'follow_up_timing': 30 # minutes
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into smaller chunks',
                     'time_estimate': '5 min',
                     'difficulty': 'medium'},
                    {'step': 'Set specific mini-goal',
                     'time_estimate': '2 min',
                     'difficulty': 'easy'},
                    {'step': 'Schedule reward after completion',
                     'time_estimate': '1 min', 
                     'difficulty': 'easy'}
                ],
                'success_metrics': ['task_initiation', 'completion_rate'],
                'follow_up_timing': 15
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['positive', 'negative', 'intermittent'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose']
        }

        # Context tracking
        self.context_tracker = {
            'time_of_day': None,
            'energy_level': None,
            'task_history': [],
            'intervention_history': [],
            'success_rate': {}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze context
        current_state = self._analyze_user_state(user_context)
        
        # Select appropriate intervention
        intervention = self._select_intervention(current_state, user_config)
        
        # Personalize delivery
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config
        )
        
        return {
            'message': self._format_message(personalized_actions, user_config),
            'actions': personalized_actions,
            'follow_up': intervention['follow_up_timing']
        }

    def _analyze_user_state(self, context):
        """Analyze user state and context for intervention selection"""
        state = {
            'cognitive_load': self._estimate_cognitive_load(context),
            'energy_level': self._estimate_energy(context),
            'task_complexity': self._analyze_task_complexity(context),
            'time_pressure': self._analyze_time_pressure(context)
        }
        
        self.context_tracker['time_of_day'] = context.get('time')
        self.context_tracker['energy_level'] = state['energy_level']
        
        return state

    def _select_intervention(self, state, user_config):
        """Select most appropriate intervention based on state and user config"""
        
        # Check cognitive load threshold
        if state['cognitive_load'] > user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
            
        # Check motivation needs
        if state['energy_level'] < 0.5:
            return self.intervention_templates['motivation']
            
        # Default to focus intervention
        return self.intervention_templates['focus']

    def _personalize_actions(self, actions, user_config):
        """Personalize action steps based on user configuration"""
        personalized = []
        
        for action in actions:
            # Adjust difficulty based on learning style
            if user_config['learning_style'] == 'systematic':
                action['step'] = self._add_structure(action['step'])
            
            # Adjust communication style
            if user_config['communication_pref'] == 'direct':
                action['step'] = self._make_direct(action['step'])
                
            personalized.append(action)
            
        return personalized

    def _format_message(self, actions, user_config):
        """Format intervention message based on user preferences"""
        if user_config['communication_pref'] == 'direct':
            return self._format_direct_message(actions)
        return self._format_supportive_message(actions)

    def track_intervention_success(self, intervention_id, success_metrics):
        """Track success of interventions for adaptation"""
        self.context_tracker['intervention_history'].append({
            'id': intervention_id,
            'metrics': success_metrics,
            'timestamp': 'current_time'
        })
        
        # Update success rate
        self.context_tracker['success_rate'][intervention_id] = \
            self._calculate_success_rate(intervention_id)

    def _estimate_cognitive_load(self, context):
        """Estimate current cognitive load from context"""
        # Implementation details
        return 0.5

    def _estimate_energy(self, context):
        """Estimate user energy level from context"""
        # Implementation details
        return 0.7

    def _analyze_task_complexity(self, context):
        """Analyze complexity of current task"""
        # Implementation details
        return 0.6

    def _analyze_time_pressure(self, context):
        """Analyze current time pressure"""
        # Implementation details
        return 0.4

    def _add_structure(self, step):
        """Add more structure to step description"""
        # Implementation details
        return step

    def _make_direct(self, step):
        """Make step description more direct"""
        # Implementation details
        return step

    def _format_direct_message(self, actions):
        """Format message in direct style"""
        # Implementation details
        return "Direct message with actions"

    def _format_supportive_message(self, actions):
        """Format message in supportive style"""
        # Implementation details
        return "Supportive message with actions"

    def _calculate_success_rate(self, intervention_id):
        """Calculate success rate for intervention"""
        # Implementation details
        return 0.8