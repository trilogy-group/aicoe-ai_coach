#!/usr/bin/env python3
"""
Synthetic Data Generator for AI Coach Testing
Generates realistic user telemetry data and behavior patterns for AI coach training and testing.

This file consolidates all synthetic data generation functionality into a single file
that can create comprehensive datasets for AI coach development and validation.
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import random
from dataclasses import dataclass, asdict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class UserProfile:
    """Represents a synthetic user profile with behavioral characteristics."""
    user_id: int
    persona_type: str
    productivity_baseline: float
    focus_tendency: float
    interruption_tolerance: float
    tool_proficiency: Dict[str, float]
    work_schedule: Dict[str, Any]
    behavioral_patterns: Dict[str, Any]
    
class SyntheticDataGenerator:
    """
    Generates realistic synthetic telemetry data for AI coach testing.
    
    Creates diverse user profiles, realistic work patterns, and behavioral
    variations that mirror real-world productivity scenarios.
    """
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Persona configurations
        self.persona_configs = {
            'customer_support': {
                'base_productivity': 0.8,
                'meeting_frequency': 0.1,
                'interruption_rate': 0.6,  # Customers interrupt, but AI helps manage
                'core_work_percentage': 0.7,  # High customer interaction focus
                'primary_apps': ['Zendesk', 'Intercom', 'Claude', 'Slack'],
                'tab_count_range': (4, 12),
                'focus_duration_range': (15, 35),
                'cognitive_load_range': (0.4, 0.75),
                'ai_usage_frequency': 0.9  # Very high AI integration
            },
            'analyst': {
                'base_productivity': 0.75,
                'meeting_frequency': 0.2,
                'interruption_rate': 0.4,
                'core_work_percentage': 0.35,
                'primary_apps': ['Excel', 'PowerBI', 'SQL Server', 'Tableau'],
                'tab_count_range': (4, 12),
                'focus_duration_range': (15, 45),
                'cognitive_load_range': (0.5, 0.8)
            },
            'developer': {
                'base_productivity': 0.8,
                'meeting_frequency': 0.15,
                'interruption_rate': 0.3,
                'core_work_percentage': 0.7,
                'primary_apps': ['VSCode', 'Terminal', 'Chrome', 'Slack'],
                'tab_count_range': (3, 15),
                'focus_duration_range': (20, 60),
                'cognitive_load_range': (0.4, 0.7)
            },
            'designer': {
                'base_productivity': 0.7,
                'meeting_frequency': 0.25,
                'interruption_rate': 0.35,
                'core_work_percentage': 0.6,
                'primary_apps': ['Figma', 'Photoshop', 'Illustrator', 'Chrome'],
                'tab_count_range': (5, 18),
                'focus_duration_range': (10, 40),
                'cognitive_load_range': (0.5, 0.75)
            }
        }
        
        # Behavioral pattern templates
        self.behavioral_patterns = {
            'morning_person': {
                'peak_hours': [8, 9, 10, 11],
                'productivity_multiplier': [1.3, 1.2, 1.1, 1.0],
                'focus_multiplier': [1.4, 1.3, 1.2, 1.1]
            },
            'afternoon_person': {
                'peak_hours': [13, 14, 15, 16],
                'productivity_multiplier': [1.0, 1.1, 1.2, 1.3],
                'focus_multiplier': [1.1, 1.2, 1.3, 1.4]
            },
            'night_owl': {
                'peak_hours': [16, 17, 18, 19],
                'productivity_multiplier': [1.0, 1.1, 1.2, 1.1],
                'focus_multiplier': [1.1, 1.2, 1.3, 1.2]
            },
            'consistent': {
                'peak_hours': [9, 10, 11, 14, 15, 16],
                'productivity_multiplier': [1.1] * 6,
                'focus_multiplier': [1.1] * 6
            }
        }
        
        # Task categories and their characteristics
        self.task_categories = {
            'admin': {'value_score_range': (0.1, 0.4), 'cognitive_load': 0.3},
            'analysis': {'value_score_range': (0.3, 0.7), 'cognitive_load': 0.7},
            'creative': {'value_score_range': (0.4, 0.8), 'cognitive_load': 0.6},
            'development': {'value_score_range': (0.5, 0.9), 'cognitive_load': 0.8},
            'meeting': {'value_score_range': (0.2, 0.6), 'cognitive_load': 0.4},
            'communication': {'value_score_range': (0.2, 0.5), 'cognitive_load': 0.3},
            'learning': {'value_score_range': (0.6, 0.9), 'cognitive_load': 0.8},
            'customer_interaction': {'value_score_range': (0.6, 0.9), 'cognitive_load': 0.6},
            'case_resolution': {'value_score_range': (0.7, 0.95), 'cognitive_load': 0.7}
        }
    
    def generate_user_profiles(self, count: int = 50) -> List[UserProfile]:
        """Generate diverse user profiles with realistic characteristics."""
        
        profiles = []
        
        for user_id in range(1, count + 1):
            # Select persona (with realistic distribution - focus on AI-receptive personas)
            persona_weights = {'customer_support': 0.25, 'analyst': 0.35, 'developer': 0.3, 'designer': 0.1}
            persona = np.random.choice(list(persona_weights.keys()), p=list(persona_weights.values()))
            
            config = self.persona_configs[persona]
            
            # Generate behavioral characteristics
            productivity_baseline = config['base_productivity'] + np.random.normal(0, 0.1)
            productivity_baseline = max(0.3, min(1.0, productivity_baseline))
            
            focus_tendency = np.random.beta(2, 2)  # Bell curve around 0.5
            interruption_tolerance = 1.0 - config['interruption_rate'] + np.random.normal(0, 0.1)
            interruption_tolerance = max(0.1, min(1.0, interruption_tolerance))
            
            # Tool proficiency (how good they are with different tools)
            tool_proficiency = {}
            for app in config['primary_apps']:
                proficiency = np.random.beta(3, 2)  # Skewed toward higher proficiency
                tool_proficiency[app] = proficiency
            
            # Work schedule preferences
            chronotype = np.random.choice(['morning_person', 'afternoon_person', 'night_owl', 'consistent'],
                                        p=[0.3, 0.4, 0.2, 0.1])
            
            work_schedule = {
                'start_hour': np.random.choice([7, 8, 9], p=[0.2, 0.6, 0.2]),
                'end_hour': np.random.choice([16, 17, 18], p=[0.1, 0.6, 0.3]),
                'chronotype': chronotype,
                'break_frequency': np.random.uniform(0.7, 1.5)  # Hours between breaks
            }
            
            # Behavioral patterns
            behavioral_patterns = {
                'multitasking_tendency': np.random.beta(2, 3),  # Most people are moderate multitaskers
                'notification_tolerance': np.random.uniform(0.3, 0.9),
                'collaboration_frequency': config['meeting_frequency'] + np.random.normal(0, 0.1),
                'learning_orientation': np.random.beta(2, 2),
                'efficiency_consciousness': np.random.beta(3, 2)
            }
            
            profile = UserProfile(
                user_id=user_id,
                persona_type=persona,
                productivity_baseline=productivity_baseline,
                focus_tendency=focus_tendency,
                interruption_tolerance=interruption_tolerance,
                tool_proficiency=tool_proficiency,
                work_schedule=work_schedule,
                behavioral_patterns=behavioral_patterns
            )
            
            profiles.append(profile)
        
        logger.info(f"✅ Generated {len(profiles)} user profiles")
        return profiles
    
    def generate_daily_telemetry(self, user_profiles: List[UserProfile], 
                                num_days: int = 30) -> pd.DataFrame:
        """Generate comprehensive daily telemetry data for all users."""
        
        telemetry_records = []
        
        for day in range(num_days):
            date = datetime.now() - timedelta(days=num_days - day - 1)
            
            for profile in user_profiles:
                # Generate multiple data points per day (every 15 minutes during work hours)
                work_start = profile.work_schedule['start_hour']
                work_end = profile.work_schedule['end_hour']
                
                for hour in range(work_start, work_end + 1):
                    for minute in [0, 15, 30, 45]:
                        timestamp = date.replace(hour=hour, minute=minute, second=0, microsecond=0)
                        
                        # Skip some periods to simulate breaks/meetings
                        if np.random.random() < 0.1:  # 10% chance of no data (break/meeting)
                            continue
                        
                        record = self._generate_telemetry_point(profile, timestamp)
                        telemetry_records.append(record)
        
        df = pd.DataFrame(telemetry_records)
        logger.info(f"✅ Generated {len(df)} telemetry records over {num_days} days")
        return df
    
    def _generate_telemetry_point(self, profile: UserProfile, timestamp: datetime) -> Dict:
        """Generate a single telemetry data point for a user at a specific time."""
        
        config = self.persona_configs[profile.persona_type]
        hour = timestamp.hour
        
        # Apply chronotype effects
        chronotype_data = self.behavioral_patterns[profile.work_schedule['chronotype']]
        hour_multiplier = 1.0
        focus_multiplier = 1.0
        
        if hour in chronotype_data['peak_hours']:
            idx = chronotype_data['peak_hours'].index(hour)
            hour_multiplier = chronotype_data['productivity_multiplier'][idx]
            focus_multiplier = chronotype_data['focus_multiplier'][idx]
        
        # Base metrics with noise
        base_productivity = profile.productivity_baseline * hour_multiplier
        base_focus = profile.focus_tendency * focus_multiplier
        
        # Tab count (influenced by multitasking tendency and persona)
        base_tabs = np.random.randint(*config['tab_count_range'])
        multitasking_factor = profile.behavioral_patterns['multitasking_tendency']
        tab_count = int(base_tabs * (0.5 + multitasking_factor))
        tab_count = max(1, min(50, tab_count))
        
        # Window switching (correlated with tab count and multitasking)
        base_switches = tab_count * np.random.uniform(1.5, 3.0)
        window_switches_15min = int(base_switches * multitasking_factor)
        
        # Focus session duration
        base_focus_duration = np.random.uniform(*config['focus_duration_range'])
        focus_session_duration = int(base_focus_duration * focus_multiplier * profile.focus_tendency)
        focus_session_duration = max(1, min(120, focus_session_duration))
        
        # Cognitive load
        base_cognitive_load = np.random.uniform(*config['cognitive_load_range'])
        task_complexity = np.random.uniform(0.8, 1.2)
        cognitive_load_score = min(1.0, base_cognitive_load * task_complexity)
        
        # Active application (based on persona and time patterns)
        app_active = np.random.choice(config['primary_apps'], 
                                    p=self._get_app_probabilities(profile, hour))
        
        # Task category (influenced by persona and time of day)
        task_category = self._get_task_category(profile, hour)
        
        # Keystrokes (influenced by app, task, and proficiency)
        app_proficiency = profile.tool_proficiency.get(app_active, 0.5)
        base_keystrokes = np.random.uniform(60, 140)
        keystrokes_per_min = int(base_keystrokes * app_proficiency * base_productivity)
        
        # Break duration
        break_frequency = profile.work_schedule['break_frequency']
        if np.random.random() < (1.0 / (break_frequency * 4)):  # Convert to 15-min probability
            break_duration_min = np.random.randint(5, 20)
        else:
            break_duration_min = np.random.randint(0, 3)
        
        # Interruption count
        interruption_base = config['interruption_rate']
        interruption_tolerance = profile.interruption_tolerance
        interruption_count = int(np.random.poisson(interruption_base * (1 - interruption_tolerance) * 15))
        
        # Core work percentage and value score
        core_work_base = config['core_work_percentage']
        efficiency = profile.behavioral_patterns['efficiency_consciousness']
        core_work_percentage = min(1.0, core_work_base * efficiency * hour_multiplier)
        
        # Value score based on task category and performance
        task_config = self.task_categories[task_category]
        value_score = np.random.uniform(*task_config['value_score_range'])
        value_score *= base_productivity * efficiency
        value_score = max(0.0, min(1.0, value_score))
        
        return {
            'timestamp': timestamp.isoformat(),
            'user_id': profile.user_id,
            'persona_type': profile.persona_type,
            'tab_count': tab_count,
            'window_switches_15min': window_switches_15min,
            'focus_session_duration': focus_session_duration,
            'cognitive_load_score': round(cognitive_load_score, 3),
            'app_active': app_active,
            'task_category': task_category,
            'keystrokes_per_min': keystrokes_per_min,
            'break_duration_min': break_duration_min,
            'interruption_count': interruption_count,
            'core_work_percentage': round(core_work_percentage, 3),
            'value_score': round(value_score, 3)
        }
    
    def _get_app_probabilities(self, profile: UserProfile, hour: int) -> List[float]:
        """Get application usage probabilities based on user profile and time."""
        
        config = self.persona_configs[profile.persona_type]
        apps = config['primary_apps']
        
        # Base probabilities
        if profile.persona_type == 'customer_support':
            if 9 <= hour <= 11 or 14 <= hour <= 16:
                # Peak customer interaction times - heavy support platform usage
                return [0.5, 0.2, 0.2, 0.1] if len(apps) == 4 else [1.0]  # Zendesk, Intercom, Claude, Slack
            elif 12 <= hour <= 13:
                # Lunch break - catch up on AI tools and optimization
                return [0.3, 0.2, 0.4, 0.1] if len(apps) == 4 else [1.0]  # More Claude usage
            else:
                return [0.4, 0.3, 0.2, 0.1] if len(apps) == 4 else [1.0]
        
        elif profile.persona_type == 'analyst':
            if 9 <= hour <= 11 or 14 <= hour <= 16:
                # Deep analysis times
                return [0.6, 0.2, 0.1, 0.1] if len(apps) == 4 else [1.0]
            else:
                return [0.4, 0.3, 0.2, 0.1] if len(apps) == 4 else [1.0]
        
        elif profile.persona_type == 'developer':
            if 9 <= hour <= 11 or 14 <= hour <= 17:
                # Coding heavy times
                return [0.7, 0.15, 0.1, 0.05] if len(apps) == 4 else [1.0]
            else:
                return [0.5, 0.2, 0.2, 0.1] if len(apps) == 4 else [1.0]
        
        elif profile.persona_type == 'designer':
            if 10 <= hour <= 12 or 15 <= hour <= 17:
                # Creative work times
                return [0.6, 0.2, 0.1, 0.1] if len(apps) == 4 else [1.0]
            else:
                return [0.4, 0.3, 0.2, 0.1] if len(apps) == 4 else [1.0]
        
        # Default equal probabilities
        return [1.0 / len(apps)] * len(apps)
    
    def _get_task_category(self, profile: UserProfile, hour: int) -> str:
        """Determine task category based on profile and time."""
        
        # Time-based task patterns
        if hour <= 9:
            # Morning - admin and planning
            categories = ['admin', 'communication', 'learning']
            weights = [0.5, 0.3, 0.2]
        elif 10 <= hour <= 12:
            # Late morning - core work
            if profile.persona_type == 'developer':
                categories = ['development', 'analysis', 'learning']
                weights = [0.6, 0.2, 0.2]
            elif profile.persona_type == 'analyst':
                categories = ['analysis', 'admin', 'communication']
                weights = [0.7, 0.2, 0.1]
            elif profile.persona_type == 'designer':
                categories = ['creative', 'analysis', 'communication']
                weights = [0.6, 0.2, 0.2]
            elif profile.persona_type == 'customer_support':
                categories = ['customer_interaction', 'case_resolution', 'communication']
                weights = [0.6, 0.3, 0.1]
            else:  # other personas
                categories = ['admin', 'communication', 'analysis']
                weights = [0.4, 0.4, 0.2]
        elif 13 <= hour <= 14:
            # Post-lunch - lighter tasks
            categories = ['communication', 'admin', 'learning']
            weights = [0.4, 0.4, 0.2]
        elif 15 <= hour <= 17:
            # Afternoon - mixed work
            if profile.persona_type == 'developer':
                categories = ['development', 'analysis', 'communication']
                weights = [0.5, 0.3, 0.2]
            elif profile.persona_type == 'analyst':
                categories = ['analysis', 'admin', 'meeting']
                weights = [0.5, 0.3, 0.2]
            elif profile.persona_type == 'designer':
                categories = ['creative', 'meeting', 'communication']
                weights = [0.5, 0.3, 0.2]
            elif profile.persona_type == 'customer_support':
                categories = ['customer_interaction', 'case_resolution', 'admin']
                weights = [0.5, 0.3, 0.2]
            else:  # other personas
                categories = ['admin', 'meeting', 'analysis']
                weights = [0.4, 0.4, 0.2]
        else:
            # End of day - admin and wrap-up
            categories = ['admin', 'communication', 'meeting']
            weights = [0.5, 0.3, 0.2]
        
        return np.random.choice(categories, p=weights)
    
    def generate_synthetic_interactions(self, user_profiles: List[UserProfile], 
                                      count: int = 100) -> List[Dict]:
        """Generate synthetic coaching interactions based on user profiles."""
        
        interactions = []
        
        for _ in range(count):
            profile = np.random.choice(user_profiles)
            
            # Generate interaction based on profile characteristics
            interaction = self._generate_interaction(profile)
            interactions.append(interaction)
        
        logger.info(f"✅ Generated {len(interactions)} synthetic interactions")
        return interactions
    
    def _generate_interaction(self, profile: UserProfile) -> Dict:
        """Generate a single coaching interaction for a user profile."""
        
        # Base acceptance rates by persona (learned from real patterns)
        base_acceptance_rates = {
            'customer_support': 0.85,  # High acceptance - AI-savvy and efficiency-focused
            'analyst': 0.875,  # Highest acceptance - data-driven mindset
            'developer': 0.78,
            'designer': 1.0
        }
        
        base_rate = base_acceptance_rates.get(profile.persona_type, 0.7)
        
        # Adjust based on user characteristics
        efficiency_factor = profile.behavioral_patterns['efficiency_consciousness']
        learning_factor = profile.behavioral_patterns['learning_orientation']
        
        adjusted_rate = base_rate * (0.7 + 0.3 * efficiency_factor) * (0.8 + 0.2 * learning_factor)
        adjusted_rate = max(0.1, min(0.95, adjusted_rate))
        
        # Determine if user accepts
        accepted = np.random.random() < adjusted_rate
        
        # Generate nudge characteristics
        nudge_confidence = np.random.uniform(0.5, 0.9)
        if profile.persona_type == 'analyst':
            nudge_confidence = np.random.uniform(0.6, 0.95)  # Analysts get higher confidence nudges
        elif profile.persona_type == 'manager':
            nudge_confidence = np.random.uniform(0.7, 0.9)   # Managers need higher confidence
        
        trigger_dimensions = ['focus', 'productivity', 'wellbeing', 'value_creation']
        weights = [0.3, 0.4, 0.2, 0.1]
        if profile.persona_type == 'developer':
            weights = [0.4, 0.3, 0.2, 0.1]  # Developers care more about focus
        elif profile.persona_type == 'analyst':
            weights = [0.2, 0.5, 0.1, 0.2]  # Analysts care about productivity and value
        
        trigger_dimension = np.random.choice(trigger_dimensions, p=weights)
        
        # Generate outcome
        if accepted:
            outcome = {
                'accepted': True,
                'response_time_seconds': np.random.uniform(5, 30),
                'productivity_impact': np.random.uniform(0.08, 0.20),
                'satisfaction_impact': np.random.uniform(0.10, 0.16),
                'follow_through_probability': np.random.uniform(0.7, 0.95),
                'user_feedback': np.random.choice([
                    "Will block time for important work",
                    "Good point about automation",
                    "Restructuring my priorities",
                    "Helpful reminder",
                    "Making this change now"
                ])
            }
        else:
            # Persona-specific dismissal reasons
            dismissal_reasons = {
                'customer_support': ['with_customer', 'urgent_case', 'in_call', 'peak_hours'],
                'analyst': ['not_relevant', 'already_doing', 'unclear', 'not_now'],
                'developer': ['too_frequent', 'in_flow', 'not_now', 'interrupting'],
                'designer': ['busy', 'not_relevant', 'unclear', 'not_now']
            }
            
            reasons = dismissal_reasons.get(profile.persona_type, ['busy', 'not_relevant', 'not_now'])
            dismissal_reason = np.random.choice(reasons)
            
            outcome = {
                'accepted': False,
                'dismissal_reason': dismissal_reason,
                'productivity_impact': 0.0,
                'satisfaction_impact': np.random.uniform(-0.05, 0.0),
                'response_time_seconds': np.random.uniform(1, 5),
                'user_feedback': np.random.choice([
                    "Not now", "Too busy", "Not helpful", 
                    "In the middle of something", "Already doing this"
                ])
            }
        
        return {
            'user_id': profile.user_id,
            'persona': profile.persona_type,
            'nudge': {
                'nudge_text': f"Synthetic {trigger_dimension} nudge for {profile.persona_type}",
                'confidence': round(nudge_confidence, 3),
                'urgency_score': np.random.uniform(0.3, 0.8),
                'trigger_dimension': trigger_dimension,
                'persona_optimized': True
            },
            'outcome': outcome,
            'timestamp': datetime.now().isoformat()
        }
    
    def add_realistic_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add realistic anomalies and edge cases to telemetry data."""
        
        df_modified = df.copy()
        
        # Add some extreme productivity days (both high and low)
        extreme_days = np.random.choice(df_modified.index, size=int(len(df_modified) * 0.05))
        
        for idx in extreme_days:
            if np.random.random() < 0.5:
                # High productivity day
                df_modified.loc[idx, 'focus_session_duration'] = int(df_modified.loc[idx, 'focus_session_duration'] * np.random.uniform(1.5, 2.0))
                df_modified.loc[idx, 'core_work_percentage'] *= np.random.uniform(1.3, 1.8)
                df_modified.loc[idx, 'interruption_count'] = int(df_modified.loc[idx, 'interruption_count'] * np.random.uniform(0.2, 0.5))
                df_modified.loc[idx, 'value_score'] *= np.random.uniform(1.2, 1.5)
            else:
                # Low productivity day (sick, distracted, etc.)
                df_modified.loc[idx, 'focus_session_duration'] = int(df_modified.loc[idx, 'focus_session_duration'] * np.random.uniform(0.3, 0.6))
                df_modified.loc[idx, 'core_work_percentage'] *= np.random.uniform(0.2, 0.5)
                df_modified.loc[idx, 'interruption_count'] = int(df_modified.loc[idx, 'interruption_count'] * np.random.uniform(1.5, 3.0))
                df_modified.loc[idx, 'cognitive_load_score'] *= np.random.uniform(1.2, 1.5)
        
        # Add some data quality issues (missing values, outliers)
        missing_indices = np.random.choice(df_modified.index, size=int(len(df_modified) * 0.02))
        for idx in missing_indices:
            # Randomly make some values missing
            columns_to_null = np.random.choice(df_modified.columns[3:], size=np.random.randint(1, 3))
            for col in columns_to_null:
                df_modified.loc[idx, col] = np.nan
        
        # Add some measurement errors
        error_indices = np.random.choice(df_modified.index, size=int(len(df_modified) * 0.01))
        for idx in error_indices:
            # Add noise to measurements
            if 'keystrokes_per_min' in df_modified.columns:
                df_modified.loc[idx, 'keystrokes_per_min'] += np.random.randint(-20, 50)
            if 'tab_count' in df_modified.columns:
                df_modified.loc[idx, 'tab_count'] += np.random.randint(-2, 10)
        
        # Ensure values stay within reasonable bounds
        df_modified = self._enforce_data_bounds(df_modified)
        
        logger.info(f"✅ Added realistic anomalies to {len(df_modified)} records")
        return df_modified
    
    def _enforce_data_bounds(self, df: pd.DataFrame) -> pd.DataFrame:
        """Ensure all values stay within realistic bounds."""
        
        bounds = {
            'tab_count': (1, 50),
            'window_switches_15min': (0, 100),
            'focus_session_duration': (1, 120),
            'cognitive_load_score': (0.0, 1.0),
            'keystrokes_per_min': (0, 300),
            'break_duration_min': (0, 60),
            'interruption_count': (0, 50),
            'core_work_percentage': (0.0, 1.0),
            'value_score': (0.0, 1.0)
        }
        
        for column, (min_val, max_val) in bounds.items():
            if column in df.columns:
                df[column] = df[column].clip(lower=min_val, upper=max_val)
        
        return df
    
    def save_datasets(self, user_profiles: List[UserProfile], 
                     telemetry_df: pd.DataFrame, 
                     interactions: List[Dict]):
        """Save all generated datasets to files."""
        
        # Save user profiles
        profiles_data = [asdict(profile) for profile in user_profiles]
        profiles_path = self.output_dir / "user_profiles.json"
        with open(profiles_path, 'w') as f:
            json.dump(profiles_data, f, indent=2, default=str)
        
        # Save telemetry data
        telemetry_path = self.output_dir / "synthetic_telemetry.csv"
        telemetry_df.to_csv(telemetry_path, index=False)
        
        # Save interactions
        interactions_path = self.output_dir / "synthetic_interactions.jsonl"
        with open(interactions_path, 'w') as f:
            for interaction in interactions:
                json.dump(interaction, f)
                f.write('\n')
        
        # Create summary report
        self._create_summary_report(user_profiles, telemetry_df, interactions)
        
        logger.info(f"✅ Saved datasets to {self.output_dir}")
        return {
            'profiles_path': profiles_path,
            'telemetry_path': telemetry_path,
            'interactions_path': interactions_path
        }
    
    def _create_summary_report(self, user_profiles: List[UserProfile], 
                              telemetry_df: pd.DataFrame, 
                              interactions: List[Dict]):
        """Create a summary report of generated data."""
        
        # Analyze user profiles
        persona_counts = {}
        for profile in user_profiles:
            persona_counts[profile.persona_type] = persona_counts.get(profile.persona_type, 0) + 1
        
        # Analyze telemetry data
        telemetry_stats = {
            'total_records': len(telemetry_df),
            'date_range': f"{telemetry_df['timestamp'].min()} to {telemetry_df['timestamp'].max()}",
            'avg_metrics': {
                'focus_duration': telemetry_df['focus_session_duration'].mean(),
                'cognitive_load': telemetry_df['cognitive_load_score'].mean(),
                'value_score': telemetry_df['value_score'].mean(),
                'core_work_percentage': telemetry_df['core_work_percentage'].mean()
            }
        }
        
        # Analyze interactions
        accepted_interactions = [i for i in interactions if i['outcome']['accepted']]
        interaction_stats = {
            'total_interactions': len(interactions),
            'acceptance_rate': len(accepted_interactions) / len(interactions) if interactions else 0,
            'persona_acceptance': {}
        }
        
        for persona in persona_counts:
            persona_interactions = [i for i in interactions if i['persona'] == persona]
            persona_accepted = [i for i in persona_interactions if i['outcome']['accepted']]
            if persona_interactions:
                interaction_stats['persona_acceptance'][persona] = len(persona_accepted) / len(persona_interactions)
        
        # Create report
        report = {
            'generation_timestamp': datetime.now().isoformat(),
            'user_profiles': {
                'total_users': len(user_profiles),
                'persona_distribution': persona_counts
            },
            'telemetry_data': telemetry_stats,
            'interaction_data': interaction_stats,
            'data_quality': {
                'missing_values': telemetry_df.isnull().sum().to_dict(),
                'outliers_detected': self._detect_outliers(telemetry_df)
            }
        }
        
        report_path = self.output_dir / "data_generation_report.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"✅ Created summary report: {report_path}")
    
    def _detect_outliers(self, df: pd.DataFrame) -> Dict:
        """Detect outliers in telemetry data."""
        
        outliers = {}
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        
        for column in numeric_columns:
            if column in ['user_id']:
                continue
                
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outlier_count = len(df[(df[column] < lower_bound) | (df[column] > upper_bound)])
            outliers[column] = outlier_count
        
        return outliers

