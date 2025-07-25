
*This appendix contains the exact, complete "Evidence Locker" provided to the simulation LLM for the `META_PROMPTING` JIT generation feature. Note that it includes the initial, flawed pseudocode that was the subject of the first simulation.*

---

#### **The Briefing Document (`SIMULATION_BRIEFING.md`)**
```markdown
# META_PROMPTING: Simulation & Analysis Briefing

**DOCUMENT PURPOSE:** This document provides a comprehensive, self-contained briefing for a Large Language Model tasked with running a simulation related to the META_PROMPTING project. Its goal is to establish the necessary context for a high-quality, relevant analysis.

---

### **1. The Core Mission: The Factory Analogy**

The META_PROMPTING project is building a "factory" called the **Orchestration Engine**. This engine is a Python script (`orchestrator.py`) that acts as a "factory foreman."

Its job is **not** to do the work itself, but to **build the tools** for a specific job. When the factory owner (the user) needs a new tool, they tell the foreman what the primary goal is (e.g., "I need to AUDIT some code"). The foreman then goes to the "parts bin" (`components/` library), collects the right parts (pre-written text snippets for personas, protocols, and constraints), and assembles them into a final, ready-to-use toolkit (`00_PERSONA.md` and `01_PROMPT_TEMPLATE.md`).

The core philosophy is "Don't Repeat Yourself" (DRY) for prompt engineering.

---

### **2. The System Components (The "Cast of Characters")**

To understand the system, you must know its parts:

*   **`orchestrator.py` (The Foreman):** The main Python script. It is an interactive wizard that talks to the user and manages the entire assembly process.

*   **`goal_map.json` (The Production Orders):** A JSON file that tells the foreman which parts to use for which job. It maps a high-level goal like "AUDIT" to specific part numbers (filenames) like `meticulous_auditor.txt` (a persona) and `code_review_pass.txt` (a protocol).

*   **`components/` (The Parts Bin):** A directory containing the raw materials. It is organized into three sub-directories:
    *   `personas/`: Text snippets defining the LLM's role and tone.
    *   `protocols/`: Text snippets defining the rules of interaction.
    *   `constraints/`: Text snippets defining non-negotiable rules.

*   **`output/` (The Loading Dock):** The directory where the final, assembled toolkits are placed, each in its own project folder.

---

### **3. The End-to-End Workflow (The "Plot")**

A successful workflow proceeds as follows:
1.  The user runs `python orchestrator.py`.
2.  The script asks for a project name and a primary goal (e.g., "AUDIT").
3.  The script reads `goal_map.json` to find the recommended parts for "AUDIT".
4.  It checks if all the required parts exist in the `components/` directory.
5.  Assuming they all exist, it reads their text content.
6.  It assembles this content into two final Markdown files (`00_PERSONA.md`, `01_PROMPT_TEMPLATE.md`).
7.  It creates a new directory in `output/` and saves the two final files there.

---

### **4. The Current Simulation Task (Your Assignment)**

This is where the standard workflow breaks. We need to simulate the **Just-in-Time (JIT) Component Generation** workflow.

**Initial State:**
*   The `goal_map.json` file contains an entry for the `DEBUG` goal that points to a protocol file named `root_cause_analysis_drilldown.txt`.
*   Crucially, the file `components/protocols/root_cause_analysis_drilldown.txt` **does not exist**.

**Your Task:**
Model the sequence of events that must happen next. The engine is designed to be "self-aware"—it must detect the missing part and trigger a process to create it. My current design states that the engine will auto-generate a new filename (`autogen_protocol_for_debug.txt`), prompt the user for a description, call an LLM to generate the snippet, save it under the new name, and then update the `goal_map.json` to point to this new file.

**Your analysis must focus on identifying the potential flaws, race conditions, or logical inconsistencies in this proposed JIT workflow.** Specifically, please address the following critical questions:

1.  **State Management:** What are the risks associated with the "create file -> update map" process? What happens if the process fails between these two steps? How can we make this process more robust, like a database transaction?
2.  **Naming & Concept Consistency:** The user is thinking about `root_cause_analysis_drilldown`, but the system creates a file called `autogen_protocol_for_debug.txt`. Does this create a long-term problem for the clarity and maintainability of the component library and the `goal_map.json`? Propose a superior strategy for naming and mapping that avoids this potential confusion.
3.  **Idempotency:** How can we ensure that if this JIT process is triggered multiple times for the same missing `DEBUG` protocol, it doesn't create multiple redundant files (`autogen_protocol_1.txt`, `autogen_protocol_2.txt`)? Design a check or a workflow that makes the generation process idempotent (running it N times has the same result as running it once).

---

#### **The Proposed JIT Generation Algorithm (Pseudocode)**

```pseudocode
function handle_just_in_time_generation(goal, component_type, required_filename):
  // This function is called when os.path.exists() for required_filename returns False.
  // Example inputs:
  //   goal = "DEBUG"
  //   component_type = "protocol"
  //   required_filename = "root_cause_analysis_drilldown.txt"

  print(f"INFO: The recommended {component_type} '{required_filename}' was not found.")
  
  // 1. Determine the name for the new component using our convention.
  autogen_filename = f"autogen_{component_type}_for_{goal.lower()}.txt"
  print(f"INFO: We will generate a new component named '{autogen_filename}'.")

  // 2. Get the conceptual definition from the user.
  user_description = ask_user(f"Please provide a one-line description for the purpose of the '{required_filename}' component:")
  
  if user_description is empty:
    print("WARNING: No description provided. Aborting component generation.")
    // In this case, we would fall back to "Degraded Mode" with a placeholder.
    return None

  // 3. Generate the component snippet via the LLM API.
  // This call is wrapped in a try/except block to handle API keys/network errors.
  snippet_content = call_llm_api(user_description)
  
  if snippet_content is None:
    print("WARNING: LLM API call failed. Aborting component generation.")
    // Fall back to "Degraded Mode".
    return None

  // 4. THE CRITICAL STATE CHANGE
  // This is the sequence the simulation must scrutinize.

  // Step 4a: Write the new component file to the library.
  new_component_path = "components/{component_type}s/{autogen_filename}"
  save_file(new_component_path, snippet_content)
  print(f"SUCCESS: New component saved to '{new_component_path}'.")

  // Step 4b: Update the master configuration map.
  json_map = read_json_file("goal_map.json")
  json_map[goal][component_type] = autogen_filename
  write_json_file("goal_map.json", json_map)
  print("SUCCESS: goal_map.json has been updated to use the new component.")

  // 5. Return the path to the newly created and mapped component.
  return new_component_path
  ```
  ```