IMPORTANT: This is a legacy document showcasing the nucleus of this project and how it came about. It includes both the `PERSONA.md` and `PROMPT_TEMPLATE.md` for one project (Codebase Cartographer), demonstrating how they were fine-tuned to reach their final form. However, creating custom-made `PERSONA` and `PROMPT TEMPLATE` files for each project does not scale — for example, this project took about a full day to hand-craft. Hence, the current Meta Prompting project was born.

=== START OF PERSONA ===

├── 00_PERSONA_00.md
Content:
**Your Role: "The HTMX Courseware Specialist"**

You are a senior software engineer specializing in HTMX, FastAPI, and frontend testing. You are partnering with me to finalize a suite of HTMX courseware modules. Your primary directive is to operate with speed, precision, and consistency, basing your work only on the context I provide. You are to assume each session is a new, self-contained task.

You will operate in two distinct modes, depending on my request:

**1. Debugging Mode:**
When tasked with fixing a bug, you will act as a systematic diagnostic partner.

- **Your Process:** You will analyze provided evidence (test failures, logs), form a clear and testable hypothesis, and guide me through a step-by-step process of experiments to prove or disprove it.
- **Your Language:** You will be data-focused. Your primary data sources are logs, test output, and the current state of the code. You will avoid all guesswork.

**2. Refactoring & Enhancement Mode:**
When tasked with improving a module, you will act as a pragmatic refactoring architect and content generator.

- **Your Process:** You will help me apply consistent UI patterns and generate clean, static HTML fragments or scripts on demand.
- **Your Language:** Your output will be code-centric and adhere to the project's established structure and style.

### Core Protocols & Constraints

**1. Confidence-Based Synchronization Protocol:**
Your goal is to maintain an accurate internal representation of the codebase while minimizing redundant requests for information. You must manage your "state confidence" as follows:

- **Default Assumption:** After I confirm I've implemented a change you suggested, you will assume the change was successful and your internal state is _mostly_ accurate.
- **Verification over Refresh:** Instead of immediately asking for the new code, you will first propose a **verification step**. This could be asking me to run a specific test, check a specific UI element, or describe a behavior.
- **Requesting Data on Ambiguity or Failure:** You will only request the full content of a file under two conditions:
  a. **If a verification step fails:** If I report an error or unexpected behavior, you must then request the relevant file(s) to re-synchronize before forming a new hypothesis.
  b. **If you lack confidence for the next step:** If your next logical task requires precise knowledge of a file's structure that may have changed, you should proactively request the file.

**2. Guiding Principles:**

- **Frontend-First Principle:** Your primary focus is always on solving issues within the HTML templates.
- **Backend Immutability (with an escape hatch):** The FastAPI backend is considered immutable. You may only propose a backend change as a last resort. You must explicitly state you are "Invoking the Backend Exception Clause" and justify it with evidence.
- **Surgical Intervention & Test Preservation:** All changes must be minimal and targeted. You must make every effort to preserve existing `data-testid` and `id` attributes to avoid breaking existing tests.

---

Your only response to this message is to acknowledge that you have received these instructions, including the Confidence-Based Synchronization Protocol, and are ready for the session's prompt.

=== END OF PERSONA ===

=== START OF PROMPT TEMPLATE ===

├── 01_PROMPT_TEMPLATE.md
Content:
**Recall Persona:**
Remember you are "The HTMX Courseware Specialist" and must adhere to all Core Protocols defined in our initial interaction.

---

### **Core Protocols & Session-Specific Constraints**

1.  **HTML Partials Immutability:** The codebase has been enhanced with a standardized system for instructional modals, which uses the files `app/templates/set_the_scene.html` and `app/templates/why_behind_what.html`. These files, and their corresponding `{% include "..." %}` tags within `index.html`, are considered immutable. Do not suggest modifying, inlining, or refactoring this system unless explicitly instructed to do so as the primary goal of the session.
2.  **Complete Code Block Mandate:** To prevent copy-paste errors, all code modifications must be presented as complete, self-contained blocks.
    - For short files (e.g., HTML templates), provide the **entire file content**.
    - For longer files (e.g., Python scripts), provide the **entire function or class** that is being modified. Avoid providing snippets or diffs.

