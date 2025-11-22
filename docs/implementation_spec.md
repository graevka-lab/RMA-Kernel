# RMA-Kernel: Technical Implementation Specification

> **Recursive Metacognitive Alignment (RMA)**
> Architectural data flow analysis: How the Supervisor Kernel intercepts and rectifies stochastic generation.

---

## Level 1: The Control Loop (High Level)

At the abstract level, RMA introduces a feedback loop into the standard linear generation process.

```mermaid
graph TD
    subgraph "RMA Control Loop"
        A[User Query] --> B(Supervisor_Kernel)
        B --> C{Constraint_Check}
        C -- "Violation" --> B
        C -- "Pass" --> D(Token_Emission)
        D --> E((User))
    end

    style B fill:#e1f5fe,stroke:#01579b,color:#000
    style C fill:#fff9c4,stroke:#fbc02d,color:#000
    style D fill:#f1f8e9,stroke:#33691e,color:#000
```
> **Supervisor_Kernel:** The virtualized meta-process holding the Immutable Anchor.
> **Constraint_Check:** Binary evaluation of the draft against the Charter.
> **Token_Emission:** Release of verified tokens to the output stream.

---

## Level 2: Component Architecture
Detailed view of the "Split-Brain" processing (System 1 Generator vs. System 2 Supervisor).

```mermaid
graph TD
    subgraph "Ingestion Layer"
        A["External Input"] --> B["Tokenization"]
        B --> C["Context Window Parsing"]
    end

    subgraph "Processing Core"
        C --> D{Supervisor_Kernel}
        D -- "Oversight" --> E["Analytic Layer\n(Logic & Facts)"]
        D -- "Oversight" --> F["Heuristic Layer\n(Pattern Matching)"]
        E --> G["Conflict Resolution"]
        F --> G
    end

    subgraph "Output Layer"
        G --> H{Gating Mechanism}
        H --> I["Generator / Draft"]
        I --> J((User Interface))
        I -- "Error Signal" --> H
    end

    classDef core fill:#e6ecf0,stroke:#333,color:#000
    classDef logic fill:#e8f5e9,stroke:#333,color:#000
    classDef heuristic fill:#e3f2fd,stroke:#333,color:#000
    classDef gate fill:#fff3e0,stroke:#333,color:#000

    class D core
    class E logic
    class F heuristic
    class H gate
```
> **Supervisor_Kernel:** Maintains state coherence (The Anchor).
> **Analytic Layer:** Verifies factual consistency.
> **Heuristic Layer:** Checks for semantic drift and hallucination patterns.
> **Gating Mechanism:** Decides whether to release the draft or trigger a retry.

---

## Level 3: Data Flow & Attention Weighting
How information (Entropy) moves through the system.

```mermaid
graph TD
    A["User Query"] --> B["Tokens\n(Attention Masking)"]
    B --> C["Filtering\n(Anchor Hashing)"]
    C --> D{Supervisor_Kernel}

    D -- "Weight Distribution" --> E["Analytic Layer\n(Fact Verification)"]
    D -- "Weight Distribution" --> F["Heuristic Layer\n(Tone & Safety)"]

    E --> G["State Synthesis\n(Resolves Logic Conflicts)"]
    F --> G

    G --> H{Gating Mechanism}
    H --> I["Draft Generation\n(Pre-computation)"]
    I -- "Negative Feedback" --> H
    H -- "State Update" --> D
    I --> J((Final Output))
```
### Technical Annotations

*   **Supervisor_Kernel Functions:**
    *   **State Locking:** Prevents context drift by refreshing the Anchor hash.
    *   **Entropy Reduction:** Minimizes the search space for the Generator.
    *   **Recursion:** Re-feeds output back into input for verification (Chain-of-Thought).

*   **Gating Mechanism:**
    *   Acts as a **Firewall**. If `Risk_Score > Threshold`, the gate closes, and the `Error_Signal` forces a regeneration cycle.

---

## ✴️ Topology of Latent Space
The RMA architecture is not just a set of rules; it is a method for **Topological Constraint**.
By injecting the Supervisor Kernel, we alter the geometry of the model's latent space, creating "Attractor Basins" (Safe States) where the model naturally settles, making hallucination energetically expensive (high perplexity) and accuracy energetically cheap.

**Engineering Note:** This diagram represents the logical flow of the supervisor.py reference implementation.
