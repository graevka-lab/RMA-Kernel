"""
RMA-Kernel Package
Recursive Metacognitive Alignment for Large Language Models.
"""

from .supervisor import Supervisor
from .verifier import Verifier
from .generator import OpenAIGenerator, DummyGenerator
from .embedding import STEmbeddingProvider, DummyEmbeddingProvider

__version__ = "1.0.0-alpha"
__author__ = "Graevka Lab"
__license__ = "AGPL-3.0"

__all__ = [
    "Supervisor",
    "Verifier",
    "OpenAIGenerator",
    "DummyGenerator",
    "STEmbeddingProvider",
    "DummyEmbeddingProvider"
]
