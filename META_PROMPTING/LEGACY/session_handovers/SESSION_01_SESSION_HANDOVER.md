# Project META_PROMPTING: Context Capsule & Session Handover

**DOCUMENT PURPOSE:**
This document serves as a complete context snapshot for the META_PROMPTING project. Its primary purpose is to re-establish the full context for the LLM assistant in a future session, ensuring a seamless continuation of our work. It also serves as a strategic summary for the human project lead.

---

### **1. The Project Mission (The "Why")**

Our core objective is to build a **meta-framework** that acts as a **non-linear force multiplier** for initiating expert-level LLM collaborations. We are solving the "Don't Repeat Yourself" (DRY) problem for prompt engineering.

The final product will be a Python script, the **"Orchestration Engine" (`orchestrator.py`)**, which will act as an interactive wizard. This engine will ask the user a series of high-level questions about a new task and then automatically generate the tailored `00_PERSONA.md` and `01_PROMPT_TEMPLATE.md` files required to start that collaboration.

---

### **2. Current State of the Project (As of Session End)**

- **Project Directory:** The `META_PROMPTING` project has been created with a clean, organized structure.
- **Architectural Documents:** The core design documents (`STRATEGIC_PLAN.md`, `PROMPT_SNIPPET_GENERATOR.md`, `generation_jobs.json`) are complete and located in the `docs/` directory.
- **BACKGROUND PROCESS INITIATED:** At the end of our session, the **Component Generation** process was kicked off. An LLM is currently processing the `generation_jobs.json` file to create the raw text snippets for our Component Library.

---

### **3. Accomplishments in This Session (What We've Done)**

We have successfully completed the entire strategic planning and design phase of the project.

1.  **Established the Core Concept:** We defined the idea of the "Orchestration Engine," a program that writes prompt frameworks.
2.  **Developed a Comprehensive Goal Taxonomy:** We created a robust, 7-point taxonomy of primary development goals (e.g., `EXPLAIN`, `DEBUG`, `GENERATE`, `REFACTOR`) that will serve as the core logic for the engine.
3.  **Designed the System Architecture:** We finalized the project's directory structure, separating the engine's source code (`orchestrator.py`), its knowledge base (`components/`), its documentation (`docs/`), and its output (`output/`).
4.  **Architected the "Meta-Prompting" Workflow:** Instead of manually creating the engine's components, we designed a system to generate them automatically.
    - We created the **`PROMPT_SNIPPET_GENERATOR.md`**, a "watertight" meta-prompt for generating a single component.
    - We created the **`generation_jobs.json`**, a machine-readable list of every component needed for our library. This is the master order list for the "parts factory."

---

### **4. The Way Forward (What Still Needs To Be Done)**

This is our actionable roadmap for the next session.

**Phase 1: Verify the Component Generation**

- **Task:** The very first thing we must do when we resume is to check the results of the background generation process.
- **Success Condition:** The `components/` directory should be fully populated with all the `.txt` snippet files listed in our `generation_jobs.json` file.
- **Action:** We will review a few of the generated snippets to ensure their quality and that the LLM adhered to the "raw text only" constraint.

**Phase 2: Design and Implement the `orchestrator.py` Script**

