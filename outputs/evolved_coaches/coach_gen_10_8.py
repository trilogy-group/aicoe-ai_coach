class EnhancedAICoach:
    def __init__(self):
        # Personality configurations with enhanced traits and preferences
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

        # Enhanced intervention templates with specific actions and metrics
        self.intervention_templates = {
            'focus': {
                'triggers': ['distraction', 'task_switching', 'low_productivity'],
                'actions': [
                    {'step': 'Close distracting apps/tabs',
                     'time_estimate': '2 min',
                     'success_metric': 'Apps closed'},
                    {'step': 'Set timer for focused work block', 
                     'time_estimate': '1 min',
                     'success_metric': 'Timer started'},
                    {'step': 'Review task priorities',
                     'time_estimate': '3 min', 
                     'success_metric': 'Priority list created'}
                ],
                'follow_up': {'timing': 25, 'type': 'check_progress'}
            },
            'planning': {
                'triggers': ['overwhelm', 'missed_deadlines', 'task_confusion'],
                'actions': [
                    {'step': 'Brain dump all tasks',
                     'time_estimate': '5 min',
                     'success_metric': 'Task list created'},
                    {'step': 'Categorize by priority/deadline',
                     'time_estimate': '5 min',
                     'success_metric': 'Tasks categorized'},
                    {'step': 'Schedule top 3 priorities',
                     'time_estimate': '3 min',
                     'success_metric': 'Calendar updated'}
                ],
                'follow_up': {'timing': 60, 'type': 'review_progress'}
            }
        }

        # Behavioral psychology principles
        self.behavior_principles = {
            'habit_formation': {
                'cue': None,
                'routine': None,
                'reward': None,
                'min_repetitions': 21
            },
            'motivation': {
                'autonomy': 0.0,
                'competence': 0.0,
                'relatedness': 0.0
            },
            'cognitive_load': {
                'current': 0.0,
                'threshold': 0.8,
                'recovery_time': 45
            }
        }

        # User context tracking
        self.user_context = {
            'personality_type': None,
            'energy_level': 1.0,
            'focus_score': 1.0,
            'recent_interventions': [],
            'successful_strategies': set(),
            'progress_metrics': {}
        }

    def generate_intervention(self, context_data):
        """Generate personalized intervention based on user context"""
        
        # Update user context
        self.update_user_context(context_data)
        
        # Check cognitive load and timing
        if not self.is_good_intervention_timing():
            return None

        # Select appropriate intervention template
        template = self.select_intervention_template()
        
        # Personalize intervention
        intervention = self.personalize_intervention(template)
        
        # Add behavioral psychology elements
        intervention = self.enhance_with_psychology(intervention)
        
        return intervention

    def update_user_context(self, context_data):
        """Update user context with new data"""
        self.user_context.update({
            'energy_level': context_data.get('energy_level', self.user_context['energy_level']),
            'focus_score': context_data.get('focus_score', self.user_context['focus_score']),
            'recent_interventions': self.user_context['recent_interventions'][-5:] + [context_data.get('last_intervention')]
        })
        
        # Update progress metrics
        if 'completed_actions' in context_data:
            self.update_progress_metrics(context_data['completed_actions'])

    def is_good_intervention_timing(self):
        """Check if it's a good time for intervention"""
        # Check cognitive load
        if self.user_context['focus_score'] < self.behavior_principles['cognitive_load']['threshold']:
            return False
            
        # Check intervention frequency
        if len(self.user_context['recent_interventions']) >= 3:
            time_since_last = time.time() - self.user_context['recent_interventions'][-1]['timestamp']
            if time_since_last < 1800:  # 30 minutes
                return False
                
        return True

    def select_intervention_template(self):
        """Select most appropriate intervention template"""
        # Get personality config
        personality = self.personality_type_configs[self.user_context['personality_type']]
        
        # Match template to current context and personality
        best_template = None
        best_score = -1
        
        for template_name, template in self.intervention_templates.items():
            score = self.calculate_template_fit(template, personality)
            if score > best_score:
                best_score = score
                best_template = template
                
        return best_template

    def personalize_intervention(self, template):
        """Personalize intervention based on user context"""
        personality = self.personality_type_configs[self.user_context['personality_type']]
        
        personalized = {
            'communication_style': personality['communication_pref'],
            'difficulty': self.adapt_difficulty(template),
            'actions': self.prioritize_actions(template['actions']),
            'motivation_hooks': [t for t in personality['motivation_triggers']],
            'follow_up': self.customize_follow_up(template['follow_up'])
        }
        
        return personalized

    def enhance_with_psychology(self, intervention):
        """Add behavioral psychology elements"""
        # Add habit formation elements
        intervention['habit_cue'] = self.identify_habit_cue()
        intervention['habit_reward'] = self.select_reward()
        
        # Add motivation elements
        intervention['motivation'] = {
            'autonomy_support': self.generate_autonomy_support(),
            'competence_building': self.identify_competence_opportunities(),
            'social_connection': self.add_social_elements()
        }
        
        # Add cognitive load management
        intervention['cognitive_strategies'] = self.generate_cognitive_strategies()
        
        return intervention

    def update_progress_metrics(self, completed_actions):
        """Update user progress metrics"""
        for action in completed_actions:
            if action['type'] not in self.user_context['progress_metrics']:
                self.user_context['progress_metrics'][action['type']] = {
                    'attempts': 0,
                    'completions': 0,
                    'success_rate': 0.0
                }
            
            metrics = self.user_context['progress_metrics'][action['type']]
            metrics['attempts'] += 1
            if action['completed']:
                metrics['completions'] += 1
                metrics['success_rate'] = metrics['completions'] / metrics['attempts']

            if metrics['success_rate'] > 0.7:
                self.user_context['successful_strategies'].add(action['type'])