class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning patterns
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types omitted for brevity
        }

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['context:high_distraction', 'time:extended_work'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2min', 'priority': 1},
                    {'step': 'Enable focus mode', 'time_est': '1min', 'priority': 1},
                    {'step': 'Set timer for focused work', 'time_est': '1min', 'priority': 2}
                ],
                'success_metrics': ['Time on task', 'Distraction count'],
                'follow_up': {'timing': '+30min', 'type': 'check_completion'}
            },
            'break': {
                'triggers': ['time:extended_focus', 'biometrics:fatigue'],
                'actions': [
                    {'step': 'Stand and stretch', 'time_est': '2min', 'priority': 1},
                    {'step': 'Short walk', 'time_est': '5min', 'priority': 2},
                    {'step': 'Hydration break', 'time_est': '1min', 'priority': 1}
                ],
                'success_metrics': ['Break completion', 'Return to focus'],
                'follow_up': {'timing': '+10min', 'type': 'energy_check'}
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_celebration'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_system']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_duration': 0,
            'break_timing': [],
            'task_completion': [],
            'intervention_responses': []
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Context analysis
        cognitive_load = self._assess_cognitive_load(current_context)
        optimal_timing = self._calculate_intervention_timing(current_context)
        
        if not optimal_timing:
            return None

        # Select appropriate intervention
        intervention = self._select_intervention(
            personality_config,
            cognitive_load,
            current_context
        )

        # Personalize intervention
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            personality_config,
            user_profile['preferences']
        )

        return {
            'type': intervention['type'],
            'actions': personalized_actions,
            'timing': optimal_timing,
            'success_metrics': intervention['success_metrics'],
            'follow_up': intervention['follow_up']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3),
            'task_familiarity': context.get('familiarity', 0.7)
        }
        
        return sum(factors.values()) / len(factors)

    def _calculate_intervention_timing(self, context):
        """Determine optimal intervention timing"""
        current_focus = context.get('focus_duration', 0)
        last_break = context.get('last_break_time', 0)
        energy_level = context.get('energy_level', 0.5)

        if current_focus > 45 and (time.time() - last_break) > 3000:
            return 'immediate'
        elif energy_level < 0.3:
            return 'next_breakpoint'
        return None

    def _select_intervention(self, personality_config, cognitive_load, context):
        """Select appropriate intervention based on personality and context"""
        if cognitive_load > 0.7:
            return self.intervention_templates['break']
        elif context.get('distractions', 0) > 3:
            return self.intervention_templates['focus']
        return self._get_default_intervention(personality_config)

    def _personalize_actions(self, actions, personality_config, preferences):
        """Personalize intervention actions based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality_config['communication_pref']
            modified_action['format'] = preferences.get('preferred_format', 'text')
            personalized.append(modified_action)
        return personalized

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track effectiveness of interventions"""
        self.user_context['intervention_responses'].append({
            'intervention_id': intervention_id,
            'response': user_response,
            'timestamp': time.time(),
            'context': self.user_context.copy()
        })
        
        self._update_intervention_models(intervention_id, user_response)

    def _update_intervention_models(self, intervention_id, response):
        """Update intervention effectiveness models"""
        # Implementation for updating ML models based on intervention effectiveness
        pass

    def get_progress_report(self):
        """Generate progress report with actionable insights"""
        return {
            'intervention_effectiveness': self._calculate_effectiveness(),
            'behavior_changes': self._analyze_behavior_changes(),
            'recommendations': self._generate_recommendations()
        }