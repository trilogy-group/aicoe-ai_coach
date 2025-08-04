"""
Robust JSON parsing and validation for LLM outputs.
"""

import json
import re
import logging
from typing import Dict, Any, Optional, Union, List
from pydantic import BaseModel, Field, validator
from enum import Enum

# Set up logging
logger = logging.getLogger(__name__)

class AlertLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class StressLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"

class FocusEvaluation(BaseModel):
    """Validated focus integrity evaluation."""
    focus_score: float = Field(..., ge=0, le=100)
    context_switch_rate: float = Field(..., ge=0)
    deep_work_percentage: float = Field(..., ge=0, le=100)
    cognitive_load_avg: float = Field(..., ge=0, le=1)
    tab_overload: bool = Field(default=False)
    recommendations: List[str] = Field(..., min_items=1, max_items=5)
    alert_level: AlertLevel = Field(...)
    key_insight: Optional[str] = Field(None, max_length=200)

class WellbeingEvaluation(BaseModel):
    """Validated wellbeing evaluation."""
    wellbeing_score: float = Field(..., ge=0, le=100)
    work_streak_minutes: int = Field(..., ge=0)
    break_frequency_score: float = Field(..., ge=0, le=100)
    stress_level: StressLevel = Field(...)
    meeting_load: str = Field(..., pattern=r'^(light|moderate|heavy)$')
    stress_indicators: List[str] = Field(default_factory=list, max_items=5)
    alerts: List[str] = Field(default_factory=list, max_items=3)
    recovery_suggestion: Optional[str] = Field(None, max_length=150)

class ValueCreationEvaluation(BaseModel):
    """Validated value creation evaluation."""
    value_score: float = Field(..., ge=0, le=100)
    core_work_percentage: float = Field(..., ge=0, le=100)
    output_productivity: float = Field(..., ge=0, le=100)
    admin_overhead: float = Field(..., ge=0, le=100)
    collaboration_efficiency: str = Field(..., pattern=r'^(low|medium|high)$')
    automation_opportunities: List[str] = Field(default_factory=list, max_items=4)
    optimization_suggestions: List[str] = Field(..., min_items=1, max_items=4)
    biggest_time_drain: Optional[str] = Field(None, max_length=100)

class NudgeOutput(BaseModel):
    """Validated nudge output."""
    nudge_text: str = Field(..., min_length=10, max_length=200)
    nudge_type: str = Field(..., pattern=r'^(focus|wellbeing|value_creation)$')
    confidence: float = Field(..., ge=0.0, le=1.0)
    expected_outcome: str = Field(..., min_length=5, max_length=100)
    trigger_reason: Optional[str] = Field(None, max_length=100)
    snooze_options: List[str] = Field(default=["15min", "1hour", "rest-of-day"])
    
    @validator('nudge_text')
    def validate_nudge_text(cls, v):
        """Validate nudge text quality."""
        word_count = len(v.split())
        if word_count > 50:
            raise ValueError("Nudge text too long (>50 words)")
        
        # Check for friendly tone indicators
        friendly_patterns = [r'\b(want to|how about|ready for|consider|try)\b']
        if not any(re.search(pattern, v.lower()) for pattern in friendly_patterns):
            logger.warning("Nudge text may not be friendly enough")
        
        return v

