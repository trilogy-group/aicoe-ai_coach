# AI Coach - Intelligent Productivity Coaching System

AI-powered productivity coach that provides real-time, personalized guidance based on user telemetry. Evolved through 101 generations using behavioral psychology and machine learning.

## Quick Start

### Installation

```bash
git clone [repository-url]
cd ai_coach
pip install -r requirements.txt
```

### Basic Usage

```bash
# Run AI coach demo
python ai_coach.py

# Create telemetry data and get coaching
telemetry = {
    'keystrokes_per_min': 45,
    'mouse_events_per_min': 20,
    'error_rate': 0.05,
    'app_switches_per_hour': 15,
    'last_break_time': '2024-01-15T10:30:00'
}

from ai_coach import AICoach
coach = AICoach()
notification = await coach.analyze_telemetry(telemetry, user_id="user123")
```

### Run Evolution System

```bash
# Standard evolution
python evolve_ai_coach.py --mode standard

# Rapid evolution  
python evolve_ai_coach.py --mode rapid

# Overnight evolution
python evolve_ai_coach.py --mode overnight
```

### Generate Synthetic Data

```bash
# Generate training data
python synthetic_data_generator.py

# Or programmatically:
from synthetic_data_generator import SyntheticDataGenerator
generator = SyntheticDataGenerator()
data = generator.generate_coaching_interactions(num_interactions=100)
```

## Files

- **`ai_coach.py`** - Complete AI coaching system (1,091 lines)
- **`evolve_ai_coach.py`** - Evolution system (712 lines)  
- **`synthetic_data_generator.py`** - Data generation (418 lines)
- **`outputs/`** - Generated data, logs, evolution results

## API

```python
# Main coaching interface
async def analyze_telemetry(telemetry: Dict, user_id: str) -> Optional[Dict]:
    """Returns coaching notification or None"""

# Evolution interface  
async def run_evolution(mode: str = "standard") -> Dict:
    """Runs evolution process, returns results"""

# Data generation interface
def generate_coaching_interactions(num_interactions: int) -> List[Dict]:
    """Generates synthetic coaching data"""
```

## Requirements

- Python 3.8+
- No external dependencies (self-contained)
- Optional: OpenAI API key for evolution (set in .env)