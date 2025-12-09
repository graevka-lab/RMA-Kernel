from typing import List, Protocol
import math

class EmbeddingProvider(Protocol):
    def embed(self, text: str) -> List[float]: ...

class DummyEmbeddingProvider:
    """
    Deterministic dummy embeddings for testing.
    Uses character codes to generate a fake vector.
    """
    def embed(self, text: str) -> List[float]:
        # Create a fake 10-dimensional vector based on text content
        seed = sum(ord(c) for c in text)
        vector = [(seed * (i + 1)) % 100 / 100.0 for i in range(10)]
        return self._normalize(vector)

    def _normalize(self, v: List[float]) -> List[float]:
        norm = math.sqrt(sum(x*x for x in v))
        return [x/norm for x in v] if norm > 0 else v

class STEmbeddingProvider:
    """
    Production provider using Sentence-Transformers (HuggingFace).
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        try:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer(model_name)
        except ImportError:
            raise ImportError("Please install sentence-transformers")

    def embed(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()
