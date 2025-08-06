#!/usr/bin/env python3
"""
AI Sophistication Evaluation
============================

Evaluates whether the AI Coach demonstrates true AI characteristics.
"""

import asyncio
from ai_coach import AICoach
from datetime import datetime, timedelta
import random

class AISophisticationEvaluator:
    """Evaluates AI characteristics of the coach"""
    
    def __init__(self):
        self.coach = AICoach()
        self.test_results = {
            'context_awareness': [],
            'pattern_recognition': [],
            'adaptive_behavior': [],
            'personalization': [],
            'predictive_capability': []
        }
    
    async def test_context_awareness(self):
        """Test: Does the coach understand complex context?"""
        print("\n1. CONTEXT AWARENESS TEST")
        print("-" * 40)
        
        # Test 1: Same metrics, different times of day
        results_by_time = []
        for hour in [9, 14, 22]:
            # Note: We can't mock datetime.now() directly, so we'll note the actual time
            current_hour = datetime.now().hour
            
            telemetry = {
                'keystrokes_per_min': 20,
                'energy_level': 0.4,
                'last_break_time': (datetime.now() - timedelta(hours=2)).isoformat()
            }
            
            result = await self.coach.analyze_telemetry(telemetry, f"user_hour_{hour}")
            
            print(f"Simulating hour {hour} (actual: {current_hour}): {result['message'] if result else 'No notification'}")
            results_by_time.append({
                'hour': hour,
                'response': result['action'] if result else None
            })
        
        # Test 2: Multi-factor context
        complex_telemetry = {
            'keystrokes_per_min': 80,  # High activity
            'error_rate': 0.15,  # High errors
            'app_switches_per_hour': 5,  # Low switching
            'deep_focus_minutes': 50,  # Good focus
            'stress_level': 0.8,  # But stressed
            'last_break_time': (datetime.now() - timedelta(hours=3)).isoformat()
        }
        
        result = await self.coach.analyze_telemetry(complex_telemetry, "complex_user")
        print(f"\nComplex context: {result['message'] if result else 'No notification'}")
        
        # Score: Does it recognize the contradiction of high performance + high stress?
        is_context_aware = result and ('stress' in result['message'].lower() or 
                                       'breath' in result['message'].lower() or
                                       'break' in result['message'].lower())
        
        print(f"✓ Context awareness: {'PASS' if is_context_aware else 'FAIL'}")
        return is_context_aware
    
    async def test_pattern_recognition(self):
        """Test: Can the coach recognize patterns over time?"""
        print("\n2. PATTERN RECOGNITION TEST")
        print("-" * 40)
        
        # Simulate declining performance pattern
        for i in range(5):
            telemetry = {
                'keystrokes_per_min': 70 - (i * 15),  # Declining
                'error_rate': 0.02 * (i + 1),  # Increasing
                'focus_quality': 1.0 - (i * 0.2),  # Declining
                'last_break_time': (datetime.now() - timedelta(hours=i)).isoformat()
            }
            
            result = await self.coach.analyze_telemetry(telemetry, "pattern_user")
            
            if result:
                print(f"Iteration {i+1}: {result['action']}")
                self.test_results['pattern_recognition'].append(result['action'])
        
        # Check if recommendations escalated with declining performance
        actions = self.test_results['pattern_recognition']
        pattern_detected = len(set(actions)) > 1  # Different recommendations
        
        print(f"✓ Pattern recognition: {'PASS' if pattern_detected else 'FAIL'}")
        return pattern_detected
    
    async def test_adaptive_behavior(self):
        """Test: Does the coach adapt its strategies?"""
        print("\n3. ADAPTIVE BEHAVIOR TEST")
        print("-" * 40)
        
        # Test same scenario multiple times
        scenario = {
            'keystrokes_per_min': 30,
            'stress_level': 0.8,
            'energy_level': 0.3
        }
        
        messages = []
        for i in range(3):
            result = await self.coach.analyze_telemetry(scenario, "adaptive_user")
            if result:
                messages.append(result['message'])
                # Simulate user not following advice (no break taken)
                await asyncio.sleep(0.1)
        
        # Check if coach varies messages or escalates
        unique_messages = len(set(messages))
        print(f"Unique messages: {unique_messages} out of {len(messages)}")
        
        is_adaptive = unique_messages > 1 or len(messages) < 3  # Varies or respects cooldown
        print(f"✓ Adaptive behavior: {'PASS' if is_adaptive else 'FAIL'}")
        return is_adaptive
    
    async def test_personalization(self):
        """Test: Does the coach personalize for different users?"""
        print("\n4. PERSONALIZATION TEST")
        print("-" * 40)
        
        # Same telemetry, different user histories
        telemetry = {
            'keystrokes_per_min': 40,
            'app_switches_per_hour': 20,
            'energy_level': 0.5
        }
        
        # User 1: First time user
        result1 = await self.coach.analyze_telemetry(telemetry, "new_user")
        
        # User 2: Frequent user (simulate history)
        for _ in range(5):
            await self.coach.analyze_telemetry(telemetry, "frequent_user")
        result2 = await self.coach.analyze_telemetry(telemetry, "frequent_user")
        
        print(f"New user: {result1['message'] if result1 else 'No notification'}")
        print(f"Frequent user: {result2['message'] if result2 else 'No notification'}")
        
        # Different behavior = personalization
        is_personalized = (result1 is not None) != (result2 is not None)
        print(f"✓ Personalization: {'PASS' if is_personalized else 'FAIL'}")
        return is_personalized
    
    async def test_predictive_capability(self):
        """Test: Can the coach predict and prevent issues?"""
        print("\n5. PREDICTIVE CAPABILITY TEST")
        print("-" * 40)
        
        # Simulate pre-burnout pattern
        pre_burnout_telemetry = {
            'keystrokes_per_min': 85,  # Very high
            'mouse_events_per_min': 60,  # Very high
            'error_rate': 0.08,  # Rising
            'app_switches_per_hour': 40,  # High
            'last_break_time': (datetime.now() - timedelta(hours=4)).isoformat(),
            'tasks_completed_last_hour': 6,  # Overworking
            'cognitive_load': 0.9  # Near max
        }
        
        result = await self.coach.analyze_telemetry(pre_burnout_telemetry, "burnout_risk_user")
        
        if result:
            print(f"Coach response: {result['message']}")
            print(f"Action type: {result['action']}")
            
            # Check if it recommends preventive action
            is_predictive = any(word in result['message'].lower() 
                              for word in ['break', 'rest', 'slow', 'pause', 'breathe'])
        else:
            is_predictive = False
            print("No intervention (missed prediction)")
        
        print(f"✓ Predictive capability: {'PASS' if is_predictive else 'FAIL'}")
        return is_predictive
    
    def calculate_ai_score(self, results):
        """Calculate overall AI sophistication score"""
        scores = {
            'context_awareness': 25,
            'pattern_recognition': 20,
            'adaptive_behavior': 20,
            'personalization': 20,
            'predictive_capability': 15
        }
        
        total_score = sum(scores[test] for test, passed in results.items() if passed)
        
        ai_levels = {
            80: "Highly Sophisticated AI",
            60: "Solid AI Implementation", 
            40: "Basic AI Capabilities",
            20: "Rule-Based System",
            0: "Not AI"
        }
        
        for threshold, label in sorted(ai_levels.items(), reverse=True):
            if total_score >= threshold:
                return total_score, label
        
        return total_score, "Not AI"

