# [Previous code remains unchanged until the AICoach class initialization]

class AICoach:
    def __init__(self):
        # [Previous initialization code remains unchanged]
        
        # NEW: Enhanced intervention timing system
        self.intervention_timing = {
            'manager': {
                'optimal_intervals': {
                    'morning': 45,      # Minutes between interventions (9am-12pm)
                    'afternoon': 35,    # (1pm-5pm)
                    'evening': 60       # (After 5pm)
                },
                'cognitive_load_thresholds': {
                    'low': 0.3,         # More frequent interventions
                    'medium': 0.6,      # Standard interval
                    'high': 0.8         # Reduced frequency
                },
                'flow_state_protection': {
                    'detection_threshold': 0.75,
                    'minimum_protection_minutes': 45,
                    'gradual_reentry': True
                }
            },
            'analyst': {
                'optimal_intervals': {
                    'morning': 40,
                    'afternoon': 30,
                    'evening': 50
                },
                'cognitive_load_thresholds': {
                    'low': 0.35,
                    'medium': 0.65,
                    'high': 0.85
                },
                'flow_state_protection': {
                    'detection_threshold': 0.8,
                    'minimum_protection_minutes': 60,
                    'gradual_reentry': True
                }
            },
            # [Similar configurations for other personas]
        }
        
        # NEW: Intervention history tracking
        self.intervention_history = {}
        
        # NEW: Adaptive timing learning
        self.timing_effectiveness = {
            'response_rates': {},
            'optimal_times': {},
            'persona_patterns': {}
        }

    async def analyze_and_coach(self, data: pd.DataFrame, user_id: int) -> Optional[Dict]:
        # Add new timing check before proceeding
        if not self._is_appropriate_intervention_time(user_id, data):
            return None
            
        # [Rest of the method remains unchanged]

    def _is_appropriate_intervention_time(self, user_id: int, data: pd.DataFrame) -> bool:
        """Enhanced intervention timing check."""
        try:
            current_time = datetime.now()
            persona = self._extract_user_context(data).get('persona_type', 'manager')
            
            # Get timing configuration
            timing_config = self.intervention_timing.get(persona, self.intervention_timing['manager'])
            
            # Check last intervention time
            last_intervention = self.intervention_history.get(user_id, {}).get('last_time')
            if last_intervention:
                # Get appropriate interval based on time of day
                current_hour = current_time.hour
                if 9 <= current_hour < 12:
                    min_interval = timing_config['optimal_intervals']['morning']
                elif 13 <= current_hour < 17:
                    min_interval = timing_config['optimal_intervals']['afternoon']
                else:
                    min_interval = timing_config['optimal_intervals']['evening']
                
                # Adjust interval based on cognitive load
                cognitive_load = self._extract_user_context(data).get('cognitive_load', 0.5)
                if cognitive_load >= timing_config['cognitive_load_thresholds']['high']:
                    min_interval *= 1.5  # Increase interval when cognitive load is high
                elif cognitive_load <= timing_config['cognitive_load_thresholds']['low']:
                    min_interval *= 0.8  # Decrease interval when cognitive load is low
                
                # Check flow state
                if self._is_in_flow_state(data):
                    protection_minutes = timing_config['flow_state_protection']['minimum_protection_minutes']
                    if (current_time - last_intervention).total_seconds() < protection_minutes * 60:
                        return False
                
                # Check minimum interval
                if (current_time - last_intervention).total_seconds() < min_interval * 60:
                    return False
            
            # Update intervention history
            if user_id not in self.intervention_history:
                self.intervention_history[user_id] = {}
            self.intervention_history[user_id]['last_time'] = current_time
            
            return True
            
        except Exception as e:
            logger.error(f"Intervention timing check failed: {str(e)}")
            return True  # Default to allowing intervention on error

    def _is_in_flow_state(self, data: pd.DataFrame) -> bool:
        """Enhanced flow state detection."""
        context = self._extract_user_context(data)
        
        flow_indicators = {
            'focus_duration': context.get('focus_duration', 0) > 25,
            'cognitive_load': 0.6 <= context.get('cognitive_load', 0) <= 0.8,
            'interruption_count': context.get('interruption_count', 0) < 2,
            'productivity_score': context.get('productivity_score', 0) > 0.8
        }
        
        return sum(flow_indicators.values()) >= 3  # At least 3 indicators must be positive

    def track_nudge_outcome(self, user_id: int, persona: str, nudge: Dict, outcome: Dict):
        """Enhanced outcome tracking with timing optimization."""
        # [Previous tracking code remains]
        
        # NEW: Track timing effectiveness
        current_hour = datetime.now().hour
        response_time = outcome.get('response_time_seconds', 0)
        accepted = outcome.get('accepted', False)
        
        if persona not in self.timing_effectiveness['response_rates']:
            self.timing_effectiveness['response_rates'][persona] = {}
        
        hour_key = f"{current_hour:02d}"
        if hour_key not in self.timing_effectiveness['response_rates'][persona]:
            self.timing_effectiveness['response_rates'][persona][hour_key] = {
                'attempts': 0,
                'acceptances': 0,
                'total_response_time': 0
            }
        
        stats = self.timing_effectiveness['response_rates'][persona][hour_key]
        stats['attempts'] += 1
        if accepted:
            stats['acceptances'] += 1
        stats['total_response_time'] += response_time
        
        # Optimize timing based on patterns
        self._optimize_intervention_timing(persona, current_hour, accepted, response_time)

    def _optimize_intervention_timing(self, persona: str, hour: int, accepted: bool, response_time: float):
        """Optimize intervention timing based on outcomes."""
        if persona not in self.timing_effectiveness['optimal_times']:
            self.timing_effectiveness['optimal_times'][persona] = {}
        
        hour_key = f"{hour:02d}"
        if hour_key not in self.timing_effectiveness['optimal_times'][persona]:
            self.timing_effectiveness['optimal_times'][persona][hour_key] = {
                'acceptance_rate': 0.0,
                'avg_response_time': 0.0,
                'sample_count': 0
            }
        
        stats = self.timing_effectiveness['optimal_times'][persona][hour_key]
        stats['sample_count'] += 1
        
        # Update running averages
        stats['acceptance_rate'] = (
            (stats['acceptance_rate'] * (stats['sample_count'] - 1) + int(accepted))
            / stats['sample_count']
        )
        
        stats['avg_response_time'] = (
            (stats['avg_response_time'] * (stats['sample_count'] - 1) + response_time)
            / stats['sample_count']
        )
        
        # Adjust intervention intervals based on patterns
        if stats['sample_count'] >= 10:  # Enough samples to make adjustments
            if stats['acceptance_rate'] < 0.3:  # Low acceptance rate
                self.intervention_timing[persona]['optimal_intervals']['morning'] *= 1.2
                self.intervention_timing[persona]['optimal_intervals']['afternoon'] *= 1.2
            elif stats['acceptance_rate'] > 0.8:  # High acceptance rate
                self.intervention_timing[persona]['optimal_intervals']['morning'] *= 0.9
                self.intervention_timing[persona]['optimal_intervals']['afternoon'] *= 0.9

# [Rest of the code remains unchanged]