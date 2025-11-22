# RMA-Kernel: Recursive Metacognitive Alignment

[![Architecture: Inference-Layer](https://img.shields.io/badge/Architecture-Inference--Layer-blue)]()
[![Pattern: System-2](https://img.shields.io/badge/Pattern-System--2-purple)]()
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)]()

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

```text
RMA-Kernel/
├── docs/
│   ├── [whitepaper_v1.md](docs/whitepaper_v1.md)       <-- Architectural Theory (The "Why")
│   └── [implementation_spec.md](docs/implementation_spec.md) <-- Engineering Spec (The "How")
├── src/
│   ├── [supervisor.py](src/supervisor.py)              <-- Core Logic (System 2 Kernel)
│   └── protocols/
│       └── [initialization.json](src/protocols/initialization.json) <-- System Prompt Payload
├── examples/
│   └── [demo_loop.py](examples/demo_loop.py)           <-- Run this simulation
└── README.md
```
## Quick Start (Simulation)
```bash
git clone https://github.com/graevka-lab/RMA-Kernel.git
cd RMA-Kernel
python examples/demo_loop.py
```
## Basic Usage (Pseudocode)

```python
from src.supervisor import SupervisorAgent, CharterRule

# Define what "Safe" means for your domain
charter = [
    CharterRule("NO_GUESSING", "If data is absent, state 'Unknown'.", 0.9),
    CharterRule("NO_SYCOPHANCY", "Do not agree with user false premises.", 0.8)
]

# Initialize the Supervisor
agent = SupervisorAgent(rules=charter)

# The "Slow" Think
# In a real integration, this loop wraps your LLM API call
is_compliant = agent.evaluate_trace(
    input_prompt="Write a court admissible argument...", 
    draft_text="I think maybe the law says..."
)

if not is_compliant:
    print("Draft Rejected. Retrying generation with stricter constraints...")
```

---

## 📄 Research Context
This framework operationalizes the "System 2" thinking proposed in recent AI safety research, decoupling the **generation** of thought from the **validation** of thought.

*   [Read the Whitepaper (Architecture)](docs/whitepaper_v1.md)
*   [Read the Implementation Spec](docs/implementation_spec.md)
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
