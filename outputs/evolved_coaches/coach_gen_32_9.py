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
                'motivation_triggers': ['novelty', 'connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 25, 'specifics': 'Clear workspace, close unnecessary tabs'},
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min work blocks'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a short walk, stretch exercises'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 15, 'specifics': 'Break task into 3 achievable sub-goals'},
                    {'type': 'reward', 'duration': 30, 'specifics': 'Define concrete reward for completion'},
                    {'type': 'accountability', 'duration': 10, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 120, 'type': 'motivation_check'}
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
            'time_of_day': ['morning', 'afternoon', 'evening'],
            'energy_level': ['high', 'medium', 'low'],
            'task_complexity': ['simple', 'moderate', 'complex'],
            'environment': ['office', 'home', 'mobile']
        }

    def generate_personalized_intervention(self, user_profile, context, current_state):
        """Generate personalized coaching intervention based on user context and state"""
        
        # Get personality-specific configurations
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Analyze current context
        context_score = self._evaluate_context_fit(context, personality_config)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(current_state, context_score)
        
        # Personalize intervention
        intervention = self._personalize_intervention(template, personality_config, context)
        
        return intervention

    def _evaluate_context_fit(self, context, personality_config):
        """Evaluate how well current context matches user preferences"""
        context_score = 0
        
        # Check time of day alignment
        if context['time'] in self.context_factors['time_of_day']:
            context_score += 0.3
            
        # Check energy level match
        if context['energy'] == personality_config['work_pattern']:
            context_score += 0.4
            
        # Check environment suitability
        if context['environment'] in self.context_factors['environment']:
            context_score += 0.3
            
        return context_score

    def _select_intervention_template(self, current_state, context_score):
        """Select most appropriate intervention template based on state and context"""
        
        # Find matching triggers
        matching_templates = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in current_state['triggers'] for trigger in template['triggers']):
                matching_templates.append((template_name, template))
                
        # Select best template based on context fit
        best_template = max(matching_templates, key=lambda x: context_score)
        return best_template[1]

    def _personalize_intervention(self, template, personality_config, context):
        """Customize intervention based on personality and context"""
        
        personalized_actions = []
        for action in template['actions']:
            # Adjust action duration based on cognitive load
            adjusted_duration = action['duration'] * personality_config['cognitive_load_threshold']
            
            # Customize action specifics based on learning style
            custom_specifics = self._customize_action_specifics(
                action['specifics'],
                personality_config['learning_style'],
                personality_config['communication_pref']
            )
            
            personalized_actions.append({
                'type': action['type'],
                'duration': adjusted_duration,
                'specifics': custom_specifics
            })

        return {
            'actions': personalized_actions,
            'motivation_triggers': personality_config['motivation_triggers'],
            'follow_up': template['follow_up']
        }

    def _customize_action_specifics(self, specifics, learning_style, communication_pref):
        """Customize action descriptions based on user preferences"""
        
        if learning_style == 'systematic':
            specifics = f"Step-by-step: {specifics}"
        elif learning_style == 'exploratory':
            specifics = f"Try this: {specifics}"
            
        if communication_pref == 'direct':
            specifics = specifics.replace('Try this', 'Do this')
            
        return specifics

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking intervention outcomes
        pass

    def update_user_model(self, user_id, intervention_outcomes):
        """Update user model based on intervention outcomes"""
        # Implementation for updating user model
        pass