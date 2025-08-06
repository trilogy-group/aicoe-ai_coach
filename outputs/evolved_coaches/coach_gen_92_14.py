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
            'focus_state': 'neutral',
            'time_of_day': None,
            'work_context': None,
            'interruption_cost': 0.0
        }

        # Behavioral psychology components
        self.behavioral_patterns = {
            'habit_strength': {},
            'motivation_factors': {},
            'resistance_points': {},
            'success_triggers': {}
        }

        # Intervention optimization
        self.intervention_config = {
            'min_time_between': 30,  # minutes
            'max_daily': 8,
            'cognitive_load_threshold': 0.7,
            'priority_threshold': 0.8
        }

        # User profile tracking
        self.user_profile = {
            'preferences': {},
            'learning_history': [],
            'response_patterns': {},
            'effectiveness_metrics': {},
            'engagement_scores': {}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(user_state)
        focus_impact = self._assess_focus_impact(environment_data)
        timing_score = self._evaluate_timing(user_state['time'])
        
        return {
            'cognitive_load': cognitive_load,
            'focus_impact': focus_impact,
            'timing_score': timing_score,
            'overall_receptivity': (cognitive_load + focus_impact + timing_score) / 3
        }

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if not self._should_intervene(context):
            return None

        intervention_type = self._select_intervention_type(context, user_profile)
        content = self._generate_content(intervention_type, user_profile)
        delivery = self._optimize_delivery(content, context)

        return {
            'type': intervention_type,
            'content': content,
            'delivery': delivery,
            'timing': self._get_optimal_timing(),
            'priority': self._calculate_priority(context)
        }

    def track_effectiveness(self, intervention_id, user_response):
        """Monitor and analyze intervention effectiveness"""
        response_data = {
            'engagement': user_response['engagement'],
            'completion': user_response['completion'],
            'feedback': user_response['feedback'],
            'behavior_change': user_response['behavior_change']
        }

        self._update_effectiveness_metrics(intervention_id, response_data)
        self._adjust_strategies(response_data)
        
        return self._calculate_effectiveness_score(response_data)

    def _calculate_cognitive_load(self, user_state):
        """Assess current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'time_pressure': user_state.get('time_pressure', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0.3),
            'mental_fatigue': user_state.get('fatigue', 0.4)
        }
        
        weights = {'task_complexity': 0.4, 'time_pressure': 0.3, 
                  'interruption_frequency': 0.2, 'mental_fatigue': 0.1}
        
        return sum(factors[k] * weights[k] for k in factors)

    def _optimize_delivery(self, content, context):
        """Optimize intervention delivery based on context"""
        return {
            'channel': self._select_channel(context),
            'format': self._select_format(content, context),
            'urgency': self._calculate_urgency(context),
            'reinforcement': self._get_reinforcement_schedule(context)
        }

    def _should_intervene(self, context):
        """Determine if intervention is appropriate now"""
        if context['cognitive_load'] > self.intervention_config['cognitive_load_threshold']:
            return False
        if context['timing_score'] < 0.4:
            return False
        if not self._check_intervention_spacing():
            return False
        return True

    def _select_intervention_type(self, context, user_profile):
        """Choose most effective intervention type for current situation"""
        options = {
            'micro_lesson': self._score_intervention('micro_lesson', context),
            'quick_tip': self._score_intervention('quick_tip', context),
            'reflection_prompt': self._score_intervention('reflection_prompt', context),
            'action_reminder': self._score_intervention('action_reminder', context)
        }
        return max(options.items(), key=lambda x: x[1])[0]

    def _generate_content(self, intervention_type, user_profile):
        """Create personalized intervention content"""
        template = self._get_content_template(intervention_type)
        personalization = self._apply_personalization(template, user_profile)
        return self._format_content(personalization, intervention_type)

    def _update_effectiveness_metrics(self, intervention_id, response_data):
        """Update intervention effectiveness tracking"""
        self.user_profile['effectiveness_metrics'][intervention_id] = response_data
        self._update_learning_patterns(response_data)
        self._adjust_intervention_parameters(response_data)

    def _adjust_strategies(self, response_data):
        """Adapt coaching strategies based on effectiveness"""
        if response_data['engagement'] < 0.5:
            self._adjust_engagement_approach()
        if response_data['behavior_change'] < 0.3:
            self._strengthen_behavioral_triggers()
        self._update_timing_preferences(response_data)