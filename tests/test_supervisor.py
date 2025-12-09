import unittest
import sys
import os

# Add project root to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.verifier import Verifier, VerificationResult, CosineDriftMetric
from src.uncertainty import UncertaintyScorer
from src.supervisor import Supervisor
from src.exceptions import MaxIterationsError, DraftRejectedError

# Mocks for testing without real LLM/Embeddings
class MockGenerator:
    def __init__(self, responses):
        self.responses = responses # List of dicts
        self.call_count = 0

    def generate(self, query, instruction=None):
        if self.call_count < len(self.responses):
            resp = self.responses[self.call_count]
            self.call_count += 1
            return resp
        return self.responses[-1]

class MockEmbedder:
    def embed(self, text):
        return [0.1, 0.2, 0.3] # Dummy vector

class TestRMAKernel(unittest.TestCase):
    def setUp(self):
        self.scorer = UncertaintyScorer(max_uncertainty=0.5)
        self.drift = CosineDriftMetric()
        self.verifier = Verifier(self.scorer, self.drift)
        self.supervisor = Supervisor(max_iterations=3)
        self.embedder = MockEmbedder()

    def test_valid_flow(self):
        """Test that a good draft passes immediately."""
        generator = MockGenerator([
            {"output": "Paris is the capital of France.", "uncertainty": 0.1}
        ])
        result = self.supervisor.run("Capital?", generator, self.verifier, self.embedder)
        self.assertEqual(result["output"], "Paris is the capital of France.")

    def test_correction_loop(self):
        """Test that supervisor retries on bad draft."""
        generator = MockGenerator([
            {"output": "I think maybe...", "uncertainty": 0.9}, # Bad
            {"output": "Paris is the capital.", "uncertainty": 0.1} # Good
        ])
        result = self.supervisor.run("Capital?", generator, self.verifier, self.embedder)
        self.assertEqual(result["output"], "Paris is the capital.")
        self.assertEqual(generator.call_count, 2)

    def test_max_iterations(self):
        """Test that it raises error if loop exceeds limit."""
        generator = MockGenerator([
            {"output": "Bad draft", "uncertainty": 0.9},
            {"output": "Bad draft", "uncertainty": 0.9},
            {"output": "Bad draft", "uncertainty": 0.9},
            {"output": "Bad draft", "uncertainty": 0.9}
        ])
        with self.assertRaises(MaxIterationsError):
            self.supervisor.run("Test", generator, self.verifier, self.embedder)

if __name__ == '__main__':
    unittest.main()
