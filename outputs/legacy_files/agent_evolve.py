#!/usr/bin/env python3
"""
Agent-Evolve Framework
=====================

A framework for continuously improving AI agents through code evolution,
synthetic data generation, and reinforcement learning from human feedback.

Inspired by the OpenEvolve approach but adapted for agent improvement.
"""

import ast
import inspect
import json
import logging
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable
import asyncio
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EvolutionTarget:
    """Represents a code component marked for evolution"""
    
    def __init__(self, name: str, code: str, file_path: str, line_number: int, target_type: str):
        self.name = name
        self.code = code
        self.file_path = file_path
        self.line_number = line_number
        self.target_type = target_type  # 'prompt', 'tool', 'function'
        self.dependencies = []
        self.metadata = {}

def evolve(target_type: str = "auto", description: str = "", priority: int = 1):
    """
    Decorator to mark functions, prompts, or tools for evolution
    
    Args:
        target_type: Type of evolution target ('prompt', 'tool', 'function', 'auto')
        description: Description of what this component does
        priority: Evolution priority (1=high, 2=medium, 3=low)
    """
    def decorator(func_or_var):
        # Store evolution metadata
        if hasattr(func_or_var, '__call__'):
            func_or_var.__evolve_metadata__ = {
                'target_type': target_type if target_type != "auto" else "function",
                'description': description,
                'priority': priority,
                'marked_for_evolution': True
            }
        else:
            # For variables/constants, we need to track them differently
            setattr(func_or_var, '__evolve_metadata__', {
                'target_type': target_type if target_type != "auto" else "prompt",
                'description': description,
                'priority': priority,
                'marked_for_evolution': True
            })
        return func_or_var
    return decorator

