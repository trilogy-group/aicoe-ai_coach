"""
OpenEvolve-based Prompt Optimization System
Evolves evaluation prompts using LLM-guided genetic algorithms.
"""

import random
import json
import asyncio
from typing import Dict, List, Tuple, Callable, Any
import numpy as np
from datetime import datetime

class ProgramDatabase:
    """Stores and manages evolved prompts with their fitness scores."""
    
    def __init__(self):
        self.programs = {}  # {id: {'prompt': str, 'fitness': float, 'generation': int}}
        self.generation_counter = 0
        self.best_programs = []  # Track top performers
    
    def add_program(self, prompt_id: str, prompt: str, fitness: float, generation: int):
        """Add a program to the database."""
        self.programs[f"{prompt_id}_gen{generation}"] = {
            'prompt': prompt,
            'fitness': fitness,
            'generation': generation,
            'timestamp': datetime.now().isoformat()
        }
        
        # Update best programs list
        self.best_programs.append((prompt_id, prompt, fitness))
        self.best_programs.sort(key=lambda x: x[2], reverse=True)
        self.best_programs = self.best_programs[:10]  # Keep top 10
    
    def get_best_programs(self, n: int = 5) -> List[Tuple[str, str, float]]:
        """Get the n best programs."""
        return self.best_programs[:n]
    
    def save_to_file(self, filename: str):
        """Save database to JSON file."""
        with open(filename, 'w') as f:
            json.dump({
                'programs': self.programs,
                'best_programs': self.best_programs,
                'generation_counter': self.generation_counter
            }, f, indent=2)

class PromptSampler:
    """Builds prompts for evolution using various strategies."""
    
    def __init__(self, openai_client):
        self.openai = openai_client
    
    async def build_evolution_prompt(self, parent_prompts: List[Tuple[str, float]], 
                                   target: str) -> str:
        """Build a prompt that guides the LLM to evolve better prompts."""
        best_performers = sorted(parent_prompts, key=lambda x: x[1], reverse=True)[:3]
        
        evolution_prompt = f"""
You are evolving prompts for an AI coaching system. Your goal is to create better evaluation prompts.

Target evaluator: {target}

Top performing parent prompts (with fitness scores):
"""
        
        for i, (prompt, fitness) in enumerate(best_performers, 1):
            evolution_prompt += f"\n{i}. (Fitness: {fitness:.3f})\n{prompt}\n"
        
        evolution_prompt += f"""
Key requirements for the evolved prompt:
1. Must evaluate workplace telemetry data effectively
2. Must produce valid JSON output with required fields
3. Should be clear, specific, and actionable
4. Should consider context and patterns in the data
5. Should generate helpful coaching suggestions

Based on the parent prompts above, create an IMPROVED prompt that:
- Combines the best elements from high-performing parents
- Fixes any weaknesses you identify
- Maintains consistency with the {target} purpose
- Optimizes for user engagement and behavior change

Output only the new evolved prompt:
"""
        
        return evolution_prompt

