"""
Initial evaluation prompts for AI Coach system.
These prompts will be evolved by OpenEvolve to optimize coaching effectiveness.
"""

INITIAL_PROMPTS = {
    'focus_integrity_evaluator': """
You are evaluating workplace focus integrity from telemetry data.

Data: {telemetry_chunk}

Analyze the data and calculate:
1. Context switch rate (window_switches_15min / 15)
2. Deep work percentage (time in focus_session_duration > 10 minutes)
3. Cognitive load average from cognitive_load_score
4. Tab overload indicator (tab_count > 30 is concerning)

Identify focus issues:
- Context switches > 18 per 15 minutes indicates scattered attention
- No deep work blocks > 30 minutes suggests fragmented workflow
- Cognitive load > 0.8 consistently shows mental overload
- Tab count > 50 indicates digital clutter

Provide specific, actionable recommendations based on the data patterns.

Output JSON format:
{
  "focus_score": 0-100 (higher is better),
  "context_switch_rate": number per minute,
  "deep_work_percentage": 0-100,
  "cognitive_load_avg": 0.0-1.0,
  "tab_overload": boolean,
  "recommendations": ["specific action 1", "specific action 2"],
  "alert_level": "low|medium|high",
  "key_insight": "one-line summary of main focus issue"
}
""",

    'wellbeing_evaluator': """
You are assessing employee wellbeing from workplace activity patterns.

Data: {telemetry_chunk}

Evaluate wellbeing indicators:
1. Break patterns (break_duration_min frequency and length)
2. Work streak duration (continuous work without breaks)
3. After-hours indicators (activity outside 9-6)
4. Stress signals (high keystrokes + high mouse clicks + high cognitive load)
5. Meeting overload (meeting_duration_min > 50% of time)

Flag wellbeing concerns:
- Work streaks > 120 minutes without break
- No breaks detected in 4+ hours
- Consistent high stress indicators (cognitive_load > 0.8)
- After-hours work becoming regular pattern
- Back-to-back meetings without recovery time

Generate supportive, non-judgmental alerts focused on sustainable performance.

Output JSON format:
{
  "wellbeing_score": 0-100 (higher is better),
  "work_streak_minutes": current streak length,
  "break_frequency_score": 0-100,
  "stress_level": "low|moderate|high",
  "meeting_load": "light|moderate|heavy",
  "stress_indicators": ["indicator1", "indicator2"],
  "alerts": ["wellbeing concern 1", "wellbeing concern 2"],
  "recovery_suggestion": "immediate action for wellbeing"
}
""",

    'value_creation_evaluator': """
You are analyzing value creation and productivity patterns from workplace activity.

Data: {telemetry_chunk}

Assess value creation metrics:
1. Core work percentage (task_category = 'Core' vs others)
2. Output indicators (code_commits, documents_created, email_sent)
3. Focus quality (correlation between deep work and output)
4. Administrative overhead (task_category = 'Admin' percentage)
5. Collaboration efficiency (meeting time vs output ratio)

Identify optimization opportunities:
- Repetitive tasks that could be automated
- Time blocks that could be protected for core work
- Low-value activities consuming significant time
- Workflow improvements based on app usage patterns
- Better tool usage for the persona type

Focus on practical, immediate improvements that increase value-creating time.

Output JSON format:
{
  "value_score": 0-100 (higher is better),
  "core_work_percentage": 0-100,
  "output_productivity": 0-100,
  "admin_overhead": 0-100,
  "collaboration_efficiency": "low|medium|high",
  "automation_opportunities": ["task1", "task2"],
  "optimization_suggestions": ["actionable tip 1", "actionable tip 2"],
  "biggest_time_drain": "primary non-value activity"
}
"""
}

# Prompt evolution constraints and targets
EVOLUTION_CONSTRAINTS = {
    'max_prompt_length': 2000,
    'required_json_fields': {
        'focus_integrity_evaluator': [
            'focus_score', 
            'recommendations', 
            'alert_level'
        ],
        'wellbeing_evaluator': [
            'wellbeing_score', 
            'alerts',
            'stress_level'
        ],
        'value_creation_evaluator': [
            'value_score', 
            'optimization_suggestions',
            'core_work_percentage'
        ]
    },
    'optimization_targets': {
        'json_validity': 0.95,        # 95% of outputs should be valid JSON
        'actionability_score': 0.80,   # 80% should have actionable suggestions
        'coaching_effectiveness': 0.75, # 75% acceptance rate target
        'response_consistency': 0.85    # 85% consistent output format
    }
}

# Nudge quality criteria for evolution
NUDGE_QUALITY_CRITERIA = {
    'length': {
        'min_words': 10,
        'max_words': 40,
        'optimal_words': 25
    },
    'tone': {
        'required_elements': ['friendly', 'supportive', 'specific'],
        'avoid_elements': ['commanding', 'vague', 'judgmental']
    },
    'structure': {
        'preferred_starters': ['Want to try', 'How about', 'Ready for'],
        'include_metric': True,  # Include specific number/metric
        'action_oriented': True  # Clear action to take
    }
}

# Sample data structure for reference
TELEMETRY_SAMPLE = {
    'record_count': 50,
    'time_range': {
        'start': '2025-08-04T09:00:00',
        'end': '2025-08-04T09:15:00'
    },
    'user_metrics': {
        'avg_keystrokes': 85.5,
        'total_window_switches': 24,
        'avg_cognitive_load': 0.72,
        'max_focus_duration': 8,
        'break_time': 0,
        'tab_count': 47
    },
    'app_usage': {
        'Browser': 35,
        'VSCode': 10,
        'Slack': 5
    },
    'task_distribution': {
        'Support': 30,
        'Core': 15,
        'Admin': 5
    }
}