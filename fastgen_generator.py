"""
FASTGEN-based Synthetic Telemetry Data Generator
Generates realistic WorkSmart-like telemetry data using LLM-guided distribution modeling.
"""

import pandas as pd
import numpy as np
import json
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import random

class MetadataEnricher:
    """Enriches field metadata using Claude for better synthetic data generation."""
    
    def __init__(self, claude_client):
        self.claude = claude_client
        self.metadata_cache = {}
    
    async def enrich_field_metadata(self, field_name: str, sample_values: List[Any]) -> Dict:
        """Generate metadata for a field based on sample values."""
        if field_name in self.metadata_cache:
            return self.metadata_cache[field_name]
        
        prompt = f"""
        Analyze telemetry field '{field_name}' with samples: {sample_values[:10]}
        
        Generate metadata for synthetic data generation:
        1. Data type and range
        2. Distribution pattern (normal, log-normal, poisson, etc.)
        3. Time-based patterns (hourly, daily, weekly)
        4. Persona correlations
        5. Realistic constraints
        
        Output as JSON with keys: type, distribution, temporal_pattern, correlations, constraints
        """
        
        try:
            response = await self.claude.generate(prompt, max_tokens=500)
            metadata = json.loads(response)
            self.metadata_cache[field_name] = metadata
            return metadata
        except:
            # Fallback to default metadata
            return self._get_default_metadata(field_name)
    
    def _get_default_metadata(self, field_name: str) -> Dict:
        """Default metadata for common fields."""
        defaults = {
            'keystrokes_per_min': {
                'type': 'int',
                'distribution': 'log_normal',
                'params': {'mu': 3.5, 'sigma': 0.8},
                'constraints': {'min': 0, 'max': 200}
            },
            'window_switches_15min': {
                'type': 'int',
                'distribution': 'negative_binomial',
                'params': {'n': 5, 'p': 0.3},
                'constraints': {'min': 0, 'max': 50}
            },
            'cognitive_load_score': {
                'type': 'float',
                'distribution': 'beta',
                'params': {'alpha': 2, 'beta': 3},
                'constraints': {'min': 0.0, 'max': 1.0}
            }
        }
        return defaults.get(field_name, {
            'type': 'float',
            'distribution': 'normal',
            'params': {'mu': 0.5, 'sigma': 0.2},
            'constraints': {'min': 0, 'max': 1}
        })

class TemporalPatternGenerator:
    """Generates time-based patterns for realistic workplace data."""
    
    def __init__(self):
        # Daily productivity curve (8AM to 6PM)
        self.daily_productivity_curve = np.array([
            0.3, 0.4, 0.6, 0.8, 0.95,  # 8AM-12PM - morning ramp up
            0.7, 0.6, 0.8, 0.85, 0.7   # 1PM-5PM - post-lunch patterns
        ])
        
        self.weekly_pattern = {
            'monday': 0.85,
            'tuesday': 0.95,
            'wednesday': 1.1,
            'thursday': 1.0,
            'friday': 0.75
        }
    
    def apply_temporal_modifiers(self, base_value: float, timestamp: datetime, 
                                field_name: str) -> float:
        """Apply time-based modifiers to a base value."""
        hour = timestamp.hour
        if 8 <= hour <= 17:
            hour_index = hour - 8
            hour_modifier = self.daily_productivity_curve[min(hour_index, 9)]
        else:
            hour_modifier = 0.2  # After hours activity
        
        day_name = timestamp.strftime('%A').lower()
        day_modifier = self.weekly_pattern.get(day_name, 1.0)
        
        # Ultradian rhythm (90-minute cycles)
        minutes_since_midnight = timestamp.hour * 60 + timestamp.minute
        ultradian_phase = minutes_since_midnight / 90
        ultradian_modifier = 0.15 * np.sin(2 * np.pi * ultradian_phase) + 1.0
        
        return base_value * hour_modifier * day_modifier * ultradian_modifier

