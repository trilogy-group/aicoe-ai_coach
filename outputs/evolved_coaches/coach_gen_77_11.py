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
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Enable do-not-disturb']},
                    {'type': 'technique', 'duration': 25, 'priority': 2, 
                     'steps': ['Set timer', 'Work in focused sprint', 'Take 5min break']}
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Break into smaller steps', 'Set micro-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['Quick exercise', 'Power pose', 'Success visualization']}
                ],
                'follow_up': {'timing': 15, 'type': 'progress_check'}
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
            intervention, 
            self.personality_type_configs[personality_type]
        )
        
        # Apply behavioral psychology principles
        motivated_actions = self._apply_motivation_principles(
            personalized_actions,
            self.personality_type_configs[personality_type]['motivation_triggers']
        )
        
        return {
            'nudge': motivated_actions,
            'timing': self._calculate_optimal_timing(),
            'follow_up': intervention['follow_up']
        }

    def _update_context(self, user_context):
        """Update context awareness parameters"""
        for factor in self.context_factors:
            if factor in user_context:
                self.context_factors[factor] = user_context[factor]

    def _select_intervention(self, personality_type):
        """Select most appropriate intervention template"""
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate intervention scores based on context match
        scores = {}
        for template_name, template in self.intervention_templates.items():
            score = self._calculate_context_match(template, user_config)
            scores[template_name] = score
            
        # Return best matching intervention
        best_match = max(scores.items(), key=lambda x: x[1])[0]
        return self.intervention_templates[best_match]

    def _personalize_actions(self, intervention, user_config):
        """Personalize intervention actions based on user preferences"""
        personalized = []
        
        for action in intervention['actions']:
            # Adjust communication style
            styled_steps = self._style_communication(
                action['steps'],
                user_config['communication_pref']
            )
            
            # Adjust to learning style
            adapted_steps = self._adapt_to_learning_style(
                styled_steps,
                user_config['learning_style']
            )
            
            personalized.append({
                **action,
                'steps': adapted_steps
            })
            
        return personalized

    def _apply_motivation_principles(self, actions, motivation_triggers):
        """Apply behavioral psychology principles to increase effectiveness"""
        enhanced_actions = []
        
        for action in actions:
            # Add motivation elements
            motivated_steps = self._add_motivation_elements(
                action['steps'],
                motivation_triggers
            )
            
            # Add progress tracking
            trackable_steps = self._add_progress_tracking(motivated_steps)
            
            enhanced_actions.append({
                **action,
                'steps': trackable_steps
            })
            
        return enhanced_actions

    def _calculate_optimal_timing(self):
        """Calculate optimal intervention timing based on context"""
        timing_score = {
            'immediate': self._calculate_urgency(),
            'short_delay': self._calculate_receptiveness(),
            'scheduled': self._calculate_planning_benefit()
        }
        return max(timing_score.items(), key=lambda x: x[1])[0]

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Track and update intervention effectiveness metrics"""
        for metric, value in metrics.items():
            if metric in self.user_metrics:
                # Update using exponential moving average
                self.user_metrics[metric] = (
                    0.8 * self.user_metrics[metric] + 0.2 * value
                )