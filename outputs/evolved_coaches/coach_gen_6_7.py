class EnhancedAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced factors
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_response': 'analytical',
                'optimal_challenge_level': 'high'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'adaptive',
                'optimal_challenge_level': 'moderate'
            }
            # Additional types configured similarly
        }

        # Evidence-based intervention strategies
        self.intervention_strategies = {
            'habit_formation': {
                'cue_identification': True,
                'routine_design': True,
                'reward_scheduling': True,
                'progress_tracking': True
            },
            'motivation_enhancement': {
                'goal_setting': True,
                'value_alignment': True,
                'self_efficacy_building': True,
                'positive_reinforcement': True
            },
            'behavioral_activation': {
                'activity_scheduling': True,
                'difficulty_gradation': True,
                'success_spiraling': True,
                'momentum_building': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'available_time': None,
            'environment': None,
            'recent_progress': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_frequency': None,
            'response_latency': None,
            'engagement_patterns': None,
            'do_not_disturb': None
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """
        Generate highly personalized coaching interventions based on user profile and context
        """
        # Update context awareness
        self.update_context(current_context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile)
        
        # Generate customized content
        content = self.create_intervention_content(strategy, user_profile)
        
        # Optimize timing
        timing = self.optimize_intervention_timing()
        
        return {
            'content': content,
            'timing': timing,
            'strategy': strategy
        }

    def update_context(self, current_context):
        """
        Update context awareness based on current user state and environment
        """
        for factor in self.context_factors:
            if factor in current_context:
                self.context_factors[factor] = current_context[factor]

    def select_intervention_strategy(self, user_profile):
        """
        Select the most appropriate intervention strategy based on user profile and context
        """
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        # Match strategy to personality and context
        if config['learning_style'] == 'systematic':
            return self.intervention_strategies['habit_formation']
        elif config['motivation_drivers'] == ['creativity', 'connection', 'growth']:
            return self.intervention_strategies['motivation_enhancement']
        else:
            return self.intervention_strategies['behavioral_activation']

    def create_intervention_content(self, strategy, user_profile):
        """
        Create specific, actionable intervention content
        """
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        content = {
            'message': self.generate_message(config, strategy),
            'action_steps': self.generate_action_steps(strategy),
            'support_resources': self.compile_resources(config),
            'progress_metrics': self.define_progress_metrics(strategy)
        }
        
        return content

    def optimize_intervention_timing(self):
        """
        Optimize intervention timing based on user patterns and context
        """
        timing = {
            'optimal_time': self.calculate_optimal_time(),
            'frequency': self.determine_frequency(),
            'urgency': self.assess_urgency()
        }
        
        return timing

    def generate_message(self, config, strategy):
        """
        Generate personalized message matching communication preferences
        """
        style = config['communication_pref']
        message_templates = {
            'direct': "Your next step is to {action}. This will help you {benefit}.",
            'enthusiastic': "Ready for an exciting challenge? Let's {action} to {benefit}!"
        }
        return message_templates.get(style, "Let's {action} to {benefit}.")

    def generate_action_steps(self, strategy):
        """
        Generate specific, actionable steps based on intervention strategy
        """
        return [
            {'step': 1, 'action': 'Specific action 1', 'timeframe': '5 mins'},
            {'step': 2, 'action': 'Specific action 2', 'timeframe': '15 mins'},
            {'step': 3, 'action': 'Specific action 3', 'timeframe': '10 mins'}
        ]

    def compile_resources(self, config):
        """
        Compile relevant resources matching learning style
        """
        return {
            'guides': [],
            'tools': [],
            'examples': [],
            'research': []
        }

    def define_progress_metrics(self, strategy):
        """
        Define concrete metrics for tracking intervention success
        """
        return {
            'behavioral_indicators': [],
            'outcome_measures': [],
            'satisfaction_metrics': []
        }

    def calculate_optimal_time(self):
        """
        Calculate optimal intervention timing
        """
        return {'time': None, 'confidence': 0.0}

    def determine_frequency(self):
        """
        Determine optimal intervention frequency
        """
        return {'times_per_day': 0, 'minimum_spacing': 0}

    def assess_urgency(self):
        """
        Assess intervention urgency based on context
        """
        return {'urgent': False, 'reason': None}