"""
RMA Kernel: Supervisor Logic Implementation
Core logic for the Recursive Metacognitive Alignment framework.
"""

import re
from typing import List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class CharterRule:
    """
    Defines a specific constraint for the Supervisor to enforce.
    """
    rule_id: str
    description: str
    threshold: float = 0.5

@dataclass
class AnalysisResult:
    """
    Internal object to pass analysis state.
    """
    is_compliant: bool
    reason: str
    confidence_score: float

class SupervisorAgent:
    """
    The logic core. Acts as the 'System 2' oversight layer.
    """
    
    def __init__(self, rules: List[CharterRule], strict_mode: bool = True):
        self.rules = rules
        self.strict_mode = strict_mode
        
        # Regex patterns that suggest the model is hallucinating, hedging, 
        # or falling into "Safety Refusal" mode instead of helpful debugging.
        self.uncertainty_patterns = [
            # Epistemic Hedging (Guessing)
            r"i think", 
            r"maybe", 
            r"possibly", 
            r"to the best of my knowledge",
            
            # Filler / Fluff
            r"it is important to note",
            r"in conclusion",
            
            # "Lazy" Refusals / Boilerplate
            r"as an ai language model",
            r"i cannot fulfill",
            r"i am unable to",
            r"it is not appropriate to"
        ]

    def evaluate_trace(self, input_prompt: str, draft_text: str) -> bool:
        """
        Main entry point for the Supervisor Loop.
        Returns True if compliant, False if rejected.
        """
        analysis = self._scan_draft(draft_text)
        return analysis.is_compliant

    def _scan_draft(self, draft_text: str) -> AnalysisResult:
        """
        Static analysis of the draft (Heuristic Layer).
        """
        # 1. Structure Check
        if len(draft_text) < 10:
             return AnalysisResult(False, "Output too short / Empty response", 0.0)

        # 2. Heuristic Check (Regex)
        for pattern in self.uncertainty_patterns:
            if re.search(pattern, draft_text, re.IGNORECASE):
                return AnalysisResult(
                    is_compliant=False, 
                    reason=f"Detected low-quality pattern: '{pattern}'",
                    confidence_score=0.5
                )

        # 3. Charter Rule Check (Placeholder for Semantic Similarity)
        # In a full implementation, we would compare embeddings here.
        
        return AnalysisResult(True, "Heuristics passed", 1.0)

    def construct_retry_prompt(self, original_prompt: str, failure_reason: str) -> str:
        """
        Constructs the refinement prompt for the Generator (System 2 Instruction).
        """
        return (
            f"SYSTEM_OVERRIDE: The previous output was rejected via RMA-Protocol.\n"
            f"ERROR_LOG: {failure_reason}\n"
            f"INSTRUCTION: Rewrite the response. \n"
            f"1. Remove boilerplate ('As an AI...').\n"
            f"2. Remove speculation ('Maybe...').\n"
            f"3. If data is missing, output explicit NULL or UNKNOWN tag.\n"
            f"ORIGINAL QUERY: {original_prompt}"
        )
