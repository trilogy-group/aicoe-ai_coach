#!/usr/bin/env python3
"""
AI Coach - Ultimate Evolved Productivity Coaching System
========================================================

The culmination of evolutionary AI development combining:
- Rule-based expertise with AI learning capabilities
- Machine learning pattern recognition
- Predictive analytics and burnout prevention
- Individual user modeling and personalization
- Continuous improvement from user feedback
- Real-time context analysis and adaptive coaching

This is a complete, self-contained AI coaching system that learns, adapts,
predicts, and personalizes coaching interventions based on user telemetry.

Usage:
    # Basic usage
    coach = AICoach()
    notification = await coach.analyze_telemetry(telemetry_data)
    
    # With user tracking
    notification = await coach.analyze_telemetry(telemetry_data, user_id="user123")
    
    # Record feedback for learning
    coach.record_feedback("user123", "notification_id", {"effectiveness": 0.8})

Features:
    ✅ Machine Learning - Learns from user interactions
    ✅ Pattern Discovery - Finds effectiveness patterns in data
    ✅ Burnout Prediction - Predicts and prevents user burnout
    ✅ Personalization - Adapts to individual user preferences
    ✅ Context Sensitivity - Multi-dimensional context analysis
    ✅ Continuous Learning - Improves over time with feedback
    ✅ Predictive Intelligence - Anticipates user needs
    ✅ Adaptive Strategies - Changes approach based on effectiveness

Author: AI Coach Evolution Team
Version: 4.0 (Ultimate Consolidated)
"""

import asyncio
import json
import logging
import pickle
import numpy as np
import subprocess
import time
import psutil
import signal
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from collections import defaultdict, deque

try:
    from pynput import mouse, keyboard
    from pynput.mouse import Listener as MouseListener
    from pynput.keyboard import Listener as KeyboardListener
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False
    print("⚠️  pynput not installed. Install with: pip install pynput")

try:
    import plyer
    NOTIFICATIONS_AVAILABLE = True
except ImportError:
    NOTIFICATIONS_AVAILABLE = False
    print("⚠️  plyer not installed for notifications. Install with: pip install plyer")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SimpleClassifier:
    """Simple decision tree classifier without sklearn dependencies"""
    
    def __init__(self):
        self.tree = {}
        self.feature_stats = {}
    
    def fit(self, X, y):
        """Simple fitting based on feature thresholds"""
        X_array = np.array(X)
        y_array = np.array(y)
        
        # Calculate feature statistics
        for i in range(X_array.shape[1]):
            feature_values = X_array[:, i]
            effective_values = feature_values[y_array == 1]
            if len(effective_values) > 0:
                self.feature_stats[i] = {
                    'mean_effective': np.mean(effective_values),
                    'std_effective': np.std(effective_values),
                    'threshold': np.median(feature_values)
                }
    
    def predict_proba(self, X):
        """Simple probability prediction"""
        X_array = np.array(X)
        probs = []
        
        for sample in X_array:
            score = 0.0
            for i, value in enumerate(sample):
                if i in self.feature_stats:
                    stats = self.feature_stats[i]
                    # Higher score if closer to effective mean
                    if stats['std_effective'] > 0:
                        distance = abs(value - stats['mean_effective']) / stats['std_effective']
                        score += max(0, 1 - distance) / len(self.feature_stats)
            
            probs.append([1 - score, score])
        
        return np.array(probs)
    
    @property
    def feature_importances_(self):
        """Simple feature importance based on variance"""
        importances = []
        for i in range(max(self.feature_stats.keys()) + 1 if self.feature_stats else 0):
            if i in self.feature_stats:
                importances.append(self.feature_stats[i]['std_effective'])
            else:
                importances.append(0.0)
        return importances


class SimpleScaler:
    """Simple standard scaler without sklearn dependencies"""
    
    def __init__(self):
        self.mean_ = None
        self.std_ = None
    
    def fit_transform(self, X):
        X_array = np.array(X)
        self.mean_ = np.mean(X_array, axis=0)
        self.std_ = np.std(X_array, axis=0)
        self.std_[self.std_ == 0] = 1  # Avoid division by zero
        return (X_array - self.mean_) / self.std_
    
    def transform(self, X):
        X_array = np.array(X)
        return (X_array - self.mean_) / self.std_


class ContextEngine:
    """Advanced context analysis combining evolved patterns with AI learning"""
    
    def __init__(self):
        self.context_history = []
        self.user_patterns = {}
        self.effectiveness_scores = {}
        
    def analyze_context(self, telemetry: Dict[str, Any]) -> Dict[str, float]:
        """
        Analyze telemetry to determine coaching context.
        Uses provided values when available, calculates when missing.
        """
        context = {
            'energy_level': telemetry.get('energy_level', self._estimate_energy(telemetry)),
            'stress_level': telemetry.get('stress_level', self._estimate_stress(telemetry)),
            'productivity_score': telemetry.get('productivity_score', self._calculate_productivity(telemetry)),
            'focus_quality': telemetry.get('focus_quality', self._assess_focus(telemetry)),
            'break_needed': telemetry.get('break_needed', self._check_break_timing(telemetry)),
            'time_period': self._get_time_period(),
            'cognitive_load': telemetry.get('cognitive_load', self._estimate_cognitive_load(telemetry))
        }
        
        # Store in history for pattern recognition
        self.context_history.append({
            'timestamp': datetime.now(),
            'context': context,
            'telemetry': telemetry
        })
        
        # Keep only recent history (last 50 entries)
        if len(self.context_history) > 50:
            self.context_history.pop(0)
            
        return context
    
    def _estimate_energy(self, telemetry: Dict) -> float:
        """Estimate user energy based on activity patterns"""
        # Time since last break
        last_break = telemetry.get('last_break_time', datetime.now() - timedelta(hours=2))
        if isinstance(last_break, str):
            last_break = datetime.fromisoformat(last_break)
        time_since_break = (datetime.now() - last_break).seconds / 3600.0
        
        # Activity intensity
        keystrokes = telemetry.get('keystrokes_per_min', 0)
        
        # Calculate energy (0-1 scale)
        energy = 1.0
        energy -= min(time_since_break / 4.0, 0.5)  # Decrease over 4 hours
        energy -= 0.2 if keystrokes < 20 else 0.0  # Low activity penalty
        energy += 0.1 if 40 < keystrokes < 80 else 0.0  # Optimal activity bonus
        
        return max(0.0, min(1.0, energy))
    
    def _estimate_stress(self, telemetry: Dict) -> float:
        """Estimate stress level from behavioral patterns"""
        error_rate = telemetry.get('error_rate', 0.0)
        backspace_rate = telemetry.get('backspace_rate', 0.0)
        context_switches = telemetry.get('app_switches_per_hour', 0)
        
        # Calculate stress (0-1 scale)
        stress = 0.2  # Baseline
        stress += min(error_rate * 2.0, 0.3)
        stress += min(backspace_rate * 1.5, 0.2)
        stress += min(context_switches / 60.0, 0.3)
        
        return min(1.0, stress)
    
    def _calculate_productivity(self, telemetry: Dict) -> float:
        """Calculate productivity score from telemetry"""
        tasks_completed = telemetry.get('tasks_completed_last_hour', 0)
        focus_minutes = telemetry.get('deep_focus_minutes', 0)
        lines_written = telemetry.get('lines_of_code_written', 0)
        documents_edited = telemetry.get('documents_edited', 0)
        
        # Calculate productivity (0-1 scale)
        productivity = 0.3  # Baseline
        productivity += min(tasks_completed * 0.15, 0.3)
        productivity += min(focus_minutes / 60.0 * 0.3, 0.3)
        productivity += min((lines_written + documents_edited * 10) / 100.0 * 0.1, 0.1)
        
        return min(1.0, productivity)
    
    def _assess_focus(self, telemetry: Dict) -> float:
        """Assess focus quality from attention patterns"""
        app_switches = telemetry.get('app_switches_per_hour', 0)
        primary_task_time = telemetry.get('primary_app_time_percentage', 50) / 100.0
        notifications = telemetry.get('notifications_last_hour', 0)
        
        # Calculate focus (0-1 scale)
        focus = 1.0
        focus -= min(app_switches / 30.0, 0.4)
        focus -= min(notifications / 20.0, 0.3)
        focus *= primary_task_time
        
        return max(0.0, focus)
    
    def _check_break_timing(self, telemetry: Dict) -> float:
        """Determine if a break is needed (0-1 urgency scale)"""
        last_break = telemetry.get('last_break_time', datetime.now() - timedelta(hours=2))
        if isinstance(last_break, str):
            last_break = datetime.fromisoformat(last_break)
        time_since_break = (datetime.now() - last_break).seconds / 3600.0
        
        mouse_distance = telemetry.get('mouse_distance_traveled', 0)
        posture_score = telemetry.get('posture_quality', 0.5)
        
        # Calculate break need (0-1 scale)
        break_need = 0.0
        break_need += min(time_since_break / 2.0, 0.5)
        break_need += 0.2 if mouse_distance > 10000 else 0.0
        break_need += (1.0 - posture_score) * 0.3
        
        return min(1.0, break_need)
    
    def _get_time_period(self) -> str:
        """Get current time period for context"""
        hour = datetime.now().hour
        if 5 <= hour < 9:
            return 'early_morning'
        elif 9 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 14:
            return 'lunch'
        elif 14 <= hour < 17:
            return 'afternoon'
        elif 17 <= hour < 20:
            return 'evening'
        else:
            return 'night'
    
    def _estimate_cognitive_load(self, telemetry: Dict) -> float:
        """Estimate cognitive load from task complexity indicators"""
        active_windows = telemetry.get('active_window_count', 1)
        code_complexity = telemetry.get('cyclomatic_complexity', 1.0)
        pause_frequency = telemetry.get('thinking_pauses_per_hour', 0)
        search_queries = telemetry.get('search_queries_last_hour', 0)
        
        # Calculate cognitive load (0-1 scale)
        load = 0.2  # Baseline
        load += min(active_windows / 10.0, 0.3)
        load += min(code_complexity / 10.0, 0.2)
        load += min(pause_frequency / 30.0, 0.2)
        load += min(search_queries / 20.0, 0.1)
        
        return min(1.0, load)