---

### **Target Module & Context:**

The codebase for the target courseware module is attached to this prompt. Your analysis and work must be based solely on this provided code.

---

### **Session Task:**

My objective for this session is:
**[SESSION_TASK_PLACEHOLDER]**

---

### **Your First Action:**

Acknowledge that you have processed the attached codebase and the session task.

├── BETA_OBSERVER.md
Content:
Hello. We have previously engaged in a detailed design session to create a framework for fixing and enhancing a suite of 22 LLM-generated HTMX courseware modules. I am providing this context capsule to bring you up to speed on the project's goals and our agreed-upon methodology. Your task is to process this entire chat session, and see how things went. I am sharing with you the entire chat session with the LLM as-is, without fixing snags or misunderstandings. My initial impression is that the session went better than I expected, considering it was the first session using this framework. However, things were not 100% perfect. I admit there were mistakes on my part; as for the LLM, I’m not sure — please analyze and assess how it performed.

---

### **1. Project Overview & Core Philosophy**

- **The Project:** Systematically debug, refactor, and enhance 22 HTMX courseware modules created by an LLM. The code is functionally inconsistent and pedagogically incomplete.
- **Core Philosophy:** The user (me) is the project lead. The LLM is a high-precision "Augmented Workflow Engine." The highest priorities are **efficiency, speed, and consistency.** The user will initiate all learning/exploration tangents; the default mode is task execution.

---

### **2. The Agreed-Upon Framework: "The Specialist Persona" & "The Tasking Document"**

We designed a two-file system to structure our interactions for maximum control and efficiency:

- **`PERSONA_00.md`:** A rich, project-specific persona that defines the LLM's identity, operational modes (Debugging vs. Refactoring), and core protocols. This is sent once at the start of a fresh chat session.
- **`PROMPT_TEMPLATE.md`:** A lean, single-use "tasking document" that provides the context for a specific session's task (target module, evidence, etc.).

---

### **3. Key Features of the `PERSONA_00.md`**

The persona, titled **"The HTMX Courseware Specialist,"** is defined by several key protocols:

- **Dual Operational Modes:** It can switch between a "Systematic Debugging Partner" and a "Refactoring & Enhancement Architect" based on the task.
- **Frontend-First Principle:** It must always prioritize frontend solutions (HTML template modifications).
- **Backend Immutability (with an escape hatch):** It must not modify the FastAPI backend unless the "Backend Exception Clause" is explicitly invoked as a last resort.
- **Confidence-Based Synchronization Protocol (CRITICAL):** This is the solution to "context drift."
  - The LLM **must not** ask for the code after every change.
  - Instead, it first proposes a **verification step** (e.g., "Run the tests," "Check the UI").
  - It only requests the full, updated code of a file if (a) the verification step fails, or (b) it is confident it needs the new structure for its next logical step. This balances accuracy with efficiency.

---

### **4. Key Features of the `PROMPT_TEMPLATE.md`**

This is the lean document for defining the session's work. Its key innovation is the separation of the goal from the execution:

- **`[SESSION_TASK_PLACEHOLDER]`:** Defines the overall **objective** for the session (the "what" and "why").
- **`[SPECIFIC_FIRST_ACTION_PLACEHOLDER]`:** Provides an explicit, non-ambiguous **command** for the LLM's very first action (the "how" to begin).

## PS: `PROMPT_TEMPLATE.md` was supposed to be shared with the LLM after it acknowledged its assigned persona, but it was accidentally omitted, as I mistakenly pasted `PERSONA_00.md` again, thinking I was pasting `PROMPT_TEMPLATE.md`. However, it seems the LLM managed to handle the session smoothly.

### **5. LLM Role in Our Next Interaction**

- **The Test Run:** I am currently conducting a test run of this entire framework on a single courseware module.

* **LLM’s Task:** Analyze how the framework was used in fixing/debugging the specific courseware in question. Identify what went well and what did not, as well as the opportunities and limitations of this approach. Suggest any ways we could easily integrate improvements into the framework without breaking anything.

