"""
Robust API Clients for Claude and OpenAI
Provides unified interface with comprehensive error handling, retry logic, and concurrency control.
"""

import os
import asyncio
import json
import logging
from typing import Dict, Any, Optional, List, Union
import time
from datetime import datetime, timedelta
import anthropic
from openai import AsyncOpenAI

# Set up logging
logger = logging.getLogger(__name__)

class RateLimiter:
    """Rate limiter for API calls."""
    
    def __init__(self, max_calls_per_minute: int = 60):
        self.max_calls = max_calls_per_minute
        self.calls = []
        self.lock = asyncio.Lock()
    
    async def acquire(self):
        """Acquire permission to make an API call."""
        async with self.lock:
            now = datetime.now()
            # Remove calls older than 1 minute
            self.calls = [call_time for call_time in self.calls 
                         if now - call_time < timedelta(minutes=1)]
            
            if len(self.calls) >= self.max_calls:
                # Calculate wait time
                oldest_call = min(self.calls)
                wait_time = 60 - (now - oldest_call).total_seconds()
                if wait_time > 0:
                    logger.warning(f"Rate limit reached, waiting {wait_time:.1f} seconds")
                    await asyncio.sleep(wait_time)
            
            self.calls.append(now)

class APIError(Exception):
    """Custom API error with retry information."""
    
    def __init__(self, message: str, provider: str, retry_count: int = 0, 
                 is_rate_limit: bool = False, is_temporary: bool = True):
        super().__init__(message)
        self.provider = provider
        self.retry_count = retry_count
        self.is_rate_limit = is_rate_limit
        self.is_temporary = is_temporary

