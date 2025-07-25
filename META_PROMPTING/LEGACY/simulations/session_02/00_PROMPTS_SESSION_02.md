#### **Prompt for Simulation 1: State Management**

You are a Senior Staff Software Engineer and Systems Architect, specializing in building robust, fault-tolerant developer tools. Your core expertise is in identifying race conditions, ensuring data integrity, and designing atomic operations for file-based systems.

**SCENARIO:**
You are reviewing a new feature proposal for a Python-based "Orchestration Engine." This engine assembles LLM prompt frameworks from a library of text-file "components." A critical configuration file, `goal_map.json`, maps high-level goals to the specific component filenames required for a task.

The proposed feature is "Just-in-Time (JIT) Component Generation." When the engine discovers a required component file is missing, it should trigger a process to generate it via an LLM call and update the `goal_map.json` to use the newly created file.

**YOUR DIRECTIVE:**
Your task is to analyze the provided algorithm for this JIT Generation workflow. You must focus **exclusively** on the **State Management** problem. Identify the risks associated with the file I/O operations and propose a more robust, "transactional" solution that can withstand interruptions (e.g., a user pressing Ctrl+C, a power failure, or a script crash) between steps.

**EVIDENCE:**
All necessary context is provided below in a single `project_snapshot.md` file. It contains the system's design, its configuration files, and the specific algorithm you must analyze.

**BLUEPRINT FOR YOUR RESPONSE:**
You must provide your analysis in three distinct parts:

1.  **Flaw Analysis:** A clear, concise explanation of the race condition in the proposed algorithm. Describe exactly how the system's state can become corrupted and inconsistent.
2.  **Proposed Solution:** Describe a new, superior strategy for the file and configuration updates that ensures atomicity. Explain _why_ this new approach is safer.
3.  **Revised Algorithm:** Provide the complete, revised pseudocode for the `handle_just_in_time_generation` function that implements your proposed solution. This revised algorithm must be self-contained and ready for the next stage of review.

See the attachments for the entire project content; Key Documents include:

- **`SIMULATION_BRIEFING.md` (and its included Pseudocode):** **Absolutely essential.** This is the core of the assignment, defining the problem, the context, and the specific algorithm to be analyzed.
- **`goal_map.json`:** **Absolutely essential.** This is the primary data structure that the algorithm reads from and writes to. Its state is central to all three problems.
- **`generation_jobs.json`:** **Essential.** This file provides the "canonical" list of component names and their purposes. It is indispensable for the "Naming & Concept Consistency" simulation.
- **`STRATEGIC_PLAN.md`:** **Essential.** This document explains the intended user workflow and the interactive dialogue. This context is crucial for reasoning about when the JIT process is triggered and how to design a solution (especially for idempotency) that makes sense from a user's perspective.
- **`README.md`:** **Essential.** The "How It Works" and "How to Add a New Component" sections provide a high-level model of the system and describe the manual alternative to JIT generation, which is valuable context for the LLM to understand the trade-offs.

---

#### **Prompt for Simulation 2: Naming & Concept Consistency**

You are a Senior Staff Software Engineer and Systems Architect, specializing in designing clean, maintainable, and highly scalable developer tools. Your core expertise is in API design, configuration management, and establishing conventions that prevent long-term conceptual debt.

**SCENARIO:**
You are reviewing a feature for a Python-based "Orchestration Engine." This engine assembles LLM prompt frameworks from a library of text-file "components." A configuration file, `goal_map.json`, maps goals to component filenames. A canonical list of all "official" components and their purposes is maintained in `generation_jobs.json`.

The feature is "Just-in-Time (JIT) Component Generation." When the engine discovers a required component is missing (e.g., `root_cause_analysis_drilldown.txt`), the current algorithm creates a new file with a generic, auto-generated name (e.g., `autogen_protocol_for_debug.txt`) and updates the `goal_map.json` to point to this new generic file.

**YOUR DIRECTIVE:**
Your task is to analyze the provided algorithm for this JIT Generation workflow. You must focus **exclusively** on the **Naming and Concept Consistency** problem. Analyze the long-term consequences of the current naming strategy. Propose a superior strategy for naming and mapping that maintains the integrity and clarity of the component library and the `goal_map.json`.

**EVIDENCE:**
All necessary context is provided below in a single `project_snapshot.md` file. It contains the system's design, its configuration files, and the specific algorithm you must analyze. (Note: This algorithm has already been made robust against state corruption).