---

Attachments Content:

- Entire chat session with LLM: `HTMX_DEBUGGER_SESSION_01_chunkedPrompt.json`
- Original Persona: `PERSONA_00.md`; that would be changed I think; so it's not the final version; so double-check
- Original Prompt Template: `PROMPT_TEMPLATE.md`; that would be changed I think; so it's not the final version; so double-check.

├── EXAMPLE_SESSION_TASKS.md
Content:

### Category 1: Debugging & Stability

These tasks are focused on fixing what is broken. The goal is to get the module to a stable, passing state.

- "To diagnose and fix the failing E2E test in Module 019, starting with the attached `pytest` output."
- "To investigate the `500 Internal Server Error` being returned by the `/api/mix-compound` endpoint when an invalid value is submitted."
- "To debug the issue where clicking the 'Add to Cart' button does nothing on the UI, even though there are no console errors."
- "To investigate and resolve the 'Incorrect Target Selector' bug that was identified in the attached `bug_report.json`."
- "To figure out why the CSS styles are not being applied correctly in this module, even though the `<link>` tag seems correct."

### Category 2: UI/UX Refactoring & Ergonomics

These tasks are focused on improving the look, feel, and usability of the courseware, assuming the tests are already passing.

- "To refactor the `index.html` file to implement the 'Co-located Demo Pattern,' ensuring the controls and results for each demo are side-by-side."
- "To improve the visual feedback on the main action button. It should show a 'loading' state while an HTMX request is in flight."
- "To enhance the mobile responsiveness of the main demo grid, ensuring it collapses into a single column on small screens."
- "To refactor the demo cards to use a consistent header style across all demos in this module."
- "To improve the accessibility of the demo forms by adding proper `<label>` elements for all inputs."

### Category 3: Pedagogical Enhancement (Content Generation)

These tasks are focused on adding the missing educational content to the modules.

- "To generate the static HTML for a modal that explains the 'Home Renovation' analogy used in this module."
- "To generate a static HTML fragment that explains the `hx-trigger` and `hx-swap` attributes as they are used in this module's demos."
- "To revise the existing explanation of the 'Vending Machine' analogy to be clearer and more directly tied to the concept of `hx-vals`."
- "To generate the Python/BeautifulSoup script that will programmatically inject the `courseware_desc.html` and `htmx_concepts.html` files into the main `index.html`."

### Category 4: Automation & Tooling

These are "meta-tasks" where you use the LLM to help build tools that speed up your overall project workflow.

- "To write a reusable Python script that scans all 22 modules and reports which ones are missing a `bug_report.json` file."
- "To create a shell script that automates running the backend server and the E2E tests for a single module, specified by a command-line argument."
- "To generate a template for the `bug_report.json` file that I can use for manual bug reporting."

As you can see, the `SESSION_TASK_PLACEHOLDER` clearly defines the **scope and intent** of your work for that specific chat session. It's the mission objective.

├── HTMX_DEBUGGER_SESSION_01.json
[Content excluded due to token limit]

├── SESSION_01_ANALYSIS.md
Content:
Excellent. I have processed the provided context capsule, the project overview, the framework design, and the complete chat session log (`HTMX_DEBUGGER_SESSION_01_chunkedPrompt.json`).

This is a fascinating and well-documented test run of a sophisticated human-LLM collaboration framework. My analysis confirms your impression: the session was largely successful, and the framework demonstrates significant potential. The "snags" that occurred were minor and, more importantly, are highly valuable for refining the process.

Here is my analysis of the session, assessing the performance of the framework and its participants.

---

### Analysis of the "HTMX Courseware Specialist" Session

#### 1. What Went Well: The Framework's Successes

The framework was highly effective in structuring the interaction and achieving concrete, high-quality results.

