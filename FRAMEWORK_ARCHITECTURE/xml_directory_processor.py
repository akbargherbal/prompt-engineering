"""
Enhanced directory processor optimized for LLM parsing and codebase recreation.
Key improvements:
1. Structured XML-like format for easy parsing
2. Embedded file metadata for recreation
3. Execution context hints
4. Dependency detection
5. Project structure inference
"""

import os
import sys
import argparse
import re
import tiktoken
import json
import logging
import hashlib
from tqdm import tqdm
from pathlib import Path
from typing import List, Dict, Tuple, Set, Optional
import nbconvert
import fnmatch

DEFAULT_OUTPUT_FILE = "codebase_structured.txt"
list_dir_ignored = []

def setup_logging(log_file: str, enable_logging: bool = True):
    if enable_logging:
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filemode="w",
        )
    else:
        logging.basicConfig(level=logging.ERROR, handlers=[logging.NullHandler()])

def count_tokens(text: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def detect_project_type(root_path: str) -> Dict[str, any]:
    """Detect project type and key files for LLM context"""
    project_info = {
        "type": "unknown",
        "language": "mixed",
        "framework": None,
        "entry_points": [],
        "config_files": [],
        "dependency_files": [],
        "test_directories": [],
        "build_files": []
    }
    
    # Check for key indicator files
    key_files = {
        "package.json": {"type": "nodejs", "language": "javascript"},
        "requirements.txt": {"type": "python", "language": "python"},
        "pyproject.toml": {"type": "python", "language": "python"},
        "setup.py": {"type": "python", "language": "python"},
        "Cargo.toml": {"type": "rust", "language": "rust"},
        "go.mod": {"type": "go", "language": "go"},
        "pom.xml": {"type": "java", "language": "java"},
        "build.gradle": {"type": "java", "language": "java"},
        "composer.json": {"type": "php", "language": "php"},
        "Gemfile": {"type": "ruby", "language": "ruby"}
    }
    
    for root, dirs, files in os.walk(root_path):
        if root.count(os.sep) - root_path.count(os.sep) > 2:  # Limit depth
            continue
            
        for file in files:
            if file in key_files:
                info = key_files[file]
                project_info.update(info)
                project_info["dependency_files"].append(os.path.join(root, file))
            
            # Config files
            if file in ["config.json", "settings.py", ".env.example", "docker-compose.yml", "Dockerfile"]:
                project_info["config_files"].append(os.path.join(root, file))
            
            # Entry points
            if file in ["main.py", "app.py", "index.js", "server.js", "main.go", "main.rs"]:
                project_info["entry_points"].append(os.path.join(root, file))
            
            # Build files
            if file in ["Makefile", "build.sh", "webpack.config.js", "vite.config.js"]:
                project_info["build_files"].append(os.path.join(root, file))
        
        # Test directories
        for dir_name in dirs:
            if dir_name in ["test", "tests", "__tests__", "spec"]:
                project_info["test_directories"].append(os.path.join(root, dir_name))
    
    return project_info

def get_file_metadata(file_path: str) -> Dict[str, any]:
    """Extract metadata useful for recreation"""
    try:
        stat = os.stat(file_path)
        ext = os.path.splitext(file_path)[1]
        
        metadata = {
            "size": stat.st_size,
            "extension": ext,
            "executable": os.access(file_path, os.X_OK),
            "relative_path": None  # Will be set by caller
        }
        
        # Language-specific metadata
        if ext in ['.py', '.js', '.ts', '.go', '.rs', '.java']:
            metadata["is_source"] = True
        elif ext in ['.json', '.yaml', '.yml', '.toml', '.ini']:
            metadata["is_config"] = True
        elif ext in ['.md', '.txt', '.rst']:
            metadata["is_documentation"] = True
        elif ext in ['.sh', '.bat', '.ps1']:
            metadata["is_script"] = True
            metadata["executable"] = True
        
        return metadata
    except Exception:
        return {"size": 0, "extension": "", "executable": False}

def extract_imports_dependencies(content: str, file_path: str) -> List[str]:
    """Extract import statements for dependency mapping"""
    ext = os.path.splitext(file_path)[1].lower()
    imports = []
    
    try:
        if ext == '.py':
            import_patterns = [
                r'^import\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)',
                r'^from\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)\s+import'
            ]
        elif ext in ['.js', '.ts']:
            import_patterns = [
                r'^import.*from\s+[\'"]([^\'"]+)[\'"]',
                r'^const.*=\s*require\([\'"]([^\'"]+)[\'"]\)'
            ]
        elif ext == '.go':
            import_patterns = [r'^import\s+[\'"]([^\'"]+)[\'"]']
        else:
            return imports
        
        for pattern in import_patterns:
            matches = re.findall(pattern, content, re.MULTILINE)
            imports.extend(matches)
    except Exception:
        pass
    
    return imports

def should_include_file(file_path: str, file_size: int, params: Dict) -> bool:
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext in params["exclude_extensions"]:
        logging.debug(f"Excluded file due to extension: {file_path}")
        return False
    
    if ext == ".json" and file_size > params["json_size_threshold"]:
        logging.debug(f"Excluded JSON file due to size: {file_path}")
        return False
    
    if file_size > params["max_file_size"]:
        logging.debug(f"Excluded file due to size: {file_path}")
        return False
    
    return True

def should_ignore_path(path: str, ignore_patterns: List[str]) -> bool:
    path_parts = Path(path).parts
    
    for pattern in ignore_patterns:
        for part in path_parts:
            if pattern.endswith("/"):
                if part == pattern[:-1]:
                    return True
            else:
                if fnmatch.fnmatch(part, pattern) or pattern in part:
                    return True
    return False

def convert_notebook_to_markdown(notebook_path: str) -> str:
    logging.info(f"Converting notebook to markdown: {notebook_path}")
    markdown_exporter = nbconvert.MarkdownExporter()
    body, _ = markdown_exporter.from_filename(notebook_path)
    
    md_path = notebook_path.rsplit(".", 1)[0] + ".md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(body)
    
    logging.info(f"Notebook converted: {md_path}")
    return md_path

def process_directory_structured(
    root_path: str,
    params: Dict,
    output_file,
    project_info: Dict,
    excluded_files: List[Tuple[str, int]]
) -> None:
    """Process directory with structured XML-like output"""
    
    # Write project header
    output_file.write("<codebase>\n")
    output_file.write(f"<project type='{project_info['type']}' language='{project_info['language']}'>\n")
    
    if project_info['entry_points']:
        output_file.write("<entry_points>\n")
        for ep in project_info['entry_points']:
            output_file.write(f"  <entry>{os.path.relpath(ep, root_path)}</entry>\n")
        output_file.write("</entry_points>\n")
    
    if project_info['dependency_files']:
        output_file.write("<dependencies>\n")
        for dep in project_info['dependency_files']:
            output_file.write(f"  <file>{os.path.relpath(dep, root_path)}</file>\n")
        output_file.write("</dependencies>\n")
    
    if project_info['test_directories']:
        output_file.write("<test_dirs>\n")
        for test_dir in project_info['test_directories']:
            output_file.write(f"  <dir>{os.path.relpath(test_dir, root_path)}</dir>\n")
        output_file.write("</test_dirs>\n")
    
    output_file.write("</project>\n\n")
    
    # Write files in structured format
    output_file.write("<files>\n")
    
    for root, dirs, files in os.walk(root_path):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if not should_ignore_path(os.path.join(root, d), params["ignore_patterns"])]
        
        for file in sorted(files):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, root_path)
            
            if should_ignore_path(file_path, params["ignore_patterns"]):
                continue
            
            try:
                file_size = os.path.getsize(file_path)
            except OSError:
                continue
            
            # Handle notebooks
            if file.endswith(".ipynb"):
                try:
                    md_path = convert_notebook_to_markdown(file_path)
                    file_path = md_path
                    rel_path = os.path.relpath(md_path, root_path)
                    file_size = os.path.getsize(md_path)
                except Exception as e:
                    logging.error(f"Error converting notebook {file_path}: {str(e)}")
                    continue
            
            if should_include_file(file_path, file_size, params):
                metadata = get_file_metadata(file_path)
                metadata["relative_path"] = rel_path
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    content_tokens = count_tokens(content)
                    if content_tokens <= params["token_limit"]:
                        # Extract imports for dependency mapping
                        imports = extract_imports_dependencies(content, file_path)
                        
                        # Write structured file entry
                        output_file.write(f"<file path='{rel_path}' size='{file_size}' ext='{metadata['extension']}'")
                        if metadata.get('executable'):
                            output_file.write(" executable='true'")
                        if imports:
                            output_file.write(f" imports='{','.join(imports[:5])}'")  # Limit to first 5 imports
                        output_file.write(">\n")
                        
                        # Content with clear delimiters
                        output_file.write("```\n")
                        output_file.write(content)
                        if not content.endswith('\n'):
                            output_file.write('\n')
                        output_file.write("```\n")
                        output_file.write("</file>\n\n")
                    else:
                        output_file.write(f"<file path='{rel_path}' size='{file_size}' excluded='token_limit'></file>\n")
                        logging.info(f"Content excluded due to token limit: {file_path}")
                        
                except Exception as e:
                    logging.error(f"Error processing file {file_path}: {str(e)}")
                    output_file.write(f"<file path='{rel_path}' error='processing_failed'></file>\n")
            else:
                excluded_files.append((file_path, file_size))
    
    output_file.write("</files>\n")
    output_file.write("</codebase>\n")

