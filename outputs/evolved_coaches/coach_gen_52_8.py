class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral factors
        self.personality_type_configs = {
            'INTJ': {
                'learning_style': 'systematic',
                'communication_pref': 'direct',
                'work_pattern': 'deep_focus',
                'motivation_drivers': ['mastery', 'autonomy'],
                'cognitive_load_threshold': 0.8
            },
            'ENFP': {
                'learning_style': 'exploratory', 
                'communication_pref': 'enthusiastic',
                'work_pattern': 'flexible',
                'motivation_drivers': ['novelty', 'social'],
                'cognitive_load_threshold': 0.6
            }
            # Additional types...
        }

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching'],
                'recommendations': [
                    {
                        'action': 'Enable focus mode for 25 minutes',
                        'time_estimate': 25,
                        'difficulty': 'low',
                        'success_metric': 'Completed focused work session',
                        'follow_up': 'Did you complete the focused session?'
                    }
                ],
                'psychological_principle': 'attention_restoration'
            },
            'productivity': {
                'triggers': ['low_output', 'procrastination'],
                'recommendations': [
                    {
                        'action': 'Break task into 3 smaller subtasks',
                        'time_estimate': 10,
                        'difficulty': 'medium', 
                        'success_metric': 'Subtasks defined and scheduled',
                        'follow_up': 'Have you broken down the task?'
                    }
                ],
                'psychological_principle': 'goal_gradient'
            }
        }

        # Cognitive load and attention management
        self.cognitive_metrics = {
            'current_load': 0.0,
            'attention_span': 25,
            'recovery_needed': False,
            'task_complexity': 0.0
        }

        # Enhanced user context tracking
        self.user_context = {
            'personality_type': None,
            'current_goals': [],
            'progress_history': {},
            'intervention_responses': {},
            'peak_productivity_times': [],
            'stress_indicators': []
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate highly personalized intervention based on user context"""
        
        # Get user profile and current context
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        # Check cognitive load and timing
        if not self.is_good_intervention_timing(current_context):
            return None

        # Select most relevant intervention
        intervention = self.select_intervention(user_profile, current_context)
        
        # Personalize based on personality type
        personalized_intervention = self.personalize_intervention(
            intervention,
            user_profile['personality_type']
        )

        # Add behavioral psychology elements
        enhanced_intervention = self.add_behavioral_elements(
            personalized_intervention,
            user_profile['motivation_drivers']
        )

        return enhanced_intervention

    def select_intervention(self, user_profile, context):
        """Select most appropriate intervention based on user state"""
        
        # Calculate intervention priorities
        priorities = {}
        for intervention_type, template in self.intervention_templates.items():
            priority = self.calculate_priority(
                template,
                context,
                user_profile
            )
            priorities[intervention_type] = priority

        # Select highest priority intervention
        selected_type = max(priorities.items(), key=lambda x: x[1])[0]
        return self.intervention_templates[selected_type]

    def personalize_intervention(self, intervention, personality_type):
        """Customize intervention based on personality preferences"""
        
        config = self.personality_type_configs[personality_type]
        
        personalized = intervention.copy()
        personalized['style'] = config['communication_pref']
        personalized['pacing'] = config['work_pattern']
        personalized['complexity'] = self.adjust_complexity(
            intervention,
            config['cognitive_load_threshold']
        )

        return personalized

    def add_behavioral_elements(self, intervention, motivation_drivers):
        """Add psychological elements to increase effectiveness"""
        
        enhanced = intervention.copy()
        
        # Add motivation triggers
        enhanced['motivational_framing'] = self.generate_motivation_frame(
            motivation_drivers
        )
        
        # Add commitment devices
        enhanced['commitment_strategy'] = self.generate_commitment_device()
        
        # Add social proof elements if relevant
        if 'social' in motivation_drivers:
            enhanced['social_proof'] = self.generate_social_proof()

        return enhanced

    def is_good_intervention_timing(self, context):
        """Determine if this is a good time to intervene"""
        
        # Check cognitive load
        if self.cognitive_metrics['current_load'] > 0.8:
            return False
            
        # Check if in flow state
        if context.get('in_flow_state', False):
            return False
            
        # Check time since last intervention
        if not self.check_intervention_spacing():
            return False
            
        return True

    def track_intervention_outcome(self, intervention_id, outcome_metrics):
        """Track and learn from intervention results"""
        
        # Record outcome
        self.user_context['intervention_responses'][intervention_id] = outcome_metrics
        
        # Update effectiveness models
        self.update_intervention_models(intervention_id, outcome_metrics)
        
        # Adjust future recommendations
        self.optimize_recommendation_engine(outcome_metrics)

    def generate_motivation_frame(self, drivers):
        """Generate motivational framing based on user's drivers"""
        frames = {
            'mastery': 'This will help you develop expertise in...',
            'autonomy': 'You have full control over how to...',
            'novelty': 'Try this innovative approach to...',
            'social': 'Others have found success by...'
        }
        return [frames[driver] for driver in drivers]

    def generate_commitment_device(self):
        """Create commitment mechanism to increase follow-through"""
        return {
            'type': 'implementation_intention',
            'template': 'When {situation} occurs, I will {action}',
            'reminder_timing': 'context_based'
        }

    def generate_social_proof(self):
        """Generate relevant social proof elements"""
        return {
            'success_stories': ['relevant_example_1', 'relevant_example_2'],
            'peer_statistics': 'X% of similar users succeeded by...',
            'community_support': 'Connect with others working on...'
        }