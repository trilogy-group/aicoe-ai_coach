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
            'environment': None,
            'prior_success_rate': None,
            'recent_behaviors': []
        }

        # Adaptive intervention timing
        self.timing_optimizer = {
            'optimal_intervals': [],
            'response_latency': [],
            'engagement_patterns': {},
            'circadian_preferences': {}
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate highly personalized behavioral nudge"""
        
        # Update context awareness
        self.update_context(context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile)
        
        # Generate tailored content
        content = self.create_intervention_content(strategy, user_profile)
        
        # Optimize timing
        timing = self.optimize_intervention_timing(user_profile)
        
        return {
            'content': content,
            'timing': timing,
            'strategy': strategy,
            'context_factors': self.context_factors
        }

    def update_context(self, context):
        """Update contextual awareness"""
        self.context_factors.update(context)
        self.context_factors['recent_behaviors'].append(context.get('current_behavior'))
        if len(self.context_factors['recent_behaviors']) > 10:
            self.context_factors['recent_behaviors'].pop(0)

    def select_intervention_strategy(self, user_profile):
        """Select most appropriate intervention strategy based on user profile and context"""
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy = {
            'type': None,
            'intensity': None,
            'framing': None
        }

        # Match strategy to personality and context
        if config['learning_style'] == 'systematic':
            strategy['type'] = 'habit_formation'
            strategy['intensity'] = 'moderate'
            strategy['framing'] = 'logical'
        else:
            strategy['type'] = 'motivation'
            strategy['intensity'] = 'high'
            strategy['framing'] = 'emotional'

        return strategy

    def create_intervention_content(self, strategy, user_profile):
        """Generate specific, actionable intervention content"""
        content = {
            'message': None,
            'action_steps': [],
            'supporting_resources': [],
            'follow_up_prompts': []
        }

        # Personalize based on strategy and profile
        if strategy['type'] == 'habit_formation':
            content['message'] = self.generate_habit_message(user_profile)
            content['action_steps'] = self.generate_action_steps(strategy)
        else:
            content['message'] = self.generate_motivation_message(user_profile)
            content['action_steps'] = self.generate_motivation_steps(strategy)

        return content

    def optimize_intervention_timing(self, user_profile):
        """Optimize intervention timing based on user patterns"""
        timing = {
            'optimal_time': None,
            'frequency': None,
            'duration': None
        }

        # Analyze engagement patterns
        patterns = self.timing_optimizer['engagement_patterns']
        preferences = self.timing_optimizer['circadian_preferences']

        # Calculate optimal timing
        timing['optimal_time'] = self.calculate_optimal_time(patterns, preferences)
        timing['frequency'] = self.calculate_optimal_frequency(user_profile)
        timing['duration'] = self.calculate_optimal_duration(user_profile)

        return timing

    def generate_habit_message(self, user_profile):
        """Generate habit-focused intervention message"""
        return "Specific habit formation message based on profile"

    def generate_motivation_message(self, user_profile):
        """Generate motivation-focused intervention message"""
        return "Specific motivation message based on profile"

    def generate_action_steps(self, strategy):
        """Generate specific action steps"""
        return ["Step 1", "Step 2", "Step 3"]

    def generate_motivation_steps(self, strategy):
        """Generate motivation-building steps"""
        return ["Motivation step 1", "Motivation step 2"]

    def calculate_optimal_time(self, patterns, preferences):
        """Calculate optimal intervention timing"""
        return "08:00"  # Placeholder

    def calculate_optimal_frequency(self, user_profile):
        """Calculate optimal intervention frequency"""
        return "daily"  # Placeholder

    def calculate_optimal_duration(self, user_profile):
        """Calculate optimal intervention duration"""
        return "1 week"  # Placeholder