def main():
    parser = argparse.ArgumentParser(
        description="Process directory for optimal LLM parsing and codebase recreation"
    )
    parser.add_argument("--enable-logging", action="store_true", default=False)
    parser.add_argument("directory_path", help="Path to the directory to process")
    parser.add_argument("--token-limit", type=int, default=10_000)
    parser.add_argument("--json-size-threshold", type=int, default=1024 * 1024)
    parser.add_argument(
        "--exclude-extensions",
        nargs="+",
        default=[".csv", ".pt", ".pkl", ".bin", ".h5", ".parquet", ".gitignore", ".zip", ".exe", ".dll", ".so"],
    )
    parser.add_argument(
        "--ignore-patterns",
        nargs="+",
        default=[
            ".env", ".git", ".history", ".idea", ".jest", ".pytest_cache", ".venv", ".vscode",
            "__pycache__", "assets", "bin", "bower_components", "build", "coverage", "dist",
            "document", "generated", "graphics", "images", "media", "migrations", "misc_docs",
            "node_modules", "obj", "packages", "public", "staticfiles", "tabs", "target",
            "test-results/", "LEGACY/", "/FastAPI", "SESSION_HANDOVER/", "utility_scripts/",
            "logs/", "staticfiles/", "vendor", "venv", "BUGS/", "TODO/", "TUTORIALS/",
            "QUIZ_COLLECTIONS/", "package-lock.json", DEFAULT_OUTPUT_FILE, "HTML_OUTPUT",
            "results_2025*"
        ],
    )
    parser.add_argument("--max-depth", type=int, default=10)
    parser.add_argument("--max-file-size", type=int, default=10 * 1024 * 1024)
    parser.add_argument("--output", default=DEFAULT_OUTPUT_FILE)
    parser.add_argument("--split-threshold", type=int, default=1000000)
    parser.add_argument("--log-file", default="directory_processing.log")
    
    args = parser.parse_args()
    
    setup_logging(args.log_file, args.enable_logging)
    logging.info("Starting enhanced directory processing")
    
    if not os.path.exists(args.directory_path) or not os.path.isdir(args.directory_path):
        logging.error(f"Invalid directory: {args.directory_path}")
        print(f"Error: Invalid directory: {args.directory_path}")
        sys.exit(1)
    
    # Detect project structure
    project_info = detect_project_type(args.directory_path)
    logging.info(f"Detected project type: {project_info}")
    
    params = vars(args)
    excluded_files = []
    
    with open(args.output, "w", encoding="utf-8") as output_file:
        process_directory_structured(args.directory_path, params, output_file, project_info, excluded_files)
    
    # Token counting and splitting logic (similar to original)
    with open(args.output, "r", encoding="utf-8") as f:
        content = f.read()
        total_tokens = count_tokens(content)
    
    logging.info(f"Total tokens: {total_tokens}")
    print(f"Processing complete. Total tokens: {total_tokens}")
    
    if total_tokens > args.split_threshold:
        logging.info("Output exceeds split threshold. Consider splitting.")
        print("Note: Output exceeds recommended token limit for single LLM context.")

if __name__ == "__main__":
    main()
