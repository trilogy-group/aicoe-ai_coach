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
                'template': 'Build habit of {behavior} by {implementation_strategy}',
                'frequency': 'recurring',
                'follow_up': True,
                'metrics': ['consistency', 'sustainability'] 
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
            'ability': ['simplicity', 'clarity', 'resources'],
            'prompt': ['context', 'timing', 'relevance']
        }

    def generate_personalized_nudge(self, user_context, personality_type):
        """Generate personalized coaching intervention based on context and type"""
        user_config = self.personality_type_configs[personality_type]
        
        # Context analysis
        attention_capacity = self._assess_cognitive_load(user_context)
        optimal_timing = self._determine_intervention_timing(user_context)
        
        # Intervention selection
        intervention = self._select_intervention_type(user_context, user_config)
        
        # Personalization
        nudge = self._personalize_content(intervention, user_config)
        
        # Add actionability
        nudge = self._enhance_actionability(nudge, attention_capacity)
        
        return {
            'content': nudge,
            'timing': optimal_timing,
            'follow_up': intervention['follow_up'],
            'success_metrics': intervention['metrics']
        }

    def _assess_cognitive_load(self, context):
        """Evaluate user's current cognitive capacity"""
        factors = {
            'task_complexity': context.get('current_task_complexity', 0.5),
            'time_pressure': context.get('deadline_proximity', 0.5),
            'interruption_frequency': context.get('notifications_per_hour', 0) / 10,
            'energy_level': context.get('energy_level', 0.5)
        }
        
        load_score = sum(factors.values()) / len(factors)
        return 1 - load_score  # Return available capacity

    def _determine_intervention_timing(self, context):
        """Calculate optimal intervention timing"""
        current_task = context.get('current_task')
        schedule = context.get('schedule', [])
        
        # Find next available attention window
        available_slots = self._find_attention_windows(schedule)
        optimal_slot = self._select_best_slot(available_slots, current_task)
        
        return optimal_slot

    def _select_intervention_type(self, context, user_config):
        """Choose appropriate intervention type based on context"""
        if context.get('needs_immediate_action'):
            return self.intervention_types['action']
        elif context.get('pattern_detected'):
            return self.intervention_types['habit']
        else:
            return self.intervention_types['reflection']

    def _personalize_content(self, intervention, user_config):
        """Customize intervention content for user"""
        template = intervention['template']
        
        # Apply communication style
        content = self._adapt_communication_style(
            template, 
            user_config['communication_pref']
        )
        
        # Add behavioral triggers
        content = self._incorporate_behavior_triggers(
            content,
            user_config['learning_style']
        )
        
        return content

    def _enhance_actionability(self, content, attention_capacity):
        """Make intervention more actionable based on capacity"""
        if attention_capacity < 0.3:
            # Simplify for low attention
            return self._create_micro_action(content)
        elif attention_capacity < 0.7:
            # Balance detail and simplicity
            return self._create_structured_action(content)
        else:
            # Provide comprehensive guidance
            return self._create_detailed_action(content)

    def track_intervention_effectiveness(self, intervention_id, metrics):
        """Track and analyze intervention success"""
        # Implementation omitted for brevity
        pass

    def adapt_strategy(self, effectiveness_data):
        """Adjust coaching strategy based on effectiveness"""
        # Implementation omitted for brevity
        pass

    def _create_micro_action(self, content):
        """Create extremely simple, immediate action step"""
        return f"Quick Win: {content}"

    def _create_structured_action(self, content):
        """Create balanced, structured action plan"""
        return f"Action Plan:\n1. {content}\n2. Track progress\n3. Review results"

    def _create_detailed_action(self, content):
        """Create comprehensive action guidance"""
        return f"""Detailed Plan:
1. {content}
2. Implementation steps: ...
3. Success metrics: ...
4. Follow-up schedule: ...
5. Resources needed: ..."""