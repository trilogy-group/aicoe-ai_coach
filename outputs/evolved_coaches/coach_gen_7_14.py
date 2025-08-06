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

        self.behavioral_triggers = {
            'time_patterns': [],
            'activity_sequences': [],
            'cognitive_load': 0.0,
            'motivation_level': 0.0,
            'distraction_indicators': []
        }

    def analyze_user_context(self, user_data):
        """Analyzes user context to determine optimal intervention timing"""
        context = {
            'cognitive_load': self._calculate_cognitive_load(user_data),
            'attention_state': self._assess_attention_state(user_data),
            'motivation_level': self._gauge_motivation(user_data),
            'task_complexity': self._evaluate_task_complexity(user_data),
            'time_of_day_factor': self._analyze_circadian_patterns(user_data)
        }
        return context

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generates highly personalized intervention based on context"""
        config = self.personality_type_configs[personality_type]
        
        # Select optimal intervention type
        intervention = self._select_intervention(user_context, config)
        
        # Personalize action steps
        actions = self._personalize_actions(
            intervention['actions'],
            config['learning_style'],
            user_context['cognitive_load']
        )

        # Add motivation elements based on personality
        motivation_elements = self._add_motivation_triggers(
            config['motivation_triggers'],
            user_context['motivation_level']
        )

        return {
            'message': self._format_message(actions, config['communication_pref']),
            'actions': actions,
            'motivation_elements': motivation_elements,
            'follow_up': intervention['follow_up_timing'],
            'success_metrics': intervention['success_metrics']
        }

    def track_intervention_effectiveness(self, nudge, user_response):
        """Tracks and analyzes intervention effectiveness"""
        metrics = {
            'completion_rate': self._calculate_completion(user_response),
            'engagement_level': self._measure_engagement(user_response),
            'behavior_change': self._assess_behavior_change(user_response),
            'user_satisfaction': self._analyze_satisfaction(user_response)
        }
        
        self._update_intervention_models(metrics)
        return metrics

    def _calculate_cognitive_load(self, user_data):
        """Estimates current cognitive load based on activity patterns"""
        factors = {
            'active_tasks': len(user_data.get('active_tasks', [])) * 0.2,
            'context_switches': user_data.get('context_switches', 0) * 0.1,
            'complexity': user_data.get('task_complexity', 0.5)
        }
        return min(sum(factors.values()), 1.0)

    def _personalize_actions(self, actions, learning_style, cognitive_load):
        """Adapts action steps based on learning style and cognitive load"""
        if cognitive_load > 0.7:
            # Simplify steps for high cognitive load
            actions = [a for a in actions if a['time_est'].split()[0] <= '5']
            
        if learning_style == 'systematic':
            # Add more detailed substeps
            for action in actions:
                action['substeps'] = self._generate_substeps(action['step'])
                
        return actions

    def _add_motivation_triggers(self, triggers, current_motivation):
        """Adds personalized motivation elements based on user triggers"""
        motivation_elements = []
        if current_motivation < 0.5:
            for trigger in triggers:
                motivation_elements.append(
                    self._generate_motivation_element(trigger)
                )
        return motivation_elements

    def _format_message(self, actions, communication_style):
        """Formats intervention message based on communication preferences"""
        if communication_style == 'direct':
            return self._create_direct_message(actions)
        elif communication_style == 'enthusiastic':
            return self._create_enthusiastic_message(actions)
        return self._create_balanced_message(actions)

    def _select_intervention(self, context, config):
        """Selects most appropriate intervention based on context"""
        best_intervention = None
        max_score = -1
        
        for intervention in self.intervention_templates.values():
            score = self._calculate_intervention_fit(
                intervention, context, config
            )
            if score > max_score:
                max_score = score
                best_intervention = intervention
                
        return best_intervention

    def adapt_to_feedback(self, feedback_data):
        """Adapts intervention strategies based on effectiveness data"""
        for metric, value in feedback_data.items():
            if value < 0.6:  # Below threshold
                self._optimize_intervention_parameter(metric)