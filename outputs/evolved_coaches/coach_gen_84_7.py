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
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Set a 25-minute focus timer', 'time_est': '1 min'},
                    {'step': 'Write your next specific task', 'time_est': '2 min'}
                ],
                'success_metrics': ['focus_duration', 'task_completion'],
                'follow_up_timing': 30 # minutes
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into 15-minute chunks', 'time_est': '5 min'},
                    {'step': 'Set 3 mini-milestones', 'time_est': '3 min'},
                    {'step': 'Schedule reward after completion', 'time_est': '2 min'}
                ],
                'success_metrics': ['task_initiation', 'milestone_completion'],
                'follow_up_timing': 60
            }
            # Additional intervention types
        }

        self.behavioral_principles = {
            'habit_formation': ['trigger', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'attention': ['focus_duration', 'context_switching', 'cognitive_load'],
            'learning': ['spaced_repetition', 'active_recall', 'elaboration']
        }

    def generate_personalized_intervention(self, user_context, personality_type):
        """Generate personalized coaching intervention based on user context and type"""
        
        user_config = self.personality_type_configs[personality_type]
        
        # Calculate cognitive load and attention state
        current_load = self._assess_cognitive_load(user_context)
        attention_capacity = self._calculate_attention_capacity(user_context)
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(
            user_context,
            current_load,
            attention_capacity,
            user_config
        )
        
        # Personalize intervention content
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            user_config['learning_style'],
            user_config['communication_pref']
        )
        
        return {
            'intervention_type': intervention['type'],
            'personalized_actions': personalized_actions,
            'timing': self._optimize_timing(user_context),
            'success_metrics': intervention['success_metrics'],
            'follow_up': intervention['follow_up_timing']
        }

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3),
            'task_familiarity': context.get('familiarity', 0.7)
        }
        
        return sum(factors.values()) / len(factors)

    def _calculate_attention_capacity(self, context):
        """Calculate available attention capacity"""
        baseline = 1.0
        deductions = {
            'fatigue': context.get('fatigue', 0) * 0.2,
            'distractions': context.get('distractions', 0) * 0.15,
            'stress': context.get('stress', 0) * 0.25
        }
        
        return baseline - sum(deductions.values())

    def _select_intervention(self, context, cognitive_load, attention, user_config):
        """Select most appropriate intervention based on context and user state"""
        
        if cognitive_load > user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        elif attention < 0.4:
            return self.intervention_templates['motivation']
        
        # Additional intervention selection logic
        return self._get_default_intervention()

    def _personalize_actions(self, actions, learning_style, comm_pref):
        """Personalize action steps based on user preferences"""
        personalized = []
        
        for action in actions:
            modified_step = self._adapt_to_style(
                action['step'],
                learning_style,
                comm_pref
            )
            personalized.append({
                'step': modified_step,
                'time_est': action['time_est'],
                'completion_check': self._create_completion_check(modified_step)
            })
            
        return personalized

    def _optimize_timing(self, context):
        """Optimize intervention timing based on user context"""
        best_times = {
            'morning': context.get('morning_receptivity', 0.7),
            'afternoon': context.get('afternoon_receptivity', 0.5),
            'evening': context.get('evening_receptivity', 0.3)
        }
        
        return max(best_times, key=best_times.get)

    def _adapt_to_style(self, content, learning_style, comm_pref):
        """Adapt content to user's learning and communication preferences"""
        if learning_style == 'systematic':
            content = f"Step-by-step: {content}"
        elif learning_style == 'exploratory':
            content = f"Try this: {content}"
            
        if comm_pref == 'direct':
            content = content.strip().rstrip('.')
        elif comm_pref == 'enthusiastic':
            content = f"{content}! 🎯"
            
        return content

    def _create_completion_check(self, action):
        """Create verification method for action completion"""
        return {
            'verification_type': 'self_report',
            'completion_criteria': f"Have you completed: {action}?",
            'evidence_required': False
        }

    def _get_default_intervention(self):
        """Return default intervention when no specific match"""
        return self.intervention_templates['focus']