class PersonaModelGenerator:
    """Generates persona-specific behavior patterns."""
    
    PERSONA_CONFIGS = {
        'developer': {
            'app_preferences': {
                'VSCode': 0.4, 
                'Browser': 0.3, 
                'Terminal': 0.15, 
                'Slack': 0.1,
                'Other': 0.05
            },
            'focus_patterns': {
                'deep_work_blocks': 120,  # minutes
                'context_switch_tolerance': 'low',
                'switch_rate_multiplier': 0.7
            },
            'productivity_peak': [10, 11, 12],  # hours
            'break_frequency': 90,  # minutes
            'meeting_load': 0.2,  # 20% of time
            'cognitive_load_base': 0.7
        },
        'analyst': {
            'app_preferences': {
                'Excel': 0.3,
                'Browser': 0.25,
                'PowerBI': 0.2,
                'Email': 0.15,
                'Other': 0.1
            },
            'focus_patterns': {
                'deep_work_blocks': 90,
                'context_switch_tolerance': 'medium',
                'switch_rate_multiplier': 1.0
            },
            'productivity_peak': [14, 15, 16],  # hours
            'break_frequency': 60,
            'meeting_load': 0.3,
            'cognitive_load_base': 0.6
        },
        'manager': {
            'app_preferences': {
                'Email': 0.3,
                'Slack': 0.25,
                'Zoom': 0.2,
                'Browser': 0.15,
                'Other': 0.1
            },
            'focus_patterns': {
                'deep_work_blocks': 45,
                'context_switch_tolerance': 'high',
                'switch_rate_multiplier': 1.5
            },
            'productivity_peak': [9, 10, 11],  # hours
            'break_frequency': 45,
            'meeting_load': 0.5,
            'cognitive_load_base': 0.5
        },
        'designer': {
            'app_preferences': {
                'Figma': 0.35,
                'Browser': 0.25,
                'Photoshop': 0.2,
                'Slack': 0.15,
                'Other': 0.05
            },
            'focus_patterns': {
                'deep_work_blocks': 150,
                'context_switch_tolerance': 'very_low',
                'switch_rate_multiplier': 0.5
            },
            'productivity_peak': [10, 11, 14, 15],  # hours
            'break_frequency': 120,
            'meeting_load': 0.15,
            'cognitive_load_base': 0.8
        }
    }
    
    def get_persona_config(self, persona_type: str) -> Dict:
        """Get configuration for a specific persona."""
        return self.PERSONA_CONFIGS.get(persona_type, self.PERSONA_CONFIGS['developer'])

