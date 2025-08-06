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
        self.behavioral_triggers = {
            'time_based': {},
            'context_based': {},
            'state_based': {}
        }

        # Intervention strategies library
        self.intervention_strategies = {
            'micro_break': {
                'threshold': 0.7,
                'duration': '2-5min',
                'triggers': ['high_cognitive_load', 'extended_focus']
            },
            'deep_work': {
                'threshold': 0.3,
                'duration': '45-90min',
                'triggers': ['low_interruption', 'high_energy']
            },
            'learning_sprint': {
                'threshold': 0.5,
                'duration': '25min',
                'triggers': ['optimal_receptivity', 'skill_gap']
            }
        }

    def assess_user_state(self, user_data):
        """
        Evaluates current user cognitive and emotional state
        """
        cognitive_load = self._calculate_cognitive_load(user_data)
        energy_level = self._assess_energy_level(user_data)
        focus_state = self._determine_focus_state(user_data)
        
        self.user_state.update({
            'cognitive_load': cognitive_load,
            'energy_level': energy_level,
            'focus_state': focus_state
        })
        
        return self.user_state

    def generate_personalized_intervention(self, user_context):
        """
        Creates targeted coaching intervention based on user state and context
        """
        user_state = self.assess_user_state(user_context)
        personality_type = user_context.get('personality_type')
        config = self.personality_type_configs.get(personality_type)

        # Select optimal intervention strategy
        strategy = self._select_intervention_strategy(user_state, config)
        
        # Personalize content and delivery
        intervention = {
            'content': self._generate_content(strategy, config),
            'timing': self._optimize_timing(user_state),
            'delivery_style': config['communication_pref'],
            'action_steps': self._generate_action_steps(strategy)
        }

        return intervention

    def _calculate_cognitive_load(self, user_data):
        """
        Estimates current cognitive load based on work patterns and context
        """
        task_complexity = user_data.get('task_complexity', 0.5)
        time_on_task = user_data.get('time_on_task', 0)
        interruption_frequency = user_data.get('interruption_frequency', 0)
        
        cognitive_load = (task_complexity * 0.4 + 
                        min(time_on_task / 120, 1) * 0.3 +
                        interruption_frequency * 0.3)
        
        return min(cognitive_load, 1.0)

    def _assess_energy_level(self, user_data):
        """
        Evaluates user energy level based on various factors
        """
        time_of_day = user_data.get('time_of_day', 12)
        breaks_taken = user_data.get('breaks_taken', 0)
        work_intensity = user_data.get('work_intensity', 0.5)

        energy = (1 - (work_intensity * 0.4) + 
                 (breaks_taken * 0.1) +
                 self._calculate_circadian_factor(time_of_day))
        
        return max(min(energy, 1.0), 0.0)

    def _determine_focus_state(self, user_data):
        """
        Analyzes current focus state and flow potential
        """
        if self.user_state['cognitive_load'] > 0.8:
            return 'overloaded'
        elif self.user_state['energy_level'] < 0.3:
            return 'fatigued'
        elif 0.3 <= self.user_state['cognitive_load'] <= 0.7:
            return 'optimal'
        else:
            return 'suboptimal'

    def _select_intervention_strategy(self, user_state, config):
        """
        Selects most appropriate intervention based on user state and preferences
        """
        if user_state['cognitive_load'] > 0.7:
            return self.intervention_strategies['micro_break']
        elif user_state['focus_state'] == 'optimal':
            return self.intervention_strategies['deep_work']
        else:
            return self.intervention_strategies['learning_sprint']

    def _generate_content(self, strategy, config):
        """
        Creates personalized content for the intervention
        """
        content = {
            'title': f"Optimized {strategy['duration']} {strategy['triggers'][0]} session",
            'description': self._personalize_message(strategy, config),
            'benefits': self._generate_benefits_list(strategy)
        }
        return content

    def _optimize_timing(self, user_state):
        """
        Determines optimal timing for intervention delivery
        """
        if user_state['cognitive_load'] > 0.8:
            return 'immediate'
        elif user_state['focus_state'] == 'optimal':
            return 'next_break'
        else:
            return 'next_context_switch'

    def _generate_action_steps(self, strategy):
        """
        Creates specific, actionable steps for the intervention
        """
        return [
            {'step': 1, 'action': 'Set clear intention', 'duration': '1min'},
            {'step': 2, 'action': 'Prepare environment', 'duration': '2min'},
            {'step': 3, 'action': 'Execute focused work', 'duration': strategy['duration']},
            {'step': 4, 'action': 'Review and reflect', 'duration': '2min'}
        ]

    def _calculate_circadian_factor(self, time_of_day):
        """
        Calculates energy factor based on circadian rhythm
        """
        peak_times = [10, 15]  # 10am and 3pm peaks
        distance_to_peak = min(abs(time_of_day - peak) for peak in peak_times)
        return max(0.5, 1 - (distance_to_peak / 12))

    def _personalize_message(self, strategy, config):
        """
        Creates personality-aligned coaching messages
        """
        style = config['communication_pref']
        if style == 'direct':
            return f"Optimize your performance with a {strategy['duration']} focused session"
        elif style == 'enthusiastic':
            return f"Ready for an energizing {strategy['duration']} breakthrough session?"
        return f"Let's improve your workflow with a {strategy['duration']} session"