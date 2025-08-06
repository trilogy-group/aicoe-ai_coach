class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced learning patterns
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types omitted for brevity
        }

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['context:high_distraction', 'pattern:task_switching'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2min', 'priority': 1},
                    {'step': 'Enable focus mode', 'time_est': '1min', 'priority': 1},
                    {'step': 'Set timer for focused work', 'time_est': '1min', 'priority': 2}
                ],
                'success_metrics': ['Time on task', 'Task completion rate'],
                'follow_up': {'timing': '+30min', 'type': 'check_progress'}
            }
            # Additional templates omitted
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_rewards'],
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_system']
        }

        # Cognitive load management
        self.cognitive_load_thresholds = {
            'max_concurrent_tasks': 3,
            'max_recommendations': 2,
            'recovery_time': 15  # minutes
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        
        # Get personalization parameters
        user_config = self.personality_type_configs[personality_type]
        
        # Analyze current cognitive load
        cognitive_load = self._assess_cognitive_load(user_context)
        
        # Select appropriate intervention
        intervention = self._select_intervention(user_context, cognitive_load)
        
        # Personalize communication style
        message = self._personalize_message(intervention, user_config['communication_pref'])
        
        # Add specific action steps
        action_plan = self._create_action_plan(intervention, user_config['learning_style'])
        
        return {
            'message': message,
            'actions': action_plan,
            'follow_up': intervention['follow_up']
        }

    def _assess_cognitive_load(self, context):
        """Evaluate current cognitive load based on context"""
        load_score = 0
        
        # Assess active tasks
        load_score += len(context.get('active_tasks', []))
        
        # Consider time of day fatigue
        load_score += self._calculate_fatigue_factor(context['time'])
        
        # Account for recent intensive activities
        load_score += len(context.get('recent_activities', []))
        
        return load_score

    def _select_intervention(self, context, cognitive_load):
        """Select most appropriate intervention based on context and load"""
        
        # Filter interventions based on cognitive load
        if cognitive_load > self.cognitive_load_thresholds['max_concurrent_tasks']:
            return self.intervention_templates['recovery']
            
        # Match intervention to context triggers
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context['triggers'] for trigger in template['triggers']):
                return template
                
        return self.intervention_templates['default']

    def _personalize_message(self, intervention, communication_style):
        """Customize intervention message based on communication preferences"""
        
        base_message = intervention.get('message', '')
        
        if communication_style == 'direct':
            return f"Action needed: {base_message}"
        elif communication_style == 'enthusiastic':
            return f"Great opportunity: {base_message}!"
        
        return base_message

    def _create_action_plan(self, intervention, learning_style):
        """Generate specific action steps based on learning style"""
        
        action_plan = []
        
        for action in intervention['actions']:
            step = {
                'description': action['step'],
                'time_estimate': action['time_est'],
                'priority': action['priority']
            }
            
            # Add learning style specific details
            if learning_style == 'systematic':
                step['sub_steps'] = self._break_down_action(action['step'])
            elif learning_style == 'exploratory':
                step['alternatives'] = self._generate_alternatives(action['step'])
                
            action_plan.append(step)
            
        return action_plan

    def _break_down_action(self, action):
        """Break complex actions into smaller steps"""
        # Implementation omitted for brevity
        pass

    def _generate_alternatives(self, action):
        """Generate alternative approaches to accomplish the same goal"""
        # Implementation omitted for brevity
        pass

    def _calculate_fatigue_factor(self, time):
        """Calculate cognitive fatigue based on time of day"""
        # Implementation omitted for brevity
        pass

    def track_intervention_effectiveness(self, intervention_id, user_response):
        """Track and analyze intervention effectiveness"""
        # Implementation omitted for brevity
        pass