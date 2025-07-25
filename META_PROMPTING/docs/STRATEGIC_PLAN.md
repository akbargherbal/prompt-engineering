### The Orchestration Engine: The Complete Process

#### **The Core Philosophy (The "Why")**

The engine's purpose is to solve your DRY problem and act as a force multiplier. It systematizes your successful ad-hoc experiments into a reliable, generative process. You are moving from being a "prompt user" to a **"framework architect."** The engine codifies your expertise in how to collaborate with an LLM, making that expertise repeatable and scalable.

---

#### **The Architecture (The "What")**

The system consists of four main parts:

1.  **The Engine (`orchestrator.py`):** An interactive Python script that acts as the "wizard" or "factory foreman." It guides you through the configuration process.
2.  **The Engine Configuration (`goal_map.json`):** An external JSON file that acts as the engine's "brain." It maps the primary goals to the recommended persona, protocol, and constraint components, making the engine's logic easily configurable without changing the source code.
3.  **The Component Library (The "Parts Bin"):** A collection of text snippets that represent codified patterns.
    - `personas/`: Contains snippets for different roles (e.g., `empathetic_guide.txt`, `meticulous_auditor.txt`).
    - `protocols/`: Contains snippets defining different interaction models (e.g., `code_review_pass.txt`, `turn_by_turn_dialogue.txt`).
    - `constraints/`: Contains snippets for different rule sets (e.g., `preserve_functional_attributes.txt`, `no_html_restructure.txt`).
4.  **The Collaboration Environment (The "Output"):** The final, generated `00_PERSONA.md` and `01_PROMPT_TEMPLATE.md` files, perfectly tailored to the specific task at hand.

---

#### **The Workflow (The "How")**

This is the step-by-step process of using the engine. It is designed as a simple, linear Command-Line Interface (CLI) for an expert user (you).

**Step 1: Invocation**

You start a new project by running the engine from your terminal.

```bash
$ python orchestrator.py
```

**Step 2: The Interactive Wizard**

The engine begins a dialogue to understand the nature of the task.

**Wizard:** `Welcome to the LLM Orchestration Engine. Let's configure a new collaboration.`
**Wizard:** `Enter a name for this project (e.g., "API_Refactor_Tool"):`
**You:** `Django_Model_Auditor`

**Wizard:** `What is the PRIMARY GOAL of this task? This will determine the core logic.`
`  [1] EXPLAIN / DOCUMENT`
`  [2] DEBUG / DIAGNOSE`
`  [3] AUDIT / REVIEW`
`  [4] GENERATE / SCAFFOLD`
`  [5] REFACTOR / OPTIMIZE`
`  [6] ENHANCE / INTEGRATE`
`  [7] TRANSFORM / MIGRATE`
**You:** `3`

**Step 3: Component Resolution & Just-in-Time Generation**

This is the core of the engine's logic.

1.  **Read Configuration:** The engine reads `goal_map.json` to find the recommended components for the selected 'AUDIT' goal (e.g., `meticulous_auditor.txt`, `code_review_pass.txt`).
2.  **Check for Components:** For each recommended component, the engine checks if the file exists in the `components/` library.
3.  **Just-in-Time Generation (if needed):**
    - If a recommended component is missing, the engine triggers the JIT workflow.
    - It informs you that a component is missing and will be auto-generated with a standard name (e.g., `autogen_protocol_for_audit.txt`).
    - It prompts you for a description of the needed snippet.
    - It then calls the LLM API to generate the component and saves it to the library.
4.  **Degraded Mode (API Failure):** If the LLM API call fails (e.g., no API key, network error), the engine will **not crash**. It will inform you of the failure, log a TODO, and insert a placeholder in the final `.md` file, allowing you to complete the process manually. The workflow is never fully blocked.

**Step 4: Framework Assembly & Generation**

Once all components are present (either pre-existing or just-in-time generated), the engine assembles the final files.

**Wizard:** `Please provide a title for the Persona (e.g., "The Code Guardian"):`
**You:** `The Django Standards Advocate`

**Wizard:** `Based on the goal 'AUDIT', I recommend the "Meticulous Auditor" persona. Is this correct? (Y/n)`
**You:** `Y`

**Wizard:** `Generating framework files in directory: ./output/Django_Model_Auditor/`
`  - SUCCESS: Created 00_PERSONA.md`
`  - SUCCESS: Created 01_PROMPT_TEMPLATE.md`
**Wizard:** `Configuration complete.`

**Step 5: The Collaboration**

You now begin your work by providing the generated `00_PERSONA.md` to the LLM, followed by the `01_PROMPT_TEMPLATE.md` (filled with the code to be audited), kicking off a highly structured and predictable collaboration.

---

### The Power of this Approach

- **It's a Force Multiplier:** It reduces the setup time for a new, high-quality collaboration from hours to seconds.
- **It Prevents "Re-inventing the Wheel":** It ensures that hard-won lessons are codified and reused.
- **It Scales Your Expertise:** The engine's logic is easily configurable via the `goal_map.json` file, allowing the system to evolve without changing its code.
- **It's Resilient:** By gracefully handling failures and operating in a "degraded mode," the engine ensures it is always a useful tool.
