def _select_optimal_intervention(self, analysis: Dict, context: Dict, persona: str) -> Dict:
    """Select optimal intervention based on evidence and context."""
    
    interventions = {
        'cognitive_restructuring': {
            'effectiveness': 0.85,
            'evidence_strength': 'strong',
            'suitable_for': ['stress', 'anxiety', 'perfectionism']
        },
        'behavioral_activation': {
            'effectiveness': 0.78,
            'evidence_strength': 'moderate',
            'suitable_for': ['procrastination', 'low_motivation', 'fatigue']
        },
        'mindfulness_based': {
            'effectiveness': 0.72,
            'evidence_strength': 'strong',
            'suitable_for': ['focus', 'stress', 'overwhelm']
        }
    }
    
    # Evaluate context and select best intervention
    current_state = self._assess_current_state(context)
    best_intervention = max(interventions.items(), 
                          key=lambda x: self._calculate_intervention_fit(x[1], current_state))
    
    return best_intervention