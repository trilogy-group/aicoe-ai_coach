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
                'techniques': ['implementation_intentions', 'habit_stacking', 'temptation_bundling'],
                'timing': self.calculate_optimal_timing,
                'reinforcement': self.adaptive_reinforcement
            },
            'motivation_enhancement': {
                'techniques': ['goal_visualization', 'progress_tracking', 'social_accountability'],
                'timing': self.calculate_optimal_timing,
                'reinforcement': self.adaptive_reinforcement
            },
            'behavioral_activation': {
                'techniques': ['graded_tasks', 'success_spirals', 'momentum_building'],
                'timing': self.calculate_optimal_timing,
                'reinforcement': self.adaptive_reinforcement
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

        # Adaptive learning parameters
        self.user_model = {
            'response_history': [],
            'intervention_effectiveness': {},
            'behavioral_patterns': {},
            'preference_profile': {},
            'progress_metrics': {}
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate highly personalized behavioral nudge based on user context"""
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile, current_context)
        
        # Generate specific actionable recommendation
        nudge = self.craft_nudge(strategy, user_profile, current_context)
        
        # Track and adapt
        self.track_intervention(user_id, nudge, current_context)
        
        return nudge

    def analyze_context(self, context_data):
        """Analyze user context for optimal intervention timing"""
        analyzed_context = {}
        
        # Assess cognitive load
        analyzed_context['cognitive_load'] = self.estimate_cognitive_load(context_data)
        
        # Evaluate attention availability
        analyzed_context['attention_availability'] = self.assess_attention(context_data)
        
        # Determine receptivity
        analyzed_context['receptivity'] = self.calculate_receptivity(context_data)
        
        return analyzed_context

    def select_intervention_strategy(self, user_profile, context):
        """Select most effective intervention strategy for current context"""
        strategies = self.intervention_strategies.keys()
        
        # Calculate effectiveness scores
        strategy_scores = {}
        for strategy in strategies:
            score = self.calculate_strategy_fit(
                strategy,
                user_profile,
                context
            )
            strategy_scores[strategy] = score
            
        return max(strategy_scores.items(), key=lambda x: x[1])[0]

    def craft_nudge(self, strategy, user_profile, context):
        """Create specific, actionable behavioral recommendation"""
        technique = self.select_technique(strategy, user_profile)
        
        nudge = {
            'message': self.generate_message(technique, user_profile),
            'action_steps': self.generate_action_steps(technique),
            'timing': self.calculate_optimal_timing(context),
            'reinforcement': self.adaptive_reinforcement(user_profile)
        }
        
        return nudge

    def calculate_optimal_timing(self, context):
        """Determine best timing for intervention delivery"""
        timing_factors = {
            'time_of_day': context.get('time_of_day', None),
            'energy_level': context.get('energy_level', None),
            'task_load': context.get('task_complexity', None)
        }
        
        return self.optimize_timing(timing_factors)

    def adaptive_reinforcement(self, user_profile):
        """Generate personalized reinforcement schedule"""
        schedule = {
            'frequency': self.calculate_optimal_frequency(user_profile),
            'intensity': self.determine_reinforcement_intensity(user_profile),
            'type': self.select_reinforcement_type(user_profile)
        }
        
        return schedule

    def track_intervention(self, user_id, nudge, context):
        """Track intervention effectiveness for continuous improvement"""
        self.user_model['response_history'].append({
            'user_id': user_id,
            'nudge': nudge,
            'context': context,
            'timestamp': self.get_timestamp()
        })
        
        self.update_effectiveness_metrics(user_id, nudge)

    def update_effectiveness_metrics(self, user_id, nudge):
        """Update intervention effectiveness tracking"""
        if user_id not in self.user_model['intervention_effectiveness']:
            self.user_model['intervention_effectiveness'][user_id] = {}
            
        strategy = nudge['strategy']
        current_effectiveness = self.calculate_effectiveness(user_id, nudge)
        
        self.user_model['intervention_effectiveness'][user_id][strategy] = current_effectiveness

    def get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now()