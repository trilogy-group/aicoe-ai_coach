#!/usr/bin/env python3
"""
OpenEvolve AI Coach Improvements System
Implements evolutionary learning algorithms to continuously improve coaching effectiveness.

This file consolidates all learning, adaptation, and improvement functionality
from iterative_learning.py and intelligent_improvements.py into a single file
that can enhance the AI coach through OpenEvolve-inspired algorithms.
"""

import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import asyncio
import logging
from dataclasses import dataclass, asdict
import random
import copy

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class EvolutionStrategy:
    """Represents a coaching strategy that can evolve."""
    strategy_id: str
    persona: str
    template_type: str
    language_style: str
    confidence_threshold: float
    timing_rules: Dict[str, Any]
    acceptance_rate: float = 0.0
    effectiveness_score: float = 0.0
    fitness_score: float = 0.0
    generation: int = 0
    mutations: List[str] = None
    
    def __post_init__(self):
        if self.mutations is None:
            self.mutations = []
    
    def calculate_fitness(self):
        """Calculate fitness score based on acceptance rate and effectiveness."""
        self.fitness_score = (self.acceptance_rate * 0.7) + (self.effectiveness_score * 0.3)
        return self.fitness_score

@dataclass
class LearningMetrics:
    """Tracks learning progress and performance metrics."""
    total_interactions: int = 0
    acceptance_rate: float = 0.0
    productivity_improvement: float = 0.0
    strategy_evolution_count: int = 0
    best_fitness_score: float = 0.0
    learning_velocity: float = 0.0
    adaptation_events: int = 0

