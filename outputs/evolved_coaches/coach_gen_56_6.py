class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced cognitive state tracking
        self.cognitive_state = {
            'attention_level': 0.0,
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'stress_level': 0.0,
            'flow_state': False
        }

        # Behavioral psychology components
        self.behavioral_triggers = {
            'time_based': {},
            'context_based': {},
            'state_based': {},
            'pattern_based': {}
        }

        # Intervention configuration
        self.intervention_settings = {
            'min_interval': 30,  # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'adaptivity_rate': 0.1
        }

        # User profile tracking
        self.user_profile = {
            'preferences': {},
            'response_history': [],
            'effectiveness_metrics': {},
            'learning_patterns': {},
            'peak_performance_times': []
        }

    def assess_context(self, user_data):
        """Evaluate current user context for intervention appropriateness"""
        context_score = 0.0
        
        # Analyze cognitive state
        cognitive_load = self._calculate_cognitive_load(user_data)
        attention_level = self._estimate_attention(user_data)
        
        # Check timing appropriateness
        timing_score = self._evaluate_timing(user_data['timestamp'])
        
        # Assess user receptivity
        receptivity = self._calculate_receptivity(user_data)
        
        return {
            'cognitive_load': cognitive_load,
            'attention_level': attention_level,
            'timing_score': timing_score,
            'receptivity': receptivity,
            'overall_score': (cognitive_load + attention_level + timing_score + receptivity) / 4
        }

    def generate_intervention(self, context, user_profile):
        """Create personalized coaching intervention"""
        if not self._should_intervene(context):
            return None
            
        intervention_type = self._select_intervention_type(context, user_profile)
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(intervention_type, context, user_profile),
            'intensity': self._calculate_intensity(context),
            'timing': self._optimize_timing(context),
            'action_steps': self._generate_action_steps(intervention_type, user_profile)
        }
        
        return self._personalize_intervention(intervention, user_profile)

    def update_effectiveness(self, intervention_id, user_response):
        """Track and update intervention effectiveness"""
        effectiveness = self._calculate_effectiveness(user_response)
        self.user_profile['effectiveness_metrics'][intervention_id] = effectiveness
        
        # Update learning patterns
        self._update_learning_patterns(intervention_id, effectiveness)
        
        # Adjust intervention parameters
        self._adapt_parameters(effectiveness)

    def _calculate_cognitive_load(self, user_data):
        """Estimate current cognitive load based on user activity"""
        task_complexity = self._assess_task_complexity(user_data['current_task'])
        context_demands = self._assess_context_demands(user_data['environment'])
        temporal_pressure = self._assess_temporal_pressure(user_data['deadlines'])
        
        return (task_complexity + context_demands + temporal_pressure) / 3

    def _estimate_attention(self, user_data):
        """Estimate user's current attention level"""
        focus_indicators = self._analyze_focus_indicators(user_data)
        distraction_level = self._assess_distractions(user_data['environment'])
        recent_activity = self._analyze_recent_activity(user_data['activity_log'])
        
        return self._combine_attention_factors(focus_indicators, distraction_level, recent_activity)

    def _generate_action_steps(self, intervention_type, user_profile):
        """Create specific, actionable recommendations"""
        base_actions = self._get_base_actions(intervention_type)
        personalized_actions = self._personalize_actions(base_actions, user_profile)
        
        return [
            {
                'step': i + 1,
                'action': action['description'],
                'timeframe': action['timeframe'],
                'difficulty': action['difficulty'],
                'expected_outcome': action['outcome']
            }
            for i, action in enumerate(personalized_actions)
        ]

    def _personalize_intervention(self, intervention, user_profile):
        """Customize intervention based on user profile"""
        personality_type = user_profile.get('personality_type', 'INTJ')
        config = self.personality_type_configs[personality_type]
        
        intervention['style'] = config['communication_pref']
        intervention['pacing'] = config['learning_style']
        intervention['structure'] = config['work_pattern']
        
        return intervention

    def _adapt_parameters(self, effectiveness):
        """Adjust intervention parameters based on effectiveness"""
        self.intervention_settings['intensity_level'] *= (1 + self.intervention_settings['adaptivity_rate'] * (effectiveness - 0.5))
        self.intervention_settings['intensity_level'] = max(0.1, min(1.0, self.intervention_settings['intensity_level']))

    def _update_learning_patterns(self, intervention_id, effectiveness):
        """Update user learning patterns based on intervention effectiveness"""
        intervention = self.user_profile['response_history'].get(intervention_id)
        if intervention:
            pattern = self._extract_pattern(intervention)
            self.user_profile['learning_patterns'][pattern] = {
                'count': self.user_profile['learning_patterns'].get(pattern, {}).get('count', 0) + 1,
                'effectiveness': (self.user_profile['learning_patterns'].get(pattern, {}).get('effectiveness', 0) + effectiveness) / 2
            }