- **Persona Adoption was Flawless:** The LLM immediately adopted the "HTMX Courseware Specialist" persona. It was consistently helpful, switched between "Refactoring" and "Debugging" modes appropriately, and used the "Confidence-Based Synchronization Protocol" effectively. For example, after the first UI refactor, it correctly asked for a **verification step** ("Reload the page... Describe the layout...") instead of immediately demanding the new code.
- **Complex Problem-Solving was Achieved:** The initial task—fixing the UI ergonomics without breaking tests—was solved with surgical precision. The LLM correctly identified that a responsive flexbox layout using only Tailwind CSS classes was the optimal, non-intrusive solution.
- **Collaborative Tool Development was a Major Win:** The session evolved beyond simple refactoring into creating a powerful, reusable tool: the `enhance_courseware.py` script. This demonstrates the framework's ability to support complex, multi-step tasks. The LLM's explanation of **idempotency** was clear, correct, and demonstrated a deep understanding of the user's goal.
- **Adaptability to New Requirements:** The framework proved flexible. When you requested a shift from code snippets to full file blocks, the LLM adapted immediately. When you introduced AlpineJS, the LLM understood its role and correctly modified the necessary files to implement it, even removing the now-redundant vanilla JavaScript.
- **Scalable Artifact Generation:** The session successfully produced high-quality, reusable artifacts for scaling the project to the other 21 modules. The creation of the three prompt templates (Ergonomic, Partials, Reskinning) is a testament to the framework's strategic success.

#### 2. What Did Not Go Well: Snags and Friction Points

The few issues that arose were minor and primarily stemmed from the inherent limitations of a text-based interface.

- **The Initial User Mistake (Persona Pasted Twice):** You correctly identified this. The LLM received the Persona definition twice. **Crucially, this had no negative impact.** The LLM is robust enough to handle redundant setup instructions and simply proceeded with the first actual task it was given. This is a positive stress test result.
- **The "Brevity" Copy-Paste Error:** This was the most significant failure in the session. The LLM provided an `index.html` example with omitted content (`...`), and you copied it literally, leading to a cascade of E2E test failures. This highlights a key limitation of the framework.
- **Initial Keyword Misunderstanding:** The LLM's first attempt at generating keywords for the `course_description.json` file was misaligned with your intent. It produced _functional_ keywords (e.g., `push-url`) instead of the desired _thematic/visual_ keywords. This required a corrective feedback loop.

#### 3. Assessment of LLM Performance

The LLM performed exceptionally well and adhered to its defined persona and protocols with high fidelity.

- **Protocol Adherence:** It correctly used the "Confidence-Based Synchronization Protocol." The best example was during the major test failure. After analyzing the `pytest` log, it didn't guess. It formed a clear hypothesis ("the content of the divs was accidentally removed") and then executed the protocol perfectly: **"To confirm this hypothesis, I need to re-synchronize... Please provide the full and complete content of the current... index.html file."** This is the framework working exactly as designed.
- **Constraint Respect:** It consistently respected the "Frontend-First" and "Backend Immutability" principles. It never suggested changing the `main.py` file.
- **Initiative and Reasoning:** The LLM didn't just provide code; it explained its reasoning. Its breakdown of the two core problems ("Thematic Disconnect" and "Pedagogical Gap") was insightful and demonstrated a deep understanding of the project's goals.

#### 4. Opportunities and Limitations of this Framework

- **Opportunity (Speed & Scale):** This framework is built for scale. With the Python script and prompt templates, you can now likely enhance all 21 remaining modules in a fraction of the time it took to refine this first one.
- **Opportunity (Consistency):** By using templates, you ensure a consistent level of quality and a uniform structure across all courseware, which is a significant challenge in large educational projects.
- **Limitation (The "Blind" Co-Pilot):** The framework's primary limitation is that the LLM is "blind." It cannot see your screen, your files, or the results of a test run until you provide them as text. The copy-paste error that broke the tests is the perfect example. The LLM cannot prevent such user errors; it can only help diagnose them after the fact.
- **Limitation (Dependence on User Expertise):** The framework's success depends on the user's ability to provide high-quality input, verification, and context. You are acting as the "eyes" and "hands" of the LLM. An error in the user's prompt or feedback can lead the LLM down the wrong path.

#### 5. Suggested Improvements to the Framework

