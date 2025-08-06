class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.context_tracker = ContextTracker()
        self.recommendation_engine = RecommendationEngine()
        self.behavioral_model = BehavioralModel()
        self.intervention_manager = InterventionManager()

class ContextTracker:
    def __init__(self):
        self.cognitive_load = 0.0
        self.attention_state = None
        self.time_patterns = {}
        self.work_context = None
        
    def update_context(self, user_id, context_data):
        self.cognitive_load = self._assess_cognitive_load(context_data)
        self.attention_state = self._detect_attention_state(context_data)
        self.work_context = self._analyze_work_context(context_data)
        self._update_time_patterns(user_id, context_data)

    def _assess_cognitive_load(self, context_data):
        # Enhanced cognitive load assessment using multiple indicators
        task_complexity = context_data.get('task_complexity', 0)
        time_pressure = context_data.get('time_pressure', 0) 
        interruption_frequency = context_data.get('interruptions', 0)
        return (0.4 * task_complexity + 0.3 * time_pressure + 0.3 * interruption_frequency)

class BehavioralModel:
    def __init__(self):
        self.motivation_factors = {}
        self.habit_patterns = {}
        self.response_history = {}
        
    def analyze_behavior(self, user_id, behavior_data):
        motivation = self._assess_motivation(behavior_data)
        habits = self._identify_habits(behavior_data)
        receptivity = self._calculate_receptivity(behavior_data)
        return {
            'motivation_level': motivation,
            'habit_strength': habits,
            'intervention_receptivity': receptivity
        }

    def _assess_motivation(self, behavior_data):
        # Enhanced motivation assessment using Self-Determination Theory
        autonomy = behavior_data.get('autonomy', 0)
        competence = behavior_data.get('competence', 0)
        relatedness = behavior_data.get('relatedness', 0)
        return (autonomy + competence + relatedness) / 3

class RecommendationEngine:
    def __init__(self):
        self.action_templates = {}
        self.success_metrics = {}
        self.adaptation_rules = {}

    def generate_recommendation(self, user_id, context, behavior):
        recommendation = {
            'action': self._select_action(context, behavior),
            'timing': self._optimize_timing(context),
            'specificity': self._add_specificity(context),
            'metrics': self._define_metrics(),
            'difficulty': self._calibrate_difficulty(behavior)
        }
        return self._personalize_recommendation(recommendation, user_id)

    def _select_action(self, context, behavior):
        if context.cognitive_load > 0.7:
            return self._generate_low_effort_action()
        elif behavior['motivation_level'] < 0.5:
            return self._generate_motivation_focused_action()
        else:
            return self._generate_optimal_action()

class InterventionManager:
    def __init__(self):
        self.intervention_history = {}
        self.effectiveness_metrics = {}
        self.timing_optimizer = TimingOptimizer()

    def create_intervention(self, user_id, context, behavior, recommendation):
        timing = self.timing_optimizer.get_optimal_timing(user_id, context)
        
        intervention = {
            'content': self._format_content(recommendation),
            'delivery_time': timing,
            'priority': self._calculate_priority(context, behavior),
            'follow_up': self._schedule_follow_up(timing)
        }
        
        return self._personalize_intervention(intervention, user_id)

    def _format_content(self, recommendation):
        return {
            'action_steps': self._break_down_steps(recommendation['action']),
            'time_estimate': self._estimate_time(recommendation['action']),
            'success_criteria': recommendation['metrics'],
            'alternatives': self._generate_alternatives(recommendation)
        }

class TimingOptimizer:
    def __init__(self):
        self.user_patterns = {}
        self.effectiveness_data = {}
        
    def get_optimal_timing(self, user_id, context):
        cognitive_load = context.cognitive_load
        attention_state = context.attention_state
        time_patterns = context.time_patterns.get(user_id, {})
        
        return self._calculate_optimal_time(
            cognitive_load,
            attention_state, 
            time_patterns
        )

    def _calculate_optimal_time(self, cognitive_load, attention_state, patterns):
        # Enhanced timing optimization using multiple factors
        if cognitive_load > 0.8:
            return 'defer'
        elif attention_state == 'flow':
            return 'after_flow'
        else:
            return self._find_next_optimal_window(patterns)