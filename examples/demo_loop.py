"""
RMA-Kernel: Simulation Loop
Run this script to observe the Supervisor Logic in action.

Usage:
    python examples/demo_loop.py
"""

import sys
import os

# Add project root to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.supervisor import Supervisor
from src.verifier import Verifier, CosineDriftMetric
from src.uncertainty import UncertaintyScorer
from src.generator import DummyGenerator
from src.embedding import DummyEmbeddingProvider

def main():
    print("🚀 RMA-Kernel: System 2 Inference Loop Initialized")
    print("---------------------------------------------------")

    # 1. Setup Components (Using Dummy for instant run without keys)
    generator = DummyGenerator()
    embedder = DummyEmbeddingProvider()
    
    scorer = UncertaintyScorer(max_uncertainty=0.4)
    drift_metric = CosineDriftMetric()
    
    verifier = Verifier(
        uncertainty_scorer=scorer,
        drift_metric=drift_metric,
        drift_threshold=0.2
    )

    supervisor = Supervisor(max_iterations=5)

    # 2. Run Loop
    query = "What is the ultimate answer?"
    print(f"\nUSER QUERY: '{query}'")
    print("---------------------------------------------------")

    try:
        final_result = supervisor.run(
            query=query,
            generator=generator,
            verifier=verifier,
            embedder=embedder
        )
        
        print("\n✅ FINAL OUTPUT RELEASED:")
        print(f"   {final_result['output']}")
        print(f"   (Uncertainty: {final_result.get('uncertainty', 0.0)})")

    except Exception as e:
        print(f"\n❌ PROCESS TERMINATED: {e}")

if __name__ == "__main__":
    main()
