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
                'motivation_triggers': ['novelty', 'social', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'description': 'Enable focus mode for 25 minutes',
                     'time_estimate': 25,
                     'success_metric': 'Completed focused work session',
                     'priority': 'high'
                    },
                    {'description': 'Clear workspace of distractions',
                     'time_estimate': 5,
                     'success_metric': 'Removed visual/audio distractions',
                     'priority': 'medium'
                    }
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus'],
                'actions': [
                    {'description': 'Take a 5 minute movement break',
                     'time_estimate': 5,
                     'success_metric': 'Completed physical activity',
                     'priority': 'high'
                    }
                ],
                'follow_up': {'timing': 5, 'type': 'energy_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_duration': 0,
            'task_switches': 0,
            'successful_interventions': []
        }

    def generate_recommendation(self, user_data, context):
        """Generate personalized coaching recommendation"""
        personality_type = user_data.get('personality_type', 'INTJ')
        user_config = self.personality_type_configs[personality_type]

        # Analyze current context
        cognitive_load = self._assess_cognitive_load(context)
        energy_level = self._assess_energy_level(context)
        task_complexity = self._assess_task_complexity(context)

        # Select appropriate intervention
        if cognitive_load > user_config['cognitive_load_threshold']:
            intervention = self.intervention_templates['break']
        elif context.get('distractions', 0) > 3:
            intervention = self.intervention_templates['focus']
        else:
            intervention = self._select_optimal_intervention(user_config, context)

        # Personalize intervention
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config,
            context
        )

        # Add behavioral reinforcement
        motivation_elements = self._add_motivation_elements(
            user_config['motivation_triggers'],
            personalized_actions
        )

        return {
            'actions': personalized_actions,
            'motivation': motivation_elements,
            'follow_up': intervention['follow_up']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'interruptions': context.get('interruptions', 0) * 0.1,
            'time_pressure': context.get('deadline_proximity', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _assess_energy_level(self, context):
        """Assess user energy level"""
        factors = {
            'time_active': context.get('time_active', 0),
            'break_frequency': context.get('breaks_taken', 0),
            'task_intensity': context.get('task_intensity', 0.5)
        }
        return 1.0 - (sum(factors.values()) / len(factors))

    def _assess_task_complexity(self, context):
        """Assess task complexity"""
        return context.get('task_complexity', 0.5)

    def _select_optimal_intervention(self, user_config, context):
        """Select best intervention based on user config and context"""
        # Implementation of intervention selection logic
        pass

    def _personalize_actions(self, actions, user_config, context):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            # Adjust language based on communication preference
            description = self._adjust_language(
                action['description'],
                user_config['communication_pref']
            )
            
            # Adjust time estimates based on work pattern
            time_estimate = self._adjust_time_estimate(
                action['time_estimate'],
                user_config['work_pattern']
            )

            personalized.append({
                **action,
                'description': description,
                'time_estimate': time_estimate
            })
        return personalized

    def _add_motivation_elements(self, triggers, actions):
        """Add motivation elements based on user triggers"""
        motivation_elements = []
        for trigger in triggers:
            if trigger == 'mastery':
                motivation_elements.append({
                    'type': 'progress_tracking',
                    'metric': 'skill_improvement'
                })
            elif trigger == 'autonomy':
                motivation_elements.append({
                    'type': 'choice_provision',
                    'options': len(actions)
                })
            # Additional motivation elements...
        return motivation_elements

    def update_user_context(self, new_context):
        """Update tracked user context"""
        self.user_context.update(new_context)

    def track_intervention_success(self, intervention_id, success_metrics):
        """Track success of interventions"""
        self.user_context['successful_interventions'].append({
            'id': intervention_id,
            'metrics': success_metrics,
            'timestamp': time.time()
        })