class AgentEvolve:
    """Main framework for agent evolution"""
    
    def __init__(self, work_dir: str = "./evolution_workspace"):
        self.work_dir = Path(work_dir)
        self.staging_dir = self.work_dir / "staging"
        self.evaluators_dir = self.work_dir / "evaluators"
        self.training_data_dir = self.work_dir / "training_data"
        self.results_dir = self.work_dir / "results"
        
        # Create directories
        for dir_path in [self.work_dir, self.staging_dir, self.evaluators_dir, 
                        self.training_data_dir, self.results_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def extract_targets(self, source_paths: List[str]) -> List[EvolutionTarget]:
        """Extract all evolution targets from source code"""
        targets = []
        
        for source_path in source_paths:
            path = Path(source_path)
            if path.is_file() and path.suffix == '.py':
                targets.extend(self._extract_from_file(path))
            elif path.is_dir():
                for py_file in path.rglob('*.py'):
                    targets.extend(self._extract_from_file(py_file))
        
        logger.info(f"Extracted {len(targets)} evolution targets")
        return targets
    
    def _extract_from_file(self, file_path: Path) -> List[EvolutionTarget]:
        """Extract evolution targets from a single Python file"""
        targets = []
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Parse AST to find decorated functions and variables
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check for @evolve decorator
                    for decorator in node.decorator_list:
                        if (isinstance(decorator, ast.Name) and decorator.id == 'evolve') or \
                           (isinstance(decorator, ast.Call) and 
                            isinstance(decorator.func, ast.Name) and 
                            decorator.func.id == 'evolve'):
                            
                            func_code = ast.get_source_segment(content, node)
                            target = EvolutionTarget(
                                name=node.name,
                                code=func_code,
                                file_path=str(file_path),
                                line_number=node.lineno,
                                target_type="function"
                            )
                            targets.append(target)
                            break
                
                # Look for variables with @evolve comments
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            # Check for #@evolve() comment above assignment
                            lines = content.split('\n')
                            if node.lineno > 1:
                                prev_line = lines[node.lineno - 2].strip()
                                if prev_line.startswith('#@evolve'):
                                    var_code = lines[node.lineno - 1]
                                    evolution_target = EvolutionTarget(
                                        name=target.id,
                                        code=var_code,
                                        file_path=str(file_path),
                                        line_number=node.lineno,
                                        target_type="prompt"
                                    )
                                    targets.append(evolution_target)
        
        except Exception as e:
            logger.error(f"Error parsing {file_path}: {e}")
        
        return targets
    
    def stage_targets(self, targets: List[EvolutionTarget]) -> None:
        """Stage evolution targets for processing"""
        for target in targets:
            target_dir = self.staging_dir / f"{target.name}_{target.target_type}"
            target_dir.mkdir(exist_ok=True)
            
            # Save target code
            with open(target_dir / "target.py", 'w') as f:
                f.write(f"# Evolution target: {target.name}\n")
                f.write(f"# Type: {target.target_type}\n")
                f.write(f"# Source: {target.file_path}:{target.line_number}\n\n")
                f.write(target.code)
            
            # Save metadata
            metadata = {
                'name': target.name,
                'target_type': target.target_type,
                'source_file': target.file_path,
                'line_number': target.line_number,
                'timestamp': datetime.now().isoformat()
            }
            
            with open(target_dir / "metadata.json", 'w') as f:
                json.dump(metadata, f, indent=2)
    
    async def generate_training_data(self, target: EvolutionTarget, num_samples: int = 30) -> List[Dict]:
        """Generate synthetic training data for a target"""
        
        training_data = []
        
        if target.target_type == "function":
            # Generate function test cases
            for i in range(num_samples):
                test_case = {
                    'input': f"test_input_{i}",
                    'expected_behavior': f"expected_output_{i}",
                    'context': f"test_context_{i}",
                    'success_criteria': ['functionality', 'performance', 'maintainability']
                }
                training_data.append(test_case)
        
        elif target.target_type == "prompt":
            # Generate prompt test scenarios
            for i in range(num_samples):
                scenario = {
                    'user_input': f"sample_user_query_{i}",
                    'context': f"scenario_context_{i}",
                    'expected_response_quality': ['relevance', 'helpfulness', 'accuracy'],
                    'success_metrics': ['user_satisfaction', 'task_completion']
                }
                training_data.append(scenario)
        
        # Save training data
        target_dir = self.staging_dir / f"{target.name}_{target.target_type}"
        with open(target_dir / "training_data.json", 'w') as f:
            json.dump(training_data, f, indent=2)
        
        logger.info(f"Generated {len(training_data)} training samples for {target.name}")
        return training_data
    
    def generate_evaluator(self, target: EvolutionTarget) -> str:
        """Generate evaluator code for a target"""
        
        evaluator_template = f'''
import json
import asyncio
from typing import Dict, List, Any, Tuple

class {target.name.title()}Evaluator:
    """Evaluator for {target.name} ({target.target_type})"""
    
    def __init__(self):
        self.metrics = {{
            'functionality': 0.0,
            'performance': 0.0,
            'user_satisfaction': 0.0,
            'maintainability': 0.0
        }}
    
    async def evaluate(self, evolved_code: str, test_data: List[Dict]) -> float:
        """Evaluate evolved code against test data"""
        total_score = 0.0
        
        for test_case in test_data:
            score = await self._evaluate_single_case(evolved_code, test_case)
            total_score += score
        
        return total_score / len(test_data) if test_data else 0.0
    
    async def _evaluate_single_case(self, code: str, test_case: Dict) -> float:
        """Evaluate a single test case"""
        # Implement specific evaluation logic based on target type
        score = 0.5  # Placeholder
        
        # Add target-specific evaluation logic here
        if "{target.target_type}" == "function":
            score += self._evaluate_function_quality(code, test_case)
        elif "{target.target_type}" == "prompt":
            score += self._evaluate_prompt_effectiveness(code, test_case)
        
        return min(score, 1.0)
    
    def _evaluate_function_quality(self, code: str, test_case: Dict) -> float:
        """Evaluate function code quality"""
        quality_score = 0.0
        
        # Check for proper error handling
        if "try:" in code and "except:" in code:
            quality_score += 0.2
        
        # Check for documentation
        if '"""' in code or "'" + "''" in code:
            quality_score += 0.2
        
        # Check for type hints
        if "->" in code and ":" in code:
            quality_score += 0.1
        
        return quality_score
    
    def _evaluate_prompt_effectiveness(self, prompt: str, test_case: Dict) -> float:
        """Evaluate prompt effectiveness"""
        effectiveness_score = 0.0
        
        # Check for clear instructions
        if len(prompt.split()) > 10:
            effectiveness_score += 0.2
        
        # Check for context awareness
        if "context" in prompt.lower():
            effectiveness_score += 0.2
        
        # Check for specific guidance
        if any(word in prompt.lower() for word in ["please", "should", "must", "consider"]):
            effectiveness_score += 0.1
        
        return effectiveness_score

# Usage
evaluator = {target.name.title()}Evaluator()
'''
        
        # Save evaluator
        evaluator_file = self.evaluators_dir / f"{target.name}_evaluator.py"
        with open(evaluator_file, 'w') as f:
            f.write(evaluator_template)
        
        logger.info(f"Generated evaluator for {target.name}")
        return evaluator_template
    
    def create_openevolve_config(self, target: EvolutionTarget) -> Dict:
        """Create OpenEvolve configuration for a target"""
        config = {
            'target_file': f"staging/{target.name}_{target.target_type}/target.py",
            'evaluator_file': f"evaluators/{target.name}_evaluator.py",
            'training_data_file': f"staging/{target.name}_{target.target_type}/training_data.json",
            'output_dir': f"results/{target.name}",
            'evolution_params': {
                'population_size': 10,
                'generations': 50,
                'mutation_rate': 0.1,
                'crossover_rate': 0.8
            },
            'llm_config': {
                'model': 'claude-3-sonnet-20240229',
                'temperature': 0.7,
                'max_tokens': 4000
            }
        }
        
        config_file = self.work_dir / f"{target.name}_config.yaml"
        with open(config_file, 'w') as f:
            # Convert to YAML format (simplified)
            for key, value in config.items():
                f.write(f"{key}: {json.dumps(value)}\n")
        
        return config

# CLI interface functions
async def main():
    """Main CLI interface"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agent_evolve.py <command> [args]")
        print("Commands: extract_targets, generate_training_data, generate_evaluators, run_evolution")
        return
    
    command = sys.argv[1]
    agent_evolve = AgentEvolve()
    
    if command == "extract_targets":
        source_paths = sys.argv[2:] if len(sys.argv) > 2 else ['.']
        targets = agent_evolve.extract_targets(source_paths)
        agent_evolve.stage_targets(targets)
        print(f"Extracted and staged {len(targets)} evolution targets")
    
    elif command == "generate_training_data":
        # Load staged targets and generate training data
        for target_dir in agent_evolve.staging_dir.iterdir():
            if target_dir.is_dir():
                metadata_file = target_dir / "metadata.json"
                if metadata_file.exists():
                    with open(metadata_file) as f:
                        metadata = json.load(f)
                    
                    target = EvolutionTarget(
                        name=metadata['name'],
                        code="",  # Will be loaded from target.py
                        file_path=metadata['source_file'],
                        line_number=metadata['line_number'],
                        target_type=metadata['target_type']
                    )
                    
                    await agent_evolve.generate_training_data(target)
    
    elif command == "generate_evaluators":
        # Generate evaluators for all staged targets
        for target_dir in agent_evolve.staging_dir.iterdir():
            if target_dir.is_dir():
                metadata_file = target_dir / "metadata.json"
                if metadata_file.exists():
                    with open(metadata_file) as f:
                        metadata = json.load(f)
                    
                    target = EvolutionTarget(
                        name=metadata['name'],
                        code="",
                        file_path=metadata['source_file'],
                        line_number=metadata['line_number'],
                        target_type=metadata['target_type']
                    )
                    
                    agent_evolve.generate_evaluator(target)
                    agent_evolve.create_openevolve_config(target)

if __name__ == "__main__":
    asyncio.run(main())