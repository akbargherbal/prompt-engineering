Here is the complete, user-ready Markdown content for "The Evidence Locker" worksheet.

---

# Step 2: The Evidence Locker

### **Gathering the Ground Truth for Your Simulation**

Welcome to the Evidence Locker. Think of yourself as a detective building a case file. An LLM, like any great detective, can't solve a mystery without evidence. It needs to see the "scene of the crime" (your code), read the "witness statements" (your logs), and understand the "background checks" (your documentation). This step is where you gather all the concrete artifacts that define the reality of your system. By providing this "ground truth," you empower the LLM to build a high-fidelity mental model of your problem, ensuring its proposed solutions are relevant and practical, not just theoretical.

---

### **Section 1: The Code Base (The System's DNA)**

First, we need the code. This is the absolute ground truth of how your system currently behaves. The LLM needs to analyze the exact logic—the functions, the variables, the control flow—to understand the mechanics of the problem you're trying to solve. Without it, the LLM is just guessing about your implementation.

**1. What are the key scripts, modules, or functions at the heart of the manual process you documented in your Pain Journal?**
Don't worry about providing every single line of code yet. Just identify the most relevant files or code blocks.

> _Example: The main Python script is `batch_processor.py`, which ingests user data. It heavily uses the `api_client` module in `utils/helpers.py` to make external calls. The whole process is kicked off by `run_nightly_job.sh`._
>
> **Your Answer:**
>
> >

**2. Are there any important configuration files (`.yml`, `.json`, `.env`, etc.) that control the behavior of this code?**
Think about files that define timeouts, feature flags, API endpoints, or other environmental parameters.

> _Example: The `config.yml` file defines API endpoints and retry logic. The `.env` file contains the `API_TIMEOUT_SECONDS=30` variable, which is a frequent source of our problems._
>
> **Your Answer:**
>
> >

**3. Where can these files be found? List file paths, Git repo URLs, or simply paste the most relevant snippets.**
The goal is to have the actual content ready to be included in your final prompt.

> _Example: All files are in the `data-processing-tools` repo under the `src/nightly_job` directory. The most critical function is `process_record()` in `batch_processor.py`._
>
> **Your Answer:**
>
> >

---

### **Section 2: The Digital Trail (Logs, Errors, and Outputs)**

If code is the system's DNA, then logs and outputs are the story of that DNA in action. They are the objective record of what *actually happened*—the errors, the successes, and the unexpected behaviors. This digital trail provides the LLM with the critical symptoms of the problem, moving from theory to tangible reality.

**1. What does a "good" log entry or a successful output look like for this process?**
This helps the LLM establish a baseline for normal, correct behavior.

> _Example: A successful log line looks like this: `[2023-10-26 02:30:15] INFO: Batch 123 completed successfully. 500 records processed in 12.5s.`_
>
> **Your Answer:**
>
> >

**2. Crucially, what do the "bad" logs, error messages, or failure outputs look like?**
This is the core evidence of the pain you documented. Be as specific as possible. Paste entire stack traces if you have them.

> _Example: We see two main errors. One is a Python traceback ending in `KeyError: 'user_id' not found in record`. The other is a custom log message: `[2023-10-26 03:15:45] ERROR: API timeout after 30 seconds for job_id 456.`_
>
> **Your Answer:**
>
> >

**3. Are there any other system outputs? (e.g., generated files, database entries, dashboard screenshots)**
Think about any artifacts that are created, modified, or left behind by the process. This shows the LLM the consequences of the system's execution.

> _Example: After a failure, I have to manually create a `failed_prompts.csv` file that contains the IDs of the records that didn't process, so I can re-run them later._
>
> **Your Answer:**
>
> >

---

### **Section 3: The Unwritten Rules (Documentation & Tribal Knowledge)**

Not all critical information lives in code or logs. Some of it exists in documentation, and even more exists only in the heads of the people who run the system. This "tribal knowledge" contains the hidden assumptions and the operational wisdom that the LLM can't possibly infer on its own.

**1. Is there any formal documentation (e.g., READMEs, Confluence/Notion pages, API docs) that describes how this system is _supposed_ to work?**
Even if it's out of date, it provides context on the system's original intent. Provide links or summaries.

> _Example: The `README.md` in the repo explains the initial setup, but it's six months out of date. The external API we call has official documentation at `api.vendor.com/docs`._
>
> **Your Answer:**
>
> >

**2. What is the "tribal knowledge" about this process? What's the critical information you'd have to tell a new team member that isn't written down anywhere?**
This is one of the most valuable inputs you can provide. Think about operational quirks, secret workarounds, or known issues.

> _Example: "Oh, you have to make sure you run the `cleanup_temp_files.sh` script first, otherwise the nightly job might pick up zombie files from a previous failed run. Also, the vendor API gets really slow between 2-3 AM EST, so we try to avoid running big jobs then, even though that's our main processing window."_
>
> **Your Answer:**
>
> >

***

**Worksheet Complete.** You have now assembled a comprehensive evidence file. With this collection of code, logs, and context, the LLM won't be operating in a vacuum. It will be reasoning about your system based on the same evidence you have. You're ready for the next step: **The Rulebook**, where we'll define the constraints and success criteria for a solution.