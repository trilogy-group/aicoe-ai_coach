class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
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
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Enable focus mode', 'time_est': '1 min'},
                    {'step': 'Set timer for focused work', 'time_est': '1 min'}
                ],
                'success_metrics': ['time_on_task', 'task_completion'],
                'follow_up_window': 30 # minutes
            },
            'productivity': {
                'triggers': ['low_output', 'procrastination'],
                'actions': [
                    {'step': 'Break task into smaller chunks', 'time_est': '5 min'},
                    {'step': 'Set SMART goals', 'time_est': '10 min'},
                    {'step': 'Schedule focused work blocks', 'time_est': '5 min'}
                ],
                'success_metrics': ['tasks_completed', 'quality_score'],
                'follow_up_window': 120
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['positive', 'negative', 'intermittent'],
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose']
        }

        self.user_context = {}
        self.intervention_history = []
        self.success_metrics = {}

    def analyze_user_context(self, context_data):
        """Analyze user context for personalized interventions"""
        self.user_context = {
            'personality_type': context_data.get('personality_type'),
            'current_task': context_data.get('current_task'),
            'cognitive_load': self._estimate_cognitive_load(context_data),
            'energy_level': context_data.get('energy_level', 0.5),
            'time_of_day': context_data.get('time_of_day'),
            'recent_activity': context_data.get('recent_activity', [])
        }
        return self.user_context

    def generate_intervention(self, trigger_type):
        """Generate personalized intervention based on trigger and context"""
        if not self.user_context:
            return None

        personality = self.personality_type_configs[self.user_context['personality_type']]
        template = self.intervention_templates[trigger_type]

        # Personalize intervention based on user context
        intervention = {
            'type': trigger_type,
            'timing': self._optimize_timing(),
            'actions': self._personalize_actions(template['actions'], personality),
            'motivation_elements': self._add_motivation_elements(personality),
            'follow_up': self._create_follow_up_plan(template)
        }

        self.intervention_history.append(intervention)
        return intervention

    def track_progress(self, intervention_id, metrics):
        """Track intervention effectiveness"""
        self.success_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion_rate', 0),
            'user_satisfaction': metrics.get('user_satisfaction', 0),
            'behavioral_change': metrics.get('behavioral_change', 0),
            'timestamp': metrics.get('timestamp')
        }
        return self._analyze_effectiveness(intervention_id)

    def _estimate_cognitive_load(self, context_data):
        """Estimate current cognitive load based on context"""
        factors = {
            'task_complexity': context_data.get('task_complexity', 0.5),
            'interruptions': len(context_data.get('recent_interruptions', [])),
            'time_pressure': context_data.get('deadline_proximity', 0.5),
            'task_familiarity': context_data.get('task_familiarity', 0.5)
        }
        return sum(factors.values()) / len(factors)

    def _optimize_timing(self):
        """Optimize intervention timing based on user context"""
        energy_level = self.user_context['energy_level']
        cognitive_load = self.user_context['cognitive_load']
        time_of_day = self.user_context['time_of_day']

        optimal_timing = {
            'delay': max(0, (cognitive_load - 0.7) * 60),  # Delay in minutes
            'frequency': self._calculate_frequency(energy_level),
            'preferred_time': self._get_preferred_time(time_of_day)
        }
        return optimal_timing

    def _personalize_actions(self, actions, personality):
        """Personalize action steps based on personality"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = personality['communication_pref']
            modified_action['complexity'] = self._adjust_complexity(
                personality['learning_style'],
                self.user_context['cognitive_load']
            )
            personalized.append(modified_action)
        return personalized

    def _add_motivation_elements(self, personality):
        """Add personalized motivation elements"""
        return {
            'triggers': personality['motivation_triggers'],
            'reinforcement_type': self._select_reinforcement(personality),
            'framing': self._personalize_framing(personality)
        }

    def _create_follow_up_plan(self, template):
        """Create personalized follow-up plan"""
        return {
            'timing': template['follow_up_window'],
            'check_points': self._generate_checkpoints(template),
            'adaptation_rules': self._create_adaptation_rules()
        }

    def _analyze_effectiveness(self, intervention_id):
        """Analyze intervention effectiveness and suggest improvements"""
        metrics = self.success_metrics[intervention_id]
        return {
            'effectiveness_score': sum(metrics.values()) / len(metrics),
            'improvement_areas': self._identify_improvement_areas(metrics),
            'suggested_adjustments': self._generate_adjustments(metrics)
        }

    def _calculate_frequency(self, energy_level):
        """Calculate optimal intervention frequency"""
        return max(30, min(120, int(100 * (1 - energy_level))))

    def _adjust_complexity(self, learning_style, cognitive_load):
        """Adjust action complexity based on learning style and cognitive load"""
        base_complexity = 0.7 if learning_style == 'systematic' else 0.5
        return base_complexity * (1 - cognitive_load)