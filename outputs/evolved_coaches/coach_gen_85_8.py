class EnhancedAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced cognitive and behavioral tracking
        self.user_state = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_state': 'optimal',
            'stress_level': 0.0,
            'receptivity': 1.0
        }
        
        # Intervention configuration
        self.intervention_settings = {
            'min_time_between': 30, # minutes
            'max_daily': 8,
            'intensity_factor': 0.7
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'task_completion': self.reward_completion,
            'focus_drop': self.focus_intervention,
            'stress_spike': self.stress_management,
            'learning_opportunity': self.growth_prompt
        }

        # Context awareness system
        self.context_tracker = {
            'time_patterns': {},
            'location_context': {},
            'activity_history': [],
            'social_context': {}
        }

    def assess_user_state(self, user_data):
        """Evaluate current user cognitive and emotional state"""
        current_state = {
            'cognitive_load': self._calculate_cognitive_load(user_data),
            'energy_level': self._assess_energy(user_data),
            'focus_state': self._determine_focus_state(user_data),
            'stress_level': self._measure_stress(user_data),
            'receptivity': self._calculate_receptivity(user_data)
        }
        self.user_state.update(current_state)
        return current_state

    def generate_intervention(self, user_context):
        """Create personalized coaching intervention"""
        if not self._should_intervene(user_context):
            return None

        intervention_type = self._select_intervention_type()
        
        intervention = {
            'content': self._generate_content(intervention_type),
            'timing': self._optimize_timing(),
            'intensity': self._calculate_intensity(),
            'delivery_method': self._select_delivery_method(),
            'follow_up': self._plan_follow_up()
        }

        return self._personalize_intervention(intervention)

    def _calculate_cognitive_load(self, data):
        """Assess current cognitive load based on activity patterns"""
        task_complexity = data.get('task_complexity', 0.5)
        context_switches = data.get('context_switches', 0)
        time_pressure = data.get('time_pressure', 0.5)
        
        return (task_complexity + (context_switches * 0.1) + time_pressure) / 3

    def _assess_energy(self, data):
        """Evaluate user energy levels"""
        time_active = data.get('time_active', 0)
        break_frequency = data.get('breaks_taken', 0)
        activity_intensity = data.get('activity_intensity', 0.5)
        
        return max(0, 1 - (time_active * 0.1) + (break_frequency * 0.2))

    def _determine_focus_state(self, data):
        """Analyze current focus and flow state"""
        productivity = data.get('productivity_score', 0.5)
        distraction_level = data.get('distractions', 0)
        deep_work_time = data.get('deep_work_duration', 0)
        
        if productivity > 0.8 and distraction_level < 0.2:
            return 'flow'
        elif productivity > 0.6:
            return 'focused'
        else:
            return 'distracted'

    def _should_intervene(self, context):
        """Determine if intervention is appropriate"""
        last_intervention = context.get('last_intervention_time', 0)
        current_receptivity = self.user_state['receptivity']
        cognitive_load = self.user_state['cognitive_load']
        
        return (
            current_receptivity > 0.6 and
            cognitive_load < 0.8 and
            self._enough_time_elapsed(last_intervention)
        )

    def _generate_content(self, intervention_type):
        """Create specific intervention content"""
        templates = {
            'focus': "I notice you might be getting distracted. Let's try {technique} for the next {duration} minutes.",
            'energy': "Time for a quick energy boost! {activity} can help refresh your mind.",
            'growth': "Great progress! Here's a challenge to stretch your abilities: {challenge}",
            'stress': "Let's take a moment to reset. Try this quick {relaxation} technique."
        }
        
        return self._fill_template(templates[intervention_type])

    def _personalize_intervention(self, intervention):
        """Customize intervention based on user profile"""
        personality = self.personality_type_configs.get(self.user_state.get('personality_type'))
        
        if personality:
            intervention['content'] = self._adapt_to_style(
                intervention['content'], 
                personality['communication_pref']
            )
            intervention['timing'] = self._adjust_timing(
                intervention['timing'],
                personality['work_pattern']
            )
        
        return intervention

    def reward_completion(self):
        """Positive reinforcement for task completion"""
        return {
            'type': 'celebration',
            'message': 'Excellent work! You're building momentum.',
            'suggestion': self._generate_next_step()
        }

    def focus_intervention(self):
        """Help restore focus during distractions"""
        return {
            'type': 'focus',
            'technique': self._select_focus_technique(),
            'duration': self._calculate_optimal_duration()
        }

    def stress_management(self):
        """Provide stress reduction guidance"""
        return {
            'type': 'relaxation',
            'technique': self._select_relaxation_technique(),
            'duration': 5
        }

    def growth_prompt(self):
        """Encourage skill development"""
        return {
            'type': 'challenge',
            'activity': self._select_growth_activity(),
            'benefit': self._explain_benefit()
        }

    def update_context(self, new_context):
        """Update context tracking system"""
        self.context_tracker['activity_history'].append(new_context)
        self._update_patterns()
        self._prune_old_data()