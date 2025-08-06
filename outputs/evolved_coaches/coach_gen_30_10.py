class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning patterns
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
                'motivation_triggers': ['novelty', 'social', 'creativity'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'type': 'environment', 'duration': 15, 'priority': 1,
                     'steps': ['Clear workspace', 'Enable do-not-disturb', 'Set timer']},
                    {'type': 'cognitive', 'duration': 5, 'priority': 2, 
                     'steps': ['Deep breathing', 'Intent setting', 'Task preview']}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'type': 'reframe', 'duration': 10, 'priority': 1,
                     'steps': ['Identify barriers', 'Break down task', 'Set micro-goal']},
                    {'type': 'energize', 'duration': 5, 'priority': 2,
                     'steps': ['Physical movement', 'Success visualization', 'Reward planning']}
                ],
                'follow_up': {'timing': 15, 'type': 'encouragement'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['cue', 'routine', 'reward'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'engagement': ['novelty', 'challenge', 'feedback']
        }

        # Context awareness parameters
        self.context_factors = {
            'time_of_day': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_activity': None
        }

        # Performance tracking
        self.metrics = {
            'intervention_success': [],
            'user_satisfaction': [],
            'behavior_change': [],
            'engagement_level': []
        }

    def generate_personalized_nudge(self, user_profile, context):
        """Generate personalized intervention based on user profile and context"""
        
        # Update context awareness
        self.context_factors.update(context)
        
        # Select appropriate intervention template
        template = self._select_intervention_template(user_profile, context)
        
        # Personalize based on personality type
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Apply behavioral psychology principles
        behavioral_elements = self._apply_behavioral_principles(
            personality_config['motivation_triggers'],
            context['current_state']
        )
        
        # Generate specific action steps
        action_steps = self._generate_action_steps(
            template,
            personality_config,
            context['cognitive_load']
        )
        
        return {
            'intervention_type': template['type'],
            'actions': action_steps,
            'behavioral_elements': behavioral_elements,
            'follow_up': template['follow_up']
        }

    def _select_intervention_template(self, user_profile, context):
        """Select most appropriate intervention template based on context"""
        
        # Calculate intervention scores based on context match
        scores = {}
        for template_name, template in self.intervention_templates.items():
            score = self._calculate_template_match(
                template,
                context,
                user_profile
            )
            scores[template_name] = score
            
        # Return best matching template
        return self.intervention_templates[max(scores, key=scores.get)]

    def _apply_behavioral_principles(self, motivation_triggers, current_state):
        """Apply behavioral psychology principles to intervention"""
        
        behavioral_elements = []
        
        # Add relevant behavioral triggers
        for trigger in motivation_triggers:
            if trigger in self.behavior_triggers:
                behavioral_elements.extend(self.behavior_triggers[trigger])
                
        # Customize based on current state
        behavioral_elements = self._customize_behavioral_elements(
            behavioral_elements,
            current_state
        )
        
        return behavioral_elements

    def _generate_action_steps(self, template, personality_config, cognitive_load):
        """Generate specific, actionable steps based on template"""
        
        action_steps = []
        
        # Filter and prioritize actions based on cognitive load
        available_actions = [
            action for action in template['actions']
            if action['type'] in personality_config['learning_style']
            and cognitive_load <= personality_config['cognitive_load_threshold']
        ]
        
        # Generate specific steps for each action
        for action in available_actions:
            steps = self._customize_action_steps(
                action['steps'],
                personality_config
            )
            action_steps.append({
                'type': action['type'],
                'duration': action['duration'],
                'priority': action['priority'],
                'steps': steps
            })
            
        return action_steps

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Track effectiveness of interventions"""
        
        # Update performance metrics
        for metric_name, value in metrics.items():
            if metric_name in self.metrics:
                self.metrics[metric_name].append(value)
        
        # Analyze patterns and adjust future interventions
        self._adjust_intervention_patterns(intervention_id, metrics)

    def _adjust_intervention_patterns(self, intervention_id, metrics):
        """Adjust intervention patterns based on effectiveness"""
        
        # Calculate success metrics
        success_rate = sum(metrics['intervention_success']) / len(metrics['intervention_success'])
        
        # Adjust templates and behavioral triggers based on performance
        if success_rate < 0.7:
            self._optimize_templates(intervention_id)
            self._update_behavioral_triggers(metrics)