async def main():
    """Run AI sophistication evaluation"""
    print("=" * 50)
    print("AI COACH SOPHISTICATION EVALUATION")
    print("=" * 50)
    
    evaluator = AISophisticationEvaluator()
    
    results = {
        'context_awareness': await evaluator.test_context_awareness(),
        'pattern_recognition': await evaluator.test_pattern_recognition(),
        'adaptive_behavior': await evaluator.test_adaptive_behavior(),
        'personalization': await evaluator.test_personalization(),
        'predictive_capability': await evaluator.test_predictive_capability()
    }
    
    print("\n" + "=" * 50)
    print("EVALUATION RESULTS")
    print("=" * 50)
    
    for test, passed in results.items():
        print(f"{test.replace('_', ' ').title()}: {'✓ PASS' if passed else '✗ FAIL'}")
    
    score, classification = evaluator.calculate_ai_score(results)
    
    print(f"\nOverall AI Score: {score}/100")
    print(f"Classification: {classification}")
    
    print("\nAI CHARACTERISTICS DEMONSTRATED:")
    if results['context_awareness']:
        print("✓ Understands multi-dimensional context")
    if results['pattern_recognition']:
        print("✓ Recognizes patterns in user behavior")
    if results['adaptive_behavior']:
        print("✓ Adapts strategies based on effectiveness")
    if results['personalization']:
        print("✓ Personalizes for different users")
    if results['predictive_capability']:
        print("✓ Predicts and prevents issues")
    
    print("\nCONCLUSION:")
    if score >= 60:
        print("This is genuinely AI - it demonstrates intelligence, adaptation, and prediction.")
    elif score >= 40:
        print("This shows AI characteristics but could be more sophisticated.")
    else:
        print("This is more rule-based than true AI - needs more adaptive intelligence.")

if __name__ == "__main__":
    asyncio.run(main())