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
                'implementation_intentions': True,
                'value_alignment': True,
                'self_efficacy_building': True
            },
            'behavioral_change': {
                'tiny_habits': True,
                'commitment_devices': True,
                'social_proof': True,
                'choice_architecture': True
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
        
        # Generate customized nudge content
        nudge = self.create_nudge_content(strategy, user_profile)
        
        # Optimize timing
        timing = self.optimize_intervention_timing()
        
        return self.format_intervention(nudge, timing)

    def update_context(self, current_context):
        """
        Update context awareness based on real-time factors
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

        # Adjust for context
        strategy['intensity'] = self.calculate_intervention_intensity()
        
        return strategy

    def create_nudge_content(self, strategy, user_profile):
        """
        Create specific, actionable nudge content
        """
        nudge = {
            'message': None,
            'action_items': [],
            'supporting_resources': [],
            'follow_up': None
        }

        # Generate personalized content
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Adapt communication style
        comm_style = personality_config['communication_pref']
        
        # Generate specific action items
        nudge['action_items'] = self.generate_action_items(strategy)
        
        return nudge

    def optimize_intervention_timing(self):
        """
        Optimize intervention timing based on user receptivity and cognitive load
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

    def calculate_intervention_intensity(self):
        """
        Calculate appropriate intervention intensity based on context
        """
        base_intensity = 0.5
        
        # Adjust for stress level
        if self.context_factors['stress_level']:
            base_intensity *= (1 - self.context_factors['stress_level'])
            
        # Adjust for cognitive load
        if self.context_factors['task_complexity']:
            base_intensity *= (1 - self.context_factors['task_complexity'])
            
        return max(0.1, min(1.0, base_intensity))

    def generate_action_items(self, strategy):
        """
        Generate specific, actionable recommendations
        """
        action_items = []
        
        if strategy['type'] == 'structured':
            action_items = [
                {'task': 'Define specific goal', 'timeframe': 'immediate'},
                {'task': 'Break down into subtasks', 'timeframe': 'short-term'},
                {'task': 'Set implementation intentions', 'timeframe': 'ongoing'}
            ]
        else:
            action_items = [
                {'task': 'Explore possible approaches', 'timeframe': 'immediate'},
                {'task': 'Choose preferred method', 'timeframe': 'short-term'},
                {'task': 'Adapt as needed', 'timeframe': 'ongoing'}
            ]
            
        return action_items

    def format_intervention(self, nudge, timing):
        """
        Format the final intervention package
        """
        return {
            'content': nudge,
            'timing': timing,
            'delivery_method': self.select_delivery_method(),
            'follow_up_schedule': self.create_follow_up_schedule()
        }