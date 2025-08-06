class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral factors
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy', 'achievement'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['novelty', 'connection', 'creativity'],
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
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min focus blocks'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take a short walk, stretch exercises'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 achievable sub-goals'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define concrete reward for completion'},
                    {'type': 'accountability', 'duration': 15, 'specifics': 'Share goals with accountability partner'}
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

    def generate_personalized_intervention(self, user_profile, context, performance_data):
        # Get personality-specific configurations
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Analyze context and cognitive load
        current_load = self._assess_cognitive_load(context, performance_data)
        optimal_timing = self._calculate_intervention_timing(context, current_load)
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(
            personality_config,
            context,
            current_load,
            performance_data
        )
        
        # Personalize action steps
        personalized_actions = self._personalize_actions(
            intervention['actions'],
            personality_config,
            context
        )
        
        return {
            'timing': optimal_timing,
            'actions': personalized_actions,
            'follow_up': intervention['follow_up'],
            'motivation_hooks': self._generate_motivation_hooks(user_profile)
        }

    def _assess_cognitive_load(self, context, performance_data):
        # Calculate current cognitive load based on multiple factors
        base_load = performance_data.get('task_complexity', 0.5)
        context_load = self._calculate_context_load(context)
        fatigue_factor = self._calculate_fatigue(context['time_active'])
        
        return min(1.0, base_load + context_load + fatigue_factor)

    def _calculate_intervention_timing(self, context, cognitive_load):
        # Determine optimal intervention timing
        base_delay = 30 # minutes
        if cognitive_load > 0.8:
            base_delay *= 0.5
        elif cognitive_load < 0.3:
            base_delay *= 1.5
            
        return self._adjust_timing_for_context(base_delay, context)

    def _select_intervention(self, personality_config, context, cognitive_load, performance_data):
        # Choose most appropriate intervention template
        if cognitive_load > personality_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
        elif performance_data.get('motivation_score', 0.5) < 0.6:
            return self.intervention_templates['motivation']
        
        return self._get_default_intervention(personality_config)

    def _personalize_actions(self, actions, personality_config, context):
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['duration'] = self._adjust_duration(
                action['duration'],
                personality_config['work_pattern']
            )
            modified_action['specifics'] = self._customize_specifics(
                action['specifics'],
                personality_config['communication_pref']
            )
            personalized.append(modified_action)
        return personalized

    def _generate_motivation_hooks(self, user_profile):
        # Generate personalized motivation triggers
        personality_drivers = self.personality_type_configs[user_profile['personality_type']]['motivation_drivers']
        
        hooks = []
        for driver in personality_drivers:
            hooks.extend(self._create_motivation_prompts(driver))
        
        return hooks

    def _create_motivation_prompts(self, motivation_type):
        # Create specific motivation prompts based on type
        prompts = {
            'mastery': ['Track your progress', 'Learn something new', 'Challenge yourself'],
            'autonomy': ['Choose your approach', 'Set your own pace', 'Define your path'],
            'purpose': ['Connect to your goals', 'Make an impact', 'Help others succeed']
        }
        return prompts.get(motivation_type, [])

    def update_effectiveness(self, intervention_results):
        # Update intervention effectiveness based on results
        for template in self.intervention_templates:
            if template in intervention_results:
                self._adjust_template_parameters(template, intervention_results[template])

    def _adjust_template_parameters(self, template, results):
        # Adjust intervention parameters based on effectiveness
        if results['success_rate'] < 0.5:
            self.intervention_templates[template]['actions'] = self._simplify_actions(
                self.intervention_templates[template]['actions']
            )
        elif results['success_rate'] > 0.8:
            self.intervention_templates[template]['actions'] = self._increase_challenge(
                self.intervention_templates[template]['actions']
            )