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
                     'steps': ['Set timer for 25 min', 'Work on single task', 'Take 5 min break']}
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframing', 'duration': 10, 'priority': 1,
                     'steps': ['Identify specific barrier', 'Break into smaller steps', 'Set micro-goal']},
                    {'type': 'reward', 'duration': 5, 'priority': 2,
                     'steps': ['Define completion criteria', 'Choose meaningful reward', 'Schedule reward time']}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['implementation_intention', 'environmental_design', 'reward_scheduling'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof'],
            'focus': ['attention_management', 'cognitive_load', 'context_switching']
        }

        # User context tracking
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Update context tracking
        self.context_factors.update(context)
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(personality_config, context)
        
        # Personalize intervention
        personalized_actions = self._personalize_actions(intervention, personality_config)
        
        return self._format_nudge(personalized_actions, personality_config)

    def _select_intervention(self, personality_config, context):
        """Select most appropriate intervention based on personality and context"""
        # Calculate intervention scores based on multiple factors
        intervention_scores = {}
        
        for intervention_type, template in self.intervention_templates.items():
            score = self._calculate_intervention_score(
                template, 
                personality_config,
                context
            )
            intervention_scores[intervention_type] = score
            
        # Return highest scoring intervention
        return self.intervention_templates[max(intervention_scores, key=intervention_scores.get)]

    def _calculate_intervention_score(self, template, personality_config, context):
        """Calculate effectiveness score for an intervention"""
        score = 0
        
        # Context alignment
        if context['time_of_day'] in template.get('optimal_times', []):
            score += 1
        
        # Personality alignment
        if personality_config['learning_style'] in template.get('learning_styles', []):
            score += 1
            
        # Cognitive load consideration
        if context['task_complexity'] <= personality_config['cognitive_load_threshold']:
            score += 1
            
        # Motivation alignment
        common_triggers = set(personality_config['motivation_triggers']) & set(template.get('triggers', []))
        score += len(common_triggers) * 0.5
        
        return score

    def _personalize_actions(self, intervention, personality_config):
        """Personalize intervention actions based on personality"""
        personalized_actions = []
        
        for action in intervention['actions']:
            # Adjust action based on personality preferences
            adjusted_action = action.copy()
            
            # Modify communication style
            adjusted_action['communication_style'] = personality_config['communication_pref']
            
            # Adjust duration based on work pattern
            if personality_config['work_pattern'] == 'deep_focus':
                adjusted_action['duration'] *= 1.5
            
            # Add personality-specific motivation elements
            adjusted_action['motivation_elements'] = [
                trigger for trigger in personality_config['motivation_triggers']
                if trigger in self.behavior_triggers['motivation']
            ]
            
            personalized_actions.append(adjusted_action)
            
        return personalized_actions

    def _format_nudge(self, actions, personality_config):
        """Format nudge message according to personality preferences"""
        nudge = {
            'style': personality_config['communication_pref'],
            'actions': actions,
            'follow_up': {
                'timing': min(action['duration'] for action in actions) + 5,
                'type': 'check_progress'
            },
            'metrics': {
                'expected_duration': sum(action['duration'] for action in actions),
                'difficulty': self._calculate_difficulty(actions),
                'success_criteria': self._define_success_criteria(actions)
            }
        }
        
        return nudge

    def _calculate_difficulty(self, actions):
        """Calculate overall difficulty of intervention"""
        return sum(len(action['steps']) * action['priority'] for action in actions) / len(actions)

    def _define_success_criteria(self, actions):
        """Define measurable success criteria for intervention"""
        return {
            'completion': [step for action in actions for step in action['steps']],
            'time_bound': max(action['duration'] for action in actions),
            'verification': 'self_report'
        }