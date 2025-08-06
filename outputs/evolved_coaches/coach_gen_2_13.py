class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'achievement', 'efficiency'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'creativity', 'social_impact'],
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
                     'steps': ['Clear workspace', 'Enable do-not-disturb', 'Set timer']},
                    {'type': 'cognitive', 'duration': 5, 'priority': 2, 
                     'steps': ['Deep breathing', 'Intent setting', 'Task visualization']}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'priority': 1,
                     'steps': ['Break task down', 'Set mini-milestone', 'Reward planning']},
                    {'type': 'reframing', 'duration': 5, 'priority': 2,
                     'steps': ['Identify barriers', 'Challenge assumptions', 'Find meaning']}
                ],
                'follow_up': {'timing': 45, 'type': 'motivation_check'}
            }
        }

        # Behavioral psychology components
        self.behavior_change_techniques = {
            'habit_formation': ['implementation_intentions', 'habit_stacking', 'environmental_cues'],
            'motivation_enhancement': ['autonomy_support', 'competence_building', 'relatedness'],
            'cognitive_restructuring': ['thought_challenging', 'reframing', 'evidence_examination']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': 'unknown',
            'recent_interventions': [],
            'intervention_outcomes': {}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized coaching intervention based on user profile and context"""
        
        # Update user context
        self.update_user_context(current_context)
        
        # Select appropriate intervention based on context
        intervention = self.select_intervention(user_profile)
        
        # Personalize based on personality type
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Apply behavioral psychology principles
        behavioral_techniques = self.select_behavior_techniques(user_profile, intervention)
        
        # Generate specific action steps
        action_steps = self.generate_action_steps(intervention, personality_config)
        
        return {
            'intervention_type': intervention,
            'action_steps': action_steps,
            'behavioral_techniques': behavioral_techniques,
            'timing': self.determine_optimal_timing(),
            'follow_up': self.generate_follow_up_plan()
        }

    def update_user_context(self, context):
        """Update user context with latest data"""
        self.user_context.update({
            'cognitive_load': self.calculate_cognitive_load(context),
            'energy_level': self.estimate_energy_level(context),
            'focus_state': self.determine_focus_state(context),
            'timestamp': context.get('timestamp')
        })

    def select_intervention(self, user_profile):
        """Select most appropriate intervention based on user state"""
        if self.user_context['cognitive_load'] > self.personality_type_configs[user_profile['personality_type']]['cognitive_load_threshold']:
            return 'focus'
        return 'motivation'

    def select_behavior_techniques(self, user_profile, intervention):
        """Select appropriate behavioral techniques based on user profile and intervention"""
        techniques = []
        if intervention == 'focus':
            techniques.extend(self.behavior_change_techniques['habit_formation'])
        elif intervention == 'motivation':
            techniques.extend(self.behavior_change_techniques['motivation_enhancement'])
        return techniques

    def generate_action_steps(self, intervention, personality_config):
        """Generate specific, actionable steps based on intervention and personality"""
        template = self.intervention_templates[intervention]
        
        # Personalize actions based on personality
        personalized_actions = []
        for action in template['actions']:
            personalized_action = {
                'steps': action['steps'],
                'duration': action['duration'],
                'priority': action['priority'],
                'style': personality_config['communication_pref'],
                'metrics': self.generate_success_metrics(action)
            }
            personalized_actions.append(personalized_action)
            
        return personalized_actions

    def determine_optimal_timing(self):
        """Determine optimal timing for intervention delivery"""
        return {
            'immediate': self.user_context['cognitive_load'] < 0.5,
            'delay_minutes': 15 if self.user_context['cognitive_load'] >= 0.5 else 0,
            'max_duration': 30
        }

    def generate_follow_up_plan(self):
        """Generate follow-up plan for intervention"""
        return {
            'timing': 30,
            'type': 'progress_check',
            'metrics': ['completion_rate', 'perceived_difficulty', 'effectiveness'],
            'adaptation_rules': {'difficulty': 'auto_adjust', 'frequency': 'response_based'}
        }

    def calculate_cognitive_load(self, context):
        """Estimate current cognitive load"""
        # Implementation for cognitive load calculation
        return 0.5

    def estimate_energy_level(self, context):
        """Estimate current energy level"""
        # Implementation for energy level estimation
        return 0.7

    def determine_focus_state(self, context):
        """Determine current focus state"""
        # Implementation for focus state determination
        return 'focused'

    def generate_success_metrics(self, action):
        """Generate measurable success metrics for actions"""
        return {
            'completion': 'binary',
            'time_spent': 'minutes',
            'effectiveness': 'scale_1_5',
            'difficulty': 'scale_1_5'
        }