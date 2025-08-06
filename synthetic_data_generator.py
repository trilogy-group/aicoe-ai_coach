#!/usr/bin/env python3
"""
Synthetic Data Generator for AI Coach Training
==============================================

This module generates high-quality synthetic telemetry data and user interaction
scenarios for training and evaluating the AI coaching system. It creates realistic
user behavior patterns, productivity scenarios, and coaching interaction data.

The generator uses behavioral psychology models to create authentic data that
reflects real workplace patterns and user responses to coaching interventions.

Features:
- Realistic telemetry data generation
- Multiple user persona simulation
- Seasonal and temporal pattern modeling
- Coaching interaction scenario creation
- Massive dataset generation capabilities
- Export in multiple formats (JSON, CSV, JSONL)

Usage:
    # Generate standard dataset
    python synthetic_data_generator.py
    
    # Generate massive dataset
    python synthetic_data_generator.py --massive --size 100000
    
    # Generate specific scenarios
    python synthetic_data_generator.py --scenarios stress,focus,energy

Author: AI Coach Evolution Team
Version: 2.0 (Consolidated Generator)
"""

import asyncio
import json
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import logging
from dataclasses import dataclass, asdict
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class UserProfile:
    """Represents a user profile with behavioral characteristics"""
    user_id: str
    name: str
    role: str
    experience_level: str
    work_pattern: str
    stress_sensitivity: float
    focus_preference: str
    notification_tolerance: float
    productivity_baseline: float
    energy_pattern: str
    break_resistance: float
    tech_savviness: float
    collaboration_level: float
    preferred_interventions: List[str]


@dataclass
class TelemetryData:
    """Represents telemetry data from user workspace"""
    timestamp: str
    user_id: str
    keystrokes_per_min: int
    mouse_events_per_min: int
    active_window_count: int
    app_switches_per_hour: int
    primary_app_time_percentage: int
    deep_focus_minutes: int
    break_duration_minutes: int
    last_break_time: str
    error_rate: float
    backspace_rate: float
    copy_paste_frequency: int
    scroll_speed: float
    click_accuracy: float
    typing_rhythm_consistency: float
    pause_frequency: int
    context_switches: int
    notification_interactions: int
    email_checks_per_hour: int
    social_media_time_minutes: int
    meeting_duration_minutes: int
    lines_of_code_written: int
    documents_edited: int
    tasks_completed: int
    screen_time_hours: float
    posture_changes: int
    eye_strain_indicators: int
    productivity_score: float
    stress_level: float
    energy_level: float
    focus_quality: float
    cognitive_load: float
    mood_indicator: float
    satisfaction_level: float


