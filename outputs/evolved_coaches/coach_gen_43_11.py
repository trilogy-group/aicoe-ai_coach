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
            'energy_level': 1.0,
            'focus_state': 'optimal',
            'stress_level': 0.0,
            'receptivity': 1.0
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'time_based': {},
            'context_based': {},
            'state_based': {}
        }

        # Intervention strategies
        self.intervention_types = {
            'micro_break': {'duration': 2, 'intensity': 0.2},
            'deep_work': {'duration': 45, 'intensity': 0.8},
            'reflection': {'duration': 5, 'intensity': 0.4},
            'skill_building': {'duration': 15, 'intensity': 0.6}
        }

        # Learning and adaptation parameters
        self.learning_rate = 0.1
        self.adaptation_threshold = 0.3
        self.effectiveness_history = []

    def assess_user_state(self, context_data):
        """
        Evaluates current user state based on multiple data points
        """
        cognitive_load = self._calculate_cognitive_load(context_data)
        energy_level = self._estimate_energy_level(context_data)
        focus_state = self._determine_focus_state(context_data)
        
        self.user_state.update({
            'cognitive_load': cognitive_load,
            'energy_level': energy_level,
            'focus_state': focus_state
        })
        
        return self.user_state

    def generate_intervention(self, user_state, context):
        """
        Creates personalized intervention based on user state and context
        """
        if not self._is_appropriate_timing(context):
            return None

        intervention_type = self._select_intervention_type(user_state)
        personalization = self._personalize_content(user_state, context)
        
        return {
            'type': intervention_type,
            'content': personalization['content'],
            'timing': personalization['timing'],
            'intensity': personalization['intensity']
        }

    def _calculate_cognitive_load(self, context_data):
        """
        Estimates current cognitive load based on work patterns and context
        """
        base_load = context_data.get('task_complexity', 0.5)
        time_pressure = context_data.get('deadline_proximity', 0.3)
        context_switches = context_data.get('context_switches', 0)
        
        cognitive_load = (base_load * 0.4 + 
                         time_pressure * 0.3 + 
                         min(context_switches * 0.1, 0.3))
        
        return min(cognitive_load, 1.0)

    def _estimate_energy_level(self, context_data):
        """
        Estimates user energy level based on activity patterns
        """
        time_active = context_data.get('time_active', 0)
        break_frequency = context_data.get('breaks_taken', 0)
        work_intensity = context_data.get('work_intensity', 0.5)
        
        energy_level = 1.0 - (time_active * 0.1) + (break_frequency * 0.15)
        energy_level *= (1 - work_intensity * 0.3)
        
        return max(min(energy_level, 1.0), 0.0)

    def _determine_focus_state(self, context_data):
        """
        Analyzes current focus state and flow potential
        """
        if (self.user_state['cognitive_load'] < 0.7 and 
            self.user_state['energy_level'] > 0.6):
            return 'optimal'
        elif self.user_state['cognitive_load'] > 0.8:
            return 'overloaded'
        else:
            return 'suboptimal'

    def _is_appropriate_timing(self, context):
        """
        Determines if intervention timing is appropriate
        """
        if context.get('in_meeting', False):
            return False
        if context.get('focus_mode', False):
            return False
        if self.user_state['cognitive_load'] > 0.9:
            return False
            
        return True

    def _select_intervention_type(self, user_state):
        """
        Selects most appropriate intervention based on user state
        """
        if user_state['cognitive_load'] > 0.7:
            return 'micro_break'
        elif user_state['energy_level'] < 0.4:
            return 'reflection'
        elif user_state['focus_state'] == 'optimal':
            return 'deep_work'
        else:
            return 'skill_building'

    def _personalize_content(self, user_state, context):
        """
        Personalizes intervention content based on user preferences and state
        """
        personality_type = context.get('personality_type', 'INTJ')
        config = self.personality_type_configs[personality_type]
        
        return {
            'content': self._generate_content(config, user_state),
            'timing': self._optimize_timing(config, context),
            'intensity': self._calibrate_intensity(user_state)
        }

    def update_effectiveness(self, intervention_result):
        """
        Updates intervention effectiveness metrics
        """
        self.effectiveness_history.append(intervention_result)
        
        if len(self.effectiveness_history) > 10:
            self._adapt_strategies()

    def _adapt_strategies(self):
        """
        Adapts intervention strategies based on effectiveness history
        """
        recent_effectiveness = sum(self.effectiveness_history[-10:]) / 10
        
        if recent_effectiveness < self.adaptation_threshold:
            self.learning_rate *= 1.1
            self._update_intervention_parameters()
        else:
            self.learning_rate *= 0.9

    def _update_intervention_parameters(self):
        """
        Updates intervention parameters based on learning
        """
        for intervention in self.intervention_types:
            self.intervention_types[intervention]['intensity'] *= (1 + self.learning_rate)
            self.intervention_types[intervention]['intensity'] = min(
                self.intervention_types[intervention]['intensity'], 1.0
            )