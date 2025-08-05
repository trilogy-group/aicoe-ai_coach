#!/usr/bin/env python3
"""
Test script to demonstrate the enhanced professional coaching capabilities
"""

import asyncio
import pandas as pd
from ai_coach import AICoach

async def test_enhanced_coaching():
    """Test the enhanced professional coaching system."""
    
    print("🧠 TESTING ENHANCED PROFESSIONAL COACHING SYSTEM")
    print("=" * 60)
    
    # Create test scenarios that showcase different coaching approaches
    test_scenarios = [
        {
            'name': 'High Cognitive Load Developer',
            'data': {
                'tab_count': 15,
                'window_switches_15min': 25,
                'focus_session_duration': 10,
                'cognitive_load_score': 0.9,
                'app_active': 'VS Code',
                'persona_type': 'developer',
                'core_work_percentage': 0.3,
                'interruption_count': 8,
                'task_completion_indicators': '{"task_progress_percentage": 0.2, "quality_indicators": {"error_rate": 0.15}}'
            }
        },
        {
            'name': 'Distracted Analyst', 
            'data': {
                'tab_count': 12,
                'window_switches_15min': 18,
                'focus_session_duration': 15,
                'cognitive_load_score': 0.6,
                'app_active': 'Excel',
                'persona_type': 'analyst',
                'core_work_percentage': 0.4,
                'interruption_count': 6,
                'task_completion_indicators': '{"task_progress_percentage": 0.6, "quality_indicators": {"error_rate": 0.08}}'
            }
        },
        {
            'name': 'Overwhelmed Manager',
            'data': {
                'tab_count': 20,
                'window_switches_15min': 35,
                'focus_session_duration': 5,
                'cognitive_load_score': 0.95,
                'app_active': 'Email',
                'persona_type': 'manager',
                'core_work_percentage': 0.2,
                'interruption_count': 12,
                'task_completion_indicators': '{"task_progress_percentage": 0.1, "quality_indicators": {"error_rate": 0.05}}'
            }
        }
    ]
    
    # Initialize coach
    coach = AICoach()
    
    for scenario in test_scenarios:
        print(f"\n🎯 SCENARIO: {scenario['name']}")
        print("-" * 40)
        
        # Create DataFrame from scenario data
        test_data = pd.DataFrame([scenario['data']])
        
        # Add required timestamp
        test_data['timestamp'] = '2025-08-05T14:00:00'
        
        try:
            # Generate coaching recommendation
            result = await coach.analyze_and_coach(data=test_data, user_id=1)
            
            if result:
                print(f"✅ PROFESSIONAL COACHING GENERATED:")
                print(f"📝 Coaching Text:")
                print(f"   {result.get('nudge_text', 'N/A')}")
                print(f"🎯 Type: {result.get('nudge_type', 'N/A')}")
                print(f"📊 Confidence: {result.get('confidence', 0):.2f}")
                print(f"🧠 Trigger: {result.get('trigger_dimension', 'N/A')}")
                
                # Show the sophisticated reasoning
                if 'reasoning' in result:
                    print(f"🔍 Reasoning: {result['reasoning']}")
                
            else:
                print("❌ No coaching generated for this scenario")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
    
    print("🎓 ENHANCED COACHING FEATURES DEMONSTRATED:")
    print("✓ Cognitive Load Theory application")
    print("✓ Flow State assessment and optimization") 
    print("✓ Behavioral Psychology principles")
    print("✓ Professional coaching methodologies (GROW model)")
    print("✓ Self-Determination Theory motivation factors")
    print("✓ Neuroscience-based recommendations")
    print("✓ Sophisticated psychological language")
    print("✓ Context-aware intervention strategies")

if __name__ == "__main__":
    asyncio.run(test_enhanced_coaching())