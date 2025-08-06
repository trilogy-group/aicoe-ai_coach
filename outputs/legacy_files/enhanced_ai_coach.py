#!/usr/bin/env python3
"""
Enhanced AI Coach with Agent-Evolve Integration
==============================================

AI Coach system with evolution decorators for continuous improvement.
Integrates concepts from agent-evolve framework for systematic optimization.
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from agent_evolve import evolve

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContextAnalyzer:
    """Analyzes user context for coaching relevance"""
    
    def __init__(self):
        self.context_history = []
        self.relevance_cache = {}
    
    @evolve(target_type="function", description="Core context analysis algorithm", priority=1)
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

class MessageGenerator:
    """Generates contextually relevant coaching messages"""
    
    def __init__(self):
        self.message_templates = self._load_templates()
        self.personalization_engine = PersonalizationEngine()
    
    #@evolve(target_type="prompt", description="Core coaching message templates", priority=1)
    def _load_templates(self) -> Dict[str, List[str]]:
        """
        Load coaching message templates. These are the core prompts that guide user behavior.
        Critical for coaching effectiveness and user engagement.
        """
        return {
            'productivity': [
                "Break down your current task into 3 smaller, manageable steps",
                "Set a 25-minute focused work session and eliminate distractions",
                "Prioritize your top 3 tasks for today and tackle the most important one first",
                "Use the 2-minute rule: if it takes less than 2 minutes, do it now",
                "Review your goals and align your current activity with your priorities"
            ],
            'wellbeing': [
                "Take 5 deep breaths and notice how you feel in this moment",
                "Stand up, stretch your arms overhead, and roll your shoulders",
                "Drink a glass of water and take a 2-minute walk",
                "Practice gratitude: think of 3 things you're thankful for today",
                "Check in with your posture and adjust for comfort and health"
            ],
            'focus': [
                "Close unnecessary browser tabs and applications to reduce cognitive load",
                "Put your phone in another room or enable focus mode",
                "Set a clear intention for the next 30 minutes of work",
                "Use noise-canceling headphones or find a quieter workspace",
                "Try the Pomodoro technique: 25 minutes focused work, 5-minute break"
            ],
            'motivation': [
                "Remind yourself why this task matters to your bigger goals",
                "Celebrate a recent win, no matter how small",
                "Visualize how you'll feel when you complete this task",
                "Connect with a colleague or friend for accountability",
                "Start with the easiest part to build momentum"
            ]
        }
    
    @evolve(target_type="function", description="Message selection and personalization algorithm", priority=1)
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
    
    def _score_template(self, template: str, context_scores: Dict[str, float], 
                       user_profile: Dict[str, Any]) -> float:
        """Score a template based on context relevance and user preferences"""
        base_score = 0.5
        
        # Keyword-based relevance scoring
        keywords = {
            'task': context_scores.get('productivity', 0),
            'break': context_scores.get('wellbeing', 0),
            'focus': context_scores.get('focus', 0),
            'goal': context_scores.get('motivation', 0)
        }
        
        for keyword, relevance in keywords.items():
            if keyword in template.lower():
                base_score += relevance * 0.3
        
        # User preference adjustment
        preferences = user_profile.get('preferences', {})
        if preferences.get('prefers_short_messages', False) and len(template) < 60:
            base_score += 0.2
        if preferences.get('prefers_action_oriented', True) and any(word in template.lower() 
                                                                   for word in ['do', 'try', 'set', 'take']):
            base_score += 0.2
        
        return min(base_score, 1.0)

class PersonalizationEngine:
    """Personalizes messages based on user profile and history"""
    
    @evolve(target_type="function", description="Message personalization algorithm", priority=2)
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

class EnhancedAICoach:
    """Main AI Coach with evolution framework integration"""
    
    def __init__(self):
        self.context_analyzer = ContextAnalyzer()
        self.message_generator = MessageGenerator()
        self.user_profiles = {}
        self.coaching_history = []
        self.performance_metrics = {
            'messages_sent': 0,
            'user_engagement': 0.0,
            'effectiveness_score': 0.0
        }
    
    @evolve(target_type="function", description="Main coaching orchestration logic", priority=1)
    async def coach_user(self, user_id: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main coaching function that orchestrates the entire coaching process.
        This is the primary user-facing interface.
        """
        try:
            # Get or create user profile
            user_profile = self.user_profiles.get(user_id, self._create_default_profile(user_id))
            
            # Analyze context
            context_scores = self.context_analyzer.analyze_context(user_data)
            
            # Determine best coaching category
            best_category = max(context_scores, key=context_scores.get)
            
            # Generate personalized message
            coaching_message = self.message_generator.generate_message(
                best_category, context_scores, user_profile
            )
            
            # Record coaching interaction
            interaction = {
                'user_id': user_id,
                'timestamp': datetime.now().isoformat(),
                'category': best_category,
                'message': coaching_message,
                'context_scores': context_scores,
                'user_context': user_data
            }
            
            self.coaching_history.append(interaction)
            self.performance_metrics['messages_sent'] += 1
            
            # Return coaching result
            return {
                'success': True,
                'coaching_message': coaching_message,
                'category': best_category,
                'relevance_score': context_scores[best_category],
                'timestamp': interaction['timestamp']
            }
            
        except Exception as e:
            logger.error(f"Error coaching user {user_id}: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'fallback_message': "Stay focused on your goals and take things one step at a time."
            }
    
    def _create_default_profile(self, user_id: str) -> Dict[str, Any]:
        """Create default user profile"""
        profile = {
            'user_id': user_id,
            'name': '',
            'communication_style': 'friendly',
            'preferences': {
                'prefers_short_messages': False,
                'prefers_action_oriented': True,
                'coaching_frequency': 'moderate'
            },
            'created_at': datetime.now().isoformat()
        }
        self.user_profiles[user_id] = profile
        return profile
    
    @evolve(target_type="function", description="User feedback processing for continuous improvement", priority=2)
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
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Get coaching performance metrics"""
        return {
            'total_messages': self.performance_metrics['messages_sent'],
            'avg_user_engagement': self.performance_metrics['user_engagement'],
            'effectiveness_score': self.performance_metrics['effectiveness_score'],
            'active_users': len(self.user_profiles),
            'coaching_categories_used': len(set(h['category'] for h in self.coaching_history)),
            'report_timestamp': datetime.now().isoformat()
        }

# Example usage and testing
async def test_enhanced_coach():
    """Test the enhanced AI coach with various scenarios"""
    coach = EnhancedAICoach()
    
    # Test scenario 1: High stress, low energy user
    test_user_data = {
        'user_id': 'test_user_1',
        'state': {
            'energy_level': 'low',
            'stress_level': 'high',
            'focus_level': 'poor'
        },
        'environment': {
            'location': 'office',
            'noise_level': 'high',
            'distractions': 'many'
        },
        'recent_activities': ['meetings', 'emails', 'calls'],
        'time_context': {
            'hour': 14,  # 2 PM
            'day_of_week': 2  # Wednesday
        }
    }
    
    result = await coach.coach_user('test_user_1', test_user_data)
    print("Test Result 1:")
    print(f"Message: {result['coaching_message']}")
    print(f"Category: {result['category']}")
    print(f"Relevance Score: {result['relevance_score']:.2f}")
    
    # Simulate user feedback
    coach.process_feedback('test_user_1', 'msg_1', {
        'satisfaction': 0.8,
        'usefulness': 0.9,
        'followed_advice': True
    })
    
    # Test scenario 2: High energy, morning user
    test_user_data_2 = {
        'user_id': 'test_user_2',
        'state': {
            'energy_level': 'high',
            'stress_level': 'low',
            'focus_level': 'good'
        },
        'environment': {
            'location': 'home',
            'noise_level': 'low',
            'distractions': 'few'
        },
        'time_context': {
            'hour': 9,  # 9 AM
            'day_of_week': 1  # Tuesday
        }
    }
    
    result2 = await coach.coach_user('test_user_2', test_user_data_2)
    print("\nTest Result 2:")
    print(f"Message: {result2['coaching_message']}")
    print(f"Category: {result2['category']}")
    print(f"Relevance Score: {result2['relevance_score']:.2f}")
    
    # Performance report
    print("\nPerformance Report:")
    report = coach.get_performance_report()
    for key, value in report.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    asyncio.run(test_enhanced_coach())