def generate_comprehensive_dataset(num_users: int = 50, num_days: int = 30, 
                                 num_interactions: int = 100) -> Dict:
    """Generate a comprehensive synthetic dataset for AI coach testing."""
    
    print("🏭 SYNTHETIC DATA GENERATOR")
    print("="*60)
    print(f"Generating comprehensive dataset:")
    print(f"  👥 Users: {num_users}")
    print(f"  📅 Days: {num_days}")
    print(f"  💬 Interactions: {num_interactions}")
    print("-"*60)
    
    generator = SyntheticDataGenerator()
    
    # Generate user profiles
    print("\n1. Generating user profiles...")
    user_profiles = generator.generate_user_profiles(num_users)
    
    # Show persona distribution
    persona_counts = {}
    for profile in user_profiles:
        persona_counts[profile.persona_type] = persona_counts.get(profile.persona_type, 0) + 1
    
    print("   Persona Distribution:")
    for persona, count in persona_counts.items():
        print(f"     {persona.title()}: {count} users ({count/num_users:.1%})")
    
    # Generate telemetry data
    print(f"\n2. Generating {num_days} days of telemetry data...")
    telemetry_df = generator.generate_daily_telemetry(user_profiles, num_days)
    
    # Add realistic anomalies
    print("   Adding realistic anomalies and edge cases...")
    telemetry_df = generator.add_realistic_anomalies(telemetry_df)
    
    print(f"   Generated {len(telemetry_df):,} telemetry records")
    
    # Generate interactions
    print(f"\n3. Generating {num_interactions} coaching interactions...")
    interactions = generator.generate_synthetic_interactions(user_profiles, num_interactions)
    
    # Show interaction statistics
    accepted_count = sum(1 for i in interactions if i['outcome']['accepted'])
    acceptance_rate = accepted_count / len(interactions)
    print(f"   Overall acceptance rate: {acceptance_rate:.1%}")
    
    # Save all datasets
    print("\n4. Saving datasets...")
    file_paths = generator.save_datasets(user_profiles, telemetry_df, interactions)
    
    print(f"\n✅ Dataset generation complete!")
    print(f"   Files saved to: outputs/")
    print(f"   📊 Telemetry records: {len(telemetry_df):,}")
    print(f"   💬 Interactions: {len(interactions)}")
    print(f"   📈 Acceptance rate: {acceptance_rate:.1%}")
    
    return {
        'user_profiles': user_profiles,
        'telemetry_df': telemetry_df,
        'interactions': interactions,
        'file_paths': file_paths,
        'stats': {
            'num_users': num_users,
            'num_records': len(telemetry_df),
            'num_interactions': len(interactions),
            'acceptance_rate': acceptance_rate,
            'persona_distribution': persona_counts
        }
    }

if __name__ == "__main__":
    # Generate comprehensive dataset
    dataset = generate_comprehensive_dataset(
        num_users=25,      # Reasonable number for demo
        num_days=14,       # 2 weeks of data
        num_interactions=50  # Good sample size
    )
    
    print(f"\n🎉 Synthetic data generation complete!")
    print(f"   Ready for AI coach training and testing")