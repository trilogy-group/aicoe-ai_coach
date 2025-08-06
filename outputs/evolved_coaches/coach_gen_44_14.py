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
        
        self.assess_cognitive_load()
        self.evaluate_attention_capacity()

    def select_intervention_strategy(self, user_profile):
        """
        Select the most appropriate intervention strategy based on user profile and context
        """
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy = {
            'approach': self.match_learning_style(config['learning_style']),
            'communication': config['communication_pref'],
            'timing': self.timing_optimizer['optimal_frequency'],
            'motivation_hooks': config['motivation_drivers']
        }
        
        return strategy

    def create_nudge_content(self, strategy, user_profile):
        """
        Create specific, actionable nudge content
        """
        nudge = {
            'message': self.generate_message(strategy),
            'action_steps': self.create_action_steps(),
            'reinforcement': self.design_reinforcement(),
            'follow_up': self.plan_follow_up()
        }
        
        return nudge

    def optimize_intervention_timing(self):
        """
        Optimize intervention timing based on user state and context
        """
        timing = {
            'optimal_time': self.calculate_optimal_time(),
            'frequency': self.determine_frequency(),
            'duration': self.calculate_duration()
        }
        
        return timing

    def assess_cognitive_load(self):
        """
        Assess current cognitive load to optimize intervention delivery
        """
        factors = [
            self.context_factors['task_complexity'],
            self.context_factors['stress_level'],
            self.context_factors['energy_level']
        ]
        
        self.timing_optimizer['cognitive_load'] = self.calculate_cognitive_load(factors)

    def evaluate_attention_capacity(self):
        """
        Evaluate current attention capacity for intervention optimization
        """
        attention_score = self.calculate_attention_score()
        self.timing_optimizer['attention_span'] = attention_score

    def format_intervention(self, nudge, timing):
        """
        Format the final intervention package
        """
        return {
            'content': nudge,
            'delivery_timing': timing,
            'tracking_metrics': self.define_tracking_metrics(),
            'adaptation_rules': self.create_adaptation_rules()
        }

    def calculate_effectiveness(self):
        """
        Calculate intervention effectiveness for continuous improvement
        """
        metrics = {
            'engagement': self.measure_engagement(),
            'behavior_change': self.measure_behavior_change(),
            'user_satisfaction': self.measure_satisfaction(),
            'goal_progress': self.measure_goal_progress()
        }
        
        return metrics