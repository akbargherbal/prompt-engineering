Here is the complete, user-ready Markdown content for the worksheet.

***

# **Step 4: The Assembly Line**
## Assembling Your Simulation Prompt

Welcome to the final phase of your "Mise en Place." You've done the hard work of introspection and preparation: you've articulated the problem in **The Pain Journal**, gathered your facts in **The Evidence Locker**, and defined the boundaries in **The Rulebook**. Now, on The Assembly Line, we bring it all together. This is where we transform your raw materials into a complete, structured briefing for the AI. A well-assembled prompt is the difference between a generic, unhelpful response and a simulation so accurate it feels like you're collaborating with an expert who can read your mind.

---

### **1. The Persona: Who is the Simulator?**

**Why this is important:** Before you give an instruction, you must establish *who* you're talking to. By assigning the LLM a specific, expert persona, you're priming it to access a specialized set of skills, vocabulary, and problem-solving patterns. You're not asking a generalist for help; you're commissioning a specialist for a solution. This step dramatically improves the quality and relevance of the output.

**Your Question:** Based on the problem you're solving, what expert persona should the AI adopt? Think about the ideal team member you would hire for this specific task. Be descriptive about their skills and mindset.

> _Example: "You are an expert Senior Python Developer specializing in data engineering and automation. You have deep experience building robust, efficient, and maintainable scripts for parsing large text files, handling system logs, and ensuring data integrity. You write clean, well-documented, and production-ready code that follows best practices for error handling and memory management."_

> **Define the Persona for your AI Simulator:**
>
> ```
> [Your answer here]
> ```

---

### **2. The Context: Where is the Problem?**

**Why this is important:** An expert can't work in a vacuum. The Context section grounds the simulation in reality by providing the "world" in which the problem exists. This is where you bring in the crucial artifacts from your **Evidence Locker**. By providing specific code snippets, log formats, file structures, and environmental details, you give the AI the same situational awareness a human developer would need.

**Your Question:** Look back at your **Evidence Locker**. Synthesize the most critical pieces of information the AI must have to understand the environment. What does the file system look like? What is the exact format of the input data? Are there existing code snippets it needs to be aware of?

> _Example: "I am working in a project directory that contains a script and a log file.
> 1.  **Log File (`processor_log.txt`):** This file contains logs from a job processing system. Lines are timestamped. Key lines are `[INFO]`, `[WARN]`, and `[ERROR]`.
> 2.  **Error Log Format:** The specific lines we care about follow this exact format: `YYYY-MM-DD HH:MM:SS [ERROR] JobID: {id} failed. Reason: {text_reason}`. The `{id}` is an alphanumeric string.
> 3.  **Goal:** To extract the `{id}` from every `[ERROR]` line and save them for a re-run."_

> **Describe the essential context for your simulation:**
>
> ```
> [Your answer here]
> ```

---

### **3. The Task: What is the Goal?**

**Why this is important:** This is the core directive. It transforms the frustration you documented in your **Pain Journal** into a clear, specific, and actionable goal for the AI. Ambiguity is the enemy of a good simulation. Your task description must be a precise instruction that leaves no room for misinterpretation about the primary objective.

**Your Question:** Using the problem you detailed in **The Pain Journal**, write a clear and concise description of the task you want the AI to perform. Explain what needs to be created, what it should do, and what the final output should be.

> _Example: "Your task is to write a complete Python script named `extract_failed_jobs.py`. This script must:
> 1.  Read the log file named `processor_log.txt` from the same directory.
> 2.  Parse the file line-by-line to find all entries containing `[ERROR]`.
> 3.  For each error line found, extract the `JobID`.
> 4.  Write all of the extracted `JobID`s into a new file named `rerun_queue.csv`, with each ID on a new line."_

> **Define the specific task for your simulation:**
>
> ```
> [Your answer here]
> ```

---

### **4. The Rulebook: What are the Rules of the Game?**

**Why this is important:** This is where you inject the "Physics of Reality" you defined in **The Rulebook** worksheet. Without rules, the AI might produce a solution that is technically correct but practically useless. Constraints, Success Criteria, and Anti-Goals are the essential guardrails that steer the simulation toward a solution that is not only correct but also efficient, maintainable, and aligned with your project's real-world requirements.

**Your Question (Part A - Constraints):** What are the non-negotiable constraints, limitations, and requirements the solution must adhere to? (e.g., programming language, libraries, performance limits).

> _Example:
> - The script must be written in Python 3.9+.
> - It must **not** use any external libraries or packages (e.g., no Pandas or Regex libraries if you want to avoid them); it should rely only on Python's standard library.
> - The script must be memory-efficient and not load the entire log file into memory at once, as the file can be several gigabytes in size.
> - The file paths for input and output should be defined as constants at the top of the script, not hardcoded in the main logic._

> **List your project's constraints:**
>
> ```
> [Your answer here]
> ```

**Your Question (Part B - Success Criteria):** What are the precise, measurable conditions that define a successful outcome? How will you know, without a doubt, that the generated solution is correct?

> _Example:
> - The script runs successfully without any errors.
> - A file named `rerun_queue.csv` is created.
> - The `rerun_queue.csv` file contains the *exact* JobIDs from the `[ERROR]` lines and *only* those JobIDs.
> - The original `processor_log.txt` file is left unchanged._

> **List your simulation's success criteria:**
>
> ```
> [Your answer here]
> ```

**Your Question (Part C - Anti-Goals):** What specific outcomes, approaches, or patterns should the AI actively avoid? What would make a solution a failure, even if it seems to work at first glance?

> _Example:
> - **Do not** extract JobIDs from `[INFO]` or `[WARN]` lines.
> - **Do not** include any other text in the output CSV, just the JobIDs.
> - **Do not** write a solution that is difficult to read or lacks comments explaining the logic.
> - **Do not** ask me clarifying questions; use the context provided and make reasonable assumptions if necessary, stating them in the code comments._

> **List your simulation's anti-goals:**
>
> ```
> [Your answer here]
> ```

---

### **5. Final Review: The Complete Prompt**

**Why this is important:** You are about to launch the simulation. This is your final pre-flight check. By assembling all the pieces into one cohesive prompt and reading it aloud, you can spot gaps, ambiguities, or contradictions. This single block of text is the culmination of your preparation—a perfect, self-contained blueprint for the AI to execute.

**Your Final Step:** Combine all your answers from sections 1-4 into the text area below. Read the entire prompt from top to bottom. Does it make perfect sense? Is it clear, complete, and unambiguous? If you were a new developer on the team, would you know exactly what to do? Refine it until the answer is a confident "yes."

> **Assemble your complete, final prompt for the LLM Simulator here:**
>
> ```
> [Paste and refine your Persona, Context, Task, and Rulebook answers into a single, cohesive prompt here. Use Markdown for clarity, like # Persona, # Task, etc.]
> ```