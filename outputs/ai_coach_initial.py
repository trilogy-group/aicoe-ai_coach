#!/usr/bin/env python3
"""
AI Coach Proof-of-Concept System
Demonstrates WorkSmart AI coaching methodology using synthetic data and evolved prompts.
"""

import asyncio
import json
import os
import pandas as pd
from datetime import datetime, timedelta
import argparse
from typing import Dict, Any, Optional
import time
import logging
import sys
from pathlib import Path

# Ensure outputs directory exists
Path("outputs").mkdir(exist_ok=True)

# Configure logging first
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('outputs/ai_coach.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Import all modules with robust error handling
try:
    # Import robust components
    from api_clients_robust import ClaudeClient, OpenAIClient, MultiProviderLLMClient
    from fastgen_generator import FastGenTelemetryGenerator
    from openevolve_optimizer import OpenEvolveOptimizer, PromptFitnessEvaluator
    from ai_coach_analyzer import AICoachAnalyzer
    from user_simulator import UserOutcomeSimulator
    logger.info("Successfully imported all modules")
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    print(f"❌ Import error: {e}")
    print("   Make sure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)


class AICoachDemo:
    def __init__(self):
        """Initialize AI Coach Demo with robust error handling."""
        self.logger = logging.getLogger(self.__class__.__name__)

        # Initialize API clients with validation
        try:
            anthropic_key = os.getenv('ANTHROPIC_API_KEY')
            openai_key = os.getenv('OPENAI_API_KEY')

            if not anthropic_key:
                raise ValueError(
                    "ANTHROPIC_API_KEY environment variable is required")

            self.claude_client = ClaudeClient(anthropic_key)
            self.openai_client = OpenAIClient(
                openai_key) if openai_key else None

            # Multi-provider setup for fallback
            providers = {"claude": self.claude_client}
            if self.openai_client:
                providers["openai"] = self.openai_client

            self.multi_client = MultiProviderLLMClient(providers)

            self.logger.info("API clients initialized successfully")

        except Exception as e:
            self.logger.error(f"Failed to initialize API clients: {e}")
            raise

        # Initialize components
        self.data_generator = None
        self.prompt_optimizer = None
        self.coach_analyzer = None
        self.outcome_simulator = UserOutcomeSimulator()

        # Metrics tracking with additional fields
        self.session_metrics = {
            'nudges_generated': 0,
            'nudges_accepted': 0,
            'total_productivity_lift': 0.0,
            'total_satisfaction_lift': 0.0,
            'evaluation_time_seconds': [],
            'nudge_generation_time_seconds': [],
            'api_errors': 0,
            'json_parse_errors': 0,
            'start_time': datetime.now()
        }

    async def initialize_system(self, mode='inference', num_synthetic_users=50):
        """Initialize the AI Coach system in training or inference mode."""
        print(f"🚀 Initializing AI Coach System in {mode} mode...")

        # Initialize data generator
        self.data_generator = FastGenTelemetryGenerator(
            self.claude_client,
            num_users=num_synthetic_users
        )

        if mode == 'training':
            await self._training_mode_initialization()
        else:
            await self._inference_mode_initialization()

        print("✅ System initialized successfully!")

    async def _training_mode_initialization(self):
        """Initialize system for prompt evolution training."""
        print("📚 Generating training dataset...")
        training_data = await self.data_generator.generate_synthetic_dataset(n_records=5000)

        print("🧬 Starting prompt evolution...")
        self.prompt_optimizer = OpenEvolveOptimizer(self.openai_client)
        fitness_evaluator = PromptFitnessEvaluator(
            self.claude_client, training_data)

        # Load initial prompts
        from initial_prompts import INITIAL_PROMPTS

        # Evolve prompts
        evolved_prompts = await self.prompt_optimizer.evolve_prompts(
            INITIAL_PROMPTS,
            fitness_evaluator.evaluate_prompt_fitness
        )

        # Save evolved prompts
        with open('outputs/evolved_prompts.json', 'w') as f:
            json.dump(evolved_prompts, f, indent=2)

        print("💡 Prompt evolution completed! Saved to outputs/evolved_prompts.json")

        # Initialize analyzer with evolved prompts
        self.coach_analyzer = AICoachAnalyzer(
            self.claude_client, evolved_prompts)

    async def _inference_mode_initialization(self):
        """Initialize system for real-time inference."""
        # Load evolved prompts if available, otherwise use initial
        try:
            with open('outputs/evolved_prompts.json', 'r') as f:
                evolved_prompts = json.load(f)
            print("📖 Loaded evolved prompts from previous training")
        except FileNotFoundError:
            from initial_prompts import INITIAL_PROMPTS
            evolved_prompts = INITIAL_PROMPTS
            print("⚠️ Using initial prompts (no training data found)")

        # Initialize analyzer
        self.coach_analyzer = AICoachAnalyzer(
            self.claude_client, evolved_prompts)

    async def run_real_time_coaching_simulation(self, duration_minutes=60):
        """Simulate real-time coaching for specified duration."""
        print(f"🎯 Starting {duration_minutes}-minute coaching simulation...")

        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=duration_minutes)

        # Generate continuous data stream
        data_stream = self.data_generator.generate_real_time_stream()

        chunk_count = 0
        async for data_chunk in data_stream:
            if datetime.now() >= end_time:
                break

            chunk_count += 1
            await self._process_data_chunk(data_chunk, chunk_count)

            # Simulate real-time delay (15-second intervals)
            await asyncio.sleep(1)  # Accelerated for demo

        # Print final metrics
        self._print_session_summary()

    async def _process_data_chunk(self, data_chunk: pd.DataFrame, chunk_id: int):
        """Process a chunk of telemetry data and generate coaching suggestions."""
        print(f"\n📊 Processing chunk {chunk_id} ({len(data_chunk)} records)")

        # Group by user for individual analysis
        for user_id in data_chunk['user_id'].unique():
            user_data = data_chunk[data_chunk['user_id'] == user_id]
            user_persona = user_data['persona_type'].iloc[0]

            # Analyze with Claude
            start_time = time.time()
            nudge = await self.coach_analyzer.analyze_telemetry_chunk(user_data, user_id)
            analysis_time = time.time() - start_time

            self.session_metrics['evaluation_time_seconds'].append(
                analysis_time)

            if nudge:
                # Generate user response simulation
                current_context = self._extract_user_context(user_data)
                outcome = self.outcome_simulator.simulate_user_response(
                    nudge, user_persona, current_context
                )

                # Log the interaction
                self._log_coaching_interaction(
                    user_id, user_persona, nudge, outcome)

                # Update metrics
                self._update_session_metrics(nudge, outcome)

    def _extract_user_context(self, user_data: pd.DataFrame) -> list:
        """Extract contextual flags from user data."""
        context = []

        latest_record = user_data.iloc[-1]

        # Detect context patterns
        if latest_record['focus_session_duration'] > 45:
            context.append('high_focus_session')

        if user_data['interruption_count'].sum() > 10:
            context.append('multiple_interruptions')

        current_hour = datetime.fromisoformat(latest_record['timestamp']).hour
        if current_hour > 16:  # After 4 PM
            context.append('end_of_day')

        if user_data['meeting_duration_min'].sum() > 240:  # >4 hours in meetings
            context.append('meeting_heavy_day')

        return context

    def _log_coaching_interaction(self, user_id: int, persona: str, nudge: Dict, outcome: Dict):
        """Log coaching interaction with structured output."""
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'persona': persona,
            'nudge': nudge,
            'outcome': outcome,
            'effectiveness_score': self._calculate_effectiveness_score(nudge, outcome)
        }

        print(f"💬 NUDGE for User {user_id} ({persona}):")
        print(f"   Text: {nudge['nudge_text']}")
        print(
            f"   Type: {nudge['nudge_type']} | Confidence: {nudge['confidence']:.2f}")
        print(f"   Accepted: {'✅' if outcome['accepted'] else '❌'}")

        if outcome['accepted']:
            print(
                f"   Impact: +{outcome['productivity_impact']:.1%} productivity, +{outcome['satisfaction_impact']:.1%} satisfaction")

        # Write to log file for analysis
        with open('outputs/coaching_interactions.jsonl', 'a') as f:
            f.write(json.dumps(interaction) + '\n')

    def _calculate_effectiveness_score(self, nudge: Dict, outcome: Dict) -> float:
        """Calculate overall effectiveness score for the interaction."""
        if not outcome['accepted']:
            return 0.0

        # Weight different factors
        base_score = nudge['confidence'] * 0.4
        impact_score = (outcome['productivity_impact'] +
                        outcome['satisfaction_impact']) * 0.6

        return min(1.0, base_score + impact_score)

    def _update_session_metrics(self, nudge: Dict, outcome: Dict):
        """Update running session metrics."""
        self.session_metrics['nudges_generated'] += 1

        if outcome['accepted']:
            self.session_metrics['nudges_accepted'] += 1
            self.session_metrics['total_productivity_lift'] += outcome['productivity_impact']
            self.session_metrics['total_satisfaction_lift'] += outcome['satisfaction_impact']

    def _print_session_summary(self):
        """Print comprehensive session summary."""
        metrics = self.session_metrics

        print("\n" + "="*60)
        print("📈 AI COACH SESSION SUMMARY")
        print("="*60)

        # Basic counts
        acceptance_rate = (metrics['nudges_accepted'] /
                           max(1, metrics['nudges_generated'])) * 100
        print(f"Nudges Generated: {metrics['nudges_generated']}")
        print(
            f"Nudges Accepted: {metrics['nudges_accepted']} ({acceptance_rate:.1f}%)")

        # Performance metrics
        if metrics['evaluation_time_seconds']:
            avg_eval_time = sum(
                metrics['evaluation_time_seconds']) / len(metrics['evaluation_time_seconds'])
            print(f"Average Evaluation Time: {avg_eval_time:.2f} seconds")
        else:
            avg_eval_time = 0

        # Impact metrics
        if metrics['nudges_accepted'] > 0:
            avg_productivity_lift = metrics['total_productivity_lift'] / \
                metrics['nudges_accepted']
            avg_satisfaction_lift = metrics['total_satisfaction_lift'] / \
                metrics['nudges_accepted']
        else:
            avg_productivity_lift = 0
            avg_satisfaction_lift = 0

        print(f"Average Productivity Lift: +{avg_productivity_lift:.1%}")
        print(f"Average Satisfaction Lift: +{avg_satisfaction_lift:.1%}")

        # ROI calculation (based on article metrics)
        total_productivity_lift = metrics['total_productivity_lift']
        simulated_roi = total_productivity_lift * 50 * 40 * \
            83 * 13  # 50 users, 40hrs/week, $83/hr, 13 weeks

        print(f"Simulated Quarterly ROI: ${simulated_roi:,.0f}")

        # Target comparisons
        print("\n🎯 TARGET COMPARISONS:")
        print(
            f"Acceptance Rate: {acceptance_rate:.1f}% (Target: >65%) {'✅' if acceptance_rate > 65 else '❌'}")
        print(
            f"Avg Productivity Lift: +{avg_productivity_lift:.1%} (Target: >12%) {'✅' if avg_productivity_lift > 0.12 else '❌'}")
        print(
            f"Response Time: {avg_eval_time:.1f}s (Target: <5s) {'✅' if avg_eval_time < 5 else '❌'}")


async def main():
    """Main entry point for the AI Coach demonstration."""
    parser = argparse.ArgumentParser(
        description='AI Coach Proof-of-Concept System')
    parser.add_argument('--mode', choices=['training', 'inference'], default='inference',
                        help='Run in training mode (evolve prompts) or inference mode (real-time coaching)')
    parser.add_argument('--duration', type=int, default=60,
                        help='Duration of real-time simulation in minutes (inference mode only)')
    parser.add_argument('--users', type=int, default=50,
                        help='Number of synthetic users to simulate')

    args = parser.parse_args()

    # Validate API keys
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("❌ Error: ANTHROPIC_API_KEY environment variable not set")
        return

    if args.mode == 'training' and not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY environment variable required for training mode")
        return

    # Initialize and run system
    demo = AICoachDemo()
    await demo.initialize_system(mode=args.mode, num_synthetic_users=args.users)

    if args.mode == 'inference':
        await demo.run_real_time_coaching_simulation(duration_minutes=args.duration)
    else:
        print("🎓 Training completed! Run with --mode inference to see real-time coaching.")

if __name__ == "__main__":
    asyncio.run(main())
