### **Step 4: The Assembly Line**

This is the final and most crucial stage of your "Mise en Place." All the careful preparation you've done in The Pain Journal, The Evidence Locker, and The Rulebook now comes together. On this assembly line, you will piece together each component to build a structured, comprehensive, and powerful prompt. You're not just asking for code; you're commissioning a simulation from your expert AI partner. Let's build the final directive.

#### **4.1 The Persona: Define Your Expert Simulator**

**Why this matters:** Before you give the LLM a task, you must first give it a role. Without a defined persona, an LLM defaults to a generic, helpful assistant, which often produces generic, unhelpful output. By assigning a specific, expert role, you ground the simulation in a world of professional standards, constraints, and know-how, dramatically improving the quality and relevance of the result.

**What expert persona should the LLM adopt for this simulation? Be specific about its role, seniority, and areas of expertise.**

- _Example: "You are a senior-level Site Reliability Engineer (SRE) specializing in cloud infrastructure, automation scripting (Bash, Python), and building robust, observable CI/CD pipelines."_

>

#### **4.2 The Scenario: Establish the Problem Context**

**Why this matters:** A great simulation requires a rich narrative. You can't just drop the LLM into the middle of a problem and expect a nuanced solution. You must first paint a picture of the world it's operating in. This section brings your Pain Journal to life, giving the LLM the same context you have, ensuring its solution is tailored to the _actual_ problem, not a simplified version of it.

**First, what is the high-level goal of the system or process you're working on?**

- _Example: "Our high-level goal is to maintain a CI/CD pipeline that reliably tests and deploys microservices with minimal manual intervention."_

>

**Next, using your Pain Journal, how would you describe the specific, recurring manual process you are trying to automate?**

- _Example: "Currently, when our integration test suite has flaky, transient failures, a developer has to manually scan thousands of lines of logs to find the job IDs of the failed tests. They then have to write a one-off script or manually trigger API calls to re-run only those specific jobs."_

>

**Finally, what makes this process so painful, inefficient, or error-prone?**

- _Example: "This process is painful because it's slow, taking up to 30 minutes of a developer's time. It's error-prone because it's easy to miscopy a job ID or re-run a job that shouldn't be, and it's inefficient because it blocks our deployment pipeline."_

>

#### **4.3 The Directive: State the Core Task**

**Why this matters:** This is the heart of your prompt—the clear, unambiguous command. After setting the stage with the persona and scenario, the directive tells the LLM exactly what you want it to _do_. A vague directive leads to a vague result. A precise, action-oriented directive leads to a precise, actionable solution.

**What is the single, primary action you want the LLM to perform in this simulation?**

- _Example: "Your task is to write a production-ready, robust bash script that fully automates the process of identifying, re-running, and confirming the status of failed jobs from a given pipeline log file."_

>

#### **4.4 The Physics: Set the Rules of the Game**

**Why this matters:** Every system operates under constraints—this is its "physics of reality." The rules you defined in your Rulebook are non-negotiable. Stating them clearly prevents the LLM from proposing solutions that are clever but unworkable in your specific environment (e.g., using a library you don't have, writing in the wrong language, or violating a security policy).

**What are the absolute, non-negotiable constraints, requirements, and environmental limitations from your Rulebook? (List them clearly)**

- _Example: "1. The script must be written in Bash and use only standard, POSIX-compliant tools available in a minimal Alpine Linux container (grep, awk, sed, curl, jq). 2. The script must be idempotent; running it multiple times on the same log file should not cause duplicate job runs. 3. It must accept the log file path as its only command-line argument."_

>

**What are the "anti-goals"—the outcomes or behaviors the solution must absolutely avoid?**

- _Example: "The script must NOT re-run jobs that were successful. It must NOT require any interactive user input during its run. It must NOT store any secret keys or API tokens directly in the script."_

>

#### **4.5 The Evidence: Provide the Raw Materials**

**Why this matters:** An expert can't work in a vacuum. The artifacts you gathered in The Evidence Locker are the ground truth for your simulation. You need to structure this data so the LLM can "read" it effectively. A common best practice is to wrap different pieces of context in clear XML-style tags so the LLM can easily parse them.

**How will you present the necessary code, logs, and other artifacts in the prompt? Describe the structure you will use.**

- _Example: "I will provide all context inside a `<context>` block. Within that, I will provide a sample of the log file inside `<log_file_sample>` tags. The documentation for the API endpoint used to re-run jobs will be inside `<api_documentation>` tags. The environment variables available to the script will be listed inside `<environment_variables>` tags."_

>

#### **4.6 The Blueprint: Define Success and Output Format**

**Why this matters:** You need to show the LLM exactly what a "finished product" looks like. This goes beyond the task itself to define the structure and quality of the output. By providing a blueprint for the solution, you guide the LLM to deliver its results in a way that is immediately useful to you, saving you from cleaning it up later.

**What specific format should the final output take? Be precise.**

- _Example: "Provide the final, complete bash script inside a single, clean ```bash code block. Do not include any explanatory text before or after the code block itself. The script must be fully self-contained."_

>

**What are the key success criteria from your Rulebook that will define a successful simulation?**

- _Example: "The solution is successful if: 1. The script correctly parses all 'FAILED' job IDs from the sample log. 2. It constructs the correct `curl` command for each failed job based on the API docs. 3. It includes robust error handling for API calls (e.g., non-200 responses). 4. It includes extensive comments explaining the 'why' behind complex command chains."_

>

---

#### **Final Assembly Checklist**

You've done it. You've prepared all the individual components needed for a high-quality simulation. Run through this final checklist one last time. When you combine these elements, you're not just writing a prompt; you're orchestrating a simulation.

- [ ] **The Persona:** Is the expert role clearly defined?
- [ ] **The Scenario:** Is the problem context and narrative compelling and complete?
- [ ] **The Directive:** Is the core task a single, unambiguous command?
- [ ] **The Physics:** Are your constraints and anti-goals explicit and non-negotiable?
- [ ] **The Evidence:** Is your contextual data structured clearly (e.g., with tags)?
- [ ] **The Blueprint:** Is the desired output format and criteria for success perfectly clear?

Once you check all these boxes, you're ready to assemble your final prompt and run the simulation.