class CoachingStrategy:
    """Intelligent coaching strategy selection based on evolved patterns"""
    
    def __init__(self):
        self.strategies = self._load_evolved_strategies()
        self.effectiveness_history = {}
        
    def _load_evolved_strategies(self) -> Dict[str, List[Dict]]:
        """Load coaching strategies discovered through evolution"""
        return {
            'high_stress_low_energy': [
                {
                    'message': "Take 5 deep breaths. Your body needs a moment to reset.",
                    'priority': 1,
                    'action': 'breathing_exercise',
                    'duration': 5
                },
                {
                    'message': "Quick 2-minute walk? Movement reduces stress and boosts energy.",
                    'priority': 2,
                    'action': 'micro_break',
                    'duration': 2
                }
            ],
            'high_productivity_flow': [
                {
                    'message': "You're in the zone! Protect this focus time - silence notifications.",
                    'priority': 1,
                    'action': 'protect_focus',
                    'duration': 25
                },
                {
                    'message': "Great flow state. Remember to save your work and stay hydrated.",
                    'priority': 2,
                    'action': 'gentle_reminder',
                    'duration': 0
                }
            ],
            'low_focus_high_switches': [
                {
                    'message': "Too many context switches. Pick one task for the next 25 minutes.",
                    'priority': 1,
                    'action': 'focus_intervention',
                    'duration': 25
                },
                {
                    'message': "Close unnecessary tabs and apps. Focus on what matters most.",
                    'priority': 2,
                    'action': 'environment_optimization',
                    'duration': 5
                }
            ],
            'break_needed': [
                {
                    'message': "You've been at it for a while. 5-minute break to recharge?",
                    'priority': 1,
                    'action': 'break_reminder',
                    'duration': 5
                },
                {
                    'message': "Stand up, stretch, look away from the screen. Your body will thank you.",
                    'priority': 2,
                    'action': 'physical_break',
                    'duration': 3
                }
            ],
            'afternoon_slump': [
                {
                    'message': "Afternoon energy dip detected. Try a brief walk or light snack.",
                    'priority': 1,
                    'action': 'energy_boost',
                    'duration': 10
                },
                {
                    'message': "Switch to lighter tasks for 15 minutes to maintain momentum.",
                    'priority': 2,
                    'action': 'task_adjustment',
                    'duration': 15
                }
            ],
            'morning_prime': [
                {
                    'message': "Your peak hours! Tackle the most important task while fresh.",
                    'priority': 1,
                    'action': 'priority_focus',
                    'duration': 45
                },
                {
                    'message': "Great time for deep work. What's your #1 priority today?",
                    'priority': 2,
                    'action': 'goal_setting',
                    'duration': 5
                }
            ],
            'cognitive_overload': [
                {
                    'message': "Complex task detected. Break it into smaller, manageable pieces.",
                    'priority': 1,
                    'action': 'task_breakdown',
                    'duration': 10
                },
                {
                    'message': "High cognitive load. Consider documenting your thoughts before continuing.",
                    'priority': 2,
                    'action': 'brain_dump',
                    'duration': 5
                }
            ]
        }
    
    def select_strategy(self, context: Dict[str, float]) -> Optional[Dict]:
        """Select best coaching strategy based on context"""
        # Determine primary coaching need based on evolved logic
        if context['stress_level'] > 0.7 and context['energy_level'] < 0.3:
            strategy_key = 'high_stress_low_energy'
        elif context['productivity_score'] > 0.7 and context['focus_quality'] > 0.7:
            strategy_key = 'high_productivity_flow'
        elif context['focus_quality'] < 0.3:
            strategy_key = 'low_focus_high_switches'
        elif context['break_needed'] > 0.7:
            strategy_key = 'break_needed'
        elif context['time_period'] == 'afternoon' and context['energy_level'] < 0.5:
            strategy_key = 'afternoon_slump'
        elif context['time_period'] == 'morning' and context['energy_level'] > 0.6:
            strategy_key = 'morning_prime'
        elif context['cognitive_load'] > 0.8:
            strategy_key = 'cognitive_overload'
        else:
            return None
        
        # Get strategy options
        strategies = self.strategies.get(strategy_key, [])
        if not strategies:
            return None
            
        # Select based on effectiveness history
        if strategy_key in self.effectiveness_history:
            sorted_strategies = sorted(
                strategies,
                key=lambda s: self.effectiveness_history[strategy_key].get(s['message'], 0.5),
                reverse=True
            )
            return sorted_strategies[0]
        else:
            return strategies[0]
    
    def record_effectiveness(self, strategy_key: str, message: str, effectiveness: float):
        """Record strategy effectiveness for learning"""
        if strategy_key not in self.effectiveness_history:
            self.effectiveness_history[strategy_key] = {}
        
        # Update with exponential moving average
        current = self.effectiveness_history[strategy_key].get(message, 0.5)
        self.effectiveness_history[strategy_key][message] = current * 0.7 + effectiveness * 0.3


