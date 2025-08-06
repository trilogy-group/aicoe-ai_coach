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
                'accountability': True,
                'positive_reinforcement': True
            },
            'behavioral_change': {
                'tiny_habits': True,
                'temptation_bundling': True,
                'environmental_design': True,
                'social_proof': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'workload': None,
            'social_context': None,
            'physical_environment': None
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_frequency': None,
            'response_latency': None,
            'attention_cycles': None,
            'interruption_cost': None
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
        timing = self.optimize_intervention_timing()
        
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
        self.assess_attention_availability()

    def select_intervention_strategy(self, user_profile):
        """Select most appropriate intervention strategy based on user profile and context"""
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy = {
            'type': None,
            'approach': None,
            'intensity': None
        }
        
        # Match strategy to personality and context
        if config['learning_style'] == 'systematic':
            strategy['type'] = 'habit_formation'
            strategy['approach'] = 'structured'
        else:
            strategy['type'] = 'motivation'
            strategy['approach'] = 'flexible'
            
        # Adjust for context
        strategy['intensity'] = self.calculate_intervention_intensity()
        
        return strategy

    def create_targeted_nudge(self, strategy, user_profile):
        """Create specific, actionable nudge based on strategy"""
        nudge = {
            'message': None,
            'action_items': [],
            'support_resources': [],
            'follow_up': None
        }
        
        # Generate personalized content
        nudge['message'] = self.generate_persuasive_message(strategy, user_profile)
        nudge['action_items'] = self.generate_action_steps(strategy)
        nudge['support_resources'] = self.compile_resources(strategy)
        nudge['follow_up'] = self.schedule_follow_up(strategy)
        
        return nudge

    def optimize_intervention_timing(self):
        """Optimize timing of intervention delivery"""
        timing = {
            'optimal_time': None,
            'frequency': None,
            'duration': None
        }
        
        # Calculate optimal timing parameters
        timing['optimal_time'] = self.calculate_optimal_time()
        timing['frequency'] = self.calculate_optimal_frequency()
        timing['duration'] = self.calculate_intervention_duration()
        
        return timing

    def analyze_cognitive_load(self):
        """Assess current cognitive load to optimize intervention"""
        workload = self.context_factors['workload']
        stress = self.context_factors['stress_level']
        
        return (workload + stress) / 2

    def assess_attention_availability(self):
        """Determine user's current attention availability"""
        time = self.context_factors['time_of_day']
        energy = self.context_factors['energy_level']
        
        return (time + energy) / 2

    def calculate_intervention_intensity(self):
        """Calculate appropriate intervention intensity"""
        cognitive_load = self.analyze_cognitive_load()
        attention = self.assess_attention_availability()
        
        return min(cognitive_load, attention)

    def generate_persuasive_message(self, strategy, user_profile):
        """Generate psychologically sophisticated persuasive message"""
        config = self.personality_type_configs[user_profile['personality_type']]
        
        # Personalize message based on psychological preferences
        if config['communication_pref'] == 'direct':
            return f"Based on {strategy['type']}, here's your next step..."
        else:
            return f"Let's explore how we can make progress on {strategy['type']}..."

    def generate_action_steps(self, strategy):
        """Generate specific, actionable steps"""
        return [
            "Specific action 1 with clear success criteria",
            "Specific action 2 with timeline",
            "Specific action 3 with measurement"
        ]

    def compile_resources(self, strategy):
        """Compile relevant support resources"""
        return [
            "Resource 1 matching strategy",
            "Resource 2 matching context",
            "Resource 3 matching personality"
        ]

    def schedule_follow_up(self, strategy):
        """Schedule appropriate follow-up based on strategy"""
        return {
            'timing': 'next_optimal_window',
            'type': 'check_in',
            'focus': strategy['type']
        }