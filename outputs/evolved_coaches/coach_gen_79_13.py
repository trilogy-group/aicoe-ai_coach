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
                    {'description': 'Enable focus mode for 25 minutes',
                     'time_estimate': 25,
                     'success_metric': 'Completed focused work session',
                     'priority': 'high'},
                    {'description': 'Clear workspace of distractions',
                     'time_estimate': 5,
                     'success_metric': 'Distraction-free environment',
                     'priority': 'medium'}
                ],
                'follow_up': {'timing': 30, 'type': 'check_completion'}
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines'],
                'actions': [
                    {'description': 'Break project into max 2-hour tasks',
                     'time_estimate': 15,
                     'success_metric': 'Task list created',
                     'priority': 'high'},
                    {'description': 'Schedule top 3 priorities',
                     'time_estimate': 10,
                     'success_metric': 'Calendar updated',
                     'priority': 'high'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'habit_formation': {
                'cue': None,
                'routine': None,
                'reward': None,
                'min_repetitions': 21
            },
            'motivation': {
                'autonomy': 0.0,
                'mastery': 0.0,
                'purpose': 0.0
            },
            'cognitive_load': {
                'current': 0.0,
                'threshold': 0.7,
                'recovery_time': 45
            }
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Assess cognitive load
        current_load = self._assess_cognitive_load(user_context)
        if current_load > config['cognitive_load_threshold']:
            return self._generate_recovery_intervention()

        # Match intervention to context
        relevant_triggers = self._identify_triggers(user_context)
        best_intervention = self._select_intervention(relevant_triggers, config)
        
        return self._personalize_intervention(best_intervention, config)

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        load_factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruptions': context.get('interruption_frequency', 0.3),
            'task_switching': context.get('task_switches', 0.4)
        }
        return sum(load_factors.values()) / len(load_factors)

    def _identify_triggers(self, context):
        """Identify relevant intervention triggers from context"""
        triggers = []
        if context.get('focus_duration', 0) < 15:
            triggers.append('distraction')
        if context.get('task_switches', 0) > 5:
            triggers.append('task_switching')
        if context.get('overdue_tasks', 0) > 0:
            triggers.append('missed_deadlines')
        return triggers

    def _select_intervention(self, triggers, config):
        """Select most appropriate intervention based on triggers and user config"""
        matching_interventions = []
        for intervention_type, intervention in self.intervention_templates.items():
            if any(trigger in intervention['triggers'] for trigger in triggers):
                matching_interventions.append(intervention)
        
        return self._rank_interventions(matching_interventions, config)[0]

    def _personalize_intervention(self, intervention, config):
        """Customize intervention based on user preferences and style"""
        personalized = intervention.copy()
        
        # Adjust communication style
        if config['communication_pref'] == 'direct':
            personalized['tone'] = 'clear and concise'
        elif config['communication_pref'] == 'enthusiastic':
            personalized['tone'] = 'energetic and encouraging'

        # Adjust for learning style
        if config['learning_style'] == 'systematic':
            personalized['format'] = 'structured_steps'
        elif config['learning_style'] == 'exploratory':
            personalized['format'] = 'discovery_based'

        # Add motivation triggers
        personalized['motivation_elements'] = config['motivation_triggers']

        return personalized

    def _generate_recovery_intervention(self):
        """Generate intervention for cognitive load recovery"""
        return {
            'type': 'recovery',
            'actions': [
                {'description': 'Take a 5-minute break',
                 'time_estimate': 5,
                 'success_metric': 'Completed break',
                 'priority': 'high'},
                {'description': 'Deep breathing exercise',
                 'time_estimate': 2,
                 'success_metric': 'Reduced stress',
                 'priority': 'medium'}
            ],
            'follow_up': {'timing': 7, 'type': 'wellbeing_check'}
        }

    def _rank_interventions(self, interventions, config):
        """Rank interventions by predicted effectiveness"""
        scored_interventions = []
        for intervention in interventions:
            score = self._calculate_intervention_score(intervention, config)
            scored_interventions.append((score, intervention))
        
        return [i[1] for i in sorted(scored_interventions, reverse=True)]

    def _calculate_intervention_score(self, intervention, config):
        """Calculate effectiveness score for an intervention"""
        score = 0
        score += len(intervention['actions']) * 0.2
        score += 0.3 if intervention.get('follow_up') else 0
        score += sum(1 for trigger in config['motivation_triggers'] 
                    if trigger in str(intervention)) * 0.1
        return score