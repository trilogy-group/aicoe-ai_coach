#!/bin/bash
# Overnight AI Coach Evolution Runner
# Runs multiple evolution processes in parallel for maximum improvement speed

echo "🌙 Starting Overnight AI Coach Evolution"
echo "Starting at: $(date)"

# Kill any existing evolution processes
pkill -f ai_coach_evolution.py
pkill -f rapid_evolution.py
sleep 3

# Create logs directory
mkdir -p logs

# Start multiple evolution processes in parallel
echo "🚀 Starting Rapid Evolution (200 cycles)..."
nohup python rapid_evolution.py ai_coach.py 200 > logs/rapid_evolution_overnight.log 2>&1 &
RAPID_PID=$!

echo "🔬 Starting Standard Evolution (100 generations, 15 population)..."
nohup python ai_coach_evolution.py ai_coach.py 100 15 > logs/standard_evolution_overnight.log 2>&1 &
STANDARD_PID=$!

# Create a monitoring script
cat > overnight_monitor.py << 'EOF'
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
EOF

# Start the monitoring script
echo "📊 Starting overnight monitor..."
nohup python overnight_monitor.py > logs/overnight_monitor.log 2>&1 &
MONITOR_PID=$!

# Save PIDs for reference
echo "Process IDs:"
echo "Rapid Evolution PID: $RAPID_PID" | tee logs/pids.txt
echo "Standard Evolution PID: $STANDARD_PID" | tee -a logs/pids.txt  
echo "Monitor PID: $MONITOR_PID" | tee -a logs/pids.txt

echo ""
echo "🌙 Overnight evolution started successfully!"
echo "📋 Monitor progress with: tail -f logs/overnight_monitor.log"
echo "🚀 Check rapid evolution: tail -f logs/rapid_evolution_overnight.log"
echo "🔬 Check standard evolution: tail -f logs/standard_evolution_overnight.log"
echo ""
echo "🛑 To stop all processes: pkill -f evolution"
echo "📊 Check status: cat logs/overnight_status.json"
echo ""
echo "Evolution will run continuously until completion or manual stop."
echo "Expected runtime: 8-12 hours for full optimization cycle."