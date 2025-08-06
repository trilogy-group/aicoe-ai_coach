#!/usr/bin/env python3
"""
AI Coach - Enhanced with True AI Capabilities
============================================

This version adds genuine AI characteristics:
- Learning from user feedback
- Pattern discovery from data
- Predictive modeling
- Adaptive personalization
- Continuous improvement
"""

import asyncio
import json
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
import pickle
from collections import defaultdict
# Note: Using simple implementations instead of sklearn for no dependencies
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler
import logging

logger = logging.getLogger(__name__)

class UserModel:
    """Learns and models individual user patterns"""
    
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

class SimpleClassifier:
    """Simple decision tree classifier without sklearn"""
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
                # Importance based on std deviation (more variance = more important)
                importances.append(self.feature_stats[i]['std_effective'])
            else:
                importances.append(0.0)
        return importances

class SimpleScaler:
    """Simple standard scaler without sklearn"""
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

class PatternLearner:
    """Discovers patterns in coaching effectiveness"""
    
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
            
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train classifier
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
            
            # Calculate mean values for effective interventions
            mean_effective = np.mean(effective_features, axis=0)
            
            patterns = []
            feature_names = ['energy', 'stress', 'productivity', 'focus', 'time_since_break', 
                           'hour_of_day', 'context_switches', 'cognitive_load']
            
            for i, (feature_name, mean_val) in enumerate(zip(feature_names, mean_effective)):
                if self.feature_importance.get(feature_name, 0) > 0.1:  # Important feature
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
    """Predicts future user states and needs"""
    
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
        if energy_trend < -0.05:  # Declining
            burnout_risk += 0.3
        if stress_trend > 0.05:  # Increasing
            burnout_risk += 0.4
        if productivity_trend < -0.05:  # Declining
            burnout_risk += 0.3
        
        return min(1.0, burnout_risk)
    
    def predict_optimal_break_time(self, user_id: str) -> Optional[int]:
        """Predict when user will need a break"""
        if user_id not in self.time_series_data or len(self.time_series_data[user_id]) < 5:
            return None
        
        recent_data = self.time_series_data[user_id][-5:]
        
        # Simple prediction based on energy decline rate
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

class AICoachEnhanced:
    """AI Coach with genuine learning and adaptation capabilities"""
    
    def __init__(self, model_path: Optional[str] = None):
        self.user_models = {}
        self.pattern_learner = PatternLearner()
        self.predictive_engine = PredictiveEngine()
        self.global_interaction_history = []
        self.model_path = model_path or "ai_coach_model.pkl"
        
        # Load existing model if available
        self._load_model()
        
        # Original components
        from ai_coach import ContextEngine, CoachingStrategy, NotificationManager
        self.context_engine = ContextEngine()
        self.coaching_strategy = CoachingStrategy()
        self.notification_manager = NotificationManager()
        
        logger.info("AI Coach Enhanced initialized with learning capabilities")
    
    def _get_user_model(self, user_id: str) -> UserModel:
        """Get or create user model"""
        if user_id not in self.user_models:
            self.user_models[user_id] = UserModel(user_id)
        return self.user_models[user_id]
    
    async def analyze_telemetry(self, telemetry: Dict[str, Any], 
                               user_id: str = 'default') -> Optional[Dict]:
        """Enhanced analysis with AI capabilities"""
        try:
            # Get user model
            user_model = self._get_user_model(user_id)
            
            # Analyze context
            context = self.context_engine.analyze_context(telemetry)
            
            # Update predictive engine
            self.predictive_engine.update_time_series(user_id, context)
            
            # Check for predictive interventions
            burnout_risk = self.predictive_engine.predict_burnout_risk(user_id)
            if burnout_risk > 0.7:
                return self._create_predictive_notification(
                    "I'm noticing signs of potential burnout. Let's take a proper break.",
                    'burnout_prevention',
                    context,
                    priority=3
                )
            
            # Predict effectiveness of potential interventions
            if self.pattern_learner.is_trained:
                effectiveness = self.pattern_learner.predict_effectiveness(context)
                if effectiveness < 0.3:
                    # Low predicted effectiveness - try different approach
                    context['force_alternative'] = True
            
            # Get personalized recommendation
            base_strategy = self.coaching_strategy.select_strategy(context)
            
            if base_strategy:
                # Personalize based on user model
                action = base_strategy['action']
                personalization_score = user_model.get_personalized_recommendation(action)
                
                # Adjust strategy based on personalization
                if personalization_score < 0.3:
                    # This strategy hasn't worked well for this user
                    # Try alternative
                    base_strategy = self._get_alternative_strategy(context, exclude=action)
                
                if base_strategy and self.notification_manager.should_notify(user_id, base_strategy['priority']):
                    # Predict optimal timing
                    optimal_break = self.predictive_engine.predict_optimal_break_time(user_id)
                    if optimal_break and 'duration' in base_strategy:
                        base_strategy['duration'] = optimal_break
                    
                    # Create notification with AI enhancements
                    notification = self._create_enhanced_notification(base_strategy, context, user_model)
                    
                    # Record interaction
                    user_model.update_from_interaction(context, base_strategy['action'])
                    self.global_interaction_history.append({
                        'user_id': user_id,
                        'timestamp': datetime.now(),
                        'context': context,
                        'action': base_strategy['action']
                    })
                    
                    # Retrain if enough data
                    if len(self.global_interaction_history) % 50 == 0:
                        self.pattern_learner.learn_from_data(self.global_interaction_history)
                    
                    self.notification_manager.record_notification(user_id)
                    return notification
            
            return None
            
        except Exception as e:
            logger.error(f"Error in enhanced analysis: {str(e)}")
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
        # Temporarily modify context to force different selection
        modified_context = context.copy()
        modified_context['excluded_action'] = exclude
        
        # This is simplified - in reality would need more sophisticated selection
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
        """Record user feedback for learning"""
        user_model = self._get_user_model(user_id)
        
        # Find the interaction
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
        """Save learned models"""
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
        """Load previously learned models"""
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

