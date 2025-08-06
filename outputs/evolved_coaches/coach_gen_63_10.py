class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 
                    'work_pattern': 'deep_focus', 'motivation_triggers': ['mastery', 'autonomy']},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic',
                    'work_pattern': 'flexible', 'motivation_triggers': ['novelty', 'social']},
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'context_switch'],
                'actions': [
                    {'type': 'time_block', 'duration': 25, 'success_metric': 'completion_rate'},
                    {'type': 'environment_optimization', 'duration': 5, 'success_metric': 'distraction_reduction'}
                ],
                'follow_up': {'timing': 30, 'type': 'progress_check'}
            },
            'productivity': {
                'triggers': ['procrastination', 'overwhelm'],
                'actions': [
                    {'type': 'task_breakdown', 'size': 'micro', 'success_metric': 'tasks_completed'},
                    {'type': 'priority_matrix', 'duration': 10, 'success_metric': 'decision_quality'}
                ],
                'follow_up': {'timing': 60, 'type': 'achievement_review'}
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'habit_formation': ['cue', 'routine', 'reward'],
            'cognitive_load': ['high', 'medium', 'low']
        }

        # User context tracking
        self.user_context = {
            'attention_span': None,
            'energy_level': None,
            'task_complexity': None,
            'environment': None,
            'recent_interventions': []
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate highly personalized coaching intervention"""
        
        # Update user context
        self.update_user_context(current_context)
        
        # Select optimal intervention timing
        if not self.is_optimal_timing():
            return None

        # Get personality-specific configuration
        personality_config = self.personality_type_configs.get(user_profile['personality_type'])
        
        # Determine intervention type based on context
        intervention_type = self.determine_intervention_type(current_context)
        
        # Generate specific action steps
        action_steps = self.generate_action_steps(
            intervention_type,
            personality_config,
            current_context
        )

        # Apply behavioral psychology principles
        enhanced_steps = self.apply_behavioral_principles(action_steps)

        return {
            'type': intervention_type,
            'actions': enhanced_steps,
            'timing': self.calculate_optimal_timing(),
            'success_metrics': self.define_success_metrics(intervention_type),
            'follow_up': self.create_follow_up_plan()
        }

    def update_user_context(self, context):
        """Update user context with latest information"""
        self.user_context.update(context)
        self.user_context['recent_interventions'].append({
            'timestamp': context['timestamp'],
            'type': context['intervention_type']
        })

    def is_optimal_timing(self):
        """Determine if current moment is optimal for intervention"""
        recent = self.user_context['recent_interventions']
        if recent:
            last_intervention = recent[-1]
            time_elapsed = self.calculate_time_elapsed(last_intervention['timestamp'])
            return time_elapsed > self.get_minimum_interval()
        return True

    def determine_intervention_type(self, context):
        """Select most appropriate intervention type"""
        attention = self.user_context['attention_span']
        energy = self.user_context['energy_level']
        complexity = self.user_context['task_complexity']

        if attention == 'low' and energy == 'low':
            return 'focus'
        elif complexity == 'high':
            return 'productivity'
        return 'default'

    def generate_action_steps(self, intervention_type, personality_config, context):
        """Generate specific, actionable steps"""
        template = self.intervention_templates[intervention_type]
        
        steps = []
        for action in template['actions']:
            step = {
                'description': self.format_action(action, personality_config),
                'duration': action['duration'],
                'success_metric': action['success_metric'],
                'alternatives': self.generate_alternatives(action),
                'difficulty': self.calculate_difficulty(action, context)
            }
            steps.append(step)
        
        return steps

    def apply_behavioral_principles(self, steps):
        """Apply behavioral psychology principles to steps"""
        enhanced = []
        for step in steps:
            enhanced_step = step.copy()
            enhanced_step.update({
                'motivation_trigger': self.select_motivation_trigger(),
                'habit_component': self.get_habit_component(),
                'cognitive_load': self.assess_cognitive_load(step)
            })
            enhanced.append(enhanced_step)
        return enhanced

    def calculate_optimal_timing(self):
        """Calculate optimal intervention timing"""
        return {
            'time_of_day': self.get_optimal_time(),
            'frequency': self.calculate_frequency(),
            'duration': self.calculate_duration()
        }

    def define_success_metrics(self, intervention_type):
        """Define specific success metrics"""
        return {
            'primary': self.get_primary_metric(intervention_type),
            'secondary': self.get_secondary_metrics(intervention_type),
            'tracking_period': self.get_tracking_period()
        }

    def create_follow_up_plan(self):
        """Create structured follow-up plan"""
        return {
            'timing': self.calculate_follow_up_timing(),
            'type': self.determine_follow_up_type(),
            'metrics': self.select_follow_up_metrics()
        }

    # Helper methods would be implemented here...