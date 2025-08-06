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
                    {'step': 'Close distracting applications',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Focus mode active'},
                    {'step': 'Set timer for focused work block',
                     'time_estimate': '1 min', 
                     'success_metric': 'Timer started'}
                ],
                'follow_up_interval': 25 # minutes
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus_period'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Physical movement completed'},
                    {'step': 'Hydrate and rest eyes',
                     'time_estimate': '3 min',
                     'success_metric': 'Break activities completed'}
                ],
                'follow_up_interval': 5
            }
            # Additional intervention types
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_rewards'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy_support', 'competence_building', 'relatedness']
        }

        # Performance tracking
        self.user_metrics = {
            'engagement_rate': 0.0,
            'completion_rate': 0.0,
            'satisfaction_score': 0.0,
            'behavior_change_index': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized coaching nudge"""
        
        # Get personality-specific configurations
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current context
        cognitive_load = self._assess_cognitive_load(user_context)
        optimal_timing = self._check_intervention_timing(user_context)
        relevant_triggers = self._identify_active_triggers(user_context)

        # Select appropriate intervention
        if not optimal_timing or cognitive_load > user_config['cognitive_load_threshold']:
            return None

        selected_intervention = self._select_best_intervention(
            relevant_triggers,
            user_config,
            user_context
        )

        # Personalize intervention
        nudge = self._personalize_intervention(
            selected_intervention,
            user_config['communication_pref'],
            user_config['motivation_triggers']
        )

        return nudge

    def _assess_cognitive_load(self, context):
        """Estimate current cognitive load based on context"""
        factors = {
            'active_tasks': len(context.get('active_tasks', [])) * 0.2,
            'time_on_task': min(context.get('focus_duration', 0) / 60, 1) * 0.3,
            'context_switches': min(context.get('task_switches', 0) / 10, 1) * 0.3,
            'interruption_rate': min(context.get('interruptions', 0) / 5, 1) * 0.2
        }
        return sum(factors.values())

    def _check_intervention_timing(self, context):
        """Determine if timing is appropriate for intervention"""
        last_intervention = context.get('last_intervention_time', 0)
        current_time = context.get('current_time', 0)
        min_interval = context.get('min_intervention_interval', 15)
        
        return (current_time - last_intervention) >= min_interval

    def _identify_active_triggers(self, context):
        """Identify relevant intervention triggers from context"""
        active_triggers = []
        
        if context.get('focus_duration', 0) > 45:
            active_triggers.append('extended_focus_period')
        
        if context.get('task_switches', 0) > 5:
            active_triggers.append('task_switching')
            
        if context.get('idle_time', 0) > 10:
            active_triggers.append('distraction')
            
        return active_triggers

    def _select_best_intervention(self, triggers, user_config, context):
        """Select most appropriate intervention based on triggers and user preferences"""
        matching_interventions = []
        
        for intervention_type, config in self.intervention_templates.items():
            if any(trigger in config['triggers'] for trigger in triggers):
                matching_interventions.append((intervention_type, config))
                
        # Select based on user preferences and current context
        return self._rank_interventions(matching_interventions, user_config, context)[0]

    def _personalize_intervention(self, intervention, comm_style, motivation_triggers):
        """Customize intervention based on user preferences"""
        
        personalized = {
            'title': self._adapt_message_style(intervention['title'], comm_style),
            'actions': intervention['actions'],
            'motivation': self._select_motivation_hook(motivation_triggers),
            'follow_up': intervention['follow_up_interval']
        }
        
        return personalized

    def update_metrics(self, interaction_results):
        """Update performance tracking metrics"""
        self.user_metrics['engagement_rate'] = (
            self.user_metrics['engagement_rate'] * 0.9 +
            interaction_results['engaged'] * 0.1
        )
        self.user_metrics['completion_rate'] = (
            self.user_metrics['completion_rate'] * 0.9 +
            interaction_results['completed'] * 0.1
        )
        self.user_metrics['satisfaction_score'] = (
            self.user_metrics['satisfaction_score'] * 0.9 +
            interaction_results['satisfaction'] * 0.1
        )
        self.user_metrics['behavior_change_index'] = (
            self.user_metrics['behavior_change_index'] * 0.9 +
            interaction_results['behavior_change'] * 0.1
        )