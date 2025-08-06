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
                'motivation_triggers': ['novelty', 'social', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Enable focus mode', 'time_est': '1 min'},
                    {'step': 'Set clear next action', 'time_est': '3 min'}
                ],
                'success_metrics': ['time_on_task', 'task_completion'],
                'follow_up_window': 30 # minutes
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into smaller chunks', 'time_est': '5 min'},
                    {'step': 'Set mini-milestone', 'time_est': '2 min'},
                    {'step': 'Schedule reward', 'time_est': '1 min'}
                ],
                'success_metrics': ['task_initiation', 'milestone_completion'],
                'follow_up_window': 60
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_change_techniques = {
            'habit_formation': {
                'cue_identification',
                'routine_design', 
                'reward_scheduling'
            },
            'motivation': {
                'autonomy_support',
                'competence_building',
                'relatedness_enhancement'
            },
            'cognitive_load': {
                'task_chunking',
                'attention_management',
                'context_switching_reduction'
            }
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': 'unknown',
            'recent_interventions': [],
            'intervention_outcomes': {},
            'daily_patterns': {}
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate personalized intervention based on user context"""
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        # Select optimal intervention
        intervention = self.select_intervention(
            personality_type=user_profile['personality_type'],
            context=current_context,
            cognitive_load=self.user_context['cognitive_load']
        )

        # Personalize content
        nudge = self.personalize_content(
            intervention=intervention,
            user_profile=user_profile,
            context=current_context
        )

        return self.format_nudge(nudge)

    def select_intervention(self, personality_type, context, cognitive_load):
        """Select most appropriate intervention based on user factors"""
        config = self.personality_type_configs[personality_type]
        
        # Check cognitive load threshold
        if cognitive_load > config['cognitive_load_threshold']:
            return self.get_minimal_intervention()
            
        # Match intervention to context and personality
        relevant_interventions = self.match_interventions(
            context=context,
            learning_style=config['learning_style'],
            work_pattern=config['work_pattern']
        )
        
        return self.optimize_intervention_selection(
            interventions=relevant_interventions,
            motivation_triggers=config['motivation_triggers']
        )

    def personalize_content(self, intervention, user_profile, context):
        """Personalize intervention content for user"""
        config = self.personality_type_configs[user_profile['personality_type']]
        
        content = {
            'message': self.generate_message(
                intervention=intervention,
                comm_style=config['communication_pref']
            ),
            'actions': self.customize_actions(
                intervention['actions'],
                context=context
            ),
            'success_metrics': intervention['success_metrics'],
            'follow_up': self.schedule_follow_up(
                window=intervention['follow_up_window'],
                context=context
            )
        }
        
        return content

    def track_intervention_outcome(self, intervention_id, metrics):
        """Track and analyze intervention effectiveness"""
        self.user_context['intervention_outcomes'][intervention_id] = {
            'metrics': metrics,
            'timestamp': self.get_current_time(),
            'context': self.user_context.copy()
        }
        
        self.update_intervention_models(intervention_id, metrics)

    def update_user_context(self, context_data):
        """Update user context with new data"""
        self.user_context.update({
            'cognitive_load': self.estimate_cognitive_load(context_data),
            'energy_level': self.estimate_energy_level(context_data),
            'focus_state': self.analyze_focus_state(context_data)
        })
        
        self.update_daily_patterns(context_data)

    def get_minimal_intervention(self):
        """Return minimal intervention for high cognitive load"""
        return {
            'type': 'minimal',
            'actions': [{'step': 'Take a 2-minute break', 'time_est': '2 min'}],
            'success_metrics': ['break_taken'],
            'follow_up_window': 15
        }

    # Helper methods
    def get_user_profile(self, user_id):
        """Get user profile from database"""
        pass

    def analyze_context(self, context):
        """Analyze current user context"""
        pass

    def match_interventions(self, context, learning_style, work_pattern):
        """Match interventions to user characteristics"""
        pass

    def optimize_intervention_selection(self, interventions, motivation_triggers):
        """Select optimal intervention"""
        pass

    def generate_message(self, intervention, comm_style):
        """Generate personalized message"""
        pass

    def customize_actions(self, actions, context):
        """Customize action steps"""
        pass

    def schedule_follow_up(self, window, context):
        """Schedule intervention follow-up"""
        pass

    def get_current_time(self):
        """Get current timestamp"""
        pass

    def update_intervention_models(self, intervention_id, metrics):
        """Update intervention effectiveness models"""
        pass

    def estimate_cognitive_load(self, context_data):
        """Estimate current cognitive load"""
        pass

    def estimate_energy_level(self, context_data):
        """Estimate current energy level"""
        pass

    def analyze_focus_state(self, context_data):
        """Analyze current focus state"""
        pass

    def update_daily_patterns(self, context_data):
        """Update tracked daily patterns"""
        pass