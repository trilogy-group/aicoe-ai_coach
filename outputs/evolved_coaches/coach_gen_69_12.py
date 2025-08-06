class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize user profile with enhanced tracking"""
        self.user_profiles[user_id] = {
            'cognitive_state': None,
            'attention_capacity': 1.0,
            'motivation_level': 0.5,
            'stress_level': 0.0,
            'learning_patterns': [],
            'intervention_preferences': {},
            'context_sensitivity': 0.5,
            'behavioral_stage': 'contemplation'
        }
        
    def assess_cognitive_load(self, user_id, context_data):
        """Enhanced cognitive load assessment"""
        base_load = self._calculate_base_load(context_data)
        temporal_factor = self._get_temporal_weight(context_data['time'])
        context_factor = self._analyze_context_demands(context_data)
        
        return min(1.0, base_load * temporal_factor * context_factor)

    def generate_intervention(self, user_id, context):
        """Generate personalized coaching intervention"""
        if not self._is_receptive(user_id, context):
            return None
            
        user_state = self._get_current_state(user_id)
        intervention_type = self._select_intervention_type(user_state)
        
        intervention = {
            'type': intervention_type,
            'content': self._generate_content(user_id, intervention_type),
            'timing': self._optimize_timing(user_id, context),
            'intensity': self._calculate_intensity(user_state),
            'action_steps': self._generate_action_steps(user_state)
        }
        
        self._record_intervention(user_id, intervention)
        return intervention

    def update_user_model(self, user_id, feedback_data):
        """Update user model based on intervention feedback"""
        profile = self.user_profiles[user_id]
        
        # Update behavioral stage
        profile['behavioral_stage'] = self._progress_behavioral_stage(
            profile['behavioral_stage'], 
            feedback_data['compliance']
        )
        
        # Update intervention preferences
        self._update_preferences(user_id, feedback_data)
        
        # Adjust sensitivity parameters
        profile['context_sensitivity'] = self._recalibrate_sensitivity(
            profile['context_sensitivity'],
            feedback_data
        )

    def _calculate_base_load(self, context_data):
        """Calculate baseline cognitive load"""
        task_complexity = context_data.get('task_complexity', 0.5)
        environmental_load = context_data.get('environmental_load', 0.3)
        current_demands = context_data.get('current_demands', 0.4)
        
        return (0.4 * task_complexity + 
                0.3 * environmental_load + 
                0.3 * current_demands)

    def _analyze_context_demands(self, context):
        """Analyze contextual demands and constraints"""
        return min(1.0, sum([
            context.get('urgency', 0) * 0.3,
            context.get('complexity', 0) * 0.4,
            context.get('pressure', 0) * 0.3
        ]))

    def _is_receptive(self, user_id, context):
        """Check if user is receptive to intervention"""
        profile = self.user_profiles[user_id]
        cognitive_load = self.assess_cognitive_load(user_id, context)
        
        return (cognitive_load < 0.8 and
                profile['attention_capacity'] > 0.3 and
                self._check_timing_appropriate(context))

    def _select_intervention_type(self, user_state):
        """Select appropriate intervention type"""
        if user_state['stress_level'] > 0.7:
            return 'stress_management'
        elif user_state['motivation_level'] < 0.3:
            return 'motivation_boost'
        elif user_state['attention_capacity'] < 0.4:
            return 'focus_enhancement'
        else:
            return 'general_coaching'

    def _generate_content(self, user_id, intervention_type):
        """Generate personalized intervention content"""
        profile = self.user_profiles[user_id]
        
        content_templates = {
            'stress_management': self._get_stress_management_content,
            'motivation_boost': self._get_motivation_content,
            'focus_enhancement': self._get_focus_content,
            'general_coaching': self._get_general_content
        }
        
        return content_templates[intervention_type](profile)

    def _generate_action_steps(self, user_state):
        """Generate specific, actionable steps"""
        return [
            {
                'step': 'immediate_action',
                'description': self._get_immediate_action(user_state),
                'difficulty': 'low',
                'expected_duration': '5min'
            },
            {
                'step': 'short_term_goal',
                'description': self._get_short_term_goal(user_state),
                'difficulty': 'medium',
                'expected_duration': '1day'
            },
            {
                'step': 'long_term_practice',
                'description': self._get_long_term_practice(user_state),
                'difficulty': 'high',
                'expected_duration': '1week'
            }
        ]

    def _optimize_timing(self, user_id, context):
        """Optimize intervention timing"""
        recent_interventions = self.intervention_history.get(user_id, [])
        current_load = self.assess_cognitive_load(user_id, context)
        
        if len(recent_interventions) > 0:
            last_intervention = recent_interventions[-1]
            time_since_last = context['time'] - last_intervention['time']
            
            if time_since_last < self._get_minimum_interval(current_load):
                return 'defer'
                
        return 'immediate'

    def _calculate_intensity(self, user_state):
        """Calculate appropriate intervention intensity"""
        base_intensity = 0.5
        modifiers = {
            'stress': -0.2 if user_state['stress_level'] > 0.6 else 0,
            'motivation': 0.2 if user_state['motivation_level'] < 0.4 else 0,
            'attention': -0.1 if user_state['attention_capacity'] < 0.5 else 0
        }
        
        return max(0.1, min(1.0, base_intensity + sum(modifiers.values())))

    def _record_intervention(self, user_id, intervention):
        """Record intervention for tracking"""
        if user_id not in self.intervention_history:
            self.intervention_history[user_id] = []
            
        self.intervention_history[user_id].append(intervention)

    def _progress_behavioral_stage(self, current_stage, compliance):
        """Progress through stages of behavioral change"""
        stages = ['precontemplation', 'contemplation', 'preparation', 
                 'action', 'maintenance']
        
        if compliance > 0.7:
            current_idx = stages.index(current_stage)
            if current_idx < len(stages) - 1:
                return stages[current_idx + 1]
                
        return current_stage