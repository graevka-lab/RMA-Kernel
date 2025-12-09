import math
from typing import Dict

class UncertaintyScorer:
    """
    Computes epistemic uncertainty for LLM drafts.
    Supports lexical heuristics ("maybe", "not sure") and numeric scores.
    """

    LEXICAL_MARKERS = {
        "maybe": 0.15,
        "possibly": 0.20,
        "not sure": 0.30,
        "uncertain": 0.35,
        "i think": 0.10,
        "it seems": 0.12,
        "as an ai": 0.9, # High penalty for boilerplate
        "i cannot": 0.9,
    }

    def __init__(self, max_uncertainty: float = 0.4):
        self.max_uncertainty = max_uncertainty

    def compute(self, draft: Dict) -> float:
        # Case 1: Numeric uncertainty provided by LLM
        if "uncertainty" in draft:
            return self._sanitize(draft["uncertainty"])

        # Case 2: Lexical markers in text
        if "output" in draft:
            return self._lexical_uncertainty(draft["output"])

        return 1.0 # Fallback: assume max uncertainty

    def _sanitize(self, value) -> float:
        try:
            u = float(value)
            return max(0.0, min(u, 1.0))
        except Exception:
            return 1.0

    def _lexical_uncertainty(self, text: str) -> float:
        text_l = text.lower()
        score = 0.0
        for phrase, weight in self.LEXICAL_MARKERS.items():
            if phrase in text_l:
                score = max(score, weight)
        return score
