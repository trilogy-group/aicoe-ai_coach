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
                     'steps': ['Set timer', 'Work in focused sprint', 'Take 5min break']}
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify barrier', 'Break into smaller steps', 'Set micro-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['Quick exercise', 'Power pose', 'Success visualization']}
                ],
                'follow_up': {'timing': 15, 'type': 'progress_check'}
            }
            # Additional templates...
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'interruption_frequency': None,
            'deadline_pressure': None
        }

        # Behavioral tracking
        self.user_metrics = {
            'intervention_responses': [],
            'completion_rates': {},
            'engagement_patterns': {},
            'progress_markers': {},
            'behavioral_changes': {}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant and personalized intervention"""
        
        # Update context awareness
        self.update_context(user_context)
        
        # Select appropriate intervention based on context
        intervention = self.select_intervention(personality_type)
        
        # Personalize based on user preferences and patterns
        personalized_actions = self.personalize_actions(
            intervention, 
            personality_type,
            self.user_metrics['engagement_patterns']
        )
        
        return self.format_nudge(personalized_actions)

    def update_context(self, context_data):
        """Update context awareness parameters"""
        for factor in self.context_factors:
            if factor in context_data:
                self.context_factors[factor] = context_data[factor]

    def select_intervention(self, personality_type):
        """Select most appropriate intervention template"""
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate intervention scores based on context match
        scores = {}
        for template_name, template in self.intervention_templates.items():
            score = self.calculate_context_match(template, user_config)
            scores[template_name] = score
            
        return self.intervention_templates[max(scores, key=scores.get)]

    def calculate_context_match(self, template, user_config):
        """Calculate how well intervention matches current context"""
        score = 0
        
        # Check trigger relevance
        for trigger in template['triggers']:
            if self.is_trigger_active(trigger):
                score += 1
                
        # Check cognitive load
        current_load = self.estimate_cognitive_load()
        if current_load <= user_config['cognitive_load_threshold']:
            score += 1
            
        # Check motivation alignment
        if any(trigger in user_config['motivation_triggers'] for trigger in template['triggers']):
            score += 1
            
        return score

    def personalize_actions(self, intervention, personality_type, engagement_history):
        """Personalize intervention actions based on user preferences"""
        user_config = self.personality_type_configs[personality_type]
        
        personalized = {
            'actions': [],
            'communication_style': user_config['communication_pref'],
            'timing': self.optimize_timing(engagement_history)
        }
        
        for action in intervention['actions']:
            modified_action = self.adapt_action(
                action,
                user_config['learning_style'],
                user_config['work_pattern']
            )
            personalized['actions'].append(modified_action)
            
        return personalized

    def format_nudge(self, personalized_intervention):
        """Format intervention into user-friendly nudge"""
        nudge = {
            'message': self.generate_message(
                personalized_intervention['actions'],
                personalized_intervention['communication_style']
            ),
            'specific_steps': self.format_action_steps(
                personalized_intervention['actions']
            ),
            'timing': personalized_intervention['timing'],
            'follow_up': self.schedule_follow_up(
                personalized_intervention['actions']
            )
        }
        return nudge

    def track_response(self, nudge_id, user_response):
        """Track user response to intervention"""
        self.user_metrics['intervention_responses'].append({
            'nudge_id': nudge_id,
            'response': user_response,
            'timestamp': self.get_current_time(),
            'context': self.context_factors.copy()
        })
        
        self.update_effectiveness_metrics(nudge_id, user_response)

    def estimate_cognitive_load(self):
        """Estimate current cognitive load based on context"""
        load = 0
        if self.context_factors['task_complexity']:
            load += self.context_factors['task_complexity'] * 0.4
        if self.context_factors['interruption_frequency']:
            load += self.context_factors['interruption_frequency'] * 0.3
        if self.context_factors['deadline_pressure']:
            load += self.context_factors['deadline_pressure'] * 0.3
        return min(load, 1.0)