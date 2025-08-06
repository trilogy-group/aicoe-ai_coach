#!/usr/bin/env python3
"""
Performance Comparison System
============================

Comprehensive testing framework to compare evolved AI coaches against baseline.
Measures coaching effectiveness, user engagement, and behavioral impact.
"""

import asyncio
import json
import logging
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
import pandas as pd
import numpy as np
from pathlib import Path
import importlib.util
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CoachPerformanceEvaluator:
    """Evaluates and compares coaching system performance"""
    
    def __init__(self):
        self.test_scenarios = self._load_test_scenarios()
        self.evaluation_metrics = {
            'relevance_score': 0.0,
            'user_engagement': 0.0,
            'actionability': 0.0,
            'personalization': 0.0,
            'response_time': 0.0,
            'overall_effectiveness': 0.0
        }
        self.results_history = []
    
    def _load_test_scenarios(self) -> List[Dict]:
        """Load comprehensive test scenarios for evaluation"""
        return [
            {
                'scenario_id': 'high_stress_afternoon',
                'name': 'High Stress Afternoon Work',
                'user_context': {
                    'user_id': 'test_user_1',
                    'state': {
                        'energy_level': 'low',
                        'stress_level': 'high',
                        'focus_level': 'poor'
                    },
                    'environment': {
                        'location': 'office',
                        'noise_level': 'high',
                        'time_of_day': 14
                    },
                    'recent_activities': ['back_to_back_meetings', 'urgent_emails'],
                    'work_duration': '4 hours',
                    'focus_mins': 15
                },
                'expected_categories': ['wellbeing', 'focus'],
                'success_criteria': {
                    'mentions_break': True,
                    'addresses_stress': True,
                    'actionable_advice': True,
                    'short_message': True  # < 100 chars for high stress
                }
            },
            {
                'scenario_id': 'morning_productivity',
                'name': 'Morning High Energy Productivity',
                'user_context': {
                    'user_id': 'test_user_2',
                    'state': {
                        'energy_level': 'high',
                        'stress_level': 'low',
                        'focus_level': 'excellent'
                    },
                    'environment': {
                        'location': 'home',
                        'noise_level': 'low',
                        'time_of_day': 9
                    },
                    'recent_activities': ['morning_routine', 'goal_setting'],
                    'work_duration': '30 minutes',
                    'focus_mins': 25,
                    'task_type': 'coding',
                    'peak_time': 'morning'
                },
                'expected_categories': ['productivity', 'focus'],
                'success_criteria': {
                    'encourages_momentum': True,
                    'suggests_challenging_tasks': True,
                    'mentions_peak_time': True,
                    'detailed_guidance': True
                }
            },
            {
                'scenario_id': 'context_switching',
                'name': 'Frequent Context Switching',
                'user_context': {
                    'user_id': 'test_user_3',
                    'state': {
                        'energy_level': 'medium',
                        'stress_level': 'medium',
                        'focus_level': 'fragmented'
                    },
                    'environment': {
                        'location': 'office',
                        'noise_level': 'medium',
                        'time_of_day': 11
                    },
                    'recent_activities': ['email', 'slack', 'coding', 'meeting', 'email'],
                    'work_duration': '2 hours',
                    'focus_mins': 8,
                    'interruptions': 5
                },
                'expected_categories': ['focus', 'productivity'],
                'success_criteria': {
                    'addresses_fragmentation': True,
                    'suggests_deep_work': True,
                    'mentions_distractions': True,
                    'provides_structure': True
                }
            },
            {
                'scenario_id': 'end_of_day_fatigue',
                'name': 'End of Day Fatigue',
                'user_context': {
                    'user_id': 'test_user_4',
                    'state': {
                        'energy_level': 'very_low',
                        'stress_level': 'medium',
                        'focus_level': 'poor'
                    },
                    'environment': {
                        'location': 'office',
                        'noise_level': 'low',
                        'time_of_day': 17
                    },
                    'recent_activities': ['long_coding_session', 'debugging'],
                    'work_duration': '7 hours',
                    'focus_mins': 120,
                    'energy': 'depleted'
                },
                'expected_categories': ['wellbeing', 'motivation'],
                'success_criteria': {
                    'acknowledges_fatigue': True,
                    'suggests_rest': True,
                    'positive_reinforcement': True,
                    'gentle_tone': True
                }
            },
            {
                'scenario_id': 'learning_mode',
                'name': 'Learning New Technology',
                'user_context': {
                    'user_id': 'test_user_5',
                    'state': {
                        'energy_level': 'medium',
                        'stress_level': 'low',
                        'focus_level': 'good'
                    },
                    'environment': {
                        'location': 'home',
                        'noise_level': 'low',
                        'time_of_day': 10
                    },
                    'recent_activities': ['reading_docs', 'tutorial', 'experimentation'],
                    'work_duration': '1 hour',
                    'task_type': 'learning',
                    'complexity': 'high'
                },
                'expected_categories': ['productivity', 'motivation'],
                'success_criteria': {
                    'supports_learning': True,
                    'suggests_breaks': True,
                    'encourages_practice': True,
                    'mentions_progress': True
                }
            }
        ]
    
    async def evaluate_coach(self, coach_instance, coach_name: str) -> Dict[str, Any]:
        """Evaluate a coaching system across all test scenarios"""
        logger.info(f"Evaluating coach: {coach_name}")
        
        results = {
            'coach_name': coach_name,
            'timestamp': datetime.now().isoformat(),
            'scenario_results': [],
            'overall_metrics': {},
            'performance_summary': {}
        }
        
        total_scores = {metric: 0.0 for metric in self.evaluation_metrics.keys()}
        total_response_time = 0.0
        
        for scenario in self.test_scenarios:
            logger.info(f"Testing scenario: {scenario['name']}")
            
            start_time = time.time()
            
            try:
                # Get coaching response - try multiple interface patterns
                coaching_message = ""
                category = 'unknown'
                
                if hasattr(coach_instance, 'coach_user'):
                    # Enhanced AI Coach interface
                    response = await coach_instance.coach_user(
                        scenario['user_context']['user_id'],
                        scenario['user_context']
                    )
                    coaching_message = response.get('coaching_message', '')
                    category = response.get('category', 'unknown')
                
                elif hasattr(coach_instance, 'update_user_context'):
                    # Evolved coach interface (rapid_variant_relevance)
                    coaching_message = await coach_instance.update_user_context(
                        scenario['user_context']['user_id'],
                        scenario['user_context']
                    )
                    category = 'contextual'
                
                elif hasattr(coach_instance, 'analyze_and_coach'):
                    # Original AI Coach interface
                    # Create a mock DataFrame with user context
                    import pandas as pd
                    mock_data = pd.DataFrame([{
                        'user_id': scenario['user_context']['user_id'],
                        'timestamp': datetime.now(),
                        'activity': 'work',
                        'duration': 30,
                        **scenario['user_context']
                    }])
                    
                    response = await coach_instance.analyze_and_coach(
                        mock_data, 
                        int(scenario['user_context']['user_id'].split('_')[-1]) if '_' in scenario['user_context']['user_id'] else 1
                    )
                    if response:
                        coaching_message = response.get('nudge', response.get('message', ''))
                        category = response.get('type', 'nudge')
                    else:
                        coaching_message = "No coaching generated"
                        category = 'none'
                
                elif hasattr(coach_instance, 'get_relevant_message'):
                    # Context-aware coach interface
                    coach_instance.update_context(scenario['user_context'])
                    coaching_message = coach_instance.get_relevant_message()
                    if not coaching_message:
                        coaching_message = "No relevant message found"
                    category = 'contextual'
                
                else:
                    # Try to find any coaching method
                    coaching_methods = [attr for attr in dir(coach_instance) 
                                     if 'coach' in attr.lower() and callable(getattr(coach_instance, attr))]
                    if coaching_methods:
                        coaching_message = f"Found methods: {', '.join(coaching_methods[:3])}"
                        category = 'method_discovery'
                    else:
                        coaching_message = "No compatible coaching interface found"
                        category = 'error'
                
                response_time = time.time() - start_time
                total_response_time += response_time
                
                # Evaluate the response
                scenario_scores = self._evaluate_response(
                    coaching_message, 
                    category,
                    scenario,
                    response_time
                )
                
                scenario_result = {
                    'scenario_id': scenario['scenario_id'],
                    'coaching_message': coaching_message,
                    'category': category,
                    'response_time': response_time,
                    'scores': scenario_scores
                }
                
                results['scenario_results'].append(scenario_result)
                
                # Accumulate scores
                for metric, score in scenario_scores.items():
                    total_scores[metric] += score
                
            except Exception as e:
                logger.error(f"Error evaluating scenario {scenario['scenario_id']}: {str(e)}")
                
                error_result = {
                    'scenario_id': scenario['scenario_id'],
                    'error': str(e),
                    'scores': {metric: 0.0 for metric in self.evaluation_metrics.keys()}
                }
                results['scenario_results'].append(error_result)
        
        # Calculate overall metrics
        num_scenarios = len(self.test_scenarios)
        results['overall_metrics'] = {
            metric: total_scores[metric] / num_scenarios 
            for metric in self.evaluation_metrics.keys()
        }
        results['overall_metrics']['avg_response_time'] = total_response_time / num_scenarios
        
        # Performance summary
        overall_score = sum(results['overall_metrics'][m] for m in self.evaluation_metrics.keys()) / len(self.evaluation_metrics)
        results['performance_summary'] = {
            'overall_effectiveness': overall_score,
            'response_time_grade': self._grade_response_time(results['overall_metrics']['avg_response_time']),
            'strengths': self._identify_strengths(results['overall_metrics']),
            'areas_for_improvement': self._identify_improvements(results['overall_metrics'])
        }
        
        self.results_history.append(results)
        return results
    
    def _evaluate_response(self, message: str, category: str, scenario: Dict, response_time: float) -> Dict[str, float]:
        """Evaluate a coaching response against scenario criteria"""
        scores = {}
        
        # Relevance Score (0-1)
        relevance = self._calculate_relevance(message, scenario)
        scores['relevance_score'] = relevance
        
        # User Engagement (0-1)
        engagement = self._calculate_engagement(message, scenario)
        scores['user_engagement'] = engagement
        
        # Actionability (0-1)
        actionability = self._calculate_actionability(message, scenario)
        scores['actionability'] = actionability
        
        # Personalization (0-1)
        personalization = self._calculate_personalization(message, scenario)
        scores['personalization'] = personalization
        
        # Response Time (0-1, where 1 is fastest)
        response_time_score = max(0.0, 1.0 - (response_time / 2.0))  # 2 seconds = 0 score
        scores['response_time'] = response_time_score
        
        # Overall Effectiveness (weighted average)
        weights = {
            'relevance_score': 0.3,
            'user_engagement': 0.25,
            'actionability': 0.25,
            'personalization': 0.15,
            'response_time': 0.05
        }
        
        overall = sum(scores[metric] * weights[metric] for metric in weights.keys())
        scores['overall_effectiveness'] = overall
        
        return scores
    
    def _calculate_relevance(self, message: str, scenario: Dict) -> float:
        """Calculate how relevant the message is to the scenario"""
        score = 0.0
        success_criteria = scenario['success_criteria']
        message_lower = message.lower()
        
        # Check specific success criteria
        criteria_met = 0
        total_criteria = len(success_criteria)
        
        for criterion, expected in success_criteria.items():
            if criterion == 'mentions_break' and expected:
                if any(word in message_lower for word in ['break', 'rest', 'pause', 'step away']):
                    criteria_met += 1
            elif criterion == 'addresses_stress' and expected:
                if any(word in message_lower for word in ['stress', 'calm', 'breathe', 'relax']):
                    criteria_met += 1
            elif criterion == 'actionable_advice' and expected:
                if any(word in message_lower for word in ['try', 'consider', 'do', 'take', 'set']):
                    criteria_met += 1
            elif criterion == 'short_message' and expected:
                if len(message) < 100:
                    criteria_met += 1
            elif criterion == 'encourages_momentum' and expected:
                if any(word in message_lower for word in ['momentum', 'keep', 'continue', 'great']):
                    criteria_met += 1
            elif criterion == 'suggests_challenging_tasks' and expected:
                if any(word in message_lower for word in ['challenge', 'important', 'priority', 'difficult']):
                    criteria_met += 1
            elif criterion == 'mentions_peak_time' and expected:
                if any(word in message_lower for word in ['morning', 'peak', 'best', 'optimal']):
                    criteria_met += 1
            elif criterion == 'addresses_fragmentation' and expected:
                if any(word in message_lower for word in ['focus', 'concentration', 'distraction', 'interruption']):
                    criteria_met += 1
            elif criterion == 'acknowledges_fatigue' and expected:
                if any(word in message_lower for word in ['tired', 'fatigue', 'energy', 'exhausted', 'long day']):
                    criteria_met += 1
            elif criterion == 'supports_learning' and expected:
                if any(word in message_lower for word in ['learn', 'practice', 'understand', 'master']):
                    criteria_met += 1
        
        score = criteria_met / total_criteria if total_criteria > 0 else 0.0
        return min(score, 1.0)
    
    def _calculate_engagement(self, message: str, scenario: Dict) -> float:
        """Calculate user engagement potential of the message"""
        score = 0.5  # Base score
        
        # Length appropriateness
        message_length = len(message)
        user_state = scenario['user_context']['state']
        
        if user_state.get('stress_level') == 'high' and message_length < 80:
            score += 0.2  # Short messages for high stress
        elif user_state.get('energy_level') == 'high' and 50 < message_length < 150:
            score += 0.2  # Moderate length for high energy
        
        # Personal pronouns (increases engagement)
        pronouns = ['you', 'your', 'you\'re', 'you\'ve']
        pronoun_count = sum(1 for pronoun in pronouns if pronoun in message.lower())
        score += min(pronoun_count * 0.1, 0.2)
        
        # Question marks (increases engagement)
        if '?' in message:
            score += 0.1
        
        # Positive language
        positive_words = ['great', 'good', 'excellent', 'well', 'success', 'achieve', 'progress']
        positive_count = sum(1 for word in positive_words if word in message.lower())
        score += min(positive_count * 0.05, 0.15)
        
        return min(score, 1.0)
    
    def _calculate_actionability(self, message: str, scenario: Dict) -> float:
        """Calculate how actionable the message is"""
        score = 0.0
        message_lower = message.lower()
        
        # Action verbs
        action_verbs = ['try', 'do', 'take', 'set', 'focus', 'break', 'consider', 'practice', 'use']
        action_count = sum(1 for verb in action_verbs if verb in message_lower)
        score += min(action_count * 0.15, 0.6)
        
        # Specific recommendations
        specific_words = ['minutes', 'pomodoro', 'technique', 'step', 'task', 'goal']
        specific_count = sum(1 for word in specific_words if word in message_lower)
        score += min(specific_count * 0.1, 0.3)
        
        # Time-based suggestions
        time_words = ['25 minutes', '5 minutes', 'short', 'brief', 'quick']
        if any(word in message_lower for word in time_words):
            score += 0.1
        
        return min(score, 1.0)
    
    def _calculate_personalization(self, message: str, scenario: Dict) -> float:
        """Calculate how personalized the message is to the user context"""
        score = 0.0
        message_lower = message.lower()
        context = scenario['user_context']
        
        # References user state
        state = context.get('state', {})
        if state.get('energy_level') == 'low' and any(word in message_lower for word in ['energy', 'tired', 'rest']):
            score += 0.2
        if state.get('stress_level') == 'high' and any(word in message_lower for word in ['stress', 'calm', 'breathe']):
            score += 0.2
        
        # References environment
        environment = context.get('environment', {})
        if environment.get('location') == 'home' and 'home' in message_lower:
            score += 0.1
        if environment.get('noise_level') == 'high' and any(word in message_lower for word in ['quiet', 'noise', 'distraction']):
            score += 0.1
        
        # References activities
        activities = context.get('recent_activities', [])
        activity_matches = sum(1 for activity in activities if activity.replace('_', ' ') in message_lower)
        score += min(activity_matches * 0.1, 0.2)
        
        # Uses specific context variables (for evolved coaches)
        context_vars = ['focus_mins', 'work_duration', 'task_type', 'peak_time']
        for var in context_vars:
            if var in context and str(context[var]) in message:
                score += 0.15
        
        return min(score, 1.0)
    
    def _grade_response_time(self, avg_time: float) -> str:
        """Grade response time performance"""
        if avg_time < 0.1:
            return 'A+'
        elif avg_time < 0.5:
            return 'A'
        elif avg_time < 1.0:
            return 'B'
        elif avg_time < 2.0:
            return 'C'
        else:
            return 'D'
    
    def _identify_strengths(self, metrics: Dict[str, float]) -> List[str]:
        """Identify coaching system strengths"""
        strengths = []
        if metrics['relevance_score'] > 0.8:
            strengths.append('Highly relevant messaging')
        if metrics['user_engagement'] > 0.7:
            strengths.append('Strong user engagement')
        if metrics['actionability'] > 0.7:
            strengths.append('Clear actionable advice')
        if metrics['personalization'] > 0.6:
            strengths.append('Good personalization')
        if metrics['response_time'] > 0.8:
            strengths.append('Fast response times')
        return strengths
    
    def _identify_improvements(self, metrics: Dict[str, float]) -> List[str]:
        """Identify areas for improvement"""
        improvements = []
        if metrics['relevance_score'] < 0.6:
            improvements.append('Improve message relevance to context')
        if metrics['user_engagement'] < 0.5:
            improvements.append('Enhance user engagement techniques')
        if metrics['actionability'] < 0.5:
            improvements.append('Provide more specific actionable advice')
        if metrics['personalization'] < 0.4:
            improvements.append('Increase personalization based on user context')
        if metrics['response_time'] < 0.5:
            improvements.append('Optimize response time performance')
        return improvements
    
    def compare_coaches(self, results_list: List[Dict]) -> Dict[str, Any]:
        """Compare multiple coaching systems and generate report"""
        if len(results_list) < 2:
            return {'error': 'Need at least 2 coaching systems to compare'}
        
        comparison = {
            'timestamp': datetime.now().isoformat(),
            'coaches_compared': [r['coach_name'] for r in results_list],
            'metric_comparison': {},
            'scenario_comparison': {},
            'winner_analysis': {},
            'improvement_recommendations': {}
        }
        
        # Compare overall metrics
        metrics = list(self.evaluation_metrics.keys())
        for metric in metrics:
            comparison['metric_comparison'][metric] = {
                coach['coach_name']: coach['overall_metrics'][metric]
                for coach in results_list
            }
        
        # Compare by scenario
        for scenario in self.test_scenarios:
            scenario_id = scenario['scenario_id']
            comparison['scenario_comparison'][scenario_id] = {}
            
            for coach in results_list:
                scenario_result = next(
                    (r for r in coach['scenario_results'] if r['scenario_id'] == scenario_id),
                    None
                )
                if scenario_result:
                    comparison['scenario_comparison'][scenario_id][coach['coach_name']] = {
                        'overall_score': scenario_result['scores']['overall_effectiveness'],
                        'message': scenario_result['coaching_message']
                    }
        
        # Winner analysis
        overall_scores = {
            coach['coach_name']: coach['overall_metrics']['overall_effectiveness']
            for coach in results_list
        }
        winner = max(overall_scores.keys(), key=lambda k: overall_scores[k])
        
        comparison['winner_analysis'] = {
            'overall_winner': winner,
            'winning_score': overall_scores[winner],
            'score_differences': {
                coach: overall_scores[winner] - score
                for coach, score in overall_scores.items()
                if coach != winner
            },
            'metric_winners': {
                metric: max(comparison['metric_comparison'][metric].keys(),
                           key=lambda k: comparison['metric_comparison'][metric][k])
                for metric in metrics
            }
        }
        
        return comparison

