class EvolutionaryAICoach:
    def __init__(self):
        # Enhanced personality configurations with more nuanced traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'stress_responses': ['analysis', 'withdrawal', 'planning'],
                'energy_management': ['focused_sprints', 'reflection_periods']
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['creativity', 'connection', 'growth'],
                'stress_responses': ['distraction', 'socializing', 'reframing'],
                'energy_management': ['variety', 'social_breaks']
            }
            # Additional types...
        }

        # Evidence-based intervention strategies
        self.intervention_strategies = {
            'habit_formation': {
                'cue_identification': True,
                'routine_design': True,
                'reward_scheduling': True,
                'progress_tracking': True
            },
            'motivation': {
                'goal_setting': True,
                'implementation_intentions': True,
                'accountability': True,
                'positive_reinforcement': True
            },
            'stress_management': {
                'cognitive_reframing': True,
                'mindfulness': True,
                'time_boxing': True,
                'boundary_setting': True
            }
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'stress_level': None,
            'task_complexity': None,
            'environmental_conditions': None,
            'social_context': None
        }

        # Behavioral psychology components
        self.behavioral_tools = {
            'reinforcement_schedules': ['fixed', 'variable', 'ratio', 'interval'],
            'commitment_devices': ['public', 'stakes', 'accountability_partners'],
            'social_proof': ['peer_comparisons', 'success_stories', 'community'],
            'loss_aversion': ['streak_maintenance', 'progress_protection']
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate highly personalized coaching intervention"""
        personality_type = user_profile['personality_type']
        config = self.personality_type_configs[personality_type]
        
        # Update context awareness
        self.context_factors.update(context)
        
        # Select optimal intervention timing
        if not self._is_appropriate_timing():
            return None
            
        # Build intervention based on user state
        intervention = self._build_targeted_intervention(
            user_profile,
            config,
            self.context_factors
        )
        
        return self._format_actionable_nudge(intervention)

    def _is_appropriate_timing(self):
        """Determine if intervention timing is optimal"""
        energy_threshold = 0.6
        stress_threshold = 0.8
        
        return (self.context_factors['energy_level'] > energy_threshold and
                self.context_factors['stress_level'] < stress_threshold)

    def _build_targeted_intervention(self, user_profile, config, context):
        """Build personalized intervention strategy"""
        intervention = {
            'type': self._select_intervention_type(config, context),
            'content': self._generate_content(user_profile, config),
            'delivery_style': config['communication_pref'],
            'intensity': self._calculate_intensity(context),
            'action_steps': self._generate_action_steps(config),
            'follow_up': self._plan_follow_up(config)
        }
        
        return intervention

    def _select_intervention_type(self, config, context):
        """Select most appropriate intervention type"""
        if context['stress_level'] > 0.7:
            return 'stress_management'
        elif context['task_complexity'] > 0.8:
            return 'habit_formation'
        else:
            return 'motivation'

    def _generate_content(self, user_profile, config):
        """Generate personalized content"""
        content = {
            'primary_message': self._craft_message(config),
            'supporting_evidence': self._get_relevant_research(),
            'personalized_examples': self._generate_examples(user_profile),
            'motivation_hooks': self._select_motivation_drivers(config)
        }
        return content

    def _calculate_intensity(self, context):
        """Calculate appropriate intervention intensity"""
        base_intensity = 0.5
        modifiers = {
            'energy_level': 0.2,
            'stress_level': -0.3,
            'task_complexity': 0.1
        }
        
        intensity = base_intensity
        for factor, modifier in modifiers.items():
            intensity += context[factor] * modifier
            
        return max(0.1, min(1.0, intensity))

    def _generate_action_steps(self, config):
        """Generate specific actionable steps"""
        return [
            {
                'step': 'immediate_action',
                'timeframe': '5 minutes',
                'difficulty': 'easy',
                'expected_outcome': 'momentum'
            },
            {
                'step': 'short_term_goal',
                'timeframe': '1 hour',
                'difficulty': 'moderate',
                'expected_outcome': 'progress'
            },
            {
                'step': 'daily_target',
                'timeframe': 'today',
                'difficulty': 'challenging',
                'expected_outcome': 'achievement'
            }
        ]

    def _plan_follow_up(self, config):
        """Plan follow-up engagement"""
        return {
            'timing': self._calculate_follow_up_timing(config),
            'type': self._select_follow_up_type(config),
            'measurement': self._define_success_metrics()
        }

    def _format_actionable_nudge(self, intervention):
        """Format intervention as actionable nudge"""
        return {
            'message': intervention['content']['primary_message'],
            'action_steps': intervention['action_steps'],
            'timing': intervention['type'],
            'style': intervention['delivery_style'],
            'intensity': intervention['intensity'],
            'follow_up': intervention['follow_up']
        }