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
        self.behavioral_models = {
            'habit_formation': {'cue': None, 'routine': None, 'reward': None},
            'motivation': {'intrinsic': 0.0, 'extrinsic': 0.0},
            'flow_state': {'depth': 0.0, 'duration': 0},
            'resistance': {'current': 0.0, 'threshold': 0.7}
        }

        # Personalization tracking
        self.user_profile = {
            'personality_type': None,
            'learning_patterns': [],
            'response_history': [],
            'success_metrics': {},
            'preference_weights': {}
        }

        # Intervention configurations
        self.intervention_types = {
            'micro_break': {'duration': 2, 'frequency': 45},
            'deep_work': {'duration': 90, 'preparation': 15},
            'reflection': {'duration': 10, 'prompt_style': 'open'},
            'skill_building': {'complexity': 'adaptive', 'scaffolding': True}
        }

    def assess_context(self, user_state, environment_data):
        """Evaluate current user context and environment"""
        self.context_tracker.update({
            'cognitive_load': self._calculate_cognitive_load(user_state),
            'energy_level': self._estimate_energy(user_state),
            'time_of_day': environment_data.get('time'),
            'work_context': environment_data.get('activity'),
            'interruption_cost': self._calculate_interruption_cost()
        })
        return self.context_tracker

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if not self._should_intervene():
            return None

        intervention = {
            'type': self._select_intervention_type(),
            'content': self._generate_content(),
            'timing': self._optimize_timing(),
            'delivery_style': self._personalize_delivery(user_profile),
            'action_steps': self._create_action_steps()
        }

        return self._validate_and_enhance(intervention)

    def track_response(self, user_response, intervention_data):
        """Track and analyze user response to intervention"""
        response_metrics = {
            'engagement': self._calculate_engagement(user_response),
            'completion': self._verify_completion(user_response),
            'satisfaction': self._measure_satisfaction(user_response),
            'behavior_change': self._assess_behavior_change()
        }

        self.user_profile['response_history'].append({
            'intervention': intervention_data,
            'response': response_metrics,
            'timestamp': self._get_timestamp()
        })

        self._update_learning_patterns(response_metrics)
        return response_metrics

    def _calculate_cognitive_load(self, user_state):
        """Estimate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': user_state.get('task_complexity', 0.5),
            'context_switches': user_state.get('context_switches', 0),
            'time_pressure': user_state.get('deadline_proximity', 0.5),
            'interruption_frequency': user_state.get('interruptions', 0)
        }
        
        weighted_load = sum(v * self.user_profile['preference_weights'].get(k, 1.0) 
                          for k, v in factors.items())
        return min(1.0, weighted_load)

    def _create_action_steps(self):
        """Generate specific, actionable recommendations"""
        context = self.context_tracker
        return {
            'immediate': self._generate_immediate_action(),
            'short_term': self._generate_short_term_steps(),
            'follow_up': self._create_follow_up_plan(),
            'success_metrics': self._define_success_metrics()
        }

    def _personalize_delivery(self, user_profile):
        """Customize intervention delivery based on user preferences"""
        personality_config = self.personality_type_configs.get(
            user_profile['personality_type'], 
            self.personality_type_configs['INTJ']
        )
        
        return {
            'tone': personality_config['communication_pref'],
            'detail_level': self._adapt_detail_level(),
            'format': self._select_optimal_format(),
            'timing': self._optimize_timing()
        }

    def _should_intervene(self):
        """Determine if intervention is appropriate now"""
        return (
            self.context_tracker['cognitive_load'] < 0.8 and
            self.context_tracker['interruption_cost'] < 0.6 and
            self._check_timing_appropriate() and
            self._verify_user_receptivity()
        )

    def _update_learning_patterns(self, metrics):
        """Update user learning patterns based on intervention results"""
        self.user_profile['learning_patterns'].append({
            'context': self.context_tracker.copy(),
            'metrics': metrics,
            'timestamp': self._get_timestamp()
        })
        
        self._optimize_future_interventions()

    def _optimize_future_interventions(self):
        """Adjust intervention strategies based on historical performance"""
        recent_patterns = self.user_profile['learning_patterns'][-10:]
        
        success_metrics = {
            'engagement': sum(p['metrics']['engagement'] for p in recent_patterns) / len(recent_patterns),
            'completion': sum(p['metrics']['completion'] for p in recent_patterns) / len(recent_patterns),
            'satisfaction': sum(p['metrics']['satisfaction'] for p in recent_patterns) / len(recent_patterns)
        }

        self.user_profile['success_metrics'] = success_metrics
        self._adjust_intervention_parameters(success_metrics)