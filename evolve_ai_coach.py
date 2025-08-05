#!/usr/bin/env python3
"""
OpenEvolve AI Coach Evolution System
===================================

Genetic algorithm optimization system for maximizing coaching effectiveness and user acceptance.
Completely self-contained evolution system that works with the AI Coach to improve coaching strategies.

This system implements:
- Genetic Algorithm for strategy optimization
- Population-based learning
- Multi-generational fitness improvement
- Scenario-specific adaptation
- Persona-targeted optimization

Author: AI Coach Evolution Team
Version: 2.0 (Self-Contained)
"""

import asyncio
import json
import random
import numpy as np
import pandas as pd
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple, Optional
from pathlib import Path
from dataclasses import dataclass, field
import copy

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class EvolutionStrategy:
    """Represents a coaching strategy that can be evolved."""
    strategy_id: str
    persona: str
    confidence_threshold: float
    language_style: str
    nudge_interval_minutes: int
    timing_rules: Dict[str, Any]
    template_preferences: List[str]
    acceptance_rate: float = 0.0
    effectiveness_score: float = 0.0
    user_satisfaction: float = 0.0
    time_savings_hours: float = 0.0
    fitness_score: float = 0.0
    generation: int = 0
    mutations: List[str] = field(default_factory=list)
    test_scenarios_passed: int = 0
    total_scenarios_tested: int = 0