class OpenEvolveOptimizer:
    """Main optimizer using OpenEvolve methodology."""
    
    def __init__(self, openai_client, population_size: int = 20, generations: int = 50):
        self.openai = openai_client
        self.population_size = population_size
        self.generations = generations
        self.program_db = ProgramDatabase()
        self.prompt_sampler = PromptSampler(openai_client)
        
        # Evolution parameters
        self.elite_ratio = 0.2  # Keep top 20%
        self.crossover_probability = 0.7
        self.mutation_probability = 0.3
        
        # Tracking
        self.evolution_history = []
    
    async def evolve_prompts(self, initial_prompts: Dict[str, str], 
                            fitness_function: Callable) -> Dict[str, str]:
        """Evolve prompts over multiple generations."""
        print(f"🧬 Starting evolution with {self.population_size} population, {self.generations} generations")
        
        # Initialize population for each evaluator
        evolved_prompts = {}
        
        for evaluator_name, initial_prompt in initial_prompts.items():
            print(f"\n📊 Evolving {evaluator_name}...")
            evolved_prompt = await self._evolve_single_evaluator(
                evaluator_name, initial_prompt, fitness_function
            )
            evolved_prompts[evaluator_name] = evolved_prompt
        
        # Save evolution history
        self.program_db.save_to_file('outputs/evolution_history.json')
        
        return evolved_prompts
    
    async def _evolve_single_evaluator(self, evaluator_name: str, initial_prompt: str,
                                      fitness_function: Callable) -> str:
        """Evolve a single evaluator prompt."""
        # Initialize population
        population = await self._initialize_population(evaluator_name, initial_prompt)
        
        for generation in range(self.generations):
            print(f"  Generation {generation + 1}/{self.generations}")
            
            # Evaluate fitness
            evaluated_population = []
            for prompt in population:
                fitness = await fitness_function(evaluator_name, prompt)
                evaluated_population.append((prompt, fitness))
                
                # Track in database
                self.program_db.add_program(
                    evaluator_name, prompt, fitness, generation
                )
            
            # Sort by fitness
            evaluated_population.sort(key=lambda x: x[1], reverse=True)
            
            # Log best fitness
            best_fitness = evaluated_population[0][1]
            avg_fitness = np.mean([f for _, f in evaluated_population])
            print(f"    Best fitness: {best_fitness:.3f}, Avg: {avg_fitness:.3f}")
            
            self.evolution_history.append({
                'generation': generation,
                'evaluator': evaluator_name,
                'best_fitness': best_fitness,
                'avg_fitness': avg_fitness
            })
            
            # Check for convergence
            if generation > 10 and self._check_convergence(evaluator_name):
                print(f"    ✓ Converged at generation {generation}")
                break
            
            # Generate next generation
            population = await self._generate_next_generation(
                evaluator_name, evaluated_population
            )
        
        # Return best prompt
        best_prompts = self.program_db.get_best_programs(1)
        return best_prompts[0][1] if best_prompts else initial_prompt
    
    async def _initialize_population(self, evaluator_name: str, 
                                   initial_prompt: str) -> List[str]:
        """Initialize population with variations of the initial prompt."""
        population = [initial_prompt]  # Include original
        
        # Generate variations
        while len(population) < self.population_size:
            if random.random() < 0.5:
                # Mutation of initial prompt
                mutated = await self._mutate_prompt(initial_prompt, evaluator_name)
                population.append(mutated)
            else:
                # Slight variation
                variation = await self._create_variation(initial_prompt, evaluator_name)
                population.append(variation)
        
        return population[:self.population_size]
    
    async def _generate_next_generation(self, evaluator_name: str,
                                       evaluated_population: List[Tuple[str, float]]) -> List[str]:
        """Generate next generation using genetic operations."""
        next_generation = []
        
        # Elitism - keep top performers
        elite_count = max(1, int(self.population_size * self.elite_ratio))
        for prompt, _ in evaluated_population[:elite_count]:
            next_generation.append(prompt)
        
        # Generate offspring
        while len(next_generation) < self.population_size:
            if random.random() < self.crossover_probability:
                # Crossover between two parents
                parent1 = self._tournament_selection(evaluated_population)
                parent2 = self._tournament_selection(evaluated_population)
                
                if parent1 != parent2:
                    child = await self._crossover_prompts(parent1[0], parent2[0], evaluator_name)
                    next_generation.append(child)
                else:
                    # If same parent selected, mutate instead
                    child = await self._mutate_prompt(parent1[0], evaluator_name)
                    next_generation.append(child)
            else:
                # Mutation
                parent = self._tournament_selection(evaluated_population)
                child = await self._mutate_prompt(parent[0], evaluator_name)
                next_generation.append(child)
        
        return next_generation[:self.population_size]
    
    def _tournament_selection(self, population: List[Tuple[str, float]], 
                            tournament_size: int = 3) -> Tuple[str, float]:
        """Select individual using tournament selection."""
        tournament = random.sample(population, min(tournament_size, len(population)))
        return max(tournament, key=lambda x: x[1])
    
    async def _crossover_prompts(self, prompt1: str, prompt2: str, 
                                evaluator_name: str) -> str:
        """Perform crossover between two prompts."""
        crossover_prompt = f"""
Combine these two evaluation prompts to create a better version for {evaluator_name}:

Prompt A:
{prompt1}

Prompt B:
{prompt2}

Create a hybrid that:
1. Takes the best structural elements from both
2. Maintains clear evaluation criteria
3. Ensures consistent JSON output format
4. Optimizes for actionable coaching suggestions
5. Preserves the specific focus of {evaluator_name}

Important: The output must be a complete, self-contained prompt.

Output only the improved prompt:
"""
        
        response = await self.openai.generate(
            crossover_prompt,
            model="gpt-4o",
            temperature=0.7,
            max_tokens=1500
        )
        
        return response.strip()
    
    async def _mutate_prompt(self, prompt: str, evaluator_name: str) -> str:
        """Perform mutation on a prompt."""
        mutation_types = [
            "improve clarity and specificity",
            "enhance evaluation criteria",
            "optimize JSON output structure",
            "increase actionability of recommendations",
            "add more contextual awareness"
        ]
        
        mutation_type = random.choice(mutation_types)
        
        mutation_prompt = f"""
Improve this {evaluator_name} evaluation prompt by focusing on: {mutation_type}

Current prompt:
{prompt}

Requirements:
1. Maintain the core purpose and functionality
2. Keep JSON output format consistent
3. Make targeted improvements based on: {mutation_type}
4. Ensure the prompt remains clear and executable

Output only the improved prompt:
"""
        
        response = await self.openai.generate(
            mutation_prompt,
            model="gpt-4o-mini",  # Use faster model for mutations
            temperature=0.8,
            max_tokens=1500
        )
        
        return response.strip()
    
    async def _create_variation(self, prompt: str, evaluator_name: str) -> str:
        """Create a variation of the prompt."""
        variation_prompt = f"""
Create a variation of this {evaluator_name} evaluation prompt that maintains its core functionality but explores a different approach:

Original prompt:
{prompt}

Create a variation that:
1. Maintains the same evaluation goals
2. Uses a different structure or phrasing
3. Keeps the JSON output format
4. Might emphasize different aspects of the evaluation

Output only the variation prompt:
"""
        
        response = await self.openai.generate(
            variation_prompt,
            model="gpt-4o-mini",
            temperature=0.9,
            max_tokens=1500
        )
        
        return response.strip()
    
    def _check_convergence(self, evaluator_name: str, window: int = 5) -> bool:
        """Check if evolution has converged."""
        if len(self.evolution_history) < window:
            return False
        
        recent_history = [h for h in self.evolution_history[-window:] 
                         if h['evaluator'] == evaluator_name]
        
        if len(recent_history) < window:
            return False
        
        # Check if best fitness hasn't improved significantly
        fitness_values = [h['best_fitness'] for h in recent_history]
        fitness_std = np.std(fitness_values)
        
        return fitness_std < 0.01  # Converged if very little variation

