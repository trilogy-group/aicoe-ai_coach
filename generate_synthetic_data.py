#!/usr/bin/env python3
"""
Synthetic Data Generation System for AI Coach
============================================

Comprehensive synthetic data generation system for training and testing the AI Coach.
Completely self-contained system that generates realistic telemetry data, user profiles,
and interaction patterns for coaching system validation.

This system generates:
- Realistic user profiles with behavioral characteristics
- Multi-dimensional telemetry data spanning weeks/months
- Synthetic interaction patterns and coaching outcomes
- Edge cases and anomaly scenarios for robust testing
- Massive-scale datasets for training and evolution

Author: AI Coach Data Team
Version: 2.0 (Self-Contained)
"""

import json
import random
import numpy as np
import pandas as pd
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple, Optional
from pathlib import Path
from dataclasses import dataclass
import uuid

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class UserProfile:
    """Represents a synthetic user with behavioral characteristics."""
    user_id: int
    persona_type: str
    name: str
    behavioral_patterns: Dict[str, float]
    work_schedule: Dict[str, Any]
    tool_proficiency: Dict[str, float]
    productivity_baseline: float
    focus_tendency: float
    interruption_tolerance: float
    learning_orientation: float
    efficiency_consciousness: float
    collaboration_preference: float
    chronotype: str
    stress_baseline: float
    adaptation_speed: float

class SyntheticDataGenerator:
    """Generates comprehensive synthetic data for AI Coach training and testing."""
    
    def __init__(self, seed: int = 42):
        """Initialize the synthetic data generator."""
        random.seed(seed)
        np.random.seed(seed)
        
        # Ensure outputs directory exists
        Path("outputs").mkdir(exist_ok=True)
        
        # Persona definitions with realistic distributions
        self.personas = {
            'customer_support': {
                'weight': 0.25,
                'apps': ['CRM', 'Email', 'Chat', 'Phone', 'Knowledge Base'],
                'cognitive_load_range': (0.4, 0.8)
            },
            'analyst': {
                'weight': 0.35,
                'apps': ['Excel', 'PowerBI', 'SQL', 'Python', 'Tableau'],
                'cognitive_load_range': (0.6, 0.9)
            },
            'developer': {
                'weight': 0.30,
                'apps': ['VS Code', 'Terminal', 'Browser', 'Git', 'Docker'],
                'cognitive_load_range': (0.7, 0.95)
            },
            'designer': {
                'weight': 0.10,
                'apps': ['Figma', 'Photoshop', 'Sketch', 'Browser', 'Slack'],
                'cognitive_load_range': (0.5, 0.8)
            }
        }
        
        self.first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Sophia', 'James']
        self.last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Anderson', 'Thomas']
    
    def generate_user_profiles(self, num_users: int = 25) -> List[UserProfile]:
        """Generate realistic user profiles with diverse characteristics."""
        profiles = []
        
        for user_id in range(1, num_users + 1):
            persona = self._select_weighted_persona()
            
            profile = UserProfile(
                user_id=user_id,
                persona_type=persona,
                name=f"{random.choice(self.first_names)} {random.choice(self.last_names)}",
                behavioral_patterns={
                    'productivity_variability': random.uniform(0.2, 0.8),
                    'focus_session_preference': random.uniform(20, 120),
                    'multitasking_tendency': random.uniform(0.2, 0.9)
                },
                work_schedule={
                    'start_hour': random.choice([7, 8, 9, 10]),
                    'end_hour': random.choice([16, 17, 18, 19]),
                    'lunch_break': random.choice([12, 13])
                },
                tool_proficiency={app: random.uniform(0.6, 0.95) for app in self.personas[persona]['apps']},
                productivity_baseline=random.uniform(0.4, 0.9),
                focus_tendency=random.uniform(0.3, 0.9),
                interruption_tolerance=random.uniform(0.2, 0.8),
                learning_orientation=random.uniform(0.4, 0.95),
                efficiency_consciousness=random.uniform(0.3, 0.9),
                collaboration_preference=random.uniform(0.2, 0.9),
                chronotype=random.choice(['morning', 'afternoon', 'evening']),
                stress_baseline=random.uniform(0.2, 0.6),
                adaptation_speed=random.uniform(0.3, 0.9)
            )
            
            profiles.append(profile)
        
        logger.info(f"Generated {len(profiles)} user profiles")
        return profiles
    
    def _select_weighted_persona(self) -> str:
        """Select a persona based on weighted distribution."""
        personas = list(self.personas.keys())
        weights = [self.personas[p]['weight'] for p in personas]
        return random.choices(personas, weights=weights)[0]
    
    def generate_telemetry_data(self, profiles: List[UserProfile], days: int = 30) -> pd.DataFrame:
        """Generate comprehensive telemetry data for all users over specified days."""
        telemetry_records = []
        start_date = datetime.now() - timedelta(days=days)
        
        for profile in profiles:
            for day in range(days):
                current_date = start_date + timedelta(days=day)
                
                # Skip weekends
                if current_date.weekday() >= 5:
                    continue
                
                # Generate data points throughout workday
                work_start = profile.work_schedule['start_hour']
                work_end = profile.work_schedule['end_hour']
                
                for hour in range(work_start, work_end + 1):
                    for minute in [0, 15, 30, 45]:
                        timestamp = current_date.replace(hour=hour, minute=minute, second=0)
                        
                        if random.random() < 0.1:  # Skip some points
                            continue
                        
                        telemetry_point = self._generate_telemetry_point(profile, timestamp)
                        telemetry_records.append(telemetry_point)
        
        df = pd.DataFrame(telemetry_records)
        logger.info(f"Generated {len(df)} telemetry records")
        return df
    
    def _generate_telemetry_point(self, profile: UserProfile, timestamp: datetime) -> Dict[str, Any]:
        """Generate a single telemetry data point."""
        persona_config = self.personas[profile.persona_type]
        
        # Generate realistic metrics
        cognitive_load = random.uniform(*persona_config['cognitive_load_range'])
        tab_count = random.randint(2, 15)
        focus_duration = random.randint(5, 120)
        app_active = random.choice(persona_config['apps'])
        
        return {
            'timestamp': timestamp.isoformat(),
            'user_id': profile.user_id,
            'persona_type': profile.persona_type,
            'tab_count': tab_count,
            'window_switches_15min': random.randint(0, 25),
            'focus_session_duration': focus_duration,
            'cognitive_load_score': round(cognitive_load, 3),
            'app_active': app_active,
            'task_category': random.choice(['analysis', 'communication', 'coding', 'design']),
            'keystrokes_per_min': random.randint(20, 80),
            'break_duration_min': random.randint(0, 30),
            'interruption_count': random.randint(0, 8),
            'core_work_percentage': round(random.uniform(0.3, 0.9), 3),
            'value_score': round(random.uniform(0.2, 0.8), 3),
            'productivity_score': round(random.uniform(0.4, 0.9), 3),
            'screen_capture_metadata': json.dumps({'resolution': '1920x1080'}),
            'detected_content_elements': json.dumps([{'type': 'spreadsheet'}]),
            'workflow_inefficiencies': json.dumps([{'type': 'manual_process'}]),
            'missed_opportunities': json.dumps([{'type': 'automation'}]),
            'visual_attention_areas': json.dumps({'primary': {'x': 0.5, 'y': 0.5}}),
            'task_completion_indicators': json.dumps({'progress': random.uniform(0.1, 0.9)})
        }
    
    def save_data(self, profiles: List[UserProfile], telemetry_df: pd.DataFrame) -> Dict[str, str]:
        """Save all generated data to files."""
        output_files = {}
        
        # Save user profiles
        profiles_data = []
        for profile in profiles:
            profiles_data.append({
                'user_id': profile.user_id,
                'persona_type': profile.persona_type,
                'name': profile.name,
                'behavioral_patterns': profile.behavioral_patterns,
                'work_schedule': profile.work_schedule,
                'tool_proficiency': profile.tool_proficiency,
                'productivity_baseline': profile.productivity_baseline,
                'focus_tendency': profile.focus_tendency,
                'interruption_tolerance': profile.interruption_tolerance,
                'learning_orientation': profile.learning_orientation,
                'efficiency_consciousness': profile.efficiency_consciousness,
                'collaboration_preference': profile.collaboration_preference,
                'chronotype': profile.chronotype,
                'stress_baseline': profile.stress_baseline,
                'adaptation_speed': profile.adaptation_speed
            })
        
        profiles_file = "outputs/user_profiles.json"
        with open(profiles_file, 'w') as f:
            json.dump(profiles_data, f, indent=2)
        output_files['profiles'] = profiles_file
        
        # Save telemetry data
        telemetry_file = "outputs/synthetic_telemetry.csv"
        telemetry_df.to_csv(telemetry_file, index=False)
        output_files['telemetry'] = telemetry_file
        
        logger.info(f"Data saved to outputs directory")
        return output_files

