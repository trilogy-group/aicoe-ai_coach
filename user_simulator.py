"""
User Outcome Simulator
Simulates user responses to AI coaching nudges based on persona and context.
"""

import random
import numpy as np
from typing import Dict, List, Any
from datetime import datetime

class UserOutcomeSimulator:
    """Simulates realistic user responses to coaching nudges."""
    
    def __init__(self):
        # Base acceptance rates by persona
        self.persona_acceptance_rates = {
            'developer': 0.72,      # Values autonomy and focus protection
            'analyst': 0.68,        # Moderate acceptance, data-driven
            'manager': 0.45,        # Lower due to meeting interruptions
            'designer': 0.75        # High acceptance for creative flow
        }
        
        # Nudge type effectiveness by persona
        self.nudge_effectiveness = {
            'developer': {
                'focus': {'productivity_lift': 0.18, 'satisfaction_lift': 0.12},
                'wellbeing': {'productivity_lift': 0.08, 'satisfaction_lift': 0.15},
                'value_creation': {'productivity_lift': 0.15, 'satisfaction_lift': 0.10}
            },
            'analyst': {
                'focus': {'productivity_lift': 0.15, 'satisfaction_lift': 0.10},
                'wellbeing': {'productivity_lift': 0.06, 'satisfaction_lift': 0.18},
                'value_creation': {'productivity_lift': 0.12, 'satisfaction_lift': 0.12}
            },
            'manager': {
                'focus': {'productivity_lift': 0.10, 'satisfaction_lift': 0.08},
                'wellbeing': {'productivity_lift': 0.05, 'satisfaction_lift': 0.20},
                'value_creation': {'productivity_lift': 0.08, 'satisfaction_lift': 0.15}
            },
            'designer': {
                'focus': {'productivity_lift': 0.20, 'satisfaction_lift': 0.15},
                'wellbeing': {'productivity_lift': 0.10, 'satisfaction_lift': 0.22},
                'value_creation': {'productivity_lift': 0.12, 'satisfaction_lift': 0.10}
            }
        }
        
        # Context modifiers that affect acceptance
        self.context_modifiers = {
            'high_focus_session': -0.25,     # Don't interrupt deep work
            'multiple_interruptions': +0.35,  # User appreciates help
            'end_of_day': -0.15,            # Lower engagement
            'meeting_heavy_day': +0.25,      # Appreciate wellbeing nudges
            'deadline_pressure': +0.20,      # More receptive to productivity help
            'monday_morning': -0.10,         # Slower start
            'friday_afternoon': -0.20        # Winding down
        }
        
        # Dismissal reasons and their probabilities
        self.dismissal_reasons = {
            'busy': 0.4,
            'not_relevant': 0.25,
            'too_frequent': 0.20,
            'unclear': 0.15
        }
        
        # Track user fatigue
        self.user_fatigue = {}  # user_id -> fatigue_score
    
    def simulate_user_response(self, nudge: Dict, user_persona: str, 
                              current_context: List[str]) -> Dict:
        """Simulate how a user responds to a nudge."""
        user_id = nudge.get('user_id', 0)
        
        # Calculate acceptance probability
        acceptance_prob = self._calculate_acceptance_probability(
            nudge, user_persona, current_context, user_id
        )
        
        # Determine if nudge is accepted
        accepted = random.random() < acceptance_prob
        
        if accepted:
            return self._generate_positive_response(nudge, user_persona)
        else:
            return self._generate_negative_response(nudge, user_persona, current_context)
    
    def _calculate_acceptance_probability(self, nudge: Dict, user_persona: str,
                                        current_context: List[str], user_id: int) -> float:
        """Calculate probability of nudge acceptance."""
        # Start with base rate for persona
        base_rate = self.persona_acceptance_rates.get(user_persona, 0.6)
        
        # Apply context modifiers
        context_adjustment = 0.0
        for context in current_context:
            if context in self.context_modifiers:
                context_adjustment += self.context_modifiers[context]
        
        # Apply confidence modifier
        confidence = nudge.get('confidence', 0.7)
        confidence_modifier = (confidence - 0.5) * 0.3
        
        # Apply fatigue modifier
        fatigue_score = self.user_fatigue.get(user_id, 0)
        fatigue_modifier = -0.1 * fatigue_score
        
        # Apply nudge quality modifiers
        quality_modifier = self._assess_nudge_quality(nudge)
        
        # Calculate final probability
        final_prob = base_rate + context_adjustment + confidence_modifier + \
                    fatigue_modifier + quality_modifier
        
        # Clamp to valid range
        return max(0.1, min(0.9, final_prob))
    
    def _assess_nudge_quality(self, nudge: Dict) -> float:
        """Assess the quality of the nudge and return modifier."""
        quality_score = 0.0
        
        nudge_text = nudge.get('nudge_text', '')
        
        # Check for personalization indicators
        if any(metric in nudge_text for metric in ['tabs', 'minutes', 'hours', '%']):
            quality_score += 0.05
        
        # Check for polite phrasing
        if any(phrase in nudge_text.lower() for phrase in ['want to', 'how about', 'ready for']):
            quality_score += 0.05
        
        # Check for specific actions
        action_words = ['close', 'block', 'schedule', 'try', 'take', 'stretch']
        if any(word in nudge_text.lower() for word in action_words):
            quality_score += 0.05
        
        # Penalize generic nudges
        generic_phrases = ['take a break', 'be more productive', 'focus better']
        if any(phrase in nudge_text.lower() for phrase in generic_phrases):
            quality_score -= 0.05
        
        return quality_score
    
    def _generate_positive_response(self, nudge: Dict, user_persona: str) -> Dict:
        """Generate response for accepted nudge."""
        nudge_type = nudge.get('nudge_type', 'focus')
        
        # Get effectiveness for this persona and nudge type
        effectiveness = self.nudge_effectiveness.get(user_persona, {}).get(
            nudge_type, 
            {'productivity_lift': 0.08, 'satisfaction_lift': 0.10}
        )
        
        # Add randomness to simulate individual variation
        productivity_impact = effectiveness['productivity_lift'] * random.uniform(0.7, 1.3)
        satisfaction_impact = effectiveness['satisfaction_lift'] * random.uniform(0.8, 1.2)
        
        # Response time varies by persona
        response_times = {
            'developer': (5, 30),    # Quick to decide
            'analyst': (10, 45),     # More deliberative
            'manager': (2, 20),      # Quick but distracted
            'designer': (15, 60)     # Thoughtful consideration
        }
        
        min_time, max_time = response_times.get(user_persona, (5, 30))
        response_time = random.uniform(min_time, max_time)
        
        # Follow-through probability
        follow_through_prob = 0.7 + (nudge.get('confidence', 0.7) - 0.5) * 0.4
        
        return {
            'accepted': True,
            'response_time_seconds': response_time,
            'productivity_impact': productivity_impact,
            'satisfaction_impact': satisfaction_impact,
            'follow_through_probability': min(0.95, follow_through_prob),
            'user_feedback': self._generate_positive_feedback(nudge_type)
        }
    
    def _generate_negative_response(self, nudge: Dict, user_persona: str,
                                  current_context: List[str]) -> Dict:
        """Generate response for rejected nudge."""
        # Determine dismissal reason
        reason = self._select_dismissal_reason(current_context)
        
        # Update fatigue
        user_id = nudge.get('user_id', 0)
        self.user_fatigue[user_id] = self.user_fatigue.get(user_id, 0) + 0.2
        
        return {
            'accepted': False,
            'dismissal_reason': reason,
            'productivity_impact': 0.0,
            'satisfaction_impact': -0.02,  # Slight negative for interruption
            'response_time_seconds': random.uniform(0.5, 3),  # Quick dismissal
            'user_feedback': self._generate_negative_feedback(reason)
        }
    
    def _select_dismissal_reason(self, current_context: List[str]) -> str:
        """Select appropriate dismissal reason based on context."""
        # Adjust probabilities based on context
        adjusted_reasons = dict(self.dismissal_reasons)
        
        if 'high_focus_session' in current_context:
            adjusted_reasons['busy'] = 0.7
        elif 'end_of_day' in current_context:
            adjusted_reasons['not_relevant'] = 0.5
        
        # Normalize probabilities
        total = sum(adjusted_reasons.values())
        normalized = {k: v/total for k, v in adjusted_reasons.items()}
        
        # Select reason
        rand = random.random()
        cumulative = 0
        for reason, prob in normalized.items():
            cumulative += prob
            if rand <= cumulative:
                return reason
        
        return 'busy'
    
    def _generate_positive_feedback(self, nudge_type: str) -> str:
        """Generate positive user feedback."""
        feedback_options = {
            'focus': [
                "Good reminder, closing tabs now",
                "Needed that push to focus",
                "Perfect timing, entering deep work"
            ],
            'wellbeing': [
                "Thanks, taking that break",
                "Good catch on the long streak",
                "Stretching now, appreciate it"
            ],
            'value_creation': [
                "Will block time for important work",
                "Good point about automation",
                "Restructuring my priorities"
            ]
        }
        
        options = feedback_options.get(nudge_type, ["Helpful suggestion"])
        return random.choice(options)
    
    def _generate_negative_feedback(self, reason: str) -> str:
        """Generate negative user feedback."""
        feedback_options = {
            'busy': [
                "In the middle of something",
                "Can't break focus right now",
                "Not now"
            ],
            'not_relevant': [
                "Doesn't apply to my current task",
                "Not helpful for what I'm doing",
                "Misunderstood my situation"
            ],
            'too_frequent': [
                "Too many interruptions today",
                "Getting these too often",
                "Need fewer nudges"
            ],
            'unclear': [
                "Not sure what you mean",
                "Suggestion unclear",
                "What specifically should I do?"
            ]
        }
        
        options = feedback_options.get(reason, ["Not helpful"])
        return random.choice(options)
    
    def reset_user_fatigue(self, user_id: int):
        """Reset fatigue for a user (e.g., new day)."""
        self.user_fatigue[user_id] = 0
    
    def get_user_stats(self, user_id: int) -> Dict:
        """Get statistics for a specific user."""
        return {
            'fatigue_level': self.user_fatigue.get(user_id, 0),
            'receptiveness': 1.0 - (self.user_fatigue.get(user_id, 0) * 0.2)
        }
    
    def simulate_long_term_impact(self, accepted_nudges: List[Dict], 
                                 time_period_days: int = 30) -> Dict:
        """Simulate long-term impact of coaching."""
        if not accepted_nudges:
            return {
                'productivity_improvement': 0,
                'satisfaction_improvement': 0,
                'behavior_change_score': 0
            }
        
        # Calculate cumulative impacts
        total_productivity = sum(n.get('productivity_impact', 0) for n in accepted_nudges)
        total_satisfaction = sum(n.get('satisfaction_impact', 0) for n in accepted_nudges)
        
        # Apply diminishing returns
        productivity_improvement = total_productivity * (1 - 0.3 * (time_period_days / 30))
        satisfaction_improvement = total_satisfaction * (1 - 0.2 * (time_period_days / 30))
        
        # Calculate behavior change score
        nudges_per_day = len(accepted_nudges) / max(1, time_period_days)
        behavior_change_score = min(1.0, nudges_per_day * 0.15)
        
        return {
            'productivity_improvement': max(0, productivity_improvement),
            'satisfaction_improvement': max(0, satisfaction_improvement),
            'behavior_change_score': behavior_change_score,
            'sustained_adoption_probability': 0.65 + behavior_change_score * 0.25
        }