#!/usr/bin/env python3
"""
Advanced Training Data Generator
Focus: Generate massive datasets with realistic edge cases and incomplete scenarios
Goal: Train AI coach for maximum practical value delivery
"""

import asyncio
import pandas as pd
import numpy as np
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any
import base64
from pathlib import Path
from ai_coach import AICoach

class AdvancedTrainingDataGenerator:
    """Generate advanced training scenarios for maximum coaching value."""
    
    def __init__(self):
        self.output_dir = Path("outputs/advanced_training")
        self.output_dir.mkdir(exist_ok=True)
        
        # Advanced scenario patterns for realistic edge cases
        self.advanced_patterns = {
            'incomplete_screenshots': {
                'partial_code_editor': [
                    "VSCode with syntax errors visible but bottom panel cut off",
                    "Half-visible Excel formula with #REF! error",
                    "Browser with form validation errors partially hidden",
                    "Terminal with error message truncated",
                    "Slack message thread with context missing"
                ],
                'corrupted_data': [
                    "Screenshot with visual artifacts making text unreadable",
                    "Blurry screen capture during rapid task switching",
                    "Screen capture during loading states",
                    "Partial window captures missing critical context"
                ],
                'multi_monitor_fragments': [
                    "Primary monitor only - missing secondary context",
                    "Secondary monitor with main work happening off-screen",
                    "Split between monitors - incomplete workflow view"
                ]
            },
            
            'realistic_workflow_chaos': {
                'crisis_situations': [
                    {
                        'name': 'Production Down',
                        'characteristics': {
                            'tab_count_range': (15, 35),
                            'stress_multiplier': 3.0,
                            'error_rate_increase': 0.4,
                            'context_switching_rate': 5.0,
                            'time_pressure': 'extreme'
                        }
                    },
                    {
                        'name': 'Demo Day Preparation',
                        'characteristics': {
                            'tab_count_range': (12, 25),
                            'perfectionism_factor': 2.5,
                            'revision_cycles': 8,
                            'anxiety_level': 0.8
                        }
                    },
                    {
                        'name': 'Data Loss Recovery',
                        'characteristics': {
                            'panic_level': 0.9,
                            'file_recovery_attempts': 12,
                            'backup_search_duration': 45,
                            'emotional_state': 'desperate'
                        }
                    }
                ],
                
                'subtle_inefficiencies': [
                    {
                        'name': 'Copy-Paste Hell',
                        'pattern': 'Repetitive manual data entry that could be automated',
                        'time_waste_factor': 2.3,
                        'recognition_difficulty': 0.7
                    },
                    {
                        'name': 'Email Archaeology',
                        'pattern': 'Searching old emails for information that should be documented',
                        'time_waste_factor': 1.8,
                        'recognition_difficulty': 0.6
                    },
                    {
                        'name': 'Tab Hoarding Syndrome',
                        'pattern': 'Keeping 50+ tabs open "just in case"',
                        'cognitive_load_increase': 0.4,
                        'memory_impact': 0.6
                    }
                ]
            },
            
            'advanced_context_scenarios': {
                'domain_expertise_required': [
                    'Financial modeling with subtle formula errors',
                    'Code review with architectural implications',
                    'Legal document analysis with compliance gaps',
                    'Medical data analysis with statistical issues',
                    'Engineering calculations with unit conversion errors'
                ],
                
                'time_sensitive_decisions': [
                    'Sprint planning with unrealistic estimates',
                    'Budget allocation with missing dependencies',
                    'Hiring decisions with incomplete candidate assessment',
                    'Security incident response with incomplete information',
                    'Product launch with unresolved technical debt'
                ]
            }
        }
        
        # Enhanced personas with realistic variance
        self.personas_advanced = {
            'senior_developer': {
                'base_productivity': 0.85,
                'expertise_areas': ['architecture', 'performance', 'mentoring'],
                'common_inefficiencies': ['perfectionism', 'over_engineering'],
                'stress_triggers': ['technical_debt', 'unrealistic_deadlines'],
                'optimal_coaching_style': 'peer_consultation'
            },
            
            'junior_developer': {
                'base_productivity': 0.55,
                'learning_curve_factor': 2.5,
                'common_inefficiencies': ['tutorial_paralysis', 'context_switching'],
                'stress_triggers': ['imposter_syndrome', 'complex_tasks'],
                'optimal_coaching_style': 'supportive_guidance'
            },
            
            'data_scientist': {
                'base_productivity': 0.70,
                'exploration_factor': 3.0,
                'common_inefficiencies': ['analysis_paralysis', 'tool_switching'],
                'strength_areas': ['pattern_recognition', 'statistical_thinking'],
                'optimal_coaching_style': 'methodology_focused'
            },
            
            'product_manager': {
                'base_productivity': 0.60,
                'context_switching_rate': 4.0,
                'common_inefficiencies': ['meeting_overload', 'decision_paralysis'],
                'strength_areas': ['prioritization', 'stakeholder_management'],
                'optimal_coaching_style': 'strategic_guidance'
            },
            
            'customer_success': {
                'base_productivity': 0.75,
                'emotional_labor_factor': 1.8,
                'common_inefficiencies': ['over_customization', 'context_loss'],
                'strength_areas': ['relationship_building', 'problem_solving'],
                'optimal_coaching_style': 'efficiency_optimization'
            }
        }

    async def generate_massive_advanced_dataset(self, record_count: int = 500000) -> Dict:
        """Generate massive dataset with advanced patterns for intensive training."""
        
        print(f"🚀 GENERATING MASSIVE ADVANCED TRAINING DATASET")
        print(f"Target Records: {record_count:,}")
        print("=" * 60)
        
        batch_size = 10000
        total_batches = record_count // batch_size
        
        all_telemetry = []
        all_interactions = []
        
        for batch_num in range(total_batches):
            print(f"📊 Processing Batch {batch_num + 1}/{total_batches}")
            
            batch_telemetry = []
            batch_interactions = []
            
            for i in range(batch_size):
                # Generate advanced scenario
                scenario = self._generate_advanced_scenario()
                telemetry_record = self._create_advanced_telemetry_record(scenario, batch_num * batch_size + i)
                batch_telemetry.append(telemetry_record)
                
                # Generate corresponding coaching interaction with realistic edge cases
                if random.random() < 0.15:  # 15% get coaching
                    interaction = await self._generate_realistic_interaction(telemetry_record, scenario)
                    if interaction:
                        batch_interactions.append(interaction)
            
            all_telemetry.extend(batch_telemetry)
            all_interactions.extend(batch_interactions)
            
            # Save batch to prevent memory issues
            if batch_num % 5 == 0:  # Save every 5 batches
                self._save_batch_data(all_telemetry[-50000:], all_interactions[-7500:], batch_num)
        
        print(f"✅ Generated {len(all_telemetry):,} telemetry records")
        print(f"✅ Generated {len(all_interactions):,} coaching interactions")
        
        # Save final consolidated dataset
        final_data = {
            'generation_timestamp': datetime.now().isoformat(),
            'total_telemetry_records': len(all_telemetry),
            'total_interactions': len(all_interactions),
            'advanced_patterns_used': list(self.advanced_patterns.keys()),
            'persona_coverage': list(self.personas_advanced.keys()),
            'training_focus': 'maximum_coaching_value_optimization'
        }
        
        # Save data
        pd.DataFrame(all_telemetry).to_csv(
            self.output_dir / "massive_advanced_telemetry.csv", 
            index=False
        )
        
        with open(self.output_dir / "massive_advanced_interactions.jsonl", "w") as f:
            for interaction in all_interactions:
                f.write(json.dumps(interaction) + "\n")
        
        with open(self.output_dir / "massive_advanced_summary.json", "w") as f:
            json.dump(final_data, f, indent=2)
        
        return final_data

    def _generate_advanced_scenario(self) -> Dict:
        """Generate realistic advanced scenario with edge cases."""
        
        scenario_type = random.choice([
            'incomplete_screenshot',
            'crisis_situation', 
            'subtle_inefficiency',
            'domain_expertise_required',
            'time_sensitive_decision',
            'normal_with_hidden_issues'
        ])
        
        persona = random.choice(list(self.personas_advanced.keys()))
        persona_config = self.personas_advanced[persona]
        
        base_scenario = {
            'scenario_type': scenario_type,
            'persona': persona,
            'persona_config': persona_config,
            'complexity_level': random.uniform(0.3, 0.95),
            'has_edge_case': random.random() < 0.4,
            'incomplete_information': random.random() < 0.3
        }
        
        # Add scenario-specific details
        if scenario_type == 'incomplete_screenshot':
            pattern = random.choice(self.advanced_patterns['incomplete_screenshots']['partial_code_editor'])
            base_scenario.update({
                'visual_pattern': pattern,
                'information_loss_factor': random.uniform(0.2, 0.8),
                'context_inference_required': True
            })
            
        elif scenario_type == 'crisis_situation':
            crisis = random.choice(self.advanced_patterns['realistic_workflow_chaos']['crisis_situations'])
            base_scenario.update({
                'crisis_type': crisis['name'],
                'crisis_characteristics': crisis['characteristics'],
                'time_pressure_multiplier': random.uniform(2.0, 4.0)
            })
            
        elif scenario_type == 'subtle_inefficiency':
            inefficiency = random.choice(self.advanced_patterns['realistic_workflow_chaos']['subtle_inefficiencies'])
            base_scenario.update({
                'inefficiency_pattern': inefficiency,
                'visibility_challenge': True,
                'potential_automation': random.random() < 0.6
            })
        
        return base_scenario

    def _create_advanced_telemetry_record(self, scenario: Dict, record_id: int) -> Dict:
        """Create realistic telemetry record based on advanced scenario."""
        
        base_time = datetime.now() - timedelta(days=random.randint(0, 30))
        persona_config = scenario['persona_config']
        
        # Base metrics influenced by persona and scenario
        base_productivity = persona_config['base_productivity']
        
        # Apply scenario modifications
        if scenario['scenario_type'] == 'crisis_situation':
            stress_factor = scenario.get('crisis_characteristics', {}).get('stress_multiplier', 1.0)
            cognitive_load = min(0.95, 0.7 + stress_factor * 0.1)
            tab_count_range = scenario.get('crisis_characteristics', {}).get('tab_count_range', (8, 15))
            tab_count = random.randint(*tab_count_range)
            productivity_modifier = -0.3  # Crisis reduces initial productivity
        else:
            cognitive_load = random.uniform(0.3, 0.8)
            tab_count = random.randint(3, 15)
            productivity_modifier = 0
        
        record = {
            'timestamp': base_time.isoformat(),
            'user_id': record_id % 1000 + 1000,  # Spread across 1000 users
            'persona_type': scenario['persona'],
            'scenario_type': scenario['scenario_type'],
            
            # Core metrics
            'productivity_score': max(0.1, min(0.95, base_productivity + productivity_modifier + random.uniform(-0.2, 0.2))),
            'cognitive_load_score': cognitive_load,
            'tab_count': tab_count,
            'focus_session_duration': random.randint(10, 180),
            'interruption_count': random.randint(0, 15),
            'current_hour': base_time.hour,
            
            # Advanced context
            'app_active': self._get_realistic_app(scenario['persona']),
            'task_category': self._get_realistic_task_category(scenario['persona']),
            'window_switches_15min': random.randint(2, 35),
            'keystrokes_per_min': random.randint(20, 120),
            'core_work_percentage': random.uniform(0.15, 0.85),
            
            # Scenario-specific inefficiencies
            'workflow_inefficiencies': self._generate_realistic_inefficiencies(scenario),
            
            # Visual analysis (including incomplete scenarios)
            'visual_analysis_available': random.random() < 0.7,  # 30% incomplete
            'screenshot_quality': random.choice(['full', 'partial', 'corrupted', 'loading']),
            
            # Advanced patterns
            'domain_complexity': scenario.get('complexity_level', 0.5),
            'time_pressure': scenario.get('time_pressure_multiplier', 1.0),
            'information_completeness': 1.0 - scenario.get('information_loss_factor', 0.0),
            
            # Task completion indicators with realistic variation
            'task_completion_indicators': self._generate_realistic_completion_indicators(scenario),
            
            # Flags for coaching triggers
            'flags': self._generate_realistic_flags(scenario, cognitive_load, tab_count)
        }
        
        return record

    def _generate_realistic_inefficiencies(self, scenario: Dict) -> List[Dict]:
        """Generate realistic workflow inefficiencies based on scenario."""
        
        inefficiencies = []
        persona = scenario['persona']
        scenario_type = scenario['scenario_type']
        
        # Persona-specific common inefficiencies
        persona_config = scenario['persona_config']
        common_issues = persona_config.get('common_inefficiencies', [])
        
        for issue in common_issues:
            if random.random() < 0.3:  # 30% chance each common issue appears
                inefficiencies.append({
                    'type': issue,
                    'severity': random.uniform(0.2, 0.8),
                    'time_waste_minutes': random.randint(5, 45),
                    'persona_specific': True,
                    'description': f"{persona} experiencing {issue}"
                })
        
        # Scenario-specific inefficiencies
        if scenario_type == 'crisis_situation':
            if random.random() < 0.8:
                inefficiencies.append({
                    'type': 'panic_multitasking',
                    'severity': 0.9,
                    'time_waste_minutes': random.randint(30, 90),
                    'crisis_induced': True,
                    'description': 'High-stress situation causing inefficient task juggling'
                })
        
        elif scenario_type == 'subtle_inefficiency':
            pattern = scenario.get('inefficiency_pattern', {})
            inefficiencies.append({
                'type': pattern.get('name', 'unknown_inefficiency'),
                'severity': 0.6,
                'time_waste_minutes': int(random.uniform(10, 60) * pattern.get('time_waste_factor', 1.0)),
                'subtle': True,
                'recognition_difficulty': pattern.get('recognition_difficulty', 0.5),
                'description': pattern.get('pattern', 'Subtle workflow inefficiency detected')
            })
        
        # Add random realistic inefficiencies
        possible_issues = [
            'excessive_context_switching', 'manual_repetitive_work', 'poor_tool_usage',
            'disorganized_workspace', 'notification_overload', 'perfectionism_paralysis'
        ]
        
        for issue in random.sample(possible_issues, random.randint(0, 2)):
            inefficiencies.append({
                'type': issue,
                'severity': random.uniform(0.3, 0.7),
                'time_waste_minutes': random.randint(5, 30),
                'common_pattern': True,
                'description': f"Common inefficiency: {issue}"
            })
        
        return inefficiencies

    def _generate_realistic_completion_indicators(self, scenario: Dict) -> Dict:
        """Generate realistic task completion indicators."""
        
        base_progress = random.uniform(0.2, 0.9)
        persona_config = scenario['persona_config']
        
        # Adjust based on scenario type
        if scenario['scenario_type'] == 'crisis_situation':
            # Crisis situations often have lower initial progress but high urgency
            progress_modifier = -0.2
            quality_impact = -0.3
        elif scenario['scenario_type'] == 'domain_expertise_required':
            # Domain expertise tasks may have slower progress but higher quality
            progress_modifier = -0.1
            quality_impact = 0.2
        else:
            progress_modifier = 0
            quality_impact = 0
        
        final_progress = max(0.1, min(0.95, base_progress + progress_modifier))
        
        indicators = {
            'task_progress_percentage': final_progress,
            'estimated_completion_hours': random.uniform(0.5, 8.0),
            'quality_indicators': {
                'error_rate': max(0.01, random.uniform(0.02, 0.15) - quality_impact),
                'review_needed': random.random() < 0.4,
                'best_practices_followed': min(0.95, random.uniform(0.6, 0.9) + quality_impact)
            },
            'blockers_detected': self._generate_realistic_blockers(scenario),
            'dependencies_status': random.choice(['clear', 'waiting', 'blocked', 'unknown'])
        }
        
        return indicators

    def _generate_realistic_blockers(self, scenario: Dict) -> List[Dict]:
        """Generate realistic project blockers."""
        
        blockers = []
        
        # Scenario-specific blockers
        if scenario['scenario_type'] == 'crisis_situation':
            crisis_blockers = [
                {'type': 'system_outage', 'severity': 'critical'},
                {'type': 'data_corruption', 'severity': 'high'},
                {'type': 'access_denied', 'severity': 'medium'}
            ]
            blockers.extend(random.sample(crisis_blockers, random.randint(1, 2)))
        
        # Persona-specific blockers
        persona = scenario['persona']
        if persona == 'junior_developer':
            if random.random() < 0.4:
                blockers.append({
                    'type': 'knowledge_gap',
                    'severity': 'medium',
                    'description': 'Needs guidance on technical approach'
                })
        
        elif persona == 'product_manager':
            if random.random() < 0.3:
                blockers.append({
                    'type': 'stakeholder_approval',
                    'severity': 'high',
                    'description': 'Waiting for executive decision'
                })
        
        # Common blockers
        common_blockers = [
            {'type': 'external_dependency', 'severity': 'medium'},
            {'type': 'resource_constraint', 'severity': 'low'},
            {'type': 'unclear_requirements', 'severity': 'medium'}
        ]
        
        if random.random() < 0.25:  # 25% chance of common blocker
            blockers.append(random.choice(common_blockers))
        
        return blockers

    def _generate_realistic_flags(self, scenario: Dict, cognitive_load: float, tab_count: int) -> List[str]:
        """Generate realistic flags for coaching triggers."""
        
        flags = []
        
        # Cognitive load flags
        if cognitive_load > 0.8:
            flags.append('high_cognitive_load')
        if cognitive_load > 0.9:
            flags.append('burnout_risk')
        
        # Tab management flags
        if tab_count > 15:
            flags.append('tab_overload')
        if tab_count > 25:
            flags.append('severe_tab_chaos')
        
        # Scenario-specific flags
        if scenario['scenario_type'] == 'crisis_situation':
            flags.extend(['crisis_mode', 'high_stress', 'time_pressure'])
        
        if scenario['scenario_type'] == 'incomplete_screenshot':
            flags.extend(['incomplete_context', 'inference_needed'])
        
        if scenario.get('has_edge_case'):
            flags.append('edge_case_detected')
        
        # Persona-specific flags
        persona_config = scenario['persona_config']
        stress_triggers = persona_config.get('stress_triggers', [])
        for trigger in stress_triggers:
            if random.random() < 0.2:  # 20% chance each trigger is active
                flags.append(f'stress_trigger_{trigger}')
        
        return flags

    async def _generate_realistic_interaction(self, telemetry_record: Dict, scenario: Dict) -> Dict:
        """Generate realistic coaching interaction with proper value delivery."""
        
        # Create coach instance for realistic nudge generation
        coach = AICoach()
        
        try:
            # Create DataFrame from telemetry record
            df = pd.DataFrame([telemetry_record])
            
            # Get actual AI coach recommendation
            nudge = await coach.analyze_and_coach(df, telemetry_record['user_id'])
            
            if not nudge:
                return None
            
            # Generate realistic user response based on scenario and persona
            user_response = self._generate_realistic_user_response(nudge, scenario, telemetry_record)
            
            interaction = {
                'timestamp': telemetry_record['timestamp'],
                'user_id': telemetry_record['user_id'],
                'persona': telemetry_record['persona_type'],
                'scenario_context': {
                    'type': scenario['scenario_type'],
                    'complexity': scenario.get('complexity_level', 0.5),
                    'edge_case': scenario.get('has_edge_case', False)
                },
                'coaching_input': {
                    'trigger_dimension': nudge.get('trigger_dimension', 'unknown'),
                    'confidence_score': nudge.get('confidence', 0.0),
                    'nudge_type': nudge.get('nudge_type', 'general')
                },
                'ai_coach_nudge': {
                    'text': nudge['nudge_text'],
                    'type': nudge.get('nudge_type', 'general'),
                    'confidence': nudge.get('confidence', 0.0),
                    'reasoning': nudge.get('reasoning', 'Not provided')
                },
                'user_response': user_response,
                'interaction_outcome': self._determine_interaction_outcome(user_response, scenario),
                'value_delivered': self._assess_value_delivered(nudge, user_response, scenario),
                'learning_data': {
                    'scenario_handled_well': user_response['accepted'] and user_response['helpfulness_rating'] >= 0.7,
                    'edge_case_success': scenario.get('has_edge_case', False) and user_response['accepted'],
                    'coaching_precision': nudge.get('confidence', 0.0) * user_response['helpfulness_rating']
                }
            }
            
            return interaction
            
        except Exception as e:
            print(f"Error generating interaction: {str(e)}")
            return None

    def _generate_realistic_user_response(self, nudge: Dict, scenario: Dict, telemetry: Dict) -> Dict:
        """Generate realistic user response based on persona and scenario context."""
        
        persona = scenario['persona']
        persona_config = scenario['persona_config'] 
        scenario_type = scenario['scenario_type']
        
        # Base acceptance probability by persona
        base_acceptance = {
            'senior_developer': 0.85,
            'junior_developer': 0.90, 
            'data_scientist': 0.75,
            'product_manager': 0.70,
            'customer_success': 0.80
        }.get(persona, 0.75)
        
        # Scenario modifiers
        scenario_modifiers = {
            'crisis_situation': -0.2,  # Less likely to accept during crisis
            'incomplete_screenshot': -0.1,  # Slight hesitation with incomplete info
            'subtle_inefficiency': 0.1,  # More appreciative of catching subtle issues
            'domain_expertise_required': -0.05,  # Slight skepticism for complex domain issues
            'time_sensitive_decision': -0.15  # Time pressure reduces acceptance
        }
        
        acceptance_prob = base_acceptance + scenario_modifiers.get(scenario_type, 0)
        
        # Nudge quality impact
        confidence = nudge.get('confidence', 0.5)
        acceptance_prob += (confidence - 0.5) * 0.3  # High confidence nudges more likely accepted
        
        # Edge case handling
        if scenario.get('has_edge_case', False):
            acceptance_prob -= 0.1  # Edge cases are harder
        
        accepted = random.random() < max(0.1, min(0.95, acceptance_prob))
        
        if accepted:
            helpfulness_rating = random.uniform(0.6, 0.95)  # Accepted nudges generally helpful
            time_saved_minutes = random.randint(5, 60)
            
            # Scenario-specific benefits
            if scenario_type == 'crisis_situation':
                time_saved_minutes *= 2  # Crisis coaching saves more time
            elif scenario_type == 'subtle_inefficiency':
                time_saved_minutes = random.randint(15, 90)  # Catching subtle issues saves lots of time
            
            feedback = random.choice([
                "This was exactly what I needed right now",
                "Good catch, didn't realize I was doing that",
                "Helpful timing on this suggestion",
                "This will definitely save me time",
                "Smart observation about my workflow"
            ])
        else:
            helpfulness_rating = random.uniform(0.1, 0.5)
            time_saved_minutes = 0
            
            feedback = random.choice([
                "Not relevant to my current situation",
                "Too generic, doesn't understand my context",
                "Wrong timing for this suggestion",
                "I'm already aware of this issue",
                "Doesn't account for my constraints"
            ])
        
        return {
            'accepted': accepted,
            'helpfulness_rating': helpfulness_rating,
            'time_saved_minutes': time_saved_minutes,
            'user_feedback': feedback,
            'response_time_seconds': random.randint(5, 30),
            'follow_up_action_taken': accepted and random.random() < 0.7
        }

    def _determine_interaction_outcome(self, user_response: Dict, scenario: Dict) -> Dict:
        """Determine the overall outcome of the coaching interaction."""
        
        if user_response['accepted']:
            outcome_type = 'successful_coaching'
            productivity_impact = user_response['time_saved_minutes'] / 60.0  # Convert to hours
            
            if scenario.get('has_edge_case', False) and user_response['helpfulness_rating'] > 0.8:
                outcome_type = 'excellent_edge_case_handling'
                productivity_impact *= 1.5  # Bonus for handling edge cases well
                
        else:
            outcome_type = 'coaching_rejected'
            productivity_impact = -0.1  # Small negative impact from interruption
        
        return {
            'outcome_type': outcome_type,
            'productivity_impact_hours': productivity_impact,
            'learning_value': user_response['helpfulness_rating'],
            'coaching_precision_score': user_response['helpfulness_rating'] if user_response['accepted'] else 0.0
        }

    def _assess_value_delivered(self, nudge: Dict, user_response: Dict, scenario: Dict) -> Dict:
        """Assess the actual value delivered by the coaching."""
        
        if not user_response['accepted']:
            return {
                'value_score': 0.1,
                'value_type': 'no_value',
                'specific_benefit': 'none',
                'measurable_impact': 0
            }
        
        # Calculate value based on multiple factors
        base_value = user_response['helpfulness_rating']
        time_value = min(1.0, user_response['time_saved_minutes'] / 60.0)  # Cap at 1 hour
        scenario_multiplier = {
            'crisis_situation': 2.0,  # Crisis coaching is extra valuable
            'subtle_inefficiency': 1.5,  # Catching subtle issues is valuable
            'domain_expertise_required': 1.3,  # Expert-level coaching is valuable
            'incomplete_screenshot': 1.2,  # Good inference is valuable
            'time_sensitive_decision': 1.4  # Timely advice is valuable
        }.get(scenario['scenario_type'], 1.0)
        
        value_score = (base_value * 0.6 + time_value * 0.4) * scenario_multiplier
        value_score = min(1.0, value_score)  # Cap at 1.0
        
        # Determine value type and specific benefit
        if value_score > 0.85:
            value_type = 'exceptional_value'
        elif value_score > 0.7:
            value_type = 'high_value'
        elif value_score > 0.5:
            value_type = 'moderate_value'
        else:
            value_type = 'low_value'
        
        specific_benefits = []
        if user_response['time_saved_minutes'] > 30:
            specific_benefits.append('significant_time_savings')
        if scenario.get('has_edge_case', False) and user_response['accepted']:
            specific_benefits.append('edge_case_resolution')
        if scenario['scenario_type'] == 'crisis_situation':
            specific_benefits.append('crisis_support')
        
        return {
            'value_score': value_score,
            'value_type': value_type,
            'specific_benefit': ', '.join(specific_benefits) if specific_benefits else 'general_improvement',
            'measurable_impact': user_response['time_saved_minutes'],
            'scenario_adapted': scenario_multiplier > 1.0
        }

    def _get_realistic_app(self, persona: str) -> str:
        """Get realistic app based on persona."""
        app_mapping = {
            'senior_developer': ['VSCode', 'Terminal', 'Slack', 'GitHub'],
            'junior_developer': ['VSCode', 'Chrome', 'Stack Overflow', 'GitHub'],
            'data_scientist': ['Jupyter', 'Python', 'Tableau', 'Excel'],
            'product_manager': ['Slack', 'Figma', 'Confluence', 'Excel'],
            'customer_success': ['Zendesk', 'Intercom', 'Salesforce', 'Slack']
        }
        return random.choice(app_mapping.get(persona, ['Chrome', 'Slack', 'Email']))

    def _get_realistic_task_category(self, persona: str) -> str:
        """Get realistic task category based on persona."""
        task_mapping = {
            'senior_developer': ['coding', 'architecture', 'code_review', 'mentoring'],
            'junior_developer': ['coding', 'learning', 'debugging', 'testing'],
            'data_scientist': ['data_analysis', 'modeling', 'visualization', 'research'],
            'product_manager': ['planning', 'communication', 'analysis', 'documentation'],
            'customer_success': ['customer_interaction', 'support', 'documentation', 'training']
        }
        return random.choice(task_mapping.get(persona, ['general_work']))

    def _save_batch_data(self, telemetry_batch: List[Dict], interactions_batch: List[Dict], batch_num: int):
        """Save batch data to prevent memory issues."""
        batch_dir = self.output_dir / f"batch_{batch_num}"
        batch_dir.mkdir(exist_ok=True)
        
        pd.DataFrame(telemetry_batch).to_csv(batch_dir / "telemetry.csv", index=False)
        
        with open(batch_dir / "interactions.jsonl", "w") as f:
            for interaction in interactions_batch:
                f.write(json.dumps(interaction) + "\n")

async def main():
    """Generate massive advanced training dataset."""
    
    generator = AdvancedTrainingDataGenerator()
    
    # Generate massive dataset focused on coaching value
    print("🎯 FOCUS: Maximum Coaching Value Optimization")
    print("📊 APPROACH: Realistic Edge Cases + Incomplete Scenarios")
    print("🚀 SCALE: Hundreds of Thousands of Training Examples")
    print()
    
    # Start with smaller scale for testing
    test_size = 50000  # 50K records for initial test
    
    results = await generator.generate_massive_advanced_dataset(test_size)
    
    print(f"\n✅ ADVANCED TRAINING DATA GENERATED")
    print(f"📈 Records: {results['total_telemetry_records']:,}")
    print(f"🎯 Interactions: {results['total_interactions']:,}")
    print(f"🔬 Edge Cases: ~{int(results['total_telemetry_records'] * 0.4):,}")
    print(f"📸 Incomplete Scenarios: ~{int(results['total_telemetry_records'] * 0.3):,}")
    print()
    print("🎉 READY FOR INTENSIVE COACHING VALUE OPTIMIZATION!")

if __name__ == "__main__":
    asyncio.run(main())