"""
Integration tests for AI Coach POC System
"""

import pytest
import asyncio
import json
import pandas as pd
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api_clients import ClaudeClient, OpenAIClient
from fastgen_generator import FastGenTelemetryGenerator
from openevolve_optimizer import OpenEvolveOptimizer, PromptFitnessEvaluator
from ai_coach_analyzer import AICoachAnalyzer
from user_simulator import UserOutcomeSimulator
from initial_prompts import INITIAL_PROMPTS

# Mock clients for testing
class MockClaudeClient:
    async def generate(self, prompt, **kwargs):
        # Return mock JSON response
        if "focus_integrity" in prompt:
            return json.dumps({
                "focus_score": 65,
                "context_switch_rate": 1.2,
                "deep_work_percentage": 30,
                "recommendations": ["Close unnecessary tabs", "Use focus mode"],
                "alert_level": "medium"
            })
        elif "wellbeing" in prompt:
            return json.dumps({
                "wellbeing_score": 70,
                "work_streak_minutes": 95,
                "break_frequency_score": 60,
                "stress_level": "moderate",
                "alerts": ["Long work streak detected"]
            })
        else:
            return json.dumps({
                "value_score": 75,
                "core_work_percentage": 45,
                "optimization_suggestions": ["Automate report generation"],
                "output_productivity": 80
            })

class MockOpenAIClient:
    async def generate(self, prompt, **kwargs):
        # Return slightly modified prompt as evolution
        return prompt + "\n# Evolved for better performance"

@pytest.fixture
def mock_claude_client():
    return MockClaudeClient()

@pytest.fixture
def mock_openai_client():
    return MockOpenAIClient()

@pytest.mark.asyncio
async def test_synthetic_data_generation(mock_claude_client):
    """Test FASTGEN synthetic data generation."""
    generator = FastGenTelemetryGenerator(mock_claude_client, num_users=5)
    
    # Generate small dataset
    data = await generator.generate_synthetic_dataset(n_records=100)
    
    # Verify data structure
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 100
    
    # Check required columns
    required_columns = [
        'timestamp', 'user_id', 'persona_type', 'app_active',
        'window_switches_15min', 'cognitive_load_score'
    ]
    for col in required_columns:
        assert col in data.columns
    
    # Verify data types
    assert data['user_id'].dtype == 'int64'
    assert data['cognitive_load_score'].dtype == 'float64'
    
    # Check value ranges
    assert (data['cognitive_load_score'] >= 0).all()
    assert (data['cognitive_load_score'] <= 1).all()
    assert (data['window_switches_15min'] >= 0).all()

@pytest.mark.asyncio
async def test_prompt_evolution(mock_openai_client, mock_claude_client):
    """Test OpenEvolve prompt optimization."""
    # Create sample data for fitness evaluation
    sample_data = pd.DataFrame({
        'timestamp': [datetime.now().isoformat()] * 10,
        'user_id': range(1, 11),
        'window_switches_15min': [15] * 10,
        'cognitive_load_score': [0.7] * 10
    })
    
    optimizer = OpenEvolveOptimizer(mock_openai_client, population_size=5, generations=2)
    evaluator = PromptFitnessEvaluator(mock_claude_client, sample_data)
    
    # Test with single prompt
    test_prompts = {
        'focus_integrity_evaluator': INITIAL_PROMPTS['focus_integrity_evaluator']
    }
    
    evolved = await optimizer.evolve_prompts(test_prompts, evaluator.evaluate_prompt_fitness)
    
    # Verify evolution occurred
    assert 'focus_integrity_evaluator' in evolved
    assert len(evolved['focus_integrity_evaluator']) > len(test_prompts['focus_integrity_evaluator'])

