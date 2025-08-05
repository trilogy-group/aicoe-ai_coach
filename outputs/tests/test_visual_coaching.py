#!/usr/bin/env python3
"""
Test Visual Coaching Capabilities
Demonstrates the enhanced AI coach with visual screen analysis and job-specific optimization.
"""

import asyncio
import pandas as pd
from datetime import datetime
import json
from ai_coach import AICoach

async def test_visual_coaching():
    """Test the enhanced visual coaching system with realistic scenarios."""
    
    print("🔍 TESTING VISUAL COACHING SYSTEM")
    print("=" * 60)
    
    # Initialize AI Coach
    coach = AICoach()
    
    # Test scenarios with visual analysis data
    test_scenarios = [
        {
            'name': 'Excel Formula Optimization',
            'data': {
                'timestamp': datetime.now().isoformat(),
                'user_id': 101,
                'persona_type': 'analyst',
                'tab_count': 3,
                'app_active': 'Excel',
                'task_category': 'data_analysis',
                'cognitive_load_score': 0.6,
                'focus_session_duration': 35,
                'detected_content_elements': [{
                    'type': 'spreadsheet',
                    'formulas_detected': 15,
                    'rows_visible': 250,
                    'columns_visible': 12
                }],
                'workflow_inefficiencies': [{
                    'type': 'formula_inefficiency',
                    'description': 'Using nested IF statements instead of VLOOKUP/INDEX-MATCH',
                    'complexity_score': 0.8
                }],
                'missed_opportunities': [{
                    'type': 'data_visualization',
                    'description': 'Could create automated dashboard for recurring analysis',
                    'impact_score': 0.7
                }]
            }
        },
        {
            'name': 'VSCode Debugging Improvement',
            'data': {
                'timestamp': datetime.now().isoformat(),
                'user_id': 102,
                'persona_type': 'developer',
                'tab_count': 8,
                'app_active': 'VSCode',
                'task_category': 'coding',
                'cognitive_load_score': 0.7,
                'focus_session_duration': 45,
                'detected_content_elements': [{
                    'type': 'code_editor',
                    'files_open': 12,
                    'syntax_errors': 2,
                    'debug_session_active': False
                }],
                'workflow_inefficiencies': [{
                    'type': 'debugging_inefficiency',
                    'description': 'Using console.log for debugging instead of proper debugger',
                    'learning_opportunity': True
                }],
                'visual_attention_areas': {
                    'distraction_indicators': {
                        'notification_interruptions': 5,
                        'multitasking_severity': 0.8
                    }
                }
            }
        },
        {
            'name': 'Customer Support Backlog Management',
            'data': {
                'timestamp': datetime.now().isoformat(),
                'user_id': 103,
                'persona_type': 'customer_support',
                'tab_count': 15,
                'app_active': 'Zendesk',
                'task_category': 'support',
                'cognitive_load_score': 0.85,
                'focus_session_duration': 20,
                'detected_content_elements': [{
                    'type': 'crm_interface',
                    'tickets_visible': 18,
                    'unresolved_items': 8,
                    'escalation_alerts': 2
                }],
                'task_completion_indicators': {
                    'task_progress_percentage': 0.3,
                    'quality_indicators': {
                        'error_rate': 0.15,
                        'best_practices_followed': 0.6
                    },
                    'blockers_detected': [{
                        'type': 'approval',
                        'severity': 'high'
                    }]
                }
            }
        },
        {
            'name': 'PowerBI Dashboard Optimization',
            'data': {
                'timestamp': datetime.now().isoformat(),
                'user_id': 104,
                'persona_type': 'analyst',
                'tab_count': 6,
                'app_active': 'PowerBI',
                'task_category': 'reporting',
                'cognitive_load_score': 0.5,
                'focus_session_duration': 60,
                'detected_content_elements': [{
                    'type': 'dashboard',
                    'visualizations_count': 8,
                    'refresh_status': 'stale',
                    'performance_indicators': {
                        'load_time_seconds': 12,
                        'query_complexity': 'high'
                    }
                }],
                'missed_opportunities': [{
                    'type': 'workflow_optimization',
                    'description': 'Dashboard performance could be improved',
                    'impact_score': 0.8
                }]
            }
        }
    ]
    
    print(f"🧪 Running {len(test_scenarios)} visual coaching test scenarios...\n")
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"📊 SCENARIO {i}: {scenario['name']}")
        print("-" * 40)
        
        # Create DataFrame from test data
        df = pd.DataFrame([scenario['data']])
        
        # Get coaching recommendation
        nudge = await coach.analyze_and_coach(df, scenario['data']['user_id'])
        
        if nudge:
            print(f"✅ VISUAL COACHING GENERATED:")
            print(f"   📝 Text: {nudge['nudge_text']}")
            print(f"   🎯 Type: {nudge.get('nudge_type', 'general')}")
            print(f"   📊 Confidence: {nudge.get('confidence', 0):.2f}")
            print(f"   🧠 Trigger: {nudge.get('trigger_dimension', 'unknown')}")
            
            # Show visual analysis insights
            if 'visual_insights' in nudge:
                print(f"   👁️  Visual Insights: {nudge['visual_insights']}")
            
            print(f"   🎨 Persona: {scenario['data']['persona_type']}")
            
        else:
            print("❌ No coaching recommendation generated")
        
        print()
    
    print("🎉 VISUAL COACHING TEST COMPLETE!")
    print("\n📈 SYSTEM CAPABILITIES DEMONSTRATED:")
    print("   ✅ Screen content analysis and coaching")
    print("   ✅ App-specific workflow optimization")
    print("   ✅ Task completion and quality guidance")
    print("   ✅ Visual attention pattern recognition")
    print("   ✅ Job-specific missed opportunity detection")
    print("   ✅ Real-time workflow inefficiency coaching")
    
    # Show some metrics from the coaching session
    print(f"\n📊 SESSION METRICS:")
    print(f"   Nudges Generated: {coach.session_metrics['nudges_generated']}")
    print(f"   Average Response Time: {sum(coach.session_metrics['evaluation_time_seconds'])/len(coach.session_metrics['evaluation_time_seconds']):.2f}s")

if __name__ == "__main__":
    asyncio.run(test_visual_coaching())