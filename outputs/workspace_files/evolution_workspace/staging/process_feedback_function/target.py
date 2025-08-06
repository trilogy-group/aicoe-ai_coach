# Evolution target: process_feedback
# Type: function
# Source: enhanced_ai_coach.py:290

def process_feedback(self, user_id: str, message_id: str, feedback: Dict[str, Any]) -> None:
        """
        Process user feedback to improve coaching effectiveness.
        This is critical for the reinforcement learning aspect.
        """
        # Find the interaction
        interaction = None
        for hist in self.coaching_history:
            if (hist['user_id'] == user_id and 
                hist.get('message_id') == message_id):
                interaction = hist
                break
        
        if not interaction:
            logger.warning(f"Interaction not found for feedback processing: {message_id}")
            return
        
        # Process different types of feedback
        satisfaction_score = feedback.get('satisfaction', 0.5)  # 0-1 scale
        usefulness_score = feedback.get('usefulness', 0.5)     # 0-1 scale
        followed_advice = feedback.get('followed_advice', False)
        
        # Update performance metrics
        self.performance_metrics['user_engagement'] = (
            self.performance_metrics['user_engagement'] * 0.9 + 
            satisfaction_score * 0.1
        )
        
        effectiveness_boost = 0.1 if followed_advice else -0.05
        self.performance_metrics['effectiveness_score'] = max(0.0, min(1.0,
            self.performance_metrics['effectiveness_score'] + effectiveness_boost
        ))
        
        # Update user profile based on feedback
        user_profile = self.user_profiles.get(user_id)
        if user_profile:
            if satisfaction_score < 0.3:
                # User didn't like the message style, adjust preferences
                if len(interaction['message']) > 80:
                    user_profile['preferences']['prefers_short_messages'] = True
            elif satisfaction_score > 0.8:
                # User liked the message, reinforce the style
                category = interaction['category']
                user_profile['preferences'][f'likes_{category}'] = True
        
        logger.info(f"Processed feedback for user {user_id}: satisfaction={satisfaction_score}")