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
                'motivation_triggers': ['novelty', 'connection', 'creativity'],
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
                    {'type': 'technique', 'duration': 45, 'specifics': 'Use Pomodoro method with 25min focused work'},
                    {'type': 'break', 'duration': 5, 'specifics': 'Take short mindful break'}
                ],
                'follow_up': {'timing': 60, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'goal_setting', 'duration': 10, 'specifics': 'Break task into 3 smaller achievable steps'},
                    {'type': 'reward', 'duration': 5, 'specifics': 'Define concrete reward for completion'},
                    {'type': 'accountability', 'duration': 15, 'specifics': 'Share goal with accountability partner'}
                ],
                'follow_up': {'timing': 120, 'type': 'motivation_check'}
            }
            # Additional templates...
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['progress', 'feedback', 'social_proof']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': {'morning': 1.2, 'afternoon': 1.0, 'evening': 0.8},
            'energy_level': {'high': 1.2, 'medium': 1.0, 'low': 0.8},
            'task_complexity': {'high': 0.8, 'medium': 1.0, 'low': 1.2}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized intervention based on user context and type"""
        config = self.personality_type_configs[personality_type]
        
        # Calculate optimal intervention timing
        timing_score = self._calculate_timing_score(user_context)
        if timing_score < 0.7:
            return None  # Skip if timing isn't optimal

        # Select appropriate intervention template
        template = self._select_intervention_template(user_context, config)
        
        # Personalize actions based on user preferences
        actions = self._personalize_actions(template['actions'], config)
        
        # Apply behavioral psychology principles
        enhanced_actions = self._apply_behavioral_principles(actions, config)
        
        return {
            'timing': timing_score,
            'actions': enhanced_actions,
            'follow_up': template['follow_up'],
            'motivation_hooks': self._generate_motivation_hooks(config)
        }

    def _calculate_timing_score(self, context):
        """Calculate optimal intervention timing score"""
        base_score = 1.0
        
        # Apply context modifiers
        for factor, value in context.items():
            if factor in self.context_factors:
                base_score *= self.context_factors[factor].get(value, 1.0)
                
        return min(max(base_score, 0.0), 1.0)

    def _select_intervention_template(self, context, config):
        """Select most appropriate intervention template"""
        best_template = None
        best_score = 0
        
        for template_name, template in self.intervention_templates.items():
            score = self._calculate_template_match(template, context, config)
            if score > best_score:
                best_score = score
                best_template = template
                
        return best_template

    def _personalize_actions(self, actions, config):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['style'] = config['communication_pref']
            modified_action['pacing'] = config['work_pattern']
            personalized.append(modified_action)
        return personalized

    def _apply_behavioral_principles(self, actions, config):
        """Apply behavioral psychology principles to actions"""
        enhanced = []
        for action in actions:
            enhanced_action = action.copy()
            enhanced_action['triggers'] = self._select_behavior_triggers(config)
            enhanced_action['reinforcement'] = self._generate_reinforcement_strategy(config)
            enhanced.append(enhanced_action)
        return enhanced

    def _generate_motivation_hooks(self, config):
        """Generate personalized motivation hooks"""
        return {
            'primary': config['motivation_triggers'][0],
            'secondary': config['motivation_triggers'][1:],
            'reinforcement_interval': self._calculate_reinforcement_interval(config)
        }

    def _calculate_reinforcement_interval(self, config):
        """Calculate optimal reinforcement interval"""
        base_interval = 30  # minutes
        return base_interval * (1 / config['cognitive_load_threshold'])

    def _select_behavior_triggers(self, config):
        """Select appropriate behavioral triggers"""
        triggers = []
        for category, options in self.behavior_triggers.items():
            triggers.append(options[0])  # Select primary trigger from each category
        return triggers

    def _generate_reinforcement_strategy(self, config):
        """Generate personalized reinforcement strategy"""
        return {
            'type': 'progressive',
            'interval': self._calculate_reinforcement_interval(config),
            'intensity': config['cognitive_load_threshold'],
            'variety': len(config['motivation_triggers'])
        }