#!/usr/bin/env python3
"""
Rapid Evolution System - Accelerated AI Coach improvement
Implements faster iteration cycles with parallel processing and simplified evaluation
"""

import os
import json
import asyncio
import time
from datetime import datetime
from typing import Dict, Any, List
import concurrent.futures
from pathlib import Path

# Import our components
from coaching_evaluator import CoachingEvaluator
from ai_coach_evolution import AICoachEvolution

class RapidEvolution:
    def __init__(self):
        self.evaluator = CoachingEvaluator()
        self.evolution = AICoachEvolution()
        self.output_dir = "outputs/rapid_evolution"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Rapid evolution parameters
        self.mini_generations = 10  # Shorter runs
        self.small_population = 5   # Smaller populations
        self.quick_eval_days = 3    # Faster evaluation
        
    def create_simplified_coach_template(self, base_code: str, focus_area: str) -> str:
        """Create a simplified coach variation focused on specific improvements"""
        
        improvement_prompts = {
            "relevance": "Improve context awareness and situational relevance of coaching messages",
            "actionability": "Make coaching recommendations more specific and actionable",
            "psychology": "Enhance psychological sophistication and research-backed content",
            "personalization": "Better adapt coaching style to user persona and current state",
            "timing": "Optimize when and how frequently coaching interventions are delivered"
        }
        
        prompt = f"""
Improve this AI coaching system with focus on: {improvement_prompts.get(focus_area, focus_area)}

KEY IMPROVEMENTS:
1. Maintain existing class structure and method signatures
2. Focus specifically on {focus_area}
3. Keep code production-ready and functional
4. Enhance effectiveness while maintaining simplicity

Return ONLY the complete Python code for the improved system.

ORIGINAL CODE:
```python
{base_code[:4000]}...
```
"""
        
        try:
            if self.evaluator.anthropic_client:
                response = self.evaluator.anthropic_client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=6000,
                    temperature=0.2,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                evolved_code = response.content[0].text.strip()
                
                # Clean up the response
                if "```python" in evolved_code:
                    evolved_code = evolved_code.split("```python")[1].split("```")[0]
                
                return evolved_code.strip()
                
        except Exception as e:
            print(f"Error creating variation for {focus_area}: {e}")
            return base_code
        
        return base_code
    
    def rapid_evaluate_coach(self, coach_path: str) -> Dict[str, float]:
        """Quick evaluation focusing on key metrics"""
        try:
            coach = self.evaluator.load_coach_module(coach_path)
            
            # Single test scenario for speed
            test_scenario = {
                'name': 'rapid_test',
                'user_profile': {
                    'user_id': 1,
                    'persona_type': 'developer',
                    'productivity_baseline': 0.7
                },
                'days': self.quick_eval_days
            }
            
            telemetry = self.evaluator.generate_realistic_telemetry(
                test_scenario['user_profile'], 
                days=test_scenario['days']
            )
            
            metrics = self.evaluator.measure_coaching_impact(
                coach, telemetry, test_scenario['user_profile']
            )
            
            return {
                'composite_fitness': metrics.get('composite_fitness', -1.0),
                'nudge_quality': metrics.get('avg_nudge_quality', 0.0),
                'behavioral_change': metrics.get('avg_behavioral_change', 0.0),
                'user_satisfaction': metrics.get('avg_user_satisfaction', 0.0),
                'total_interactions': metrics.get('total_interactions', 0)
            }
            
        except Exception as e:
            print(f"Rapid evaluation error for {coach_path}: {e}")
            return {
                'composite_fitness': -1.0,
                'nudge_quality': 0.0,
                'behavioral_change': 0.0,
                'user_satisfaction': 0.0,
                'total_interactions': 0
            }
    
    def run_rapid_cycle(self, base_coach_path: str) -> Dict[str, Any]:
        """Run one rapid evolution cycle"""
        
        print(f"\n🚀 Starting Rapid Evolution Cycle")
        cycle_start = time.time()
        
        # Read base coach
        with open(base_coach_path, 'r') as f:
            base_code = f.read()
        
        # Create focused variations
        focus_areas = ["relevance", "actionability", "psychology", "personalization", "timing"]
        variations = []
        
        print("Creating variations...")
        for i, focus in enumerate(focus_areas):
            print(f"  - Creating {focus} variant...")
            
            evolved_code = self.create_simplified_coach_template(base_code, focus)
            
            # Save variation
            variation_path = os.path.join(self.output_dir, f"rapid_variant_{focus}.py")
            with open(variation_path, 'w') as f:
                f.write(evolved_code)
            
            variations.append((variation_path, focus))
        
        # Evaluate all variations
        print("Evaluating variations...")
        results = []
        
        # Include original for comparison
        base_metrics = self.rapid_evaluate_coach(base_coach_path)
        results.append({
            'path': base_coach_path,
            'focus': 'original',
            'metrics': base_metrics,
            'fitness': base_metrics['composite_fitness']
        })
        print(f"  - Original: {base_metrics['composite_fitness']:.4f}")
        
        # Evaluate variations
        for var_path, focus in variations:
            metrics = self.rapid_evaluate_coach(var_path)
            results.append({
                'path': var_path,
                'focus': focus,
                'metrics': metrics,
                'fitness': metrics['composite_fitness']
            })
            print(f"  - {focus}: {metrics['composite_fitness']:.4f}")
        
        # Find best performer
        results.sort(key=lambda x: x['fitness'], reverse=True)
        best = results[0]
        
        cycle_time = time.time() - cycle_start
        
        cycle_summary = {
            'timestamp': datetime.now().isoformat(),
            'cycle_time': cycle_time,
            'best_fitness': best['fitness'],
            'best_focus': best['focus'],
            'best_path': best['path'],
            'all_results': results,
            'improvement': best['fitness'] - base_metrics['composite_fitness']
        }
        
        print(f"✅ Cycle completed in {cycle_time:.1f}s")
        print(f"   Best: {best['focus']} ({best['fitness']:.4f})")
        print(f"   Improvement: {cycle_summary['improvement']:.4f}")
        
        return cycle_summary
    
    def continuous_rapid_evolution(self, base_coach_path: str, max_cycles: int = 100):
        """Run continuous rapid evolution cycles"""
        
        print(f"🔄 Starting Continuous Rapid Evolution")
        print(f"   Max cycles: {max_cycles}")
        print(f"   Base coach: {base_coach_path}")
        
        current_best_path = base_coach_path
        current_best_fitness = -1.0
        cycle_history = []
        
        for cycle in range(max_cycles):
            print(f"\n{'='*50}")
            print(f"RAPID CYCLE {cycle + 1}/{max_cycles}")
            print(f"{'='*50}")
            
            # Run evolution cycle
            cycle_result = self.run_rapid_cycle(current_best_path)
            cycle_history.append(cycle_result)
            
            # Update best if improved
            if cycle_result['best_fitness'] > current_best_fitness:
                current_best_fitness = cycle_result['best_fitness']
                current_best_path = cycle_result['best_path']
                
                # Save new best
                best_coach_path = os.path.join(self.output_dir, f"best_coach_cycle_{cycle+1}.py")
                with open(cycle_result['best_path'], 'r') as src:
                    with open(best_coach_path, 'w') as dst:
                        dst.write(src.read())
                
                print(f"🎉 NEW BEST! Fitness: {current_best_fitness:.4f}")
                print(f"   Saved to: {best_coach_path}")
            else:
                print(f"📊 No improvement. Best remains: {current_best_fitness:.4f}")
            
            # Save progress
            progress_file = os.path.join(self.output_dir, "rapid_evolution_progress.json")
            with open(progress_file, 'w') as f:
                json.dump({
                    'cycles_completed': cycle + 1,
                    'current_best_fitness': current_best_fitness,
                    'current_best_path': current_best_path,
                    'cycle_history': cycle_history[-10:],  # Keep last 10
                    'total_improvement': current_best_fitness - cycle_history[0]['all_results'][0]['fitness']
                }, f, indent=2)
            
            # Early stopping if excellent performance
            if current_best_fitness > 0.8:
                print(f"🏆 Excellent performance achieved! Stopping at cycle {cycle + 1}")
                break
            
            # Brief pause between cycles
            time.sleep(2)
        
        print(f"\n🎯 Rapid Evolution Complete!")
        print(f"   Total cycles: {len(cycle_history)}")
        print(f"   Final fitness: {current_best_fitness:.4f}")
        print(f"   Total improvement: {current_best_fitness - cycle_history[0]['all_results'][0]['fitness']:.4f}")
        print(f"   Best coach: {current_best_path}")
        
        return {
            'completed_cycles': len(cycle_history),
            'final_best_fitness': current_best_fitness,
            'final_best_path': current_best_path,
            'total_improvement': current_best_fitness - cycle_history[0]['all_results'][0]['fitness'],
            'cycle_history': cycle_history
        }


def main():
    import sys
    
    base_coach = sys.argv[1] if len(sys.argv) > 1 else "ai_coach.py"
    max_cycles = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    
    rapid_evo = RapidEvolution()
    
    print("🚀 RAPID AI COACH EVOLUTION")
    print(f"Base coach: {base_coach}")
    print(f"Max cycles: {max_cycles}")
    
    results = rapid_evo.continuous_rapid_evolution(base_coach, max_cycles)
    
    print(f"\n✅ Evolution completed!")
    print(f"Best coach saved to: {results['final_best_path']}")


if __name__ == "__main__":
    main()