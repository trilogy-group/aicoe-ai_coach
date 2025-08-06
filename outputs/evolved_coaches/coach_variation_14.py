def _initialize_timing_intelligence(self):
    self.timing_intelligence = {
        'optimal_intervals': {
            'manager': {'morning': 45, 'afternoon': 30, 'evening': 60},
            'developer': {'morning': 60, 'afternoon': 40, 'evening': 50},
            'analyst': {'morning': 40, 'afternoon': 35, 'evening': 45},
            'designer': {'morning': 50, 'afternoon': 45, 'evening': 55}
        },
        'cognitive_state_modifiers': {
            'flow': 2.0,  # Double the interval during flow
            'stress': 0.5,  # Halve the interval during stress
            'fatigue': 1.5  # Increase interval when fatigued
        },
        'context_modifiers': {
            'meeting': 1.5,
            'deep_work': 2.0,
            'light_work': 0.8
        }
    }