# Example usage showing AI capabilities
async def demo_ai_capabilities():
    """Demonstrate true AI capabilities"""
    coach = AICoachEnhanced()
    
    print("AI COACH ENHANCED - Demonstrating True AI")
    print("=" * 50)
    
    # Simulate user interactions over time
    user_id = "ai_test_user"
    
    # Simulate declining performance pattern
    for hour in range(5):
        telemetry = {
            'last_break_time': (datetime.now() - timedelta(hours=hour)).isoformat(),
            'keystrokes_per_min': 70 - (hour * 10),
            'error_rate': 0.02 * (hour + 1),
            'stress_level': 0.3 + (hour * 0.15),
            'energy_level': 0.8 - (hour * 0.15),
            'app_switches_per_hour': 20 + (hour * 5)
        }
        
        notification = await coach.analyze_telemetry(telemetry, user_id)
        
        if notification:
            print(f"\nHour {hour + 1}:")
            print(f"Message: {notification['message']}")
            if 'ai_predicted' in notification:
                print("🤖 AI PREDICTED this intervention!")
            if 'ai_insights' in notification:
                insights = notification['ai_insights']
                if insights.get('personalization_score') is not None:
                    print(f"Personalization Score: {insights['personalization_score']:.2f}")
                if insights.get('predicted_effectiveness') is not None:
                    print(f"Predicted Effectiveness: {insights['predicted_effectiveness']:.2f}")
                if insights.get('next_state_prediction'):
                    print(f"Next State Prediction: {insights['next_state_prediction']}")
            
            # Simulate feedback
            effectiveness = 0.8 if 'break' in notification['message'] else 0.4
            coach.record_feedback(user_id, f"notif_{hour}", {'effectiveness': effectiveness})
    
    print("\n" + "=" * 50)
    print("AI Learning Results:")
    print(f"- Trained on {len(coach.global_interaction_history)} interactions")
    print(f"- Discovered {len(coach.pattern_learner.discovered_patterns)} patterns")
    print(f"- User models: {len(coach.user_models)}")
    
    if coach.pattern_learner.feature_importance:
        print("\nFeature Importance (what the AI learned matters most):")
        for feature, importance in sorted(coach.pattern_learner.feature_importance.items(), 
                                        key=lambda x: x[1], reverse=True)[:3]:
            print(f"  - {feature}: {importance:.3f}")

if __name__ == "__main__":
    asyncio.run(demo_ai_capabilities())