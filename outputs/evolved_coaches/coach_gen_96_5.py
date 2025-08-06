class EnhancedAICoach:
    def __init__(self):
        # Personality configurations from Parent 2
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types omitted for brevity
        }

        # Enhanced intervention configurations
        self.intervention_types = {
            'quick_win': {
                'duration': '5-15min',
                'cognitive_load': 'low',
                'motivation_triggers': ['autonomy', 'mastery'],
                'follow_up_window': 24 # hours
            },
            'habit_formation': {
                'duration': '21-days',
                'cognitive_load': 'medium',
                'motivation_triggers': ['consistency', 'progress'],
                'follow_up_window': 48
            },
            'deep_change': {
                'duration': '90-days',
                'cognitive_load': 'high', 
                'motivation_triggers': ['purpose', 'identity'],
                'follow_up_window': 72
            }
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'commitment': ['public declaration', 'written goals', 'accountability partner'],
            'reinforcement': ['progress tracking', 'milestone rewards', 'streak bonuses'],
            'social_proof': ['peer success stories', 'community challenges', 'group metrics'],
            'scarcity': ['limited time offers', 'exclusive content', 'early access'],
            'authority': ['expert validation', 'research citations', 'credentialed advice']
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze context and cognitive load
        current_load = self._assess_cognitive_load(user_context)
        optimal_timing = self._calculate_optimal_timing(user_context)
        
        # Select appropriate intervention type
        intervention = self._select_intervention_type(current_load, user_config)
        
        # Build specific action steps
        action_steps = self._create_action_steps(
            intervention,
            user_config['learning_style'],
            user_context
        )

        # Add behavioral triggers
        motivation_elements = self._add_behavioral_triggers(
            personality_type,
            intervention['motivation_triggers']
        )

        return {
            'nudge_content': self._format_nudge(action_steps, motivation_elements),
            'timing': optimal_timing,
            'follow_up': intervention['follow_up_window'],
            'success_metrics': self._define_success_metrics(action_steps)
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        load_factors = {
            'current_tasks': context.get('active_tasks', 0) * 0.3,
            'time_pressure': context.get('deadline_proximity', 0) * 0.4,
            'complexity': context.get('task_complexity', 0) * 0.3
        }
        return sum(load_factors.values())

    def _calculate_optimal_timing(self, context):
        """Calculate optimal intervention timing"""
        energy_level = context.get('energy_level', 0.5)
        focus_state = context.get('focus_state', 0.5)
        time_availability = context.get('available_time', 30)
        
        optimal_score = (energy_level * 0.4 + focus_state * 0.3 + 
                        (time_availability/60) * 0.3)
        
        return {
            'score': optimal_score,
            'suggested_time': context.get('next_break_time', None),
            'max_duration': min(time_availability, 30)
        }

    def _select_intervention_type(self, cognitive_load, user_config):
        """Select appropriate intervention based on load and user preferences"""
        if cognitive_load > 0.7:
            return self.intervention_types['quick_win']
        elif cognitive_load > 0.4:
            return self.intervention_types['habit_formation']
        else:
            return self.intervention_types['deep_change']

    def _create_action_steps(self, intervention, learning_style, context):
        """Create specific, measurable action steps"""
        steps = []
        
        if learning_style == 'systematic':
            steps = self._generate_systematic_steps(intervention, context)
        else:
            steps = self._generate_exploratory_steps(intervention, context)
            
        return [{
            'step': step,
            'duration': self._estimate_duration(step),
            'difficulty': self._assess_difficulty(step),
            'resources': self._identify_resources(step)
        } for step in steps]

    def _add_behavioral_triggers(self, personality_type, motivation_triggers):
        """Add relevant behavioral psychology elements"""
        selected_triggers = []
        
        for trigger in motivation_triggers:
            if trigger in self.behavior_triggers:
                selected_triggers.extend(self.behavior_triggers[trigger])
                
        return selected_triggers

    def _define_success_metrics(self, action_steps):
        """Define concrete success metrics for recommendations"""
        return {
            'completion_rate': 'Percentage of steps completed',
            'time_to_completion': 'Time taken vs estimated duration',
            'difficulty_rating': 'User-reported difficulty vs predicted',
            'satisfaction_score': 'User satisfaction with outcomes',
            'behavioral_change': 'Measured change in target behavior'
        }

    def _format_nudge(self, action_steps, motivation_elements):
        """Format the final nudge content"""
        return {
            'title': 'Your Personalized Action Plan',
            'steps': action_steps,
            'motivation': motivation_elements,
            'estimated_impact': self._calculate_impact_score(action_steps),
            'difficulty_level': self._calculate_overall_difficulty(action_steps)
        }

    def track_progress(self, user_id, nudge_id, completion_data):
        """Track user progress and adjust future recommendations"""
        # Implementation for progress tracking
        pass

    def update_user_model(self, user_id, interaction_data):
        """Update user model based on interactions"""
        # Implementation for user model updates
        pass