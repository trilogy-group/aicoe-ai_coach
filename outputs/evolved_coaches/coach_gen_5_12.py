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
                    {'type': 'technique', 'duration': 25, 'specifics': 'Use Pomodoro timer'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful pause'}
                ],
                'follow_up': {'timing': 30, 'metric': 'focus_duration'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller steps'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'metric': 'task_completion'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 1.2, 'afternoon': 1.0, 'evening': 0.8},
            'energy_level': {'high': 1.2, 'medium': 1.0, 'low': 0.8},
            'task_complexity': {'high': 0.8, 'medium': 1.0, 'low': 1.2}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.7:
            return None  # Skip if poor timing
            
        # Select appropriate intervention template
        template = self._select_intervention_template(user_context, config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(actions, config['motivation_triggers'])
        
        return {
            'timing': timing_score,
            'actions': enhanced_actions,
            'follow_up': template['follow_up'],
            'expected_impact': self._calculate_impact_score(enhanced_actions, user_context)
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        time_factor = self.context_factors['time_of_day'][context['time']]
        energy_factor = self.context_factors['energy_level'][context['energy']]
        task_factor = self.context_factors['task_complexity'][context['task_type']]
        
        return (time_factor * energy_factor * task_factor) / 3

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        relevant_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                relevance_score = self._calculate_template_relevance(template, context, config)
                relevant_templates.append((template, relevance_score))
        
        return max(relevant_templates, key=lambda x: x[1])[0]

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = config['communication_pref']
            modified_action['learning_approach'] = config['learning_style']
            personalized.append(modified_action)
        return personalized

    def _apply_behavior_principles(self, actions, motivation_triggers):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['triggers'] = self._select_motivation_triggers(action, motivation_triggers)
            enhanced_action['reinforcement'] = self._generate_reinforcement_strategy(action)
            enhanced.append(enhanced_action)
        return enhanced

    def _calculate_impact_score(self, actions, context):
        """Calculate expected impact score for interventions"""
        base_score = sum(action['duration'] for action in actions) / 100
        context_modifier = self._calculate_timing_score(context)
        return base_score * context_modifier

    def track_intervention_effectiveness(self, intervention_id, user_feedback):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking and analyzing intervention results
        pass

    def update_user_model(self, user_id, intervention_results):
        """Update user model based on intervention results"""
        # Implementation for updating user model
        pass