- **Task:** This is the main event. We will now design and write the core engine itself.
- **Key Design Decisions to Discuss:**
  1.  **User Interface:** How will the script handle the interactive questions? (e.g., using Python's `input()` function, or a more advanced library like `rich` or `questionary`).
  2.  **Component Assembly Logic:** How will the script read the snippets from the `components/` directory and stitch them together into the final Markdown files? (e.g., simple file reading and string concatenation).
- **Implementation Steps:**
  1.  Write the code to parse the command-line arguments (if any).
  2.  Write the interactive dialogue flow based on our 7-goal taxonomy.
  3.  Write the logic to read the appropriate `.txt` files from the `components/` subdirectories based on user choices.
  4.  Write the logic to create a new project directory in `output/` and write the final, assembled `00_PERSONA.md` and `01_PROMPT_TEMPLATE.md` files.

---

### **5. Definition of "Done" (How We'll Know The Job Is Complete)**

The **META_PROMPTING** project will be considered complete when the following conditions are met:

1.  The `components/` directory is fully populated with high-quality, standardized text snippets.
2.  The `orchestrator.py` script is a fully functional, standalone Command-Line Interface (CLI) tool.
3.  A user can run `python orchestrator.py` from the terminal, answer the series of interactive questions, and the script will successfully generate a new, ready-to-use collaboration framework in the `output/` directory without any errors.

---

### **6. Strategic Addendum: Key Project Documents**

This addendum provides a summary of the core strategic documents that inform the philosophy and quality assurance of the META_PROMPTING project.

- **1. File: `WHITE_PAPER.md` (The Project Manifesto)**
  This document, titled "White Paper: Orchestrated AI Collaboration," articulates the core problem and vision of the project. It defines the current "Artisanal Prompting Problem" characterized by context drift, inconsistent quality, and a lack of reusability. It then introduces our solution: the **Orchestration Engine**, a meta-framework that transforms prompt engineering into a scalable, repeatable discipline. The paper outlines the engine's core principles, including the Persona as a behavioral contract, the Protocol as a state machine, a component-based architecture, and a goal-oriented taxonomy. It frames the project as a strategic shift from being a user of LLMs to being the architect of the human-AI system.

- **2. File: `LEGACY_DOC.md` (The "Hand-Crafted" Gold Standard)**
  This file contains the original, hand-crafted `PERSONA.md` and `PROMPT_TEMPLATE.md` for the "Network Mentor" project. It serves as a legacy exhibit of the "artisanal" method we are seeking to automate. Its value lies in demonstrating the depth and nuance required for a truly effective, expert-level collaboration, including a detailed persona ("The Network Mentor & Digital Detective"), a turn-by-turn dialogue protocol, and a comprehensive curriculum framework. This document represents the high-quality benchmark that our automated Orchestration Engine must meet or exceed.

- **3. File: `AB_TESTING.md` (The Quality Assurance Methodology)**
  This document addresses the critical question of whether industrializing the process will sacrifice quality. It proposes a formal, scientific methodology for A/B testing the output of our new Orchestration Engine against the proven, hand-crafted "gold standard" from the `LEGACY_DOC.md`. The process involves establishing a benchmark "Golden Task," generating a "Challenger" framework with the engine, running a blind test, and scoring both sessions on a quantitative **Quality Scorecard**. This scorecard includes metrics like "Time to First Value," "Persona Adherence," and "Number of Corrective Interventions." This methodology provides a data-driven way to prove and improve the quality of our meta-framework, ensuring we are building a true force multiplier, not a mediocrity engine.

- **4. File: `SIMULATION_EXERCISE_01.md` (The Strategic Crossroads Analysis)**
  This document serves as a critical strategic analysis at a key project juncture. It identifies a potential "A/B Test Fallacy," where validating the engine against a single legacy task could create a brittle tool that is falsely perceived as complete. It simulates three distinct development pathways: a "Static MVP Library," a "Big Upfront Design," and an "Evolutionary Library & Self-Aware Engine." After evaluating each pathway against the project's core constraints using a decision matrix, it unequivocally recommends the "Evolutionary" approach. This pathway is chosen because it is the only one that ensures long-term scalability and aligns with the project's mission by building an engine that learns and grows organically with each new use case. Remind me to talk about this subject after you familiarize yourself with the whole project, as there are some things I’ll need to clarify with you. See `LEGACY/generation_jobs.json` to get an idea.

---

IMPORTANT: Always ask when you're in doubt about something that doesn't make sense or contradicts this session handover, as I might have done things outside our chat sessions that changed the existing conditions or assumptions.

---