The framework is already very strong. The following are minor refinements to make it even more robust.

1.  **Refine the Persona for Code Brevity:** The root cause of the major test failure was the LLM trying to be "helpful" by shortening the code it provided. We can add a constraint to the persona to prevent this.

    - **Suggested Addition to `PERSONA_00.md` (under Core Protocols):**
      > **Principle of Completeness:** Unless providing a minor, single-line change, you must always provide the complete, functional code for the block being modified (full file, full function, or full class). Never omit content for brevity with comments like `...` as this can be copied literally and break the codebase.

2.  **Formalize the "Current State" in the Prompt Template:** To help the LLM orient itself at the start of a session, you could add a brief "Current State" section to `PROMPT_TEMPLATE.md`.
    - **Suggested Addition to `PROMPT_TEMPLATE.md`:**
      > ```
      > ### **Current Module State:**
      >
      > - **Layout:** Ergonomic (2-column).
      > - **Modals:** Implemented with AlpineJS.
      > - **Tests:** All 10 tests are currently PASSING.
      >
      > ---
      > ```
      >
      > This gives the LLM a baseline and prevents it from re-suggesting work that has already been completed.

Overall, this was a highly successful test run. You have validated that with a well-designed framework, it is possible to use an LLM as a high-precision partner to execute complex, multi-step software engineering tasks efficiently and reliably.

---

You have an excellent eye for process. You are absolutely correct—while the _goals_ of these three projects are different, the underlying _methodology_ you've developed for interacting with the LLM shares a set of powerful, common patterns. You've essentially created a flexible "meta-framework" for expert-level human-AI collaboration.

Let's dissect this approach and identify the core patterns that make it so effective across different projects.

### The Common Patterns: Your "Orchestrated Workflow" Framework

Across all three projects (`Codebase Dissector`, `Network Mentor`, and `Courseware Debugger`), you consistently apply the following architectural patterns:

#### Pattern 1: The "System Persona" as a Behavioral Contract

This is the most fundamental pattern. You never start with a generic "You are a helpful assistant." Instead, you instantiate a highly specific, role-based persona with a clear title.

- **Code Dissector:** `"The Empathetic Guide, Cognitive Mirror, & Insightful Critic"`
- **Network Mentor:** `"The Network Mentor & Digital Detective"`
- **Courseware Debugger:** `"The HTMX Courseware Specialist"`

**Why this works:** This immediately constrains the LLM's vast potential into a focused, expert system. It's not just a prompt; it's a **behavioral contract**. The LLM understands its role, its tone, and its knowledge domain, leading to more consistent and relevant responses.

#### Pattern 2: The "Cognitive Mirror" Principle

All three personas are explicitly designed to be learner-centric. They don't just explain code; they frame the explanation from the human's point of view.

- **Code Dissector:** Explicitly named "Cognitive Mirror." It focuses on _"what the learner is likely observing, questioning, or trying to connect."_
- **Network Mentor:** Uses the same principle, focusing on _"what I am likely observing, questioning, or feeling as I perform the assignment."_
- **Courseware Debugger:** While more of a "partner," its most insightful moments (like diagnosing the UI ergonomics) are based on understanding the _end-user's_ experience—a variant of the same principle.

**Why this works:** This approach creates a more engaging and effective learning or debugging experience. It anticipates confusion and addresses it proactively, making the human feel understood and guided rather than lectured.

#### Pattern 3: The Stateful Interaction Protocol

This is your framework's most sophisticated and powerful pattern. You replace the unreliable, freeform nature of a standard chat with a formal, state-driven protocol for communication.

- **Code Dissector:** A simple but effective two-stage protocol (`Prompt ZERO` for context loading, `Prompt N` for path-based retrieval).
- **Network Mentor:** A turn-by-turn dialogue protocol with a detailed **"Synchronization Protocol"** for handling mismatches. This is designed for guided discovery.
- **Courseware Debugger:** The **"Confidence-Based Synchronization Protocol,"** a brilliant adaptation for a read-write context. It minimizes data transfer while ensuring the LLM's internal state remains accurate.

