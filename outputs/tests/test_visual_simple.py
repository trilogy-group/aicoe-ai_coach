#!/usr/bin/env python3
"""
Simple Visual Coaching Test
Direct test of visual analysis nudge generation.
"""

import pandas as pd
from datetime import datetime
from ai_coach import AICoach

def test_visual_nudges():
    """Test visual analysis nudge generation directly."""
    
    print("🔍 TESTING VISUAL NUDGE GENERATION")
    print("=" * 50)
    
    coach = AICoach()
    
    # Test context with visual analysis flags
    test_contexts = [
        {
            'name': 'Formula Optimization',
            'context': {
                'flags': ['formula_optimization_needed'],
                'app_active': 'Excel',
                'detected_content_elements': [{'type': 'spreadsheet', 'formulas_detected': 5}]
            }
        },
        {
            'name': 'Manual Calculation',
            'context': {
                'flags': ['manual_calculation_detected'],
                'app_active': 'Excel',
                'detected_content_elements': [{'type': 'spreadsheet', 'rows_visible': 100, 'formulas_detected': 0}]
            }
        },
        {
            'name': 'Too Many Files',
            'context': {
                'flags': ['too_many_files_open'],
                'app_active': 'VSCode',
                'detected_content_elements': [{'type': 'code_editor', 'files_open': 15}]
            }
        },
        {
            'name': 'Syntax Errors',
            'context': {
                'flags': ['syntax_errors_present'],
                'app_active': 'VSCode',
                'detected_content_elements': [{'type': 'code_editor', 'syntax_errors': 3}]
            }
        },
        {
            'name': 'Notification Overload',
            'context': {
                'flags': ['notification_overload'],
                'visual_attention_areas': {
                    'distraction_indicators': {'notification_interruptions': 7}
                }
            }
        },
        {
            'name': 'High Error Rate',
            'context': {
                'flags': ['high_error_rate'],
                'task_completion_indicators': {
                    'quality_indicators': {'error_rate': 0.15}
                }
            }
        },
        {
            'name': 'CRM Backlog',
            'context': {
                'flags': ['backlog_accumulation'],
                'detected_content_elements': [{'type': 'crm_interface', 'unresolved_items': 12}]
            }
        }
    ]
    
    for test in test_contexts:
        print(f"\n📊 {test['name']}:")
        nudge_text = coach._generate_visual_analysis_nudge(test['context'])
        if nudge_text:
            print(f"   ✅ {nudge_text}")
        else:
            print(f"   ❌ No visual nudge generated")
    
    print(f"\n🎉 Visual nudge generation test complete!")

if __name__ == "__main__":
    test_visual_nudges()