class SyntheticDataGenerator:
    """
    Main synthetic data generator for AI coach training and evaluation.
    
    Generates realistic user telemetry, coaching scenarios, and interaction data
    based on behavioral psychology models and workplace productivity research.
    """
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # User personas and archetypes
        self.user_archetypes = self._define_user_archetypes()
        self.scenario_templates = self._define_scenario_templates()
        
        # Temporal patterns
        self.work_hours = list(range(9, 18))
        self.peak_hours = [10, 11, 14, 15]
        self.slump_hours = [13, 16]
        
        # Data generation parameters
        self.noise_level = 0.15  # Amount of random variation
        self.correlation_strength = 0.7  # How much metrics correlate
        
    def _define_user_archetypes(self) -> List[Dict[str, Any]]:
        """Define different user persona archetypes"""
        return [
            {
                'role': 'software_developer',
                'name': 'Focused Developer',
                'experience_level': 'senior',
                'work_pattern': 'deep_work_blocks',
                'stress_sensitivity': 0.4,
                'focus_preference': 'long_sessions',
                'notification_tolerance': 0.2,
                'productivity_baseline': 0.75,
                'energy_pattern': 'morning_peak',
                'break_resistance': 0.8,
                'tech_savviness': 0.95,
                'collaboration_level': 0.3,
                'preferred_interventions': ['focus_protection', 'scheduled_breaks', 'eye_rest'],
                'typical_metrics': {
                    'keystrokes_per_min': (45, 85),
                    'deep_focus_minutes': (120, 240),
                    'app_switches_per_hour': (5, 15),
                    'lines_of_code_written': (50, 200)
                }
            },
            {
                'role': 'project_manager',
                'name': 'Multitasking Manager',
                'experience_level': 'senior',
                'work_pattern': 'context_switching',
                'stress_sensitivity': 0.7,
                'focus_preference': 'short_bursts',
                'notification_tolerance': 0.8,
                'productivity_baseline': 0.65,
                'energy_pattern': 'steady',
                'break_resistance': 0.4,
                'tech_savviness': 0.7,
                'collaboration_level': 0.9,
                'preferred_interventions': ['stress_management', 'priority_focus', 'time_blocking'],
                'typical_metrics': {
                    'keystrokes_per_min': (30, 60),
                    'deep_focus_minutes': (30, 90),
                    'app_switches_per_hour': (25, 45),
                    'email_checks_per_hour': (8, 15)
                }
            },
            {
                'role': 'designer',
                'name': 'Creative Designer',
                'experience_level': 'mid',
                'work_pattern': 'creative_bursts',
                'stress_sensitivity': 0.6,
                'focus_preference': 'flow_sessions',
                'notification_tolerance': 0.5,
                'productivity_baseline': 0.7,
                'energy_pattern': 'afternoon_peak',
                'break_resistance': 0.5,
                'tech_savviness': 0.8,
                'collaboration_level': 0.6,
                'preferred_interventions': ['inspiration_breaks', 'environment_change', 'creative_exercises'],
                'typical_metrics': {
                    'keystrokes_per_min': (20, 45),
                    'deep_focus_minutes': (60, 180),
                    'app_switches_per_hour': (15, 30),
                    'documents_edited': (3, 8)
                }
            },
            {
                'role': 'data_analyst',
                'name': 'Analytical Researcher',
                'experience_level': 'senior',
                'work_pattern': 'analysis_cycles',
                'stress_sensitivity': 0.3,
                'focus_preference': 'extended_sessions',
                'notification_tolerance': 0.3,
                'productivity_baseline': 0.8,
                'energy_pattern': 'morning_peak',
                'break_resistance': 0.7,
                'tech_savviness': 0.9,
                'collaboration_level': 0.4,
                'preferred_interventions': ['data_breaks', 'eye_rest', 'posture_checks'],
                'typical_metrics': {
                    'keystrokes_per_min': (35, 70),
                    'deep_focus_minutes': (90, 200),
                    'app_switches_per_hour': (8, 20),
                    'tasks_completed': (2, 6)
                }
            },
            {
                'role': 'customer_support',
                'name': 'Support Specialist',
                'experience_level': 'junior',
                'work_pattern': 'reactive_responses',
                'stress_sensitivity': 0.8,
                'focus_preference': 'short_tasks',
                'notification_tolerance': 0.9,
                'productivity_baseline': 0.6,
                'energy_pattern': 'variable',
                'break_resistance': 0.3,
                'tech_savviness': 0.6,
                'collaboration_level': 0.8,
                'preferred_interventions': ['stress_relief', 'empathy_support', 'energy_boosts'],
                'typical_metrics': {
                    'keystrokes_per_min': (40, 80),
                    'deep_focus_minutes': (20, 60),
                    'app_switches_per_hour': (30, 50),
                    'notification_interactions': (15, 30)
                }
            }
        ]
    
    def _define_scenario_templates(self) -> Dict[str, Dict]:
        """Define coaching scenario templates"""
        return {
            'high_stress': {
                'description': 'User experiencing high stress levels',
                'triggers': {
                    'stress_level': (0.7, 1.0),
                    'error_rate': (0.1, 0.3),
                    'backspace_rate': (0.15, 0.4),
                    'app_switches_per_hour': (35, 60)
                },
                'expected_interventions': ['breathing_exercise', 'stress_relief', 'break_suggestion'],
                'duration_minutes': (30, 120),
                'likelihood_by_role': {
                    'project_manager': 0.8,
                    'customer_support': 0.9,
                    'software_developer': 0.4,
                    'designer': 0.6,
                    'data_analyst': 0.3
                }
            },
            'focus_depletion': {
                'description': 'User losing focus and concentration',
                'triggers': {
                    'focus_quality': (0.1, 0.4),
                    'app_switches_per_hour': (40, 70),
                    'deep_focus_minutes': (0, 20),
                    'context_switches': (25, 50)
                },
                'expected_interventions': ['focus_restoration', 'environment_optimization', 'distraction_removal'],
                'duration_minutes': (45, 90),
                'likelihood_by_role': {
                    'project_manager': 0.9,
                    'customer_support': 0.8,
                    'software_developer': 0.5,
                    'designer': 0.6,
                    'data_analyst': 0.4
                }
            },
            'energy_slump': {
                'description': 'User experiencing energy/motivation drop',
                'triggers': {
                    'energy_level': (0.2, 0.5),
                    'keystrokes_per_min': (10, 30),
                    'productivity_score': (0.2, 0.4),
                    'mood_indicator': (0.2, 0.5)
                },
                'expected_interventions': ['energy_boost', 'motivation_reminder', 'light_exercise'],
                'duration_minutes': (60, 180),
                'likelihood_by_role': {
                    'project_manager': 0.7,
                    'customer_support': 0.8,
                    'software_developer': 0.6,
                    'designer': 0.7,
                    'data_analyst': 0.5
                }
            },
            'flow_state': {
                'description': 'User in optimal productivity state',
                'triggers': {
                    'focus_quality': (0.8, 1.0),
                    'productivity_score': (0.8, 1.0),
                    'deep_focus_minutes': (60, 240),
                    'app_switches_per_hour': (2, 8)
                },
                'expected_interventions': ['flow_protection', 'minimal_interruption', 'gentle_reminders'],
                'duration_minutes': (30, 120),
                'likelihood_by_role': {
                    'project_manager': 0.3,
                    'customer_support': 0.2,
                    'software_developer': 0.8,
                    'designer': 0.9,
                    'data_analyst': 0.9
                }
            },
            'burnout_risk': {
                'description': 'Signs of potential burnout developing',
                'triggers': {
                    'stress_level': (0.8, 1.0),
                    'energy_level': (0.1, 0.3),
                    'satisfaction_level': (0.1, 0.4),
                    'screen_time_hours': (9, 12)
                },
                'expected_interventions': ['burnout_prevention', 'workload_adjustment', 'wellness_check'],
                'duration_minutes': (120, 480),
                'likelihood_by_role': {
                    'project_manager': 0.6,
                    'customer_support': 0.7,
                    'software_developer': 0.5,
                    'designer': 0.4,
                    'data_analyst': 0.5
                }
            }
        }
    
    def generate_user_profile(self, archetype: Dict[str, Any], user_id: str) -> UserProfile:
        """Generate a specific user profile from an archetype"""
        # Add some variation to the archetype
        variation = random.uniform(0.8, 1.2)
        
        return UserProfile(
            user_id=user_id,
            name=f"{archetype['name']} {random.randint(1, 999)}",
            role=archetype['role'],
            experience_level=archetype['experience_level'],
            work_pattern=archetype['work_pattern'],
            stress_sensitivity=min(1.0, archetype['stress_sensitivity'] * variation),
            focus_preference=archetype['focus_preference'],
            notification_tolerance=min(1.0, archetype['notification_tolerance'] * variation),
            productivity_baseline=min(1.0, archetype['productivity_baseline'] * variation),
            energy_pattern=archetype['energy_pattern'],
            break_resistance=min(1.0, archetype['break_resistance'] * variation),
            tech_savviness=min(1.0, archetype['tech_savviness'] * variation),
            collaboration_level=min(1.0, archetype['collaboration_level'] * variation),
            preferred_interventions=archetype['preferred_interventions'].copy()
        )
    
    def generate_telemetry_datapoint(self, profile: UserProfile, 
                                   timestamp: datetime,
                                   scenario: Optional[str] = None) -> TelemetryData:
        """Generate a single telemetry datapoint for a user"""
        
        # Get archetype for baseline metrics
        archetype = next(a for a in self.user_archetypes if a['role'] == profile.role)
        
        # Time-based factors
        hour = timestamp.hour
        is_work_hour = hour in self.work_hours
        is_peak_hour = hour in self.peak_hours
        is_slump_hour = hour in self.slump_hours
        
        # Energy pattern influence
        energy_multiplier = self._get_energy_multiplier(profile.energy_pattern, hour)
        base_productivity = profile.productivity_baseline * energy_multiplier
        
        # Apply scenario effects if specified
        if scenario and scenario in self.scenario_templates:
            scenario_data = self.scenario_templates[scenario]
            triggers = scenario_data['triggers']
        else:
            triggers = {}
        
        # Generate base metrics with correlations
        base_energy = max(0.1, min(1.0, base_productivity + random.uniform(-0.2, 0.2)))
        base_stress = max(0.0, min(1.0, (1 - base_energy) * profile.stress_sensitivity + random.uniform(-0.1, 0.1)))
        base_focus = max(0.1, min(1.0, base_energy - (base_stress * 0.5) + random.uniform(-0.15, 0.15)))
        
        # Override with scenario-specific values if present
        energy_level = triggers.get('energy_level', (base_energy, base_energy))[0] if scenario else base_energy
        stress_level = triggers.get('stress_level', (base_stress, base_stress))[0] if scenario else base_stress  
        focus_quality = triggers.get('focus_quality', (base_focus, base_focus))[0] if scenario else base_focus
        
        # Generate correlated metrics
        typical_metrics = archetype['typical_metrics']
        
        # Keystroke activity influenced by focus and energy
        activity_factor = (energy_level * 0.6 + focus_quality * 0.4)
        ks_min, ks_max = typical_metrics.get('keystrokes_per_min', (30, 60))
        keystrokes_per_min = int((ks_min + (ks_max - ks_min) * activity_factor) * random.uniform(0.8, 1.2))
        
        # Mouse activity correlated with keystrokes
        mouse_ratio = random.uniform(0.3, 0.7)
        mouse_events_per_min = int(keystrokes_per_min * mouse_ratio)
        
        # App switching inversely correlated with focus
        app_switches_base = typical_metrics.get('app_switches_per_hour', (15, 30))
        app_switches_factor = (1 - focus_quality) * random.uniform(0.8, 1.2)
        app_switches = int(app_switches_base[0] + (app_switches_base[1] - app_switches_base[0]) * app_switches_factor)
        
        # Deep focus time correlated with focus quality
        focus_base = typical_metrics.get('deep_focus_minutes', (30, 120))
        deep_focus_minutes = int(focus_base[0] + (focus_base[1] - focus_base[0]) * focus_quality * random.uniform(0.7, 1.3))
        
        # Error rates influenced by stress
        error_rate = max(0.01, min(0.5, 0.05 + (stress_level * 0.2) + random.uniform(-0.02, 0.02)))
        backspace_rate = max(0.05, min(0.6, error_rate * 2.5 + random.uniform(-0.05, 0.05)))
        
        # Productivity metrics
        productivity_score = max(0.1, min(1.0, (energy_level * 0.4 + focus_quality * 0.6) * random.uniform(0.8, 1.2)))
        cognitive_load = max(0.1, min(1.0, (1 - focus_quality) + (stress_level * 0.5) + random.uniform(-0.1, 0.1)))
        
        # Generate other metrics with realistic ranges
        current_time = timestamp
        last_break = current_time - timedelta(minutes=random.randint(30, 180))
        
        return TelemetryData(
            timestamp=timestamp.isoformat(),
            user_id=profile.user_id,
            keystrokes_per_min=max(0, keystrokes_per_min),
            mouse_events_per_min=max(0, mouse_events_per_min),
            active_window_count=random.randint(1, 8),
            app_switches_per_hour=max(0, app_switches),
            primary_app_time_percentage=random.randint(40, 85),
            deep_focus_minutes=max(0, deep_focus_minutes),
            break_duration_minutes=random.randint(2, 15),
            last_break_time=last_break.isoformat(),
            error_rate=error_rate,
            backspace_rate=backspace_rate,
            copy_paste_frequency=random.randint(5, 25),
            scroll_speed=random.uniform(0.5, 2.0),
            click_accuracy=max(0.7, min(1.0, 0.95 - (stress_level * 0.2))),
            typing_rhythm_consistency=max(0.3, min(1.0, 0.8 - (stress_level * 0.3))),
            pause_frequency=random.randint(10, 40),
            context_switches=random.randint(5, 25),
            notification_interactions=random.randint(3, 20),
            email_checks_per_hour=random.randint(2, 12),
            social_media_time_minutes=random.randint(0, 30),
            meeting_duration_minutes=random.randint(0, 120),
            lines_of_code_written=typical_metrics.get('lines_of_code_written', (0, 50))[1] if 'lines_of_code_written' in typical_metrics else 0,
            documents_edited=typical_metrics.get('documents_edited', (0, 3))[1] if 'documents_edited' in typical_metrics else 0,
            tasks_completed=random.randint(1, 5),
            screen_time_hours=random.uniform(6.0, 10.0),
            posture_changes=random.randint(5, 20),
            eye_strain_indicators=random.randint(1, 8),
            productivity_score=productivity_score,
            stress_level=stress_level,
            energy_level=energy_level,
            focus_quality=focus_quality,
            cognitive_load=cognitive_load,
            mood_indicator=max(0.1, min(1.0, energy_level - (stress_level * 0.3) + random.uniform(-0.1, 0.1))),
            satisfaction_level=max(0.1, min(1.0, productivity_score - (stress_level * 0.2) + random.uniform(-0.1, 0.1)))
        )
    
    def _get_energy_multiplier(self, energy_pattern: str, hour: int) -> float:
        """Get energy level multiplier based on pattern and time"""
        if energy_pattern == 'morning_peak':
            if 8 <= hour <= 11:
                return 1.2
            elif 13 <= hour <= 15:
                return 0.8
            else:
                return 1.0
        elif energy_pattern == 'afternoon_peak':
            if 13 <= hour <= 16:
                return 1.2
            elif 8 <= hour <= 10:
                return 0.8
            else:
                return 1.0
        elif energy_pattern == 'steady':
            return 1.0 + random.uniform(-0.1, 0.1)
        else:  # variable
            return random.uniform(0.7, 1.3)
    
    def generate_coaching_interaction(self, telemetry: TelemetryData, 
                                    profile: UserProfile,
                                    coaching_result: Optional[Dict] = None) -> Dict[str, Any]:
        """Generate a coaching interaction based on telemetry and profile"""
        
        # Determine scenario type based on telemetry
        scenario_type = self._identify_scenario_type(telemetry)
        
        # Simulate coaching system response if not provided
        if not coaching_result:
            coaching_result = self._simulate_coaching_response(telemetry, profile, scenario_type)
        
        # Simulate user response based on profile and coaching
        user_response = self._simulate_user_response(coaching_result, profile)
        
        return {
            'interaction_id': f"{profile.user_id}_{telemetry.timestamp}",
            'timestamp': telemetry.timestamp,
            'user_id': profile.user_id,
            'scenario_type': scenario_type,
            'telemetry_context': {
                'stress_level': telemetry.stress_level,
                'energy_level': telemetry.energy_level,
                'focus_quality': telemetry.focus_quality,
                'productivity_score': telemetry.productivity_score,
                'cognitive_load': telemetry.cognitive_load
            },
            'coaching_intervention': coaching_result,
            'user_response': user_response,
            'effectiveness_score': user_response.get('effectiveness', 0.5),
            'user_satisfaction': user_response.get('satisfaction', 0.5),
            'behavioral_change': user_response.get('behavioral_change', 0.0)
        }
    
    def _identify_scenario_type(self, telemetry: TelemetryData) -> str:
        """Identify the scenario type from telemetry data"""
        # High stress scenario
        if telemetry.stress_level > 0.7:
            return 'high_stress'
        
        # Flow state scenario
        elif telemetry.focus_quality > 0.8 and telemetry.productivity_score > 0.8:
            return 'flow_state'
        
        # Focus depletion scenario
        elif telemetry.focus_quality < 0.4 or telemetry.app_switches_per_hour > 35:
            return 'focus_depletion'
        
        # Energy slump scenario
        elif telemetry.energy_level < 0.4:
            return 'energy_slump'
        
        # Burnout risk scenario
        elif (telemetry.stress_level > 0.8 and telemetry.energy_level < 0.3 
              and telemetry.satisfaction_level < 0.4):
            return 'burnout_risk'
        
        else:
            return 'normal_operation'
    
    def _simulate_coaching_response(self, telemetry: TelemetryData, 
                                  profile: UserProfile, scenario_type: str) -> Dict[str, Any]:
        """Simulate what the coaching system would recommend"""
        
        if scenario_type in self.scenario_templates:
            interventions = self.scenario_templates[scenario_type]['expected_interventions']
            selected_intervention = random.choice(interventions)
        else:
            selected_intervention = 'general_wellness_check'
        
        # Generate coaching message based on intervention type
        messages = {
            'breathing_exercise': "Take a moment to breathe. Try 4-7-8 breathing: inhale for 4, hold for 7, exhale for 8.",
            'stress_relief': "I notice your stress levels are elevated. Consider taking a short walk or doing some light stretching.",
            'break_suggestion': "You've been working intensely. A 5-10 minute break could help refresh your mind.",
            'focus_restoration': "Your focus seems scattered. Try closing unnecessary tabs and focusing on one task for 25 minutes.",
            'environment_optimization': "Consider optimizing your workspace. Reduce distractions and create a focused environment.",
            'distraction_removal': "I see many context switches. Try using Do Not Disturb mode for the next hour.",
            'energy_boost': "Your energy seems low. A quick walk, healthy snack, or brief exercise might help.",
            'motivation_reminder': "Remember your goals for today. What's the most important task you want to complete?",
            'light_exercise': "A few minutes of stretching or light movement could boost your energy and mood.",
            'flow_protection': "You're in a great flow state! Consider silencing notifications to maintain this focus.",
            'minimal_interruption': "Great focus! I'll check back with you later to avoid interrupting your productivity.",
            'gentle_reminders': "Excellent work! Remember to stay hydrated and take care of your posture.",
            'burnout_prevention': "I'm seeing signs of potential burnout. Consider reducing your workload and prioritizing self-care.",
            'workload_adjustment': "Your stress and energy levels suggest you might be overloaded. Can you delegate or postpone some tasks?",
            'wellness_check': "How are you feeling today? Your metrics suggest you might benefit from some wellness attention."
        }
        
        priority = 3 if scenario_type in ['high_stress', 'burnout_risk'] else 2 if scenario_type in ['focus_depletion', 'energy_slump'] else 1
        
        return {
            'message': messages.get(selected_intervention, "Take care of yourself today."),
            'action': selected_intervention,
            'priority': priority,
            'suggested_duration': random.randint(2, 15),
            'confidence': random.uniform(0.6, 0.95),
            'personalization_score': min(1.0, profile.notification_tolerance + random.uniform(-0.2, 0.2))
        }
    
    def _simulate_user_response(self, coaching_result: Dict, profile: UserProfile) -> Dict[str, Any]:
        """Simulate user response to coaching intervention"""
        
        # Base acceptance probability
        base_acceptance = profile.notification_tolerance
        
        # Adjust based on intervention type and user preferences
        intervention = coaching_result['action']
        if intervention in profile.preferred_interventions:
            base_acceptance += 0.3
        
        # Adjust based on priority and user tolerance
        priority = coaching_result.get('priority', 1)
        if priority > 2 and profile.notification_tolerance < 0.5:
            base_acceptance -= 0.2
        
        # Random factors
        base_acceptance += random.uniform(-0.2, 0.2)
        base_acceptance = max(0.0, min(1.0, base_acceptance))
        
        # Determine if user accepts the intervention
        accepted = random.random() < base_acceptance
        
        if accepted:
            # Simulate effectiveness based on intervention appropriateness
            effectiveness = random.uniform(0.6, 0.95)
            satisfaction = random.uniform(0.7, 0.9)
            behavioral_change = random.uniform(0.3, 0.8)
        else:
            effectiveness = random.uniform(0.1, 0.4)
            satisfaction = random.uniform(0.2, 0.5)
            behavioral_change = random.uniform(0.0, 0.2)
        
        return {
            'accepted': accepted,
            'effectiveness': effectiveness,
            'satisfaction': satisfaction,
            'behavioral_change': behavioral_change,
            'response_time_seconds': random.uniform(2, 30),
            'follow_through': accepted and random.random() < 0.7,
            'feedback_provided': random.random() < 0.3,
            'dismissal_reason': None if accepted else random.choice([
                'too_busy', 'not_relevant', 'poor_timing', 'notification_fatigue', 'personal_preference'
            ])
        }
    
    async def generate_dataset(self, num_users: int = 50, 
                             days_per_user: int = 30,
                             interactions_per_day: int = 8,
                             scenarios: Optional[List[str]] = None) -> Dict[str, Any]:
        """Generate comprehensive synthetic dataset"""
        
        logger.info(f"Generating dataset: {num_users} users, {days_per_user} days each")
        
        # Generate user profiles
        profiles = []
        for i in range(num_users):
            archetype = random.choice(self.user_archetypes)
            profile = self.generate_user_profile(archetype, f"user_{i+1:04d}")
            profiles.append(profile)
        
        # Generate telemetry and interaction data
        telemetry_data = []
        interaction_data = []
        
        start_date = datetime.now() - timedelta(days=days_per_user)
        
        for profile in profiles:
            logger.info(f"Generating data for {profile.user_id}")
            
            for day in range(days_per_user):
                current_date = start_date + timedelta(days=day)
                
                # Skip weekends (optional)
                if current_date.weekday() >= 5:
                    continue
                
                for interaction in range(interactions_per_day):
                    # Generate timestamp during work hours
                    hour = random.choice(self.work_hours)
                    minute = random.randint(0, 59)
                    timestamp = current_date.replace(hour=hour, minute=minute)
                    
                    # Select scenario if specified
                    scenario = None
                    if scenarios:
                        scenario = random.choice(scenarios) if random.random() < 0.3 else None
                    
                    # Generate telemetry
                    telemetry = self.generate_telemetry_datapoint(profile, timestamp, scenario)
                    telemetry_data.append(telemetry)
                    
                    # Generate coaching interaction (30% chance)
                    if random.random() < 0.3:
                        interaction = self.generate_coaching_interaction(telemetry, profile)
                        interaction_data.append(interaction)
        
        # Create summary statistics
        summary = {
            'generation_timestamp': datetime.now().isoformat(),
            'num_users': num_users,
            'num_profiles': len(profiles),
            'num_telemetry_points': len(telemetry_data),
            'num_interactions': len(interaction_data),
            'days_generated': days_per_user,
            'scenario_types': list(self.scenario_templates.keys()),
            'user_archetypes': [a['role'] for a in self.user_archetypes]
        }
        
        return {
            'summary': summary,
            'user_profiles': profiles,
            'telemetry_data': telemetry_data,
            'interaction_data': interaction_data
        }
    
    async def generate_massive_dataset(self, size: int = 100000) -> Dict[str, Any]:
        """Generate massive dataset for training"""
        logger.info(f"Generating massive dataset with {size} interactions")
        
        # Calculate parameters
        num_users = min(1000, size // 100)  # At least 100 interactions per user
        interactions_per_user = size // num_users
        
        return await self.generate_dataset(
            num_users=num_users,
            days_per_user=30,
            interactions_per_day=interactions_per_user // 30
        )
    
    def save_dataset(self, dataset: Dict[str, Any], filename_prefix: str = "synthetic_data"):
        """Save dataset in multiple formats"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save summary
        with open(self.output_dir / f"{filename_prefix}_summary_{timestamp}.json", 'w') as f:
            json.dump(dataset['summary'], f, indent=2, default=str)
        
        # Save user profiles
        profiles_df = pd.DataFrame([asdict(p) for p in dataset['user_profiles']])
        profiles_df.to_csv(self.output_dir / f"{filename_prefix}_profiles_{timestamp}.csv", index=False)
        
        # Save telemetry data
        telemetry_df = pd.DataFrame([asdict(t) for t in dataset['telemetry_data']])
        telemetry_df.to_csv(self.output_dir / f"{filename_prefix}_telemetry_{timestamp}.csv", index=False)
        
        # Save interaction data  
        with open(self.output_dir / f"{filename_prefix}_interactions_{timestamp}.jsonl", 'w') as f:
            for interaction in dataset['interaction_data']:
                f.write(json.dumps(interaction, default=str) + '\n')
        
        # Save combined JSON
        with open(self.output_dir / f"{filename_prefix}_complete_{timestamp}.json", 'w') as f:
            # Convert dataclass objects to dicts for JSON serialization
            json_dataset = {
                'summary': dataset['summary'],
                'user_profiles': [asdict(p) for p in dataset['user_profiles']],
                'telemetry_data': [asdict(t) for t in dataset['telemetry_data']],
                'interaction_data': dataset['interaction_data']
            }
            json.dump(json_dataset, f, indent=2, default=str)
        
        logger.info(f"Dataset saved with prefix: {filename_prefix}_{timestamp}")
        
        return {
            'summary_file': f"{filename_prefix}_summary_{timestamp}.json",
            'profiles_file': f"{filename_prefix}_profiles_{timestamp}.csv", 
            'telemetry_file': f"{filename_prefix}_telemetry_{timestamp}.csv",
            'interactions_file': f"{filename_prefix}_interactions_{timestamp}.jsonl",
            'complete_file': f"{filename_prefix}_complete_{timestamp}.json"
        }


async def main():
    """Main function for running synthetic data generation"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate Synthetic Data for AI Coach')
    parser.add_argument('--users', type=int, default=50, help='Number of users')
    parser.add_argument('--days', type=int, default=30, help='Days per user')
    parser.add_argument('--interactions', type=int, default=8, help='Interactions per day')
    parser.add_argument('--massive', action='store_true', help='Generate massive dataset')
    parser.add_argument('--size', type=int, default=100000, help='Size for massive dataset')
    parser.add_argument('--scenarios', type=str, help='Comma-separated scenario types')
    parser.add_argument('--output-dir', type=str, default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    # Create generator
    generator = SyntheticDataGenerator(args.output_dir)
    
    print("🔬 SYNTHETIC DATA GENERATOR")
    print("=" * 50)
    
    # Parse scenarios if provided
    scenario_list = None
    if args.scenarios:
        scenario_list = [s.strip() for s in args.scenarios.split(',')]
        print(f"Focusing on scenarios: {scenario_list}")
    
    # Generate dataset
    if args.massive:
        print(f"Generating massive dataset with {args.size} interactions...")
        dataset = await generator.generate_massive_dataset(args.size)
    else:
        print(f"Generating standard dataset...")
        print(f"Users: {args.users}, Days: {args.days}, Interactions/day: {args.interactions}")
        dataset = await generator.generate_dataset(
            num_users=args.users,
            days_per_user=args.days,
            interactions_per_day=args.interactions,
            scenarios=scenario_list
        )
    
    # Save dataset
    prefix = "massive_synthetic" if args.massive else "synthetic_data"
    files = generator.save_dataset(dataset, prefix)
    
    # Print summary
    summary = dataset['summary']
    print(f"\n📊 GENERATION COMPLETE")
    print(f"=" * 50)
    print(f"Users: {summary['num_users']}")
    print(f"Profiles: {summary['num_profiles']}")
    print(f"Telemetry Points: {summary['num_telemetry_points']}")
    print(f"Coaching Interactions: {summary['num_interactions']}")
    print(f"Days Generated: {summary['days_generated']}")
    
    print(f"\n📁 FILES GENERATED:")
    for file_type, filename in files.items():
        print(f"  {file_type}: {filename}")
    
    print(f"\n✅ Synthetic data generation completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())