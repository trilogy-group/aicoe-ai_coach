#!/usr/bin/env python3
import time
import json
import os
from datetime import datetime
import subprocess

def get_process_status(pid):
    try:
        result = subprocess.run(['ps', '-p', str(pid)], capture_output=True, text=True)
        return len(result.stdout.strip().split('\n')) > 1
    except:
        return False

def monitor_overnight():
    rapid_pid = None
    standard_pid = None
    
    # Try to find running processes
    try:
        result = subprocess.run(['pgrep', '-f', 'rapid_evolution.py'], capture_output=True, text=True)
        if result.stdout.strip():
            rapid_pid = int(result.stdout.strip().split('\n')[0])
    except:
        pass
    
    try:
        result = subprocess.run(['pgrep', '-f', 'ai_coach_evolution.py'], capture_output=True, text=True)
        if result.stdout.strip():
            standard_pid = int(result.stdout.strip().split('\n')[0])
    except:
        pass
    
    start_time = datetime.now()
    
    while True:
        current_time = datetime.now()
        runtime = current_time - start_time
        
        rapid_running = rapid_pid and get_process_status(rapid_pid)
        standard_running = standard_pid and get_process_status(standard_pid)
        
        status = {
            'timestamp': current_time.isoformat(),
            'runtime_hours': runtime.total_seconds() / 3600,
            'rapid_evolution_running': rapid_running,
            'standard_evolution_running': standard_running,
            'rapid_pid': rapid_pid,
            'standard_pid': standard_pid
        }
        
        # Save status
        with open('logs/overnight_status.json', 'w') as f:
            json.dump(status, f, indent=2)
        
        print(f"[{current_time.strftime('%H:%M:%S')}] Runtime: {runtime.total_seconds()/3600:.1f}h | Rapid: {'✅' if rapid_running else '❌'} | Standard: {'✅' if standard_running else '❌'}")
        
        # If both processes stopped, we're done
        if not rapid_running and not standard_running:
            print("🏁 All evolution processes completed!")
            break
        
        # Check every 5 minutes
        time.sleep(300)

if __name__ == "__main__":
    monitor_overnight()
