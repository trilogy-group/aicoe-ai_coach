class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced context tracking
        self.context_tracker = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'time_of_day': None,
            'work_context': None,
            'interruption_cost': 0.0
        }

        # Behavioral psychology components
        self.behavior_engine = {
            'habit_formation': {},
            'motivation_triggers': {},
            'resistance_patterns': {},
            'success_metrics': {}
        }

        # User profile and personalization
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'effectiveness_scores': {},
            'preferred_times': [],
            'avoid_times': []
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        interruption_cost = self._estimate_interruption_cost(environment_data)
        
        return {
            'is_receptive': cognitive_load < 0.7 and interruption_cost < 0.5,
            'optimal_timing': self._check_timing_window(),
            'context_score': self._calculate_context_score(user_state)
        }

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if not self._should_intervene(context):
            return None

        intervention_type = self._select_intervention_type(context)
        
        return {
            'content': self._personalize_content(intervention_type, user_profile),
            'delivery_style': self._optimize_delivery(user_profile),
            'timing': self._optimize_timing(context),
            'action_steps': self._generate_action_steps(intervention_type)
        }

    def track_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        self.user_profile['response_history'].append({
            'intervention_id': intervention_id,
            'response': user_response,
            'context': self.context_tracker.copy(),
            'timestamp': self._get_timestamp()
        })
        
        self._update_effectiveness_metrics(intervention_id, user_response)
        self._adapt_strategies(intervention_id, user_response)

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'time_pressure': user_state.get('time_pressure', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'fatigue_level': user_state.get('fatigue', 0.4)
        }
        
        weights = {'task_complexity': 0.4, 'time_pressure': 0.3, 
                  'interruption_frequency': 0.2, 'fatigue_level': 0.1}
                  
        return sum(factors[k] * weights[k] for k in factors)

    def _personalize_content(self, intervention_type, user_profile):
        """Create highly personalized intervention content"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        content = {
            'message': self._generate_message(intervention_type, personality_config),
            'tone': personality_config['communication_pref'],
            'complexity': self._adjust_complexity(personality_config['learning_style']),
            'examples': self._get_relevant_examples(user_profile),
            'action_items': self._create_action_items(intervention_type)
        }
        
        return content

    def _optimize_delivery(self, user_profile):
        """Optimize intervention delivery based on user preferences"""
        return {
            'channel': self._select_best_channel(user_profile),
            'format': self._select_content_format(user_profile),
            'urgency': self._calculate_urgency(),
            'reinforcement_schedule': self._get_reinforcement_schedule()
        }

    def _generate_action_steps(self, intervention_type):
        """Create specific, actionable recommendations"""
        return {
            'immediate_actions': self._get_immediate_actions(intervention_type),
            'short_term_goals': self._get_short_term_goals(),
            'success_metrics': self._define_success_metrics(),
            'follow_up_schedule': self._create_follow_up_schedule()
        }

    def _adapt_strategies(self, intervention_id, response):
        """Adapt coaching strategies based on effectiveness"""
        effectiveness = self._calculate_effectiveness(response)
        
        if effectiveness < 0.5:
            self._adjust_approach(intervention_id)
            self._update_timing_preferences(response)
            self._modify_content_strategy(response)

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        return (context['is_receptive'] and 
                context['optimal_timing'] and 
                context['context_score'] > 0.7)

    def _update_effectiveness_metrics(self, intervention_id, response):
        """Update intervention effectiveness tracking"""
        self.user_profile['effectiveness_scores'][intervention_id] = {
            'response_quality': self._assess_response_quality(response),
            'behavior_change': self._measure_behavior_change(response),
            'user_satisfaction': response.get('satisfaction_score', 0),
            'long_term_impact': self._estimate_long_term_impact(response)
        }