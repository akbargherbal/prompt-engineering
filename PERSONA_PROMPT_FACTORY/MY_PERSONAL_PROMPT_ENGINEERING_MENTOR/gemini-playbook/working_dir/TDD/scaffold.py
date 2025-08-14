# create_scaffold.py
from pathlib import Path
import shutil
import argparse  # MODIFICATION: Imported argparse to handle command-line arguments

# --- Configuration ---
PROJECT_NAME = "ai_chat_app"
SOURCE_FILES_TO_COPY = [
    "STATIC_MOCKUP.html",
    "current_features.json",
    "GEMINI.md",
    "app_summary.md",
]

# --- MODIFICATION: Set up argument parser ---
parser = argparse.ArgumentParser(
    description="Creates a project scaffold in a specified target directory."
)
parser.add_argument(
    "target_dir",
    type=str,
    help="The target directory where the project scaffold will be created. E.g., './work_dir/01'",
)
args = parser.parse_args()
# --- End of Modification ---

# --- MODIFICATION: Define the project root based on the user's input ---
# Instead of being in the current folder, it's now inside the user-provided directory.
base_dir = Path(args.target_dir)
project_root = base_dir / PROJECT_NAME
# --- End of Modification ---

print(f"Creating project scaffold in: {project_root.resolve()}")

# Define all directories and files to be created (No changes to this dictionary)
structure = {
    "app": {
        "static": {"styles.css": "/* Tailwind CSS output will go here */"},
        "templates": {
            "index.html": "<!DOCTYPE html>\n<html>\n<head>\n  <title>AI Chat</title>\n</head>\n<body>\n  <h1>Loading...</h1>\n</body>\n</html>"
        },
        "__init__.py": "",
        "main.py": "# FastAPI application will be defined here.",
    },
    "tests": {
        "__init__.py": "",
        ".gitkeep": "",  # Ensures the empty tests directory is committed
    },
}

# --- MODIFICATION: Create the full path, including intermediate directories ---
# The addition of `parents=True` ensures that if './work_dir/01' doesn't exist,
# it will be created automatically.
project_root.mkdir(parents=True, exist_ok=True)
# --- End of Modification ---


# Create all subdirectories and files (No changes to this function)
def create_structure(base_path, dir_dict):
    for name, content in dir_dict.items():
        path = base_path / name
        if isinstance(content, dict):
            path.mkdir(exist_ok=True)
            create_structure(path, content)
        else:
            print(f"  Creating file: {path}")
            path.touch()
            if content:
                path.write_text(content, encoding="utf-8")


create_structure(project_root, structure)

# Copy the user's source material into the project root (No changes here)
print("\nCopying source files into the project...")
for file_name in SOURCE_FILES_TO_COPY:
    source_path = Path(file_name)
    if source_path.exists():
        destination_path = project_root / file_name
        print(f"  Copying {source_path} to {destination_path}")
        shutil.copy(source_path, destination_path)
    else:
        print(f"  Warning: Source file not found, skipping: {file_name}")

print("\nScaffolding complete.")
print(f"Project created at: {project_root.resolve()}")
