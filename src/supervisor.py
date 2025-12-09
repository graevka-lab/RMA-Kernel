"""
RMA Kernel: Supervisor Logic Implementation
Core logic for the Recursive Metacognitive Alignment framework.
"""

from typing import Any, Dict, Protocol
from .verifier import Verifier
from .exceptions import MaxIterationsError, DraftRejectedError

class DraftGenerator(Protocol):
    def generate(self, query: str, instruction: str | None = None) -> Dict[str, Any]: ...

class EmbeddingProvider(Protocol):
    def embed(self, text: str) -> list[float]: ...

class Supervisor:
    def __init__(self, max_iterations: int = 5):
        self.max_iterations = max_iterations

    def run(self, query: str, generator: DraftGenerator, verifier: Verifier, embedder: EmbeddingProvider) -> Dict[str, Any]:
        query_embedding = embedder.embed(query)
        instruction = None

        for i in range(self.max_iterations):
            print(f"   [Supervisor] Cycle {i+1}/{self.max_iterations}...")
            
            # 1. Generate
            draft = generator.generate(query, instruction)
            
            # 2. Embed Draft
            draft_text = draft.get("output", "")
            draft_embedding = embedder.embed(draft_text)

            # 3. Verify
            result = verifier.verify(draft, query_embedding, draft_embedding)

            if result.fatal:
                raise DraftRejectedError(f"Fatal error: {result.reason}")

            if result.is_valid:
                return draft
            
            # 4. Correct
            print(f"   [Supervisor] Rejected: {result.reason}. Correcting...")
            instruction = result.corrected_instruction

        raise MaxIterationsError("Exceeded max iterations without convergence.")
