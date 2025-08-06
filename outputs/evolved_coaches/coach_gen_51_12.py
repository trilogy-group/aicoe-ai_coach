class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced traits and learning patterns
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'achievement', 'efficiency'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'creativity', 'social_impact'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Focus time logged'}
                ],
                'follow_up': {'timing': 30, 'type': 'check_completion'}
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines', 'task_overload'],
                'actions': [
                    {'step': 'Break down project into smaller tasks',
                     'time_estimate': '10 min',
                     'success_metric': 'Tasks created'},
                    {'step': 'Prioritize tasks using urgency/importance matrix',
                     'time_estimate': '5 min', 
                     'success_metric': 'Tasks prioritized'}
                ],
                'follow_up': {'timing': 60, 'type': 'review_progress'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'persuasion': ['reciprocity', 'commitment', 'social_proof']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_state': 'fresh',
            'recent_interventions': [],
            'success_metrics': {}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        
        # Get personality-specific configurations
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Assess current cognitive load and energy state
        cognitive_load = self._assess_cognitive_load(current_context)
        self.user_context['cognitive_load'] = cognitive_load

        # Select appropriate intervention based on context
        intervention = self._select_intervention(
            personality_config,
            cognitive_load,
            current_context
        )

        # Personalize intervention content
        personalized_content = self._personalize_content(
            intervention,
            personality_config,
            user_profile
        )

        # Add behavioral psychology elements
        enhanced_content = self._apply_behavior_principles(
            personalized_content,
            personality_config['motivation_triggers']
        )

        return enhanced_content

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context factors"""
        load_factors = {
            'active_tasks': 0.1,
            'interruptions': 0.15,
            'time_pressure': 0.2,
            'task_complexity': 0.25
        }
        
        cognitive_load = sum(
            load_factors[factor] * context.get(factor, 0) 
            for factor in load_factors
        )
        
        return min(cognitive_load, 1.0)

    def _select_intervention(self, personality_config, cognitive_load, context):
        """Select most appropriate intervention based on user state"""
        if cognitive_load > personality_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        
        if context.get('task_overload', False):
            return self.intervention_templates['planning']
            
        # Additional intervention selection logic...
        return self._get_default_intervention()

    def _personalize_content(self, intervention, personality_config, user_profile):
        """Personalize intervention content for user"""
        content = {
            'message': self._format_message(
                intervention,
                personality_config['communication_pref']
            ),
            'actions': self._adapt_actions(
                intervention['actions'],
                personality_config['learning_style']
            ),
            'timing': self._optimize_timing(
                user_profile['peak_hours'],
                self.user_context['energy_level']
            )
        }
        
        return content

    def _apply_behavior_principles(self, content, motivation_triggers):
        """Apply behavioral psychology principles to content"""
        enhanced = content.copy()
        
        # Add motivation elements
        enhanced['motivation'] = {
            'trigger': self._select_motivation_trigger(motivation_triggers),
            'reinforcement': self._generate_reinforcement(),
            'social_proof': self._get_social_proof()
        }
        
        # Add habit formation elements
        enhanced['habit'] = {
            'cue': self._identify_habit_cue(),
            'routine': content['actions'],
            'reward': self._generate_reward()
        }
        
        return enhanced

    def track_intervention_success(self, intervention_id, metrics):
        """Track success metrics for interventions"""
        self.user_context['success_metrics'][intervention_id] = metrics
        self._update_intervention_effectiveness(intervention_id, metrics)

    def _get_default_intervention(self):
        """Return default intervention template"""
        return self.intervention_templates['focus']

    def _format_message(self, intervention, communication_style):
        """Format message according to communication preferences"""
        # Message formatting logic
        pass

    def _adapt_actions(self, actions, learning_style):
        """Adapt action steps to learning style"""
        # Action adaptation logic
        pass

    def _optimize_timing(self, peak_hours, energy_level):
        """Optimize intervention timing"""
        # Timing optimization logic
        pass

    def _select_motivation_trigger(self, triggers):
        """Select appropriate motivation trigger"""
        # Trigger selection logic
        pass

    def _generate_reinforcement(self):
        """Generate reinforcement strategy"""
        # Reinforcement generation logic
        pass

    def _get_social_proof(self):
        """Get relevant social proof"""
        # Social proof logic
        pass

    def _identify_habit_cue(self):
        """Identify appropriate habit formation cue"""
        # Habit cue identification logic
        pass

    def _generate_reward(self):
        """Generate appropriate reward"""
        # Reward generation logic
        pass

    def _update_intervention_effectiveness(self, intervention_id, metrics):
        """Update intervention effectiveness based on metrics"""
        # Effectiveness updating logic
        pass