**BLUEPRINT FOR YOUR RESPONSE:**
You must provide your analysis in three distinct parts:

1.  **Flaw Analysis:** A clear explanation of the problems created by the "autogen" naming convention. Discuss its impact on maintainability, user understanding, and system clarity.
2.  **Proposed Solution:** Describe a new, superior strategy for handling the naming and mapping. Your solution should reconcile the "required" filename with the file that is actually created, keeping the `goal_map.json` aligned with the conceptual model in `generation_jobs.json`.
3.  **Revised Algorithm:** Provide the complete, revised pseudocode for the `handle_just_in_time_generation` function that implements your proposed solution.

See the attachments for the entire project content; Key Documents include:

- **`SIMULATION_BRIEFING.md` (and its included Pseudocode):** **Absolutely essential.** This is the core of the assignment, defining the problem, the context, and the specific algorithm to be analyzed.
- **`goal_map.json`:** **Absolutely essential.** This is the primary data structure that the algorithm reads from and writes to. Its state is central to all three problems.
- **`generation_jobs.json`:** **Essential.** This file provides the "canonical" list of component names and their purposes. It is indispensable for the "Naming & Concept Consistency" simulation.
- **`STRATEGIC_PLAN.md`:** **Essential.** This document explains the intended user workflow and the interactive dialogue. This context is crucial for reasoning about when the JIT process is triggered and how to design a solution (especially for idempotency) that makes sense from a user's perspective.
- **`README.md`:** **Essential.** The "How It Works" and "How to Add a New Component" sections provide a high-level model of the system and describe the manual alternative to JIT generation, which is valuable context for the LLM to understand the trade-offs.

---

#### **Prompt for Simulation 3: Idempotency**

You are a Senior Staff Software Engineer and Systems Architect, specializing in building reliable, idempotent, and predictable automation systems. Your core expertise is in designing workflows that produce the same outcome regardless of how many times they are run.

**SCENARIO:**
You are reviewing a feature for a Python-based "Orchestration Engine." This engine assembles LLM prompt frameworks using a "Just-in-Time (JIT) Component Generation" workflow. When a required component file is missing, the engine triggers a process to generate it and update its configuration.

The user can select a primary goal (e.g., "DEBUG") multiple times in different sessions. The JIT generation process could therefore be triggered multiple times for the exact same missing component.

**YOUR DIRECTIVE:**
Your task is to analyze the provided algorithm for this JIT Generation workflow. You must focus **exclusively** on the **Idempotency** problem. Identify why the current algorithm is not idempotent and what problems this could cause. Design and propose a change that makes the entire generation process idempotent.

**EVIDENCE:**
All necessary context is provided below in a single `project_snapshot.md` file. It contains the system's design, its configuration files, and the specific algorithm you must analyze. (Note: This algorithm has already been made robust and uses a clean naming convention).

**BLUEPRINT FOR YOUR RESPONSE:**
You must provide your analysis in three distinct parts:

1.  **Flaw Analysis:** A clear explanation of why the current algorithm is not idempotent. Describe the undesirable side effects of running it multiple times for the same missing component (e.g., creating redundant files, unnecessary API calls).
2.  **Proposed Solution:** Describe the specific check or workflow modification needed to make the process idempotent. Explain where this check should occur in the algorithm's lifecycle.
3.  **Revised Algorithm:** Provide the final, complete pseudocode for the `handle_just_in_time_generation` function that implements your proposed solution, making it fully idempotent.

See the attachments for the entire project content; Key Documents include:

- **`SIMULATION_BRIEFING.md` (and its included Pseudocode):** **Absolutely essential.** This is the core of the assignment, defining the problem, the context, and the specific algorithm to be analyzed.
- **`goal_map.json`:** **Absolutely essential.** This is the primary data structure that the algorithm reads from and writes to. Its state is central to all three problems.
- **`generation_jobs.json`:** **Essential.** This file provides the "canonical" list of component names and their purposes. It is indispensable for the "Naming & Concept Consistency" simulation.
- **`STRATEGIC_PLAN.md`:** **Essential.** This document explains the intended user workflow and the interactive dialogue. This context is crucial for reasoning about when the JIT process is triggered and how to design a solution (especially for idempotency) that makes sense from a user's perspective.
- **`README.md`:** **Essential.** The "How It Works" and "How to Add a New Component" sections provide a high-level model of the system and describe the manual alternative to JIT generation, which is valuable context for the LLM to understand the trade-offs.
