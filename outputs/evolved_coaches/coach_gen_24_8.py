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
                    {'description': 'Enable focus mode for 25 minutes',
                     'time_estimate': 25,
                     'success_metric': 'Completed focused work session',
                     'priority': 'high'},
                    {'description': 'Clear desktop and close unnecessary tabs',
                     'time_estimate': 2,
                     'success_metric': 'Reduced open windows/tabs',
                     'priority': 'medium'}
                ],
                'follow_up': {'timing': 30, 'type': 'check_completion'}
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines'],
                'actions': [
                    {'description': 'Break project into max 2-hour tasks',
                     'time_estimate': 15,
                     'success_metric': 'Task list created',
                     'priority': 'high'},
                    {'description': 'Schedule top 3 priorities for tomorrow',
                     'time_estimate': 10,
                     'success_metric': 'Calendar updated',
                     'priority': 'high'}
                ],
                'follow_up': {'timing': 60, 'type': 'review_progress'}
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'habit_formation': {
                'cue': None,
                'routine': None,
                'reward': None,
                'min_repetitions': 21
            },
            'motivation': {
                'autonomy': 0.0,
                'mastery': 0.0,
                'purpose': 0.0
            }
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': 'unknown',
            'recent_interventions': [],
            'successful_strategies': set()
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        
        # Get personality-specific config
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Calculate cognitive load and check threshold
        current_load = self._assess_cognitive_load(current_context)
        if current_load > personality_config['cognitive_load_threshold']:
            return self._generate_recovery_intervention()

        # Select relevant intervention template
        template = self._select_intervention_template(current_context)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], personality_config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(actions)
        
        return {
            'message': self._format_message(enhanced_actions, personality_config),
            'actions': enhanced_actions,
            'follow_up': template['follow_up']
        }

    def _assess_cognitive_load(self, context):
        """Calculate current cognitive load based on context"""
        factors = {
            'open_tasks': len(context.get('active_tasks', [])) * 0.1,
            'time_pressure': context.get('deadline_proximity', 0) * 0.2,
            'task_complexity': context.get('task_complexity', 0) * 0.3,
            'interruptions': len(context.get('recent_interruptions', [])) * 0.1
        }
        return sum(factors.values())

    def _select_intervention_template(self, context):
        """Select most appropriate intervention template based on context"""
        triggers = set()
        for template in self.intervention_templates.values():
            if any(trigger in context for trigger in template['triggers']):
                triggers.add(template)
        
        return max(triggers, key=lambda t: len(set(t['triggers']) & set(context)))

    def _personalize_actions(self, actions, personality_config):
        """Customize actions based on personality preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality_config['communication_pref']
            modified_action['pacing'] = personality_config['work_pattern']
            personalized.append(modified_action)
        return personalized

    def _apply_behavior_principles(self, actions):
        """Enhance actions with behavioral psychology principles"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['habit_cue'] = self._identify_habit_cue(action)
            enhanced_action['reward'] = self._design_reward(action)
            enhanced_action['motivation_elements'] = self._add_motivation_elements(action)
            enhanced.append(enhanced_action)
        return enhanced

    def _format_message(self, actions, personality_config):
        """Format intervention message according to personality preferences"""
        style = personality_config['communication_pref']
        if style == 'direct':
            return self._format_direct_message(actions)
        elif style == 'enthusiastic':
            return self._format_enthusiastic_message(actions)
        return self._format_default_message(actions)

    def update_user_context(self, new_context):
        """Update tracked user context with new information"""
        self.user_context.update(new_context)
        self._prune_old_interventions()
        self._update_success_metrics()

    def track_intervention_success(self, intervention_id, success_metrics):
        """Track success of previous interventions"""
        if success_metrics['completed']:
            self.user_context['successful_strategies'].add(
                success_metrics['strategy_type']
            )