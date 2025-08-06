# Evolution target: personalize
# Type: function
# Source: enhanced_ai_coach.py:183

def personalize(self, message: str, user_profile: Dict[str, Any]) -> str:
        """
        Personalize coaching message based on user profile.
        Adapts tone, style, and content to user preferences.
        """
        name = user_profile.get('name', '')
        communication_style = user_profile.get('communication_style', 'friendly')
        
        # Add personal touch
        if name and len(message) > 50:  # Only for longer messages
            message = f"{name}, {message.lower()}"
        
        # Adjust tone based on communication style
        if communication_style == 'direct':
            # Make message more direct and concise
            message = message.replace('Consider ', '').replace('Try ', '')
            message = message.replace('You might want to ', '')
        elif communication_style == 'encouraging':
            # Add encouraging words
            encouraging_prefixes = ["You've got this! ", "Great job so far. ", "You're doing well. "]
            import random
            message = random.choice(encouraging_prefixes) + message
        
        return message