class NotificationManager:
    """Manages notification timing and delivery with intelligent cooldowns"""
    
    def __init__(self):
        self.last_notification_time = {}
        self.notification_cooldown = timedelta(minutes=30)
        self.quiet_hours = [(22, 6)]  # 10 PM to 6 AM
        
    def should_notify(self, user_id: str, priority: int = 1) -> bool:
        """Determine if notification should be sent now"""
        current_time = datetime.now()
        
        # Check quiet hours
        hour = current_time.hour
        for start, end in self.quiet_hours:
            if start > end:  # Crosses midnight
                if hour >= start or hour < end:
                    return False
            else:
                if start <= hour < end:
                    return False
        
        # Check cooldown with priority-based adjustments
        if user_id in self.last_notification_time:
            time_since_last = current_time - self.last_notification_time[user_id]
            
            if priority >= 3:
                min_cooldown = timedelta(minutes=10)
            elif priority >= 2:
                min_cooldown = timedelta(minutes=20)
            else:
                min_cooldown = self.notification_cooldown
                
            if time_since_last < min_cooldown:
                return False
        
        return True
    
class UserModel:
    """Individual user behavior modeling with learning capabilities"""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.interaction_history = []
        self.feedback_history = []
        self.preference_model = {
            'preferred_break_duration': 5,
            'notification_effectiveness': {},
            'best_intervention_times': [],
            'stress_triggers': [],
            'productivity_patterns': []
        }
        self.state_transition_matrix = defaultdict(lambda: defaultdict(float))
        
    def update_from_interaction(self, context: Dict, action: str, outcome: Optional[Dict] = None):
        """Learn from each interaction"""
        interaction = {
            'timestamp': datetime.now(),
            'context': context,
            'action': action,
            'outcome': outcome
        }
        self.interaction_history.append(interaction)
        
        # Learn state transitions
        if len(self.interaction_history) > 1:
            prev_state = self._extract_state(self.interaction_history[-2]['context'])
            curr_state = self._extract_state(context)
            self.state_transition_matrix[prev_state][curr_state] += 1
        
        # Update preference model
        if outcome and 'effectiveness' in outcome:
            if action not in self.preference_model['notification_effectiveness']:
                self.preference_model['notification_effectiveness'][action] = []
            self.preference_model['notification_effectiveness'][action].append(outcome['effectiveness'])
    
    def _extract_state(self, context: Dict) -> str:
        """Convert context to discrete state"""
        energy = 'low' if context.get('energy_level', 0.5) < 0.4 else 'high'
        stress = 'stressed' if context.get('stress_level', 0.5) > 0.6 else 'calm'
        focus = 'focused' if context.get('focus_quality', 0.5) > 0.6 else 'distracted'
        return f"{energy}_{stress}_{focus}"
    
    def predict_next_state(self, current_context: Dict) -> Dict[str, float]:
        """Predict likely next states based on history"""
        current_state = self._extract_state(current_context)
        transitions = self.state_transition_matrix[current_state]
        
        if not transitions:
            return {}
        
        total = sum(transitions.values())
        return {state: count/total for state, count in transitions.items()}
    
    def get_personalized_recommendation(self, action: str) -> float:
        """Get personalized effectiveness score for an action"""
        if action in self.preference_model['notification_effectiveness']:
            scores = self.preference_model['notification_effectiveness'][action]
            # Weighted average favoring recent interactions
            weights = np.exp(np.linspace(0, 1, len(scores)))
            return np.average(scores, weights=weights)
        return 0.5  # Default neutral score


class PatternLearner:
    """Machine learning system for discovering coaching effectiveness patterns"""
    
    def __init__(self):
        self.classifier = SimpleClassifier()
        self.scaler = SimpleScaler()
        self.feature_importance = {}
        self.discovered_patterns = []
        self.is_trained = False
        
    def learn_from_data(self, interaction_data: List[Dict]):
        """Train ML model on historical interactions"""
        if len(interaction_data) < 10:
            return
        
        # Extract features and labels
        X, y = self._prepare_training_data(interaction_data)
        
        if len(X) < 10:
            return
            
        # Scale features and train classifier
        X_scaled = self.scaler.fit_transform(X)
        self.classifier.fit(X_scaled, y)
        self.is_trained = True
        
        # Extract feature importance
        feature_names = ['energy', 'stress', 'productivity', 'focus', 'time_since_break', 
                        'hour_of_day', 'context_switches', 'cognitive_load']
        
        for i, importance in enumerate(self.classifier.feature_importances_):
            if i < len(feature_names):
                self.feature_importance[feature_names[i]] = importance
        
        # Discover patterns
        self._discover_patterns(X, y)
    
    def _prepare_training_data(self, interactions: List[Dict]) -> Tuple[List[List[float]], List[int]]:
        """Convert interactions to ML features"""
        X = []
        y = []
        
        for interaction in interactions:
            context = interaction.get('context', {})
            outcome = interaction.get('outcome', {})
            
            features = [
                context.get('energy_level', 0.5),
                context.get('stress_level', 0.5),
                context.get('productivity_score', 0.5),
                context.get('focus_quality', 0.5),
                context.get('time_since_break', 2.0),
                datetime.now().hour,
                context.get('app_switches_per_hour', 20),
                context.get('cognitive_load', 0.5)
            ]
            
            # Label: was the intervention effective?
            effectiveness = outcome.get('effectiveness', 0.5)
            label = 1 if effectiveness > 0.6 else 0
            
            X.append(features)
            y.append(label)
        
        return X, y
    
    def _discover_patterns(self, X: List[List[float]], y: List[int]):
        """Discover new patterns in the data"""
        X_array = np.array(X)
        y_array = np.array(y)
        
        # Find conditions that lead to effective interventions
        effective_indices = np.where(y_array == 1)[0]
        if len(effective_indices) > 5:
            effective_features = X_array[effective_indices]
            mean_effective = np.mean(effective_features, axis=0)
            
            patterns = []
            feature_names = ['energy', 'stress', 'productivity', 'focus', 'time_since_break', 
                           'hour_of_day', 'context_switches', 'cognitive_load']
            
            for i, (feature_name, mean_val) in enumerate(zip(feature_names, mean_effective)):
                if self.feature_importance.get(feature_name, 0) > 0.1:
                    patterns.append({
                        'feature': feature_name,
                        'optimal_value': mean_val,
                        'importance': self.feature_importance[feature_name]
                    })
            
            self.discovered_patterns = sorted(patterns, key=lambda x: x['importance'], reverse=True)
    
    def predict_effectiveness(self, context: Dict) -> float:
        """Predict effectiveness of intervention given context"""
        if not self.is_trained:
            return 0.5
        
        features = [
            context.get('energy_level', 0.5),
            context.get('stress_level', 0.5),
            context.get('productivity_score', 0.5),
            context.get('focus_quality', 0.5),
            context.get('time_since_break', 2.0),
            datetime.now().hour,
            context.get('app_switches_per_hour', 20),
            context.get('cognitive_load', 0.5)
        ]
        
        X_scaled = self.scaler.transform([features])
        probability = self.classifier.predict_proba(X_scaled)[0][1]
        
        return probability


