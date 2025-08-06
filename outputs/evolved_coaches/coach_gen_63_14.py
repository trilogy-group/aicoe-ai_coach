class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_triggers': ['mastery', 'achievement', 'efficiency'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_triggers': ['novelty', 'creativity', 'social_impact'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Focus timer started'},
                    {'step': 'Clear workspace',
                     'time_estimate': '3 min', 
                     'success_metric': 'Desk organized'}
                ],
                'follow_up_interval': 30 # minutes
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus', 'stress_signals'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Deep breathing exercise',
                     'time_estimate': '3 min',
                     'success_metric': 'Breathing cycles done'},
                    {'step': 'Hydrate',
                     'time_estimate': '1 min',
                     'success_metric': 'Water consumed'}
                ],
                'follow_up_interval': 15
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_rewards'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'competence', 'relatedness']
        }

        self.user_context = {}
        self.intervention_history = []
        
    def analyze_user_context(self, context_data):
        """Analyze user context for personalized interventions"""
        self.user_context = {
            'personality_type': context_data.get('personality_type'),
            'current_task': context_data.get('current_task'),
            'cognitive_load': self._estimate_cognitive_load(context_data),
            'energy_level': context_data.get('energy_level', 0.5),
            'time_of_day': context_data.get('time_of_day'),
            'recent_breaks': context_data.get('recent_breaks', []),
            'productivity_metrics': context_data.get('productivity_metrics', {})
        }
        return self.user_context

    def generate_intervention(self):
        """Generate personalized intervention based on context"""
        personality_config = self.personality_type_configs[self.user_context['personality_type']]
        
        # Select appropriate intervention template
        template = self._select_intervention_template()
        
        # Personalize intervention
        intervention = {
            'type': template['type'],
            'timing': self._optimize_timing(),
            'actions': self._personalize_actions(template['actions'], personality_config),
            'motivation_hook': self._generate_motivation_hook(personality_config),
            'follow_up': {
                'interval': template['follow_up_interval'],
                'type': 'check_progress'
            }
        }
        
        self.intervention_history.append(intervention)
        return intervention

    def _estimate_cognitive_load(self, context_data):
        """Estimate current cognitive load based on context"""
        factors = {
            'task_complexity': context_data.get('task_complexity', 0.5),
            'time_pressure': context_data.get('time_pressure', 0.5),
            'interruptions': len(context_data.get('recent_interruptions', [])),
            'task_switching': context_data.get('task_switches_per_hour', 0)
        }
        
        weights = {'task_complexity': 0.4, 'time_pressure': 0.3, 
                  'interruptions': 0.2, 'task_switching': 0.1}
        
        cognitive_load = sum(factors[k] * weights[k] for k in factors)
        return min(cognitive_load, 1.0)

    def _select_intervention_template(self):
        """Select appropriate intervention template based on context"""
        cognitive_load = self.user_context['cognitive_load']
        energy_level = self.user_context['energy_level']
        
        if cognitive_load > 0.7:
            return self.intervention_templates['break']
        elif energy_level < 0.3:
            return self.intervention_templates['energize']
        else:
            return self.intervention_templates['focus']

    def _personalize_actions(self, actions, personality_config):
        """Personalize action steps based on personality"""
        personalized_actions = []
        for action in actions:
            personalized_action = action.copy()
            personalized_action['style'] = personality_config['communication_pref']
            personalized_action['complexity'] = self._adjust_complexity(
                action, personality_config['learning_style']
            )
            personalized_actions.append(personalized_action)
        return personalized_actions

    def _generate_motivation_hook(self, personality_config):
        """Generate personalized motivation message"""
        triggers = personality_config['motivation_triggers']
        return {
            'message': f"This aligns with your goal of {triggers[0]}",
            'principle': self.behavior_principles['motivation'][0],
            'reinforcement': self._select_reinforcement(triggers)
        }

    def _optimize_timing(self):
        """Optimize intervention timing"""
        recent_breaks = self.user_context['recent_breaks']
        time_of_day = self.user_context['time_of_day']
        
        if not recent_breaks or (time_of_day - recent_breaks[-1]).minutes > 90:
            return 'immediate'
        return 'defer_15min'

    def _adjust_complexity(self, action, learning_style):
        """Adjust action complexity based on learning style"""
        if learning_style == 'systematic':
            return {'detail_level': 'high', 'steps': 'sequential'}
        return {'detail_level': 'moderate', 'steps': 'flexible'}

    def _select_reinforcement(self, triggers):
        """Select appropriate reinforcement based on motivation triggers"""
        return {
            'type': 'achievement_badge' if 'achievement' in triggers else 'progress_bar',
            'milestone': 'completion',
            'reward': self._generate_reward(triggers)
        }

    def _generate_reward(self, triggers):
        """Generate appropriate reward based on motivation triggers"""
        return {
            'type': 'mastery_points' if 'mastery' in triggers else 'creativity_bonus',
            'value': 100,
            'unlock': 'new_capability'
        }