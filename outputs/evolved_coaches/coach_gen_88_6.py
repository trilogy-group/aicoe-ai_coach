class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral factors
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'autonomy', 'achievement'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'social_connection', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'specifics': 'Clear workspace of distractions'},
                    {'type': 'technique', 'duration': 25, 'specifics': 'Use Pomodoro timer'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take mindful pause'}
                ],
                'follow_up': {'timing': 30, 'metric': 'focus_duration'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller steps'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define meaningful completion reward'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 60, 'metric': 'task_completion'}
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progressive_rewards', 'social_proof'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'relatedness']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 0.8, 'afternoon': 0.6, 'evening': 0.4},
            'energy_level': {'high': 1.0, 'medium': 0.7, 'low': 0.4},
            'task_complexity': {'high': 0.9, 'medium': 0.6, 'low': 0.3},
            'interruption_frequency': {'high': 0.3, 'medium': 0.6, 'low': 0.9}
        }

    def generate_personalized_intervention(self, user_data, context):
        """Generate personalized coaching intervention based on user data and context"""
        
        # Calculate cognitive load and attention capacity
        cognitive_load = self._assess_cognitive_load(user_data, context)
        attention_capacity = self._calculate_attention_capacity(context)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(user_data, cognitive_load)
        
        # Personalize actions based on user preferences and context
        personalized_actions = self._personalize_actions(
            template['actions'],
            user_data['personality_type'],
            cognitive_load,
            attention_capacity
        )

        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavior_principles(personalized_actions, user_data)

        return {
            'intervention_type': template['type'],
            'actions': enhanced_actions,
            'timing': self._optimize_timing(context),
            'follow_up': template['follow_up'],
            'success_metrics': self._define_success_metrics(template, user_data)
        }

    def _assess_cognitive_load(self, user_data, context):
        """Calculate current cognitive load based on context and user state"""
        base_load = context['task_complexity'] * 0.4
        interruption_load = context['interruption_frequency'] * 0.3
        time_pressure_load = context['deadline_proximity'] * 0.3
        
        return min(1.0, base_load + interruption_load + time_pressure_load)

    def _calculate_attention_capacity(self, context):
        """Determine user's current attention capacity"""
        time_factor = self.context_factors['time_of_day'][context['time_of_day']]
        energy_factor = self.context_factors['energy_level'][context['energy_level']]
        
        return time_factor * energy_factor

    def _select_intervention_template(self, user_data, cognitive_load):
        """Select most appropriate intervention template based on user needs"""
        if cognitive_load > 0.7:
            return self.intervention_templates['focus']
        elif user_data.get('motivation_level', 0.5) < 0.6:
            return self.intervention_templates['motivation']
        # Additional template selection logic...

    def _personalize_actions(self, actions, personality_type, cognitive_load, attention_capacity):
        """Customize actions based on user characteristics"""
        config = self.personality_type_configs[personality_type]
        
        personalized = []
        for action in actions:
            if cognitive_load <= config['cognitive_load_threshold']:
                personalized.append({
                    **action,
                    'style': config['communication_pref'],
                    'learning_approach': config['learning_style'],
                    'difficulty': self._adjust_difficulty(action, attention_capacity)
                })
        
        return personalized

    def _apply_behavior_principles(self, actions, user_data):
        """Enhance actions with behavioral psychology principles"""
        enhanced = []
        for action in actions:
            enhanced.append({
                **action,
                'reinforcement': self._select_reinforcement(user_data),
                'habit_cue': self._identify_habit_trigger(action, user_data),
                'motivation_elements': self._add_motivation_elements(user_data)
            })
        return enhanced

    def _optimize_timing(self, context):
        """Determine optimal timing for intervention delivery"""
        return {
            'best_time': self._calculate_optimal_time(context),
            'frequency': self._determine_frequency(context),
            'spacing': self._calculate_spacing(context)
        }

    def _define_success_metrics(self, template, user_data):
        """Define specific, measurable success metrics"""
        return {
            'primary_metric': template['follow_up']['metric'],
            'target_value': self._calculate_target(template, user_data),
            'measurement_period': template['follow_up']['timing'],
            'progress_indicators': self._define_progress_indicators(template)
        }