"""
API Clients for Claude and OpenAI
Provides unified interface with error handling and retry logic.
"""

import os
import asyncio
import json
from typing import Dict, Any, Optional, List
import time
import anthropic
import openai
from openai import AsyncOpenAI

class APIClient:
    """Base API client with common functionality."""
    
    def __init__(self, api_key: str, max_retries: int = 3, timeout: int = 30):
        self.api_key = api_key
        self.max_retries = max_retries
        self.timeout = timeout
    
    async def _retry_with_backoff(self, func, *args, **kwargs):
        """Retry function with exponential backoff."""
        for attempt in range(self.max_retries):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise
                wait_time = 2 ** attempt
                print(f"⚠️ API call failed, retrying in {wait_time}s... Error: {str(e)}")
                await asyncio.sleep(wait_time)

class ClaudeClient(APIClient):
    """Anthropic Claude API client."""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
    
    async def generate(self, prompt: str, max_tokens: int = 1000, 
                      temperature: float = 0.7, model: str = "claude-3-5-sonnet-20241022") -> str:
        """Generate completion from Claude."""
        async def _call():
            response = await self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        
        return await self._retry_with_backoff(_call)
    
    async def messages_create(self, **kwargs):
        """Direct access to messages.create for compatibility."""
        return await self._retry_with_backoff(self.client.messages.create, **kwargs)

class OpenAIClient(APIClient):
    """OpenAI API client."""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = AsyncOpenAI(api_key=api_key)
        self.chat = self.client.chat  # For compatibility
    
    async def generate(self, prompt: str, max_tokens: int = 1500,
                      temperature: float = 0.7, model: str = "gpt-4o") -> str:
        """Generate completion from OpenAI."""
        async def _call():
            response = await self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        
        return await self._retry_with_backoff(_call)
    
    async def chat_completions_create(self, **kwargs):
        """Direct access to chat.completions.create for compatibility."""
        return await self._retry_with_backoff(self.client.chat.completions.create, **kwargs)

# Multi-provider client for fallback support
class MultiProviderLLMClient:
    """Client that can fall back between providers."""
    
    def __init__(self, providers: Dict[str, APIClient]):
        self.providers = providers
        self.usage_stats = {name: {'calls': 0, 'errors': 0} for name in providers}
    
    async def generate_with_fallback(self, prompt: str, preferred_provider: str = "claude",
                                   **kwargs) -> Dict[str, Any]:
        """Generate with fallback to other providers if needed."""
        providers_order = [preferred_provider] + [p for p in self.providers if p != preferred_provider]
        
        for provider_name in providers_order:
            if provider_name not in self.providers:
                continue
                
            try:
                start_time = time.time()
                result = await self.providers[provider_name].generate(prompt, **kwargs)
                elapsed = time.time() - start_time
                
                self.usage_stats[provider_name]['calls'] += 1
                
                return {
                    "provider": provider_name,
                    "result": result,
                    "elapsed_seconds": elapsed
                }
            except Exception as e:
                self.usage_stats[provider_name]['errors'] += 1
                print(f"Provider {provider_name} failed: {e}")
                continue
        
        raise Exception("All providers failed")
    
    def get_usage_stats(self) -> Dict[str, Dict[str, int]]:
        """Get usage statistics for all providers."""
        return self.usage_stats