class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced behavioral traits
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

        # Enhanced intervention templates with specific actions
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps', 'time_est': '2 min'},
                    {'step': 'Set timer for focused work', 'time_est': '25 min'},
                    {'step': 'Take structured break', 'time_est': '5 min'}
                ],
                'success_metrics': ['focused_time', 'task_completion'],
                'priority': 'high'
            },
            'motivation': {
                'triggers': ['procrastination', 'low_energy', 'task_avoidance'],
                'actions': [
                    {'step': 'Break task into smaller chunks', 'time_est': '5 min'},
                    {'step': 'Set mini-milestone', 'time_est': '1 min'},
                    {'step': 'Reward progress', 'time_est': '2 min'}
                ],
                'success_metrics': ['task_initiation', 'milestone_completion'],
                'priority': 'medium'
            }
            # Additional templates...
        }

        self.behavioral_tracking = {
            'engagement_metrics': {},
            'intervention_effectiveness': {},
            'progress_indicators': {},
            'cognitive_load': {}
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        
        # Get personality configuration
        user_config = self.personality_type_configs[personality_type]
        
        # Assess current cognitive load
        cognitive_load = self._assess_cognitive_load(user_context)
        
        # Select appropriate intervention based on context
        intervention = self._select_intervention(
            user_context, 
            user_config,
            cognitive_load
        )
        
        # Personalize intervention content
        personalized_content = self._personalize_content(
            intervention,
            user_config['communication_pref'],
            user_config['learning_style']
        )
        
        # Add behavioral psychology elements
        enhanced_content = self._add_behavioral_elements(
            personalized_content,
            user_config['motivation_triggers']
        )
        
        return enhanced_content

    def _assess_cognitive_load(self, context):
        """Assess current cognitive load based on context"""
        factors = {
            'active_tasks': len(context.get('active_tasks', [])),
            'time_pressure': context.get('deadline_proximity', 0),
            'task_complexity': context.get('task_complexity', 0),
            'interruption_frequency': context.get('interruptions', 0)
        }
        
        # Calculate weighted cognitive load score
        load_score = sum(factors.values()) / len(factors)
        
        self.behavioral_tracking['cognitive_load'] = load_score
        return load_score

    def _select_intervention(self, context, user_config, cognitive_load):
        """Select most appropriate intervention based on context"""
        
        # Check cognitive load threshold
        if cognitive_load > user_config['cognitive_load_threshold']:
            return self.intervention_templates['focus']
            
        # Match context triggers to intervention templates
        matching_interventions = []
        for template_name, template in self.intervention_templates.items():
            if any(trigger in context for trigger in template['triggers']):
                matching_interventions.append(template)
                
        # Select highest priority matching intervention
        return max(matching_interventions, key=lambda x: x['priority'])

    def _personalize_content(self, intervention, comm_style, learning_style):
        """Personalize intervention content for user"""
        
        personalized_actions = []
        for action in intervention['actions']:
            # Adapt language style
            step = self._adapt_language(action['step'], comm_style)
            
            # Add learning style elements
            if learning_style == 'systematic':
                step = f"{step} [Expected outcome: {intervention['success_metrics']}]"
            elif learning_style == 'exploratory':
                step = f"{step} [Try this approach: {self._generate_exploration_prompt(step)}]"
                
            personalized_actions.append({
                'step': step,
                'time_est': action['time_est']
            })
            
        return {
            'actions': personalized_actions,
            'metrics': intervention['success_metrics']
        }

    def _add_behavioral_elements(self, content, motivation_triggers):
        """Add behavioral psychology elements to intervention"""
        
        enhanced_content = content.copy()
        
        # Add motivation aligned with triggers
        motivation_element = self._generate_motivation_prompt(motivation_triggers)
        enhanced_content['motivation'] = motivation_element
        
        # Add commitment device
        enhanced_content['commitment'] = self._generate_commitment_prompt()
        
        # Add progress tracking
        enhanced_content['progress_check'] = {
            'timeframe': '1 hour',
            'check_points': self._generate_progress_checkpoints(content['actions'])
        }
        
        return enhanced_content

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Track effectiveness of interventions"""
        self.behavioral_tracking['intervention_effectiveness'][intervention_id] = metrics
        self._update_intervention_models(metrics)

    def _adapt_language(self, content, style):
        """Adapt language based on communication style"""
        if style == 'direct':
            return content
        elif style == 'enthusiastic':
            return f"{content}! 💪"
        return content

    def _generate_exploration_prompt(self, step):
        """Generate exploratory learning prompt"""
        return f"Experiment with different approaches to {step.lower()}"

    def _generate_motivation_prompt(self, triggers):
        """Generate motivation prompt based on triggers"""
        prompts = {
            'mastery': "This will help you master your craft.",
            'autonomy': "You're in control of your progress.",
            'achievement': "Each step brings you closer to your goal.",
            'novelty': "Try this fresh approach!",
            'social_connection': "Share your progress with your team!",
            'creativity': "Make this process your own!"
        }
        return [prompts[trigger] for trigger in triggers]

    def _generate_commitment_prompt(self):
        """Generate commitment device prompt"""
        return "Will you commit to trying this for the next 25 minutes?"

    def _generate_progress_checkpoints(self, actions):
        """Generate progress checkpoints"""
        return [f"Complete {action['step']}" for action in actions]

    def _update_intervention_models(self, metrics):
        """Update intervention models based on effectiveness metrics"""
        # Implementation for model updating based on effectiveness metrics
        pass