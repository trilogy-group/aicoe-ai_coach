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
                    {'type': 'goal_setting', 'duration': 10, 'priority': 1,
                     'steps': ['Break task down', 'Set mini-milestone', 'Reward plan']},
                    {'type': 'reframing', 'duration': 5, 'priority': 2,
                     'steps': ['Identify barriers', 'Challenge assumptions', 'Find meaning']}
                ],
                'follow_up': {'timing': 45, 'type': 'motivation_check'}
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_reward', 'progress_tracking', 'streak_maintenance'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'cognitive_load': ['task_chunking', 'complexity_reduction', 'context_switching_minimization']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_score': 1.0,
            'recent_interventions': [],
            'successful_strategies': set(),
            'improvement_areas': set()
        }

    def generate_personalized_nudge(self, user_state, personality_type):
        """Generate contextually relevant and personalized coaching intervention"""
        config = self.personality_type_configs[personality_type]
        
        # Assess current context
        cognitive_capacity = self._assess_cognitive_capacity(user_state)
        optimal_timing = self._check_intervention_timing(user_state)
        
        if not optimal_timing:
            return None

        # Select appropriate intervention
        intervention = self._select_intervention(user_state, config)
        
        # Personalize based on user preferences and state
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            config,
            cognitive_capacity
        )

        return {
            'message': self._format_message(personalized_actions, config),
            'actions': personalized_actions,
            'follow_up': intervention['follow_up'],
            'metrics': self._define_success_metrics(personalized_actions)
        }

    def _assess_cognitive_capacity(self, user_state):
        """Evaluate user's current cognitive load and capacity"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'time_pressure': user_state.get('time_pressure', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'energy_level': user_state.get('energy', 0.8)
        }
        
        return 1.0 - (sum(factors.values()) / len(factors))

    def _check_intervention_timing(self, user_state):
        """Determine if timing is appropriate for intervention"""
        last_intervention = self.user_context['recent_interventions'][-1] if self.user_context['recent_interventions'] else None
        
        if last_intervention:
            time_elapsed = user_state['timestamp'] - last_intervention['timestamp']
            if time_elapsed < 900:  # 15 minutes minimum between interventions
                return False
                
        return True

    def _select_intervention(self, user_state, config):
        """Select most appropriate intervention based on context"""
        triggers = self._identify_triggers(user_state)
        
        best_match = None
        best_score = -1
        
        for name, intervention in self.intervention_templates.items():
            match_score = len(set(triggers) & set(intervention['triggers']))
            if match_score > best_score:
                best_score = match_score
                best_match = intervention
                
        return best_match

    def _personalize_actions(self, actions, config, cognitive_capacity):
        """Customize actions based on user preferences and state"""
        personalized = []
        
        for action in actions:
            if cognitive_capacity < config['cognitive_load_threshold']:
                # Simplify actions when cognitive load is high
                action['steps'] = action['steps'][:2]
                action['duration'] *= 0.7
            
            action['style'] = config['communication_pref']
            action['learning_approach'] = config['learning_style']
            
            personalized.append(action)
            
        return personalized

    def _format_message(self, actions, config):
        """Format coaching message according to user preferences"""
        style = config['communication_pref']
        
        if style == 'direct':
            return self._format_direct_message(actions)
        elif style == 'enthusiastic':
            return self._format_enthusiastic_message(actions)
        
        return self._format_neutral_message(actions)

    def _define_success_metrics(self, actions):
        """Define measurable success metrics for interventions"""
        return {
            'completion_rate': 'Percentage of action steps completed',
            'time_to_implement': 'Time taken to complete all actions',
            'perceived_difficulty': 'User-reported difficulty (1-5 scale)',
            'effectiveness': 'User-reported effectiveness (1-5 scale)',
            'behavioral_change': 'Observable change in target behavior'
        }

    def update_user_context(self, interaction_results):
        """Update user context based on intervention results"""
        self.user_context['recent_interventions'].append(interaction_results)
        
        if interaction_results['success']:
            self.user_context['successful_strategies'].add(
                interaction_results['intervention_type']
            )
        else:
            self.user_context['improvement_areas'].add(
                interaction_results['intervention_type']
            )
            
        self._update_effectiveness_metrics(interaction_results)