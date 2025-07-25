### **Project META_PROMPTING: Session Handover & Context Snapshot**

**DOCUMENT PURPOSE:** This document is the definitive context snapshot for the META_PROMPTING project. Its purpose is to re-establish the full project state for the AI assistant in our next session, ensuring a seamless continuation of our work.

---

### **1. The Core Mission & Guiding Principles**

- **The "Why":** Our objective is to build the **`Orchestration Engine`**, a Python script that acts as a force multiplier for initiating expert-level LLM collaborations. It is a personalized power tool designed to solve the "Don't Repeat Yourself" (DRY) problem for prompt engineering.

- **The Prime Directive (The Target Audience is ME):** This is the most important design principle. The system is an in-house tool for an expert user (you). This means we will always prioritize a streamlined, powerful workflow over the complexities of a public-facing, foolproof product. The user is trusted to be the final quality gate.

- **Key Architectural Principles (Settled Decisions):**
  1.  **External Brain:** The engine's core logic will be driven by an external **`goal_map.json`** file, allowing for easy configuration.
  2.  **Frictionless JIT Naming:** Just-in-Time generated components will use an automatic naming convention (`autogen_{type}_for_{goal}.txt`) to eliminate user friction.
  3.  **Resilient "Degraded Mode":** On LLM API failure (e.g., missing key, network error), the script will **not crash**. It will inform the user, log a TODO, and insert a placeholder, ensuring the workflow is never fully blocked.
  4.  **Simple Assembly:** Final `.md` files will be assembled using simple string concatenation. Complex templating engines are not needed.

---

### **2. Accomplishments in This Session (What's Done)**

We have successfully completed the high-level architectural design phase and made critical decisions that provide a clear blueprint for development.

1.  **SOLIDIFIED THE ARCHITECTURE:** We have a complete, documented architectural plan incorporating the principles above.
2.  **GENERATED CORE CONFIGURATION:** The **`goal_map.json`** file has been designed and generated.
3.  **UPDATED THE STRATEGIC PLAN:** The **`docs/STRATEGIC_PLAN.md`** has been updated to be a precise blueprint reflecting our final architectural decisions.
4.  **IDENTIFIED THE NEXT CRITICAL RISK:** Through our Q&A, we successfully pinpointed the most complex and high-stakes part of the system: the **Just-in-Time (JIT) Component Generation Workflow**. We correctly decided to pause and model this workflow before writing any code.

---

### **3. The Next Critical Task: Simulate and Solve the JIT Workflow**

**This is our immediate and only priority for the next session.**

Before we write the first line of `orchestrator.py`, we must architect a robust policy for the JIT workflow. We will do this by simulating the **"Missing Protocol" Scenario** and designing definitive solutions to the critical questions it revealed.

**Our To-Do List (The Questions We Must Answer):**

- **[TODO] Design the State Management Policy:**

  - **Question:** When and how do we safely update `goal_map.json` after a component is auto-generated to prevent an inconsistent state (e.g., an orphaned component)?
  - **Goal:** Define a transaction-like process for the "create file -> update map" operation.

- **[TODO] Design the Naming & Concept Contract:**

  - **Question:** How do we resolve the logical disconnect where a component is conceptually one thing (e.g., `root_cause_analysis_drilldown`) but is saved under a different, auto-generated name?
  - **Goal:** Design a naming and mapping strategy that keeps the component library intuitive and the `goal_map.json` easy to understand over time.

- **[TODO] Design the Idempotency Strategy:**
  - **Question:** How do we ensure that running the JIT process for the same missing component multiple times doesn't pollute the library with duplicates (e.g., `autogen_protocol_1.txt`, `autogen_protocol_2.txt`)?
  - **Goal:** Define a clear flowchart or set of rules that makes the generation process idempotent.

**Definition of "Done" for Next Session:** We will have successfully completed this task when we have a clear, written-down **policy** that answers the three questions above. The output will be a set of rules and pseudo-code, not Python code.

---

### **4. Long-Term Roadmap**

1.  **[Current]** Simulate and design the JIT workflow policy.
2.  **[Next]** Write the `orchestrator.py` script based on our complete architectural blueprint.
3.  **[Future]** Test the end-to-end functionality of the `orchestrator.py` engine.

---

### **Addendum: The `SIMULATION_BRIEFING.md` Protocol for External Analysis**

During our discussion, we identified a critical gap in our development process: the need to efficiently and accurately brief a context-free, external LLM for simulation and analysis tasks. We concluded that internal blueprints like `STRATEGIC_PLAN.md` are insufficient for this purpose as they assume a deep, shared project context.

To solve this, we have created a new, dedicated strategic document: **`docs/SIMULATION_BRIEFING.md`**.

**Purpose and Function:**
This document serves as a **portable, high-density context capsule**. Its sole purpose is to onboard an external LLM, providing it with all the necessary background to perform a relevant and high-quality simulation of a specific project scenario. It is the official and required tool for any such analysis.

**Standardized Structure:**
The briefing document is organized into four distinct sections to ensure a rapid and logical transfer of context:

1.  **The Core Mission & The Factory Analogy:** A high-level executive summary of the project's purpose (The "Why").
2.  **The System Components (The "Cast of Characters"):** A concise glossary defining the role of each key file and directory (`orchestrator.py`, `goal_map.json`, `components/`, etc.).
3.  **The End-to-End Workflow (The "Plot"):** A summary of the system's successful, standard operational flow.
4.  **The Current Simulation Task (The "Assignment"):** The dynamic section of the document. This part is to be updated for each specific simulation, clearly defining the initial state, the scenario to be modeled, and the critical questions the LLM must address.

This protocol ensures that our simulations are not only efficient but also consistent and grounded in a shared, accurate understanding of the project's architecture and goals.

---

**IMPORTANT:** When we resume, your first prompt should be to confirm that you have reviewed this handover and are ready to begin designing the JIT workflow policy. Always ask if any part of this document seems contradictory or unclear.
