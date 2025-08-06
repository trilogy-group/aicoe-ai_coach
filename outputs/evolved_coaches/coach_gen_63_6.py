class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced traits and preferences
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'achievement', 'efficiency'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'creativity', 'social_impact'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Set timer for focused work block', 
                     'time_estimate': '1 min',
                     'success_metric': 'Timer started'},
                    {'step': 'Review task priorities',
                     'time_estimate': '3 min', 
                     'success_metric': 'Priority list created'}
                ],
                'follow_up_window': 30 # minutes
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into smaller chunks',
                     'time_estimate': '5 min',
                     'success_metric': 'Subtasks created'},
                    {'step': 'Set mini-milestone reward',
                     'time_estimate': '2 min',
                     'success_metric': 'Reward defined'},
                    {'step': 'Visualize successful completion',
                     'time_estimate': '3 min',
                     'success_metric': 'Vision exercise completed'}
                ],
                'follow_up_window': 60
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['positive', 'negative', 'intermittent'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'cognitive_load': ['chunking', 'spacing', 'sequencing']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_score': 0.0,
            'recent_interventions': [],
            'successful_strategies': set(),
            'improvement_areas': set()
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        
        # Get personality-specific configs
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Analyze current context
        cognitive_load = self._assess_cognitive_load(current_context)
        optimal_timing = self._check_intervention_timing(current_context)
        
        if not optimal_timing:
            return None

        # Select appropriate intervention
        intervention = self._select_intervention(
            personality_config,
            cognitive_load,
            current_context
        )

        # Personalize intervention
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            personality_config,
            user_profile['preferences']
        )

        # Add behavioral psychology elements
        enhanced_intervention = self._enhance_with_psychology(
            personalized_actions,
            personality_config['motivation_triggers']
        )

        return {
            'intervention_type': intervention['type'],
            'actions': enhanced_intervention,
            'timing': optimal_timing,
            'follow_up': intervention['follow_up_window']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'active_tasks': len(context['active_tasks']) * 0.2,
            'interruptions': context['interruption_count'] * 0.1,
            'time_pressure': context['deadline_proximity'] * 0.3,
            'task_complexity': context['task_complexity'] * 0.4
        }
        return sum(factors.values())

    def _check_intervention_timing(self, context):
        """Determine optimal intervention timing"""
        if context['in_flow_state']:
            return False
        
        time_since_last = context['time_since_last_intervention']
        if time_since_last < 30: # minutes
            return False
            
        return True

    def _select_intervention(self, personality_config, cognitive_load, context):
        """Select most appropriate intervention based on context"""
        if cognitive_load > personality_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        
        if context['task_progress'] < 0.3:
            return self.intervention_templates['motivation']
            
        return self.intervention_templates['focus']

    def _personalize_actions(self, actions, personality_config, preferences):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality_config['communication_pref']
            modified_action['format'] = preferences['preferred_format']
            personalized.append(modified_action)
        return personalized

    def _enhance_with_psychology(self, actions, motivation_triggers):
        """Add behavioral psychology elements to intervention"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['principle'] = self._select_behavior_principle(action)
            enhanced_action['motivation_hook'] = self._select_motivation_trigger(
                motivation_triggers
            )
            enhanced.append(enhanced_action)
        return enhanced

    def _select_behavior_principle(self, action):
        """Select appropriate behavioral principle"""
        if action['time_estimate'] <= '2 min':
            return self.behavior_principles['habit_formation']
        return self.behavior_principles['reinforcement']

    def _select_motivation_trigger(self, triggers):
        """Select appropriate motivation trigger"""
        return triggers[0] # Simplified selection for example

    def track_intervention_outcome(self, intervention_id, outcome_metrics):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking outcomes and updating strategies
        pass

    def update_user_context(self, new_context_data):
        """Update tracked user context"""
        # Implementation for updating user context
        pass