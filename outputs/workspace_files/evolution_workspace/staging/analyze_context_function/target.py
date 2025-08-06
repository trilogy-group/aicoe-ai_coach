# Evolution target: analyze_context
# Type: function
# Source: enhanced_ai_coach.py:29

def analyze_context(self, user_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Analyze user context and return relevance scores for different coaching categories.
        This is a critical function that determines coaching effectiveness.
        """
        context_scores = {
            'productivity': 0.5,
            'wellbeing': 0.5,
            'focus': 0.5,
            'motivation': 0.5
        }
        
        # Time-based scoring
        hour = datetime.now().hour
        if 9 <= hour <= 12:  # Morning productive hours
            context_scores['productivity'] += 0.3
        elif 13 <= hour <= 15:  # Post-lunch focus dip
            context_scores['focus'] += 0.4
            context_scores['wellbeing'] += 0.2
        elif 16 <= hour <= 18:  # Afternoon energy
            context_scores['motivation'] += 0.3
        
        # User state analysis
        user_state = user_data.get('state', {})
        energy_level = user_state.get('energy_level', 'medium')
        stress_level = user_state.get('stress_level', 'medium')
        
        if energy_level == 'low':
            context_scores['wellbeing'] += 0.4
            context_scores['productivity'] -= 0.2
        elif energy_level == 'high':
            context_scores['productivity'] += 0.3
            context_scores['focus'] += 0.2
        
        if stress_level == 'high':
            context_scores['wellbeing'] += 0.5
            context_scores['focus'] -= 0.3
        
        # Environment factors
        environment = user_data.get('environment', {})
        if environment.get('noise_level') == 'high':
            context_scores['focus'] += 0.3
        if environment.get('location') == 'home':
            context_scores['motivation'] += 0.2
        
        # Normalize scores
        for category in context_scores:
            context_scores[category] = max(0.0, min(1.0, context_scores[category]))
        
        return context_scores