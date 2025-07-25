Here is the complete, user-ready Markdown content for "The Assembly Line" worksheet.

---

# **The Simulation Starter Kit**
## **Step 4: The Assembly Line**

***

You’ve done the hard work of preparation. You’ve documented your pain, gathered your evidence, and defined the rules of the game. Now, in this final step of your "Mise en Place," we bring it all together. This worksheet is your assembly line, a structured process to combine all your raw materials into a single, high-fidelity prompt that will command the LLM to act as a powerful Systems Simulator.

A great simulation isn't about a clever one-line request; it's about providing a complete, well-structured "world" for the LLM to operate within. By assembling your inputs here, you ensure the AI has the role, the context, the goal, and the constraints it needs to deliver an exceptional, system-aware solution. Let's build your final prompt.

### **4.1 The Persona: Defining Your Expert Simulator**

**Why this is important:** Before you give the LLM a task, you must give it a job. By assigning a specific, expert persona, you prime the model to access a more specialized and relevant set of knowledge and reasoning patterns. You're not just asking for code; you're asking for the professional judgment of a seasoned expert who has solved this exact type of problem before.

**Your Question:** What specific, expert role should the AI adopt for this simulation? Be precise. Think about seniority, specialization, and the tools they would master.

> _Example: You are a Principal DevOps Engineer with a decade of experience in building resilient, automated data processing pipelines. You are a master of Python scripting for infrastructure tasks and believe in clear, maintainable, and dependency-free code._
>
> **Write the persona for your simulator here:**
>
> ```
>
> ```

### **4.2 The Context: Grounding the Simulation in Reality**

**Why this is important:** This is where your **Evidence Locker** comes into play. An LLM without context will hallucinate solutions for a generic, imaginary system. To get a solution for *your* system, you must provide the "state of the world" as it exists right now. This includes the exact code, file structures, log formats, and error messages that define the problem space. This grounds the simulation in reality.

**Your Question:** From your Evidence Locker worksheet, assemble all the relevant source code, log snippets, file directory structures, and error messages. Be as complete and precise as possible. It's better to provide too much context than too little.

> _Example:_
> _"Here is the context of my current system._
>
> _**The problematic script, `run_job.py`:**_
> ```python
> # run_job.py
> import random
> def run_data_job(job_id):
>   # Simulates a job that can fail
>   if random.random() > 0.7:
>     print(f"ERROR: Job {job_id} failed due to a transient network error.")
>     return False
>   print(f"SUCCESS: Job {job_id} completed.")
>   return True
> ```
>
> _**The log file it produces, `job_output.log`:**_
> ```log
> SUCCESS: Job A113 completed.
> SUCCESS: Job B921 completed.
> ERROR: Job C457 failed due to a transient network error.
> SUCCESS: Job D833 completed.
> ERROR: Job E109 failed due to a transient network error.
> ```
>
> _**The project file structure:**_
> ```
> /project/
> |-- run_job.py
> |-- job_output.log
> ```
>
> **Write or paste your full context here:**
>
> ```
>
> ```

### **4.3 The Goal: Defining the Core Task**

**Why this is important:** Drawing directly from your **Pain Journal**, this is where you articulate the central objective. After understanding its role and the world it's in, the AI needs a clear, singular mission. What is the one thing you want it to accomplish? A vague goal leads to a vague solution. A precise goal leads to a precise and actionable output.

**Your Question:** What is the single, primary objective you want the AI to accomplish in this simulation? Describe the desired outcome.

> _Example: Your task is to write a new, standalone Python script named `remediate_logs.py`. This script must parse the `job_output.log` file, identify all the `job_id`s for jobs that FAILED, and generate a new JSON file named `rerun_jobs.json` containing a list of only the failed job IDs to be re-processed._
>
> **Write the core goal for your simulation here:**
>
> ```
>
> ```

### **4.4 The Rules: Establishing the "Physics of Reality"**

**Why this is important:** This is where your **Rulebook** becomes the law of the land for the simulation. Constraints are not limitations; they are guide rails that ensure the AI’s solution is practical, compliant, and useful in *your* specific environment. By defining what the solution *must* do (Success Criteria) and what it *must not* do (Anti-Goals), you define the "physics" of the solution space.

**Your Question:** What are the absolute, non-negotiable success criteria and constraints from your Rulebook?

> **Part A: Success Criteria (What it MUST do):**
> _Example:_
> _- The script must be written in Python 3.8+._
> _- It must use ONLY standard libraries included with Python (no `pip install <package>`)._
> _- It must produce a JSON file `rerun_jobs.json` in the format: `{"jobs_to_rerun": ["C457", "E109"]}`._
> _- The code must be well-commented to explain the logic._
>
> **Write your non-negotiable success criteria here:**
>
> ```
>
> ```
>
> **Part B: Constraints & Anti-Goals (What it MUST NOT do):**
> _Example:_
> _- The script must NOT modify the original `job_output.log` file in any way._
> _- The script must NOT attempt to re-run the jobs itself; it only prepares the data for the rerun._
> _- Do NOT use the `pandas` or `regex` libraries. Solve it using basic string and file operations._
>
> **Write your hard constraints and anti-goals here:**
>
> ```
>
> ```

### **4.5 The Blueprint: Specifying the Final Output**

**Why this is important:** The final step is to leave nothing to chance. You must tell the simulator *exactly* how you want the solution delivered. Should it be a single code block? Should it include an explanation? Should it be formatted as a specific file? A clear output blueprint ensures you get a finished product, not just a casual suggestion.

**Your Question:** How, specifically, should the AI present its final output? Define the format, structure, and any required comments or explanations.

> _Example: Present the final solution as a single, complete Python script inside a Markdown code block. The script should be ready to be saved as `remediate_logs.py` and run. Following the code block, provide a brief section under a `### Rationale` heading that explains your key design choices, such as why you chose a specific method for parsing the file._
>
> **Define your desired output format here:**
>
> ```
>
> ```

***

**Congratulations!** You have completed your Developer's Mise en Place. You have systematically transformed a vague, recurring pain into a precise, context-rich, and rules-based simulation request. You can now copy and paste the contents of these sections, in order, into your chosen LLM. You are no longer just asking for code; you are initiating a high-fidelity systems simulation.