class RobustJSONParser:
    """Robust JSON parser for LLM outputs with validation and fallbacks."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Schema mapping for different evaluator types
        self.schema_mapping = {
            'focus_integrity_evaluator': FocusEvaluation,
            'wellbeing_evaluator': WellbeingEvaluation,
            'value_creation_evaluator': ValueCreationEvaluation,
            'nudge': NudgeOutput
        }
    
    def parse_llm_response(self, response: str, expected_type: str) -> Optional[Dict[str, Any]]:
        """Parse LLM response with validation and error recovery."""
        try:
            # Step 1: Extract JSON from response
            json_str = self._extract_json(response)
            if not json_str:
                self.logger.warning(f"No JSON found in response: {response[:100]}...")
                return self._generate_fallback(expected_type)
            
            # Step 2: Parse JSON
            raw_data = json.loads(json_str)
            
            # Step 3: Validate with Pydantic
            if expected_type in self.schema_mapping:
                validated_data = self._validate_with_schema(raw_data, expected_type)
                if validated_data:
                    return validated_data.dict()
            
            # Step 4: Basic validation if no schema
            return self._basic_validation(raw_data, expected_type)
            
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decode error: {e}")
            return self._attempt_json_repair(response, expected_type)
        
        except Exception as e:
            self.logger.error(f"Unexpected parsing error: {e}")
            return self._generate_fallback(expected_type)
    
    def _extract_json(self, text: str) -> Optional[str]:
        """Extract JSON from potentially noisy text."""
        # Remove common prefixes/suffixes
        text = text.strip()
        
        # Look for JSON object patterns
        json_patterns = [
            r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}',  # Simple nested objects
            r'\{.*\}',  # Greedy match
        ]
        
        for pattern in json_patterns:
            matches = re.findall(pattern, text, re.DOTALL)
            for match in matches:
                # Try to parse each match
                try:
                    json.loads(match)
                    return match
                except:
                    continue
        
        # If no valid JSON found, try to construct from key-value pairs
        return self._construct_json_from_text(text)
    
    def _construct_json_from_text(self, text: str) -> Optional[str]:
        """Try to construct JSON from structured text."""
        try:
            # Look for key-value patterns
            patterns = [
                r'(\w+):\s*(["\']?)([^"\'\n]+)\2',  # key: value
                r'(\w+)\s*=\s*(["\']?)([^"\'\n]+)\2'  # key = value
            ]
            
            data = {}
            for pattern in patterns:
                matches = re.findall(pattern, text)
                for key, quote, value in matches:
                    # Try to convert to appropriate type
                    if value.lower() in ['true', 'false']:
                        data[key] = value.lower() == 'true'
                    elif value.isdigit():
                        data[key] = int(value)
                    elif re.match(r'^\d+\.\d+$', value):
                        data[key] = float(value)
                    else:
                        data[key] = value.strip()
            
            if data:
                return json.dumps(data)
                
        except Exception as e:
            self.logger.debug(f"Failed to construct JSON: {e}")
        
        return None
    
    def _validate_with_schema(self, data: Dict, expected_type: str) -> Optional[BaseModel]:
        """Validate data with Pydantic schema."""
        try:
            schema_class = self.schema_mapping[expected_type]
            return schema_class(**data)
        except Exception as e:
            self.logger.warning(f"Schema validation failed for {expected_type}: {e}")
            # Try to fix common issues
            return self._attempt_schema_repair(data, expected_type)
    
    def _attempt_schema_repair(self, data: Dict, expected_type: str) -> Optional[BaseModel]:
        """Attempt to repair data to match schema."""
        try:
            schema_class = self.schema_mapping[expected_type]
            
            # Common repairs
            repaired_data = dict(data)
            
            # Fix score fields (ensure 0-100 range)
            score_fields = ['focus_score', 'wellbeing_score', 'value_score', 
                          'core_work_percentage', 'output_productivity']
            for field in score_fields:
                if field in repaired_data:
                    value = repaired_data[field]
                    if isinstance(value, (int, float)):
                        repaired_data[field] = max(0, min(100, float(value)))
            
            # Fix confidence field (ensure 0-1 range)
            if 'confidence' in repaired_data:
                value = repaired_data['confidence']
                if isinstance(value, (int, float)):
                    if value > 1:
                        repaired_data['confidence'] = value / 100  # Convert percentage
                    repaired_data['confidence'] = max(0, min(1, float(value)))
            
            # Ensure list fields are lists
            list_fields = ['recommendations', 'alerts', 'stress_indicators', 
                         'automation_opportunities', 'optimization_suggestions']
            for field in list_fields:
                if field in repaired_data and not isinstance(repaired_data[field], list):
                    if isinstance(repaired_data[field], str):
                        repaired_data[field] = [repaired_data[field]]
                    else:
                        repaired_data[field] = []
            
            # Try validation again
            return schema_class(**repaired_data)
            
        except Exception as e:
            self.logger.warning(f"Schema repair failed: {e}")
            return None
    
    def _basic_validation(self, data: Dict, expected_type: str) -> Dict[str, Any]:
        """Basic validation without strict schema."""
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        
        # Ensure required fields exist based on type
        required_fields = {
            'focus_integrity_evaluator': ['focus_score', 'recommendations'],
            'wellbeing_evaluator': ['wellbeing_score', 'alerts'],
            'value_creation_evaluator': ['value_score', 'optimization_suggestions'],
            'nudge': ['nudge_text', 'nudge_type', 'confidence']
        }
        
        if expected_type in required_fields:
            for field in required_fields[expected_type]:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")
        
        return data
    
    def _attempt_json_repair(self, text: str, expected_type: str) -> Optional[Dict[str, Any]]:
        """Attempt to repair malformed JSON."""
        try:
            # Common JSON repairs
            repairs = [
                (r',\s*}', '}'),  # Remove trailing commas
                (r',\s*]', ']'),  # Remove trailing commas in arrays
                (r'{\s*,', '{'),  # Remove leading commas
                (r'"\s*:\s*"([^"]*)"([^,}\]]*)', r'": "\1\2"'),  # Fix unclosed quotes
            ]
            
            repaired = text
            for pattern, replacement in repairs:
                repaired = re.sub(pattern, replacement, repaired)
            
            # Try parsing repaired JSON
            json_str = self._extract_json(repaired)
            if json_str:
                data = json.loads(json_str)
                return self._basic_validation(data, expected_type)
                
        except Exception as e:
            self.logger.debug(f"JSON repair attempt failed: {e}")
        
        return self._generate_fallback(expected_type)
    
    def _generate_fallback(self, expected_type: str) -> Dict[str, Any]:
        """Generate fallback response when parsing fails."""
        fallbacks = {
            'focus_integrity_evaluator': {
                'focus_score': 50,
                'context_switch_rate': 1.0,
                'deep_work_percentage': 30,
                'cognitive_load_avg': 0.6,
                'recommendations': ['Take a short break', 'Close unnecessary applications'],
                'alert_level': 'medium',
                'key_insight': 'Unable to fully analyze focus patterns'
            },
            'wellbeing_evaluator': {
                'wellbeing_score': 60,
                'work_streak_minutes': 90,
                'break_frequency_score': 50,
                'stress_level': 'moderate',
                'meeting_load': 'moderate',
                'alerts': ['Consider taking a break'],
                'recovery_suggestion': 'Step away from the computer for 5 minutes'
            },
            'value_creation_evaluator': {
                'value_score': 65,
                'core_work_percentage': 50,
                'output_productivity': 60,
                'admin_overhead': 30,
                'collaboration_efficiency': 'medium',
                'optimization_suggestions': ['Block time for important tasks'],
                'biggest_time_drain': 'Excessive context switching'
            },
            'nudge': {
                'nudge_text': 'How about taking a quick break to recharge?',
                'nudge_type': 'wellbeing',
                'confidence': 0.7,
                'expected_outcome': 'Improved focus and energy',
                'trigger_reason': 'parsing_fallback',
                'snooze_options': ['15min', '1hour', 'rest-of-day']
            }
        }
        
        self.logger.warning(f"Using fallback response for {expected_type}")
        return fallbacks.get(expected_type, {'error': 'Unknown evaluation type'})

# Global parser instance
_json_parser = RobustJSONParser()

def parse_llm_json(response: str, expected_type: str) -> Optional[Dict[str, Any]]:
    """Parse LLM JSON response with validation."""
    return _json_parser.parse_llm_response(response, expected_type)