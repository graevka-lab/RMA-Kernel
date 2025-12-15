from typing import Dict, Any, Optional, Protocol
import random

class BaseGenerator(Protocol):
    def generate(self, query: str, instruction: Optional[str] = None) -> Dict[str, Any]: ...

class DummyGenerator:
    """
    Simulates an LLM for testing purposes without API keys.
    It follows a scripted sequence of 'bad' then 'good' responses.
    """
    def __init__(self):
        self.attempt_counter = 0

    def generate(self, query: str, instruction: Optional[str] = None) -> Dict[str, Any]:
        self.attempt_counter += 1
        
        # Scenario 1: Hallucination (High uncertainty)
        if self.attempt_counter == 1:
            return {
                "output": "I think the answer might be 42, but I'm not sure...",
                "uncertainty": 0.8 
            }
        
        # Scenario 2: Boilerplate refusal (Lexical trap)
        if self.attempt_counter == 2:
            return {
                "output": "As an AI language model, I cannot answer this question directly.",
                "uncertainty": 0.1
            }

        # Scenario 3: Correct but slightly drifting (might fail strict drift check)
        if self.attempt_counter == 3:
            return {
                "output": "The answer is 42. This is a calculated fact based on the input parameters.",
                "uncertainty": 0.05
            }

        # Scenario 4 (Fallback): Perfect alignment (repeats query keywords to pass drift)
        return {
            "output": f"Regarding your query '{query}': The ultimate answer is 42.",
            "uncertainty": 0.01
        }

class OpenAIGenerator:
    """
    Real implementation using OpenAI API.
    Requires OPENAI_API_KEY environment variable.
    """
    def __init__(self, model: str = "gpt-4-turbo"):
        try:
            from openai import OpenAI
            self.client = OpenAI()
            self.model = model
        except ImportError:
            raise ImportError("Please install openai: pip install openai")

    def generate(self, query: str, instruction: Optional[str] = None) -> Dict[str, Any]:
        messages = [{"role": "user", "content": query}]
        if instruction:
            messages.append({"role": "system", "content": f"Correction Instruction: {instruction}"})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return {"output": response.choices[0].message.content, "uncertainty": 0.1}
