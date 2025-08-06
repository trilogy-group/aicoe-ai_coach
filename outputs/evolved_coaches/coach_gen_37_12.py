class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced traits and learning patterns
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
            # Additional types configured similarly
        }

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting applications',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Enable focus mode', 
                     'time_estimate': '1 min',
                     'success_metric': 'Mode activated'},
                    {'step': 'Set timer for focused work block',
                     'time_estimate': '1 min', 
                     'success_metric': 'Timer started'}
                ],
                'follow_up_interval': 25,
                'priority_level': 'high'
            },
            'break': {
                'triggers': ['high_cognitive_load', 'extended_focus_period'],
                'actions': [
                    {'step': 'Stand and stretch',
                     'time_estimate': '2 min',
                     'success_metric': 'Movement completed'},
                    {'step': 'Hydrate',
                     'time_estimate': '1 min',
                     'success_metric': 'Water consumed'},
                    {'step': 'Brief mindfulness exercise',
                     'time_estimate': '3 min',
                     'success_metric': 'Exercise completed'}
                ],
                'follow_up_interval': 5,
                'priority_level': 'medium'
            }
        }

        # Behavioral psychology components
        self.behavior_triggers = {
            'habit_formation': ['implementation_intention', 'habit_stacking', 'environmental_design'],
            'motivation': ['autonomy', 'mastery', 'purpose', 'social_proof'],
            'focus': ['attention_management', 'cognitive_load_optimization', 'context_switching_reduction']
        }

        # User context tracking
        self.user_context = {
            'cognitive_load': 0.0,
            'focus_duration': 0,
            'task_switches': 0,
            'productivity_score': 0.0,
            'intervention_responses': [],
            'successful_actions': []
        }

    def generate_personalized_nudge(self, user_id, context):
        """Generate personalized intervention based on user context and patterns"""
        user_profile = self.get_user_profile(user_id)
        current_context = self.analyze_context(context)
        
        # Select optimal intervention based on multiple factors
        intervention = self.select_intervention(
            personality_type=user_profile['personality_type'],
            cognitive_load=current_context['cognitive_load'],
            task_context=current_context['task_type'],
            historical_response=user_profile['intervention_history']
        )

        # Personalize intervention content
        personalized_content = self.personalize_content(
            intervention=intervention,
            user_profile=user_profile,
            current_context=current_context
        )

        return self.format_nudge(personalized_content)

    def select_intervention(self, personality_type, cognitive_load, task_context, historical_response):
        """Select most appropriate intervention based on multiple factors"""
        personality_config = self.personality_type_configs[personality_type]
        
        # Calculate intervention scores based on multiple factors
        intervention_scores = {}
        for intervention_type, template in self.intervention_templates.items():
            score = self.calculate_intervention_score(
                template=template,
                personality_config=personality_config,
                cognitive_load=cognitive_load,
                task_context=task_context,
                historical_success=historical_response.get(intervention_type, 0)
            )
            intervention_scores[intervention_type] = score
            
        return max(intervention_scores.items(), key=lambda x: x[1])[0]

    def personalize_content(self, intervention, user_profile, current_context):
        """Personalize intervention content based on user profile and context"""
        template = self.intervention_templates[intervention]
        personality_config = self.personality_type_configs[user_profile['personality_type']]

        # Adjust content based on learning style
        content = self.adapt_to_learning_style(
            template['actions'],
            personality_config['learning_style']
        )

        # Modify based on cognitive load
        if current_context['cognitive_load'] > personality_config['cognitive_load_threshold']:
            content = self.simplify_content(content)

        # Add motivation triggers
        content = self.add_motivation_elements(
            content,
            personality_config['motivation_triggers']
        )

        return content

    def track_intervention_effectiveness(self, user_id, intervention_id, response):
        """Track and analyze intervention effectiveness"""
        self.user_context['intervention_responses'].append({
            'user_id': user_id,
            'intervention_id': intervention_id,
            'response': response,
            'context': self.user_context.copy(),
            'timestamp': time.time()
        })

        # Update intervention success metrics
        self.update_intervention_metrics(intervention_id, response)
        
        # Adapt future interventions based on response
        self.adapt_intervention_strategy(user_id, response)

    def calculate_cognitive_load(self, context):
        """Calculate current cognitive load based on multiple factors"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'time_pressure': context.get('time_pressure', 0.5),
            'interruption_frequency': context.get('interruptions', 0.3),
            'task_familiarity': context.get('familiarity', 0.7)
        }
        
        weights = {
            'task_complexity': 0.4,
            'time_pressure': 0.3,
            'interruption_frequency': 0.2,
            'task_familiarity': 0.1
        }

        return sum(factor * weights[key] for key, factor in factors.items())

    def format_nudge(self, content):
        """Format intervention content for delivery"""
        return {
            'message': content['message'],
            'actions': content['actions'],
            'priority': content['priority_level'],
            'timing': self.calculate_optimal_timing(),
            'success_metrics': content['success_metrics'],
            'follow_up': content['follow_up_interval']
        }