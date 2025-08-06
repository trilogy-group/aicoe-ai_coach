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
                     'steps': ['Set timer', 'Use Pomodoro method', 'Take structured breaks']}
                ],
                'follow_up': {'timing': '+30min', 'metric': 'focus_score'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframing', 'duration': 10, 'priority': 1,
                     'steps': ['Identify barriers', 'Break down task', 'Set micro-goals']},
                    {'type': 'reward', 'duration': 5, 'priority': 2,
                     'steps': ['Define reward', 'Set achievement criteria', 'Schedule reward']}
                ],
                'follow_up': {'timing': '+1hr', 'metric': 'task_progress'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.6:
            return None

        # Select appropriate intervention
        intervention = self._select_intervention(user_context, config)
        if not intervention:
            return None

        # Personalize action steps
        actions = self._personalize_actions(intervention['actions'], config)

        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(actions, config['motivation_triggers'])

        return {
            'type': intervention['type'],
            'actions': enhanced_actions,
            'timing': self._optimize_timing(user_context),
            'follow_up': intervention['follow_up'],
            'success_metrics': self._define_metrics(intervention)
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        task_factor = self.context_factors['task_complexity'][context['task']]
        
        return (time_factor + energy_factor + task_factor) / 3

    def _select_intervention(self, context, config):
        """Select most appropriate intervention based on context"""
        relevant_interventions = []
        for intervention_type, details in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in details['triggers']):
                relevance_score = self._calculate_relevance(details, context, config)
                relevant_interventions.append((intervention_type, relevance_score))
        
        if not relevant_interventions:
            return None
            
        return max(relevant_interventions, key=lambda x: x[1])[0]

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user configuration"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = config['communication_pref']
            modified_action['pace'] = config['work_pattern']
            modified_action['complexity'] = self._adjust_complexity(action, config)
            personalized.append(modified_action)
        return personalized

    def _apply_behavior_principles(self, actions, motivation_triggers):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['triggers'] = self._match_motivation_triggers(action, motivation_triggers)
            enhanced_action['reinforcement'] = self._generate_reinforcement(action)
            enhanced.append(enhanced_action)
        return enhanced

    def _optimize_timing(self, context):
        """Optimize intervention timing based on context"""
        return {
            'optimal_time': self._calculate_optimal_time(context),
            'frequency': self._calculate_frequency(context),
            'duration': self._calculate_duration(context)
        }

    def _define_metrics(self, intervention):
        """Define success metrics for intervention"""
        return {
            'primary': intervention['follow_up']['metric'],
            'secondary': ['engagement', 'completion', 'satisfaction'],
            'measurement_timing': intervention['follow_up']['timing']
        }

    def track_effectiveness(self, intervention_id, metrics):
        """Track intervention effectiveness for continuous improvement"""
        # Implementation for effectiveness tracking
        pass