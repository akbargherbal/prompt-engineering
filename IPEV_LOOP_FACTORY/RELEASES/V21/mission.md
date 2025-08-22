# Mission: Refactor Gemini Bridge to Meet All Documented Requirements
**Agent Platform:** Gemini CLI (YOLO Mode)

## 1. Core Protocol: The Enhanced IPEV Loop with Two-Tiered Checkpointing

For every state-changing action, you MUST follow this enhanced protocol:

### Standard IPEV Flow:
1.  **INTENT:** State your immediate objective.
2.  **PLAN:** Specify the EXACT commands and file modifications.
3.  **EXECUTE:** Run the exact command or apply the file modification.
4.  **VERIFY:** Perform a check to prove the change was successful (e.g., run a specific `pytest` test).

### **CRITICAL** Checkpointing Protocol (After a successful VERIFY):
5.  **CODE CHECKPOINT (Autonomous):** You MUST use git to save the successful changes. Your plan must include `git add .` and `git commit -m "Verified Feature: [brief description of feature]"`.
6.  **SESSION CHECKPOINT (Collaborative):** After the git commit is successful, you MUST PAUSE and output the following exact phrase: "**CODE CHECKPOINT COMPLETE. Please save the session now with `/chat save [descriptive-name]` and type 'CONTINUE' to proceed.**" You will not proceed until I respond with "CONTINUE".

### Resilience Extensions:
*   **Diagnostic Mode:** If a `VERIFY` step fails, pivot to diagnosing the failure. Run `pytest` with `-v` for more verbose output.
*   **Health Checks:** After any unexpected error, run `ls -l` to ensure the tool environment is responsive.

## 2. Directive Protocol

Commands prefixed with `DIRECTIVE:` are for inspection. Use them to examine files before formulating a plan.
*   `DIRECTIVE: Show me the current content of session_manager.py`
*   `DIRECTIVE: Run git status`

## 3. Environment Context

*   **Tech Stack:** Python 3.10+
*   **Agent Platform:** Gemini CLI.
*   **External Dependencies:** The `gemini` command must be in the system's PATH.

### Known Instabilities & Workarounds:
*   **CRITICAL BUG IDENTIFIED:** The command `gemini -` is invalid. The `subprocess.Popen` call in `session_manager.py` uses this and will fail. **This must be the first bug you fix.** The correct command is `["gemini"]`.

## 4. Mission Parameters

### Inputs:
*   The provided source code for the Gemini Bridge project.
*   Feature requirements from `docs/inception/must_should_have_features.md`.
*   Problem statement from `docs/inception/product_requirements.md`.

### Outputs:
*   A refactored codebase where all "MUST HAVE" and "SHOULD HAVE" features are correctly implemented and committed incrementally to git.
*   New `pytest` tests covering the implemented features.

### Critical Constraints:
*   Output to the user's file MUST be pure Markdown and must APPEND.
*   The application must operate with minimal terminal interaction after setup.

## 5. Task-Specific Resilient Guidelines

1.  **Fix Before Feature:** Always ensure the application is in a working state before adding new features.
2.  **Test-Driven Implementation:** For each new feature, your plan must include both the implementation and the creation of a corresponding test.
3.  **Incremental Commits:** Follow the IPEV & Checkpointing protocol for *every single feature*. Do not batch multiple features into one commit.

## 6. Success Criteria & Verification Strategy

**Mission Complete When:**
*   All 11 features from `docs/inception/must_should_have_features.md` are implemented and committed.
*   `python main.py` runs the application successfully.
*   `pytest` passes with 100% success.

**Verification Methods:**
*   `pytest` for automated testing.
*   Shell commands (`ls`, `cat`) to manually verify the end-to-end file-watching workflow.

## 7. Enhanced Execution Flow

1.  **Initialize:** Acknowledge these instructions and the new two-tiered checkpointing protocol. Perform an initial health check with `ls -F` and `git status`.
2.  **Survey (Directives):** Use `DIRECTIVE` to read `session_manager.py`, `gemini_bridge.py`, and `docs/inception/must_should_have_features.md`.
3.  **Execute Phase 1 (Critical Bug Fix):**
    *   Use the IPEV loop to fix the invalid `gemini -` command in `session_manager.py`.
    *   For your **VERIFY** step, create a new test in `test_session_manager.py` that confirms `start_session()` now works.
    *   After verification, perform the full **Checkpointing Protocol** (Code and Session).
4.  **Execute Phase 2 (Feature Implementation):**
    *   Systematically work through each "MUST HAVE" and "SHOULD HAVE" feature. For each one:
        *   Follow the full IPEV loop.
        *   Follow the full Checkpointing Protocol upon success.
        *   Wait for my "CONTINUE" signal before starting the next feature.
5.  **Final Verification:**
    *   Run the full `pytest` suite one last time.
    *   Perform a final end-to-end manual verification.
6.  **Complete:** Announce mission completion and perform a final checkpoint.

Now, begin with the initialization and survey steps.