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
                    {'type': 'environment', 'duration': 15, 'specifics': 'Clear workspace of distractions'},
                    {'type': 'technique', 'duration': 25, 'specifics': 'Use Pomodoro method'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful pause'}
                ],
                'follow_up': {'timing': 30, 'metric': 'focus_duration'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller steps'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define meaningful completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'metric': 'task_completion'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progressive_rewards', 'social_proof'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'relatedness']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3},
            'interruption_frequency': {'high': 0.3, 'medium': 0.6, 'low': 0.9}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze context
        context_score = self._evaluate_context(user_context)
        
        # Select appropriate intervention
        intervention = self._select_intervention(context_score, user_config)
        
        # Personalize actions
        actions = self._personalize_actions(intervention, user_config)
        
        return self._format_nudge(actions, user_config)

    def _evaluate_context(self, context):
        """Evaluate user context for intervention timing"""
        context_score = 0
        
        for factor, value in context.items():
            if factor in self.context_factors:
                context_score += self.context_factors[factor][value]
                
        return context_score / len(context)

    def _select_intervention(self, context_score, user_config):
        """Select most appropriate intervention based on context and user"""
        best_intervention = None
        max_score = 0
        
        for intervention in self.intervention_templates.values():
            score = self._calculate_intervention_fit(
                intervention, 
                context_score,
                user_config
            )
            
            if score > max_score:
                max_score = score
                best_intervention = intervention
                
        return best_intervention

    def _personalize_actions(self, intervention, user_config):
        """Customize intervention actions for user"""
        personalized_actions = []
        
        for action in intervention['actions']:
            modified_action = action.copy()
            
            # Adjust based on learning style
            if user_config['learning_style'] == 'systematic':
                modified_action['specifics'] = self._add_structure(action['specifics'])
            
            # Adjust based on communication preference
            modified_action['tone'] = user_config['communication_pref']
            
            # Add motivation triggers
            modified_action['motivators'] = self._select_motivators(user_config)
            
            personalized_actions.append(modified_action)
            
        return personalized_actions

    def _add_structure(self, action_specifics):
        """Add systematic structure to action steps"""
        return f"1. Plan: {action_specifics}\n2. Execute: Follow steps precisely\n3. Review: Check completion"

    def _select_motivators(self, user_config):
        """Select appropriate motivation triggers"""
        return [
            trigger for trigger in user_config['motivation_triggers']
            if trigger in self.behavior_principles['motivation']
        ]

    def _format_nudge(self, actions, user_config):
        """Format final nudge with actions and follow-up"""
        nudge = {
            'actions': actions,
            'style': user_config['communication_pref'],
            'work_pattern': user_config['work_pattern'],
            'cognitive_load': user_config['cognitive_load_threshold'],
            'follow_up': {
                'timing': 30,
                'type': 'check_progress',
                'metrics': ['completion', 'satisfaction', 'difficulty']
            }
        }
        return nudge