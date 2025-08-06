class EnhancedAICoach:
    def __init__(self):
        # Personality configurations from Parent 2
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types...
        }
        
        # Enhanced intervention configurations
        self.intervention_types = {
            'quick_win': {
                'duration': '5-15min',
                'cognitive_load': 'low',
                'motivation_triggers': ['autonomy', 'mastery'],
                'follow_up_window': 24 # hours
            },
            'habit_formation': {
                'duration': '21-days',
                'cognitive_load': 'medium',
                'motivation_triggers': ['consistency', 'progress'],
                'follow_up_window': 48
            },
            'deep_change': {
                'duration': '90-days',
                'cognitive_load': 'high', 
                'motivation_triggers': ['purpose', 'identity'],
                'follow_up_window': 72
            }
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'cue': ['environmental', 'temporal', 'emotional', 'social'],
            'routine': ['existing', 'desired', 'alternative'],
            'reward': ['intrinsic', 'extrinsic', 'social']
        }

        self.user_context = {}
        self.intervention_history = []
        self.success_metrics = {}

    def analyze_user_context(self, user_data):
        """Analyzes user context and preferences"""
        self.user_context = {
            'personality_type': user_data.get('personality_type'),
            'learning_style': self.personality_type_configs[user_data.get('personality_type')]['learning_style'],
            'peak_energy_times': user_data.get('peak_times'),
            'current_goals': user_data.get('goals'),
            'progress_metrics': user_data.get('metrics'),
            'constraints': user_data.get('constraints')
        }
        return self.user_context

    def generate_personalized_nudge(self, context, goal):
        """Generates personalized behavioral nudges"""
        personality_config = self.personality_type_configs[self.user_context['personality_type']]
        
        nudge = {
            'content': self._create_nudge_content(context, goal, personality_config),
            'timing': self._optimize_timing(context),
            'format': personality_config['communication_pref'],
            'action_steps': self._generate_action_steps(goal),
            'success_metrics': self._define_success_metrics(goal),
            'follow_up': self._schedule_follow_up(goal)
        }
        
        return nudge

    def _create_nudge_content(self, context, goal, personality_config):
        """Creates personalized nudge content"""
        content = {
            'message': self._craft_message(goal, personality_config),
            'motivation_triggers': self._select_motivation_triggers(personality_config),
            'cognitive_load': self._assess_cognitive_load(context),
            'specificity_level': self._determine_specificity(goal)
        }
        return content

    def _generate_action_steps(self, goal):
        """Generates specific, actionable steps"""
        return {
            'immediate': self._create_quick_wins(goal),
            'short_term': self._create_habit_steps(goal),
            'long_term': self._create_sustained_change(goal),
            'alternatives': self._generate_alternatives(goal),
            'difficulty_level': self._assess_difficulty(goal)
        }

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Tracks and analyzes intervention effectiveness"""
        self.success_metrics[intervention_id] = {
            'completion_rate': metrics.get('completion'),
            'satisfaction': metrics.get('satisfaction'),
            'behavior_change': metrics.get('behavior_change'),
            'retention': metrics.get('retention')
        }
        return self._analyze_effectiveness(intervention_id)

    def adapt_recommendations(self, user_feedback):
        """Adapts recommendations based on feedback"""
        updated_recommendations = {
            'content': self._adjust_content_style(user_feedback),
            'timing': self._optimize_timing_pattern(user_feedback),
            'difficulty': self._adjust_difficulty(user_feedback),
            'format': self._adjust_format(user_feedback)
        }
        return updated_recommendations

    def generate_progress_report(self, user_id):
        """Generates detailed progress reports"""
        return {
            'interventions': self.intervention_history,
            'success_metrics': self.success_metrics,
            'behavior_changes': self._analyze_behavior_changes(),
            'recommendations': self._generate_next_steps()
        }

    def _optimize_timing(self, context):
        """Optimizes intervention timing"""
        return {
            'best_time': self._calculate_optimal_time(context),
            'frequency': self._determine_frequency(context),
            'spacing': self._calculate_spacing(context)
        }

    def _schedule_follow_up(self, goal):
        """Schedules appropriate follow-up"""
        intervention_type = self._determine_intervention_type(goal)
        return {
            'timing': self.intervention_types[intervention_type]['follow_up_window'],
            'type': self._determine_follow_up_type(goal),
            'metrics': self._define_follow_up_metrics(goal)
        }

    def _analyze_effectiveness(self, intervention_id):
        """Analyzes intervention effectiveness"""
        metrics = self.success_metrics[intervention_id]
        return {
            'effectiveness_score': self._calculate_effectiveness(metrics),
            'areas_for_improvement': self._identify_improvement_areas(metrics),
            'recommended_adjustments': self._generate_adjustments(metrics)
        }

    def _calculate_effectiveness(self, metrics):
        """Calculates overall effectiveness score"""
        weights = {'completion_rate': 0.3, 'satisfaction': 0.2, 
                  'behavior_change': 0.3, 'retention': 0.2}
        
        score = sum(metrics[key] * weights[key] for key in weights)
        return score