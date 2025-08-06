class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'cognitive_style': 'analytical',
                'stress_response': 'problem_solving'
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'cognitive_style': 'intuitive',
                'stress_response': 'reframing'
            }
            # Additional types...
        }

        # Evidence-based intervention strategies
        self.intervention_strategies = {
            'habit_formation': {
                'techniques': ['implementation_intentions', 'habit_stacking', 'temptation_bundling'],
                'timing': 'context_dependent',
                'frequency': 'adaptive'
            },
            'motivation_enhancement': {
                'techniques': ['goal_visualization', 'progress_tracking', 'value_alignment'],
                'timing': 'low_motivation_periods',
                'frequency': 'as_needed'
            },
            'behavioral_activation': {
                'techniques': ['graded_tasks', 'success_spirals', 'momentum_building'],
                'timing': 'action_opportunities',
                'frequency': 'daily'
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

        # Adaptive nudge configuration
        self.nudge_params = {
            'min_interval': 3600,  # seconds
            'max_daily': 5,
            'priority_threshold': 0.7,
            'receptivity_window': True
        }

    def generate_personalized_intervention(self, user_profile, current_context):
        """Generate highly personalized coaching intervention"""
        
        # Update context awareness
        self.update_context(current_context)
        
        # Select optimal intervention strategy
        strategy = self.select_intervention_strategy(user_profile)
        
        # Generate specific actionable recommendations
        recommendations = self.generate_recommendations(strategy, user_profile)
        
        # Apply psychological optimization
        optimized_intervention = self.optimize_psychology(recommendations)
        
        return optimized_intervention

    def update_context(self, current_context):
        """Update context awareness parameters"""
        for factor, value in current_context.items():
            if factor in self.context_factors:
                self.context_factors[factor] = value
                
        self.evaluate_receptivity()

    def select_intervention_strategy(self, user_profile):
        """Select most appropriate intervention strategy based on user profile and context"""
        personality_type = user_profile.get('personality_type')
        config = self.personality_type_configs.get(personality_type)
        
        strategy_scores = {}
        for strategy, details in self.intervention_strategies.items():
            score = self.calculate_strategy_fit(strategy, config)
            strategy_scores[strategy] = score
            
        return max(strategy_scores.items(), key=lambda x: x[1])[0]

    def generate_recommendations(self, strategy, user_profile):
        """Generate specific, actionable recommendations"""
        strategy_details = self.intervention_strategies[strategy]
        
        recommendations = []
        for technique in strategy_details['techniques']:
            action = self.create_specific_action(technique, user_profile)
            if action:
                recommendations.append(action)
                
        return self.prioritize_recommendations(recommendations)

    def optimize_psychology(self, recommendations):
        """Apply psychological optimization techniques"""
        optimized = []
        for rec in recommendations:
            # Apply motivation enhancement
            rec = self.enhance_motivation(rec)
            
            # Apply cognitive load optimization
            rec = self.optimize_cognitive_load(rec)
            
            # Apply behavioral psychology principles
            rec = self.apply_behavioral_principles(rec)
            
            optimized.append(rec)
            
        return optimized

    def evaluate_receptivity(self):
        """Evaluate user receptivity to interventions"""
        factors = [
            self.context_factors['energy_level'],
            self.context_factors['stress_level'],
            self.context_factors['available_time']
        ]
        
        self.nudge_params['receptivity_window'] = all(f > 0.5 for f in factors if f is not None)

    def calculate_strategy_fit(self, strategy, config):
        """Calculate how well a strategy fits user profile and context"""
        base_score = 0.5
        
        # Adjust for learning style match
        if config['learning_style'] == 'systematic' and strategy == 'habit_formation':
            base_score += 0.2
            
        # Adjust for motivation alignment
        if any(driver in config['motivation_drivers'] for driver in ['mastery', 'achievement']):
            base_score += 0.15
            
        # Adjust for context
        if self.context_factors['energy_level'] and self.context_factors['energy_level'] > 0.7:
            base_score += 0.1
            
        return min(base_score, 1.0)

    def create_specific_action(self, technique, user_profile):
        """Create specific, actionable recommendation"""
        if technique == 'implementation_intentions':
            return {
                'action': 'Specific implementation intention',
                'template': 'When {trigger}, I will {action}',
                'examples': self.generate_relevant_examples(user_profile),
                'difficulty': 'low',
                'time_required': '2 minutes'
            }
        # Additional technique handlers...
        return None

    def prioritize_recommendations(self, recommendations):
        """Prioritize recommendations based on expected impact and context"""
        scored_recs = []
        for rec in recommendations:
            impact_score = self.calculate_impact_score(rec)
            feasibility_score = self.calculate_feasibility_score(rec)
            final_score = (impact_score + feasibility_score) / 2
            scored_recs.append((rec, final_score))
            
        return [rec for rec, score in sorted(scored_recs, key=lambda x: x[1], reverse=True)]

    def calculate_impact_score(self, recommendation):
        """Calculate expected impact of recommendation"""
        return 0.8  # Placeholder for actual impact calculation

    def calculate_feasibility_score(self, recommendation):
        """Calculate feasibility of recommendation given current context"""
        return 0.7  # Placeholder for actual feasibility calculation