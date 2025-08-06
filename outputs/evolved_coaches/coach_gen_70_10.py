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
                    {'type': 'environment', 'duration': 25, 'specifics': 'Clear workspace, close unnecessary tabs'},
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min work blocks'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a brief walk, stretch exercises'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 achievable sub-goals'},
                    {'type': 'reward', 'duration': 30, 'specifics': 'Define concrete reward for completion'},
                    {'type': 'accountability', 'duration': 5, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 120, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['challenge', 'feedback', 'progress']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': ['morning', 'afternoon', 'evening'],
            'energy_level': ['high', 'medium', 'low'],
            'task_complexity': ['simple', 'moderate', 'complex'],
            'environment': ['office', 'home', 'mobile']
        }

    def generate_personalized_intervention(self, user_profile, context):
        """Generate personalized coaching intervention based on user profile and context"""
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Context-aware intervention selection
        suitable_interventions = self._filter_interventions_by_context(context)
        selected_intervention = self._select_optimal_intervention(
            suitable_interventions,
            personality_config,
            context
        )

        # Enhance intervention with behavioral psychology
        enhanced_intervention = self._apply_behavioral_principles(
            selected_intervention,
            personality_config['motivation_triggers']
        )

        return self._format_intervention(enhanced_intervention, personality_config)

    def _filter_interventions_by_context(self, context):
        """Filter suitable interventions based on current context"""
        suitable = []
        for intervention in self.intervention_templates.values():
            if self._is_contextually_appropriate(intervention, context):
                suitable.append(intervention)
        return suitable

    def _is_contextually_appropriate(self, intervention, context):
        """Check if intervention is appropriate for current context"""
        return (
            context['time_of_day'] in self.context_factors['time_of_day'] and
            context['energy_level'] >= intervention.get('min_energy_required', 0) and
            context['task_complexity'] in self.context_factors['task_complexity']
        )

    def _select_optimal_intervention(self, interventions, personality_config, context):
        """Select the most effective intervention based on user profile and context"""
        scored_interventions = []
        for intervention in interventions:
            score = self._calculate_intervention_score(
                intervention,
                personality_config,
                context
            )
            scored_interventions.append((score, intervention))
        return max(scored_interventions, key=lambda x: x[0])[1]

    def _calculate_intervention_score(self, intervention, personality_config, context):
        """Calculate effectiveness score for an intervention"""
        score = 0
        score += self._match_learning_style(intervention, personality_config['learning_style'])
        score += self._match_communication_style(intervention, personality_config['communication_pref'])
        score += self._assess_cognitive_load(intervention, personality_config['cognitive_load_threshold'])
        return score

    def _apply_behavioral_principles(self, intervention, motivation_triggers):
        """Enhance intervention with behavioral psychology principles"""
        enhanced = intervention.copy()
        enhanced['behavioral_components'] = {
            'motivation_alignment': self._align_with_motivation(intervention, motivation_triggers),
            'habit_formation': self._add_habit_formation_elements(intervention),
            'engagement_hooks': self._add_engagement_elements(intervention)
        }
        return enhanced

    def _format_intervention(self, intervention, personality_config):
        """Format intervention according to user's communication preferences"""
        return {
            'title': self._generate_title(intervention, personality_config),
            'actions': self._format_actions(intervention['actions'], personality_config),
            'follow_up': intervention['follow_up'],
            'expected_outcomes': self._generate_outcomes(intervention),
            'success_metrics': self._define_metrics(intervention)
        }

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation for tracking and analyzing intervention results
        pass

    def update_intervention_models(self, effectiveness_data):
        """Update intervention models based on effectiveness data"""
        # Implementation for updating intervention models
        pass