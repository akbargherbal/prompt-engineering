import pandas as pd
import regex as re
import os
from pathlib import Path
import json


def get_code_from_file(file_path):
    """Get code content from file with proper error handling."""
    path = Path(file_path)
    if not path.exists():
        return "Error: File not found"

    try:
        with path.open("r", encoding="utf-8") as file:
            code = file.read()
    except Exception as e:
        return f"Error: {str(e)}"

    extension = path.suffix.lower()
    if extension == ".py":
        language = "python"
        comment = "#"
        comment_line = f"{comment} code from Python file"
    elif extension == ".js":
        language = "javascript"
        comment = "//"
        comment_line = f"{comment} code from JS code file"
    else:
        language = extension[1:] if extension else "text"
        comment = "//"
        comment_line = f"{comment} code from {language} file"

    return f"```{language}\n{comment_line}\n{code}\n```"


def merge_text_files(
    input_path,
    file_pattern="*.md",
    separator="=" * 40,
    include_filenames=True,
    recursive=False,
    output_file=None,
):
    """
    Merges all text files matching the file_pattern in the input_path into a single text file or returns the merged content.

    Parameters:
    - input_path (str or Path): Directory path where files to merge are located.
    - file_pattern (str or list of str): Pattern(s) to match files to merge. Default is '*.md'.
    - separator (str): Separator between contents of each file. Default is '='*40.
    - include_filenames (bool): Include file names before each file's content. Default is True.
    - recursive (bool): Search for files recursively in subdirectories. Default is False.
    - output_file (str or Path, optional): Path to the output file. If provided, the merged content is written to this file,
      and the function returns the path. If None, the function returns the merged content as a string. Default is None.

    Returns:
    - str: The merged content if output_file is None, otherwise the path to the output file.
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input directory '{input_path}' does not exist")

    if not input_path.is_dir():
        raise ValueError(f"Input path '{input_path}' is not a directory")

    # Handle file_pattern as string or list
    if isinstance(file_pattern, str):
        patterns = [file_pattern]
    elif isinstance(file_pattern, list):
        patterns = file_pattern
    else:
        raise ValueError("file_pattern must be a string or a list of strings")

    # Collect files matching patterns
    files = []
    for pattern in patterns:
        try:
            if recursive:
                files.extend(input_path.rglob(pattern))
            else:
                files.extend(input_path.glob(pattern))
        except Exception as e:
            print(f"Warning: Error searching for pattern '{pattern}': {e}")
            continue

    if not files:
        print(f"Warning: No files found matching patterns {patterns} in {input_path}")
        return "" if output_file is None else None

    # Exclude the output file to avoid self-inclusion
    if output_file is not None:
        output_file_path = Path(output_file).resolve()
        files = [file for file in files if file.resolve() != output_file_path]

    # Sort files for consistent output
    files.sort()

    # Merge contents
    merged_parts = []
    for file in files:
        try:
            with file.open("r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Warning: Could not read file {file}: {e}")
            continue

        if include_filenames:
            try:
                rel_path = file.relative_to(input_path)
            except ValueError:
                # If file is not relative to input_path, use full path
                rel_path = file
            part = f"File: {rel_path}\n{content}"
        else:
            part = content
        merged_parts.append(part)

    if not merged_parts:
        print("Warning: No files could be read successfully")
        return "" if output_file is None else None

    # Join parts with separator
    merged_content = f"\n{separator}\n".join(merged_parts)

    if output_file is not None:
        output_file = Path(output_file)
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with output_file.open("w", encoding="utf-8") as f:
                f.write(merged_content)
            return str(output_file)
        except Exception as e:
            print(f"Error writing to {output_file}: {e}")
            raise
    else:
        return merged_content


# Initialize appendices with error handling
try:
    APPENDIX_A = get_code_from_file(
        "./appendices/APPENDIX_A_BETA_gemini-api-template.py"
    )
except Exception as e:
    print(f"Warning: Could not load APPENDIX_A: {e}")
    APPENDIX_A = f"Error loading APPENDIX_A: {e}"

try:
    APPENDIX_B = get_code_from_file("./appendices/APPENDIX_B_recover.py")
except Exception as e:
    print(f"Warning: Could not load APPENDIX_B: {e}")
    APPENDIX_B = f"Error loading APPENDIX_B: {e}"

try:
    APPENDIX_E = merge_text_files(
        input_path="./appendices/simulation_tool_kit",
        file_pattern="*.md",
        include_filenames=False,
    )
except Exception as e:
    print(f"Warning: Could not load APPENDIX_E: {e}")
    APPENDIX_E = f"Error loading APPENDIX_E: {e}"


def extract_placeholders_from_text(text):
    """
    Extract all placeholders from text using regex patterns.
    Supports various placeholder formats like:
    - PYTHON_SCRIPT_A_PLACEHOLDER
    - LLM_CONVERSATION_C_PLACEHOLDER
    - TOOLKIT_D_PLACEHOLDER
    - Any format ending with _PLACEHOLDER
    """
    if not isinstance(text, str):
        return {}

    # Pattern to find placeholders ending with _PLACEHOLDER
    placeholder_pattern = r"\b[A-Z_]*_([A-Z])_PLACEHOLDER\b"

    # Create a mapping of placeholder to appendix letter
    placeholder_mapping = {}
    try:
        for match in re.finditer(placeholder_pattern, text):
            full_placeholder = match.group(0)
            appendix_letter = match.group(1)
            placeholder_mapping[full_placeholder] = appendix_letter
    except Exception as e:
        print(f"Error extracting placeholders: {e}")
        return {}

    return placeholder_mapping


def find_appendix_files(appendices_dir):
    """
    Find all appendix files in the directory and create a mapping
    from appendix letter to file path.
    """
    appendices_dir = Path(appendices_dir)
    if not appendices_dir.exists():
        raise FileNotFoundError(
            f"Appendices directory '{appendices_dir}' does not exist"
        )

    if not appendices_dir.is_dir():
        raise ValueError(f"Path '{appendices_dir}' is not a directory")

    # Pattern to match APPENDIX_X files where X is a letter
    appendix_pattern = r"APPENDIX_([A-Z])"
    appendix_files = {}

    try:
        for file_path in appendices_dir.glob("APPENDIX_*"):
            if file_path.is_file():  # Only process files, not directories
                match = re.match(appendix_pattern, file_path.name)
                if match:
                    appendix_letter = match.group(1)
                    appendix_files[appendix_letter] = file_path
    except Exception as e:
        print(f"Error scanning appendices directory: {e}")

    return appendix_files


def read_appendix_content_default(file_path):
    """
    Default method to read appendix file content with proper encoding.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"Error: File {file_path} does not exist")
        return ""

    if not file_path.is_file():
        print(f"Error: Path {file_path} is not a file")
        return ""

    try:
        with file_path.open("r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""


def process_appendix_c_json(file_path):
    """
    Custom processor for APPENDIX_C - extracts specific JSON chunks.
    Improved with better error handling.
    """
    file_path = Path(file_path)
    content = ""

    try:
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read()

        json_data = json.loads(content)

        # Safely extract chunkedPrompt from JSON if it exists
        if "chunkedPrompt" in json_data:
            chunked_prompt_data = json_data["chunkedPrompt"]
            if (
                isinstance(chunked_prompt_data, dict)
                and "chunks" in chunked_prompt_data
            ):
                chunked_prompt = chunked_prompt_data["chunks"][:9]
                return f"```json\n{json.dumps(chunked_prompt, indent=2)}\n```"
            else:
                print(
                    f"Warning: 'chunks' key not found in chunkedPrompt for {file_path}"
                )
                return f"```json\n{json.dumps(chunked_prompt_data, indent=2)}\n```"
        else:
            # Fallback for different JSON structure
            return f"```json\n{json.dumps(json_data, indent=2)}\n```"

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from {file_path}: {e}")
        if content:  # Only return content if it was successfully read
            return f"```json\n{content}\n```"
        else:
            return f"Error: Could not parse JSON from {file_path}"
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return f"Error: File {file_path} not found"
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return f"Error processing {file_path}: {e}"


def create_content_overrides():
    """
    Define custom content processing for specific appendices.

    Returns:
        dict: Mapping of appendix letter to either:
            - A callable function that takes file_path and returns processed content
            - A string with hardcoded content
    """
    return {
        "A": APPENDIX_A + f"\n\n=== END OF APPENDIX A ===",  # HACK: add separator
        "B": APPENDIX_B + f"\n\n=== END OF APPENDIX B ===",  # HACK: add separator
        # Custom JSON processor for Appendix C
        "C": process_appendix_c_json,
        "E": APPENDIX_E + f"\n\n=== END OF APPENDIX E ===",  # HACK: add separator
        # Example of hardcoded content override
        # 'E': "This is hardcoded content for Appendix E that doesn't come from a file",
        # Example of another custom processor
        # 'F': lambda file_path: f"```python\n{read_appendix_content_default(file_path)}\n```",
        # You can add more overrides here as needed
    }


def get_appendix_content(appendix_letter, file_path, overrides):
    """
    Get content for an appendix, using overrides if available.

    Args:
        appendix_letter: The letter identifier (A, B, C, etc.)
        file_path: Path to the appendix file
        overrides: Dictionary of override processors/content

    Returns:
        str: Processed content for the appendix
    """
    if not isinstance(appendix_letter, str) or len(appendix_letter) != 1:
        print(f"Warning: Invalid appendix letter: {appendix_letter}")
        return ""

    content = ""  # Initialize content variable

    if appendix_letter in overrides:
        override = overrides[appendix_letter]

        try:
            if callable(override):
                # It's a custom processor function
                content = override(file_path)
            else:
                # It's hardcoded string content
                content = str(override)
        except Exception as e:
            print(f"Error processing override for appendix {appendix_letter}: {e}")
            # Fallback to default reading
            content = read_appendix_content_default(file_path)
    else:
        # Use default file reading
        content = read_appendix_content_default(file_path)

    # HACK: Add separator after content
    if content and not content.startswith("Error"):
        content += f"\n\n=== END OF APPENDIX {appendix_letter} ==="

    return content


def replace_placeholders_dynamically(white_paper_path, appendices_dir, output_path):
    """
    Dynamically replace placeholders in white paper with appendix content.

    Args:
        white_paper_path: Path to the white paper file
        appendices_dir: Directory containing appendix files
        output_path: Path for the output file

    Returns:
        bool: True if successful, False otherwise
    """
    # Convert paths to Path objects for consistency
    white_paper_path = Path(white_paper_path)
    appendices_dir = Path(appendices_dir)
    output_path = Path(output_path)

    # Read the white paper
    try:
        with white_paper_path.open("r", encoding="utf-8") as f:
            white_paper_content = f.read()
        print(f"✓ Successfully read {white_paper_path}")
    except FileNotFoundError:
        print(f"✗ White paper file '{white_paper_path}' not found")
        return False
    except Exception as e:
        print(f"✗ Error reading white paper file: {e}")
        return False

    # Extract placeholders from the white paper
    placeholder_mapping = extract_placeholders_from_text(white_paper_content)
    if not placeholder_mapping:
        print("✓ No placeholders found in white paper")
        # Still write the original content to output
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with output_path.open("w", encoding="utf-8") as f:
                f.write(white_paper_content)
            print(f"✓ Original content written to '{output_path}'")
            return True
        except Exception as e:
            print(f"✗ Error writing output file: {e}")
            return False

    print(f"\n=== FOUND PLACEHOLDERS ===")
    for placeholder, letter in placeholder_mapping.items():
        print(f"  {placeholder} -> Appendix {letter}")

    # Get content overrides
    content_overrides = create_content_overrides()
    if content_overrides:
        print(f"\n=== CONTENT OVERRIDES AVAILABLE ===")
        for letter, override in content_overrides.items():
            if callable(override):
                print(f"  Appendix {letter}: Custom processor function")
            else:
                print(f"  Appendix {letter}: Hardcoded content")

    # Find available appendix files
    try:
        appendix_files = find_appendix_files(appendices_dir)
        print(f"\n=== AVAILABLE APPENDICES ===")
        for letter, file_path in sorted(appendix_files.items()):
            override_status = " (with override)" if letter in content_overrides else ""
            print(f"  Appendix {letter}: {file_path.name}{override_status}")
    except (FileNotFoundError, ValueError) as e:
        print(f"✗ {e}")
        return False

    # Perform replacements
    replacement_count = 0
    missing_appendices = []

    print(f"\n=== PERFORMING REPLACEMENTS ===")
    for placeholder, appendix_letter in placeholder_mapping.items():
        content = ""

        # Handle hardcoded content overrides (no file needed)
        if appendix_letter in content_overrides and not callable(
            content_overrides[appendix_letter]
        ):
            content = str(content_overrides[appendix_letter])
            white_paper_content = white_paper_content.replace(placeholder, content)
            replacement_count += 1
            print(f"✓ Replaced '{placeholder}' with hardcoded content")
            continue

        # Handle file-based content (with or without overrides)
        if appendix_letter in appendix_files:
            file_path = appendix_files[appendix_letter]
            content = get_appendix_content(
                appendix_letter, file_path, content_overrides
            )

            if content:
                white_paper_content = white_paper_content.replace(placeholder, content)
                replacement_count += 1
                override_note = (
                    " (custom processed)"
                    if appendix_letter in content_overrides
                    and callable(content_overrides[appendix_letter])
                    else ""
                )
                print(
                    f"✓ Replaced '{placeholder}' with content from '{file_path.name}'{override_note}"
                )
            else:
                print(f"✗ Could not read/process content from '{file_path.name}'")
        elif appendix_letter not in content_overrides:
            missing_appendices.append(appendix_letter)
            print(
                f"✗ No appendix file found for '{placeholder}' (Appendix {appendix_letter})"
            )

    # Write the updated white paper
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as f:
            f.write(white_paper_content)
        print(f"\n✓ Output written to '{output_path}'")
    except Exception as e:
        print(f"✗ Error writing output file: {e}")
        return False

    # Summary
    print(f"\n=== SUMMARY ===")
    print(f"✓ Completed! Made {replacement_count} replacements")

    if missing_appendices:
        print(
            f"⚠ Warning: Missing appendices for letters: {sorted(missing_appendices)}"
        )

    # Check for remaining placeholders
    try:
        remaining_placeholders = re.findall(
            r"\b[A-Z_]*_PLACEHOLDER\b", white_paper_content
        )
        if remaining_placeholders:
            print(
                f"⚠ Warning: {len(set(remaining_placeholders))} placeholder types still remain:"
            )
            for placeholder in sorted(set(remaining_placeholders)):
                print(f"  - {placeholder}")
        else:
            print("✓ All placeholders successfully replaced!")
    except Exception as e:
        print(f"Warning: Could not check for remaining placeholders: {e}")

    return True


def main():
    """Main function to run the placeholder replacement process."""
    # Configuration - easily customizable
    white_paper_path = "./WHITE_PAPER_v02.md"
    appendices_dir = "./appendices"
    output_path = "./white_paper.md"

    print("=== DYNAMIC PLACEHOLDER REPLACEMENT WITH OVERRIDES ===")

    try:
        success = replace_placeholders_dynamically(
            white_paper_path=white_paper_path,
            appendices_dir=appendices_dir,
            output_path=output_path,
        )

        if success:
            print("\n🎉 Process completed successfully!")
            print(f"📄 Your completed white paper is ready: {output_path}")
        else:
            print("\n❌ Process failed. Please check the errors above.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the errors above.")


# Example usage for adding new overrides:
def example_custom_processors():
    """
    Examples of how to add custom processors for different appendices.
    Add these to the create_content_overrides() function as needed.
    """

    # Example 1: Custom JSON processor (like your current APPENDIX_C)
    def process_json_appendix(file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                data = json.loads(f.read())
            # Custom processing logic here
            return f"```json\n{json.dumps(data['specific_key'], indent=2)}\n```"
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            return f"Error processing JSON: {e}"

    # Example 2: Code formatter
    def format_as_python(file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                code = f.read()
            return f"```python\n{code}\n```"
        except FileNotFoundError as e:
            return f"Error reading file: {e}"

    # Example 3: Extract specific lines
    def extract_lines(file_path, start=1, end=10):
        try:
            with open(file_path, encoding="utf-8") as f:
                lines = f.readlines()
            return "".join(lines[start - 1 : end])
        except (FileNotFoundError, IndexError) as e:
            return f"Error extracting lines: {e}"

    # These would go in create_content_overrides():
    # 'D': process_json_appendix,
    # 'E': format_as_python,
    # 'F': lambda fp: extract_lines(fp, 1, 5),


if __name__ == "__main__":
    main()
