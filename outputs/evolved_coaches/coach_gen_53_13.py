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
                     'steps': ['Clear desk', 'Close unnecessary apps', 'Set timer']},
                    {'type': 'cognitive', 'duration': 5, 'priority': 2, 
                     'steps': ['Deep breath', 'State intention', 'Visualize completion']}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Challenge assumption', 'Find meaning']},
                    {'type': 'small_win', 'duration': 10, 'priority': 2,
                     'steps': ['Break task down', 'Complete mini-task', 'Celebrate']}
                ],
                'follow_up': {'timing': 15, 'type': 'reinforcement'}
            }
            # Additional templates...
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'interruption_frequency': None,
            'deadline_pressure': None
        }

        # Behavioral tracking
        self.user_metrics = {
            'intervention_response_rate': 0.0,
            'completion_rate': 0.0,
            'satisfaction_score': 0.0,
            'behavioral_change_index': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized coaching nudge"""
        
        # Update context awareness
        self._update_context(user_context)
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(personality_type)
        
        # Personalize based on user preferences and state
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            self.personality_type_configs[personality_type]
        )

        # Apply behavioral psychology principles
        enhanced_nudge = self._apply_behavioral_principles(personalized_actions)
        
        return {
            'message': enhanced_nudge['message'],
            'actions': enhanced_nudge['actions'],
            'timing': enhanced_nudge['timing'],
            'follow_up': enhanced_nudge['follow_up']
        }

    def _update_context(self, user_context):
        """Update context awareness parameters"""
        self.context_factors.update(user_context)
        
    def _select_intervention(self, personality_type):
        """Select most appropriate intervention template"""
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate intervention fitness scores
        scores = {}
        for template_name, template in self.intervention_templates.items():
            score = self._calculate_intervention_fitness(
                template, user_config, self.context_factors
            )
            scores[template_name] = score
            
        # Select best matching intervention
        best_intervention = max(scores.items(), key=lambda x: x[1])[0]
        return self.intervention_templates[best_intervention]

    def _personalize_actions(self, actions, user_config):
        """Personalize intervention actions based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            
            # Adjust based on learning style
            if user_config['learning_style'] == 'systematic':
                modified_action['steps'] = self._add_structure(action['steps'])
            elif user_config['learning_style'] == 'exploratory':
                modified_action['steps'] = self._add_flexibility(action['steps'])
                
            # Adjust communication style
            modified_action['message'] = self._adapt_communication(
                action.get('message', ''),
                user_config['communication_pref']
            )
            
            personalized.append(modified_action)
            
        return personalized

    def _apply_behavioral_principles(self, actions):
        """Apply behavioral psychology principles to enhance effectiveness"""
        enhanced = {
            'message': '',
            'actions': [],
            'timing': {},
            'follow_up': {}
        }
        
        for action in actions:
            # Apply motivation principles
            action = self._enhance_motivation(action)
            
            # Consider cognitive load
            action = self._manage_cognitive_load(action)
            
            # Add social proof elements
            action = self._add_social_proof(action)
            
            enhanced['actions'].append(action)
            
        # Optimize timing based on context
        enhanced['timing'] = self._optimize_timing(self.context_factors)
        
        # Set up follow-up mechanism
        enhanced['follow_up'] = self._create_follow_up_plan(actions)
        
        return enhanced

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Track and update intervention effectiveness metrics"""
        self.user_metrics.update(metrics)
        
        # Adjust future interventions based on effectiveness
        self._adjust_intervention_parameters(intervention_id, metrics)

    def _calculate_intervention_fitness(self, template, user_config, context):
        """Calculate fitness score for intervention template"""
        # Implementation details...
        pass

    def _optimize_timing(self, context):
        """Optimize intervention timing based on context"""
        # Implementation details...
        pass

    def _create_follow_up_plan(self, actions):
        """Create personalized follow-up plan"""
        # Implementation details...
        pass