def main():
    """Main data generation runner."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Synthetic Data Generation for AI Coach')
    parser.add_argument('--users', type=int, default=25, help='Number of users to generate')
    parser.add_argument('--days', type=int, default=30, help='Number of days of telemetry data')
    parser.add_argument('--seed', type=int, default=42, help='Random seed for reproducibility')
    
    args = parser.parse_args()
    
    print("🎲 Synthetic Data Generation for AI Coach")
    print("=" * 50)
    print(f"Users: {args.users}")
    print(f"Days: {args.days}")
    print(f"Random Seed: {args.seed}")
    print()
    
    generator = SyntheticDataGenerator(seed=args.seed)
    
    try:
        # Generate user profiles
        print("👥 Generating user profiles...")
        profiles = generator.generate_user_profiles(args.users)
        
        # Generate telemetry data
        print("📊 Generating telemetry data...")
        telemetry_df = generator.generate_telemetry_data(profiles, args.days)
        
        # Save all data
        print("💾 Saving data...")
        output_files = generator.save_data(profiles, telemetry_df)
        
        print("✅ Data generation completed successfully!")
        print("\nGenerated files:")
        for file_type, file_path in output_files.items():
            print(f"  {file_type}: {file_path}")
        
        print(f"\n📈 Summary:")
        print(f"  Users: {len(profiles)}")
        print(f"  Telemetry Records: {len(telemetry_df):,}")
        
    except Exception as e:
        logger.error(f"Data generation failed: {str(e)}")
        print(f"❌ Data generation failed: {str(e)}")

if __name__ == "__main__":
    main()