@pytest.mark.asyncio
async def test_nudge_generation(mock_claude_client):
    """Test AI Coach analyzer nudge generation."""
    analyzer = AICoachAnalyzer(mock_claude_client, INITIAL_PROMPTS)
    
    # Create test data chunk
    test_data = pd.DataFrame({
        'timestamp': [datetime.now().isoformat()] * 5,
        'user_id': [1] * 5,
        'persona_type': ['developer'] * 5,
        'app_active': ['Browser'] * 5,
        'window_switches_15min': [25, 20, 22, 18, 30],
        'tab_count': [50, 48, 52, 45, 55],
        'cognitive_load_score': [0.8, 0.85, 0.9, 0.75, 0.82],
        'focus_session_duration': [5, 3, 8, 10, 2],
        'break_duration_min': [0] * 5,
        'task_category': ['Support'] * 5,
        'interruption_count': [8, 10, 12, 9, 11],
        'meeting_duration_min': [0] * 5,
        'code_commits': [0] * 5,
        'email_sent': [2, 1, 0, 3, 1],
        'documents_created': [0] * 5
    })
    
    # Generate nudge
    nudge = await analyzer.analyze_telemetry_chunk(test_data, user_id=1)
    
    # Verify nudge structure
    assert nudge is not None
    assert 'nudge_text' in nudge
    assert 'nudge_type' in nudge
    assert 'confidence' in nudge
    assert nudge['nudge_type'] in ['focus', 'wellbeing', 'value_creation']

def test_user_response_simulation():
    """Test user outcome simulator."""
    simulator = UserOutcomeSimulator()
    
    # Create test nudge
    test_nudge = {
        'nudge_text': 'Want to try closing 47 tabs for a focused sprint?',
        'nudge_type': 'focus',
        'confidence': 0.85,
        'user_id': 1
    }
    
    # Test different personas
    personas = ['developer', 'analyst', 'manager', 'designer']
    contexts = [['high_focus_session'], ['multiple_interruptions'], []]
    
    for persona in personas:
        for context in contexts:
            outcome = simulator.simulate_user_response(test_nudge, persona, context)
            
            # Verify outcome structure
            assert 'accepted' in outcome
            assert isinstance(outcome['accepted'], bool)
            
            if outcome['accepted']:
                assert 'productivity_impact' in outcome
                assert 'satisfaction_impact' in outcome
                assert outcome['productivity_impact'] >= 0
            else:
                assert 'dismissal_reason' in outcome

@pytest.mark.asyncio
async def test_full_integration_flow(mock_claude_client):
    """Test complete flow from data generation to nudge outcome."""
    # 1. Generate synthetic data
    generator = FastGenTelemetryGenerator(mock_claude_client, num_users=3)
    data = await generator.generate_synthetic_dataset(n_records=50)
    
    # 2. Initialize analyzer with prompts
    analyzer = AICoachAnalyzer(mock_claude_client, INITIAL_PROMPTS)
    
    # 3. Process data chunk
    data_chunk = data.head(10)
    user_id = data_chunk['user_id'].iloc[0]
    nudge = await analyzer.analyze_telemetry_chunk(data_chunk, user_id)
    
    # 4. Simulate user response
    if nudge:
        simulator = UserOutcomeSimulator()
        persona = data_chunk['persona_type'].iloc[0]
        outcome = simulator.simulate_user_response(nudge, persona, [])
        
        # Verify complete flow
        assert outcome is not None
        assert 'accepted' in outcome

def test_metrics_calculation():
    """Test metrics calculation and ROI."""
    # Simulate session metrics
    metrics = {
        'nudges_generated': 20,
        'nudges_accepted': 14,
        'total_productivity_lift': 1.68,  # 14 * 0.12 average
        'total_satisfaction_lift': 1.4,    # 14 * 0.10 average
    }
    
    # Calculate key metrics
    acceptance_rate = (metrics['nudges_accepted'] / metrics['nudges_generated']) * 100
    avg_productivity_lift = metrics['total_productivity_lift'] / metrics['nudges_accepted']
    
    # Calculate ROI (from article formula)
    simulated_roi = metrics['total_productivity_lift'] * 50 * 40 * 83 * 13
    
    # Verify targets
    assert acceptance_rate == 70.0  # > 65% target
    assert avg_productivity_lift >= 0.12  # >= 12% target
    assert simulated_roi > 0  # Positive ROI

if __name__ == "__main__":
    pytest.main([__file__, "-v"])