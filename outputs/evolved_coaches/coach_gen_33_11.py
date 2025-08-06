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
                'follow_up': True
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy'],
                'actions': [
                    {'type': 'goal_reminder', 'duration': 2, 'impact': 0.6},
                    {'type': 'small_win', 'duration': 10, 'impact': 0.7},
                    {'type': 'accountability', 'duration': 5, 'impact': 0.8}
                ],
                'follow_up': True
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate', 'intermittent', 'social'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose']
        }

        self.user_context = {}
        self.intervention_history = []
        self.success_metrics = {}

    def analyze_user_context(self, context_data):
        """Analyze user context for personalized interventions"""
        cognitive_load = self._estimate_cognitive_load(context_data)
        attention_state = self._assess_attention_state(context_data)
        energy_level = self._evaluate_energy_level(context_data)
        
        self.user_context = {
            'cognitive_load': cognitive_load,
            'attention_state': attention_state,
            'energy_level': energy_level,
            'time_of_day': context_data.get('time'),
            'current_task': context_data.get('task'),
            'recent_activity': context_data.get('activity')
        }
        
        return self.user_context

    def generate_intervention(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['type']]
        
        # Select appropriate intervention template
        template = self._select_intervention_template(context)
        
        # Personalize actions based on user traits
        actions = self._personalize_actions(
            template['actions'],
            personality_config,
            context
        )
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(actions)
        
        intervention = {
            'type': template['type'],
            'actions': enhanced_actions,
            'timing': self._optimize_timing(context),
            'delivery_style': personality_config['communication_pref'],
            'success_metrics': self._define_success_metrics(enhanced_actions),
            'follow_up_schedule': self._create_follow_up_schedule(enhanced_actions)
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def track_effectiveness(self, intervention_id, metrics):
        """Track intervention effectiveness and adapt strategies"""
        self.success_metrics[intervention_id] = metrics
        self._update_intervention_weights(metrics)
        self._adapt_strategies(metrics)
        return self._generate_effectiveness_report(intervention_id)

    def _estimate_cognitive_load(self, context):
        """Estimate current cognitive load based on context"""
        factors = {
            'task_complexity': 0.3,
            'interruption_frequency': 0.2,
            'time_pressure': 0.3,
            'decision_density': 0.2
        }
        
        load = sum(factors[f] * context.get(f, 0) for f in factors)
        return min(load, 1.0)

    def _personalize_actions(self, actions, personality_config, context):
        """Personalize intervention actions based on user traits and context"""
        personalized = []
        for action in actions:
            adapted_action = {
                'step': action['type'],
                'duration': self._adjust_duration(
                    action['duration'],
                    personality_config['work_pattern']
                ),
                'style': personality_config['communication_pref'],
                'difficulty': self._adjust_difficulty(
                    action['impact'],
                    context['cognitive_load']
                ),
                'motivation_hook': self._select_motivation_trigger(
                    personality_config['motivation_triggers']
                )
            }
            personalized.append(adapted_action)
        return personalized

    def _apply_behavior_principles(self, actions):
        """Apply behavioral psychology principles to enhance effectiveness"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action.update({
                'reinforcement': self._select_reinforcement_type(action),
                'habit_trigger': self._identify_habit_trigger(action),
                'reward_schedule': self._design_reward_schedule(action)
            })
            enhanced.append(enhanced_action)
        return enhanced

    def _optimize_timing(self, context):
        """Optimize intervention timing based on context"""
        return {
            'optimal_time': self._calculate_optimal_time(context),
            'frequency': self._determine_frequency(context),
            'spacing': self._calculate_spacing(context)
        }

    def _create_follow_up_schedule(self, actions):
        """Create follow-up schedule for intervention actions"""
        return [{
            'action': action['step'],
            'timing': self._calculate_follow_up_timing(action),
            'type': 'check_in' if action['difficulty'] > 0.7 else 'reminder'
        } for action in actions]

    def _define_success_metrics(self, actions):
        """Define specific success metrics for intervention"""
        return {
            'completion_rate': 'percentage',
            'time_to_completion': 'minutes',
            'perceived_difficulty': 'scale_1_5',
            'behavioral_change': 'binary',
            'user_satisfaction': 'scale_1_10'
        }