class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced traits and preferences
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

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'step': 'Close unnecessary browser tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Open tabs reduced by 50%'},
                    {'step': 'Enable do-not-disturb mode',
                     'time_estimate': '1 min',
                     'success_metric': 'Zero notifications for next hour'}
                ],
                'priority': 'high',
                'follow_up_interval': 30 # minutes
            },
            'productivity': {
                'triggers': ['procrastination', 'low_output'],
                'actions': [
                    {'step': 'Break task into 25-minute segments',
                     'time_estimate': '5 min',
                     'success_metric': 'Complete 2 focused segments'},
                    {'step': 'Remove primary distraction source',
                     'time_estimate': '3 min', 
                     'success_metric': 'Distraction-free for 25 min'}
                ],
                'priority': 'medium',
                'follow_up_interval': 60
            }
            # Additional templates...
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_rewards'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof']
        }

        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 0.0,
            'focus_score': 0.0,
            'recent_interventions': [],
            'successful_strategies': set(),
            'progress_metrics': {}
        }

    def generate_personalized_nudge(self, user_profile, current_context):
        """Generate personalized intervention based on user profile and context"""
        
        # Update user context
        self._update_user_context(current_context)
        
        # Check cognitive load and intervention timing
        if not self._should_intervene():
            return None

        # Select appropriate intervention
        intervention = self._select_intervention(user_profile)
        
        # Personalize based on personality type
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        # Apply behavioral principles
        enhanced_intervention = self._apply_behavior_principles(intervention, personality_config)
        
        # Add specific metrics and follow-up
        return self._format_intervention(enhanced_intervention, user_profile)

    def _update_user_context(self, current_context):
        """Update user context with latest metrics and patterns"""
        self.user_context['cognitive_load'] = current_context.get('cognitive_load', 0.5)
        self.user_context['energy_level'] = current_context.get('energy_level', 0.5)
        self.user_context['focus_score'] = current_context.get('focus_score', 0.5)
        
        # Prune old interventions
        self.user_context['recent_interventions'] = [
            i for i in self.user_context['recent_interventions'] 
            if (time.time() - i['timestamp']) < 3600
        ]

    def _should_intervene(self):
        """Determine if intervention is appropriate based on context"""
        if self.user_context['cognitive_load'] > 0.8:
            return False
            
        if len(self.user_context['recent_interventions']) > 3:
            return False
            
        return True

    def _select_intervention(self, user_profile):
        """Select most appropriate intervention based on user profile and context"""
        # Match intervention to current needs and personality
        personality_config = self.personality_type_configs[user_profile['personality_type']]
        
        best_intervention = None
        max_score = -1
        
        for intervention_type, template in self.intervention_templates.items():
            score = self._calculate_intervention_fit(
                template, 
                personality_config,
                self.user_context
            )
            
            if score > max_score:
                max_score = score
                best_intervention = template
                
        return best_intervention

    def _apply_behavior_principles(self, intervention, personality_config):
        """Enhance intervention with behavioral psychology principles"""
        enhanced = intervention.copy()
        
        # Add motivation elements
        enhanced['motivation_elements'] = [
            principle for principle in self.behavior_principles['motivation']
            if principle in personality_config['motivation_triggers']
        ]
        
        # Add habit formation support
        enhanced['habit_support'] = {
            'trigger': self._identify_habit_trigger(intervention),
            'routine': intervention['actions'],
            'reward': self._design_reward(personality_config)
        }
        
        return enhanced

    def _format_intervention(self, intervention, user_profile):
        """Format intervention with specific metrics and follow-up"""
        formatted = {
            'title': f"Personalized {intervention['priority']} priority recommendation",
            'actions': intervention['actions'],
            'motivation': self._format_motivation(intervention['motivation_elements']),
            'metrics': {
                action['step']: action['success_metric'] 
                for action in intervention['actions']
            },
            'follow_up': {
                'interval': intervention['follow_up_interval'],
                'check_points': self._generate_checkpoints(intervention)
            }
        }
        
        return formatted

    def track_intervention_success(self, intervention_id, success_metrics):
        """Track success of previous interventions"""
        if success_metrics['completed']:
            self.user_context['successful_strategies'].add(intervention_id)
        
        self.user_context['progress_metrics'][intervention_id] = success_metrics

    def _calculate_intervention_fit(self, template, personality_config, context):
        """Calculate how well an intervention matches current needs"""
        score = 0
        
        # Check timing appropriateness
        score += self._evaluate_timing_fit(template, context)
        
        # Check personality match
        score += self._evaluate_personality_fit(template, personality_config)
        
        # Check previous success
        score += self._evaluate_historical_success(template)
        
        return score