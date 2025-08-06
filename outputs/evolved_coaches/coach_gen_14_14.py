class EvolutionaryAICoach:
    def __init__(self):
        # Personality and learning style configurations
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }

        # Enhanced behavioral psychology frameworks
        self.behavior_frameworks = {
            'motivation': ['autonomy', 'competence', 'relatedness'], # Self-determination theory
            'habit_formation': ['cue', 'routine', 'reward', 'craving'],
            'cognitive_load': ['intrinsic', 'extraneous', 'germane'],
            'attention': ['focused', 'sustained', 'divided', 'selective']
        }

        # Action templates with specific metrics
        self.action_templates = {
            'deep_work': {
                'duration': 25, # minutes
                'success_metrics': ['task_completion', 'focus_quality'],
                'priority': 'high',
                'follow_up': True
            },
            'skill_building': {
                'duration': 45,
                'success_metrics': ['competency_gain', 'practice_consistency'],
                'priority': 'medium', 
                'follow_up': True
            }
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate contextually relevant coaching intervention"""
        user_config = self.personality_type_configs[personality_type]
        
        # Context analysis
        attention_capacity = self._assess_cognitive_load(user_context)
        optimal_timing = self._determine_intervention_timing(user_context)
        current_motivation = self._assess_motivation_state(user_context)

        # Personalization factors
        learning_style = user_config['learning_style']
        comm_style = user_config['communication_pref']
        work_pattern = user_config['work_pattern']

        # Generate specific recommendation
        recommendation = self._create_actionable_recommendation(
            context=user_context,
            attention=attention_capacity,
            motivation=current_motivation,
            learning_style=learning_style,
            work_pattern=work_pattern
        )

        return {
            'nudge': recommendation,
            'timing': optimal_timing,
            'format': comm_style,
            'follow_up': self._schedule_follow_up(recommendation)
        }

    def _assess_cognitive_load(self, context):
        """Evaluate current cognitive capacity"""
        cognitive_factors = {
            'task_complexity': context.get('task_difficulty', 0.5),
            'time_pressure': context.get('deadline_proximity', 0.3),
            'distractions': context.get('environment_distractions', 0.2)
        }
        
        total_load = sum(cognitive_factors.values())
        return 1.0 - min(total_load, 1.0) # Available capacity

    def _determine_intervention_timing(self, context):
        """Calculate optimal intervention timing"""
        energy_level = context.get('energy_level', 0.5)
        task_urgency = context.get('task_urgency', 0.5)
        last_break = context.get('time_since_break', 0)

        if last_break > 90: # minutes
            return 'immediate'
        elif energy_level < 0.3:
            return 'after_break'
        else:
            return 'next_task_boundary'

    def _assess_motivation_state(self, context):
        """Evaluate current motivation using SDT framework"""
        return {
            'autonomy': context.get('control_level', 0.5),
            'competence': context.get('skill_confidence', 0.5),
            'relatedness': context.get('social_support', 0.5)
        }

    def _create_actionable_recommendation(self, context, attention, motivation, learning_style, work_pattern):
        """Generate specific, actionable coaching recommendation"""
        if attention < 0.3:
            return self._generate_focus_intervention(work_pattern)
        elif min(motivation.values()) < 0.4:
            return self._generate_motivation_intervention(motivation)
        else:
            return self._generate_optimization_intervention(learning_style)

    def _generate_focus_intervention(self, work_pattern):
        """Create focus-building recommendation"""
        if work_pattern == 'deep_focus':
            return {
                'action': 'Initialize deep work session',
                'duration': '25 minutes',
                'steps': [
                    'Clear workspace of distractions',
                    'Set clear session goal',
                    'Enable do-not-disturb mode',
                    'Start timer'
                ],
                'success_metric': 'Uninterrupted focus time'
            }
        else:
            return {
                'action': 'Progressive focus building',
                'duration': '15 minutes',
                'steps': [
                    'Complete one small task',
                    'Take 2-minute break',
                    'Increment focus period'
                ],
                'success_metric': 'Task completion rate'
            }

    def _generate_motivation_intervention(self, motivation_state):
        """Create motivation-enhancing recommendation"""
        weakest_factor = min(motivation_state.items(), key=lambda x: x[1])[0]
        
        interventions = {
            'autonomy': {
                'action': 'Enhance work ownership',
                'steps': [
                    'Choose next task focus',
                    'Set personal work rhythm',
                    'Define success criteria'
                ]
            },
            'competence': {
                'action': 'Build skill confidence',
                'steps': [
                    'Break down complex task',
                    'Review past successes',
                    'Set learning milestone'
                ]
            },
            'relatedness': {
                'action': 'Increase collaboration',
                'steps': [
                    'Share progress with team',
                    'Seek peer feedback',
                    'Offer help to others'
                ]
            }
        }
        
        return interventions[weakest_factor]

    def _generate_optimization_intervention(self, learning_style):
        """Create performance-optimizing recommendation"""
        return {
            'action': 'Enhance current workflow',
            'duration': '30 minutes',
            'steps': [
                'Review productivity patterns',
                'Identify improvement area',
                'Test new approach',
                'Measure results'
            ],
            'success_metric': 'Efficiency gain'
        }

    def _schedule_follow_up(self, recommendation):
        """Create follow-up schedule for recommendation"""
        return {
            'timing': 'end_of_session',
            'metrics': recommendation['success_metric'],
            'adjustment_triggers': ['low_completion', 'high_difficulty']
        }