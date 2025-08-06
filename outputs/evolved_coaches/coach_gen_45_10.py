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
                'energy_management': 'recharge_alone'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_response': 'social',
                'energy_management': 'recharge_socially'
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
            'behavior_change': {
                'tiny_habits': True,
                'implementation_intentions': True,
                'environmental_design': True,
                'accountability': True
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
            'optimal_times': [],
            'do_not_disturb': [],
            'frequency_caps': {},
            'response_history': []
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate highly personalized behavioral nudge"""
        
        # Update context awareness
        self.update_context(current_context)
        
        # Select optimal intervention timing
        if not self.is_optimal_timing():
            return None
            
        # Match personality type to optimal strategy
        personality_type = user_profile['personality_type']
        user_config = self.personality_type_configs[personality_type]
        
        # Generate intervention based on psychological profile
        intervention = self.select_intervention_strategy(user_config)
        
        # Personalize communication style
        message = self.personalize_message(intervention, user_config)
        
        # Add specific action steps
        action_steps = self.generate_action_steps(intervention, current_context)
        
        return {
            'message': message,
            'action_steps': action_steps,
            'timing': self.get_optimal_timing(),
            'context_relevance': self.assess_relevance(current_context)
        }

    def update_context(self, current_context):
        """Update context awareness parameters"""
        for factor, value in current_context.items():
            if factor in self.context_factors:
                self.context_factors[factor] = value
        
        self.update_timing_model()

    def is_optimal_timing(self):
        """Determine if current moment is optimal for intervention"""
        current_time = self.get_current_time()
        
        if current_time in self.timing_optimizer['do_not_disturb']:
            return False
            
        if self.exceeded_frequency_cap():
            return False
            
        return self.calculate_timing_score() > 0.7

    def select_intervention_strategy(self, user_config):
        """Select most appropriate intervention strategy"""
        
        # Match strategy to personality and context
        if user_config['learning_style'] == 'systematic':
            strategy = self.intervention_strategies['habit_formation']
        else:
            strategy = self.intervention_strategies['motivation']
            
        # Adapt to stress levels
        if self.context_factors['stress_level'] == 'high':
            strategy = self.modify_for_stress(strategy)
            
        return strategy

    def personalize_message(self, intervention, user_config):
        """Personalize intervention message"""
        
        tone = user_config['communication_pref']
        motivation = user_config['motivation_drivers'][0]
        
        template = self.get_message_template(intervention, tone)
        
        return self.fill_template(template, {
            'tone': tone,
            'motivation': motivation,
            'context': self.context_factors
        })

    def generate_action_steps(self, intervention, context):
        """Generate specific, actionable steps"""
        
        steps = []
        
        # Break down intervention into tiny steps
        for component in intervention:
            step = {
                'action': self.get_concrete_action(component),
                'timeframe': self.suggest_timeframe(context),
                'difficulty': self.assess_difficulty(component),
                'resources': self.identify_resources(component)
            }
            steps.append(step)
            
        return steps

    def assess_relevance(self, context):
        """Assess contextual relevance of intervention"""
        relevance_score = 0.0
        
        # Calculate relevance based on multiple factors
        relevance_score += self.timing_relevance()
        relevance_score += self.context_relevance(context)
        relevance_score += self.workload_relevance()
        
        return relevance_score / 3.0

    def update_timing_model(self):
        """Update intervention timing model"""
        
        # Update optimal times based on response history
        self.timing_optimizer['optimal_times'] = \
            self.calculate_optimal_times()
            
        # Update frequency caps
        self.timing_optimizer['frequency_caps'] = \
            self.calculate_frequency_caps()

    def exceeded_frequency_cap(self):
        """Check if frequency cap is exceeded"""
        current_frequency = len(self.timing_optimizer['response_history'])
        return current_frequency >= self.timing_optimizer['frequency_caps']

    def calculate_timing_score(self):
        """Calculate timing optimization score"""
        score = 0.0
        
        # Consider multiple timing factors
        score += self.time_of_day_score()
        score += self.energy_level_score()
        score += self.workload_score()
        
        return score / 3.0