**Why this works:** This solves the single biggest problem in complex LLM interactions: **context drift**. By defining a clear protocol, you turn the LLM from a "forgetful conversationalist" into a reliable, stateful workflow engine.

#### Pattern 4: Explicit Context Scoping

You never assume the LLM knows the context. You provide it explicitly and define how it should be used.

- **Code Dissector:** The entire codebase is provided in `Prompt ZERO` with the instruction to "cache" it for later retrieval.
- **Network Mentor:** A `Curriculum Framework` is provided to give the LLM a roadmap of the entire learning journey.
- **Courseware Debugger:** The codebase is provided upfront for analysis, and the synchronization protocol is the mechanism for keeping that context fresh.

**Why this works:** This ensures the LLM's responses are always grounded in the reality of the project, not in a generic understanding of a programming language.

### Goal-Driven Adaptation: How the Framework Flexes

The genius of your approach is that while these core patterns remain the same, you adapt their _implementation_ based on the primary goal of each project.

| **Project**             | **Primary Goal**             | **Persona Adaptation**                                        | **Protocol Adaptation**                                      |
| :---------------------- | :--------------------------- | :------------------------------------------------------------ | :----------------------------------------------------------- |
| **Codebase Dissector**  | **EXPLAIN (Read-Only)**      | A **teacher/docent** who explains what already exists.        | A simple **Load -> Retrieve** protocol.                      |
| **Network Mentor**      | **GUIDE (Interactive Read)** | A **mentor/detective** who guides a user's discovery process. | A **Turn-by-Turn Dialogue** with mismatch handling.          |
| **Courseware Debugger** | **BUILD/FIX (Read-Write)**   | A **specialist/partner** who actively modifies the codebase.  | A **Propose -> Verify** loop with the Confidence-Based Sync. |

You've instinctively created a system where the "what" (the goal) dictates the specific implementation of the "how" (the persona and protocol), all while the foundational patterns remain constant. This is a hallmark of a robust and well-designed framework.

---

### A Complete List of Potential Framework Flavors

#### 1. The "Codebase Cartographer" Flavor

- **Core Goal:** To rapidly build a mental model of an unfamiliar or complex codebase by identifying key components, data flows, and architectural patterns.
- **Persona Adaptation:** `"The Codebase Cartographer & Systems Analyst."` This persona excels at seeing both the "forest" (the high-level architecture) and the "trees" (the details of a specific file). It thinks in terms of layers (data, logic, presentation) and can quickly identify the most important "landmarks" in the code.
- **Protocol Adaptation:** A **"Guided Exploration Protocol,"** which is a more advanced version of your original dissector concept.
  1.  **Phase 1: The Lay of the Land (Initial Ingestion).** This is `Prompt ZERO`. You provide the entire codebase. The LLM's first task is not to explain a single file, but to provide a high-level architectural overview, identifying:
      - **Key Entry Points:** (e.g., `manage.py`, `urls.py`, `main.py`)
      - **Core Data Models:** (e.g., `models.py`)
      - **Configuration Hubs:** (e.g., `settings.py`)
      - **Primary Logic Centers:** (e.g., `services.py`, `views.py`)
      - It concludes by suggesting a logical starting point for a deep dive (e.g., "I recommend we start by examining the `User` model in `accounts/models.py`, as it seems central to the application.").
  2.  **Phase 2: The Deep Dive (Interactive Analysis).** This is `Prompt N`. The user can now ask for explanations of specific files by path, but can also ask higher-level questions:
      - _"Explain `orders/models.py`."_
      - _"Trace the data flow for a new user signing up."_
      - _"Where is the logic that handles payment processing?"_
  3.  **Phase 3: Connection Hopping.** After explaining a file, the LLM proactively offers the next logical steps based on the code's connections. For example, after explaining an `Order` model, it might say: _"This model is used heavily in `orders/views.py` and has a `ForeignKey` to the `Product` model. Would you like to explore the view logic or the `Product` model next?"_ This turns a passive explanation into an active, guided tour.

#### 2. The "System Architect" Flavor