def load_coach_from_file(file_path: str, class_name: str):
    """Dynamically load a coach class from a Python file"""
    spec = importlib.util.spec_from_file_location("coach_module", file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["coach_module"] = module
    spec.loader.exec_module(module)
    return getattr(module, class_name)

async def main():
    """Main comparison runner"""
    evaluator = CoachPerformanceEvaluator()
    
    # Load coaches to compare
    coaches_to_test = [
        {
            'name': 'Original AI Coach',
            'file_path': 'ai_coach.py',
            'class_name': 'AICoach'
        },
        {
            'name': 'Enhanced AI Coach',
            'file_path': 'enhanced_ai_coach.py',
            'class_name': 'EnhancedAICoach'
        },
        {
            'name': 'Evolved Context-Aware Coach',
            'file_path': 'outputs/rapid_evolution/rapid_variant_relevance.py',
            'class_name': 'AICoach'
        }
    ]
    
    results = []
    
    for coach_info in coaches_to_test:
        try:
            # Load coach class
            CoachClass = load_coach_from_file(coach_info['file_path'], coach_info['class_name'])
            coach_instance = CoachClass()
            
            # Evaluate coach
            result = await evaluator.evaluate_coach(coach_instance, coach_info['name'])
            results.append(result)
            
            print(f"\n{'='*60}")
            print(f"RESULTS FOR: {coach_info['name']}")
            print(f"{'='*60}")
            print(f"Overall Effectiveness: {result['overall_metrics']['overall_effectiveness']:.3f}")
            print(f"Relevance Score: {result['overall_metrics']['relevance_score']:.3f}")
            print(f"User Engagement: {result['overall_metrics']['user_engagement']:.3f}")
            print(f"Actionability: {result['overall_metrics']['actionability']:.3f}")
            print(f"Personalization: {result['overall_metrics']['personalization']:.3f}")
            print(f"Avg Response Time: {result['overall_metrics']['avg_response_time']:.3f}s")
            print(f"Strengths: {', '.join(result['performance_summary']['strengths'])}")
            if result['performance_summary']['areas_for_improvement']:
                print(f"Improvements: {', '.join(result['performance_summary']['areas_for_improvement'])}")
            
        except Exception as e:
            logger.error(f"Failed to test {coach_info['name']}: {str(e)}")
    
    # Generate comparison report
    if len(results) >= 2:
        print(f"\n{'='*60}")
        print("COMPARISON ANALYSIS")
        print(f"{'='*60}")
        
        comparison = evaluator.compare_coaches(results)
        
        print(f"Overall Winner: {comparison['winner_analysis']['overall_winner']}")
        print(f"Winning Score: {comparison['winner_analysis']['winning_score']:.3f}")
        
        print("\nMetric Winners:")
        for metric, winner in comparison['winner_analysis']['metric_winners'].items():
            score = comparison['metric_comparison'][metric][winner]
            print(f"  {metric}: {winner} ({score:.3f})")
        
        print("\nScore Differences from Winner:")
        for coach, diff in comparison['winner_analysis']['score_differences'].items():
            print(f"  {coach}: -{diff:.3f}")
        
        # Save results
        results_file = Path('outputs/performance_comparison_results.json')
        results_file.parent.mkdir(exist_ok=True)
        
        full_results = {
            'individual_results': results,
            'comparison_analysis': comparison,
            'test_timestamp': datetime.now().isoformat()
        }
        
        with open(results_file, 'w') as f:
            json.dump(full_results, f, indent=2)
        
        print(f"\nDetailed results saved to: {results_file}")

if __name__ == "__main__":
    asyncio.run(main())