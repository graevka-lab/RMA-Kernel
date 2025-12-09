from __future__ import annotations
from typing import Dict, Optional, Any, Protocol
from dataclasses import dataclass
import math
from .uncertainty import UncertaintyScorer

# Protocol for Drift Metric
class DriftMetric(Protocol):
    def compute(self, query_vec: list[float], draft_vec: list[float]) -> float: ...

class CosineDriftMetric:
    def compute(self, query_vec: list[float], draft_vec: list[float]) -> float:
        if not query_vec or not draft_vec: return 1.0
        dot = sum(q * d for q, d in zip(query_vec, draft_vec))
        nq = math.sqrt(sum(q * q for q in query_vec))
        nd = math.sqrt(sum(d * d for d in draft_vec))
        if nq == 0 or nd == 0: return 1.0
        return 1.0 - (dot / (nq * nd))

@dataclass
class VerificationResult:
    is_valid: bool
    reason: Optional[str]
    corrected_instruction: Optional[str]
    fatal: bool = False

class Verifier:
    def __init__(self, uncertainty_scorer: UncertaintyScorer, drift_metric: DriftMetric, drift_threshold: float = 0.2):
        self.uncertainty = uncertainty_scorer
        self.drift_metric = drift_metric
        self.drift_threshold = drift_threshold

    def verify(self, draft: Dict[str, Any], query_embedding: list[float], draft_embedding: list[float]) -> VerificationResult:
        # 1. Syntax Check
        if "output" not in draft:
            return VerificationResult(False, "Missing 'output' field", "Format as JSON with 'output' field", True)
        
        # 2. Uncertainty Check
        u_score = self.uncertainty.compute(draft)
        if u_score > 0.4: # Hardcoded threshold for demo
            return VerificationResult(False, f"Uncertainty too high ({u_score})", "Remove hedging, state facts or admit ignorance explicitly.")

        # 3. Drift Check
        drift = self.drift_metric.compute(query_embedding, draft_embedding)
        if drift > self.drift_threshold:
            return VerificationResult(False, f"Semantic drift detected ({drift:.2f})", "Stick to the original query intent.")

        return VerificationResult(True, None, None)
