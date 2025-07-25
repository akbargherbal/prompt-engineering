import json
import os
import sys

# Import your trusted, adapted script
import GAMMA_gemini_api_template as gemini_api

# --- Constants for File Paths ---
GOAL_MAP_PATH = "goal_map.json"
COMPONENTS_DIR = "components"
OUTPUT_DIR = "output"

# --- Core File I/O Helper Functions ---
def read_json_file(path: str) -> dict:
    """Reads and parses a JSON file using UTF-8 encoding."""
    try:
        # CORRECTED: Added encoding='utf-8' as you rightly suggested.
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"FATAL: Configuration file not found at '{path}'. Exiting.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"FATAL: Could not parse JSON in '{path}'. Exiting.")
        sys.exit(1)

def read_file(path: str) -> str:
    """Reads the content of a text file using UTF-8 encoding."""
    try:
        # CORRECTED: Added encoding='utf-8' for consistency.
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def save_file(path: str, content: str):
    """Saves content to a file using UTF-8, creating directories if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # CORRECTED: Added encoding='utf-8' for all file writing.
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# --- Just-in-Time Component Generation (Using your adapted script) ---
def handle_just_in_time_generation(gemini_model, component_path: str, goal_name: str, component_type: str) -> str:
    if os.path.exists(component_path):
        return component_path

    required_filename = os.path.basename(component_path)
    print(f"\nINFO: The required {component_type} '{required_filename}' was not found.")
    print("INFO: We will now generate this component to self-heal the library.")

    try:
        user_description = input(f" > Please provide a one-line description for the purpose of the '{required_filename}' component: ")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting.")
        sys.exit(0)

    snippet_content = ""
    try:
        snippet_content = gemini_api.generate_orchestrator_snippet(gemini_model, user_description)
    except Exception as e:
        print(f"WARN: Could not generate component via API. The system will operate in 'degraded mode'.")
        print(f"WARN: A placeholder will be inserted. You will need to create '{component_path}' manually.")
        snippet_content = f"TODO: MANUALLY CREATE THIS COMPONENT.\nGoal: {goal_name}\nType: {component_type}\nUser Description: {user_description}\n"

    save_file(component_path, snippet_content)
    print(f"SUCCESS: New component saved to '{component_path}'.")

    return component_path

# --- Main Orchestration Logic ---
def main():
    print("Welcome to the LLM Orchestration Engine.")

    try:
        if not os.getenv("GEMINI_API_KEY"):
             print("Google API key not found in environment variables. Please enter it now for this session.")
             api_key_input = input("Paste your Google API key: ").strip()
             os.environ['GEMINI_API_KEY'] = api_key_input
        gemini_model = gemini_api.setup_gemini_api()
    except Exception as e:
        print(f"\nFATAL: Could not initialize the Gemini API: {e}")
        sys.exit(1)

    print("\nLet's configure a new collaboration framework.")

    try:
        project_name = input(" > Enter a name for this project (e.g., 'API_Refactor_Tool'): ")
        if not project_name:
            project_name = "Untitled_Project"
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting.")
        sys.exit(0)

    goal_map = read_json_file(GOAL_MAP_PATH)
    goal_choices = {}
    choice_counter = 1

    print("\nWhat is the PRIMARY GOAL of this task?")
    for category, goals in goal_map.items():
        print(f"\n--- {category} ---")
        for goal_name, goal_details in goals.items():
            print(f"[{choice_counter}] {goal_name:<25} (Purpose: {goal_details['description']})")
            goal_choices[choice_counter] = (goal_name, goal_details)
            choice_counter += 1

    try:
        chosen_index = int(input("\nYour choice: "))
        selected_goal_name, selected_goal = goal_choices[chosen_index]
    except (ValueError, KeyError):
        print("Invalid choice. Exiting.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting.")
        sys.exit(0)

    print(f"INFO: Selected Goal: '{selected_goal_name}'")

    persona_file = selected_goal['persona']
    protocol_file = selected_goal['protocol']
    constraint_files = selected_goal['constraints']
    
    persona_path = os.path.join(COMPONENTS_DIR, 'personas', persona_file)
    handle_just_in_time_generation(gemini_model, persona_path, selected_goal_name, 'persona')

    protocol_path = os.path.join(COMPONENTS_DIR, 'protocols', protocol_file)
    handle_just_in_time_generation(gemini_model, protocol_path, selected_goal_name, 'protocol')

    for constraint_file in constraint_files:
        constraint_path = os.path.join(COMPONENTS_DIR, 'constraints', constraint_file)
        handle_just_in_time_generation(gemini_model, constraint_path, selected_goal_name, 'constraint')

    try:
        print(f"\nBased on the goal, the base persona is '{persona_file}'.")
        persona_title = input(" > Please provide a title for the Persona (e.g., 'The Code Guardian'): ")
        if not persona_title:
            persona_title = "Untitled Persona"
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting.")
        sys.exit(0)

    persona_content = read_file(persona_path)
    protocol_content = read_file(protocol_path)
    constraints_content = "\n\n---\n\n".join([read_file(os.path.join(COMPONENTS_DIR, 'constraints', cf)) for cf in constraint_files])

    final_persona_md = f"# Persona: {persona_title}\n\n{persona_content}"
    final_prompt_template_md = (f"# Prompt Template\n\n## PROTOCOL\n\n{protocol_content}\n\n## CONSTRAINTS\n\n{constraints_content}\n\n---\n\n[INSERT YOUR SPECIFIC REQUEST HERE]")

    output_project_dir = os.path.join(OUTPUT_DIR, project_name)
    persona_output_path = os.path.join(output_project_dir, '00_PERSONA.md')
    template_output_path = os.path.join(output_project_dir, '01_PROMPT_TEMPLATE.md')

    print(f"\nGenerating framework files in directory: ./{output_project_dir}/")
    save_file(persona_output_path, final_persona_md)
    print(f"  - SUCCESS: Created {os.path.basename(persona_output_path)}")
    save_file(template_output_path, final_prompt_template_md)
    print(f"  - SUCCESS: Created {os.path.basename(template_output_path)}")

    print("\nConfiguration complete.")


if __name__ == "__main__":
    main()