class OpenEvolveOptimizer:
    """Genetic algorithm optimizer for AI coaching strategies."""
    
    def __init__(self, population_size: int = 50, mutation_rate: float = 0.15, 
                 crossover_rate: float = 0.8, elite_ratio: float = 0.2):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_ratio = elite_ratio
        self.elite_count = max(1, int(population_size * elite_ratio))
        
        # Ensure outputs directory exists
        Path("outputs").mkdir(exist_ok=True)
        Path("outputs/evolution").mkdir(exist_ok=True)
        
        # Evolution parameters
        self.max_generations = 100
        self.target_fitness = 0.95
        self.stagnation_threshold = 10  # Generations without improvement
        
        # Persona configurations for evolution
        self.personas = ['manager', 'analyst', 'developer', 'designer', 'customer_support']
        
        # Evolution state
        self.current_generation = 0
        self.best_fitness_history = []
        self.population_history = []
        self.evolution_stats = {
            'total_generations': 0,
            'total_mutations': 0,
            'total_crossovers': 0,
            'best_fitness_achieved': 0.0,
            'convergence_generation': None
        }
        
        # Load existing evolution state if available
        self._load_evolution_state()
        
    def _load_evolution_state(self):
        """Load existing evolution state from file."""
        try:
            state_file = Path("outputs/evolution/evolution_state.json")
            if state_file.exists():
                with open(state_file, 'r') as f:
                    state = json.load(f)
                    self.current_generation = state.get('current_generation', 0)
                    self.best_fitness_history = state.get('best_fitness_history', [])
                    self.evolution_stats = state.get('evolution_stats', self.evolution_stats)
                    logger.info(f"Loaded evolution state from generation {self.current_generation}")
        except Exception as e:
            logger.warning(f"Could not load evolution state: {str(e)}")
    
    def _save_evolution_state(self):
        """Save current evolution state to file."""
        try:
            state = {
                'current_generation': self.current_generation,
                'best_fitness_history': self.best_fitness_history,
                'evolution_stats': self.evolution_stats,
                'timestamp': datetime.now().isoformat()
            }
            
            with open("outputs/evolution/evolution_state.json", 'w') as f:
                json.dump(state, f, indent=2)
                
        except Exception as e:
            logger.error(f"Could not save evolution state: {str(e)}")
    
    def create_initial_population(self) -> List[EvolutionStrategy]:
        """Create initial population of coaching strategies."""
        population = []
        
        for i in range(self.population_size):
            for persona in self.personas:
                strategy = EvolutionStrategy(
                    strategy_id=f"gen0_{persona}_{i}",
                    persona=persona,
                    confidence_threshold=random.uniform(0.3, 0.9),
                    language_style=random.choice(['direct', 'consultative', 'technical', 'supportive', 'challenging']),
                    nudge_interval_minutes=random.randint(15, 120),
                    timing_rules=self._generate_timing_rules(),
                    template_preferences=self._generate_template_preferences(),
                    generation=0
                )
                population.append(strategy)
                
                if len(population) >= self.population_size:
                    break
            if len(population) >= self.population_size:
                break
        
        return population[:self.population_size]
    
    def _generate_timing_rules(self) -> Dict[str, Any]:
        """Generate random timing rules for a strategy."""
        return {
            'quiet_hours': random.sample(range(9, 18), k=random.randint(2, 6)),
            'peak_hours': random.sample(range(9, 17), k=random.randint(2, 4)),
            'avoid_lunch': random.choice([True, False]),
            'respect_focus_time': random.choice([True, False]),
            'interruption_sensitivity': random.uniform(0.1, 0.9)
        }
    
    def _generate_template_preferences(self) -> List[str]:
        """Generate random template preferences."""
        all_templates = [
            'focus_optimization', 'productivity_boost', 'wellbeing_check',
            'automation_suggestion', 'workflow_improvement', 'break_reminder',
            'energy_management', 'distraction_reduction', 'goal_alignment'
        ]
        return random.sample(all_templates, k=random.randint(3, 7))
    
    async def evaluate_strategy(self, strategy: EvolutionStrategy, test_scenarios: List[Dict]) -> float:
        """Evaluate a strategy's fitness using test scenarios."""
        total_score = 0.0
        scenarios_passed = 0
        
        for scenario in test_scenarios:
            # Simulate coaching interaction
            score = await self._simulate_coaching_interaction(strategy, scenario)
            total_score += score
            if score > 0.7:  # Threshold for "passing" a scenario
                scenarios_passed += 1
        
        # Update strategy metrics
        strategy.test_scenarios_passed = scenarios_passed
        strategy.total_scenarios_tested = len(test_scenarios)
        
        # Calculate fitness components
        acceptance_component = scenarios_passed / len(test_scenarios) if test_scenarios else 0
        effectiveness_component = total_score / len(test_scenarios) if test_scenarios else 0
        
        # Bonus for well-balanced strategies
        balance_bonus = 0.1 if 0.4 <= strategy.confidence_threshold <= 0.8 else 0
        timing_bonus = 0.05 if 30 <= strategy.nudge_interval_minutes <= 90 else 0
        
        fitness = (acceptance_component * 0.4 + 
                  effectiveness_component * 0.3 + 
                  balance_bonus + timing_bonus) * 100
        
        strategy.fitness_score = fitness
        strategy.acceptance_rate = acceptance_component
        strategy.effectiveness_score = effectiveness_component
        
        return fitness
    
    async def _simulate_coaching_interaction(self, strategy: EvolutionStrategy, scenario: Dict) -> float:
        """Simulate a coaching interaction and return success score."""
        try:
            # Extract scenario parameters
            persona = scenario.get('persona', strategy.persona)
            context = scenario.get('context', {})
            expected_outcome = scenario.get('expected_outcome', 'positive')
            
            # Simulate strategy application
            confidence_match = abs(strategy.confidence_threshold - context.get('confidence_needed', 0.7))
            timing_appropriateness = self._assess_timing_appropriateness(strategy, context)
            language_fit = self._assess_language_fit(strategy, persona, context)
            
            # Calculate interaction success
            base_score = max(0, 1.0 - confidence_match)  # Closer to needed confidence = higher score
            timing_score = timing_appropriateness
            language_score = language_fit
            
            # Combine scores
            interaction_score = (base_score * 0.4 + timing_score * 0.3 + language_score * 0.3)
            
            # Apply persona-specific adjustments
            persona_multiplier = self._get_persona_multiplier(strategy.persona, persona)
            final_score = interaction_score * persona_multiplier
            
            return min(1.0, max(0.0, final_score))
            
        except Exception as e:
            logger.error(f"Error simulating coaching interaction: {str(e)}")
            return 0.0
    
    def _assess_timing_appropriateness(self, strategy: EvolutionStrategy, context: Dict) -> float:
        """Assess how appropriate the timing rules are for the context."""
        current_hour = context.get('current_hour', 12)
        focus_state = context.get('focus_state', 'normal')
        interruption_level = context.get('interruption_level', 0.5)
        
        score = 0.7  # Base score
        
        # Check quiet hours
        if current_hour in strategy.timing_rules.get('quiet_hours', []):
            if focus_state == 'deep_focus':
                score -= 0.3  # Bad to interrupt deep focus during quiet hours
            else:
                score += 0.1  # Good to respect quiet hours
        
        # Check peak hours
        if current_hour in strategy.timing_rules.get('peak_hours', []):
            if focus_state == 'low_energy':
                score += 0.2  # Good to coach during peak hours when energy is low
        
        # Interruption sensitivity
        sensitivity = strategy.timing_rules.get('interruption_sensitivity', 0.5)
        if interruption_level > sensitivity:
            score -= 0.2  # Strategy not sensitive enough to high interruption environment
        
        return min(1.0, max(0.0, score))
    
    def _assess_language_fit(self, strategy: EvolutionStrategy, persona: str, context: Dict) -> float:
        """Assess how well the language style fits the persona and context."""
        style_persona_fit = {
            'manager': {'direct': 0.9, 'consultative': 0.8, 'technical': 0.4, 'supportive': 0.7, 'challenging': 0.8},
            'analyst': {'direct': 0.7, 'consultative': 0.6, 'technical': 0.9, 'supportive': 0.5, 'challenging': 0.6},
            'developer': {'direct': 0.8, 'consultative': 0.5, 'technical': 0.9, 'supportive': 0.6, 'challenging': 0.7},
            'designer': {'direct': 0.6, 'consultative': 0.8, 'technical': 0.5, 'supportive': 0.9, 'challenging': 0.6},
            'customer_support': {'direct': 0.7, 'consultative': 0.9, 'technical': 0.6, 'supportive': 0.9, 'challenging': 0.4}
        }
        
        base_fit = style_persona_fit.get(persona, {}).get(strategy.language_style, 0.5)
        
        # Adjust based on context
        stress_level = context.get('stress_level', 0.5)
        if stress_level > 0.7 and strategy.language_style == 'supportive':
            base_fit += 0.2
        elif stress_level > 0.7 and strategy.language_style == 'challenging':
            base_fit -= 0.3
        
        return min(1.0, max(0.0, base_fit))
    
    def _get_persona_multiplier(self, strategy_persona: str, scenario_persona: str) -> float:
        """Get multiplier based on persona match."""
        if strategy_persona == scenario_persona:
            return 1.0
        else:
            # Slight penalty for persona mismatch, but not too harsh
            return 0.8
    
    def mutate_strategy(self, strategy: EvolutionStrategy) -> EvolutionStrategy:
        """Apply mutations to a strategy."""
        mutated = copy.deepcopy(strategy)
        mutations = []
        
        # Confidence threshold mutation
        if random.random() < self.mutation_rate:
            delta = random.uniform(-0.1, 0.1)
            mutated.confidence_threshold = max(0.1, min(0.9, mutated.confidence_threshold + delta))
            mutations.append(f"confidence_delta_{delta:.2f}")
        
        # Language style mutation
        if random.random() < self.mutation_rate * 0.5:
            styles = ['direct', 'consultative', 'technical', 'supportive', 'challenging']
            mutated.language_style = random.choice(styles)
            mutations.append(f"language_to_{mutated.language_style}")
        
        # Nudge interval mutation
        if random.random() < self.mutation_rate:
            delta = random.randint(-15, 15)
            mutated.nudge_interval_minutes = max(15, min(120, mutated.nudge_interval_minutes + delta))
            mutations.append(f"interval_delta_{delta}")
        
        # Timing rules mutation
        if random.random() < self.mutation_rate * 0.3:
            mutated.timing_rules = self._generate_timing_rules()
            mutations.append("timing_rules_regenerated")
        
        # Template preferences mutation
        if random.random() < self.mutation_rate * 0.3:
            # Add or remove a template preference
            all_templates = [
                'focus_optimization', 'productivity_boost', 'wellbeing_check',
                'automation_suggestion', 'workflow_improvement', 'break_reminder',
                'energy_management', 'distraction_reduction', 'goal_alignment'
            ]
            if random.choice([True, False]) and len(mutated.template_preferences) < 8:
                # Add a template
                available = [t for t in all_templates if t not in mutated.template_preferences]
                if available:
                    mutated.template_preferences.append(random.choice(available))
                    mutations.append(f"added_template_{available[-1]}")
            elif len(mutated.template_preferences) > 2:
                # Remove a template
                removed = mutated.template_preferences.pop(random.randint(0, len(mutated.template_preferences) - 1))
                mutations.append(f"removed_template_{removed}")
        
        # Update metadata
        mutated.strategy_id = f"gen{self.current_generation + 1}_{mutated.persona}_{random.randint(1000, 9999)}"
        mutated.generation = self.current_generation + 1
        mutated.mutations.extend(mutations)
        
        # Reset fitness metrics
        mutated.fitness_score = 0.0
        mutated.acceptance_rate = 0.0
        mutated.effectiveness_score = 0.0
        
        self.evolution_stats['total_mutations'] += len(mutations)
        
        return mutated
    
    def crossover_strategies(self, parent1: EvolutionStrategy, parent2: EvolutionStrategy) -> Tuple[EvolutionStrategy, EvolutionStrategy]:
        """Create offspring through crossover of two parent strategies."""
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        
        # Confidence threshold crossover
        if random.random() < self.crossover_rate:
            alpha = random.random()
            new_conf1 = alpha * parent1.confidence_threshold + (1 - alpha) * parent2.confidence_threshold
            new_conf2 = alpha * parent2.confidence_threshold + (1 - alpha) * parent1.confidence_threshold
            child1.confidence_threshold = new_conf1
            child2.confidence_threshold = new_conf2
        
        # Language style crossover
        if random.random() < self.crossover_rate * 0.7:
            child1.language_style = parent2.language_style
            child2.language_style = parent1.language_style
        
        # Nudge interval crossover
        if random.random() < self.crossover_rate:
            child1.nudge_interval_minutes = parent2.nudge_interval_minutes
            child2.nudge_interval_minutes = parent1.nudge_interval_minutes
        
        # Timing rules crossover (mix rules)
        if random.random() < self.crossover_rate * 0.5:
            # Combine quiet hours
            combined_quiet = list(set(parent1.timing_rules.get('quiet_hours', []) + 
                                    parent2.timing_rules.get('quiet_hours', [])))
            child1.timing_rules['quiet_hours'] = combined_quiet[:6]  # Limit to 6 hours
            child2.timing_rules['quiet_hours'] = combined_quiet[:6]
            
            # Mix other timing rules
            child1.timing_rules['interruption_sensitivity'] = parent2.timing_rules.get('interruption_sensitivity', 0.5)
            child2.timing_rules['interruption_sensitivity'] = parent1.timing_rules.get('interruption_sensitivity', 0.5)
        
        # Template preferences crossover
        if random.random() < self.crossover_rate * 0.6:
            # Combine and shuffle template preferences
            combined_templates = list(set(parent1.template_preferences + parent2.template_preferences))
            random.shuffle(combined_templates)
            
            mid_point = len(combined_templates) // 2
            child1.template_preferences = combined_templates[:mid_point + 2]
            child2.template_preferences = combined_templates[mid_point:]
        
        # Update metadata
        child1.strategy_id = f"gen{self.current_generation + 1}_{child1.persona}_cross_{random.randint(1000, 9999)}"
        child2.strategy_id = f"gen{self.current_generation + 1}_{child2.persona}_cross_{random.randint(1000, 9999)}"
        child1.generation = self.current_generation + 1
        child2.generation = self.current_generation + 1
        
        # Reset fitness metrics
        for child in [child1, child2]:
            child.fitness_score = 0.0
            child.acceptance_rate = 0.0
            child.effectiveness_score = 0.0
            child.mutations = [f"crossover_gen_{self.current_generation + 1}"]
        
        self.evolution_stats['total_crossovers'] += 1
        
        return child1, child2
    
    def select_parents(self, population: List[EvolutionStrategy]) -> Tuple[EvolutionStrategy, EvolutionStrategy]:
        """Select two parents using tournament selection."""
        tournament_size = 3
        
        # Tournament selection for parent 1
        tournament1 = random.sample(population, min(tournament_size, len(population)))
        parent1 = max(tournament1, key=lambda x: x.fitness_score)
        
        # Tournament selection for parent 2 (ensure different from parent 1)
        attempts = 0
        while attempts < 10:
            tournament2 = random.sample(population, min(tournament_size, len(population)))
            parent2 = max(tournament2, key=lambda x: x.fitness_score)
            if parent2.strategy_id != parent1.strategy_id:
                break
            attempts += 1
        else:
            # Fallback: just pick a different strategy
            available = [s for s in population if s.strategy_id != parent1.strategy_id]
            parent2 = random.choice(available) if available else parent1
        
        return parent1, parent2
    
    def generate_test_scenarios(self, num_scenarios: int = 20) -> List[Dict]:
        """Generate test scenarios for evaluating strategies."""
        scenarios = []
        
        scenario_templates = [
            {
                'name': 'high_cognitive_load',
                'persona': 'developer',
                'context': {
                    'cognitive_load': 0.9,
                    'focus_state': 'fragmented',
                    'current_hour': 14,
                    'stress_level': 0.8,
                    'confidence_needed': 0.7,
                    'interruption_level': 0.6
                },
                'expected_outcome': 'supportive_break_suggestion'
            },
            {
                'name': 'distraction_overload',
                'persona': 'analyst',
                'context': {
                    'cognitive_load': 0.6,
                    'focus_state': 'distracted',
                    'current_hour': 10,
                    'stress_level': 0.5,
                    'confidence_needed': 0.8,
                    'interruption_level': 0.8
                },
                'expected_outcome': 'focus_restoration'
            },
            {
                'name': 'flow_state_protection',
                'persona': 'developer',
                'context': {
                    'cognitive_load': 0.4,
                    'focus_state': 'deep_focus',
                    'current_hour': 15,
                    'stress_level': 0.2,
                    'confidence_needed': 0.9,
                    'interruption_level': 0.1
                },
                'expected_outcome': 'minimal_intervention'
            },
            {
                'name': 'energy_management',
                'persona': 'manager',
                'context': {
                    'cognitive_load': 0.7,
                    'focus_state': 'low_energy',
                    'current_hour': 16,
                    'stress_level': 0.6,
                    'confidence_needed': 0.6,
                    'interruption_level': 0.7
                },
                'expected_outcome': 'energy_boost_suggestion'
            },
            {
                'name': 'creative_workflow',
                'persona': 'designer',
                'context': {
                    'cognitive_load': 0.5,
                    'focus_state': 'creative',
                    'current_hour': 11,
                    'stress_level': 0.3,
                    'confidence_needed': 0.7,
                    'interruption_level': 0.3
                },
                'expected_outcome': 'creative_enhancement'
            }
        ]
        
        # Generate scenarios with variations
        for _ in range(num_scenarios):
            template = random.choice(scenario_templates)
            scenario = copy.deepcopy(template)
            
            # Add some random variation
            context = scenario['context']
            context['cognitive_load'] = max(0.1, min(1.0, context['cognitive_load'] + random.uniform(-0.1, 0.1)))
            context['stress_level'] = max(0.0, min(1.0, context['stress_level'] + random.uniform(-0.1, 0.1)))
            context['current_hour'] = random.randint(9, 17)
            
            scenarios.append(scenario)
        
        return scenarios
    
    async def evolve_population(self, generations: int = 50) -> Dict[str, Any]:
        """Run the evolution process for specified generations."""
        logger.info(f"Starting evolution for {generations} generations")
        
        # Generate test scenarios
        test_scenarios = self.generate_test_scenarios(30)
        
        # Create or load initial population
        if self.current_generation == 0:
            population = self.create_initial_population()
            logger.info(f"Created initial population of {len(population)} strategies")
        else:
            # Load existing population if available
            population = self.create_initial_population()  # Fallback
            logger.info(f"Continuing evolution from generation {self.current_generation}")
        
        best_strategy = None
        stagnation_count = 0
        last_best_fitness = 0
        
        for generation in range(generations):
            self.current_generation = generation
            logger.info(f"Generation {generation + 1}/{generations}")
            
            # Evaluate population
            fitness_tasks = []
            for strategy in population:
                fitness_tasks.append(self.evaluate_strategy(strategy, test_scenarios))
            
            fitness_scores = await asyncio.gather(*fitness_tasks)
            
            # Update population fitness
            for strategy, fitness in zip(population, fitness_scores):
                strategy.fitness_score = fitness
            
            # Sort by fitness
            population.sort(key=lambda x: x.fitness_score, reverse=True)
            
            # Track best fitness
            current_best_fitness = population[0].fitness_score
            self.best_fitness_history.append(current_best_fitness)
            
            if current_best_fitness > self.evolution_stats['best_fitness_achieved']:
                self.evolution_stats['best_fitness_achieved'] = current_best_fitness
                best_strategy = copy.deepcopy(population[0])
                logger.info(f"New best fitness: {current_best_fitness:.2f}")
            
            # Check for stagnation
            if abs(current_best_fitness - last_best_fitness) < 0.01:
                stagnation_count += 1
            else:
                stagnation_count = 0
            
            if stagnation_count >= self.stagnation_threshold:
                logger.info(f"Evolution converged at generation {generation + 1}")
                self.evolution_stats['convergence_generation'] = generation + 1
                break
            
            last_best_fitness = current_best_fitness
            
            # Check if target fitness reached
            if current_best_fitness >= self.target_fitness:
                logger.info(f"Target fitness {self.target_fitness} reached at generation {generation + 1}")
                break
            
            # Create next generation
            new_population = []
            
            # Keep elite strategies
            elite_count = self.elite_count
            new_population.extend(population[:elite_count])
            
            # Generate offspring
            while len(new_population) < self.population_size:
                parent1, parent2 = self.select_parents(population)
                child1, child2 = self.crossover_strategies(parent1, parent2)
                
                # Apply mutations
                if random.random() < 0.7:  # 70% chance to mutate
                    child1 = self.mutate_strategy(child1)
                if random.random() < 0.7:
                    child2 = self.mutate_strategy(child2)
                
                new_population.extend([child1, child2])
            
            # Trim to population size
            population = new_population[:self.population_size]
            
            # Save progress
            if generation % 10 == 0:
                self._save_evolution_state()
                await self._save_generation_results(generation, population)
        
        # Final statistics
        self.evolution_stats['total_generations'] = self.current_generation + 1
        
        # Save final results
        await self._save_final_results(best_strategy, population)
        
        logger.info("Evolution completed!")
        return {
            'best_strategy': best_strategy,
            'final_population': population,
            'evolution_stats': self.evolution_stats,
            'fitness_history': self.best_fitness_history
        }
    
    async def _save_generation_results(self, generation: int, population: List[EvolutionStrategy]):
        """Save results for a specific generation."""
        try:
            results = {
                'generation': generation,
                'timestamp': datetime.now().isoformat(),
                'population_size': len(population),
                'best_fitness': max(s.fitness_score for s in population),
                'average_fitness': sum(s.fitness_score for s in population) / len(population),
                'strategies': []
            }
            
            # Save top 10 strategies from this generation
            top_strategies = sorted(population, key=lambda x: x.fitness_score, reverse=True)[:10]
            for strategy in top_strategies:
                results['strategies'].append({
                    'strategy_id': strategy.strategy_id,
                    'persona': strategy.persona,
                    'fitness_score': strategy.fitness_score,
                    'acceptance_rate': strategy.acceptance_rate,
                    'effectiveness_score': strategy.effectiveness_score,
                    'confidence_threshold': strategy.confidence_threshold,
                    'language_style': strategy.language_style,
                    'nudge_interval_minutes': strategy.nudge_interval_minutes,
                    'mutations': strategy.mutations
                })
            
            filename = f"outputs/evolution/generation_{generation:03d}_results.json"
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
                
        except Exception as e:
            logger.error(f"Error saving generation results: {str(e)}")
    
    async def _save_final_results(self, best_strategy: EvolutionStrategy, final_population: List[EvolutionStrategy]):
        """Save final evolution results."""
        try:
            results = {
                'evolution_completed': datetime.now().isoformat(),
                'total_generations': self.evolution_stats['total_generations'],
                'total_mutations': self.evolution_stats['total_mutations'],
                'total_crossovers': self.evolution_stats['total_crossovers'],
                'best_fitness_achieved': self.evolution_stats['best_fitness_achieved'],
                'convergence_generation': self.evolution_stats['convergence_generation'],
                'fitness_history': self.best_fitness_history,
                'best_strategy': {
                    'strategy_id': best_strategy.strategy_id if best_strategy else None,
                    'persona': best_strategy.persona if best_strategy else None,
                    'fitness_score': best_strategy.fitness_score if best_strategy else 0,
                    'acceptance_rate': best_strategy.acceptance_rate if best_strategy else 0,
                    'effectiveness_score': best_strategy.effectiveness_score if best_strategy else 0,
                    'confidence_threshold': best_strategy.confidence_threshold if best_strategy else 0,
                    'language_style': best_strategy.language_style if best_strategy else None,
                    'nudge_interval_minutes': best_strategy.nudge_interval_minutes if best_strategy else 0,
                    'timing_rules': best_strategy.timing_rules if best_strategy else {},
                    'template_preferences': best_strategy.template_preferences if best_strategy else [],
                    'generation': best_strategy.generation if best_strategy else 0,
                    'mutations': best_strategy.mutations if best_strategy else []
                } if best_strategy else None,
                'final_population_stats': {
                    'size': len(final_population),
                    'average_fitness': sum(s.fitness_score for s in final_population) / len(final_population) if final_population else 0,
                    'fitness_std': np.std([s.fitness_score for s in final_population]) if final_population else 0,
                    'persona_distribution': {}
                }
            }
            
            # Calculate persona distribution
            if final_population:
                persona_counts = {}
                for strategy in final_population:
                    persona_counts[strategy.persona] = persona_counts.get(strategy.persona, 0) + 1
                results['final_population_stats']['persona_distribution'] = persona_counts
            
            # Save to multiple files for redundancy
            with open("outputs/evolution/final_evolution_results.json", 'w') as f:
                json.dump(results, f, indent=2)
            
            with open("outputs/evolution_results.json", 'w') as f:
                json.dump(results, f, indent=2)
            
            logger.info("Final evolution results saved successfully")
            
        except Exception as e:
            logger.error(f"Error saving final results: {str(e)}")

