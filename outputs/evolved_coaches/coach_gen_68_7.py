class EvolutionaryAICoach:
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
                'follow_up_window': 30 # minutes
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
                'follow_up_window': 60
            }
            # Additional intervention types
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_reward', 'progress_tracking', 'streak_maintenance'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof'],
            'cognitive_load': ['chunking', 'spacing', 'interleaving']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_score': 1.0,
            'interruption_frequency': 0,
            'task_completion_rate': 0.0,
            'recent_interventions': []
        }

    def generate_intervention(self, user_id, context):
        """Generate personalized intervention based on user context"""
        
        # Get user personality type and preferences
        user_profile = self.get_user_profile(user_id)
        personality_config = self.personality_type_configs[user_profile['personality_type']]

        # Analyze current context
        current_state = self.analyze_user_state(context)
        
        # Select appropriate intervention
        intervention_type = self.select_intervention_type(current_state, personality_config)
        
        # Personalize intervention
        intervention = self.personalize_intervention(
            intervention_type,
            personality_config,
            current_state
        )

        # Apply behavioral principles
        intervention = self.apply_behavior_principles(intervention, user_profile)

        # Update tracking
        self.update_user_context(intervention)

        return intervention

    def analyze_user_state(self, context):
        """Analyze user's current state and needs"""
        state = {
            'cognitive_load': self.estimate_cognitive_load(context),
            'energy_level': self.estimate_energy_level(context),
            'focus_score': self.calculate_focus_score(context),
            'primary_need': self.identify_primary_need(context)
        }
        return state

    def select_intervention_type(self, state, personality_config):
        """Select most appropriate intervention type"""
        if state['cognitive_load'] > personality_config['cognitive_load_threshold']:
            return 'focus'
        elif state['energy_level'] < 0.4:
            return 'motivation'
        # Additional selection logic
        return 'default'

    def personalize_intervention(self, intervention_type, personality_config, state):
        """Personalize intervention based on user preferences and state"""
        template = self.intervention_templates[intervention_type].copy()
        
        # Adjust communication style
        template['tone'] = personality_config['communication_pref']
        
        # Adjust difficulty based on state
        template['actions'] = self.adjust_action_difficulty(
            template['actions'],
            state['cognitive_load']
        )

        # Add personalized motivation triggers
        template['motivation_elements'] = [
            trigger for trigger in personality_config['motivation_triggers']
        ]

        return template

    def apply_behavior_principles(self, intervention, user_profile):
        """Apply behavioral psychology principles to intervention"""
        principles = self.select_relevant_principles(user_profile)
        
        for principle in principles:
            intervention = self.apply_principle(intervention, principle)
            
        return intervention

    def update_user_context(self, intervention):
        """Update user context tracking"""
        self.user_context['recent_interventions'].append({
            'type': intervention['type'],
            'timestamp': self.get_current_time(),
            'expected_completion': self.estimate_completion_time(intervention)
        })
        
        # Cleanup old interventions
        self.cleanup_old_interventions()

    # Additional helper methods...