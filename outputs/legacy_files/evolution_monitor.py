#!/usr/bin/env python3
"""
Evolution Monitor - Real-time tracking of AI Coach evolution progress
Monitors evolution process and provides insights into improvement patterns
"""

import json
import time
import os
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict
import subprocess
import signal
import sys

class EvolutionMonitor:
    def __init__(self):
        self.results_file = "/Users/stanhus/Documents/work/ai_coach/outputs/coaching_evaluation_results.json"
        self.evolution_summary_file = "/Users/stanhus/Documents/work/ai_coach/outputs/evolved_coaches/evolution_summary.json"
        self.log_file = "/Users/stanhus/Documents/work/ai_coach/evolution_log.txt"
        
    def load_results(self) -> List[Dict]:
        """Load evaluation results"""
        try:
            with open(self.results_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def load_evolution_summary(self) -> Dict:
        """Load evolution summary if available"""
        try:
            with open(self.evolution_summary_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def get_latest_log_lines(self, num_lines: int = 10) -> List[str]:
        """Get latest lines from evolution log"""
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
                return lines[-num_lines:] if lines else []
        except FileNotFoundError:
            return []
    
    def analyze_progress(self) -> Dict:
        """Analyze evolution progress"""
        results = self.load_results()
        
        if not results:
            return {"status": "no_data", "message": "No evaluation results found"}
        
        # Group by generation if available
        fitness_scores = []
        timestamps = []
        best_scores = []
        
        for result in results:
            fitness = result['metrics'].get('composite_fitness', -1.0)
            timestamp = datetime.fromisoformat(result['timestamp'])
            
            fitness_scores.append(fitness)
            timestamps.append(timestamp)
        
        # Calculate statistics
        current_best = max(fitness_scores) if fitness_scores else -1.0
        avg_fitness = sum(fitness_scores) / len(fitness_scores) if fitness_scores else -1.0
        improvement_trend = fitness_scores[-10:] if len(fitness_scores) >= 10 else fitness_scores
        
        # Check if evolution is running
        evolution_active = self.check_evolution_process()
        
        return {
            "status": "active" if evolution_active else "completed",
            "current_best_fitness": current_best,
            "average_fitness": avg_fitness,
            "total_evaluations": len(results),
            "improvement_trend": improvement_trend,
            "latest_timestamp": timestamps[-1].isoformat() if timestamps else None,
            "evolution_active": evolution_active
        }
    
    def check_evolution_process(self) -> bool:
        """Check if evolution process is still running"""
        try:
            result = subprocess.run(['pgrep', '-f', 'ai_coach_evolution.py'], 
                                  capture_output=True, text=True)
            return len(result.stdout.strip()) > 0
        except:
            return False
    
    def display_status(self):
        """Display current evolution status"""
        progress = self.analyze_progress()
        
        print(f"\n{'='*60}")
        print(f"AI COACH EVOLUTION MONITOR")
        print(f"{'='*60}")
        print(f"Status: {progress['status'].upper()}")
        print(f"Best Fitness: {progress['current_best_fitness']:.4f}")
        print(f"Average Fitness: {progress['average_fitness']:.4f}") 
        print(f"Total Evaluations: {progress['total_evaluations']}")
        print(f"Evolution Active: {progress['evolution_active']}")
        
        if progress['latest_timestamp']:
            print(f"Last Update: {progress['latest_timestamp']}")
        
        # Show recent log lines
        recent_logs = self.get_latest_log_lines(5)
        if recent_logs:
            print(f"\nRecent Activity:")
            for line in recent_logs:
                print(f"  {line.strip()}")
        
        # Show improvement trend
        if len(progress['improvement_trend']) > 1:
            trend = progress['improvement_trend']
            trend_direction = "↗️" if trend[-1] > trend[0] else "↘️" if trend[-1] < trend[0] else "→"
            print(f"\nFitness Trend: {trend_direction} ({trend[0]:.4f} → {trend[-1]:.4f})")
        
        print(f"{'='*60}\n")
    
    def restart_evolution_if_needed(self):
        """Restart evolution if it's not running and should be"""
        if not self.check_evolution_process():
            print("Evolution process not running. Restarting...")
            
            # Kill any zombie processes
            try:
                subprocess.run(['pkill', '-f', 'ai_coach_evolution.py'], 
                             capture_output=True)
                time.sleep(2)
            except:
                pass
            
            # Start new evolution process
            cmd = ['nohup', 'python', 'ai_coach_evolution.py', 'ai_coach.py', '50', '20']
            with open('evolution_log.txt', 'a') as log_file:
                subprocess.Popen(cmd, stdout=log_file, stderr=log_file)
            
            print("Evolution process restarted!")
            time.sleep(5)  # Give it time to start
    
    def optimize_evolution_parameters(self):
        """Analyze results and suggest parameter optimizations"""
        results = self.load_results()
        
        if len(results) < 20:  # Need enough data
            return
        
        # Analyze fitness distribution
        fitness_scores = [r['metrics'].get('composite_fitness', -1.0) for r in results[-20:]]
        
        # If too many failures, reduce population size
        failure_rate = sum(1 for f in fitness_scores if f <= -1.0) / len(fitness_scores)
        
        if failure_rate > 0.8:
            print("High failure rate detected. Consider:")
            print("- Reducing population size")
            print("- Simplifying evolution prompts")
            print("- Checking for data format issues")
        
        # If good improvement, consider increasing parameters
        elif failure_rate < 0.2 and len(set(fitness_scores)) > 1:
            recent_best = max(fitness_scores)
            if recent_best > -0.5:
                print("Good progress detected. Consider:")
                print("- Increasing population size for more diversity")
                print("- Adding more generations")
    
    def continuous_monitor(self, check_interval: int = 30):
        """Continuously monitor evolution progress"""
        print("Starting continuous evolution monitoring...")
        print(f"Checking every {check_interval} seconds")
        print("Press Ctrl+C to stop monitoring\n")
        
        try:
            iteration = 0
            while True:
                iteration += 1
                print(f"\n--- Monitor Check #{iteration} ---")
                
                # Display current status
                self.display_status()
                
                # Restart if needed
                self.restart_evolution_if_needed()
                
                # Analyze and optimize if we have enough data
                if iteration % 10 == 0:  # Every 10 iterations
                    self.optimize_evolution_parameters()
                
                # Wait for next check
                time.sleep(check_interval)
                
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped by user.")
            
            # Ask if user wants to keep evolution running
            try:
                keep_running = input("Keep evolution process running? (y/N): ").lower().strip()
                if keep_running != 'y':
                    print("Stopping evolution process...")
                    subprocess.run(['pkill', '-f', 'ai_coach_evolution.py'], 
                                 capture_output=True)
                    print("Evolution stopped.")
                else:
                    print("Evolution continues running in background.")
            except KeyboardInterrupt:
                print("\nForce stopping evolution...")
                subprocess.run(['pkill', '-f', 'ai_coach_evolution.py'], 
                             capture_output=True)


def main():
    monitor = EvolutionMonitor()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "status":
            monitor.display_status()
        elif sys.argv[1] == "restart":
            monitor.restart_evolution_if_needed()
        elif sys.argv[1] == "stop":
            subprocess.run(['pkill', '-f', 'ai_coach_evolution.py'])
            print("Evolution process stopped.")
        else:
            print("Usage: python evolution_monitor.py [status|restart|stop]")
    else:
        # Default: continuous monitoring
        monitor.continuous_monitor()


if __name__ == "__main__":
    main()