#!/usr/bin/env python3
"""
Simple AI Coach Usage Example
============================

Shows how to use the AI Coach with telemetry data.
"""

import asyncio
from ai_coach import AICoach, coach_me
from datetime import datetime, timedelta

async def example_1_basic():
    """Example 1: Most basic usage"""
    print("Example 1: Basic Usage")
    print("-" * 30)
    
    # Minimal telemetry - just keystroke data
    telemetry = {
        'keystrokes_per_min': 15,  # Low activity
        'app_switches_per_hour': 45  # High context switching
    }
    
    # Get coaching
    notification = await coach_me(telemetry)
    
    if notification:
        print(f"Coach says: {notification['message']}")
    else:
        print("No coaching needed")
    print()

async def example_2_detailed():
    """Example 2: Detailed telemetry"""
    print("Example 2: Detailed Telemetry")
    print("-" * 30)
    
    coach = AICoach()
    
    # Rich telemetry data
    telemetry = {
        # Time tracking
        'last_break_time': (datetime.now() - timedelta(hours=3)).isoformat(),
        
        # Activity metrics
        'keystrokes_per_min': 65,
        'mouse_events_per_min': 30,
        'app_switches_per_hour': 15,
        
        # Productivity metrics
        'tasks_completed_last_hour': 4,
        'deep_focus_minutes': 45,
        'lines_of_code_written': 200,
        'primary_app_time_percentage': 85,
        
        # Stress indicators
        'error_rate': 0.02,
        'backspace_rate': 0.05,
        
        # Physical wellness
        'posture_quality': 0.4,  # Poor posture
        'mouse_distance_traveled': 15000  # High activity
    }
    
    notification = await coach.analyze_telemetry(telemetry, user_id="power_user")
    
    if notification:
        print(f"Coach says: {notification['message']}")
        print(f"Recommended action: {notification['action']} for {notification['suggested_duration']} minutes")
        print(f"Your current state:")
        for metric, value in notification['context'].items():
            print(f"  - {metric}: {value}")
    print()

async def example_3_continuous():
    """Example 3: Continuous monitoring simulation"""
    print("Example 3: Continuous Monitoring (5 iterations)")
    print("-" * 30)
    
    coach = AICoach()
    
    # Simulate changing conditions over time
    for hour in range(5):
        print(f"\nHour {hour + 1}:")
        
        telemetry = {
            'last_break_time': (datetime.now() - timedelta(hours=hour)).isoformat(),
            'keystrokes_per_min': 70 - (hour * 10),  # Decreasing activity
            'error_rate': 0.01 * (hour + 1),  # Increasing errors
            'app_switches_per_hour': 10 + (hour * 10),  # Increasing distractions
            'deep_focus_minutes': max(0, 60 - (hour * 15)),  # Decreasing focus
            'stress_level': min(1.0, 0.2 + (hour * 0.2))  # Increasing stress
        }
        
        notification = await coach.analyze_telemetry(telemetry, user_id="test_user")
        
        if notification:
            print(f"  Coach: {notification['message']}")
        else:
            print(f"  Coach: Keep going!")
        
        # Simulate time passing (in real usage, this would be actual time)
        await asyncio.sleep(1)

async def example_4_config():
    """Example 4: Using configuration"""
    print("\nExample 4: Custom Configuration")
    print("-" * 30)
    
    # First create a config file
    import json
    config = {
        "notification_cooldown_minutes": 15,  # More frequent notifications
        "quiet_hours": [[22, 6], [12, 13]]  # No notifications 10pm-6am and 12pm-1pm
    }
    
    with open("coach_config.json", "w") as f:
        json.dump(config, f)
    
    # Use coach with config
    coach = AICoach(config_path="coach_config.json")
    
    telemetry = {
        'keystrokes_per_min': 10,
        'last_break_time': (datetime.now() - timedelta(hours=4)).isoformat()
    }
    
    notification = await coach.analyze_telemetry(telemetry)
    
    if notification:
        print(f"Coach says: {notification['message']}")
    
    # Clean up
    import os
    os.remove("coach_config.json")

async def main():
    """Run all examples"""
    await example_1_basic()
    await example_2_detailed()
    await example_3_continuous()
    await example_4_config()
    
    print("\n" + "=" * 50)
    print("AI Coach Examples Complete!")
    print("Integration tips:")
    print("1. Collect telemetry from your monitoring tools")
    print("2. Call coach.analyze_telemetry() periodically")
    print("3. Display notifications to users when returned")
    print("4. Track effectiveness and provide feedback")

if __name__ == "__main__":
    asyncio.run(main())