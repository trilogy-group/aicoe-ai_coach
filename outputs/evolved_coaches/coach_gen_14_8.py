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
                    {'type': 'environment', 'duration': 5, 'impact': 0.7},
                    {'type': 'timeblock', 'duration': 25, 'impact': 0.8},
                    {'type': 'mindfulness', 'duration': 3, 'impact': 0.6}
                ],
                'follow_up': {'timing': 30, 'type': 'check_progress'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy'],
                'actions': [
                    {'type': 'goal_reminder', 'duration': 2, 'impact': 0.6},
                    {'type': 'small_win', 'duration': 10, 'impact': 0.7},
                    {'type': 'accountability', 'duration': 5, 'impact': 0.8}
                ],
                'follow_up': {'timing': 15, 'type': 'reinforcement'}
            }
            # Additional templates...
        }

        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_score': 1.0,
            'recent_interventions': [],
            'success_rate': {}
        }

    def generate_personalized_nudge(self, user_state, personality_type):
        """Generate personalized intervention based on user state and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current context
        context_score = self._analyze_context(user_state)
        
        # Select optimal intervention
        intervention = self._select_intervention(
            context_score,
            user_config,
            user_state['current_activity']
        )

        # Personalize delivery
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config['learning_style'],
            user_config['communication_pref']
        )

        # Add behavioral psychology elements
        enhanced_nudge = self._enhance_with_psychology(
            personalized_actions,
            user_config['motivation_triggers']
        )

        return {
            'nudge': enhanced_nudge,
            'timing': self._calculate_optimal_timing(user_state),
            'follow_up': intervention['follow_up']
        }

    def _analyze_context(self, user_state):
        """Analyze user context for intervention relevance"""
        context_score = {
            'cognitive_availability': 1 - user_state.get('cognitive_load', 0),
            'energy_level': user_state.get('energy_level', 1),
            'focus_state': user_state.get('focus_score', 1),
            'interruption_cost': self._calculate_interruption_cost(user_state)
        }
        
        return context_score

    def _select_intervention(self, context_score, user_config, activity):
        """Select most appropriate intervention based on context"""
        available_interventions = self.intervention_templates.copy()
        
        # Filter by cognitive load threshold
        available_interventions = {
            k:v for k,v in available_interventions.items() 
            if context_score['cognitive_availability'] >= user_config['cognitive_load_threshold']
        }

        # Score interventions
        scored_interventions = self._score_interventions(
            available_interventions,
            context_score,
            activity
        )

        return max(scored_interventions, key=lambda x: x['score'])

    def _personalize_actions(self, actions, learning_style, comm_pref):
        """Personalize intervention actions"""
        personalized = []
        
        for action in actions:
            enhanced_action = action.copy()
            
            # Adapt to learning style
            enhanced_action['format'] = self._adapt_to_learning_style(
                action['type'],
                learning_style
            )
            
            # Adjust communication style
            enhanced_action['messaging'] = self._adapt_communication(
                action['type'],
                comm_pref
            )
            
            personalized.append(enhanced_action)
            
        return personalized

    def _enhance_with_psychology(self, actions, motivation_triggers):
        """Add behavioral psychology elements to intervention"""
        enhanced = []
        
        for action in actions:
            psychology_enhanced = action.copy()
            
            # Add motivation elements
            psychology_enhanced['motivators'] = self._select_motivators(
                action['type'],
                motivation_triggers
            )
            
            # Add commitment devices
            psychology_enhanced['commitment'] = self._generate_commitment_device(
                action['type']
            )
            
            enhanced.append(psychology_enhanced)
            
        return enhanced

    def _calculate_optimal_timing(self, user_state):
        """Calculate optimal intervention timing"""
        return {
            'delay': self._compute_delay(user_state),
            'duration': self._compute_duration(user_state),
            'frequency': self._compute_frequency(user_state)
        }

    def update_user_context(self, interaction_result):
        """Update user context based on intervention results"""
        self.user_context['cognitive_load'] = interaction_result.get('cognitive_load', 0)
        self.user_context['energy_level'] = interaction_result.get('energy_level', 1)
        self.user_context['focus_score'] = interaction_result.get('focus_score', 1)
        
        # Update intervention history
        self.user_context['recent_interventions'].append({
            'type': interaction_result['intervention_type'],
            'success': interaction_result['success'],
            'timestamp': interaction_result['timestamp']
        })
        
        # Update success rates
        intervention_type = interaction_result['intervention_type']
        current_success = self.user_context['success_rate'].get(intervention_type, 0)
        self.user_context['success_rate'][intervention_type] = (
            current_success * 0.9 + interaction_result['success'] * 0.1
        )