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
                     'description': 'Clear workspace of distractions',
                     'success_metric': 'Uninterrupted focus time'},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'description': 'Use Pomodoro technique: 25min focus + 5min break',
                     'success_metric': 'Completed pomodoros'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'description': 'Break task into smaller 15-minute chunks',
                     'success_metric': 'Tasks initiated'},
                    {'type': 'reward', 'duration': 1, 'priority': 2,
                     'description': 'Set specific reward for completion',
                     'success_metric': 'Task completion rate'}
                ],
                'follow_up': {'timing': 30, 'type': 'motivation_check'}
            }
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        current_context = self._evaluate_context(context)
        
        # Select optimal intervention based on context and user preferences
        intervention = self._select_intervention(personality_config, current_context)
        
        # Adjust for cognitive load
        if current_context['cognitive_load'] > personality_config['cognitive_load_threshold']:
            intervention = self._simplify_intervention(intervention)
            
        return self._format_nudge(intervention, personality_config)

    def _evaluate_context(self, context):
        """Evaluate current context factors"""
        cognitive_load = (
            self.context_factors['time_of_day'][context['time']] *
            self.context_factors['energy_level'][context['energy']] *
            self.context_factors['task_complexity'][context['task_type']]
        )
        
        return {
            'cognitive_load': cognitive_load,
            'prime_time': context['time'] in ['morning', 'afternoon'],
            'task_urgency': context['urgency'],
            'recent_activity': context['activity_history'][-3:]
        }

    def _select_intervention(self, personality_config, context):
        """Select most appropriate intervention based on personality and context"""
        available_interventions = self.intervention_templates.copy()
        
        # Filter by cognitive capacity
        if context['cognitive_load'] > 0.7:
            available_interventions = {k:v for k,v in available_interventions.items() 
                                    if len(v['actions']) <= 2}
            
        # Prioritize based on personality preferences
        scored_interventions = self._score_interventions(
            available_interventions,
            personality_config,
            context
        )
        
        return max(scored_interventions, key=scored_interventions.get)

    def _simplify_intervention(self, intervention):
        """Simplify intervention when cognitive load is high"""
        simplified = intervention.copy()
        simplified['actions'] = [
            action for action in intervention['actions'] 
            if action['priority'] == 1
        ]
        return simplified

    def _format_nudge(self, intervention, personality_config):
        """Format intervention according to user's communication preferences"""
        style = personality_config['communication_pref']
        
        if style == 'direct':
            return {
                'message': f"Action required: {intervention['actions'][0]['description']}",
                'duration': intervention['actions'][0]['duration'],
                'success_metric': intervention['actions'][0]['success_metric']
            }
        else:
            return {
                'message': f"Would you like to try {intervention['actions'][0]['description']}?",
                'duration': intervention['actions'][0]['duration'],
                'success_metric': intervention['actions'][0]['success_metric']
            }

    def _score_interventions(self, interventions, personality_config, context):
        """Score interventions based on predicted effectiveness"""
        scores = {}
        for name, intervention in interventions.items():
            score = 0
            # Score based on personality match
            score += sum(trigger in personality_config['motivation_triggers'] 
                        for trigger in intervention['triggers'])
            
            # Score based on context appropriateness
            score += 2 if context['prime_time'] else 0
            score += 1 if context['task_urgency'] == 'high' else 0
            
            # Penalty for recent similar interventions
            score -= sum(1 for activity in context['recent_activity'] 
                        if activity['type'] == name)
            
            scores[name] = score
            
        return scores