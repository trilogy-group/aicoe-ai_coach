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
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Focus time logged'}
                ],
                'follow_up': {'timing': '+30 min', 'type': 'check_progress'}
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines', 'task_overload'],
                'actions': [
                    {'step': 'Brain dump all tasks',
                     'time_estimate': '5 min', 
                     'success_metric': 'Tasks listed'},
                    {'step': 'Prioritize top 3 tasks',
                     'time_estimate': '3 min',
                     'success_metric': 'Priorities set'}
                ],
                'follow_up': {'timing': '+2 hours', 'type': 'review_progress'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'cognitive_load': ['chunking', 'spacing', 'retrieval_practice']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': None,
            'recent_interventions': [],
            'intervention_outcomes': {}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        
        # Get personality-specific configs
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Assess current cognitive load and context
        cognitive_load = self._assess_cognitive_load(current_context)
        if cognitive_load > personality_config['cognitive_load_threshold']:
            return self._generate_simplified_nudge()

        # Select appropriate intervention template
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
        """Assess current cognitive load based on context factors"""
        factors = {
            'num_active_tasks': 0.2,
            'time_pressure': 0.3,
            'task_complexity': 0.3,
            'interruption_frequency': 0.2
        }
        
        load = sum(factors[f] * context.get(f, 0) for f in factors)
        self.user_context['cognitive_load'] = load
        return load

    def _select_intervention_template(self, context):
        """Select most appropriate intervention template for current context"""
        matching_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                matching_templates.append((template_name, template))
                
        # Select best match based on context and recent intervention history
        return self._rank_templates(matching_templates)[0][1]

    def _personalize_actions(self, actions, personality_config):
        """Customize actions based on personality preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality_config['communication_pref']
            modified_action['pace'] = personality_config['work_pattern']
            personalized.append(modified_action)
        return personalized

    def _apply_behavior_principles(self, actions):
        """Apply behavioral psychology principles to enhance effectiveness"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['trigger'] = self._identify_trigger(action)
            enhanced_action['reward'] = self._design_reward(action)
            enhanced_action['reinforcement'] = self._plan_reinforcement(action)
            enhanced.append(enhanced_action)
        return enhanced

    def track_intervention_outcome(self, intervention_id, outcome_metrics):
        """Track and analyze intervention effectiveness"""
        self.user_context['intervention_outcomes'][intervention_id] = outcome_metrics
        self._update_intervention_strategies(outcome_metrics)

    def _update_intervention_strategies(self, outcome_metrics):
        """Adapt intervention strategies based on outcome data"""
        if outcome_metrics['success_rate'] < 0.5:
            self._adjust_difficulty()
        if outcome_metrics['engagement'] < 0.7:
            self._enhance_motivation_triggers()

    def _generate_simplified_nudge(self):
        """Generate simplified intervention for high cognitive load situations"""
        return {
            'message': 'Take a 2-minute breather to reset.',
            'actions': [{'step': 'Close eyes and breathe deeply', 'time_estimate': '2 min'}],
            'follow_up': {'timing': '+5 min', 'type': 'check_energy'}
        }

    def get_intervention_analytics(self):
        """Return analytics on intervention effectiveness"""
        return {
            'success_rate': self._calculate_success_rate(),
            'engagement_level': self._calculate_engagement(),
            'behavior_change': self._measure_behavior_change()
        }