class PromptFitnessEvaluator:
    """Evaluates fitness of evolved prompts."""
    
    def __init__(self, claude_client, synthetic_data_sample):
        self.claude = claude_client
        self.test_data = synthetic_data_sample
        self.evaluation_cache = {}  # Cache results for efficiency
    
    async def evaluate_prompt_fitness(self, prompt_id: str, prompt_text: str) -> float:
        """Evaluate fitness of a prompt using multiple criteria."""
        # Check cache
        cache_key = f"{prompt_id}_{hash(prompt_text)}"
        if cache_key in self.evaluation_cache:
            return self.evaluation_cache[cache_key]
        
        total_score = 0.0
        test_cases = min(10, len(self.test_data) // 50)  # Adaptive test cases
        weights = {
            'json_validity': 0.3,
            'actionability': 0.3,
            'consistency': 0.2,
            'completeness': 0.2
        }
        
        test_results = []
        
        for i in range(test_cases):
            # Select random data chunk
            start_idx = random.randint(0, len(self.test_data) - 50)
            data_chunk = self.test_data.iloc[start_idx:start_idx + 50]
            
            try:
                # Test prompt with Claude
                result = await self._test_prompt_with_claude(prompt_text, data_chunk)
                
                # Evaluate different aspects
                scores = {
                    'json_validity': self._score_json_validity(result),
                    'actionability': self._score_actionability(result),
                    'consistency': self._score_consistency(result, prompt_id),
                    'completeness': self._score_completeness(result, prompt_id)
                }
                
                # Calculate weighted score
                test_score = sum(scores[k] * weights[k] for k in scores)
                test_results.append(test_score)
                
            except Exception as e:
                # Penalize prompts that cause errors
                print(f"    ⚠️ Evaluation error: {str(e)[:50]}...")
                test_results.append(0.0)
        
        # Final fitness is average of test results
        fitness = np.mean(test_results) if test_results else 0.0
        
        # Cache result
        self.evaluation_cache[cache_key] = fitness
        
        return fitness
    
    async def _test_prompt_with_claude(self, prompt_text: str, data_chunk) -> str:
        """Test a prompt with Claude API."""
        # Format prompt with data
        filled_prompt = prompt_text.format(telemetry_chunk=data_chunk.to_json())
        
        # Add instruction to ensure JSON output
        full_prompt = filled_prompt + "\n\nRemember to output valid JSON only."
        
        response = await self.claude.generate(
            full_prompt,
            max_tokens=800,
            temperature=0.3  # Lower temperature for consistency
        )
        
        return response
    
    def _score_json_validity(self, result: str) -> float:
        """Score based on valid JSON output."""
        try:
            parsed = json.loads(result)
            # Check if it's a dictionary (not a list or primitive)
            if isinstance(parsed, dict):
                return 1.0
            return 0.5
        except json.JSONDecodeError:
            # Try to extract JSON from the response
            import re
            json_match = re.search(r'\{.*\}', result, re.DOTALL)
            if json_match:
                try:
                    json.loads(json_match.group())
                    return 0.7  # Partial credit for embedded JSON
                except:
                    pass
            return 0.0
    
    def _score_actionability(self, result: str) -> float:
        """Score based on actionability of recommendations."""
        try:
            parsed = json.loads(result)
        except:
            return 0.0
        
        score = 0.0
        
        # Check for recommendations/suggestions
        recommendation_keys = ['recommendations', 'suggestions', 'optimization_suggestions', 
                             'alerts', 'actions', 'nudges']
        
        for key in recommendation_keys:
            if key in parsed and isinstance(parsed[key], list) and len(parsed[key]) > 0:
                score += 0.5
                
                # Check quality of recommendations
                recommendations = parsed[key]
                if all(isinstance(r, str) and len(r) > 10 for r in recommendations[:3]):
                    score += 0.3  # Good quality recommendations
                
                if len(recommendations) >= 2:
                    score += 0.2  # Multiple recommendations
                
                break
        
        return min(1.0, score)
    
    def _score_consistency(self, result: str, prompt_id: str) -> float:
        """Score based on output consistency."""
        try:
            parsed = json.loads(result)
        except:
            return 0.0
        
        # Expected fields for each evaluator
        expected_fields = {
            'focus_integrity_evaluator': ['focus_score', 'recommendations'],
            'wellbeing_evaluator': ['wellbeing_score', 'alerts'],
            'value_creation_evaluator': ['value_score', 'optimization_suggestions']
        }
        
        required_fields = expected_fields.get(prompt_id, ['score', 'recommendations'])
        
        # Check if all required fields are present
        fields_present = sum(1 for field in required_fields if field in parsed)
        
        return fields_present / len(required_fields)
    
    def _score_completeness(self, result: str, prompt_id: str) -> float:
        """Score based on completeness of evaluation."""
        try:
            parsed = json.loads(result)
        except:
            return 0.0
        
        score = 0.0
        
        # Check for numeric scores
        score_keys = [k for k in parsed.keys() if 'score' in k]
        if score_keys:
            for key in score_keys:
                if isinstance(parsed[key], (int, float)) and 0 <= parsed[key] <= 100:
                    score += 0.3
                    break
        
        # Check for detailed analysis fields
        analysis_indicators = ['rate', 'percentage', 'count', 'duration', 'level']
        analysis_fields = sum(1 for k in parsed.keys() 
                            if any(indicator in k for indicator in analysis_indicators))
        
        if analysis_fields > 0:
            score += min(0.4, analysis_fields * 0.1)
        
        # Check for contextual information
        if any(k in parsed for k in ['alert_level', 'confidence', 'severity', 'priority']):
            score += 0.3
        
        return min(1.0, score)