class OpenEvolveImprover:
    """
    OpenEvolve-inspired system for continuously improving AI coach performance.
    
    Implements evolutionary algorithms to adapt coaching strategies:
    - Population: Multiple coaching strategies per persona
    - Selection: High-performing strategies are reinforced
    - Mutation: Language, timing, and approach adaptations
    - Crossover: Successful patterns shared across personas
    - Fitness: Measured by acceptance rate × effectiveness score
    """
    
    def __init__(self, ai_coach_instance=None, learning_state_path: str = "outputs/learning_state.json"):
        self.ai_coach = ai_coach_instance
        self.learning_state_path = Path(learning_state_path)
        self.learning_state_path.parent.mkdir(exist_ok=True)
        
        # Evolution parameters
        self.population_size = 8  # Strategies per persona
        self.mutation_rate = 0.3
        self.crossover_rate = 0.4
        self.elite_ratio = 0.25  # Top 25% preserved each generation
        self.max_generations = 100
        
        # Learning configuration
        self.min_interactions_for_evolution = 5
        self.fitness_improvement_threshold = 0.05
        self.adaptation_sensitivity = 0.1
        
        # Strategy populations by persona
        self.strategy_populations: Dict[str, List[EvolutionStrategy]] = {}
        self.learning_metrics = LearningMetrics()
        self.interaction_history: List[Dict] = []
        
        # Load existing learning state
        self.load_learning_state()
        
        # Initialize populations if empty
        if not self.strategy_populations:
            self._initialize_strategy_populations()
    
    def _initialize_strategy_populations(self):
        """Initialize base strategy populations for each persona."""
        
        base_strategies = {
            'manager': [
                {
                    'template_type': 'consultative',
                    'language_style': 'professional',
                    'confidence_threshold': 0.8,
                    'timing_rules': {'interval_minutes': 60, 'avoid_hours': [8, 17, 18]}
                },
                {
                    'template_type': 'directive',
                    'language_style': 'direct',
                    'confidence_threshold': 0.75,
                    'timing_rules': {'interval_minutes': 45, 'avoid_hours': [12, 13]}
                },
                {
                    'template_type': 'supportive',
                    'language_style': 'encouraging',
                    'confidence_threshold': 0.7,
                    'timing_rules': {'interval_minutes': 90, 'avoid_hours': [8, 9]}
                }
            ],
            'analyst': [
                {
                    'template_type': 'technical',
                    'language_style': 'detailed',
                    'confidence_threshold': 0.6,
                    'timing_rules': {'interval_minutes': 30, 'avoid_hours': [12, 13]}
                },
                {
                    'template_type': 'efficiency',
                    'language_style': 'data_driven',
                    'confidence_threshold': 0.65,
                    'timing_rules': {'interval_minutes': 35, 'avoid_hours': []}
                },
                {
                    'template_type': 'tools_focused',
                    'language_style': 'specific',
                    'confidence_threshold': 0.55,
                    'timing_rules': {'interval_minutes': 25, 'avoid_hours': []}
                }
            ],
            'developer': [
                {
                    'template_type': 'flow_aware',
                    'language_style': 'technical',
                    'confidence_threshold': 0.7,
                    'timing_rules': {'interval_minutes': 45, 'quiet_hours': [9, 10, 11, 14, 15, 16]}
                },
                {
                    'template_type': 'productivity',
                    'language_style': 'direct',
                    'confidence_threshold': 0.75,
                    'timing_rules': {'interval_minutes': 30, 'quiet_hours': [10, 11, 15, 16]}
                },
                {
                    'template_type': 'workspace',
                    'language_style': 'practical',
                    'confidence_threshold': 0.65,
                    'timing_rules': {'interval_minutes': 60, 'quiet_hours': [9, 10, 14, 15]}
                }
            ],
            'designer': [
                {
                    'template_type': 'creative',
                    'language_style': 'inspiring',
                    'confidence_threshold': 0.7,
                    'timing_rules': {'interval_minutes': 40, 'avoid_hours': []}
                },
                {
                    'template_type': 'visual',
                    'language_style': 'aesthetic',
                    'confidence_threshold': 0.65,
                    'timing_rules': {'interval_minutes': 50, 'avoid_hours': [12, 13]}
                }
            ]
        }
        
        for persona, strategies in base_strategies.items():
            self.strategy_populations[persona] = []
            
            for i, strategy_config in enumerate(strategies):
                # Create multiple variations of each base strategy
                for variation in range(self.population_size // len(strategies) + 1):
                    if len(self.strategy_populations[persona]) >= self.population_size:
                        break
                        
                    strategy = EvolutionStrategy(
                        strategy_id=f"{persona}_{i}_{variation}",
                        persona=persona,
                        **strategy_config,
                        generation=0,
                        mutations=[]
                    )
                    
                    # Add random mutations to create diversity
                    if variation > 0:
                        strategy = self._mutate_strategy(strategy, mutation_strength=0.1)
                    
                    self.strategy_populations[persona].append(strategy)
    
    def process_interaction_feedback(self, interaction_data: Dict):
        """Process user interaction feedback to drive evolution."""
        
        self.interaction_history.append({
            **interaction_data,
            'timestamp': datetime.now().isoformat()
        })
        
        # Update learning metrics
        self.learning_metrics.total_interactions += 1
        
        # Calculate running acceptance rate
        recent_interactions = self.interaction_history[-50:]  # Last 50 interactions
        accepted_count = sum(1 for i in recent_interactions if i.get('outcome', {}).get('accepted', False))
        self.learning_metrics.acceptance_rate = accepted_count / len(recent_interactions) if recent_interactions else 0
        
        # Update strategy performance
        persona = interaction_data.get('persona', 'unknown')
        outcome = interaction_data.get('outcome', {})
        
        if persona in self.strategy_populations:
            # Find best matching strategy (simplified - in production would use more sophisticated matching)
            best_strategy = max(self.strategy_populations[persona], key=lambda s: s.fitness_score)
            
            # Update strategy performance based on interaction outcome
            if outcome.get('accepted', False):
                best_strategy.acceptance_rate = min(1.0, best_strategy.acceptance_rate + 0.1)
                best_strategy.effectiveness_score = min(1.0, best_strategy.effectiveness_score + 
                                                       outcome.get('productivity_impact', 0.1))
            else:
                best_strategy.acceptance_rate = max(0.0, best_strategy.acceptance_rate - 0.05)
            
            best_strategy.calculate_fitness()
        
        # Trigger evolution if conditions are met
        if (self.learning_metrics.total_interactions % self.min_interactions_for_evolution == 0 and
            self.learning_metrics.total_interactions > 0):
            asyncio.create_task(self._evolve_strategies())
    
    async def _evolve_strategies(self):
        """Run one generation of evolutionary improvement."""
        
        logger.info("🧬 Starting strategy evolution...")
        
        evolution_results = {}
        
        for persona, population in self.strategy_populations.items():
            if len(population) < 2:
                continue
                
            # Calculate fitness for all strategies
            for strategy in population:
                strategy.calculate_fitness()
            
            # Sort by fitness (best first)
            population.sort(key=lambda s: s.fitness_score, reverse=True)
            
            # Selection: Keep elite strategies
            elite_count = max(1, int(len(population) * self.elite_ratio))
            elite_strategies = population[:elite_count]
            
            # Create new population
            new_population = copy.deepcopy(elite_strategies)
            
            # Fill remaining slots with crossover and mutation
            while len(new_population) < self.population_size:
                if random.random() < self.crossover_rate and len(elite_strategies) >= 2:
                    # Crossover
                    parent1, parent2 = random.sample(elite_strategies, 2)
                    child = self._crossover_strategies(parent1, parent2)
                    new_population.append(child)
                else:
                    # Mutation
                    parent = random.choice(elite_strategies)
                    mutant = self._mutate_strategy(copy.deepcopy(parent))
                    new_population.append(mutant)
            
            # Update population
            self.strategy_populations[persona] = new_population[:self.population_size]
            
            # Track evolution results
            best_fitness = max(s.fitness_score for s in new_population)
            evolution_results[persona] = {
                'best_fitness': best_fitness,
                'elite_count': elite_count,
                'population_size': len(new_population)
            }
        
        # Update learning metrics
        self.learning_metrics.strategy_evolution_count += 1
        self.learning_metrics.best_fitness_score = max(
            max(s.fitness_score for s in pop) for pop in self.strategy_populations.values()
        )
        
        # Apply best strategies to AI coach if available
        if self.ai_coach:
            await self._apply_evolved_strategies()
        
        # Save learning state
        self.save_learning_state()
        
        logger.info(f"🧬 Evolution complete: {evolution_results}")
        return evolution_results
    
    def _crossover_strategies(self, parent1: EvolutionStrategy, parent2: EvolutionStrategy) -> EvolutionStrategy:
        """Create child strategy by crossing over two parent strategies."""
        
        child = EvolutionStrategy(
            strategy_id=f"cross_{parent1.strategy_id[:8]}_{parent2.strategy_id[:8]}",
            persona=parent1.persona,
            template_type=random.choice([parent1.template_type, parent2.template_type]),
            language_style=random.choice([parent1.language_style, parent2.language_style]),
            confidence_threshold=(parent1.confidence_threshold + parent2.confidence_threshold) / 2,
            timing_rules=self._merge_timing_rules(parent1.timing_rules, parent2.timing_rules),
            generation=max(parent1.generation, parent2.generation) + 1,
            mutations=[f"crossover_from_{parent1.strategy_id}_{parent2.strategy_id}"]
        )
        
        return child
    
    def _merge_timing_rules(self, rules1: Dict, rules2: Dict) -> Dict:
        """Merge timing rules from two parent strategies."""
        merged = {}
        
        # Average numerical values
        for key in ['interval_minutes']:
            if key in rules1 and key in rules2:
                merged[key] = int((rules1[key] + rules2[key]) / 2)
            elif key in rules1:
                merged[key] = rules1[key]
            elif key in rules2:
                merged[key] = rules2[key]
        
        # Combine lists
        for key in ['avoid_hours', 'quiet_hours']:
            combined = set()
            if key in rules1:
                combined.update(rules1[key])
            if key in rules2:
                combined.update(rules2[key])
            if combined:
                merged[key] = list(combined)
        
        return merged
    
    def _mutate_strategy(self, strategy: EvolutionStrategy, mutation_strength: float = None) -> EvolutionStrategy:
        """Apply mutations to a strategy."""
        
        if mutation_strength is None:
            mutation_strength = self.mutation_rate
        
        mutations = []
        
        # Mutate confidence threshold
        if random.random() < mutation_strength:
            delta = random.uniform(-0.1, 0.1)
            strategy.confidence_threshold = max(0.4, min(0.9, strategy.confidence_threshold + delta))
            mutations.append(f"confidence_delta_{delta:.2f}")
        
        # Mutate timing rules
        if random.random() < mutation_strength:
            if 'interval_minutes' in strategy.timing_rules:
                delta = random.randint(-15, 15)
                strategy.timing_rules['interval_minutes'] = max(15, min(120, 
                    strategy.timing_rules['interval_minutes'] + delta))
                mutations.append(f"interval_delta_{delta}")
        
        # Mutate language style
        if random.random() < mutation_strength * 0.5:  # Less frequent
            language_options = {
                'manager': ['professional', 'consultative', 'supportive', 'direct'],
                'analyst': ['detailed', 'data_driven', 'specific', 'technical'],
                'developer': ['technical', 'direct', 'practical', 'concise'],
                'designer': ['inspiring', 'aesthetic', 'creative', 'visual']
            }
            
            if strategy.persona in language_options:
                new_style = random.choice(language_options[strategy.persona])
                if new_style != strategy.language_style:
                    strategy.language_style = new_style
                    mutations.append(f"language_to_{new_style}")
        
        # Update strategy metadata
        strategy.generation += 1
        strategy.mutations.extend(mutations)
        strategy.strategy_id = f"mut_{strategy.strategy_id[:12]}_{strategy.generation}"
        
        return strategy
    
    async def _apply_evolved_strategies(self):
        """Apply the best evolved strategies to the AI coach."""
        
        if not self.ai_coach:
            return
        
        improvements = {}
        
        for persona, population in self.strategy_populations.items():
            # Get best strategy for this persona
            best_strategy = max(population, key=lambda s: s.fitness_score)
            
            # Apply improvements to AI coach
            if hasattr(self.ai_coach, 'persona_intelligence'):
                if persona not in self.ai_coach.persona_intelligence:
                    self.ai_coach.persona_intelligence[persona] = {}
                
                # Update confidence threshold
                self.ai_coach.persona_intelligence[persona]['confidence_override'] = best_strategy.confidence_threshold
                
                # Update timing rules
                if 'interval_minutes' in best_strategy.timing_rules:
                    self.ai_coach.persona_intelligence[persona]['nudge_interval_minutes'] = \
                        best_strategy.timing_rules['interval_minutes']
                
                # Update language style
                self.ai_coach.persona_intelligence[persona]['language_style'] = best_strategy.language_style
                
                improvements[persona] = {
                    'fitness_score': best_strategy.fitness_score,
                    'confidence_threshold': best_strategy.confidence_threshold,
                    'language_style': best_strategy.language_style,
                    'generation': best_strategy.generation
                }
        
        logger.info(f"🚀 Applied evolved strategies: {improvements}")
        return improvements
    
    def analyze_learning_patterns(self) -> Dict[str, Any]:
        """Analyze learning patterns and provide insights."""
        
        if not self.interaction_history:
            return {"status": "No interaction data available"}
        
        # Recent interactions analysis
        recent_interactions = self.interaction_history[-20:]
        
        # Acceptance rates by persona
        persona_stats = {}
        for interaction in recent_interactions:
            persona = interaction.get('persona', 'unknown')
            if persona not in persona_stats:
                persona_stats[persona] = {'total': 0, 'accepted': 0}
            
            persona_stats[persona]['total'] += 1
            if interaction.get('outcome', {}).get('accepted', False):
                persona_stats[persona]['accepted'] += 1
        
        # Calculate acceptance rates
        for persona in persona_stats:
            stats = persona_stats[persona]
            stats['acceptance_rate'] = stats['accepted'] / stats['total'] if stats['total'] > 0 else 0
        
        # Dismissal reason analysis
        dismissal_reasons = {}
        for interaction in recent_interactions:
            outcome = interaction.get('outcome', {})
            if not outcome.get('accepted', False):
                reason = outcome.get('dismissal_reason', 'unknown')
                dismissal_reasons[reason] = dismissal_reasons.get(reason, 0) + 1
        
        # Strategy evolution analysis
        strategy_generations = {}
        for persona, population in self.strategy_populations.items():
            strategy_generations[persona] = {
                'max_generation': max(s.generation for s in population),
                'avg_fitness': sum(s.fitness_score for s in population) / len(population),
                'best_fitness': max(s.fitness_score for s in population)
            }
        
        return {
            "learning_metrics": asdict(self.learning_metrics),
            "persona_acceptance_rates": persona_stats,
            "dismissal_patterns": dismissal_reasons,
            "strategy_evolution": strategy_generations,
            "recent_interaction_count": len(recent_interactions),
            "total_interaction_count": len(self.interaction_history),
            "learning_recommendations": self._generate_learning_recommendations()
        }
    
    def _generate_learning_recommendations(self) -> List[str]:
        """Generate recommendations based on learning analysis."""
        
        recommendations = []
        
        # Check acceptance rates
        if self.learning_metrics.acceptance_rate < 0.65:
            recommendations.append("Consider increasing confidence thresholds to reduce low-quality nudges")
        
        if self.learning_metrics.acceptance_rate > 0.9:
            recommendations.append("Consider decreasing confidence thresholds to increase nudge frequency")
        
        # Check evolution progress
        if self.learning_metrics.strategy_evolution_count < 3:
            recommendations.append("System needs more interactions to drive meaningful evolution")
        
        # Persona-specific recommendations
        recent_interactions = self.interaction_history[-10:]
        persona_performance = {}
        
        for interaction in recent_interactions:
            persona = interaction.get('persona', 'unknown')
            accepted = interaction.get('outcome', {}).get('accepted', False)
            
            if persona not in persona_performance:
                persona_performance[persona] = []
            persona_performance[persona].append(accepted)
        
        for persona, performance in persona_performance.items():
            acceptance_rate = sum(performance) / len(performance)
            if acceptance_rate < 0.5:
                recommendations.append(f"Focus evolution efforts on {persona} persona (low acceptance: {acceptance_rate:.1%})")
        
        return recommendations
    
    def get_best_strategies(self) -> Dict[str, EvolutionStrategy]:
        """Get the best evolved strategy for each persona."""
        
        best_strategies = {}
        
        for persona, population in self.strategy_populations.items():
            best_strategy = max(population, key=lambda s: s.fitness_score)
            best_strategies[persona] = best_strategy
        
        return best_strategies
    
    def export_evolved_intelligence(self, output_path: str = "outputs/evolved_intelligence.json"):
        """Export evolved intelligence for integration with AI coach."""
        
        best_strategies = self.get_best_strategies()
        learning_analysis = self.analyze_learning_patterns()
        
        evolved_intelligence = {
            "evolution_metadata": {
                "total_generations": self.learning_metrics.strategy_evolution_count,
                "total_interactions": self.learning_metrics.total_interactions,
                "best_fitness_score": self.learning_metrics.best_fitness_score,
                "export_timestamp": datetime.now().isoformat()
            },
            "persona_strategies": {
                persona: {
                    "strategy_id": strategy.strategy_id,
                    "confidence_threshold": strategy.confidence_threshold,
                    "language_style": strategy.language_style,
                    "template_type": strategy.template_type,
                    "timing_rules": strategy.timing_rules,
                    "fitness_score": strategy.fitness_score,
                    "acceptance_rate": strategy.acceptance_rate,
                    "generation": strategy.generation,
                    "mutations": strategy.mutations
                } for persona, strategy in best_strategies.items()
            },
            "learning_insights": learning_analysis,
            "integration_config": {
                "recommended_confidence_thresholds": {
                    persona: strategy.confidence_threshold 
                    for persona, strategy in best_strategies.items()
                },
                "recommended_intervals": {
                    persona: strategy.timing_rules.get('interval_minutes', 30)
                    for persona, strategy in best_strategies.items()
                },
                "language_adaptations": {
                    persona: strategy.language_style
                    for persona, strategy in best_strategies.items()
                }
            }
        }
        
        # Save to file
        output_path = Path(output_path)
        output_path.parent.mkdir(exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(evolved_intelligence, f, indent=2)
        
        logger.info(f"📊 Exported evolved intelligence to {output_path}")
        return evolved_intelligence
    
    def load_learning_state(self):
        """Load learning state from disk."""
        
        if not self.learning_state_path.exists():
            logger.info("No existing learning state found, starting fresh")
            return
        
        try:
            with open(self.learning_state_path, 'r') as f:
                state_data = json.load(f)
            
            # Load learning metrics
            if 'learning_metrics' in state_data:
                metrics_data = state_data['learning_metrics']
                self.learning_metrics = LearningMetrics(**metrics_data)
            
            # Load interaction history
            if 'interaction_history' in state_data:
                self.interaction_history = state_data['interaction_history']
            
            # Load strategy populations
            if 'strategy_populations' in state_data:
                for persona, strategies_data in state_data['strategy_populations'].items():
                    self.strategy_populations[persona] = [
                        EvolutionStrategy(**strategy_data) for strategy_data in strategies_data
                    ]
            
            logger.info(f"✅ Loaded learning state: {self.learning_metrics.total_interactions} interactions")
            
        except Exception as e:
            logger.error(f"Failed to load learning state: {e}")
    
    def save_learning_state(self):
        """Save current learning state to disk."""
        
        state_data = {
            "learning_metrics": asdict(self.learning_metrics),
            "interaction_history": self.interaction_history[-100:],  # Keep last 100 interactions
            "strategy_populations": {
                persona: [asdict(strategy) for strategy in population]
                for persona, population in self.strategy_populations.items()
            },
            "save_timestamp": datetime.now().isoformat()
        }
        
        try:
            with open(self.learning_state_path, 'w') as f:
                json.dump(state_data, f, indent=2)
            
            logger.info(f"💾 Saved learning state to {self.learning_state_path}")
            
        except Exception as e:
            logger.error(f"Failed to save learning state: {e}")

async def run_evolution_cycle(ai_coach_instance=None, cycles: int = 5):
    """Run multiple evolution cycles to improve the AI coach."""
    
    print("🧬 OPENEVOLVE IMPROVEMENT SYSTEM")
    print("="*60)
    print(f"Running {cycles} evolution cycles to improve AI coach performance")
    print("-"*60)
    
    # Initialize improver
    improver = OpenEvolveImprover(ai_coach_instance)
    
    # Load synthetic interaction data if available
    interaction_file = Path("outputs/coaching_interactions.jsonl")
    if interaction_file.exists():
        print("📊 Loading existing interaction data...")
        
        with open(interaction_file, 'r') as f:
            for line in f:
                try:
                    interaction = json.loads(line.strip())
                    improver.process_interaction_feedback(interaction)
                except json.JSONDecodeError:
                    continue
        
        print(f"✅ Loaded {len(improver.interaction_history)} interactions")
    
    # Run evolution cycles
    for cycle in range(cycles):
        print(f"\n🔄 Evolution Cycle {cycle + 1}/{cycles}")
        print("-" * 40)
        
        # Generate some synthetic feedback for demonstration
        synthetic_interactions = _generate_synthetic_interactions(5)
        for interaction in synthetic_interactions:
            improver.process_interaction_feedback(interaction)
        
        # Trigger evolution
        evolution_results = await improver._evolve_strategies()
        
        # Analyze current state
        analysis = improver.analyze_learning_patterns()
        
        print(f"📈 Cycle {cycle + 1} Results:")
        print(f"   Total Interactions: {analysis['total_interaction_count']}")
        print(f"   Acceptance Rate: {analysis['learning_metrics']['acceptance_rate']:.1%}")
        print(f"   Best Fitness: {analysis['learning_metrics']['best_fitness_score']:.3f}")
        print(f"   Strategy Generations: {analysis['learning_metrics']['strategy_evolution_count']}")
        
        # Show persona performance
        if 'persona_acceptance_rates' in analysis:
            print("   Persona Performance:")
            for persona, stats in analysis['persona_acceptance_rates'].items():
                print(f"     {persona.title()}: {stats['acceptance_rate']:.1%} acceptance")
    
    # Export final evolved intelligence
    final_intelligence = improver.export_evolved_intelligence()
    
    # Show final recommendations
    recommendations = analysis.get('learning_recommendations', [])
    if recommendations:
        print(f"\n💡 Learning Recommendations:")
        for i, rec in enumerate(recommendations, 1):
            print(f"   {i}. {rec}")
    
    print(f"\n🎉 Evolution Complete!")
    print(f"   Best evolved strategies exported to outputs/evolved_intelligence.json")
    print(f"   System ready for enhanced coaching performance")
    
    return improver, final_intelligence

def _generate_synthetic_interactions(count: int) -> List[Dict]:
    """Generate synthetic interactions for testing evolution."""
    
    personas = ['manager', 'analyst', 'developer', 'designer']
    interactions = []
    
    for _ in range(count):
        persona = random.choice(personas)
        
        # Simulate interaction outcome based on persona characteristics
        base_acceptance_rates = {
            'manager': 0.57,
            'analyst': 0.875,
            'developer': 0.78,
            'designer': 1.0
        }
        
        accepted = random.random() < base_acceptance_rates.get(persona, 0.7)
        
        interaction = {
            'user_id': random.randint(1, 100),
            'persona': persona,
            'nudge': {
                'nudge_text': f"Synthetic nudge for {persona}",
                'confidence': random.uniform(0.5, 0.9),
                'trigger_dimension': random.choice(['focus', 'productivity', 'wellbeing', 'value_creation'])
            },
            'outcome': {
                'accepted': accepted,
                'productivity_impact': random.uniform(0.08, 0.20) if accepted else 0.0,
                'dismissal_reason': random.choice(['busy', 'not_relevant', 'too_frequent']) if not accepted else None,
                'response_time_seconds': random.uniform(2, 30)
            }
        }
        
        interactions.append(interaction)
    
    return interactions

if __name__ == "__main__":
    async def main():
        # Run standalone evolution demonstration
        improver, intelligence = await run_evolution_cycle(cycles=3)
        
        # Show best strategies
        best_strategies = improver.get_best_strategies()
        print(f"\n🏆 Best Evolved Strategies:")
        for persona, strategy in best_strategies.items():
            print(f"   {persona.title()}: Fitness {strategy.fitness_score:.3f}, Gen {strategy.generation}")
        
        return improver
    
    asyncio.run(main())