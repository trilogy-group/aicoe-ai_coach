class EnhancedAICoach:
    def __init__(self):
        # Personality and learning profiles
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
        self.behavioral_patterns = {
            'habit_strength': {},
            'motivation_factors': {},
            'resistance_patterns': {},
            'success_triggers': {}
        }
        
        # Intervention configuration
        self.intervention_settings = {
            'min_time_between': 30, # minutes
            'max_daily': 8,
            'intensity_level': 0.5,
            'nudge_style': 'adaptive'
        }

    def assess_user_state(self, user_data):
        """Evaluate current user cognitive and emotional state"""
        current_state = {
            'cognitive_load': self._calculate_cognitive_load(user_data),
            'energy_level': self._estimate_energy(user_data),
            'receptivity': self._assess_receptivity(user_data),
            'progress_phase': self._determine_progress_phase(user_data)
        }
        return current_state

    def generate_personalized_intervention(self, user_state, user_profile):
        """Create targeted coaching intervention"""
        if not self._should_intervene(user_state):
            return None
            
        intervention = {
            'type': self._select_intervention_type(user_state, user_profile),
            'content': self._generate_content(user_state, user_profile),
            'timing': self._optimize_timing(user_state),
            'intensity': self._calibrate_intensity(user_state),
            'action_steps': self._create_action_steps(user_state, user_profile)
        }
        
        return self._format_intervention(intervention)

    def _calculate_cognitive_load(self, user_data):
        """Estimate current cognitive load based on multiple factors"""
        load_factors = {
            'task_complexity': 0.3,
            'context_switches': 0.2,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2
        }
        
        total_load = sum(
            load_factors[factor] * user_data.get(factor, 0) 
            for factor in load_factors
        )
        return min(total_load, 1.0)

    def _assess_receptivity(self, user_data):
        """Determine user's current receptivity to coaching"""
        factors = {
            'recent_success': 0.2,
            'energy_level': 0.3,
            'time_availability': 0.3,
            'stress_level': -0.2
        }
        
        receptivity = sum(
            factors[f] * user_data.get(f, 0)
            for f in factors
        )
        return max(0, min(receptivity, 1.0))

    def _select_intervention_type(self, user_state, user_profile):
        """Choose most appropriate intervention type"""
        options = {
            'micro_habit': {'cognitive_load_max': 0.3, 'energy_min': 0.2},
            'reflection': {'cognitive_load_max': 0.6, 'energy_min': 0.4},
            'challenge': {'cognitive_load_max': 0.7, 'energy_min': 0.7},
            'reinforcement': {'cognitive_load_max': 0.4, 'energy_min': 0.3}
        }
        
        suitable_types = [
            t for t, reqs in options.items()
            if user_state['cognitive_load'] <= reqs['cognitive_load_max']
            and user_state['energy_level'] >= reqs['energy_min']
        ]
        
        return self._rank_intervention_types(suitable_types, user_profile)[0]

    def _create_action_steps(self, user_state, user_profile):
        """Generate specific, actionable next steps"""
        learning_style = user_profile['learning_style']
        progress_phase = user_state['progress_phase']
        
        action_templates = {
            'systematic': {
                'beginning': ['Break down goal into components', 'Create timeline'],
                'middle': ['Review progress metrics', 'Adjust approach'],
                'advanced': ['Optimize process', 'Share learnings']
            },
            'exploratory': {
                'beginning': ['Experiment with approaches', 'Document insights'],
                'middle': ['Identify patterns', 'Build on successes'],
                'advanced': ['Synthesize learning', 'Expand application']
            }
        }
        
        base_steps = action_templates[learning_style][progress_phase]
        return self._personalize_steps(base_steps, user_profile)

    def _optimize_timing(self, user_state):
        """Determine optimal intervention timing"""
        factors = {
            'cognitive_load': -0.3,
            'energy_level': 0.2,
            'time_of_day_fit': 0.3,
            'task_breakpoint': 0.2
        }
        
        timing_score = sum(
            factors[f] * user_state.get(f, 0)
            for f in factors
        )
        
        return self._calculate_optimal_delay(timing_score)

    def _calibrate_intensity(self, user_state):
        """Adjust intervention intensity based on user state"""
        base_intensity = self.intervention_settings['intensity_level']
        
        modifiers = {
            'cognitive_load': -0.2,
            'energy_level': 0.2,
            'receptivity': 0.3
        }
        
        intensity = base_intensity + sum(
            modifiers[m] * user_state.get(m, 0)
            for m in modifiers
        )
        
        return max(0.1, min(intensity, 1.0))

    def update_effectiveness(self, intervention_results):
        """Update system based on intervention effectiveness"""
        self._update_behavioral_patterns(intervention_results)
        self._adjust_intervention_settings(intervention_results)
        self._refine_user_model(intervention_results)