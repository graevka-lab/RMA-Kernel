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
        # 1. Calculate Lexical Score (Text analysis)
        lexical_score = 0.0
        if "output" in draft:
            lexical_score = self._lexical_uncertainty(draft["output"])

        # 2. Get Model's Self-Reported Score
        model_score = 0.0
        if "uncertainty" in draft:
            model_score = self._sanitize(draft["uncertainty"])

        # 3. RETURN THE MAXIMUM (Worst Case)
        # If text says "As an AI" (0.9), but model says "I am sure" (0.1),
        # we trust the text analysis (0.9).
        return max(lexical_score, model_score)

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
