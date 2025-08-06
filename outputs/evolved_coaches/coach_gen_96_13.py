class EnhancedAICoach:
    def __init__(self):
        # Personality configurations from Parent 2
        self.personality_type_configs = {
            'INTJ': {'learning_style': 'systematic', 'communication_pref': 'direct', 'work_pattern': 'deep_focus'},
            'ENFP': {'learning_style': 'exploratory', 'communication_pref': 'enthusiastic', 'work_pattern': 'flexible'},
            # Additional types omitted for brevity
        }

        # Enhanced intervention configurations
        self.intervention_types = {
            'action': {
                'template': '{specific_action} for {duration} to achieve {outcome}',
                'frequency': 'daily',
                'follow_up': True,
                'metrics': ['completion_rate', 'effectiveness']
            },
            'habit': {
                'template': 'Build habit of {behavior} by {implementation_intention}',
                'frequency': 'recurring',
                'follow_up': True,
                'metrics': ['consistency', 'automaticity']
            },
            'reflection': {
                'template': 'Reflect on {topic} considering {aspects}',
                'frequency': 'weekly',
                'follow_up': False,
                'metrics': ['insight_gained', 'behavior_change']
            }
        }

        # Behavioral psychology principles
        self.behavior_triggers = {
            'motivation': ['autonomy', 'mastery', 'purpose'],
            'ability': ['simplicity', 'resources', 'skills'],
            'prompt': ['context', 'timing', 'format']
        }

        self.user_context = {}
        self.intervention_history = []
        self.effectiveness_metrics = {}

    def generate_personalized_nudge(self, user_id, context):
        """Generate personalized intervention based on user context and history"""
        user_profile = self._get_user_profile(user_id)
        current_context = self._analyze_context(context)
        
        # Select optimal intervention type
        intervention = self._select_intervention(user_profile, current_context)
        
        # Apply behavioral psychology principles
        enhanced_intervention = self._apply_behavior_principles(intervention)
        
        # Add specificity and actionability
        actionable_intervention = self._make_actionable(enhanced_intervention)
        
        self._log_intervention(user_id, actionable_intervention)
        return actionable_intervention

    def _get_user_profile(self, user_id):
        """Retrieve and analyze user profile including personality type and preferences"""
        profile = {
            'personality_type': 'INTJ',  # Would be fetched from database
            'learning_history': self.intervention_history,
            'effectiveness_patterns': self.effectiveness_metrics
        }
        return profile

    def _analyze_context(self, context):
        """Analyze current user context for optimal intervention timing"""
        return {
            'cognitive_load': self._estimate_cognitive_load(context),
            'attention_availability': self._check_attention_availability(context),
            'task_complexity': context.get('task_complexity', 'medium'),
            'time_of_day': context.get('time_of_day'),
            'environment': context.get('environment')
        }

    def _select_intervention(self, profile, context):
        """Select most appropriate intervention based on user profile and context"""
        personality_config = self.personality_type_configs[profile['personality_type']]
        
        if context['cognitive_load'] == 'high':
            return self._generate_simple_intervention(personality_config)
        else:
            return self._generate_comprehensive_intervention(personality_config)

    def _apply_behavior_principles(self, intervention):
        """Apply behavioral psychology principles to strengthen intervention"""
        enhanced = intervention.copy()
        
        # Add motivation triggers
        enhanced['motivation_elements'] = [
            trigger for trigger in self.behavior_triggers['motivation']
            if self._is_relevant_trigger(trigger, intervention)
        ]
        
        # Add ability enhancers
        enhanced['ability_support'] = self._generate_ability_support(intervention)
        
        # Optimize prompt timing and format
        enhanced['delivery'] = self._optimize_delivery(intervention)
        
        return enhanced

    def _make_actionable(self, intervention):
        """Add specific, measurable actions to intervention"""
        actionable = intervention.copy()
        
        actionable.update({
            'specific_steps': self._generate_action_steps(intervention),
            'success_metrics': self._define_success_metrics(intervention),
            'time_estimate': self._estimate_time_requirement(intervention),
            'difficulty_level': self._assess_difficulty(intervention),
            'alternative_approaches': self._generate_alternatives(intervention)
        })
        
        return actionable

    def track_effectiveness(self, user_id, intervention_id, metrics):
        """Track and analyze intervention effectiveness"""
        self.effectiveness_metrics[intervention_id] = metrics
        self._update_user_model(user_id, metrics)
        self._optimize_future_interventions(user_id)

    def _generate_action_steps(self, intervention):
        """Generate specific, sequential action steps"""
        return [
            {'step': 1, 'action': 'Define specific goal', 'duration': '5 mins'},
            {'step': 2, 'action': 'Break down into subtasks', 'duration': '10 mins'},
            {'step': 3, 'action': 'Set up environment', 'duration': '5 mins'},
            {'step': 4, 'action': 'Execute first subtask', 'duration': '25 mins'}
        ]

    def _define_success_metrics(self, intervention):
        """Define measurable success metrics"""
        return {
            'completion': 'Binary task completion',
            'quality': 'Scale of 1-5',
            'time_spent': 'Minutes',
            'perceived_value': 'Scale of 1-5'
        }

    def _estimate_cognitive_load(self, context):
        """Estimate current cognitive load based on context"""
        factors = {
            'task_complexity': context.get('task_complexity', 0.5),
            'distractions': context.get('distractions', 0.3),
            'fatigue': context.get('fatigue', 0.2)
        }
        return sum(factors.values()) / len(factors)

    def _check_attention_availability(self, context):
        """Assess user's current attention availability"""
        return {
            'focus_level': context.get('focus_level', 'medium'),
            'interruption_cost': context.get('interruption_cost', 'low'),
            'time_pressure': context.get('time_pressure', 'medium')
        }

    def _log_intervention(self, user_id, intervention):
        """Log intervention for tracking and analysis"""
        self.intervention_history.append({
            'user_id': user_id,
            'intervention': intervention,
            'timestamp': 'current_timestamp',
            'context': self.user_context
        })