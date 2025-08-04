#!/usr/bin/env python3
"""
System Validation Script
Tests robustness of all components before running the main system.
"""

import asyncio
import logging
import os
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def validate_imports():
    """Test that all imports work correctly."""
    try:
        from api_clients_robust import ClaudeClient, OpenAIClient, MultiProviderLLMClient
        from json_parser import parse_llm_json, RobustJSONParser
        from config_loader import get_config, validate_environment
        logger.info("✅ All critical imports successful")
        return True
    except ImportError as e:
        logger.error(f"❌ Import validation failed: {e}")
        return False

async def validate_api_clients():
    """Test API client initialization and basic functionality."""
    try:
        # Test API key validation
        anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        if not anthropic_key:
            logger.warning("⚠️ ANTHROPIC_API_KEY not set")
            return False
        
        # Test client initialization
        claude_client = ClaudeClient(anthropic_key)
        logger.info("✅ Claude client initialized")
        
        # Test OpenAI if available
        openai_key = os.getenv('OPENAI_API_KEY')
        if openai_key:
            openai_client = OpenAIClient(openai_key)
            logger.info("✅ OpenAI client initialized")
        else:
            logger.info("ℹ️ OpenAI client not available (no API key)")
        
        return True
    except Exception as e:
        logger.error(f"❌ API client validation failed: {e}")
        return False

async def validate_json_parser():
    """Test JSON parser robustness."""
    try:
        from json_parser import RobustJSONParser
        parser = RobustJSONParser()
        
        # Test valid JSON
        valid_json = '{"focus_score": 75, "recommendations": ["test"]}'
        result = parser.parse_llm_response(valid_json, 'focus_integrity_evaluator')
        assert result is not None
        
        # Test malformed JSON
        malformed_json = '{"focus_score": 75, "recommendations": ["test"'
        result = parser.parse_llm_response(malformed_json, 'focus_integrity_evaluator')
        assert result is not None  # Should return fallback
        
        # Test garbage input
        garbage = "This is not JSON at all!"
        result = parser.parse_llm_response(garbage, 'focus_integrity_evaluator')
        assert result is not None  # Should return fallback
        
        logger.info("✅ JSON parser robustness validated")
        return True
    except Exception as e:
        logger.error(f"❌ JSON parser validation failed: {e}")
        return False

async def validate_directory_structure():
    """Check required directories and files exist."""
    try:
        # Check outputs directory
        Path("outputs").mkdir(exist_ok=True)
        
        # Check required files
        required_files = [
            "main.py",
            "api_clients_robust.py",
            "json_parser.py",
            "config_loader.py",
            "requirements.txt"
        ]
        
        missing_files = []
        for file in required_files:
            if not Path(file).exists():
                missing_files.append(file)
        
        if missing_files:
            logger.error(f"❌ Missing required files: {missing_files}")
            return False
        
        logger.info("✅ Directory structure validated")
        return True
    except Exception as e:
        logger.error(f"❌ Directory validation failed: {e}")
        return False

async def validate_configuration():
    """Test configuration loading."""
    try:
        from config_loader import get_config
        config = get_config()
        assert config is not None
        assert hasattr(config, 'api')
        assert hasattr(config, 'coaching')
        logger.info("✅ Configuration loading validated")
        return True
    except Exception as e:
        logger.error(f"❌ Configuration validation failed: {e}")
        return False

async def run_validation():
    """Run complete system validation."""
    print("🔍 AI Coach System Validation")
    print("=" * 40)
    
    validations = [
        ("Import System", validate_imports),
        ("Directory Structure", validate_directory_structure),
        ("Configuration", validate_configuration),
        ("JSON Parser", validate_json_parser),
        ("API Clients", validate_api_clients),
    ]
    
    results = []
    for name, validator in validations:
        print(f"\n🧪 Testing {name}...")
        result = await validator()
        results.append((name, result))
    
    print("\n" + "=" * 40)
    print("📊 VALIDATION RESULTS")
    print("=" * 40)
    
    passed = 0
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {name}")
        if result:
            passed += 1
    
    print(f"\n📈 Overall: {passed}/{len(results)} validations passed")
    
    if passed == len(results):
        print("\n🎉 System validation SUCCESSFUL!")
        print("   Ready to run: python main.py")
        return True
    else:
        print("\n⚠️ System validation FAILED!")
        print("   Please fix the issues above before running main.py")
        return False

async def main():
    """Main validation function."""
    success = await run_validation()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    asyncio.run(main())