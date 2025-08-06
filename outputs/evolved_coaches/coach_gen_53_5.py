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
                     'steps': ['Clear desk', 'Close unnecessary apps', 'Put phone away']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer', 'Work in focused sprint', 'Take short break']}
                ],
                'follow_up': {'timing': 30, 'type': 'check_completion'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Challenge assumption', 'Find meaning']},
                    {'type': 'small_win', 'duration': 10, 'priority': 2,
                     'steps': ['Break task down', 'Complete tiny step', 'Celebrate progress']}
                ],
                'follow_up': {'timing': 15, 'type': 'check_progress'}
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_reward', 'progress_tracking', 'streak_maintenance'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3},
            'interruption_cost': {'high': 0.9, 'medium': 0.5, 'low': 0.2}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on context and personality"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.6:
            return None  # Don't interrupt if timing isn't right

        # Select appropriate intervention
        intervention = self._select_intervention(user_context, config)
        
        # Personalize action steps
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            config['learning_style'],
            config['cognitive_load_threshold']
        )

        # Apply behavioral psychology principles
        enhanced_intervention = self._apply_behavior_principles(
            personalized_actions,
            config['motivation_triggers']
        )

        return {
            'type': intervention['type'],
            'actions': enhanced_intervention,
            'timing': timing_score,
            'follow_up': intervention['follow_up']
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        complexity_factor = self.context_factors['task_complexity'][context['task']]
        interruption_factor = self.context_factors['interruption_cost'][context['interruption']]
        
        return (time_factor * energy_factor * complexity_factor * interruption_factor)

    def _select_intervention(self, context, config):
        """Select most appropriate intervention based on context"""
        relevant_interventions = []
        for intervention_type, details in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in details['triggers']):
                relevant_interventions.append((intervention_type, details))
        
        # Select best intervention based on context match and user preferences
        return max(relevant_interventions, 
                  key=lambda x: self._calculate_intervention_fit(x[1], config))

    def _personalize_actions(self, actions, learning_style, cognitive_threshold):
        """Personalize action steps based on learning style and cognitive load"""
        personalized = []
        current_load = 0
        
        for action in actions:
            if current_load + (action['duration'] / 60) <= cognitive_threshold:
                modified_action = action.copy()
                if learning_style == 'systematic':
                    modified_action['steps'] = self._add_detail_to_steps(action['steps'])
                elif learning_style == 'exploratory':
                    modified_action['steps'] = self._add_flexibility_to_steps(action['steps'])
                
                personalized.append(modified_action)
                current_load += (action['duration'] / 60)
                
        return personalized

    def _apply_behavior_principles(self, actions, motivation_triggers):
        """Enhance actions with behavioral psychology principles"""
        enhanced_actions = []
        
        for action in actions:
            enhanced_action = action.copy()
            # Add immediate reward
            enhanced_action['reward'] = self._generate_reward(motivation_triggers)
            # Add progress tracking
            enhanced_action['progress_markers'] = self._create_progress_markers(action['steps'])
            # Add habit formation elements
            enhanced_action['habit_cue'] = self._identify_habit_cue(action['type'])
            
            enhanced_actions.append(enhanced_action)
            
        return enhanced_actions

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and adapt based on intervention effectiveness"""
        # Implementation for tracking and adapting interventions
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interaction data"""
        # Implementation for updating user model
        pass