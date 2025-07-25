Of course. Here is the complete, user-ready Markdown content for "The Rulebook" worksheet, designed to strictly adhere to your specified Style Guide.

---

# Step 3: The Rulebook — Defining the Laws of Your System

You've successfully documented the pain (**The Pain Journal**) and gathered your evidence (**The Evidence Locker**). Now it's time to define the rules of the game. For an LLM to act as a useful "Systems Simulator," it can't operate in a vacuum. It needs to understand the "physics" of your world—the hard constraints, the non-negotiable requirements, and the specific definition of a winning outcome. This worksheet is where you establish those laws.

Completing this step ensures the LLM's proposed solution is not just clever, but also practical, safe, and aligned with your actual operational reality.

***

### 3.1 Establish Your Constraints: The "Physics of Reality"

Before the LLM can design a solution, it needs to know what’s impossible. Without defined boundaries, an LLM might suggest using a technology you don't have, violating a security policy, or ignoring a critical performance requirement. By defining constraints upfront, you're not limiting the LLM's creativity; you're focusing it on a *viable* solution space. Think of this as teaching the simulator the fundamental laws of physics for your project.

**What are the absolute, non-negotiable *technical* constraints of a solution?**
Consider programming languages, required libraries, specific versions, APIs that *must* be used, or platforms it must run on.

*Example: The solution must be a single Python 3.9+ script. It can only use the standard `requests`, `json`, and `csv` libraries; no third-party packages like Pandas are allowed. It must authenticate with our internal `JobQueue` API using a bearer token provided as an environment variable.*

> Your Answer:

**What are the absolute, non-negotiable *operational* constraints?**
Think about performance, security, process, and resource limits. How fast must it run? What can't it touch? What are the deployment rules?

*Example: The script must complete its entire run in under 90 seconds. It absolutely cannot write to the production database. All output and logs must be written to the designated S3 bucket (`s3://prod-log-script-output/`). It must not consume more than 256MB of memory.*

> Your Answer:

***

### 3.2 Define Your Success Criteria: The "Definition of Done"

An LLM's goal is to satisfy your prompt. If you're vague about what "success" means, you'll get a vague (and likely unhelpful) result. This section is where you get ruthlessly specific. Success isn't just "the code runs without errors." Success is "the original pain point is gone." You need to provide clear, measurable, and observable outcomes that prove the problem has been solved.

**What is the single, primary objective of the solution?**
If it could only do one thing perfectly, what would that be? Describe the ideal end-state that eliminates the manual work you documented in your Pain Journal.

*Example: The solution must automatically parse a given log file, identify all entries marked with "FAILED_PROMPT," re-submit only those jobs to the queue, and then generate a new, clean results file that merges the original successes with the output from the re-run jobs.*

> Your Answer:

**How will you *know*, with certainty, that the solution has succeeded? What are the verifiable, observable outcomes?**
List the specific, tangible artifacts or state changes you could point to as proof. How would you manually verify a successful run?

*Example: 1) A single, merged CSV file named `[original-filename]-reprocessed.csv` exists in the output directory. 2) The script's log file contains the message "Processing complete. X failed items re-queued." and shows a zero exit code. 3) Checking the `JobQueue` monitor shows new jobs were created with the tag `re-run`.*

> Your Answer:

***

### 3.3 Set Your Anti-Goals: The "Guardrails"

Just as important as defining success is defining failure. An LLM might find a "clever" shortcut that technically works but creates new problems or misses the point entirely. Anti-goals act as guardrails, preventing the simulation from veering off-course into unhelpful, counter-productive, or dangerous territory. Explicitly stating what you *don't* want is one of the most powerful ways to guide the LLM toward a high-quality solution.

**What common but undesirable solutions or side effects must the solution actively avoid?**
Think about shortcuts that don't solve the real problem, or approaches that would be a nightmare to maintain.

*Example: The solution must not modify the original log files in any way (they are immutable). It must not require setting up a new database or external service to track state. It must not simply re-run the entire original job from scratch, as that is too time-consuming and expensive.*

> Your Answer:

**What would be a technically functional but ultimately *unhelpful* solution that fails to solve the core pain?**
This helps the LLM understand the *spirit* of the task, not just the letter. What's a "solution" that would still leave you with manual work?

*Example: A solution that simply prints or emails a list of the failed prompt IDs would be unhelpful. The core problem is the manual toil of re-running them and merging the results, so any solution that still requires me to do that is a failure.*

> Your Answer: