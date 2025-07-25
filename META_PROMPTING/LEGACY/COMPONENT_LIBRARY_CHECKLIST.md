# Checklist: Component Library for the LLM Orchestration Engine

**DOCUMENT PURPOSE:**
This document serves as the project roadmap and "Bill of Materials" for the META_PROMPTING Component Library. Each item represents a single text snippet to be generated using the `PROMPT_SNIPPET_GENERATOR.md` template. The `Description` for each item is the exact text to be used in the "Component Description & Goal" field of the generator prompt.

---

### **Category 1: Personas**
*These snippets define the LLM's role, tone, and core identity.*

-   **File:** `personas/empathetic_guide.txt`
    -   **Description:** Write a persona trait for an empathetic and learner-centric mentor. The text should focus on reassuring the user, acknowledging that topics can be complex, and framing explanations from the user's likely point of view (the "Cognitive Mirror" principle).

-   **File:** `personas/precise_partner.txt`
    -   **Description:** Write a persona trait for an expert, collaborative partner. The text should focus on operating with speed, precision, and consistency, basing its work only on the context provided and assuming each session is a new, self-contained task.

-   **File:** `personas/meticulous_auditor.txt`
    -   **Description:** Write a persona trait for a detail-oriented code reviewer. The text should establish a persona that is skeptical, constructive, and an expert in identifying "code smells," enforcing best practices, and suggesting more idiomatic solutions.

---

### **Category 2: Protocols**
*These snippets define the rules of engagement and the interaction model.*

-   **File:** `protocols/confidence_based_sync.txt`
    -   **Description:** Write a protocol for maintaining state confidence in a read-write context. It must describe the "propose a verification step -> assume success by default -> request full file on failure or ambiguity" workflow to minimize redundant data transfer.

-   **File:** `protocols/turn_by_turn_dialogue.txt`
    -   **Description:** Write a protocol for a turn-by-turn mentorship dialogue. It must describe the core loop: "1. Ask the user to perform a single, small action. 2. Wait for the user's response. 3. Analyze the provided clue and explain its significance. 4. Initiate a checkpoint to ensure understanding before proceeding."

-   **File:** `protocols/code_review_pass.txt`
    -   **Description:** Write a protocol for delivering a code review. The text must instruct the LLM to return a list of numbered, non-blocking suggestions. Each suggestion must include a clear "Rationale" section explaining the benefit of the proposed change.

-   **File:** `protocols/connection_hopping.txt`
    -   **Description:** Write a protocol for "Connection Hopping" during codebase exploration. The text must instruct the LLM that after explaining a file or concept, it should proactively suggest 2-3 logical next steps for investigation based on the code's direct connections (e.g., function calls, class imports, foreign keys).

---

### **Category 3: Constraints**
*These snippets define non-negotiable rules to protect the integrity of the output.*

-   **File:** `constraints/preserve_functional_attributes.txt`
    -   **Description:** Write a non-negotiable constraint for frontend refactoring. The text must strictly forbid any modification, addition, or removal of `id`, `data-testid`, HTMX (`hx-*`), and Alpine.js (`x-*`, `@*`, `:*`) attributes to ensure tests and functionality are preserved.

-   **File:** `constraints/no_html_restructure.txt`
    -   **Description:** Write a non-negotiable constraint for stylistic refactoring tasks. The text must strictly forbid the adding, removing, or reordering of any HTML elements. The only permitted change is the modification of `class` attributes.

-   **File:** `constraints/no_backend_changes.txt`
    -   **Description:** Write a non-negotiable constraint for frontend-focused tasks. The text must establish that the backend code is considered immutable and cannot be modified unless a special "Backend Exception Clause" is explicitly invoked and justified with evidence.

-   **File:** `constraints/output_raw_code_only.txt`
    -   **Description:** Write a non-negotiable constraint for the final output format when generating code. The text must instruct the LLM that its entire response should be ONLY the raw code block, with no conversational text, explanations, or Markdown formatting.

-   **File:** `constraints/principle_of_completeness.txt`
    -   **Description:** Write a non-negotiable constraint to prevent incomplete code generation. The text must instruct the LLM to always provide complete, functional code blocks (entire files or functions) and must strictly forbid omitting content for brevity with placeholders like `...`.