async def main():
    """Main evolution runner."""
    import argparse
    
    parser = argparse.ArgumentParser(description='OpenEvolve AI Coach Evolution System')
    parser.add_argument('--generations', type=int, default=50, help='Number of generations to evolve')
    parser.add_argument('--population', type=int, default=50, help='Population size')
    parser.add_argument('--mutation-rate', type=float, default=0.15, help='Mutation rate')
    parser.add_argument('--crossover-rate', type=float, default=0.8, help='Crossover rate')
    
    args = parser.parse_args()
    
    print("🧬 OpenEvolve AI Coach Evolution System")
    print("=" * 50)
    print(f"Generations: {args.generations}")
    print(f"Population Size: {args.population}")
    print(f"Mutation Rate: {args.mutation_rate}")
    print(f"Crossover Rate: {args.crossover_rate}")
    print()
    
    # Initialize optimizer
    optimizer = OpenEvolveOptimizer(
        population_size=args.population,
        mutation_rate=args.mutation_rate,
        crossover_rate=args.crossover_rate
    )
    
    # Run evolution
    try:
        results = await optimizer.evolve_population(args.generations)
        
        print("🎉 Evolution Completed!")
        print(f"Best Fitness Achieved: {results['evolution_stats']['best_fitness_achieved']:.2f}")
        print(f"Total Generations: {results['evolution_stats']['total_generations']}")
        print(f"Total Mutations: {results['evolution_stats']['total_mutations']}")
        print(f"Total Crossovers: {results['evolution_stats']['total_crossovers']}")
        
        if results['best_strategy']:
            best = results['best_strategy']
            print(f"\n🏆 Best Strategy:")
            print(f"  Persona: {best.persona}")
            print(f"  Fitness: {best.fitness_score:.2f}")
            print(f"  Acceptance Rate: {best.acceptance_rate:.1%}")
            print(f"  Language Style: {best.language_style}")
            print(f"  Confidence Threshold: {best.confidence_threshold:.2f}")
            print(f"  Generation: {best.generation}")
        
    except Exception as e:
        logger.error(f"Evolution failed: {str(e)}")
        print(f"❌ Evolution failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())