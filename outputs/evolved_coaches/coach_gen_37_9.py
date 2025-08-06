class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced psychological models
        self.cognitive_models = {
            'attention': {'capacity': 0.0, 'fatigue': 0.0, 'recovery_rate': 0.0},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0, 'goal_alignment': 0.0},
            'emotional': {'valence': 0.0, 'arousal': 0.0, 'dominance': 0.0}
        }

        # Context tracking
        self.context_tracker = {
            'time_of_day': None,
            'work_phase': None, 
            'energy_level': 0.0,
            'task_complexity': 0.0,
            'interruption_cost': 0.0
        }

        # Behavioral intervention settings
        self.intervention_config = {
            'min_interval': 1800,  # 30 minutes
            'max_daily': 8,
            'intensity_scale': 0.0,
            'success_threshold': 0.7
        }

        # User profile and history
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'success_metrics': {},
            'preference_weights': {}
        }

    def update_cognitive_state(self, metrics):
        """Update cognitive load and attention state"""
        self.cognitive_models['attention']['capacity'] = metrics['focus_level']
        self.cognitive_models['attention']['fatigue'] = metrics['mental_fatigue']
        self.cognitive_models['motivation']['intrinsic'] = metrics['engagement']
        self.cognitive_models['emotional']['valence'] = metrics['mood']

    def assess_intervention_timing(self):
        """Determine optimal intervention timing"""
        current_load = self.cognitive_models['attention']['capacity']
        fatigue = self.cognitive_models['attention']['fatigue']
        task_complexity = self.context_tracker['task_complexity']

        timing_score = (1 - current_load) * (1 - fatigue) * (1 - task_complexity)
        return timing_score > self.intervention_config['success_threshold']

    def generate_personalized_nudge(self, context):
        """Generate contextually relevant coaching intervention"""
        personality = self.user_profile['personality_type']
        learning_style = self.personality_type_configs[personality]['learning_style']
        comm_pref = self.personality_type_configs[personality]['communication_pref']

        # Select intervention type based on context and user profile
        if self.cognitive_models['attention']['fatigue'] > 0.7:
            return self.generate_recovery_intervention()
        elif self.cognitive_models['motivation']['intrinsic'] < 0.4:
            return self.generate_motivation_intervention()
        else:
            return self.generate_growth_intervention()

    def generate_recovery_intervention(self):
        """Generate fatigue management intervention"""
        return {
            'type': 'recovery',
            'message': 'Time for a strategic break to maintain peak performance',
            'actions': [
                'Take a 5-minute mindfulness break',
                'Do quick physical movement',
                'Hydrate and stretch'
            ],
            'duration': 300
        }

    def generate_motivation_intervention(self):
        """Generate motivation-focused intervention"""
        return {
            'type': 'motivation',
            'message': 'Let\'s reconnect with your core objectives',
            'actions': [
                'Review your top 3 goals for today',
                'Visualize successful completion',
                'Break next task into smaller steps'
            ],
            'duration': 180
        }

    def generate_growth_intervention(self):
        """Generate growth and learning intervention"""
        return {
            'type': 'growth',
            'message': 'Opportunity to enhance your skills',
            'actions': [
                'Try this new productivity technique',
                'Reflect on recent achievements',
                'Set a micro-learning goal'
            ],
            'duration': 240
        }

    def track_intervention_success(self, intervention_id, metrics):
        """Track effectiveness of interventions"""
        self.user_profile['response_history'].append({
            'intervention_id': intervention_id,
            'timestamp': metrics['timestamp'],
            'success_rate': metrics['completion_rate'],
            'engagement': metrics['user_engagement'],
            'impact': metrics['behavioral_change']
        })

        # Update success metrics
        self.user_profile['success_metrics'][intervention_id] = {
            'effectiveness': metrics['effectiveness'],
            'relevance': metrics['relevance'],
            'timing': metrics['timing_score']
        }

    def adapt_intervention_strategy(self):
        """Adapt coaching strategy based on historical performance"""
        history = self.user_profile['response_history']
        if len(history) > 10:
            recent_success = sum(h['success_rate'] for h in history[-10:]) / 10
            
            # Adjust intervention parameters
            self.intervention_config['intensity_scale'] = min(1.0, recent_success + 0.1)
            self.intervention_config['min_interval'] *= (1.0 + (0.5 - recent_success))
            
            # Update preference weights
            self.update_preference_weights(history[-10:])

    def update_preference_weights(self, recent_history):
        """Update user preference weights based on intervention success"""
        for record in recent_history:
            intervention_type = record['intervention_id'].split('_')[0]
            current_weight = self.user_profile['preference_weights'].get(intervention_type, 1.0)
            success_factor = record['success_rate']
            
            # Exponential moving average update
            new_weight = current_weight * 0.7 + success_factor * 0.3
            self.user_profile['preference_weights'][intervention_type] = new_weight