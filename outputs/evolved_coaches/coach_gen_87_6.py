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
                     'steps': ['Clear desk', 'Close unnecessary tabs', 'Put phone away']},
                    {'type': 'technique', 'duration': 25, 'priority': 2,
                     'steps': ['Set timer for 25 minutes', 'Work on single task', 'Take 5 min break']}
                ],
                'follow_up': {'timing': 30, 'type': 'completion_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 5, 'priority': 1,
                     'steps': ['Identify specific barrier', 'Break into smaller steps', 'Set micro-goal']},
                    {'type': 'energize', 'duration': 10, 'priority': 2,
                     'steps': ['Quick exercise', 'Deep breathing', 'Review purpose']}
                ],
                'follow_up': {'timing': 15, 'type': 'progress_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['implementation_intention', 'environmental_design', 'reward_scheduling'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof'],
            'focus': ['attention_management', 'cognitive_load', 'context_switching']
        }

        # Progress tracking
        self.user_metrics = {
            'engagement': 0.0,
            'completion_rate': 0.0,
            'behavior_change': 0.0,
            'satisfaction': 0.0
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze context and cognitive load
        current_load = self._assess_cognitive_load(user_context)
        if current_load > user_config['cognitive_load_threshold']:
            return self._generate_simplified_nudge(user_context)

        # Select relevant intervention template
        template = self._select_intervention_template(user_context)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], user_config)
        
        # Add behavioral psychology elements
        motivation_elements = self._add_motivation_triggers(
            user_config['motivation_triggers']
        )

        return {
            'message': self._format_message(actions, user_config['communication_pref']),
            'actions': actions,
            'motivation': motivation_elements,
            'follow_up': template['follow_up']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruptions': context.get('interruption_frequency', 0.3),
            'fatigue': context.get('energy_level', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _select_intervention_template(self, context):
        """Select most relevant intervention template"""
        # Match context triggers to templates
        matches = []
        for template_name, template in self.intervention_templates.items():
            score = sum(1 for trigger in template['triggers'] if trigger in context)
            matches.append((score, template_name))
        
        best_match = max(matches, key=lambda x: x[0])[1]
        return self.intervention_templates[best_match]

    def _personalize_actions(self, actions, user_config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            if user_config['learning_style'] == 'systematic':
                modified_action['steps'] = self._add_metrics(action['steps'])
            elif user_config['learning_style'] == 'exploratory':
                modified_action['steps'] = self._add_alternatives(action['steps'])
            personalized.append(modified_action)
        return personalized

    def _add_motivation_triggers(self, triggers):
        """Add motivation elements based on behavioral psychology"""
        motivation_elements = []
        for trigger in triggers:
            if trigger in self.behavior_triggers['motivation']:
                motivation_elements.append({
                    'type': trigger,
                    'technique': self._get_motivation_technique(trigger)
                })
        return motivation_elements

    def _format_message(self, actions, communication_style):
        """Format message according to communication preference"""
        if communication_style == 'direct':
            return self._format_direct_message(actions)
        return self._format_encouraging_message(actions)

    def update_metrics(self, interaction_results):
        """Update user engagement and effectiveness metrics"""
        self.user_metrics['engagement'] = (
            self.user_metrics['engagement'] * 0.7 + 
            interaction_results['engagement'] * 0.3
        )
        self.user_metrics['completion_rate'] = (
            self.user_metrics['completion_rate'] * 0.7 +
            interaction_results['completion'] * 0.3
        )
        self.user_metrics['behavior_change'] = (
            self.user_metrics['behavior_change'] * 0.8 +
            interaction_results['behavior_change'] * 0.2
        )
        self.user_metrics['satisfaction'] = (
            self.user_metrics['satisfaction'] * 0.7 +
            interaction_results['satisfaction'] * 0.3
        )