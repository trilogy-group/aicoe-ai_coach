class EnhancedAICoach:
    def __init__(self):
        self.user_profiles = {}
        self.intervention_history = {}
        self.behavioral_patterns = {}
        self.cognitive_models = {}
        
    def initialize_user(self, user_id):
        """Initialize tracking for a new user"""
        self.user_profiles[user_id] = {
            'preferences': {},
            'learning_style': None,
            'motivation_factors': [],
            'response_history': [],
            'cognitive_load': 0.0,
            'attention_span': 0.0,
            'energy_level': 0.0,
            'flow_state': False
        }
        
        self.intervention_history[user_id] = []
        self.behavioral_patterns[user_id] = {
            'daily_rhythm': {},
            'productivity_peaks': [],
            'break_patterns': [],
            'task_completion_rates': {}
        }
        
    def assess_context(self, user_id, context_data):
        """Evaluate current user context for intervention timing"""
        cognitive_load = self._calculate_cognitive_load(context_data)
        attention_span = self._estimate_attention(context_data)
        energy_level = self._analyze_energy_state(context_data)
        
        return {
            'cognitive_load': cognitive_load,
            'attention_span': attention_span,
            'energy_level': energy_level,
            'optimal_timing': self._determine_timing(user_id, context_data),
            'receptivity': self._calculate_receptivity(user_id, context_data)
        }

    def generate_intervention(self, user_id, context):
        """Create personalized coaching intervention"""
        if not self._should_intervene(user_id, context):
            return None
            
        user_state = self.assess_context(user_id, context)
        
        intervention = {
            'type': self._select_intervention_type(user_state),
            'content': self._generate_content(user_id, user_state),
            'intensity': self._calibrate_intensity(user_state),
            'timing': self._optimize_timing(user_id, context),
            'delivery_method': self._select_delivery_method(user_state)
        }
        
        self._record_intervention(user_id, intervention)
        return intervention

    def _select_intervention_type(self, user_state):
        """Choose most appropriate intervention based on user state"""
        if user_state['cognitive_load'] > 0.8:
            return 'micro_break'
        elif user_state['energy_level'] < 0.3:
            return 'energy_boost'
        elif user_state['attention_span'] < 0.4:
            return 'focus_enhancement'
        else:
            return 'progress_check'

    def _generate_content(self, user_id, user_state):
        """Create specific, actionable recommendation content"""
        intervention_type = self._select_intervention_type(user_state)
        user_prefs = self.user_profiles[user_id]['preferences']
        
        content_templates = {
            'micro_break': [
                "Take a 2-minute stretch break focusing on {body_part}",
                "Do {num_reps} deep breaths using the 4-7-8 technique",
                "Look away from your screen at something {distance} away"
            ],
            'energy_boost': [
                "Stand up and do {exercise_type} for 60 seconds",
                "Drink a glass of water and walk for {duration} minutes",
                "Do {num_reps} jumping jacks to increase blood flow"
            ],
            'focus_enhancement': [
                "Clear your workspace of {item_type} to reduce distractions",
                "Set a {duration} minute timer for focused work on {task}",
                "Use noise-canceling headphones for the next {duration} minutes"
            ],
            'progress_check': [
                "Review your top 3 priorities for {timeframe}",
                "Write down your next actionable step for {task}",
                "Evaluate progress on {project} against your goal"
            ]
        }
        
        return self._personalize_content(
            content_templates[intervention_type],
            user_prefs,
            user_state
        )

    def _calibrate_intensity(self, user_state):
        """Adjust intervention intensity based on user state"""
        base_intensity = 0.5
        modifiers = {
            'cognitive_load': -0.3,
            'energy_level': 0.2,
            'attention_span': 0.1
        }
        
        intensity = base_intensity
        for metric, modifier in modifiers.items():
            intensity += user_state[metric] * modifier
            
        return max(0.1, min(1.0, intensity))

    def _optimize_timing(self, user_id, context):
        """Determine optimal intervention timing"""
        patterns = self.behavioral_patterns[user_id]
        current_time = context.get('timestamp')
        
        return {
            'optimal_hour': self._find_optimal_hour(patterns, current_time),
            'min_spacing': self._calculate_spacing(patterns),
            'max_frequency': self._determine_frequency(patterns)
        }

    def _record_intervention(self, user_id, intervention):
        """Track intervention history"""
        self.intervention_history[user_id].append({
            'timestamp': intervention['timing'],
            'type': intervention['type'],
            'intensity': intervention['intensity'],
            'response': None  # To be updated with user response
        })

    def update_user_response(self, user_id, intervention_id, response_data):
        """Process user response to intervention"""
        self.user_profiles[user_id]['response_history'].append(response_data)
        self._adapt_strategies(user_id, response_data)
        self._update_behavioral_patterns(user_id, response_data)

    def _adapt_strategies(self, user_id, response_data):
        """Adjust coaching strategies based on user response"""
        effectiveness = response_data.get('effectiveness', 0.0)
        satisfaction = response_data.get('satisfaction', 0.0)
        
        if effectiveness < 0.3 or satisfaction < 0.3:
            self._adjust_intervention_parameters(user_id, 'decrease')
        elif effectiveness > 0.7 and satisfaction > 0.7:
            self._adjust_intervention_parameters(user_id, 'increase')

    def _should_intervene(self, user_id, context):
        """Determine if intervention is appropriate"""
        user_state = self.assess_context(user_id, context)
        last_intervention = self.intervention_history[user_id][-1] if self.intervention_history[user_id] else None
        
        return (
            not self.user_profiles[user_id]['flow_state'] and
            user_state['receptivity'] > 0.6 and
            (not last_intervention or 
             self._sufficient_time_elapsed(last_intervention, context))
        )