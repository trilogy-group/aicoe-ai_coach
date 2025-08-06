"""
AI Coach Evolution System - LLM-Driven Iterative Improvement
Uses real performance feedback to evolve coaching effectiveness
"""

import os
import json
import time
import asyncio
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
import numpy as np
from openai import OpenAI
import anthropic
from coaching_evaluator import CoachingEvaluator

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AICoachEvolution:
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.anthropic_client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.evaluator = CoachingEvaluator()
        
        # Evolution parameters
        self.population_size = 10
        self.max_iterations = 20
        self.elite_ratio = 0.3  # Top 30% survive
        self.mutation_rate = 0.7
        
        # Results tracking
        self.evolution_history = []
        self.best_coaches = []
        
    def evolve_coaching_system(self, base_coach_path: str, output_dir: str = "outputs/evolved_coaches") -> Dict[str, Any]:
        """Main evolution loop - iteratively improve AI coaching system"""
        
        logger.info(f"Starting AI Coach Evolution with {self.max_iterations} iterations")
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize population with base coach
        population = self.initialize_population(base_coach_path, output_dir)
        
        generation_results = []
        
        for generation in range(self.max_iterations):
            logger.info(f"\n{'='*60}")
            logger.info(f"GENERATION {generation + 1}/{self.max_iterations}")
            logger.info(f"{'='*60}")
            
            # Evaluate entire population
            fitness_scores = []
            for i, coach_path in enumerate(population):
                logger.info(f"Evaluating coach {i+1}/{len(population)}: {os.path.basename(coach_path)}")
                
                try:
                    metrics = self.evaluator.evaluate_coach(coach_path)
                    fitness = metrics.get('composite_fitness', -1.0)
                    fitness_scores.append((fitness, coach_path, metrics))
                    
                    logger.info(f"Coach {i+1} fitness: {fitness:.4f}")
                    
                except Exception as e:
                    logger.error(f"Error evaluating coach {i+1}: {e}")
                    fitness_scores.append((-1.0, coach_path, {}))
            
            # Sort by fitness (highest first)
            fitness_scores.sort(key=lambda x: x[0], reverse=True)
            
            # Track generation results
            generation_result = {
                'generation': generation + 1,
                'best_fitness': fitness_scores[0][0],
                'avg_fitness': np.mean([f[0] for f in fitness_scores]),
                'population_size': len(population),
                'best_coach': os.path.basename(fitness_scores[0][1]),
                'timestamp': datetime.now().isoformat()
            }
            generation_results.append(generation_result)
            
            logger.info(f"Generation {generation + 1} Results:")
            logger.info(f"  Best Fitness: {generation_result['best_fitness']:.4f}")
            logger.info(f"  Average Fitness: {generation_result['avg_fitness']:.4f}")
            logger.info(f"  Best Coach: {generation_result['best_coach']}")
            
            # Save best coach of this generation
            best_coach_path = fitness_scores[0][1]
            self.save_generation_best(best_coach_path, generation + 1, output_dir)
            
            # Early stopping if we achieve excellent performance
            if fitness_scores[0][0] > 0.9:
                logger.info(f"Excellent fitness achieved ({fitness_scores[0][0]:.4f}). Stopping evolution.")
                break
            
            # Selection: Keep elite performers
            num_elite = max(1, int(len(population) * self.elite_ratio))
            elite_coaches = [coach_path for _, coach_path, _ in fitness_scores[:num_elite]]
            
            # Generate next generation
            population = self.generate_next_generation(
                elite_coaches, fitness_scores, generation + 1, output_dir
            )
        
        # Final results
        evolution_summary = {
            'total_generations': len(generation_results),
            'best_overall_fitness': max(gen['best_fitness'] for gen in generation_results),
            'final_best_coach': generation_results[-1]['best_coach'],
            'improvement_rate': generation_results[-1]['best_fitness'] - generation_results[0]['best_fitness'],
            'generation_results': generation_results,
            'evolution_completed': datetime.now().isoformat()
        }
        
        # Save evolution summary
        summary_path = os.path.join(output_dir, "evolution_summary.json")
        with open(summary_path, 'w') as f:
            json.dump(evolution_summary, f, indent=2)
        
        logger.info(f"\nEvolution completed!")
        logger.info(f"Best fitness achieved: {evolution_summary['best_overall_fitness']:.4f}")
        logger.info(f"Improvement: {evolution_summary['improvement_rate']:.4f}")
        logger.info(f"Results saved to: {output_dir}")
        
        return evolution_summary
    
    def initialize_population(self, base_coach_path: str, output_dir: str) -> List[str]:
        """Create initial population by creating variations of base coach"""
        
        logger.info("Initializing population...")
        population = [base_coach_path]  # Include original
        
        # Read base coach code
        with open(base_coach_path, 'r') as f:
            base_code = f.read()
        
        # Create variations
        for i in range(self.population_size - 1):
            variation_prompt = self.get_variation_prompt(base_code, i + 1)
            
            try:
                # Use LLM to create variation
                evolved_code = self.generate_code_variation(variation_prompt, base_code)
                
                # Save variation
                variation_path = os.path.join(output_dir, f"coach_variation_{i+1}.py")
                with open(variation_path, 'w') as f:
                    f.write(evolved_code)
                
                population.append(variation_path)
                logger.info(f"Created variation {i+1}: {os.path.basename(variation_path)}")
                
            except Exception as e:
                logger.error(f"Error creating variation {i+1}: {e}")
                population.append(base_coach_path)  # Fallback to base
        
        return population
    
    def generate_next_generation(self, elite_coaches: List[str], fitness_scores: List, generation: int, output_dir: str) -> List[str]:
        """Generate next generation through crossover and mutation"""
        
        logger.info(f"Generating generation {generation + 1}...")
        next_population = elite_coaches.copy()  # Keep elite
        
        # Get performance feedback for improvement
        performance_feedback = self.analyze_population_performance(fitness_scores)
        
        while len(next_population) < self.population_size:
            try:
                # Select parents from elite coaches
                parent1 = np.random.choice(elite_coaches)
                parent2 = np.random.choice(elite_coaches) if len(elite_coaches) > 1 else parent1
                
                # Create offspring through LLM-driven evolution
                offspring_code = self.create_offspring(parent1, parent2, performance_feedback, generation)
                
                # Save offspring
                offspring_path = os.path.join(output_dir, f"coach_gen_{generation+1}_{len(next_population)}.py")
                with open(offspring_path, 'w') as f:
                    f.write(offspring_code)
                
                next_population.append(offspring_path)
                
            except Exception as e:
                logger.error(f"Error creating offspring: {e}")
                # Fallback: add random elite
                next_population.append(np.random.choice(elite_coaches))
        
        return next_population
    
    def create_offspring(self, parent1_path: str, parent2_path: str, performance_feedback: Dict, generation: int) -> str:
        """Create offspring by combining successful traits from parents"""
        
        # Read parent codes
        with open(parent1_path, 'r') as f:
            parent1_code = f.read()
        with open(parent2_path, 'r') as f:
            parent2_code = f.read()
        
        evolution_prompt = f"""
You are an expert AI systems optimizer. Create an improved AI coaching system by combining the best traits from two successful parent systems and addressing performance feedback.

PERFORMANCE FEEDBACK FROM EVALUATION:
{json.dumps(performance_feedback, indent=2)}

PARENT 1 CODE:
```python
{parent1_code[:3000]}...
```

PARENT 2 CODE:
```python
{parent2_code[:3000]}...
```

EVOLUTION OBJECTIVES:
1. Combine the most effective coaching strategies from both parents
2. Address weaknesses identified in performance feedback
3. Enhance user satisfaction and behavioral change rates
4. Improve relevance and actionability of coaching interventions
5. Maintain psychological sophistication while increasing effectiveness

SPECIFIC IMPROVEMENTS TO IMPLEMENT:
- Enhance nudge personalization based on user context
- Improve timing and frequency of interventions
- Add more sophisticated behavioral psychology techniques
- Better integration of cognitive load and attention management
- More actionable and specific recommendations

CONSTRAINTS:
- Maintain the same class structure and method signatures
- Keep all existing functionality while improving effectiveness
- Focus on evidence-based psychological interventions
- Ensure code is production-ready and well-structured

Return ONLY the complete Python code for the evolved AI coach system.
"""

        # Generate evolved code using Claude (best for code generation)
        try:
            response = self.anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=8000,
                temperature=0.3,
                messages=[{"role": "user", "content": evolution_prompt}]
            )
            
            evolved_code = response.content[0].text
            
            # Extract just the Python code if there's extra text
            if "```python" in evolved_code:
                evolved_code = evolved_code.split("```python")[1].split("```")[0]
            
            return evolved_code.strip()
            
        except Exception as e:
            logger.error(f"Error generating offspring with Claude: {e}")
            # Fallback to parent1
            return parent1_code
    
    def analyze_population_performance(self, fitness_scores: List) -> Dict[str, Any]:
        """Analyze population performance to guide evolution"""
        
        if not fitness_scores:
            return {}
        
        # Extract metrics from fitness scores
        all_metrics = [metrics for _, _, metrics in fitness_scores if metrics]
        
        if not all_metrics:
            return {}
        
        analysis = {
            'population_size': len(fitness_scores),
            'avg_nudge_quality': np.mean([m.get('avg_nudge_quality', 0) for m in all_metrics]),
            'avg_behavioral_change': np.mean([m.get('avg_behavioral_change', 0) for m in all_metrics]),
            'avg_user_satisfaction': np.mean([m.get('avg_user_satisfaction', 0) for m in all_metrics]),
            'avg_relevance': np.mean([m.get('avg_relevance', 0) for m in all_metrics]),
            'avg_actionability': np.mean([m.get('avg_actionability', 0) for m in all_metrics]),
            'performance_variance': np.std([f for f, _, _ in fitness_scores]),
            'top_performer_fitness': fitness_scores[0][0] if fitness_scores else 0,
            'weakest_areas': self.identify_weak_areas(all_metrics),
            'improvement_opportunities': self.identify_improvements(all_metrics)
        }
        
        return analysis
    
    def identify_weak_areas(self, metrics_list: List[Dict]) -> List[str]:
        """Identify areas where the population performs poorly"""
        weak_areas = []
        
        thresholds = {
            'avg_nudge_quality': 0.6,
            'avg_behavioral_change': 0.5,
            'avg_user_satisfaction': 0.7,
            'avg_relevance': 0.6,
            'avg_actionability': 0.5
        }
        
        for metric, threshold in thresholds.items():
            values = [m.get(metric, 0) for m in metrics_list]
            if values and np.mean(values) < threshold:
                weak_areas.append(metric)
        
        return weak_areas
    
    def identify_improvements(self, metrics_list: List[Dict]) -> List[str]:
        """Identify specific improvement opportunities"""
        improvements = []
        
        avg_metrics = {
            'nudge_quality': np.mean([m.get('avg_nudge_quality', 0) for m in metrics_list]),
            'behavioral_change': np.mean([m.get('avg_behavioral_change', 0) for m in metrics_list]),
            'user_satisfaction': np.mean([m.get('avg_user_satisfaction', 0) for m in metrics_list]),
            'relevance': np.mean([m.get('avg_relevance', 0) for m in metrics_list]),
            'actionability': np.mean([m.get('avg_actionability', 0) for m in metrics_list])
        }
        
        if avg_metrics['nudge_quality'] < 0.7:
            improvements.append("Enhance psychological sophistication and research-backed content")
        
        if avg_metrics['behavioral_change'] < 0.6:
            improvements.append("Improve motivation and persuasion techniques")
        
        if avg_metrics['user_satisfaction'] < 0.7:
            improvements.append("Better personalization and user experience")
        
        if avg_metrics['relevance'] < 0.6:
            improvements.append("Improve context awareness and situational relevance")
        
        if avg_metrics['actionability'] < 0.5:
            improvements.append("Provide more specific and actionable recommendations")
        
        return improvements
    
    def get_variation_prompt(self, base_code: str, variation_num: int) -> str:
        """Generate prompt for creating code variations"""
        
        variation_strategies = [
            "Focus on enhancing psychological depth and research citations",
            "Improve personalization and context awareness",
            "Enhance actionability and specific recommendations", 
            "Optimize for different personality types and work styles",
            "Strengthen behavioral change motivation techniques",
            "Improve timing and frequency of interventions",
            "Add more sophisticated cognitive load management",
            "Enhance user satisfaction through better UX",
            "Strengthen evidence-based intervention selection"
        ]
        
        strategy = variation_strategies[variation_num % len(variation_strategies)]
        
        return f"""
Create an improved version of this AI coaching system with the following focus: {strategy}

Original code structure should be maintained, but improve the coaching effectiveness by:
1. Enhancing the specific area mentioned above
2. Maintaining all existing functionality
3. Adding psychological sophistication where relevant
4. Improving user engagement and satisfaction

Return ONLY the complete Python code.
"""
    
    def generate_code_variation(self, prompt: str, base_code: str) -> str:
        """Generate code variation using LLM"""
        
        full_prompt = f"{prompt}\n\nBASE CODE:\n```python\n{base_code}\n```"
        
        try:
            response = self.anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=8000,
                temperature=0.4,
                messages=[{"role": "user", "content": full_prompt}]
            )
            
            evolved_code = response.content[0].text
            
            # Extract Python code if wrapped
            if "```python" in evolved_code:
                evolved_code = evolved_code.split("```python")[1].split("```")[0]
            
            return evolved_code.strip()
            
        except Exception as e:
            logger.error(f"Error generating variation: {e}")
            return base_code  # Fallback to original
    
    def save_generation_best(self, best_coach_path: str, generation: int, output_dir: str):
        """Save the best coach from each generation"""
        
        with open(best_coach_path, 'r') as f:
            best_code = f.read()
        
        best_path = os.path.join(output_dir, f"best_coach_gen_{generation}.py")
        with open(best_path, 'w') as f:
            f.write(best_code)
        
        logger.info(f"Saved best coach from generation {generation}: {os.path.basename(best_path)}")


def evolve_ai_coach(base_coach_path: str, max_iterations: int = 20, population_size: int = 10) -> Dict[str, Any]:
    """Main function to evolve AI coaching system"""
    
    evolution_system = AICoachEvolution()
    evolution_system.max_iterations = max_iterations
    evolution_system.population_size = population_size
    
    return evolution_system.evolve_coaching_system(base_coach_path)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        base_coach = sys.argv[1]
    else:
        base_coach = "/Users/stanhus/Documents/work/ai_coach/ai_coach.py"
    
    # Set evolution parameters
    max_iter = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    pop_size = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    
    print(f"Starting AI Coach Evolution...")
    print(f"Base coach: {base_coach}")
    print(f"Max iterations: {max_iter}")
    print(f"Population size: {pop_size}")
    
    results = evolve_ai_coach(base_coach, max_iter, pop_size)
    print(f"\nEvolution completed!")
    print(f"Best fitness: {results['best_overall_fitness']:.4f}")
    print(f"Improvement: {results['improvement_rate']:.4f}")