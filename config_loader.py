"""
Robust configuration loading and validation system.
"""

import os
import yaml
import logging
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, validator
from pathlib import Path

class APIConfig(BaseModel):
    """API configuration with validation."""
    anthropic_model: str = Field(default="claude-3-5-sonnet-20241022")
    anthropic_max_tokens: int = Field(default=1000, ge=100, le=4000)
    anthropic_temperature: float = Field(default=0.3, ge=0.0, le=2.0)
    anthropic_timeout: int = Field(default=30, ge=5, le=120)
    
    openai_model: str = Field(default="gpt-4o")
    openai_evolution_model: str = Field(default="gpt-4o-mini")
    openai_max_tokens: int = Field(default=1500, ge=100, le=4000)
    openai_temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    openai_timeout: int = Field(default=30, ge=5, le=120)

class DataGenerationConfig(BaseModel):
    """Data generation configuration."""
    default_users: int = Field(default=50, ge=1, le=1000)
    default_records: int = Field(default=10000, ge=100, le=1000000)
    days_of_history: int = Field(default=30, ge=1, le=365)
    time_acceleration: int = Field(default=60, ge=1, le=3600)

class EvolutionConfig(BaseModel):
    """Evolution algorithm configuration."""
    population_size: int = Field(default=20, ge=5, le=100)
    generations: int = Field(default=50, ge=5, le=500)
    elite_ratio: float = Field(default=0.2, ge=0.1, le=0.5)
    crossover_probability: float = Field(default=0.7, ge=0.1, le=0.9)
    mutation_probability: float = Field(default=0.3, ge=0.1, le=0.9)
    convergence_threshold: float = Field(default=0.01, ge=0.001, le=0.1)

class CoachingConfig(BaseModel):
    """Coaching system configuration."""
    max_daily_nudges: int = Field(default=3, ge=1, le=10)
    min_nudge_interval_minutes: int = Field(default=30, ge=5, le=240)
    confidence_threshold: float = Field(default=0.7, ge=0.5, le=0.95)
    analysis_window_minutes: int = Field(default=15, ge=5, le=60)
    max_words: int = Field(default=40, ge=10, le=100)

class SystemConfig(BaseModel):
    """Complete system configuration."""
    api: APIConfig = Field(default_factory=APIConfig)
    data_generation: DataGenerationConfig = Field(default_factory=DataGenerationConfig)
    evolution: EvolutionConfig = Field(default_factory=EvolutionConfig)
    coaching: CoachingConfig = Field(default_factory=CoachingConfig)
    
    # Environment variables
    anthropic_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        # Load API keys from environment
        self.anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
    
    @validator('anthropic_api_key')
    def validate_anthropic_key(cls, v):
        if not v:
            raise ValueError("ANTHROPIC_API_KEY environment variable is required")
        if not v.startswith('sk-ant-'):
            logging.warning("Anthropic API key format looks unusual")
        return v
    
    def validate_for_mode(self, mode: str):
        """Validate configuration for specific mode."""
        if mode == 'training' and not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY is required for training mode")

class ConfigLoader:
    """Robust configuration loader with validation and defaults."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path or "config.yaml"
        self.config: Optional[SystemConfig] = None
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup basic logging."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def load_config(self) -> SystemConfig:
        """Load and validate configuration."""
        try:
            config_data = {}
            
            # Try to load YAML config
            if Path(self.config_path).exists():
                with open(self.config_path, 'r') as f:
                    config_data = yaml.safe_load(f) or {}
                self.logger.info(f"Loaded configuration from {self.config_path}")
            else:
                self.logger.warning(f"Config file {self.config_path} not found, using defaults")
            
            # Create and validate config
            self.config = SystemConfig(**config_data)
            self.logger.info("Configuration validation successful")
            
            return self.config
            
        except Exception as e:
            self.logger.error(f"Configuration loading failed: {e}")
            self.logger.info("Falling back to default configuration")
            self.config = SystemConfig()
            return self.config
    
    def get_config(self) -> SystemConfig:
        """Get loaded configuration or load if not already loaded."""
        if self.config is None:
            return self.load_config()
        return self.config
    
    def validate_api_keys(self, mode: str = 'inference'):
        """Validate API keys for the given mode."""
        if self.config is None:
            self.load_config()
        
        try:
            self.config.validate_for_mode(mode)
            self.logger.info(f"API key validation successful for {mode} mode")
        except ValueError as e:
            self.logger.error(f"API key validation failed: {e}")
            raise

# Global config loader instance
_config_loader = ConfigLoader()

def get_config() -> SystemConfig:
    """Get global configuration instance."""
    return _config_loader.get_config()

def validate_environment(mode: str = 'inference'):
    """Validate environment for given mode."""
    _config_loader.validate_api_keys(mode)