class EnhancedAICoach:
    def __init__(self):
        self.user_profile = {}
        self.intervention_history = []
        self.behavior_metrics = {}
        self.success_metrics = {
            'nudge_quality': 0,
            'behavioral_change': 0, 
            'user_satisfaction': 0,
            'relevance': 0,
            'actionability': 0
        }
        
        # Enhanced psychological frameworks
        self.behavioral_models = {
            'motivation': ['autonomy', 'competence', 'relatedness'],
            'stages_of_change': ['precontemplation', 'contemplation', 'preparation', 'action', 'maintenance'],
            'cognitive_load': ['intrinsic', 'extraneous', 'germane']
        }
        
        # Expanded intervention types
        self.intervention_types = {
            'micro_nudge': {'duration': '1-2 min', 'cognitive_load': 'low'},
            'mini_session': {'duration': '5-10 min', 'cognitive_load': 'medium'},
            'deep_dive': {'duration': '15-30 min', 'cognitive_load': 'high'}
        }

    def analyze_user_context(self, user_data):
        """Enhanced context analysis incorporating multiple data points"""
        context = {
            'attention_level': self._assess_attention(user_data),
            'cognitive_capacity': self._assess_cognitive_load(user_data),
            'motivation_state': self._assess_motivation(user_data),
            'readiness_stage': self._assess_stage_of_change(user_data),
            'environmental_factors': self._assess_environment(user_data)
        }
        return context

    def generate_personalized_intervention(self, user_context):
        """Creates highly personalized coaching interventions"""
        intervention = {
            'type': self._select_intervention_type(user_context),
            'content': self._generate_content(user_context),
            'timing': self._optimize_timing(user_context),
            'delivery_method': self._select_delivery_method(user_context),
            'action_steps': self._create_action_steps(user_context),
            'success_metrics': self._define_success_metrics()
        }
        return intervention

    def _assess_attention(self, user_data):
        """Evaluates current attention capacity"""
        factors = ['time_of_day', 'recent_activity', 'device_usage']
        attention_score = sum(user_data.get(f, 0) for f in factors) / len(factors)
        return attention_score

    def _assess_cognitive_load(self, user_data):
        """Analyzes current cognitive load"""
        load_factors = {
            'task_complexity': 0.4,
            'environmental_distractions': 0.3,
            'fatigue_level': 0.3
        }
        return sum(load_factors[k] * user_data.get(k, 0) for k in load_factors)

    def _assess_motivation(self, user_data):
        """Evaluates motivation using Self-Determination Theory"""
        motivation_factors = {
            'autonomy': self._calculate_autonomy(user_data),
            'competence': self._calculate_competence(user_data),
            'relatedness': self._calculate_relatedness(user_data)
        }
        return motivation_factors

    def _create_action_steps(self, context):
        """Generates specific, actionable steps"""
        return {
            'immediate': self._generate_immediate_actions(context),
            'short_term': self._generate_short_term_actions(context),
            'long_term': self._generate_long_term_actions(context)
        }

    def track_progress(self, user_id, metrics):
        """Enhanced progress tracking"""
        self.behavior_metrics[user_id] = {
            'behavioral_changes': metrics.get('changes', []),
            'engagement_level': metrics.get('engagement', 0),
            'completion_rate': metrics.get('completion', 0),
            'satisfaction_score': metrics.get('satisfaction', 0)
        }
        return self._calculate_progress_score(user_id)

    def adapt_strategy(self, user_id):
        """Adapts coaching strategy based on progress"""
        progress = self.behavior_metrics.get(user_id, {})
        
        if progress.get('engagement_level', 0) < 0.5:
            return self._increase_engagement_tactics()
        elif progress.get('completion_rate', 0) < 0.7:
            return self._enhance_actionability()
        else:
            return self._maintain_momentum()

    def _increase_engagement_tactics(self):
        """Implements enhanced engagement strategies"""
        return {
            'shorter_interventions': True,
            'increased_feedback': True,
            'gamification_elements': True,
            'social_proof': True
        }

    def _enhance_actionability(self):
        """Improves action step clarity and achievability"""
        return {
            'step_breakdown': True,
            'difficulty_adjustment': True,
            'concrete_examples': True,
            'progress_markers': True
        }

    def _maintain_momentum(self):
        """Strategies to maintain positive behavior change"""
        return {
            'positive_reinforcement': True,
            'challenge_progression': True,
            'habit_integration': True,
            'success_celebration': True
        }

    def evaluate_effectiveness(self):
        """Measures overall coaching effectiveness"""
        metrics = {
            'engagement_rate': self._calculate_engagement(),
            'behavior_change': self._calculate_behavior_change(),
            'user_satisfaction': self._calculate_satisfaction(),
            'intervention_relevance': self._calculate_relevance(),
            'action_completion': self._calculate_completion()
        }
        return metrics

    def update_success_metrics(self, metrics):
        """Updates system success metrics"""
        for key in self.success_metrics:
            if key in metrics:
                self.success_metrics[key] = (
                    self.success_metrics[key] * 0.7 + metrics[key] * 0.3
                )
        return self.success_metrics