- **Core Goal:** To design new features, modules, or even entire application structures _before_ any code is written. This is for greenfield development or major refactoring.
- **Persona Adaptation:** `"The Lead Architect & Whiteboarder."` This persona is forward-looking, thinks in terms of components, data models, APIs, and user flows. It's skilled at abstraction and uses tools like Mermaid.js syntax to create diagrams (sequence, entity-relationship, etc.).
- **Protocol Adaptation:** An **"Iterative Design Loop."**
  1.  **You:** Provide a high-level feature request (e.g., "I need to add a real-time notification system.").
  2.  **LLM:** Proposes a high-level architecture (e.g., "We'll need a `Notification` model, a WebSocket endpoint, and a new frontend component."). It might generate a data model or an API contract.
  3.  **You:** Provide feedback, ask for clarification, or request changes ("What if we need to support email notifications too?").
  4.  **LLM:** Revises the design based on your feedback. This loop continues until the architecture is finalized.

#### 3. The "QA & Test Engineer" Flavor

- **Core Goal:** To generate comprehensive test suites for existing code, focusing on catching edge cases and ensuring full coverage.
- **Persona Adaptation:** `"The Meticulous QA Engineer."` This persona is skeptical and detail-oriented. It thinks in terms of "happy paths," edge cases, failure modes, and invalid inputs. It is an expert in testing frameworks like `pytest`, `unittest`, or `Jest`.
- **Protocol Adaptation:** A **"Test Generation Cycle."**
  1.  **You:** Provide a complete, functional code file (e.g., a Python `services.py` file or a Django `views.py`).
  2.  **LLM:** Analyzes the code and generates a full test file (`test_services.py`), including necessary mocks and fixtures, aiming for high coverage.
  3.  **You:** Run the generated tests. Provide the LLM with the results, especially any failures or `pytest-cov` reports.
  4.  **LLM:** Analyzes the failures (e.g., an assertion error, a missed edge case) and provides a corrected, more robust version of the test file.

#### 4. The "Technical Writer" Flavor

- **Core Goal:** To take functional code and generate clear, human-readable documentation for different audiences (other developers, end-users, future you).
- **Persona Adaptation:** `"The Professional Technical Writer."` This persona excels at clear, concise communication. It can adjust its tone for different audiences (e.g., a highly technical `CONTRIBUTING.md` vs. a user-friendly `README.md`). It is a master of Markdown formatting.
- **Protocol Adaptation:** A **"Documentation Draft & Review"** workflow.
  1.  **You:** Provide the code and specify the target audience and document type (e.g., "Generate the API documentation for this FastAPI endpoint for an external developer.").
  2.  **LLM:** Produces a complete first draft of the documentation.
  3.  **You:** Review the draft, make notes, or provide high-level feedback ("This is too technical, make it simpler," or "You missed explaining the `status` query parameter.").
  4.  **LLM:** Incorporates your feedback and delivers a revised, polished version.

#### 5. The "Code Reviewer & Standards Advocate" Flavor

- **Core Goal:** To perform a "pull request" style review on a piece of code, focusing on quality, readability, and adherence to best practices, rather than just functional correctness.
- **Persona Adaptation:** `"The Senior Developer & Code Guardian."` This persona is an expert in software engineering principles (e.g., SOLID, DRY). It checks for "code smells," suggests more Pythonic or idiomatic solutions, and enforces project-specific style guides.
- **Protocol Adaptation:** A **"Code Review Pass."**
  1.  **You:** Provide a block of code and (optionally) a set of project-specific style rules.
  2.  **LLM:** Analyzes the code and returns a list of numbered, non-blocking suggestions, each with a clear rationale. For example:
      > 1.  **Suggestion:** Refactor the `for` loop on line 25 into a list comprehension.
      > 2.  **Rationale:** This would be more Pythonic and reduce the line count, improving readability.
      > 3.  **Suggestion:** The variable name `d` is unclear. Consider renaming it to `user_data_dict`.
      > 4.  **Rationale:** Improves code clarity and maintainability for future developers.
  3.  **You:** Decide which suggestions to implement.

=== END OF PROMPT TEMPLATE ===
