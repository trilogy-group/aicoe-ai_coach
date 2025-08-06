class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced traits and learning patterns
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
                'motivation_triggers': ['novelty', 'connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting applications',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Mode activated'},
                    {'step': 'Set timer for focused work block',
                     'time_estimate': '1 min', 
                     'success_metric': 'Timer started'}
                ],
                'follow_up_interval': 25,
                'priority_level': 'high'
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus', 'stress_signals'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Hydrate and rest eyes',
                     'time_estimate': '3 min',
                     'success_metric': 'Break taken'}
                ],
                'follow_up_interval': 15,
                'priority_level': 'medium'
            }
            # Additional intervention types
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': {
                'cue': None,
                'routine': None,
                'reward': None,
                'craving': None
            },
            'motivation': {
                'autonomy': 0.0,
                'competence': 0.0,
                'relatedness': 0.0
            }
        }

        # Context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_duration': 0,
            'task_complexity': 0.0,
            'interruption_frequency': 0.0
        }

        # Performance metrics
        self.metrics = {
            'nudge_effectiveness': [],
            'behavior_changes': [],
            'user_satisfaction': [],
            'intervention_relevance': [],
            'action_completion': []
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate personalized intervention based on user context and patterns"""
        personality_type = self.get_user_personality(user_id)
        config = self.personality_type_configs[personality_type]
        
        # Update context tracking
        self.update_user_context(context)
        
        # Select appropriate intervention
        intervention = self.select_intervention(config)
        
        # Personalize based on user preferences
        personalized_actions = self.personalize_actions(
            intervention['actions'],
            config['learning_style'],
            config['communication_pref']
        )
        
        # Apply behavioral psychology
        motivated_actions = self.apply_motivation_techniques(
            personalized_actions,
            config['motivation_triggers']
        )
        
        return {
            'actions': motivated_actions,
            'timing': self.optimize_timing(context),
            'priority': intervention['priority_level'],
            'follow_up': intervention['follow_up_interval']
        }

    def update_user_context(self, context):
        """Update user context tracking with new data"""
        self.user_context['cognitive_load'] = self.calculate_cognitive_load(context)
        self.user_context['energy_level'] = self.estimate_energy_level(context)
        self.user_context['focus_duration'] = context.get('focus_duration', 0)
        self.user_context['task_complexity'] = self.assess_task_complexity(context)
        self.user_context['interruption_frequency'] = context.get('interruptions', 0)

    def select_intervention(self, config):
        """Select most appropriate intervention based on context"""
        if self.user_context['cognitive_load'] > config['cognitive_load_threshold']:
            return self.intervention_templates['break']
        elif self.user_context['interruption_frequency'] > 5:
            return self.intervention_templates['focus']
        # Additional intervention selection logic
        return self.intervention_templates['focus']

    def personalize_actions(self, actions, learning_style, communication_pref):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            if learning_style == 'systematic':
                modified_action['step'] = f"Step {len(personalized)+1}: {action['step']}"
            if communication_pref == 'direct':
                modified_action['step'] = modified_action['step'].replace('Consider', 'Do')
            personalized.append(modified_action)
        return personalized

    def apply_motivation_techniques(self, actions, motivation_triggers):
        """Apply motivation techniques to increase engagement"""
        motivated_actions = []
        for action in actions:
            enhanced_action = action.copy()
            if 'mastery' in motivation_triggers:
                enhanced_action['progress_tracking'] = True
            if 'autonomy' in motivation_triggers:
                enhanced_action['alternatives'] = self.generate_alternatives(action)
            motivated_actions.append(enhanced_action)
        return motivated_actions

    def optimize_timing(self, context):
        """Optimize intervention timing based on user context"""
        if self.user_context['cognitive_load'] > 0.7:
            return 'immediate'
        elif self.user_context['focus_duration'] > 45:
            return 'next_break'
        return 'default'

    def track_effectiveness(self, nudge_id, metrics):
        """Track intervention effectiveness"""
        self.metrics['nudge_effectiveness'].append(metrics['effectiveness'])
        self.metrics['behavior_changes'].append(metrics['behavior_change'])
        self.metrics['user_satisfaction'].append(metrics['satisfaction'])
        self.metrics['intervention_relevance'].append(metrics['relevance'])
        self.metrics['action_completion'].append(metrics['completion'])