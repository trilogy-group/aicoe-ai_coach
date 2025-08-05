#!/usr/bin/env python3
"""
Intensive AI Learning with Massive Dataset
Uses the 200K+ telemetry records and 20K+ interactions for deep learning.
"""

import asyncio
import json
import pandas as pd
from datetime import datetime
from pathlib import Path
import logging
from openevolve_runner import OpenEvolveImprover

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def run_intensive_learning():
    """Run intensive AI learning on massive dataset."""
    
    print("🔥 INTENSIVE AI LEARNING SYSTEM")
    print("Using massive dataset: 200K+ telemetry, 20K+ interactions")
    print("=" * 70)
    
    # Initialize the learning system
    improver = OpenEvolveImprover()
    
    # Load massive interaction dataset
    interactions_file = "outputs/massive_synthetic_interactions.jsonl"
    
    if not Path(interactions_file).exists():
        print(f"❌ Massive dataset not found: {interactions_file}")
        print("Please run: python generate_massive_dataset.py 200000")
        return
    
    print(f"📊 Loading massive interaction dataset...")
    
    interactions_loaded = 0
    with open(interactions_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            try:
                interaction = json.loads(line.strip())
                improver.process_interaction_feedback(interaction)
                interactions_loaded += 1
                
                if interactions_loaded % 5000 == 0:
                    logger.info(f"Processed {interactions_loaded:,} interactions...")
                    
            except json.JSONDecodeError:
                continue
    
    logger.info(f"✅ Loaded {interactions_loaded:,} massive interactions")
    
    print(f"\n🧠 CURRENT LEARNING STATE:")
    print(f"   Total Interactions Processed: {improver.learning_metrics.total_interactions:,}")
    print(f"   Current Acceptance Rate: {improver.learning_metrics.acceptance_rate:.1%}")
    print(f"   Strategy Evolutions: {improver.learning_metrics.strategy_evolution_count}")
    print(f"   Best Fitness Score: {improver.learning_metrics.best_fitness_score:.3f}")
    
    # Run multiple evolution cycles for deep learning
    print(f"\n🚀 RUNNING INTENSIVE EVOLUTION CYCLES...")
    
    evolution_cycles = 10
    for cycle in range(1, evolution_cycles + 1):
        print(f"\n🔄 Evolution Cycle {cycle}/{evolution_cycles}")
        print("-" * 40)
        
        # Run evolution with intensive parameters
        results = await improver._evolve_strategies()
        
        # Show results for this cycle
        if results:
            best_fitness = max(
                max(s.fitness_score for s in pop) 
                for pop in improver.strategy_populations.values()
            )
            
            print(f"   Best Fitness This Cycle: {best_fitness:.3f}")
            
            for persona, result in results.items():
                print(f"   {persona.title()}: {result['best_fitness']:.3f} (pop: {result['population_size']})")
    
    # Export the ultra-evolved intelligence
    print(f"\n💾 EXPORTING ULTRA-EVOLVED INTELLIGENCE...")
    evolved_intelligence = improver.export_evolved_intelligence("outputs/ultra_evolved_intelligence.json")
    
    # Analyze final results
    best_strategies = improver.get_best_strategies()
    
    print(f"\n🏆 ULTRA-EVOLVED AI COACH ANALYSIS:")
    print("=" * 50)
    
    total_acceptance = 0
    total_effectiveness = 0
    total_generations = 0
    
    for persona, strategy in best_strategies.items():
        print(f"\n📊 {persona.upper()} PERSONA:")
        print(f"   Strategy ID: {strategy.strategy_id}")
        print(f"   Acceptance Rate: {strategy.acceptance_rate:.1%}")
        print(f"   Effectiveness Score: {strategy.effectiveness_score:.1%}")
        print(f"   Fitness Score: {strategy.fitness_score:.3f}")
        print(f"   Generations Evolved: {strategy.generation}")
        print(f"   Total Mutations: {len(strategy.mutations)}")
        print(f"   Language Style: {strategy.language_style}")
        print(f"   Confidence Threshold: {strategy.confidence_threshold:.3f}")
        
        # Show key mutations
        if strategy.mutations:
            recent_mutations = strategy.mutations[-3:]  # Last 3 mutations
            print(f"   Recent Mutations: {', '.join(recent_mutations)}")
        
        total_acceptance += strategy.acceptance_rate
        total_effectiveness += strategy.effectiveness_score
        total_generations += strategy.generation
    
    # Calculate overall system performance
    avg_acceptance = total_acceptance / len(best_strategies)
    avg_effectiveness = total_effectiveness / len(best_strategies)
    avg_generations = total_generations / len(best_strategies)
    
    print(f"\n🎯 SYSTEM-WIDE PERFORMANCE:")
    print(f"   Average Acceptance Rate: {avg_acceptance:.1%}")
    print(f"   Average Effectiveness: {avg_effectiveness:.1%}")
    print(f"   Average Generations: {avg_generations:.0f}")
    print(f"   Total Learning Cycles: {improver.learning_metrics.strategy_evolution_count}")
    print(f"   Final Fitness Score: {improver.learning_metrics.best_fitness_score:.3f}")
    
    # Calculate AI Integration level
    max_generation = max(s.generation for s in best_strategies.values())
    total_mutations = sum(len(s.mutations) for s in best_strategies.values())
    
    generation_factor = min(max_generation / 100, 0.8)
    mutation_factor = min(total_mutations / 1000, 0.3)
    complexity_factor = min(len(best_strategies) / 10, 0.1)
    
    ai_integration = max(15.0, min(95.0, (generation_factor + mutation_factor + complexity_factor) * 100))
    
    print(f"   AI Integration Level: {ai_integration:.1f}%")
    
    # Performance projections
    learning_velocity = improver.learning_metrics.best_fitness_score / max(1, improver.learning_metrics.strategy_evolution_count)
    
    print(f"\n📈 PERFORMANCE PROJECTIONS:")
    print(f"   Learning Velocity: {learning_velocity:.4f}/cycle")
    
    if avg_acceptance > 0.8:
        print(f"   🏆 ULTRA-HIGH ACCEPTANCE ACHIEVED!")
    if avg_effectiveness > 0.8:
        print(f"   🏆 ULTRA-HIGH EFFECTIVENESS ACHIEVED!")
    if ai_integration > 90:
        print(f"   🏆 MAXIMUM AI INTEGRATION ACHIEVED!")
    
    # Save comprehensive results
    comprehensive_results = {
        "intensive_learning_results": {
            "timestamp": datetime.now().isoformat(),
            "interactions_processed": interactions_loaded,
            "evolution_cycles": evolution_cycles,
            "final_metrics": {
                "average_acceptance_rate": avg_acceptance,
                "average_effectiveness": avg_effectiveness,
                "average_generations": avg_generations,
                "best_fitness_score": improver.learning_metrics.best_fitness_score,
                "ai_integration_level": ai_integration,
                "learning_velocity": learning_velocity
            },
            "persona_strategies": {
                persona: {
                    "acceptance_rate": strategy.acceptance_rate,
                    "effectiveness_score": strategy.effectiveness_score,
                    "fitness_score": strategy.fitness_score,
                    "generation": strategy.generation,
                    "mutations_count": len(strategy.mutations),
                    "language_style": strategy.language_style,
                    "confidence_threshold": strategy.confidence_threshold
                }
                for persona, strategy in best_strategies.items()
            }
        }
    }
    
    with open("outputs/intensive_learning_results.json", 'w') as f:
        json.dump(comprehensive_results, f, indent=2)
    
    print(f"\n💾 RESULTS SAVED:")
    print(f"   • outputs/ultra_evolved_intelligence.json")
    print(f"   • outputs/intensive_learning_results.json")
    print(f"\n🎉 INTENSIVE AI LEARNING COMPLETE!")
    
    return comprehensive_results

if __name__ == "__main__":
    asyncio.run(run_intensive_learning())