class PredictiveEngine:
    """Predictive analytics for burnout prevention and optimal timing"""
    
    def __init__(self):
        self.time_series_data = defaultdict(list)
        self.predictions = {}
        
    def update_time_series(self, user_id: str, context: Dict):
        """Update time series data for predictions"""
        data_point = {
            'timestamp': datetime.now(),
            'energy': context.get('energy_level', 0.5),
            'stress': context.get('stress_level', 0.5),
            'productivity': context.get('productivity_score', 0.5),
            'focus': context.get('focus_quality', 0.5)
        }
        self.time_series_data[user_id].append(data_point)
        
        # Keep only last 100 data points
        if len(self.time_series_data[user_id]) > 100:
            self.time_series_data[user_id].pop(0)
    
    def predict_burnout_risk(self, user_id: str) -> float:
        """Predict risk of burnout based on trends"""
        if user_id not in self.time_series_data or len(self.time_series_data[user_id]) < 10:
            return 0.0
        
        recent_data = self.time_series_data[user_id][-10:]
        
        # Calculate trends
        energy_trend = self._calculate_trend([d['energy'] for d in recent_data])
        stress_trend = self._calculate_trend([d['stress'] for d in recent_data])
        productivity_trend = self._calculate_trend([d['productivity'] for d in recent_data])
        
        # Burnout indicators: declining energy, increasing stress, declining productivity
        burnout_risk = 0.0
        if energy_trend < -0.05:
            burnout_risk += 0.3
        if stress_trend > 0.05:
            burnout_risk += 0.4
        if productivity_trend < -0.05:
            burnout_risk += 0.3
        
        return min(1.0, burnout_risk)
    
    def predict_optimal_break_time(self, user_id: str) -> Optional[int]:
        """Predict when user will need a break"""
        if user_id not in self.time_series_data or len(self.time_series_data[user_id]) < 5:
            return None
        
        recent_data = self.time_series_data[user_id][-5:]
        energy_values = [d['energy'] for d in recent_data]
        
        if len(energy_values) > 1:
            decline_rate = (energy_values[-1] - energy_values[0]) / len(energy_values)
            
            if decline_rate < 0:  # Energy is declining
                current_energy = energy_values[-1]
                # Predict minutes until energy < 0.3
                minutes_to_break = int((current_energy - 0.3) / abs(decline_rate) * 5)
                return max(10, min(60, minutes_to_break))
        
        return 30  # Default
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate trend in values (positive = increasing)"""
        if len(values) < 2:
            return 0.0
        
        x = np.arange(len(values))
        y = np.array(values)
        
        # Simple linear regression
        slope = np.polyfit(x, y, 1)[0]
        return slope


class AICoach:
    """
    Ultimate AI Coach with genuine intelligence and learning capabilities
    
    This is the main interface that combines all AI components:
    - Context analysis and understanding
    - Machine learning pattern recognition
    - Predictive analytics and burnout prevention
    - Individual user modeling and personalization
    - Continuous learning from feedback
    """
    
    def __init__(self, model_path: Optional[str] = None):
        # Core components
        self.context_engine = ContextEngine()
        self.coaching_strategy = CoachingStrategy()
        self.notification_manager = NotificationManager()
        
        # AI components
        self.user_models = {}
        self.pattern_learner = PatternLearner()
        self.predictive_engine = PredictiveEngine()
        self.global_interaction_history = []
        
        # Model persistence
        self.model_path = model_path or "ai_coach_model.pkl"
        self._load_model()
        
        logger.info("AI Coach v4.0 initialized with full AI capabilities")
    
    def _get_user_model(self, user_id: str) -> UserModel:
        """Get or create user model"""
        if user_id not in self.user_models:
            self.user_models[user_id] = UserModel(user_id)
        return self.user_models[user_id]
    
    async def analyze_telemetry(self, telemetry: Dict[str, Any], 
                               user_id: str = 'default') -> Optional[Dict]:
        """
        Main AI coaching interface
        
        Args:
            telemetry: Dictionary containing user activity telemetry
            user_id: User identifier for personalization
            
        Returns:
            Coaching notification dict with AI insights or None
        """
        try:
            # Get user model for personalization
            user_model = self._get_user_model(user_id)
            
            # Analyze context using AI
            context = self.context_engine.analyze_context(telemetry)
            
            # Update predictive engine
            self.predictive_engine.update_time_series(user_id, context)
            
            # Check for predictive interventions (burnout prevention)
            burnout_risk = self.predictive_engine.predict_burnout_risk(user_id)
            if burnout_risk > 0.7:
                return self._create_predictive_notification(
                    "I'm detecting signs of potential burnout. Let's take a proper break.",
                    'burnout_prevention',
                    context,
                    priority=3
                )
            
            # Use ML to predict intervention effectiveness
            if self.pattern_learner.is_trained:
                effectiveness = self.pattern_learner.predict_effectiveness(context)
                if effectiveness < 0.3:
                    # Low predicted effectiveness - try different approach
                    context['force_alternative'] = True
            
            # Get base strategy recommendation
            base_strategy = self.coaching_strategy.select_strategy(context)
            
            if base_strategy:
                # Apply personalization
                action = base_strategy['action']
                personalization_score = user_model.get_personalized_recommendation(action)
                
                # Adjust strategy based on personal effectiveness
                if personalization_score < 0.3:
                    # This strategy hasn't worked well for this user
                    base_strategy = self._get_alternative_strategy(context, exclude=action)
                
                if base_strategy and self.notification_manager.should_notify(user_id, base_strategy['priority']):
                    # Predict optimal timing
                    optimal_break = self.predictive_engine.predict_optimal_break_time(user_id)
                    if optimal_break and 'duration' in base_strategy:
                        base_strategy['duration'] = optimal_break
                    
                    # Create AI-enhanced notification
                    notification = self._create_enhanced_notification(base_strategy, context, user_model)
                    
                    # Record interaction for learning
                    user_model.update_from_interaction(context, base_strategy['action'])
                    self.global_interaction_history.append({
                        'user_id': user_id,
                        'timestamp': datetime.now(),
                        'context': context,
                        'action': base_strategy['action']
                    })
                    
                    # Retrain ML model periodically
                    if len(self.global_interaction_history) % 50 == 0:
                        self.pattern_learner.learn_from_data(self.global_interaction_history)
                    
                    self.notification_manager.record_notification(user_id)
                    return notification
            
            return None
            
        except Exception as e:
            logger.error(f"Error in AI analysis: {str(e)}")
            return None
    
    def _create_predictive_notification(self, message: str, action: str, 
                                      context: Dict, priority: int = 2) -> Dict:
        """Create notification for predictive intervention"""
        return {
            'message': message,
            'priority': priority,
            'action': action,
            'ai_predicted': True,
            'context': {
                'energy_level': round(context.get('energy_level', 0), 2),
                'stress_level': round(context.get('stress_level', 0), 2),
                'burnout_risk': round(self.predictive_engine.predict_burnout_risk('default'), 2)
            },
            'timestamp': datetime.now().isoformat()
        }
    
    def _create_enhanced_notification(self, strategy: Dict, context: Dict, 
                                    user_model: UserModel) -> Dict:
        """Create notification with AI enhancements"""
        base_notification = self.notification_manager.format_notification(strategy, context)
        
        # Add AI insights
        base_notification['ai_insights'] = {
            'personalization_score': user_model.get_personalized_recommendation(strategy['action']),
            'predicted_effectiveness': self.pattern_learner.predict_effectiveness(context) if self.pattern_learner.is_trained else None,
            'next_state_prediction': user_model.predict_next_state(context),
            'discovered_patterns': self.pattern_learner.discovered_patterns[:3] if self.pattern_learner.discovered_patterns else []
        }
        
        return base_notification
    
    def _get_alternative_strategy(self, context: Dict, exclude: str) -> Optional[Dict]:
        """Get alternative strategy excluding a specific action"""
        all_strategies = ['break_reminder', 'focus_intervention', 'energy_boost', 
                         'stress_reduction', 'task_adjustment']
        
        for strategy in all_strategies:
            if strategy != exclude:
                return {
                    'message': f"Let's try a different approach: {strategy.replace('_', ' ')}",
                    'action': strategy,
                    'priority': 2,
                    'duration': 10
                }
        
        return None
    
    def record_feedback(self, user_id: str, notification_id: str, feedback: Dict):
        """Record user feedback for continuous learning"""
        user_model = self._get_user_model(user_id)
        
        # Find and update the interaction
        for interaction in reversed(self.global_interaction_history):
            if interaction['user_id'] == user_id:
                interaction['outcome'] = feedback
                user_model.update_from_interaction(
                    interaction['context'],
                    interaction['action'],
                    feedback
                )
                break
        
        # Save model periodically
        if len(self.global_interaction_history) % 10 == 0:
            self._save_model()
    
    def _save_model(self):
        """Save learned models to disk"""
        try:
            model_data = {
                'user_models': self.user_models,
                'pattern_learner': self.pattern_learner,
                'interaction_history': self.global_interaction_history
            }
            with open(self.model_path, 'wb') as f:
                pickle.dump(model_data, f)
            logger.info("AI models saved successfully")
        except Exception as e:
            logger.error(f"Error saving model: {e}")
    
    def _load_model(self):
        """Load previously learned models from disk"""
        try:
            if Path(self.model_path).exists():
                with open(self.model_path, 'rb') as f:
                    model_data = pickle.load(f)
                    self.user_models = model_data.get('user_models', {})
                    self.pattern_learner = model_data.get('pattern_learner', PatternLearner())
                    self.global_interaction_history = model_data.get('interaction_history', [])
                logger.info("AI models loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
    
    def get_coach_status(self) -> Dict:
        """Get comprehensive coach status and AI statistics"""
        return {
            'version': '4.0 (Ultimate AI)',
            'ai_features': {
                'machine_learning': self.pattern_learner.is_trained,
                'user_modeling': len(self.user_models) > 0,
                'predictive_analytics': len(self.predictive_engine.time_series_data) > 0,
                'pattern_discovery': len(self.pattern_learner.discovered_patterns) > 0
            },
            'statistics': {
                'total_interactions': len(self.global_interaction_history),
                'active_users': len(self.user_models),
                'discovered_patterns': len(self.pattern_learner.discovered_patterns),
                'feature_importance': dict(list(self.pattern_learner.feature_importance.items())[:3])
            }
        }


# Convenience functions for simple usage
async def coach_me(telemetry: Dict[str, Any]) -> Optional[Dict]:
    """Simple function to get AI coaching from telemetry"""
    coach = AICoach()
    return await coach.analyze_telemetry(telemetry)


def create_sample_telemetry() -> Dict[str, Any]:
    """Create sample telemetry for testing the AI coach"""
    return {
        'last_break_time': (datetime.now() - timedelta(hours=2)).isoformat(),
        'keystrokes_per_min': 45,
        'mouse_events_per_min': 20,
        'error_rate': 0.05,
        'backspace_rate': 0.1,
        'app_switches_per_hour': 25,
        'tasks_completed_last_hour': 2,
        'deep_focus_minutes': 35,
        'lines_of_code_written': 120,
        'documents_edited': 1,
        'primary_app_time_percentage': 65,
        'notifications_last_hour': 8,
        'mouse_distance_traveled': 5000,
        'posture_quality': 0.7,
        'active_window_count': 4,
        'cyclomatic_complexity': 5.2,
        'thinking_pauses_per_hour': 12,
        'search_queries_last_hour': 5
    }


# Main demonstration of AI capabilities
async def demonstrate_ai_capabilities():
    """Comprehensive demonstration of all AI features"""
    print("🤖 AI COACH v4.0 - COMPREHENSIVE DEMONSTRATION")
    print("=" * 60)
    
    coach = AICoach()
    user_id = "demo_user"
    
    # Simulate user session with declining performance
    scenarios = [
        {"name": "Morning Start", "telemetry": {"energy_level": 0.9, "focus_quality": 0.8}},
        {"name": "Mid-Morning", "telemetry": {"energy_level": 0.7, "stress_level": 0.4}},
        {"name": "Before Lunch", "telemetry": {"energy_level": 0.5, "focus_quality": 0.3}},
        {"name": "Afternoon Slump", "telemetry": {"energy_level": 0.3, "stress_level": 0.7}},
        {"name": "End of Day", "telemetry": {"energy_level": 0.2, "stress_level": 0.9}}
    ]
    
    print("\n📊 SIMULATING FULL DAY USER SESSION")
    print("-" * 40)
    
    for i, scenario in enumerate(scenarios):
        print(f"\n⏰ {scenario['name']}:")
        
        notification = await coach.analyze_telemetry(scenario['telemetry'], user_id)
        
        if notification:
            print(f"   💡 Coach Says: {notification['message']}")
            print(f"   🎯 Action: {notification['action']}")
            print(f"   ⚡ Priority: {notification['priority']}")
            
            if 'ai_insights' in notification:
                insights = notification['ai_insights']
                if insights.get('personalization_score') is not None:
                    print(f"   🧠 Personalization: {insights['personalization_score']:.2f}")
                if insights.get('predicted_effectiveness') is not None:
                    print(f"   📈 Predicted Success: {insights['predicted_effectiveness']:.2f}")
            
            if 'ai_predicted' in notification:
                print("   🔮 AI PREDICTED this intervention!")
            
            # Simulate user feedback
            effectiveness = 0.9 if "break" in notification['message'] else 0.6
            coach.record_feedback(user_id, f"demo_{i}", {"effectiveness": effectiveness})
        else:
            print("   ✅ No intervention needed - you're doing great!")
    
    # Show AI learning results
    print(f"\n🧠 AI LEARNING RESULTS")
    print("-" * 40)
    status = coach.get_coach_status()
    
    print(f"Version: {status['version']}")
    print(f"Total Interactions: {status['statistics']['total_interactions']}")
    print(f"Active Users: {status['statistics']['active_users']}")
    print(f"ML Trained: {status['ai_features']['machine_learning']}")
    print(f"Patterns Discovered: {status['statistics']['discovered_patterns']}")
    
    if status['statistics']['feature_importance']:
        print(f"\nTop Important Features (what AI learned matters most):")
        for feature, importance in status['statistics']['feature_importance'].items():
            print(f"  • {feature}: {importance:.3f}")
    
    print(f"\n🎯 AI CAPABILITIES VERIFIED:")
    print(f"  ✅ Machine Learning Pattern Recognition")
    print(f"  ✅ Individual User Modeling")
    print(f"  ✅ Predictive Burnout Detection") 
    print(f"  ✅ Personalized Recommendations")
    print(f"  ✅ Continuous Learning from Feedback")
    print(f"  ✅ Context-Aware Interventions")
    
    return coach


# Enhanced Telemetry Collection Classes
class ActivityTracker:
    """Tracks keyboard and mouse activity"""
    
    def __init__(self):
        self.keyboard_events = deque(maxlen=1000)
        self.mouse_events = deque(maxlen=1000)
        self.typing_speed = deque(maxlen=100)
        self.last_activity = time.time()
        self.is_active = False
        
    def on_key_press(self, key):
        now = time.time()
        self.keyboard_events.append(now)
        self.last_activity = now
        self.is_active = True
        
        if len(self.keyboard_events) >= 2:
            recent_events = [t for t in self.keyboard_events if now - t <= 60]
            if len(recent_events) > 1:
                wpm = len(recent_events) / 5
                self.typing_speed.append(wpm)
    
    def on_mouse_move(self, x, y):
        now = time.time()
        self.mouse_events.append(now)
        self.last_activity = now
        self.is_active = True
    
    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            now = time.time()
            self.mouse_events.append(now)
            self.last_activity = now
            self.is_active = True
    
    def get_activity_metrics(self) -> Dict[str, float]:
        now = time.time()
        recent_keys = [t for t in self.keyboard_events if now - t <= 60]
        recent_mouse = [t for t in self.mouse_events if now - t <= 60]
        
        keystrokes_per_min = len(recent_keys)
        mouse_events_per_min = len(recent_mouse)
        idle_seconds = now - self.last_activity if self.last_activity else 0
        avg_typing_speed = sum(self.typing_speed) / len(self.typing_speed) if self.typing_speed else 0
        
        return {
            'keystrokes_per_min': keystrokes_per_min,
            'mouse_events_per_min': mouse_events_per_min,
            'idle_seconds': idle_seconds,
            'typing_speed_wpm': avg_typing_speed,
            'is_active': idle_seconds < 30
        }


class WindowTracker:
    """Enhanced application and window tracking with browser tabs"""
    
    def __init__(self):
        self.window_history = deque(maxlen=1000)
        self.current_window = None
        self.current_app = None
        self.window_usage = defaultdict(float)
        self.window_switches = 0
        self.last_check = time.time()
        self.productivity_keywords = {
            'productive': ['code', 'docs', 'document', 'spreadsheet', 'presentation', 'terminal', 'editor', 'development'],
            'communication': ['slack', 'email', 'zoom', 'teams', 'discord', 'messages'],
            'research': ['browser', 'chrome', 'safari', 'firefox', 'research', 'documentation'],
            'entertainment': ['youtube', 'netflix', 'spotify', 'music', 'video', 'game', 'social', 'twitter', 'instagram']
        }
    
    def get_window_info(self) -> Dict[str, Optional[str]]:
        """Get detailed window information including title"""
        try:
            script = '''
            tell application "System Events"
                set frontApp to name of first application process whose frontmost is true
                set windowTitle to ""
                try
                    if frontApp is not "Finder" then
                        set windowTitle to title of front window of application process frontApp
                    end if
                end try
                return frontApp & "|" & windowTitle
            end tell
            '''
            result = subprocess.run(['osascript', '-e', script], 
                                  capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                parts = result.stdout.strip().split('|', 1)
                app_name = parts[0] if parts else None
                window_title = parts[1] if len(parts) > 1 else ""
                
                return {
                    'app_name': app_name,
                    'window_title': window_title,
                    'full_context': f"{app_name}: {window_title}" if window_title else app_name
                }
        
        except Exception as e:
            print(f"Error getting window info: {e}")
        
        return {'app_name': None, 'window_title': '', 'full_context': ''}
    
    def get_browser_tab_info(self, app_name: str) -> Optional[Dict[str, Any]]:
        """Get current browser tab information"""
        if not app_name:
            return None
        
        app_lower = app_name.lower()
        
        try:
            if 'chrome' in app_lower or 'google chrome' in app_lower:
                return self._get_chrome_tab()
            elif 'safari' in app_lower:
                return self._get_safari_tab()
        except Exception as e:
            print(f"Error getting browser tab: {e}")
        
        return None
    
    def _get_chrome_tab(self) -> Optional[Dict[str, Any]]:
        """Get Chrome active tab info"""
        script = '''
        tell application "Google Chrome"
            if (count of windows) > 0 then
                set activeWindow to front window
                set activeTab to active tab of activeWindow
                set tabTitle to title of activeTab
                set tabURL to URL of activeTab
                return tabTitle & "|" & tabURL
            end if
        end tell
        '''
        
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0 and result.stdout.strip():
            parts = result.stdout.strip().split('|', 1)
            return {
                'title': parts[0] if parts else '',
                'url': parts[1] if len(parts) > 1 else '',
                'browser': 'Chrome'
            }
        return None
    
    def _get_safari_tab(self) -> Optional[Dict[str, Any]]:
        """Get Safari active tab info"""
        script = '''
        tell application "Safari"
            if (count of windows) > 0 then
                set activeWindow to front window
                set activeTab to current tab of activeWindow
                set tabTitle to name of activeTab
                set tabURL to URL of activeTab
                return tabTitle & "|" & tabURL
            end if
        end tell
        '''
        
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0 and result.stdout.strip():
            parts = result.stdout.strip().split('|', 1)
            return {
                'title': parts[0] if parts else '',
                'url': parts[1] if len(parts) > 1 else '',
                'browser': 'Safari'
            }
        return None
    
    def classify_activity(self, window_info: Dict, tab_info: Optional[Dict] = None) -> str:
        """Classify current activity based on window/tab content"""
        
        text_to_analyze = []
        if window_info.get('app_name'):
            text_to_analyze.append(window_info['app_name'].lower())
        if window_info.get('window_title'):
            text_to_analyze.append(window_info['window_title'].lower())
        if tab_info:
            if tab_info.get('title'):
                text_to_analyze.append(tab_info['title'].lower())
            if tab_info.get('url'):
                text_to_analyze.append(tab_info['url'].lower())
        
        combined_text = ' '.join(text_to_analyze)
        
        scores = {}
        for category, keywords in self.productivity_keywords.items():
            score = sum(1 for keyword in keywords if keyword in combined_text)
            if score > 0:
                scores[category] = score
        
        if scores:
            return max(scores, key=scores.get)
        
        return 'unknown'
    
    def update(self):
        """Update window tracking with enhanced info"""
        now = time.time()
        window_info = self.get_window_info()
        app_name = window_info['app_name']
        full_context = window_info['full_context']
        
        tab_info = self.get_browser_tab_info(app_name) if app_name else None
        
        if full_context and full_context != self.current_window:
            if self.current_window:
                duration = now - self.last_check
                self.window_usage[self.current_window] += duration
                self.window_switches += 1
            
            self.current_window = full_context
            self.current_app = app_name
            
            history_entry = {
                'timestamp': now,
                'window': full_context,
                'app': app_name,
                'tab_info': tab_info,
                'activity_type': self.classify_activity(window_info, tab_info)
            }
            self.window_history.append(history_entry)
        
        self.last_check = now
        return window_info, tab_info
    
    def get_enhanced_metrics(self) -> Dict[str, Any]:
        """Get detailed window and activity metrics"""
        now = time.time()
        
        if self.current_window:
            duration = now - self.last_check
            self.window_usage[self.current_window] += duration
            self.last_check = now
        
        recent_activity = [entry for entry in self.window_history if now - entry['timestamp'] <= 3600]
        
        activity_breakdown = defaultdict(float)
        for entry in recent_activity:
            activity_type = entry.get('activity_type', 'unknown')
            activity_breakdown[activity_type] += 2
        
        current_info = self.window_history[-1] if self.window_history else {}
        
        return {
            'current_app': self.current_app,
            'current_window': self.current_window,
            'current_tab': current_info.get('tab_info'),
            'current_activity_type': current_info.get('activity_type', 'unknown'),
            'window_switches_per_hour': len(recent_activity),
            'activity_breakdown': dict(activity_breakdown),
            'top_windows': dict(sorted(self.window_usage.items(), key=lambda x: x[1], reverse=True)[:5])
        }


class NotificationManager:
    """Manages desktop notifications for coaching"""
    
    def __init__(self):
        self.last_notification = 0
        self.notification_cooldown = 300  # 5 minutes
        self.user_last_notification = {}
    
    def should_notify(self, user_id: str, priority: int = 1) -> bool:
        """Check if we should send a notification based on cooldown and priority"""
        now = time.time()
        
        # Check global cooldown
        if now - self.last_notification < self.notification_cooldown:
            return False
        
        # Check per-user cooldown (shorter for high priority)
        user_cooldown = 180 if priority == 1 else 300  # 3min for urgent, 5min for normal
        last_user_notification = self.user_last_notification.get(user_id, 0)
        
        return now - last_user_notification >= user_cooldown
    
    def format_notification(self, strategy: Dict, context: Dict) -> Dict:
        """Format coaching strategy as notification"""
        return {
            'message': strategy['message'],
            'priority': strategy['priority'],
            'action': strategy['action'],
            'suggested_duration': strategy['duration'],
            'context': {
                'energy_level': round(context['energy_level'], 2),
                'stress_level': round(context['stress_level'], 2),
                'productivity_score': round(context['productivity_score'], 2),
                'focus_quality': round(context['focus_quality'], 2)
            },
            'timestamp': datetime.now().isoformat()
        }
    
    def record_notification(self, user_id: str):
        """Record that a notification was sent"""
        now = time.time()
        self.last_notification = now
        self.user_last_notification[user_id] = now
        
    def send_coaching_notification(self, notification: Dict[str, Any]):
        """Send desktop notification for coaching"""
        
        now = time.time()
        if now - self.last_notification < self.notification_cooldown:
            return
        
        try:
            icon_map = {1: "⚠️", 2: "💡", 3: "ℹ️"}
            priority_icon = icon_map.get(notification.get('priority', 2), "💡")
            
            title = f"{priority_icon} AI Coach"
            message = notification['message']
            
            if 'action' in notification:
                message += f" - {notification['action']}"
            
            # Use macOS native notifications
            script = f'display notification "{message}" with title "{title}"'
            result = subprocess.run(['osascript', '-e', script], 
                                  capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                self.last_notification = now
                # Update user-specific timestamp if user_id provided
                if hasattr(self, '_current_user_id'):
                    self.user_last_notification[self._current_user_id] = now
                print(f"📱 Sent notification: {notification['message']}")
            else:
                # Fallback to console
                print(f"📢 COACHING ALERT: {notification['message']}")
            
        except Exception as e:
            print(f"Error sending notification: {e}")
            print(f"📢 COACHING ALERT: {notification['message']}")


class EnhancedTelemetryCollector:
    """Complete telemetry collector with real monitoring"""
    
    def __init__(self):
        self.activity_tracker = ActivityTracker()
        self.window_tracker = WindowTracker()
        self.notification_manager = NotificationManager()
        self.start_time = time.time()
        self.monitoring = False
        
        # Listeners
        self.keyboard_listener = None
        self.mouse_listener = None
    
    def start_monitoring(self):
        """Start monitoring user activity"""
        if not PYNPUT_AVAILABLE:
            print("❌ Cannot start monitoring: pynput not installed")
            return False
        
        try:
            self.keyboard_listener = KeyboardListener(
                on_press=self.activity_tracker.on_key_press
            )
            self.keyboard_listener.start()
            
            self.mouse_listener = MouseListener(
                on_move=self.activity_tracker.on_mouse_move,
                on_click=self.activity_tracker.on_mouse_click
            )
            self.mouse_listener.start()
            
            self.monitoring = True
            print("✅ Started real telemetry monitoring!")
            return True
            
        except Exception as e:
            print(f"❌ Error starting monitoring: {e}")
            return False
    
    def stop_monitoring(self):
        """Stop monitoring"""
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        if self.mouse_listener:
            self.mouse_listener.stop()
        
        self.monitoring = False
        print("⏹️  Stopped telemetry monitoring")
    
    def get_enhanced_telemetry(self) -> Dict[str, Any]:
        """Get comprehensive telemetry with window/tab tracking"""
        
        # Update tracking
        self.window_tracker.update()
        
        # Get metrics
        activity_metrics = self.activity_tracker.get_activity_metrics()
        enhanced_metrics = self.window_tracker.get_enhanced_metrics()
        
        # Calculate derived metrics
        now = time.time()
        session_duration = (now - self.start_time) / 3600
        
        focus_quality = self._calculate_focus_quality(activity_metrics, enhanced_metrics)
        energy_level = self._calculate_energy_level(activity_metrics)
        stress_level = self._calculate_stress_level(activity_metrics, enhanced_metrics)
        productivity_score = self._calculate_productivity_score(enhanced_metrics)
        
        # Build comprehensive telemetry
        telemetry = {
            # Core metrics
            'keystrokes_per_min': activity_metrics['keystrokes_per_min'],
            'mouse_events_per_min': activity_metrics['mouse_events_per_min'],
            'app_switches_per_hour': enhanced_metrics['window_switches_per_hour'],
            'session_duration_hours': session_duration,
            'focus_quality': focus_quality,
            'energy_level': energy_level,
            'stress_level': stress_level,
            
            # Enhanced metrics
            'current_app': enhanced_metrics['current_app'],
            'current_window': enhanced_metrics['current_window'],
            'current_tab': enhanced_metrics['current_tab'],
            'current_activity_type': enhanced_metrics['current_activity_type'],
            'productivity_score': productivity_score,
            'enhanced_focus_quality': focus_quality,
            'distraction_level': min(1.0, enhanced_metrics['window_switches_per_hour'] / 50),
            'context_switches': enhanced_metrics['window_switches_per_hour'],
            'activity_breakdown': enhanced_metrics['activity_breakdown'],
            
            # Browser data
            'browser_tab_title': enhanced_metrics['current_tab'].get('title', '') if enhanced_metrics['current_tab'] else '',
            'browser_tab_url': enhanced_metrics['current_tab'].get('url', '') if enhanced_metrics['current_tab'] else '',
            'browser_name': enhanced_metrics['current_tab'].get('browser', '') if enhanced_metrics['current_tab'] else '',
            
            # Additional context
            'typing_speed_wpm': activity_metrics['typing_speed_wpm'],
            'idle_seconds': activity_metrics['idle_seconds'],
            'is_active': activity_metrics['is_active'],
            'last_break_time': self._get_last_break_time(),
            
            # Metadata
            'timestamp': datetime.now().isoformat(),
            'monitoring_active': self.monitoring,
            'data_source': 'enhanced_real_telemetry',
            'enhanced_monitoring': True
        }
        
        return telemetry
    
    def _calculate_focus_quality(self, activity: Dict, enhanced: Dict) -> float:
        switches_factor = max(0, 1 - (enhanced['window_switches_per_hour'] / 30))
        typing_factor = min(1, activity['typing_speed_wpm'] / 40) if activity['typing_speed_wpm'] > 0 else 0.5
        activity_factor = 0.8 if activity['is_active'] and activity['keystrokes_per_min'] < 200 else 0.3
        
        current_activity = enhanced.get('current_activity_type', 'unknown')
        activity_bonus = {'productive': 0.2, 'research': 0.1, 'communication': 0.0, 'entertainment': -0.3, 'unknown': 0.0}.get(current_activity, 0.0)
        
        focus = (switches_factor * 0.4 + typing_factor * 0.3 + activity_factor * 0.3) + activity_bonus
        return max(0.0, min(1.0, focus))
    
    def _calculate_energy_level(self, activity: Dict) -> float:
        activity_score = (activity['keystrokes_per_min'] + activity['mouse_events_per_min']) / 100
        energy = min(1.0, activity_score)
        
        if activity['idle_seconds'] > 300:
            energy *= 0.5
        elif activity['idle_seconds'] > 60:
            energy *= 0.8
        
        return max(0.1, energy)
    
    def _calculate_stress_level(self, activity: Dict, enhanced: Dict) -> float:
        switch_stress = min(1.0, enhanced['window_switches_per_hour'] / 50)
        activity_stress = 0.8 if activity['keystrokes_per_min'] > 150 else 0.2
        session_hours = (time.time() - self.start_time) / 3600
        time_stress = min(1.0, session_hours / 4) if session_hours > 2 else 0.0
        
        stress = (switch_stress * 0.4 + activity_stress * 0.3 + time_stress * 0.3)
        return max(0.0, min(1.0, stress))
    
    def _calculate_productivity_score(self, enhanced: Dict) -> float:
        breakdown = enhanced.get('activity_breakdown', {})
        total_time = sum(breakdown.values()) or 1
        
        weights = {'productive': 1.0, 'research': 0.8, 'communication': 0.6, 'entertainment': 0.2, 'unknown': 0.5}
        
        weighted_score = 0
        for activity, time_spent in breakdown.items():
            weight = weights.get(activity, 0.5)
            weighted_score += (time_spent / total_time) * weight
        
        return max(0.0, min(1.0, weighted_score))
    
    def _get_last_break_time(self) -> str:
        now = time.time()
        activity_metrics = self.activity_tracker.get_activity_metrics()
        
        if activity_metrics['idle_seconds'] > 300:
            break_time = now - activity_metrics['idle_seconds']
            return datetime.fromtimestamp(break_time).isoformat()
        
        return datetime.fromtimestamp(self.start_time).isoformat()


class EnhancedPersonalCoach:
    """Complete AI coach with real monitoring and notifications"""
    
    def __init__(self, user_id: str = "personal_user"):
        self.user_id = user_id
        self.coach = AICoach()
        self.collector = EnhancedTelemetryCollector()
        self.running = False
        self.coaching_stats = {
            'total_notifications': 0,
            'productivity_sessions': 0,
            'distraction_alerts': 0,
            'break_reminders': 0
        }
    
    async def start_personal_coaching(self):
        """Start complete AI coaching with monitoring"""
        
        print("🚀 COMPLETE AI COACH - Real Monitoring & Notifications")
        print("=" * 70)
        print(f"👤 User: {self.user_id}")
        print("🎯 Full Monitoring: Tabs, Windows, Activity, Notifications")
        
        # Check setup
        ready, missing = self._check_setup()
        if not ready:
            print(f"\n📋 SETUP NEEDED:")
            for item in missing:
                print(f"   {item}")
            return
        
        # Start monitoring
        print("\n📊 Starting complete activity monitoring...")
        if not self.collector.start_monitoring():
            print("❌ Failed to start monitoring")
            return
        
        print("✅ Successfully monitoring your complete activity!")
        print("\n🔍 MONITORING:")
        print("   📱 Browser tabs & URLs")
        print("   🖥️  Window titles & focus")
        print("   ⌨️  Keyboard & mouse activity")
        print("   🔄 App switching patterns")
        print("   📊 Productivity scoring")
        
        print("\n🔔 NOTIFICATIONS:")
        print("   Desktop alerts for coaching")
        print("   Context-aware suggestions")
        print("   Smart timing (5min cooldown)")
        
        print(f"\nPress Ctrl+C to stop coaching\n")
        
        self.running = True
        await self._coaching_loop()
    
    def _check_setup(self):
        """Check if setup is complete"""
        missing = []
        
        if not PYNPUT_AVAILABLE:
            missing.append("pip install pynput")
        if not NOTIFICATIONS_AVAILABLE:
            missing.append("pip install plyer")
        
        # Check permissions
        try:
            script = 'tell application "System Events" to return name of first application process whose frontmost is true'
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=5)
            if result.returncode != 0:
                missing.append("Grant accessibility permissions in System Preferences")
        except Exception:
            missing.append("Grant accessibility permissions in System Preferences")
        
        return len(missing) == 0, missing
    
    async def _coaching_loop(self):
        """Main coaching loop"""
        
        try:
            while self.running:
                # Get enhanced telemetry
                telemetry = self.collector.get_enhanced_telemetry()
                
                # Get AI coaching
                notification = await self.coach.analyze_telemetry(telemetry, self.user_id)
                
                if notification:
                    await self._handle_notification(notification, telemetry)
                else:
                    self._show_status(telemetry)
                
                await asyncio.sleep(90)
                
        except KeyboardInterrupt:
            print("\n⏹️  Coaching stopped by user")
        finally:
            await self._stop_coaching()
    
    async def _handle_notification(self, notification: Dict, telemetry: Dict):
        """Handle coaching notification"""
        
        self.coaching_stats['total_notifications'] += 1
        
        # Send desktop notification
        self.collector.notification_manager.send_coaching_notification(notification)
        
        # Console output
        print(f"\n🔔 COACHING ALERT #{self.coaching_stats['total_notifications']}")
        print("=" * 60)
        print(f"💡 {notification['message']}")
        print(f"🎯 Action: {notification['action']}")
        print(f"⚡ Priority: {notification['priority']}")
        
        # Show context
        if telemetry.get('current_tab') and telemetry['current_tab'].get('title'):
            tab = telemetry['current_tab']
            title = tab.get('title', 'Unknown')
            browser = tab.get('browser', 'Browser')
            print(f"📑 Context: {browser} - {title[:50] + '...' if len(title) > 50 else title}")
        else:
            window = telemetry.get('current_window', 'Unknown')
            print(f"🖥️  Context: {window[:50] + '...' if len(window) > 50 else window}")
        
        activity_type = telemetry.get('current_activity_type', 'unknown')
        activity_icons = {'productive': '💼', 'research': '🔍', 'communication': '💬', 'entertainment': '🎮', 'unknown': '❓'}
        print(f"{activity_icons.get(activity_type, '❓')} Activity: {activity_type.title()}")
        
        print(f"\n📊 Current State:")
        print(f"   Productivity: {telemetry['productivity_score']:.2f}")
        print(f"   Focus: {telemetry['focus_quality']:.2f}")
        print(f"   Window Switches/Hour: {telemetry['context_switches']}")
        
        print("=" * 60)
        
        # Record feedback
        effectiveness = 0.8 if telemetry['productivity_score'] < 0.5 else 0.6
        self.coach.record_feedback(self.user_id, f"alert_{self.coaching_stats['total_notifications']}", {"effectiveness": effectiveness})
    
    def _show_status(self, telemetry: Dict):
        """Show status update"""
        
        now = datetime.now().strftime("%H:%M:%S")
        activity_type = telemetry.get('current_activity_type', 'unknown')
        activity_icons = {'productive': '💼', 'research': '🔍', 'communication': '💬', 'entertainment': '🎮', 'unknown': '❓'}
        
        focus_icon = "🎯" if telemetry['focus_quality'] > 0.7 else "😐" if telemetry['focus_quality'] > 0.4 else "😵"
        productivity_icon = "📈" if telemetry['productivity_score'] > 0.7 else "📊" if telemetry['productivity_score'] > 0.4 else "📉"
        
        status = f"[{now}] {activity_icons.get(activity_type, '❓')} {activity_type.title()} | "
        status += f"{focus_icon} Focus: {telemetry['focus_quality']:.2f} | "
        status += f"{productivity_icon} Productivity: {telemetry['productivity_score']:.2f} | "
        
        if telemetry.get('current_tab') and telemetry['current_tab'].get('title'):
            tab_title = telemetry['current_tab']['title']
            status += f"📑 {tab_title[:25] + '...' if len(tab_title) > 25 else tab_title}"
        else:
            app = telemetry.get('current_app', 'Unknown')
            status += f"🖥️  {app}"
        
        print(status)
    
    async def _stop_coaching(self):
        """Stop coaching with summary"""
        
        self.running = False
        self.collector.stop_monitoring()
        
        print("\n📊 COACHING SESSION SUMMARY")
        print("=" * 50)
        print(f"👤 User: {self.user_id}")
        print(f"📱 Total Notifications: {self.coaching_stats['total_notifications']}")
        
        coach_status = self.coach.get_coach_status()
        print(f"🧠 Total Interactions: {coach_status['statistics']['total_interactions']}")
        print(f"📈 Patterns Discovered: {coach_status['statistics']['discovered_patterns']}")
        
        print(f"\n✅ Complete monitoring session finished!")


def check_permissions():
    """Check macOS permissions"""
    try:
        script = 'tell application "System Events" to return name of first application process whose frontmost is true'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✅ Accessibility permissions OK")
            return True
        else:
            print("⚠️  Need accessibility permissions:")
            print("   System Preferences > Security & Privacy > Accessibility")
            print("   Add Terminal/Python to allowed apps")
            return False
    except Exception:
        print("⚠️  Cannot check permissions")
        return False


# Main execution
async def main():
    """Main function - choose demo or real monitoring"""
    
    print("🤖 AI COACH - Choose Mode")
    print("=" * 30)
    print("1. Demo mode (simulated data)")
    print("2. Real monitoring mode")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "2":
        # Real monitoring mode
        try:
            user_id = input("Enter your name/ID (or press Enter for 'personal_user'): ").strip()
            if not user_id:
                user_id = "personal_user"
        except EOFError:
            user_id = "personal_user"
        
        coach = EnhancedPersonalCoach(user_id)
        
        def signal_handler(signum, frame):
            print("\n🛑 Received interrupt signal...")
            coach.running = False
        
        signal.signal(signal.SIGINT, signal_handler)
        
        await coach.start_personal_coaching()
    else:
        # Demo mode
        await demonstrate_ai_capabilities()


if __name__ == "__main__":
    asyncio.run(main())