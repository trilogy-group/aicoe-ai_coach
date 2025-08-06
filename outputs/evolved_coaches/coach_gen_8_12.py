class EnhancedAICoach:
    def __init__(self):
        # Personality type configurations with enhanced traits
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
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'actions': [
                    {'text': 'Block distracting websites for next 25 minutes',
                     'duration': 25,
                     'priority': 'high',
                     'success_metric': 'focused_time'},
                    {'text': 'Close unnecessary browser tabs',
                     'duration': 2,
                     'priority': 'medium',
                     'success_metric': 'reduced_tabs'}
                ]
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines'],
                'actions': [
                    {'text': 'Break current project into 3-5 smaller tasks',
                     'duration': 10,
                     'priority': 'high',
                     'success_metric': 'task_completion_rate'},
                    {'text': 'Schedule top 3 priorities for tomorrow',
                     'duration': 5,
                     'priority': 'medium',
                     'success_metric': 'priority_completion'}
                ]
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'reinforcement': ['immediate_feedback', 'progress_tracking', 'milestone_rewards'],
            'habit_formation': ['trigger_identification', 'routine_design', 'reward_association'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof']
        }

        self.user_context = {
            'cognitive_load': 0.0,
            'energy_level': 1.0,
            'focus_score': 1.0,
            'recent_interventions': [],
            'action_completion_rate': 0.0
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate personalized intervention based on user context and personality"""
        personality_type = self.get_user_personality(user_id)
        config = self.personality_type_configs[personality_type]
        
        # Update user context
        self.update_user_context(context)
        
        # Check cognitive load threshold
        if self.user_context['cognitive_load'] > config['cognitive_load_threshold']:
            return self.generate_minimal_intervention()
            
        # Select appropriate intervention
        intervention = self.select_intervention(config)
        
        # Personalize based on communication preference
        personalized_actions = self.personalize_actions(
            intervention['actions'],
            config['communication_pref'],
            config['learning_style']
        )
        
        return {
            'message': self.format_message(personalized_actions, config),
            'actions': personalized_actions,
            'follow_up': self.generate_follow_up(intervention)
        }

    def update_user_context(self, context):
        """Update user context with new information"""
        self.user_context.update({
            'cognitive_load': self.calculate_cognitive_load(context),
            'energy_level': self.estimate_energy_level(context),
            'focus_score': self.calculate_focus_score(context)
        })

    def select_intervention(self, config):
        """Select most appropriate intervention based on context"""
        relevant_interventions = []
        for intervention_type, intervention in self.intervention_templates.items():
            if any(trigger in self.user_context for trigger in intervention['triggers']):
                relevance_score = self.calculate_relevance(intervention, config)
                relevant_interventions.append((relevance_score, intervention))
        
        return max(relevant_interventions, key=lambda x: x[0])[1]

    def personalize_actions(self, actions, comm_pref, learning_style):
        """Personalize action steps based on user preferences"""
        personalized = []
        for action in actions:
            modified_action = action.copy()
            modified_action['text'] = self.adapt_communication(
                action['text'], 
                comm_pref,
                learning_style
            )
            personalized.append(modified_action)
        return personalized

    def generate_follow_up(self, intervention):
        """Generate follow-up checks for intervention"""
        return {
            'timing': self.calculate_optimal_timing(intervention),
            'check_type': 'action_completion',
            'metrics': [action['success_metric'] for action in intervention['actions']]
        }

    def calculate_relevance(self, intervention, config):
        """Calculate intervention relevance score"""
        context_match = sum(1 for trigger in intervention['triggers'] 
                          if trigger in self.user_context)
        motivation_match = sum(1 for trigger in config['motivation_triggers'] 
                             if trigger in self.behavior_principles['motivation'])
        return (context_match * 0.6) + (motivation_match * 0.4)

    def calculate_optimal_timing(self, intervention):
        """Calculate optimal timing for follow-up"""
        base_duration = max(action['duration'] for action in intervention['actions'])
        return base_duration + 5  # Add buffer time

    def adapt_communication(self, message, comm_pref, learning_style):
        """Adapt message to user's communication preference and learning style"""
        if comm_pref == 'direct':
            message = f"Action required: {message}"
        elif comm_pref == 'enthusiastic':
            message = f"Ready for positive change? {message}!"
            
        if learning_style == 'systematic':
            message = f"{message} [Step-by-step guide available]"
        elif learning_style == 'exploratory':
            message = f"{message} [Multiple approaches available]"
            
        return message

    def get_user_personality(self, user_id):
        """Get user personality type from profile"""
        # Implementation would fetch from user database
        return 'INTJ'  # Default for example

    def calculate_cognitive_load(self, context):
        """Calculate current cognitive load"""
        # Implementation would use context signals
        return 0.5

    def estimate_energy_level(self, context):
        """Estimate user energy level"""
        # Implementation would use context signals
        return 0.8

    def calculate_focus_score(self, context):
        """Calculate user focus score"""
        # Implementation would use context signals
        return 0.7

    def generate_minimal_intervention(self):
        """Generate minimal intervention for high cognitive load"""
        return {
            'message': "Taking a 2-minute breather would help right now.",
            'actions': [{'text': 'Take a deep breath', 'duration': 2, 'priority': 'high'}],
            'follow_up': {'timing': 3, 'check_type': 'wellbeing'}
        }