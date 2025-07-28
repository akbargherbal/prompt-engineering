**IMPORTANT: LEGACY (PRE-v1.0) & OUT-OF-DATE SIMULATION BRIEFINGS — IGNORE UNTIL FURTHER NOTICE**

# META_PROMPTING: Simulation & Analysis Briefing

**DOCUMENT PURPOSE:** This document is a comprehensive, self-contained briefing for a Large Language Model tasked with running a simulation related to the META_PROMPTING project. Its goal is to establish the necessary context for a high-quality, relevant analysis in a minimal amount of time.

---

### **1. The Core Mission: A "Robotic Kitchen Assistant"**

Imagine you're a world-class chef. Before you can cook, you spend an hour meticulously preparing your kitchen: laying out the right knives, grabbing specific spices, and setting the game plan. This setup is critical, but it's repetitive.

The META_PROMPTING project builds a **"Robotic Kitchen Assistant"** (`orchestrator.py`) that does this entire setup for you in seconds. You tell it what you want to "cook" (your primary goal), and it prepares the entire workstation perfectly by assembling pre-made components into a final, ready-to-use toolkit (`00_PERSONA.md` and `01_PROMPT_TEMPLATE.md`).

The core philosophy is "Don't Repeat Yourself" (DRY) for expert-level prompt engineering.

---

### **2. The System Components (The "Cast of Characters")**

To understand the system, you must know its parts:

- **`orchestrator.py` (The Foreman):** The main Python script. It is an interactive wizard that talks to the user and manages the entire assembly process.

- **`goal_map.json` (The Recipe Book):** A JSON file that tells the foreman which parts to use for which job. It maps a high-level goal like "AUDIT" to specific part numbers (filenames).

- **`components/` (The Parts Bin):** A directory containing the raw materials (text snippets). It is organized into three sub-directories:

  - `personas/`: Defines the LLM's role and tone.
  - `protocols/`: Defines the rules of interaction.
  - `constraints/`: Defines non-negotiable rules.

- **`output/` (The Loading Dock):** The directory where the final, assembled toolkits are placed, each in its own project folder.

---

### **3. The End-to-End Workflow (The "Plot")**

A successful workflow proceeds as follows:

1.  The user runs `python orchestrator.py`.
2.  The script asks for a project name and a primary goal.
3.  The script reads `goal_map.json` to find the recommended parts for that goal.
4.  It checks if all the required parts exist in the `components/` directory.
5.  Assuming they all exist, it reads their text content.
6.  It assembles this content into two final Markdown files (`00_PERSONA.md`, `01_PROMPT_TEMPLATE.md`).
7.  It creates a new directory in `output/` and saves the two final files there.

---

### **4. The Current Simulation Task (Your Assignment)**

**[This section must be updated for each specific simulation.]**

This is where the standard workflow is to be tested or a new feature is to be analyzed. You must clearly define the scenario for the simulation LLM.

- **Initial State:** Describe the state of the system _before_ the scenario begins. Which files exist? Which are missing? What are their specific contents? (e.g., _"`goal_map.json` contains an entry for `DEBUG` that points to `root_cause_analysis.txt`, but that component file does not exist."_)

- **The Scenario:** Describe the sequence of events or the specific algorithm that needs to be analyzed. This is the core of the simulation. (e.g., _"The user runs the orchestrator and selects the `DEBUG` goal. The system must now execute the Just-in-Time Generation workflow."_)

- **Critical Questions:** State the explicit questions the simulation must answer. Guide the LLM's analysis toward the most important risks or design problems.
  1.  (e.g., "What are the race conditions in the proposed file-write sequence?")
  2.  (e.g., "Does the proposed naming convention create long-term technical debt?")
  3.  (e.g., "Is the proposed algorithm idempotent? If not, what are the side effects?")

---

### **The Evidence: The Proposed Algorithm/Feature**

**[This section must be updated for each specific simulation.]**

Provide the explicit algorithm, pseudocode, or feature description that the simulation LLM must analyze. This is the concrete "evidence" to be scrutinized.

```pseudocode
// Insert the specific, relevant pseudocode or algorithm to be tested here.
// This ensures the simulation is grounded in a concrete proposal, not abstract ideas.
```

---

### **Final "Evidence Locker" for Simulation**

To ensure a high-fidelity analysis, the simulation LLM must be provided with the complete context. The "Evidence Locker" package should include the content of the following files:

1.  **This `SIMULATION_BRIEFING.md` document:** Sets the stage and defines the core questions.
2.  **`goal_map.json`:** Provides the initial state of the system's "brain."
3.  **`DESIGN_PHILOSOPHY.md`:** Explains the "why" behind the project and the profile of the target user.
4.  **`README.md` and `STRATEGIC_PLAN.md`:** Provide additional context on the system's architecture and intended user workflow.
5.  **The "Proposed Algorithm/Feature":** The complete pseudocode block defined above.

This package provides a high-fidelity "digital twin" of the system and the proposed change, ensuring the simulation's results will be directly relevant and maximally valuable.
