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
                    {'type': 'environment', 'duration': 15, 'specifics': 'Clear workspace of distractions'},
                    {'type': 'technique', 'duration': 25, 'specifics': 'Use Pomodoro method'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful pause'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into smaller chunks'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'type': 'achievement_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['positive', 'negative', 'intermittent'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_performance': None
        }

        # User engagement tracking
        self.user_metrics = {
            'intervention_response_rate': 0.0,
            'completion_rate': 0.0,
            'satisfaction_score': 0.0,
            'behavior_change_index': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Update context awareness
        self.update_context(user_context)
        
        # Select appropriate intervention template
        template = self.select_intervention_template()
        
        # Personalize based on personality type
        config = self.personality_type_configs[personality_type]
        
        # Apply behavioral psychology principles
        nudge = self.apply_behavior_principles(template, config)
        
        # Adjust for cognitive load
        nudge = self.optimize_cognitive_load(nudge, config['cognitive_load_threshold'])
        
        return nudge

    def update_context(self, user_context):
        """Update context awareness parameters"""
        for factor in user_context:
            if factor in self.context_factors:
                self.context_factors[factor] = user_context[factor]

    def select_intervention_template(self):
        """Select most appropriate intervention template based on context"""
        # Implementation of template selection logic
        best_template = None
        highest_relevance = 0
        
        for template_name, template in self.intervention_templates.items():
            relevance = self.calculate_template_relevance(template)
            if relevance > highest_relevance:
                highest_relevance = relevance
                best_template = template
                
        return best_template

    def apply_behavior_principles(self, template, personality_config):
        """Apply behavioral psychology principles to intervention"""
        enhanced_template = template.copy()
        
        # Add motivation triggers
        for trigger in personality_config['motivation_triggers']:
            enhanced_template['actions'].append({
                'type': 'motivation',
                'duration': 5,
                'specifics': f'Leverage {trigger} motivation'
            })
            
        # Apply reinforcement strategy
        enhanced_template['reinforcement'] = self.select_reinforcement_strategy()
        
        return enhanced_template

    def optimize_cognitive_load(self, nudge, threshold):
        """Optimize intervention for cognitive load"""
        current_load = self.estimate_cognitive_load(nudge)
        
        while current_load > threshold:
            # Simplify actions if cognitive load too high
            if len(nudge['actions']) > 1:
                nudge['actions'].pop()
            current_load = self.estimate_cognitive_load(nudge)
            
        return nudge

    def estimate_cognitive_load(self, nudge):
        """Estimate cognitive load of intervention"""
        load = 0.0
        for action in nudge['actions']:
            load += action['duration'] / 60.0  # Convert to hours
        return load

    def select_reinforcement_strategy(self):
        """Select appropriate reinforcement strategy"""
        return {
            'type': 'positive',
            'schedule': 'intermittent',
            'reward_type': 'achievement_based'
        }

    def track_engagement(self, user_response):
        """Track user engagement metrics"""
        self.user_metrics['intervention_response_rate'] = user_response['response_rate']
        self.user_metrics['completion_rate'] = user_response['completion_rate']
        self.user_metrics['satisfaction_score'] = user_response['satisfaction']
        self.user_metrics['behavior_change_index'] = user_response['behavior_change']

    def calculate_template_relevance(self, template):
        """Calculate relevance score for intervention template"""
        relevance = 0.0
        for trigger in template['triggers']:
            if self.is_trigger_relevant(trigger):
                relevance += 1.0
        return relevance / len(template['triggers'])

    def is_trigger_relevant(self, trigger):
        """Check if trigger is relevant to current context"""
        # Implementation of trigger relevance checking
        return True  # Placeholder