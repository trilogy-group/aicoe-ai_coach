class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_response': 'analytical',
                'decision_style': 'logical'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'adaptive',
                'decision_style': 'intuitive'
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
            'motivation': {
                'goal_setting': True,
                'value_alignment': True,
                'self_efficacy': True,
                'social_proof': True
            },
            'behavioral_change': {
                'implementation_intentions': True,
                'commitment_devices': True,
                'environmental_design': True,
                'accountability': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'task_complexity': None,
            'environmental_conditions': None,
            'social_context': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_frequency': None,
            'user_receptivity': None,
            'cognitive_load': None,
            'attention_span': None,
            'recovery_needs': None
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
        Update context awareness based on current user situation
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
        
        strategy = {
            'type': None,
            'approach': None,
            'intensity': None
        }

        # Match strategy to personality and context
        if config['learning_style'] == 'systematic':
            strategy['type'] = 'structured'
            strategy['approach'] = 'analytical'
        else:
            strategy['type'] = 'flexible'
            strategy['approach'] = 'intuitive'

        # Adjust for cognitive load
        strategy['intensity'] = self.calculate_optimal_intensity()
        
        return strategy

    def create_intervention_content(self, strategy, user_profile):
        """
        Generate specific, actionable intervention content
        """
        content = {
            'message': None,
            'action_steps': [],
            'supporting_resources': [],
            'follow_up_prompts': []
        }

        # Personalize message style
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        communication_style = personality_config['communication_pref']

        # Generate actionable steps
        content['action_steps'] = self.generate_action_steps(strategy)
        
        # Add supporting resources
        content['supporting_resources'] = self.compile_resources(strategy)
        
        # Create follow-up structure
        content['follow_up_prompts'] = self.create_follow_up_sequence()

        return content

    def optimize_intervention_timing(self):
        """
        Optimize intervention timing based on user context and cognitive state
        """
        timing = {
            'optimal_time': None,
            'frequency': None,
            'duration': None
        }

        # Calculate optimal timing
        timing['optimal_time'] = self.calculate_optimal_time()
        timing['frequency'] = self.calculate_optimal_frequency()
        timing['duration'] = self.calculate_optimal_duration()

        return timing

    def calculate_optimal_intensity(self):
        """
        Calculate optimal intervention intensity based on context
        """
        base_intensity = 0.5
        
        # Adjust for stress level
        if self.context_factors['stress_level']:
            base_intensity *= (1 - self.context_factors['stress_level'])
            
        # Adjust for cognitive load
        if self.context_factors['task_complexity']:
            base_intensity *= (1 - self.context_factors['task_complexity'])
            
        return max(0.1, min(1.0, base_intensity))

    def generate_action_steps(self, strategy):
        """
        Generate specific, actionable steps based on intervention strategy
        """
        return [
            {'step': 1, 'action': 'Specific action 1', 'timeframe': 'immediate'},
            {'step': 2, 'action': 'Specific action 2', 'timeframe': 'short-term'},
            {'step': 3, 'action': 'Specific action 3', 'timeframe': 'long-term'}
        ]

    def compile_resources(self, strategy):
        """
        Compile relevant supporting resources
        """
        return [
            {'type': 'article', 'content': 'Relevant content 1'},
            {'type': 'exercise', 'content': 'Practical exercise 1'},
            {'type': 'tool', 'content': 'Supporting tool 1'}
        ]

    def create_follow_up_sequence(self):
        """
        Create structured follow-up sequence
        """
        return [
            {'timing': '+1 day', 'prompt': 'Check-in question 1'},
            {'timing': '+3 days', 'prompt': 'Check-in question 2'},
            {'timing': '+1 week', 'prompt': 'Progress review'}
        ]