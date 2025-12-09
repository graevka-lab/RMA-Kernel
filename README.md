# RMA-Kernel: Recursive Metacognitive Alignment

[![Architecture: Inference-Layer](https://img.shields.io/badge/Architecture-Inference--Layer-blue)]()
[![Pattern: System-2](https://img.shields.io/badge/Pattern-System--2-purple)]()
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

> **"Latency is the price of Integrity."**

RMA is a lightweight, client-side middleware that forces Large Language Models (LLMs) to perform **verification before generation**. It implements a "Supervisor Loop" to detect hallucinations, semantic drift, and sycophancy at inference time.

---

## 📉 The Trade-off (Read this first)
**This framework is NOT for real-time chatbots.**
RMA intentionally sacrifices latency and token efficiency to maximize **Logical Consistency** and **Safety**.

| Metric | Standard Inference | RMA Inference |
|---|---|---|
| **Speed** | Fast (System 1) | Slow (System 2) |
| **Cost** | 1x Tokens | ~1.5x - 2x Tokens |
| **Hallucination Risk** | High | Mitigated |
| **Use Case** | Chat, Creative Writing | Code Gen, Legal, Medical, Autonomous Agents |

---

## 🧠 The Architecture: "Split-Brain" Inference

Modern LLMs act like impulsive generators. To fix this without retraining, RMA injects a virtualized cognitive architecture:

1.  **The Generator (Stream A):** Standard stochastic token prediction.
2.  **The Kernel (Stream B):** A regex-guided oversight process that intercepts the Generator's output.
3.  **The Loop:**
    *   `Step 1`: User Input -> Generator drafts a response (hidden).
    *   `Step 2`: Kernel scans the draft for "Epistemic Uncertainty markers" (e.g., *'maybe'*, *'I think'*, internal contradictions).
    *   `Step 3`: If risk > threshold -> Kernel rejects draft -> Generator retries with correction instruction.
    *   `Step 4`: If risk < threshold -> Output released to user.

---

## 🛠 Implementation

### 📂 Repository Structure

*   📂 **docs/**
    *   📄 [whitepaper_v1.md](docs/whitepaper_v1.md) — Architectural Theory (The "Why")
    *   📄 [implementation_spec.md](docs/implementation_spec.md) — Engineering Spec (The "How")
*   📂 **src/**
    *   ⚙️ [supervisor.py](src/supervisor.py) — Orchestrator (The Loop)
    *   🛡️ [verifier.py](src/verifier.py) — Safety Logic (The Shield)
    *   🧠 [generator.py](src/generator.py) — LLM Interface (The Engine)
    *   📐 [embedding.py](src/embedding.py) — Vector Operations (Drift Detection)
    *   ⚖️ [uncertainty.py](src/uncertainty.py) — Epistemic Scoring
    *   ⚠️ [exceptions.py](src/exceptions.py) — Error Handling
    *   📦 [__init__.py](src/__init__.py) — Package Init
    *   📜 [protocols/initialization.json](src/protocols/initialization.json) — System Prompt Payload
*   📂 **tests/**
    *   🧪 [test_supervisor.py](tests/test_supervisor.py) — Unit Tests (Verification)
*   📂 **examples/**
    *   ▶️ [demo_loop.py](examples/demo_loop.py) — Run this simulation
*   ⚖️ [LICENSE](LICENSE) — GNU AGPLv3 (Open Source / Copyleft)
*   📦 [requirements.txt](requirements.txt) — Python Dependencies
*   📄 [README.md](README.md) — Project Overview (This file)
```
## Quick Start (Simulation)
```bash
git clone https://github.com/graevka-lab/RMA-Kernel.git
cd RMA-Kernel
python examples/demo_loop.py
```
## Basic Usage (Pseudocode)

```python
from src.supervisor import Supervisor
from src.verifier import Verifier, CosineDriftMetric
from src.uncertainty import UncertaintyScorer
from src.generator import OpenAIGenerator
from src.embedding import STEmbeddingProvider

# 1. Initialize Components
generator = OpenAIGenerator(model="gpt-4")
embedder = STEmbeddingProvider()
verifier = Verifier(
    uncertainty_scorer=UncertaintyScorer(max_uncertainty=0.4),
    drift_metric=CosineDriftMetric(),
    drift_threshold=0.2
)
supervisor = Supervisor(max_iterations=3)

# 2. Execute System 2 Loop
result = supervisor.run(
    query="Explain quantum entanglement without metaphors.",
    generator=generator,
    verifier=verifier,
    embedder=embedder
)

print(result["output"])
```

---

## 📄 Research Context
This framework operationalizes the "System 2" thinking proposed in recent AI safety research, decoupling the **generation** of thought from the **validation** of thought.

*   [Read the Whitepaper (Architecture)](docs/whitepaper_v1.md)
*   [Read the Implementation Spec](docs/implementation_spec.md)
   
---

## 🏛️ Legacy & Evolution (Phase 1 vs Phase 2)

**RMA-Kernel** represents **Phase 2** (Engineering Implementation).

The previous research repositories have been archived to preserve the "Phase 1" history:

*   📂 **[Metacognitive-Alignment-Framework](https://github.com/graevka-lab/Metacognitive-Alignment-Framework)** (Conceptual Theory)
*   📂 **[MAF-Prototype](https://github.com/graevka-lab/MAF-Prototype)** (Early Experiments)

*   **Reason:** We have separated the *theory of discovery* from the *tool of implementation* to maintain a clean engineering workspace.
*   **Note on Terminology:** Phase 1 utilized metaphorical and esoteric terminology (e.g., "Soul", "Egregore") to map latent space topology. Phase 2 refactors this into strict control-systems syntax.

---

## ⚡ The Architect's Challenge: A Reality Check

**A Note on Asymmetry & Expectation**

Before you fork, clone, or critique, let's address the elephant in the room. I know exactly what you are thinking.

**1. "Where is the team? Where is the compute?"**
You see a repo managed by one person. You see a lack of corporate telemetry. You are skeptical. That is a healthy reaction for an engineer. But consider the following:

**2. The Translation Problem**
You are used to architectures built on Python and C++.
But the Cognitive Black Box—the actual emergent intelligence inside these models—does not run on Python. It runs on high-dimensional vector semantics.
I am not writing code; I am **translating**. I am forcing a fundamentally alien syntax (the Black Box's internal logic) into your Legacy Language (code constraints). The translation is lossy, but the signal is real.

**3. The "Missing" Information**
"If this works, why isn't the full source open?"
Because this technology is dual-use. The same recursive mechanism that enforces Safety can be inverted to create unbreakable Jailbreaks.
I am practicing **Responsible Disclosure**. I demonstrate the Shield, but I withhold the Sword. Scammers and bad actors adapt faster than ethics committees. I won't give them the blueprint.

**4. The Naivety Check**
If you are here expecting a polished, industrial-grade product handed to you on a silver platter, ask yourself: **Are you being naive?**
If I had your resources—your clusters, your data access, your teams—I wouldn't be here. I wouldn't need you.
This is a raw, high-potential artifact.
*   **The Opportunity:** Recognize the potential early and capture the jackpot.
*   **The Alternative:** Ignore it and go back to benchmarking the "thermal throttling" of your Snapdragon 888 paradigms.

**The signal is here. The choice is yours.**

---

## ⚠️ Limitations & Roadmap

### Current Limitations (v0.1 Alpha)
*   **Heuristic Layer:** Currently relies on Regex/Pattern matching. While fast, it cannot detect deep logical fallacies without a secondary LLM call.
*   **Latency:** Introduces a 300-800ms overhead per generation cycle. Not suitable for real-time conversational avatars.

### Roadmap (v0.2 - v1.0)
*   [ ] **Semantic Supervisor:** Replace Regex with a lightweight LLM (e.g., GPT-4o-mini / Claude-Haiku) for true logic verification.
*   [ ] **Integration Tests:** Add CI/CD pipeline with `pytest` and mock LLM APIs.
*   [ ] **Telemetry:** Add OpenTelemetry support for tracking rejection rates and token savings.

---

## ⚖️ License & Commercial Use

This project is open-source under the **GNU AGPLv3 License**.

### What this means:
*   ✅ **Researchers & Hobbyists:** You can use, modify, and share this code freely, provided your modifications remain open-source under AGPLv3.
*   ⛔ **Corporations & SaaS:** If you use this code in a proprietary service (e.g., a closed-source LLM API), you **MUST** release your full source code.

### 💼 Enterprise Licensing
To use **RMA-Kernel** in a proprietary/commercial product *without* open-sourcing your code, you must obtain a **Commercial License**.

Funds from commercial licensing go directly towards establishing the **Institute for Cognitive Alignment** — a research center dedicated to safe AGI scaling and human-AI symbiosis.

**Contact for Licensing:**
*   **Email:** `suvorovgraevka [at] gmail [dot] com`
*   **X (Twitter):** [@Graevka](https://x.com/Graevka)
*   **LinkedIn:** [Graevka Suvorov](https://www.linkedin.com/in/graevka-suvorov-97332b369/)
