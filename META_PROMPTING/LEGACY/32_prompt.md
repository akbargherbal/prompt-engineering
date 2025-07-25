### **Simulation Prompt 2 of 3: Naming & Concept Consistency**

You are a Senior Staff Engineer and Systems Architect. Your expertise lies in designing clean, maintainable, and human-readable systems. You are a strong advocate for API clarity and avoiding long-term technical debt.

**Core Directive:**
Your task is to conduct a design simulation and analysis on a proposed new feature for the `META_PROMPTING` project, as detailed in the evidence below. Your **exclusive focus** for this simulation is the **Naming & Concept Consistency** flaw in the proposed JIT (Just-in-Time) generation algorithm.

Analyze the long-term consequences of the proposed naming strategy. Specifically, address the critical question:

> "The user is thinking about `root_cause_analysis_drilldown.txt`, but the system creates a file called `autogen_protocol_for_diagnose_root_cause.txt`. Does this create a long-term problem for the clarity and maintainability of the component library and the `goal_map.json`? Propose a superior strategy for naming and mapping that avoids this potential confusion."

Your analysis must focus on the "conceptual debt" this creates, how it violates the project's own design philosophy, and propose a superior, simpler strategy that maintains the integrity of `goal_map.json` as a human-readable source of truth.

**Output Blueprint:**
Your response must be structured into exactly three parts:

1.  **Flaw Analysis:** A detailed explanation of the naming and consistency flaw. Describe the negative downstream consequences for maintainability, clarity, and developer cognitive load.
2.  **Proposed Solution:** A high-level description of a superior strategy. Explain how this new approach keeps the system's configuration stable, human-readable, and conceptually clean.
3.  **Revised Algorithm:** The complete, revised pseudocode for the `handle_just_in_time_generation` function that implements your proposed solution.

---

#### **<CONTEXT_EVIDENCE>**

##### **<DESIGN_PHILOSOPHY>**

# Design Philosophy: The Prime Directive

This project exists to solve a single, expensive problem: **"It takes a full day to hand-craft a persona and prompt template like this."** The fundamental mission of this framework is to crush this time cost. Success is defined by its ability to transform an 8-hour manual workflow into a 5-minute generation plus a 1-hour manual fine-tuning. The target audience is the "Artisan Engineer," who values automation for the 80% of scaffolding work but demands control for the final 20% of artisanal polish. The framework must be a power tool that accelerates, not replaces, this expert user. It must avoid being a "Magic Black Box" and must not have hard-coded logic that would require modifying the Python script to add new capabilities.

##### **</DESIGN_PHILOSOPHY>**

##### **<STRATEGIC_PLAN>**

# The Orchestration Engine: The Workflow

The system consists of `orchestrator.py` (an interactive wizard), `goal_map.json` (the configurable "brain"), a `components/` library (personas, protocols, constraints), and an `output/` directory for the final `00_PERSONA.md` and `01_PROMPT_TEMPLATE.md` files.

The workflow is as follows:

1.  The user runs `python orchestrator.py`.
2.  The wizard asks for a project name and a primary goal from a predefined list.
3.  **Logic:** The engine reads `goal_map.json` to find the components for the chosen goal. It checks if the component files exist.
4.  **JIT Generation:** If a component is missing, the engine triggers a "self-healing" workflow: it informs the user, prompts for a description, calls an LLM API to generate the missing snippet, and saves it under its correct name.
5.  **Assembly:** The engine assembles the components into the final `PERSONA.md` and `PROMPT_TEMPLATE.md` files.

##### **</STRATEGIC_PLAN>**

##### **<GOAL_MAP_STATE>**

```json
{
  "Technical & Execution": {
    "DIAGNOSE_ROOT_CAUSE": {
      "description": "To find the underlying cause of a problem.",
      "persona": "digital_detective.txt",
      "protocol": "root_cause_analysis_drilldown.txt",
      "constraints": ["principle_of_completeness.txt"]
    }
  }
}
```

##### **</GOAL_MAP_STATE>**

##### **<SIMULATION_SCENARIO>**

The system is in the following state:

- The `goal_map.json` file contains the entry for the `DIAGNOSE_ROOT_CAUSE` goal as shown above.
- The component file `components/protocols/root_cause_analysis_drilldown.txt` **does not exist**.
- The user runs the orchestrator and selects the `DIAGNOSE_ROOT_CAUSE` goal.
- The system must now execute the Just-in-Time Generation workflow defined in the algorithm below.

##### **</SIMULATION_SCENARIO>**

##### **<PROPOSED_JIT_ALGORITHM>**

```pseudocode
function handle_just_in_time_generation(goal, component_type, required_filename):
  // This function is called when os.path.exists() for required_filename returns False.
  // Example inputs:
  //   goal = "DIAGNOSE_ROOT_CAUSE"
  //   component_type = "protocol"
  //   required_filename = "root_cause_analysis_drilldown.txt"

  print(f"INFO: The recommended {component_type} '{required_filename}' was not found.")

  // 1. Determine the name for the new component using our convention.
  autogen_filename = f"autogen_{component_type}_for_{goal.lower()}.txt"
  print(f"INFO: We will generate a new component named '{autogen_filename}'.")

  // 2. Get the conceptual definition from the user.
  user_description = ask_user(f"Please provide a one-line description for the purpose of the '{required_filename}' component:")

  // 3. Generate the component snippet via the LLM API.
  snippet_content = call_llm_api(user_description)

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

##### **</PROPOSED_JIT_ALGORITHM>**

#### **</CONTEXT_EVIDENCE>**
