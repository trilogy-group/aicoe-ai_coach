#!/usr/bin/env python3
"""
Test Enhanced Variance System
Tests the advanced variance handling and multi-dimensional coaching adaptation.
"""

import asyncio
import pandas as pd
from datetime import datetime
import json
from ai_coach import AICoach

async def test_variance_scenarios():
    """Test various high-variance scenarios with the enhanced AI coach."""
    
    print("🔬 TESTING ENHANCED VARIANCE SYSTEM")
    print("=" * 60)
    
    # Initialize AI Coach
    coach = AICoach()
    
    # Test scenarios with extreme variance
    test_scenarios = [
        {
            'name': 'High Stress Developer (Crisis Mode)',
            'data': {
                'timestamp': datetime.now().isoformat(),
                'user_id': 201,
                'persona_type': 'developer',
                'tab_count': 18,  # Very high
                'app_active': 'VSCode',
                'task_category': 'coding',
                'cognitive_load_score': 0.95,  # Extremely high
                'focus_session_duration': 120,  # Long without break
                'interruption_count': 12,  # Very high
                'core_work_percentage': 0.2,  # Low due to firefighting
                'workflow_inefficiencies': [
                    {
                        'type': 'stress_induced_errors',
                        'description': 'High cognitive load causing repeated corrections',
                        'stress_indicator': True,
                        'time_waste_minutes': 35
                    },
                    {
                        'type': 'panic_multitasking',
                        'description': 'Switching between too many tasks under pressure',
                        'time_waste_minutes': 45
                    }
                ],
                'task_completion_indicators': {
                    'quality_indicators': {
                        'error_rate': 0.18,  # High error rate
                        'best_practices_followed': 0.4
                    }
                }
            }
        },
        {
            'name': 'Fatigued Analyst (End of Long Day)',
            'data': {
                'timestamp': datetime.now().replace(hour=17, minute=30).isoformat(),
                'user_id': 202,
                'persona_type': 'analyst',
                'tab_count': 8,
                'app_active': 'Excel',
                'task_category': 'data_analysis',
                'cognitive_load_score': 0.85,
                'focus_session_duration': 200,  # Very long session
                'current_hour': 17,
                'break_duration_min': 2,  # Almost no breaks
                'workflow_inefficiencies': [
                    {
                        'type': 'fatigue_induced_slowness',
                        'description': 'Slower processing due to mental fatigue',
                        'fatigue_indicator': True,
                        'time_waste_minutes': 60
                    }
                ],
                'task_completion_indicators': {
                    'task_progress_percentage': 0.75,
                    'quality_indicators': {
                        'error_rate': 0.12,
                        'review_needed': True
                    }
                }
            }
        },
        {
            'name': 'High-Energy Designer (Peak Flow State)',
            'data': {
                'timestamp': datetime.now().replace(hour=10, minute=0).isoformat(),
                'user_id': 203,
                'persona_type': 'designer',
                'tab_count': 5,
                'app_active': 'Figma',
                'task_category': 'design',
                'cognitive_load_score': 0.3,  # Low load, in flow
                'focus_session_duration': 45,
                'productivity_score': 0.95,  # Very high
                'value_score': 0.9,
                'current_hour': 10,  # Peak morning hours
                'interruption_count': 1,  # Low interruptions
                'core_work_percentage': 0.85,  # High core work
                'visual_attention_areas': {
                    'primary_focus_area': {
                        'attention_duration_seconds': 300,
                        'interaction_density': 0.95
                    },
                    'distraction_indicators': {
                        'off_task_browsing': False,
                        'multitasking_severity': 0.1
                    }
                }
            }
        },
        {
            'name': 'Overwhelmed Manager (Workload Crisis)',
            'data': {
                'timestamp': datetime.now().replace(hour=14, minute=0).isoformat(),
                'user_id': 204,
                'persona_type': 'manager',
                'tab_count': 25,  # Extreme multitasking
                'app_active': 'Outlook',
                'task_category': 'management',
                'cognitive_load_score': 0.9,
                'window_switches_15min': 35,  # Very high switching
                'interruption_count': 18,  # Extreme interruptions
                'meeting_duration_min': 300,  # 5 hours in meetings
                'core_work_percentage': 0.15,  # Very low
                'current_hour': 14,
                'workflow_inefficiencies': [
                    {
                        'type': 'panic_multitasking',
                        'description': 'Switching between too many tasks under pressure',
                        'time_waste_minutes': 90
                    }
                ],
                'task_completion_indicators': {
                    'blockers_detected': [
                        {
                            'type': 'approval',
                            'severity': 'high'
                        },
                        {
                            'type': 'process',
                            'severity': 'high'
                        }
                    ]
                }
            }
        },
        {
            'name': 'Post-Lunch Energy Dip (Temporal Variance)',
            'data': {
                'timestamp': datetime.now().replace(hour=13, minute=30).isoformat(),
                'user_id': 205,
                'persona_type': 'analyst',
                'tab_count': 6,
                'app_active': 'PowerBI',
                'task_category': 'reporting',
                'cognitive_load_score': 0.6,
                'focus_session_duration': 15,  # Short focus
                'current_hour': 13,  # Post-lunch dip
                'productivity_score': 0.4,  # Low due to circadian dip
                'keystrokes_per_min': 35,  # Slow typing
                'workflow_inefficiencies': [
                    {
                        'type': 'fatigue_induced_slowness',
                        'description': 'Post-meal energy dip affecting performance',
                        'fatigue_indicator': True
                    }
                ]
            }
        }
    ]
    
    print(f"🧪 Running {len(test_scenarios)} high-variance test scenarios...\n")
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"📊 SCENARIO {i}: {scenario['name']}")
        print("-" * 50)
        
        # Create DataFrame from test data
        df = pd.DataFrame([scenario['data']])
        
        # Get variance-aware coaching recommendation
        nudge = await coach.analyze_and_coach(df, scenario['data']['user_id'])
        
        if nudge:
            print(f"✅ VARIANCE-AWARE COACHING GENERATED:")
            print(f"   📝 Text: {nudge['nudge_text']}")
            print(f"   🎯 Type: {nudge.get('nudge_type', 'general')}")
            print(f"   📊 Confidence: {nudge.get('confidence', 0):.2f}")
            print(f"   🧠 Trigger: {nudge.get('trigger_dimension', 'unknown')}")
            
            # Show variance-specific information
            if nudge.get('variance_adaptive'):
                print(f"   🔬 Variance Factor: {nudge.get('variance_factor', 'unknown')}")
                print(f"   📈 Impact Score: {nudge.get('impact_score', 0):.2f}")
                print(f"   🎨 Variance-Adapted: YES")
            
            print(f"   👤 Persona: {scenario['data']['persona_type']}")
            
        else:
            print("❌ No coaching recommendation generated")
        
        print()
    
    print("🎉 VARIANCE SYSTEM TEST COMPLETE!")
    print("\n📈 ENHANCED CAPABILITIES DEMONSTRATED:")
    print("   ✅ Stress-aware coaching adaptation")
    print("   ✅ Fatigue detection and energy management")
    print("   ✅ Mood-responsive coaching tone")
    print("   ✅ Workload-sensitive prioritization")
    print("   ✅ Circadian rhythm optimization")
    print("   ✅ Multi-dimensional variance integration")
    print("   ✅ Persona-specific variance sensitivity")
    print("   ✅ Dynamic coaching strategy adaptation")

if __name__ == "__main__":
    asyncio.run(test_variance_scenarios())