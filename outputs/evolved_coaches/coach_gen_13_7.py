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
                'motivation_triggers': ['novelty', 'social_connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'priority': 1,
                     'steps': ['Clear desk', 'Block notifications', 'Set timer']},
                    {'type': 'cognitive', 'duration': 5, 'priority': 2, 
                     'steps': ['Brief meditation', 'Intent setting', 'Success visualization']}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'priority': 1,
                     'steps': ['Break task down', 'Set mini-milestone', 'Plan reward']},
                    {'type': 'energy_management', 'duration': 5, 'priority': 2,
                     'steps': ['Quick exercise', 'Power pose', 'Positive affirmation']}
                ],
                'follow_up': {'timing': 20, 'type': 'motivation_check'}
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None,
            'cognitive_load': None
        }

        # Behavioral tracking
        self.user_metrics = {
            'intervention_response_rate': 0.0,
            'completion_rate': 0.0,
            'satisfaction_score': 0.0,
            'behavioral_change_index': 0.0,
            'engagement_level': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized coaching nudge"""
        
        # Update context awareness
        self._update_context(user_context)
        
        # Select optimal intervention based on context
        intervention = self._select_intervention(personality_type)
        
        # Personalize based on user preferences and state
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            self.personality_type_configs[personality_type]
        )

        # Apply behavioral psychology principles
        motivated_actions = self._apply_motivation_principles(
            personalized_actions,
            self.personality_type_configs[personality_type]['motivation_triggers']
        )

        return {
            'nudge_content': motivated_actions,
            'timing': self._calculate_optimal_timing(),
            'follow_up': intervention['follow_up']
        }

    def _update_context(self, user_context):
        """Update context awareness parameters"""
        self.context_factors.update(user_context)
        self._calculate_cognitive_load()

    def _calculate_cognitive_load(self):
        """Estimate current cognitive load based on context"""
        factors = [
            self.context_factors['task_complexity'],
            self.context_factors['energy_level'],
            len(self.context_factors['recent_performance'])
        ]
        self.context_factors['cognitive_load'] = sum(factors) / len(factors)

    def _select_intervention(self, personality_type):
        """Select most appropriate intervention based on context"""
        user_config = self.personality_type_configs[personality_type]
        
        # Match intervention to current needs and preferences
        if self.context_factors['cognitive_load'] > user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        return self.intervention_templates['motivation']

    def _personalize_actions(self, actions, user_config):
        """Customize actions based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = user_config['communication_pref']
            modified_action['pacing'] = user_config['work_pattern']
            modified_action['format'] = user_config['learning_style']
            personalized.append(modified_action)
        return personalized

    def _apply_motivation_principles(self, actions, motivation_triggers):
        """Apply behavioral psychology principles to increase effectiveness"""
        enhanced_actions = []
        for action in actions:
            enhanced = action.copy()
            enhanced['reinforcement'] = self._select_reinforcement(motivation_triggers)
            enhanced['framing'] = self._optimize_framing(motivation_triggers)
            enhanced['social_proof'] = self._add_social_proof()
            enhanced_actions.append(enhanced)
        return enhanced_actions

    def _calculate_optimal_timing(self):
        """Determine best timing for intervention delivery"""
        energy_curve = self._get_energy_pattern()
        task_urgency = self._get_task_urgency()
        return self._optimize_timing(energy_curve, task_urgency)

    def update_metrics(self, interaction_results):
        """Update tracking metrics based on intervention results"""
        self.user_metrics.update(interaction_results)
        self._adapt_strategies(interaction_results)

    def _adapt_strategies(self, results):
        """Adjust intervention strategies based on performance"""
        if results['satisfaction_score'] < 0.7:
            self._refine_personalization()
        if results['completion_rate'] < 0.6:
            self._adjust_difficulty()