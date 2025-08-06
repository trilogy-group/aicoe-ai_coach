class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }
        
        # Enhanced user state tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_state': 'neutral',
            'stress_level': 0.0,
            'receptivity': 0.0
        }
        
        # Behavioral psychology patterns
        self.behavior_patterns = {
            'work_cycles': [],
            'response_history': [],
            'intervention_effectiveness': {},
            'habit_formation_progress': {}
        }
        
        # Context awareness parameters
        self.context = {
            'time_of_day': None,
            'work_context': None,
            'environment': None,
            'recent_activities': []
        }
        
        # Intervention strategies library
        self.strategies = {
            'motivation': self._get_motivation_strategies(),
            'focus': self._get_focus_strategies(),
            'stress': self._get_stress_management(),
            'productivity': self._get_productivity_techniques()
        }

    def update_user_state(self, metrics):
        """Update user state based on real-time metrics"""
        self.user_state.update({
            'cognitive_load': self._calculate_cognitive_load(metrics),
            'energy_level': self._assess_energy_level(metrics),
            'focus_state': self._determine_focus_state(metrics),
            'stress_level': self._measure_stress(metrics),
            'receptivity': self._calculate_receptivity(metrics)
        })

    def generate_intervention(self, user_context):
        """Generate personalized coaching intervention"""
        # Update context
        self._update_context(user_context)
        
        # Select optimal intervention timing
        if not self._is_good_intervention_timing():
            return None
            
        # Get personalized strategy
        strategy = self._select_optimal_strategy()
        
        # Generate specific actionable recommendation
        intervention = self._create_intervention(strategy)
        
        # Track intervention
        self._log_intervention(intervention)
        
        return intervention

    def _select_optimal_strategy(self):
        """Select best strategy based on user state and context"""
        strategies = []
        
        # Consider cognitive load
        if self.user_state['cognitive_load'] > 0.7:
            strategies.extend(self.strategies['focus'])
            
        # Consider energy level
        if self.user_state['energy_level'] < 0.4:
            strategies.extend(self.strategies['motivation'])
            
        # Consider stress level
        if self.user_state['stress_level'] > 0.6:
            strategies.extend(self.strategies['stress'])
            
        # Weight strategies by effectiveness history
        weighted_strategies = self._weight_by_effectiveness(strategies)
        
        return self._select_best_strategy(weighted_strategies)

    def _create_intervention(self, strategy):
        """Create specific actionable intervention"""
        return {
            'content': self._personalize_content(strategy),
            'timing': self._optimize_timing(),
            'format': self._select_delivery_format(),
            'action_steps': self._generate_action_steps(strategy),
            'follow_up': self._create_follow_up_plan()
        }

    def _personalize_content(self, strategy):
        """Personalize intervention content"""
        personality = self._get_user_personality()
        learning_style = self.personality_type_configs[personality]['learning_style']
        comm_pref = self.personality_type_configs[personality]['communication_pref']
        
        return self._adapt_content(strategy, learning_style, comm_pref)

    def _generate_action_steps(self, strategy):
        """Generate specific actionable steps"""
        steps = []
        context = self.context['work_context']
        
        for step in strategy['steps']:
            specific_step = {
                'action': self._contextualize_step(step, context),
                'timeframe': self._suggest_timeframe(step),
                'success_criteria': self._define_success_criteria(step),
                'potential_obstacles': self._identify_obstacles(step),
                'mitigation_strategies': self._suggest_mitigations(step)
            }
            steps.append(specific_step)
            
        return steps

    def _calculate_receptivity(self, metrics):
        """Calculate user receptivity to interventions"""
        factors = [
            metrics.get('focus_duration', 0),
            metrics.get('task_completion_rate', 0),
            metrics.get('response_time', 0),
            self.user_state['cognitive_load'],
            self.user_state['stress_level']
        ]
        return sum(factors) / len(factors)

    def _is_good_intervention_timing(self):
        """Determine if current moment is good for intervention"""
        return (
            self.user_state['receptivity'] > 0.6 and
            self.user_state['cognitive_load'] < 0.8 and
            self._check_time_spacing() and
            not self._is_in_flow_state()
        )

    def _log_intervention(self, intervention):
        """Track intervention for effectiveness analysis"""
        self.behavior_patterns['intervention_effectiveness'][intervention['id']] = {
            'timestamp': self._get_timestamp(),
            'user_state': self.user_state.copy(),
            'context': self.context.copy(),
            'response': None
        }

    def _update_effectiveness(self, intervention_id, response):
        """Update intervention effectiveness tracking"""
        if intervention_id in self.behavior_patterns['intervention_effectiveness']:
            self.behavior_patterns['intervention_effectiveness'][intervention_id]['response'] = response
            self._adjust_strategies(intervention_id, response)

    def process_feedback(self, feedback):
        """Process user feedback and adapt strategies"""
        self._update_effectiveness(feedback['intervention_id'], feedback['response'])
        self._adjust_user_model(feedback)
        self._refine_timing_model(feedback)
        self._update_strategy_weights(feedback)