class RobustAPIClient:
    """Base API client with robust error handling and retry logic."""
    
    def __init__(self, api_key: str, provider: str, max_retries: int = 3, 
                 timeout: int = 30, max_calls_per_minute: int = 60):
        if not api_key:
            raise ValueError(f"API key is required for {provider}")
            
        self.api_key = api_key
        self.provider = provider
        self.max_retries = max_retries
        self.timeout = timeout
        self.rate_limiter = RateLimiter(max_calls_per_minute)
        
        # Statistics
        self.stats = {
            'total_calls': 0,
            'successful_calls': 0,
            'failed_calls': 0,
            'retries': 0,
            'rate_limit_hits': 0,
            'total_response_time': 0.0
        }
    
    async def _retry_with_backoff(self, func, *args, **kwargs):
        """Retry function with exponential backoff and jitter."""
        last_exception = None
        start_time = time.time()
        
        for attempt in range(self.max_retries + 1):
            try:
                # Rate limiting
                await self.rate_limiter.acquire()
                
                # Update stats
                self.stats['total_calls'] += 1
                if attempt > 0:
                    self.stats['retries'] += 1
                
                # Make the call with timeout
                result = await asyncio.wait_for(
                    func(*args, **kwargs), 
                    timeout=self.timeout
                )
                
                # Update success stats
                elapsed = time.time() - start_time
                self.stats['successful_calls'] += 1
                self.stats['total_response_time'] += elapsed
                
                return result
                
            except asyncio.TimeoutError as e:
                last_exception = APIError(
                    f"API call timed out after {self.timeout}s", 
                    self.provider, attempt, is_temporary=True
                )
                logger.warning(f"{self.provider} timeout on attempt {attempt + 1}")
                
            except Exception as e:
                # Classify the error
                is_rate_limit = self._is_rate_limit_error(e)
                is_temporary = self._is_temporary_error(e)
                
                last_exception = APIError(
                    str(e), self.provider, attempt, 
                    is_rate_limit=is_rate_limit, is_temporary=is_temporary
                )
                
                if is_rate_limit:
                    self.stats['rate_limit_hits'] += 1
                
                logger.warning(f"{self.provider} call failed on attempt {attempt + 1}: {str(e)[:100]}")
                
                # Don't retry on permanent errors
                if not is_temporary and attempt == 0:
                    logger.error(f"Permanent error detected, not retrying: {str(e)}")
                    break
            
            # Calculate wait time with exponential backoff and jitter
            if attempt < self.max_retries:
                base_wait = min(2 ** attempt, 60)  # Cap at 60 seconds
                jitter = base_wait * 0.1 * (2 * time.time() % 1 - 1)
                wait_time = max(1, base_wait + jitter)
                
                if last_exception and last_exception.is_rate_limit:
                    wait_time = max(wait_time, 60)  # Minimum 1 minute for rate limits
                
                logger.info(f"Retrying {self.provider} in {wait_time:.1f}s...")
                await asyncio.sleep(wait_time)
        
        # All retries exhausted
        self.stats['failed_calls'] += 1
        raise last_exception or APIError("Unknown error", self.provider)
    
    def _is_rate_limit_error(self, error: Exception) -> bool:
        """Check if error is due to rate limiting."""
        error_str = str(error).lower()
        rate_limit_indicators = [
            'rate limit', 'too many requests', '429', 'quota exceeded',
            'requests per minute', 'rate exceeded', 'throttle'
        ]
        return any(indicator in error_str for indicator in rate_limit_indicators)
    
    def _is_temporary_error(self, error: Exception) -> bool:
        """Check if error is temporary and worth retrying."""
        error_str = str(error).lower()
        
        # Permanent errors - don't retry
        permanent_indicators = [
            'invalid api key', 'unauthorized', '401', 'forbidden', '403',
            'not found', '404', 'invalid request', 'bad request', '400'
        ]
        
        if any(indicator in error_str for indicator in permanent_indicators):
            return False
        
        # Temporary errors - worth retrying
        temporary_indicators = [
            'timeout', 'connection', 'network', '500', '502', '503', '504',
            'internal server error', 'bad gateway', 'service unavailable',
            'gateway timeout', 'rate limit', '429', 'server error'
        ]
        
        return any(indicator in error_str for indicator in temporary_indicators)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get API usage statistics."""
        total = self.stats['total_calls']
        success_rate = (self.stats['successful_calls'] / total * 100) if total > 0 else 0
        avg_response_time = (self.stats['total_response_time'] / 
                           max(self.stats['successful_calls'], 1))
        
        return {
            **self.stats,
            'success_rate_percent': round(success_rate, 1),
            'average_retries_per_call': round(self.stats['retries'] / max(total, 1), 2),
            'average_response_time_seconds': round(avg_response_time, 2)
        }

class ClaudeClient(RobustAPIClient):
    """Robust Anthropic Claude API client."""
    
    def __init__(self, api_key: str, max_retries: int = 3, timeout: int = 30):
        super().__init__(api_key, "Claude", max_retries, timeout, max_calls_per_minute=50)
        
        try:
            self.client = anthropic.AsyncAnthropic(api_key=api_key)
        except Exception as e:
            logger.error(f"Failed to initialize Claude client: {e}")
            raise APIError(f"Claude client initialization failed: {e}", "Claude")
    
    async def generate(self, prompt: str, max_tokens: int = 1000, 
                      temperature: float = 0.7, model: str = "claude-3-5-sonnet-20241022") -> str:
        """Generate completion from Claude with robust error handling."""
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string")
        
        if len(prompt) > 200000:  # Claude's context limit
            logger.warning(f"Prompt length {len(prompt)} may exceed Claude's limits")
        
        async def _call():
            response = await self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            if not response.content or len(response.content) == 0:
                raise APIError("Empty response from Claude", "Claude")
            
            return response.content[0].text
        
        return await self._retry_with_backoff(_call)
    
    async def messages_create(self, **kwargs):
        """Direct access to messages.create for compatibility."""
        return await self._retry_with_backoff(self.client.messages.create, **kwargs)

class OpenAIClient(RobustAPIClient):
    """Robust OpenAI API client."""
    
    def __init__(self, api_key: str, max_retries: int = 3, timeout: int = 30):
        super().__init__(api_key, "OpenAI", max_retries, timeout, max_calls_per_minute=60)
        
        try:
            self.client = AsyncOpenAI(api_key=api_key)
            self.chat = self.client.chat  # For compatibility
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise APIError(f"OpenAI client initialization failed: {e}", "OpenAI")
    
    async def generate(self, prompt: str, max_tokens: int = 1500,
                      temperature: float = 0.7, model: str = "gpt-4o") -> str:
        """Generate completion from OpenAI with robust error handling."""
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string")
        
        if len(prompt) > 128000:  # GPT-4's context limit (rough estimate)
            logger.warning(f"Prompt length {len(prompt)} may exceed GPT-4's limits")
        
        async def _call():
            response = await self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            if not response.choices or len(response.choices) == 0:
                raise APIError("Empty response from OpenAI", "OpenAI")
            
            content = response.choices[0].message.content
            if not content:
                raise APIError("Null content in OpenAI response", "OpenAI")
            
            return content
        
        return await self._retry_with_backoff(_call)
    
    async def chat_completions_create(self, **kwargs):
        """Direct access to chat.completions.create for compatibility."""
        return await self._retry_with_backoff(self.client.chat.completions.create, **kwargs)

class MultiProviderLLMClient:
    """Robust multi-provider client with intelligent fallback."""
    
    def __init__(self, providers: Dict[str, RobustAPIClient]):
        self.providers = providers
        self.usage_stats = {name: {'calls': 0, 'errors': 0, 'fallbacks': 0} 
                           for name in providers}
        self.provider_health = {name: 1.0 for name in providers}  # Health scores 0-1
    
    async def generate_with_fallback(self, prompt: str, preferred_provider: str = "claude",
                                   **kwargs) -> Dict[str, Any]:
        """Generate with intelligent fallback based on provider health."""
        # Sort providers by health score, with preferred provider first
        providers_order = sorted(
            self.providers.keys(),
            key=lambda p: (p != preferred_provider, -self.provider_health[p])
        )
        
        last_error = None
        for provider_name in providers_order:
            if provider_name not in self.providers:
                continue
                
            try:
                start_time = time.time()
                result = await self.providers[provider_name].generate(prompt, **kwargs)
                elapsed = time.time() - start_time
                
                # Update success stats
                self.usage_stats[provider_name]['calls'] += 1
                self._update_provider_health(provider_name, success=True, response_time=elapsed)
                
                # Track if we used fallback
                if provider_name != preferred_provider:
                    self.usage_stats[provider_name]['fallbacks'] += 1
                    logger.info(f"Successfully fell back to {provider_name}")
                
                return {
                    "provider": provider_name,
                    "result": result,
                    "elapsed_seconds": elapsed,
                    "was_fallback": provider_name != preferred_provider
                }
                
            except Exception as e:
                last_error = e
                self.usage_stats[provider_name]['errors'] += 1
                self._update_provider_health(provider_name, success=False)
                
                logger.warning(f"Provider {provider_name} failed: {str(e)[:100]}")
                continue
        
        # All providers failed
        raise APIError(f"All providers failed. Last error: {last_error}", "MultiProvider")
    
    def _update_provider_health(self, provider_name: str, success: bool, response_time: float = 0):
        """Update provider health score based on performance."""
        current_health = self.provider_health[provider_name]
        
        if success:
            # Improve health, factor in response time
            time_factor = max(0.5, min(1.0, 10 / max(response_time, 1)))  # Prefer faster responses
            self.provider_health[provider_name] = min(1.0, current_health * 0.95 + 0.05 * time_factor)
        else:
            # Degrade health
            self.provider_health[provider_name] = max(0.1, current_health * 0.8)
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """Get comprehensive usage statistics."""
        stats = {}
        for provider_name, provider in self.providers.items():
            provider_stats = provider.get_stats()
            stats[provider_name] = {
                **provider_stats,
                **self.usage_stats[provider_name],
                'health_score': round(self.provider_health[provider_name], 3)
            }
        return stats
    
    def get_health_report(self) -> str:
        """Get a formatted health report."""
        report = "🏥 PROVIDER HEALTH REPORT\n"
        report += "=" * 30 + "\n"
        
        for provider_name, health in self.provider_health.items():
            status = "🟢" if health > 0.8 else "🟡" if health > 0.5 else "🔴"
            report += f"{status} {provider_name}: {health:.1%} health\n"
        
        return report

# Backwards compatibility aliases
APIClient = RobustAPIClient