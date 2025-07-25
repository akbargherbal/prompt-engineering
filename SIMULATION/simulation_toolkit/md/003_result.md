Of course. As a Master Curriculum Designer and AI Pedagogy Expert, I will now create the complete content for "The Rulebook" worksheet, meticulously following every principle of the provided Style Guide.

---

# The Rulebook
### Phase 3 of the Developer's Mise en Place

Congratulations on reaching Phase 3! You’ve documented your pain and gathered your evidence. Now it's time to define the rules of the game. "The Rulebook" is where you establish the 'laws of physics' for your simulation. By defining your constraints, success criteria, and anti-goals *before* you write the prompt, you force the LLM to think within your reality, leading to solutions that are not just clever, but practical, safe, and genuinely useful.

Let's build the guardrails for our simulation.

---

## Step 1: Establish Your Constraints (The "Laws of Physics")

**Why this matters:** Before you ask an LLM to design a solution, you must tell it what is and isn't possible. Constraints aren't limitations; they are the foundation of a realistic solution. By defining the technical, process, and resource boundaries, you prevent the simulation from suggesting a perfect-but-impossible system (like "rewrite it in Rust with a team of five engineers"). This step ensures the LLM's creativity is grounded in your project's reality.

#### **1.1: What are the absolute technical constraints of the solution?**

Think about the environment where this will run. What technologies are mandatory? What is strictly forbidden?

_Example: The solution must be a single Python 3.9+ script. It can only use the standard library and the `requests` library, as no other external packages can be installed in the production environment. It cannot write to a database._

>

#### **1.2: What are the immovable process constraints?**

Consider the workflow this solution must fit into. What inputs are fixed? What outputs are non-negotiable? Who interacts with this process?

_Example: The script must read log data from a specific S3 bucket path. The input files are always gzipped JSONL files. The final output must be a new JSONL file uploaded to a different, specified S3 path._

>

#### **1.3: What are the key resource constraints?**

Think about time, performance, and maintenance. How fast must this run? Who will maintain it? Are there budget limitations?

_Example: The entire process must complete in under 5 minutes. The script will be maintained by junior developers, so it must be heavily commented and avoid complex abstractions. It cannot use any paid third-party APIs._

>

---

## Step 2: Define Your Success Criteria (The "Winning Conditions")

**Why this matters:** A simulation needs a clear target. Simply saying "fix the problem" is too vague. By defining precise, verifiable success criteria, you give the LLM a clear picture of what "done" looks like. This turns the simulation from a vague brainstorming session into a goal-oriented engineering exercise, producing a solution you can actually test and validate.

#### **2.1: What is the single, primary outcome that defines success?**

If the solution does only one thing perfectly, what would it be? This is your "Minimum Viable Success."

_Example: A single, clean `merged_results.jsonl` file is created, containing the combined results of the original successful jobs and the newly successful re-run jobs._

>

#### **2.2: How will you objectively verify that the solution worked?**

What specific, measurable checks can you perform to know, with certainty, that the outcome is correct? This is your acceptance test.

_Example: I will verify success by checking three things: 1) The script exits with code 0. 2) The number of lines in the new `merged_results.jsonl` file equals the count of original successes plus the count of re-run successes. 3) No "failed" or "error" statuses exist in the final output file._

>

#### **2.3: Beyond the minimum, what would a "gold standard" solution include?**

Think about bonus features that would make this solution exceptionally helpful. What would turn it from good to great?

_Example: The "gold standard" solution would also output a brief summary to the console, like: "Processed 1000 log entries. Found 50 failures. Re-ran 50 jobs. 48 succeeded. Final output contains 998 successful results." It would also automatically archive the original log files it processed into a separate `processed/` directory._

>

---

## Step 3: Set Your Anti-Goals (The "Failure Modes")

**Why this matters:** Telling the simulation what *not* to do is just as important as telling it what to do. Anti-goals help you avoid solutions that are technically correct but practically disastrous. By explicitly stating undesirable outcomes (like corrupting data or creating a maintenance nightmare), you steer the LLM away from common pitfalls and toward a solution that is not only effective but also robust and safe.

#### **3.1: What are the absolutely unacceptable side effects?**

What potential outcome would be a deal-breaker, no matter how well the solution works otherwise?

_Example: The solution absolutely must not modify or delete the original source log files. It must never lose the data from the originally successful jobs. It cannot hang indefinitely if an API call fails during the re-run process._

>

#### **3.2: What types of solutions or patterns do you want to explicitly avoid?**

Have you tried things that didn't work? Are there common but "wrong" ways to solve this that you want the LLM to ignore?

_Example: I want to avoid any solution that requires manual intervention, like a human having to copy/paste a list of failed IDs. I also want to avoid solutions that involve writing multiple, separate scripts that need to be run in a specific order._

>

#### **3.3: What would make this solution too complex or brittle to maintain?**

Think about future-you. What would make this a nightmare to debug or update?

_Example: Any solution that requires a complex configuration file would be too brittle. A solution that relies on parsing human-readable text from the logs instead of structured data (like JSON fields) would also be too fragile and likely to break._

>

---

### You've Built The Rulebook!

Excellent work. You have now defined the reality for your simulation. With these constraints, success criteria, and anti-goals, you have a powerful set of guardrails. This ensures the LLM's output will be tailored, safe, and directly applicable to your problem.

**Next Up:** You're ready for the final step of your preparation: **The Assembly Line**, where you'll combine everything you've documented into a final, structured prompt to run your simulation.