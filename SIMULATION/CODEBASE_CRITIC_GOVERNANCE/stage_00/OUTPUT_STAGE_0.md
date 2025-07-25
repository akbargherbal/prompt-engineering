### The "Before" Design

```pseudocode
// --- ORIGINAL, FLAWED ALGORITHM ---
function handle_just_in_time_generation(goal, component_type, required_filename):
  // 1. Create a generic, auto-generated filename.
  autogen_filename = f"autogen_{component_type}_for_{goal.lower()}.txt"
  // 2. Get a description from the user and call an LLM API.
  snippet_content = call_llm_api(...)
  // 3. Write the new snippet to the `autogen_filename`.
  save_file(...)
  // 4. Update goal_map.json to point to the `autogen_filename`.
  write_json_file(...)
```

### The "After" Design (Critic's Proposal)

```pseudocode
// --- FINAL, SYNTHESIZED ALGORITHM ---
function handle_just_in_time_generation(goal, component_type, required_filename):
  // 1. Determine the canonical path using the correct, intended filename.
  component_path = "components/{component_type}s/{required_filename}"

  // 2. IDEMPOTENCY CHECK (Insight from Simulation #3)
  // Check if the final artifact already exists. If so, our work is done.
  if os.path.exists(component_path):
    return component_path

  // --- If we are here, proceed with one-time generation. ---

  // 3. Get description from user and generate snippet via LLM.
  snippet_content = call_llm_api(...)

  // 4. Write the component to its final, correct path.
  // (Insight from Simulation #2: The goal_map.json is NEVER modified).
  save_file(component_path, snippet_content)

  // 5. Return the path.
  return component_path
```
