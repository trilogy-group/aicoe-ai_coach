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
            'work_load': None,
            'social_context': None,
            'physical_environment': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': [],
            'response_rates': {},
            'engagement_patterns': {},
            'cognitive_load': {}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate highly personalized behavioral nudge"""
        
        # Update context awareness
        self.update_context(context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile)
        
        # Generate specific actionable recommendation
        nudge = self.create_targeted_nudge(strategy, user_profile)
        
        # Optimize timing
        timing = self.optimize_intervention_timing(user_profile)
        
        return {
            'nudge': nudge,
            'timing': timing,
            'context': self.context_factors,
            'strategy': strategy
        }

    def update_context(self, context):
        """Update contextual awareness factors"""
        for factor in context:
            if factor in self.context_factors:
                self.context_factors[factor] = context[factor]
        
        self.analyze_cognitive_load()
        self.assess_receptivity()

    def select_intervention_strategy(self, user_profile):
        """Select optimal intervention strategy based on user profile and context"""
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
            strategy['approach'] = 'logical'
        else:
            strategy['type'] = 'flexible'
            strategy['approach'] = 'intuitive'
            
        # Adjust for cognitive load
        strategy['intensity'] = self.calculate_optimal_intensity()
        
        return strategy

    def create_targeted_nudge(self, strategy, user_profile):
        """Create specific actionable recommendation"""
        nudge = {
            'content': None,
            'action_steps': [],
            'motivation_hooks': [],
            'follow_up': None
        }
        
        # Generate personalized content
        nudge['content'] = self.generate_content(strategy, user_profile)
        
        # Create specific action steps
        nudge['action_steps'] = self.generate_action_steps(strategy)
        
        # Add motivation hooks
        nudge['motivation_hooks'] = self.add_motivation_elements(user_profile)
        
        # Plan follow up
        nudge['follow_up'] = self.plan_follow_up(strategy)
        
        return nudge

    def optimize_intervention_timing(self, user_profile):
        """Optimize timing of intervention delivery"""
        timing = {
            'optimal_time': None,
            'frequency': None,
            'spacing': None
        }
        
        # Calculate optimal delivery time
        timing['optimal_time'] = self.calculate_optimal_time()
        
        # Determine ideal frequency
        timing['frequency'] = self.determine_frequency(user_profile)
        
        # Calculate optimal spacing
        timing['spacing'] = self.calculate_spacing()
        
        return timing

    def analyze_cognitive_load(self):
        """Analyze current cognitive load"""
        load_factors = {
            'task_complexity': self.context_factors['work_load'],
            'time_pressure': True if self.context_factors['stress_level'] > 7 else False,
            'distractions': self.assess_environment_distractions()
        }
        return load_factors

    def assess_receptivity(self):
        """Assess user receptivity to interventions"""
        receptivity = {
            'attention_availability': self.calculate_attention_availability(),
            'motivation_level': self.assess_current_motivation(),
            'emotional_state': self.analyze_emotional_state()
        }
        return receptivity

    def calculate_optimal_intensity(self):
        """Calculate optimal intervention intensity"""
        cognitive_load = self.analyze_cognitive_load()
        receptivity = self.assess_receptivity()
        
        if cognitive_load['task_complexity'] == 'high':
            return 'low'
        elif receptivity['motivation_level'] == 'high':
            return 'high'
        else:
            return 'medium'

    def generate_content(self, strategy, user_profile):
        """Generate personalized content"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        content = {
            'tone': personality_config['communication_pref'],
            'structure': strategy['type'],
            'focus': personality_config['motivation_drivers'][0]
        }
        
        return content

    def generate_action_steps(self, strategy):
        """Generate specific action steps"""
        return [
            {'step': 1, 'action': 'Specific action 1', 'timeframe': 'immediate'},
            {'step': 2, 'action': 'Specific action 2', 'timeframe': 'today'},
            {'step': 3, 'action': 'Specific action 3', 'timeframe': 'this week'}
        ]

    def add_motivation_elements(self, user_profile):
        """Add personalized motivation elements"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        return [
            {'type': 'value_alignment', 'content': personality_config['motivation_drivers']},
            {'type': 'social_proof', 'content': 'Relevant success stories'},
            {'type': 'progress_visualization', 'content': 'Progress metrics'}
        ]

    def plan_follow_up(self, strategy):
        """Plan intervention follow up"""
        return {
            'timeframe': '24h',
            'type': 'check_in',
            'focus': 'progress_assessment'
        }