class FastGenTelemetryGenerator:
    """Main generator for synthetic WorkSmart telemetry data."""
    
    def __init__(self, claude_client, num_users: int = 50, days_of_data: int = 30):
        self.claude = claude_client
        self.num_users = num_users
        self.days_of_data = days_of_data
        
        self.metadata_enricher = MetadataEnricher(claude_client)
        self.temporal_gen = TemporalPatternGenerator()
        self.persona_gen = PersonaModelGenerator()
        
        # Initialize user personas
        self.users = self._initialize_user_personas()
    
    def _initialize_user_personas(self) -> List[Dict]:
        """Create a diverse set of user personas."""
        users = []
        persona_distribution = {
            'developer': 0.4,
            'analyst': 0.3,
            'manager': 0.2,
            'designer': 0.1
        }
        
        for user_id in range(1, self.num_users + 1):
            # Assign persona based on distribution
            rand = random.random()
            cumulative = 0
            persona_type = 'developer'
            
            for persona, prob in persona_distribution.items():
                cumulative += prob
                if rand <= cumulative:
                    persona_type = persona
                    break
            
            users.append({
                'id': user_id,
                'persona_type': persona_type,
                'skill_level': random.uniform(0.5, 1.0),
                'experience_years': random.randint(1, 15)
            })
        
        return users
    
    async def generate_synthetic_dataset(self, n_records: int = 10000) -> pd.DataFrame:
        """Generate a complete synthetic dataset."""
        print(f"📊 Generating {n_records} synthetic telemetry records...")
        
        all_records = []
        timestamps = self._generate_time_series()
        
        record_count = 0
        for timestamp in timestamps:
            if record_count >= n_records:
                break
                
            # Generate records for subset of users (simulating not all users active at once)
            active_users = random.sample(self.users, k=random.randint(10, min(30, len(self.users))))
            
            for user in active_users:
                if record_count >= n_records:
                    break
                    
                record = await self._generate_record(user, timestamp)
                all_records.append(record)
                record_count += 1
            
            # Progress indicator
            if record_count % 1000 == 0:
                print(f"  Generated {record_count}/{n_records} records...")
        
        df = pd.DataFrame(all_records)
        print(f"✅ Generated {len(df)} synthetic records")
        
        # Save to CSV for inspection
        df.to_csv('outputs/synthetic_telemetry.csv', index=False)
        
        return df
    
    def _generate_time_series(self) -> List[datetime]:
        """Generate realistic timestamp series."""
        timestamps = []
        start_date = datetime.now() - timedelta(days=self.days_of_data)
        
        current_time = start_date.replace(hour=8, minute=0, second=0)
        end_time = datetime.now()
        
        while current_time < end_time:
            # Skip weekends
            if current_time.weekday() < 5:  # Monday = 0, Friday = 4
                # Generate timestamps every 1-5 minutes during work hours
                if 8 <= current_time.hour <= 18:
                    timestamps.append(current_time)
            
            # Move to next timestamp
            current_time += timedelta(minutes=random.randint(1, 5))
        
        return timestamps
    
    async def _generate_record(self, user: Dict, timestamp: datetime) -> Dict:
        """Generate a single telemetry record."""
        persona_config = self.persona_gen.get_persona_config(user['persona_type'])
        
        # Base activity level
        base_activity = self.temporal_gen.apply_temporal_modifiers(
            1.0, timestamp, 'base_activity'
        )
        
        # Choose active application based on persona preferences
        app_active = np.random.choice(
            list(persona_config['app_preferences'].keys()),
            p=list(persona_config['app_preferences'].values())
        )
        
        # Generate correlated metrics
        record = {
            'timestamp': timestamp.isoformat(),
            'user_id': user['id'],
            'persona_type': user['persona_type'],
            'app_active': app_active,
            'window_title': self._generate_window_title(app_active),
            'tab_count': self._generate_tab_count(user['persona_type'], base_activity),
            'window_switches_15min': self._generate_window_switches(
                persona_config, base_activity
            ),
            'keystrokes_per_min': self._generate_keystrokes(
                app_active, base_activity, user['skill_level']
            ),
            'mouse_clicks_per_min': self._generate_mouse_clicks(app_active, base_activity),
            'break_duration_min': self._generate_break_duration(timestamp, persona_config),
            'task_category': self._determine_task_category(app_active, user['persona_type']),
            'cognitive_load_score': self._calculate_cognitive_load(persona_config, base_activity),
            'focus_session_duration': self._generate_focus_duration(persona_config),
            'interruption_count': self._generate_interruptions(base_activity),
            'meeting_duration_min': self._generate_meeting_duration(
                timestamp, persona_config['meeting_load']
            ),
            'code_commits': self._generate_commits(user['persona_type'], timestamp),
            'email_sent': self._generate_emails(user['persona_type'], base_activity),
            'documents_created': self._generate_documents(user['persona_type'], base_activity)
        }
        
        return record
    
    def _generate_window_title(self, app: str) -> str:
        """Generate realistic window titles."""
        titles = {
            'VSCode': ['main.py - ai_coach', 'index.js - project', 'README.md - docs'],
            'Browser': ['Dashboard - Analytics', 'Google Search', 'Stack Overflow'],
            'Slack': ['#general - Team Chat', '#dev-team - Discussion', 'Direct Messages'],
            'Email': ['Inbox - 23 unread', 'Compose - Project Update', 'Calendar - Today'],
            'Excel': ['Q4_Analysis.xlsx', 'Budget_2025.xlsx', 'Data_Export.csv'],
            'Zoom': ['Team Standup', 'Client Meeting', '1:1 with Manager']
        }
        return random.choice(titles.get(app, ['Untitled']))
    
    def _generate_tab_count(self, persona_type: str, activity_level: float) -> int:
        """Generate browser tab count based on persona."""
        base_tabs = {
            'developer': 15,
            'analyst': 20,
            'manager': 25,
            'designer': 10
        }
        base = base_tabs.get(persona_type, 15)
        return max(1, int(np.random.poisson(base * activity_level)))
    
    def _generate_window_switches(self, persona_config: Dict, activity_level: float) -> int:
        """Generate context switch count."""
        base_rate = 8 * persona_config['focus_patterns']['switch_rate_multiplier']
        return max(0, int(np.random.poisson(base_rate * activity_level)))
    
    def _generate_keystrokes(self, app: str, activity_level: float, skill_level: float) -> int:
        """Generate keystroke rate."""
        app_rates = {
            'VSCode': 120,
            'Email': 80,
            'Slack': 60,
            'Browser': 40,
            'Excel': 50
        }
        base_rate = app_rates.get(app, 50)
        return max(0, int(np.random.lognormal(
            np.log(base_rate * activity_level * skill_level), 0.5
        )))
    
    def _generate_mouse_clicks(self, app: str, activity_level: float) -> int:
        """Generate mouse click rate."""
        app_rates = {
            'Browser': 30,
            'Excel': 40,
            'Figma': 50,
            'PowerBI': 35,
            'VSCode': 20
        }
        base_rate = app_rates.get(app, 25)
        return max(0, int(np.random.poisson(base_rate * activity_level)))
    
    def _generate_break_duration(self, timestamp: datetime, persona_config: Dict) -> int:
        """Generate break duration based on patterns."""
        # Check if it's time for a break
        minutes_since_start = (timestamp.hour - 8) * 60 + timestamp.minute
        break_interval = persona_config['break_frequency']
        
        if minutes_since_start % break_interval < 5:  # Within 5 minutes of break time
            return random.randint(5, 15)
        return 0
    
    def _determine_task_category(self, app: str, persona_type: str) -> str:
        """Categorize current task."""
        categories = {
            'VSCode': 'Core',
            'Excel': 'Core' if persona_type == 'analyst' else 'Support',
            'Email': 'Admin',
            'Slack': 'Support',
            'Browser': 'Support',  # Could be research or distraction
            'Zoom': 'Support',
            'Figma': 'Core' if persona_type == 'designer' else 'Support'
        }
        return categories.get(app, 'Support')
    
    def _calculate_cognitive_load(self, persona_config: Dict, activity_level: float) -> float:
        """Calculate cognitive load score."""
        base_load = persona_config['cognitive_load_base']
        variation = np.random.beta(2, 3) * 0.3  # Add some variation
        return min(1.0, base_load * activity_level + variation)
    
    def _generate_focus_duration(self, persona_config: Dict) -> int:
        """Generate current focus session duration."""
        max_duration = persona_config['focus_patterns']['deep_work_blocks']
        # Exponential decay - most sessions are shorter
        return int(np.random.exponential(max_duration / 3))
    
    def _generate_interruptions(self, activity_level: float) -> int:
        """Generate interruption count."""
        base_rate = 3  # Average interruptions per hour
        return max(0, int(np.random.poisson(base_rate * activity_level)))
    
    def _generate_meeting_duration(self, timestamp: datetime, meeting_load: float) -> int:
        """Generate meeting duration for current period."""
        # Meetings more common 9-11 AM and 2-4 PM
        hour = timestamp.hour
        if hour in [9, 10, 14, 15]:
            if random.random() < meeting_load:
                return random.choice([30, 60])  # 30 or 60 minute meetings
        return 0
    
    def _generate_commits(self, persona_type: str, timestamp: datetime) -> int:
        """Generate code commits (developers only)."""
        if persona_type != 'developer':
            return 0
        
        # Commits typically happen in afternoon
        if timestamp.hour >= 14 and random.random() < 0.1:
            return random.randint(1, 3)
        return 0
    
    def _generate_emails(self, persona_type: str, activity_level: float) -> int:
        """Generate emails sent."""
        base_rates = {
            'manager': 15,
            'analyst': 8,
            'developer': 3,
            'designer': 5
        }
        base_rate = base_rates.get(persona_type, 5)
        
        if random.random() < 0.3:  # 30% chance of sending emails
            return max(0, int(np.random.poisson(base_rate * activity_level)))
        return 0
    
    def _generate_documents(self, persona_type: str, activity_level: float) -> int:
        """Generate documents created."""
        creation_rates = {
            'analyst': 0.3,
            'designer': 0.4,
            'developer': 0.2,
            'manager': 0.15
        }
        
        if random.random() < creation_rates.get(persona_type, 0.2) * activity_level:
            return 1
        return 0
    
    def generate_real_time_stream(self):
        """Generate continuous stream of telemetry data for real-time simulation."""
        async def stream_generator():
            while True:
                # Generate data for current time window
                current_time = datetime.now()
                active_users = random.sample(
                    self.users, 
                    k=random.randint(5, min(20, len(self.users)))
                )
                
                records = []
                for user in active_users:
                    record = await self._generate_record(user, current_time)
                    records.append(record)
                
                yield pd.DataFrame(records)
                
                # Wait before generating next batch
                await asyncio.sleep(1)  # 1 second for demo
        
        return stream_generator()