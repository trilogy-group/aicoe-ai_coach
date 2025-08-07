# AI Coach - Personal Productivity Coaching System

An AI-powered productivity coach that monitors your real computer activity and provides personalized coaching suggestions through desktop notifications.

## Features

✅ **Real-Time Activity Monitoring**
- Browser tab and URL tracking (Chrome, Safari, Firefox)
- Window title and application focus detection
- Keyboard and mouse activity monitoring
- Automatic activity classification (productive, research, communication, entertainment)

✅ **Intelligent Coaching**
- Machine learning pattern recognition
- Personalized recommendations based on your work habits
- Predictive burnout prevention
- Context-aware interventions

✅ **Desktop Notifications**
- macOS native notifications
- Smart timing with cooldown periods
- Priority-based alerting

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd ai_coach

# Install required packages
pip install -r requirements.txt
```

### Requirements

- Python 3.8+
- macOS (for full functionality)
- Required packages:
  - `pynput` - keyboard/mouse monitoring
  - `psutil` - system monitoring
  - `numpy` - data processing

## Usage

### 1. Demo Mode (Simulated Data)

Test the AI coaching logic with simulated telemetry:

```bash
python ai_coach.py
# Choose option 1
```

### 2. Real Monitoring Mode (Your Actual Activity)

Monitor your real computer activity and receive personalized coaching:

```bash
python ai_coach.py
# Choose option 2
# Enter your name when prompted
```

#### macOS Permissions Required

For real monitoring, grant accessibility permissions:
1. Open **System Preferences > Security & Privacy**
2. Click **Privacy** tab > **Accessibility**
3. Add **Terminal** (or your Python app)
4. Enable the checkbox ✅

## How It Works

The AI Coach monitors your activity patterns and provides timely interventions:

- **Focus Protection**: When you're in deep work, it suggests protecting your focus time
- **Break Reminders**: After extended work sessions, it recommends breaks
- **Distraction Alerts**: When context-switching is high, it suggests refocusing
- **Productivity Insights**: Real-time feedback on your work patterns

### Activity Classification

Your activities are automatically classified as:
- 💼 **Productive**: Coding, documents, spreadsheets
- 🔍 **Research**: Browsing, documentation, learning
- 💬 **Communication**: Email, Slack, messaging
- 🎮 **Entertainment**: Social media, videos, games

### Scoring Metrics

- **Focus Quality** (0.0-1.0): Measures concentration based on app switching and activity patterns
- **Productivity Score** (0.0-1.0): Weighted score of time spent on productive vs. non-productive activities
- **Energy Level** (0.0-1.0): Estimated based on activity intensity
- **Stress Level** (0.0-1.0): Calculated from switching patterns and session duration

## Privacy

All data stays on your local machine. No telemetry is sent to external servers. Your activity data is only used for real-time coaching and is not permanently stored.

## Evolution System (Optional)

For developers interested in improving the AI coach:

```bash
# Evolve the coaching algorithms
python evolve_ai_coach.py --mode standard

# Generate synthetic training data
python synthetic_data_generator.py
```

## API Usage

```python
from ai_coach import AICoach

# Initialize coach
coach = AICoach()

# Analyze telemetry (async)
import asyncio

async def get_coaching():
    telemetry = {
        'keystrokes_per_min': 45,
        'mouse_events_per_min': 20,
        'app_switches_per_hour': 15,
        'energy_level': 0.7,
        'focus_quality': 0.8
    }
    
    notification = await coach.analyze_telemetry(telemetry, user_id="user123")
    if notification:
        print(f"Coach says: {notification['message']}")

asyncio.run(get_coaching())
```

## File Structure

```
ai_coach/
├── ai_coach.py           # Main coaching system with monitoring
├── evolve_ai_coach.py    # Evolution system for improving algorithms
├── synthetic_data_generator.py  # Generate training data
├── outputs/              # Generated data and evolution results
└── README.md            # This file
```

## Troubleshooting

**No notifications appearing?**
- Check macOS notification settings
- Ensure Terminal has accessibility permissions
- Notifications have a 5-minute cooldown

**Keyboard/mouse not tracked?**
- Grant accessibility permissions in System Preferences
- Restart Terminal after granting permissions

**Browser tabs not detected?**
- Works with Chrome, Safari, and Firefox
- Browser must be the active window

## License

MIT License - See LICENSE file for details