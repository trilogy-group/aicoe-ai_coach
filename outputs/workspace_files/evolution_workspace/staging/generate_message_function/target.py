# Evolution target: generate_message
# Type: function
# Source: enhanced_ai_coach.py:125

def generate_message(self, category: str, context_scores: Dict[str, float], 
                        user_profile: Dict[str, Any]) -> str:
        """
        Generate personalized coaching message based on context and user profile.
        This function determines the actual message the user receives.
        """
        if category not in self.message_templates:
            category = 'productivity'  # Default fallback
        
        templates = self.message_templates[category]
        
        # Score each template based on context
        scored_templates = []
        for template in templates:
            score = self._score_template(template, context_scores, user_profile)
            scored_templates.append((template, score))
        
        # Select highest scoring template
        best_template = max(scored_templates, key=lambda x: x[1])[0]
        
        # Personalize the message
        personalized_message = self.personalization_engine.personalize(
            best_template, user_profile
        )
        
        return personalized_message