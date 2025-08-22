# The IPEV Loop 2.0: A Resilient Framework for Agentic AI

## What's New in 2.0?

This evolved version of the IPEV Loop incorporates hard-won lessons from real-world deployment with unstable AI tools. Key improvements include:

- **Diagnostic Mode**: Replaces the primitive "HALT" with intelligent meta-debugging capabilities
- **Directive Protocol**: Introduces a formal control channel for user overrides and inspection commands
- **Agent State Management**: Adds health checks and recovery protocols for session corruption
- **Tool Instability Workarounds**: Provides escape hatches when the agent's own tools become unreliable

The original IPEV Loop remains the core "happy path" protocol, but 2.0 makes it resilient enough for the imperfect AI tools of today.

---

## Introduction: The Two-Week Failure That Led to a Breakthrough

If you've tried using an Agentic LLM like Gemini CLI for a complex, multi-step task, you may have felt a familiar frustration. You give it a clear goal, a list of files, and what seems like a simple instruction—"process these files and append the results to an output file"—only to watch it fail in baffling ways.

Perhaps it gets stuck in a logic loop, refusing to start the work because of an overly rigid protocol you designed. Or, worse, it starts the work, reports success after every step, but you later discover it was overwriting your output file on each iteration, leaving you with only the last piece of the puzzle.

This isn't a hypothetical scenario. It was the real-world, two-week struggle that led to the framework in this guide. But the journey didn't end with the first breakthrough. After months of field testing with beta-level tools, we discovered that even a well-designed protocol could fail in spectacular ways when the underlying agent tools themselves became unreliable.

The initial conclusion was that the tool was "no good," but the reality was more nuanced: **both our mental model for instructing these agents was wrong, and we needed strategies for when the agents themselves break down.**

This guide provides a battle-tested strategy to handle both challenges. It introduces the **Intent-Plan-Execute-Verify (IPEV) Loop 2.0**, a design pattern that transforms agents from unreliable black boxes into transparent, predictable, and genuinely resilient partners—even when the tools they run on are buggy, unstable, or prone to failure.

## Part I: The Foundation - Core IPEV Loop

### The Core Challenge: The Ambiguity Gap

The fundamental reason that simple prompts fail for stateful tasks (like file I/O, database changes, or API calls) is the **Ambiguity Gap**.

Let's analyze the two failure modes from our foundational example:

1. **The Over-Constrained Prompt (Brittle Rigidity):** The first attempt involved a highly detailed, multi-file prompt with a mandatory "Environment Grounding Protocol."

   - **Intent:** To eliminate any possible misinterpretation of the environment (OS, paths).
   - **Result:** The agent became paralyzed. It couldn't satisfy the rigid, brittle prerequisites, and the cognitive overhead of the protocol prevented it from ever starting the actual task. It was like giving a chef a 100-page safety manual to read before boiling water.
   - **Lesson:** Over-constraining an agent with rigid, procedural rules makes it fragile. It removes the agent's ability to use its own intelligence to adapt and solve problems.

2. **The Under-Specified Prompt (Implicit Trust):** The second attempt simplified the instructions, trusting the agent to understand the core task.
   - **Intent:** To remove the procedural roadblocks and focus on the primary goal.
   - **Result:** The agent successfully processed all the files but failed on the most critical detail. The human instruction "append to the file" was conceptually understood, but the agent's default `write_file` tool executed an _overwrite_ operation. The final output contained only the result of the last operation.
   - **Lesson:** Never assume an agent's tool execution will perfectly match your high-level intent. The ambiguity of natural language is the primary source of critical, silent failures.

These failures reveal a universal truth: for any task that changes the state of a system, you cannot afford ambiguity. The solution is not more rules or more trust, but a better operational protocol.

### The Solution: The Intent-Plan-Execute-Verify (IPEV) Loop

The IPEV loop is a simple but powerful framework for structuring your instructions. It forces the agent to make its reasoning and execution strategy explicit _before_ taking any action, turning a potential failure into a transparent, correctable step.

It consists of four phases for every significant action the agent takes:

#### 1. **Intent (The "What")**

This is the high-level objective. It's where you define the goal for a specific step in the workflow. This is what most prompts already do well.

- **Purpose:** To set the context and desired outcome for the agent.
- **Example:** `"My intent is to process the source file '01-intro.md' and append the translated content to 'output.md'."`

#### 2. **Plan (The "How")**

This is the heart of the IPEV loop and the single most important addition to your prompting strategy. Before acting, you require the agent to translate its high-level intent into a low-level, unambiguous execution plan. This plan must specify the **exact tool, command, and parameters** it will use.

- **Purpose:** To close the Ambiguity Gap. It forces the agent to show its work and commit to a specific, literal action, exposing any potential misinterpretations before they cause harm.
- **Good Plan (Unambiguous):** `"PLAN: I will read the content of '01-intro.md'. After generation, I will append the result to 'output.md' by calling the Python write_file tool with the mode parameter set to 'a'."`
- **Bad Plan (Ambiguous):** `"PLAN: I will save the output to the file."` (This is just a restatement of the intent and doesn't specify _how_).

By demanding a plan, you move the potential point of failure from a silent execution error to a transparent planning error, which is easily caught and corrected.

#### 3. **Execute (The "Do")**

This step is straightforward: the agent executes the _exact_ plan it just declared.

- **Purpose:** To perform the state-changing action in a predictable way.
- **Instruction:** `"Now, execute the plan you have stated."`

#### 4. **Verify (The "Proof")**

After execution, the agent must perform a check to confirm that the action had the intended effect. This creates a closed feedback loop, allowing the agent to catch its own errors and self-correct.

- **Purpose:** To confirm success and detect failure immediately. This prevents errors from compounding.
- **Good Verification Steps:**
  - **File I/O:** `"VERIFY: I will now use the shell tool to run ls -l output.md and confirm its file size has increased since the last step."`
  - **API Call:** `"VERIFY: I will now send a GET request to the /users/123 endpoint and confirm the response contains the updated user data."`
  - **Database:** `"VERIFY: I will now execute a SELECT COUNT(*) query on the products table to confirm a new row was added."`

If the verification step fails, this triggers the enhanced protocols detailed in Part II.

## Part II: Building a Resilient Agent

Real-world deployment revealed that the original IPEV Loop, while excellent for handling ambiguity, was insufficient for handling the instability and unpredictability of bleeding-edge AI tools. The following protocols transform the framework from a "happy path" guide into a genuinely resilient system.

### The Diagnostic Mode: Beyond the Brittle Halt

**The Problem with Simple Failure Handling**

The original protocol's safety mechanism was primitive: "If verification fails, report the failure and HALT." In practice, this created a dead end when verification tools themselves became the source of problems. A `pytest` command that hangs indefinitely, a database connection that times out, or a file system that becomes temporarily unavailable—these aren't mission failures, they're diagnostic challenges.

**The Solution: Meta-Debugging Protocol**

When a VERIFY step fails repeatedly or behaves unexpectedly, the agent's mission should pivot. Its new goal becomes diagnosing and fixing the verification process itself.

**Diagnostic Mode Protocol:**

1. **Pattern Recognition:** If the same VERIFY step fails 2+ times consecutively, or if a command hangs/freezes, automatically enter Diagnostic Mode.

2. **Isolation Strategy:** Break down the failing verification into smaller, testable components:
   - **Example:** If `pytest tests/` hangs, try `pytest tests/test_single_file.py`
   - **Example:** If `curl api.example.com/health` times out, try `ping api.example.com` first

3. **Instrumentation Strategy:** Add debugging flags and verbose output to gather more information:
   - **Example:** Use `pytest -v --timeout=30 --tb=short` instead of bare `pytest`
   - **Example:** Use `curl -v --max-time 10` instead of bare `curl`

4. **Recovery or Workaround:** Based on diagnostic results, either:
   - Fix the underlying issue (restart a service, clear a cache)
   - Implement an alternative verification method
   - Escalate to manual verification if tools are fundamentally broken

**Diagnostic Mode Example:**

```
INTENT: Verify that the new user was created in the database.
PLAN: I will run `psql -c "SELECT COUNT(*) FROM users WHERE email='new@user.com'"` to confirm the user exists.
EXECUTE: [Command hangs indefinitely]

ENTERING DIAGNOSTIC MODE:
- Isolation Test: `psql -c "SELECT 1"` → Works (database is responsive)
- Instrumentation: `psql -c "SELECT COUNT(*) FROM users WHERE email='new@user.com'" --set=statement_timeout=5000` → Returns result
- Root Cause: Original query lacked timeout protection
- Resolution: Update verification plan to include timeout parameters
```

### The Directive Protocol: A Control Channel for User Commands

**The Problem with Mission-Only Thinking**

The original framework treated every user input as part of the main mission flow, forcing simple inspection commands through the full IPEV loop. When a user asks "document the current problem" or "show me the contents of that file," they need an immediate, direct response—not a formal verification step.

**The Solution: Formal Control Channel**

The Directive Protocol creates a prioritized "escape hatch" from the main IPEV loop for inspection, debugging, and manual override commands.

**Directive Protocol Rules:**

1. **Prefix Recognition:** Any command prefixed with `DIRECTIVE:` is executed immediately and standalone
2. **No Auto-Verification:** Directive commands MUST NOT trigger automatic VERIFY steps unless explicitly requested
3. **Scope Limitation:** Directives are for inspection and debugging, not mission-critical state changes
4. **Return to Mission:** After completing a directive, the agent returns to its previous mission context

**Directive Syntax Examples:**

```
DIRECTIVE: Show me the current contents of output.log
DIRECTIVE: List all files in the current directory
DIRECTIVE: Document the error we just encountered
DIRECTIVE: Check the process list for any hanging pytest processes
DIRECTIVE: Save a checkpoint before we try the risky operation
```

**When to Use Directives:**

- **Inspection:** Checking file contents, system state, or error logs
- **Debugging:** Isolating problems or gathering diagnostic information
- **Manual Overrides:** Bypassing broken tools or implementing workarounds
- **Session Management:** Saving checkpoints or cleaning up resources

### Agent State Management: Health Checks and Recovery

**The Problem with Stateless Assumptions**

The original framework focused on verifying external world state but ignored the internal health of the agent and its host application. In reality, AI tools can enter corrupted states—chat histories can become poisoned, API connections can break, and the agent's own tools can stop responding correctly.

**The Solution: Comprehensive State Monitoring**

Agent State Management treats the agent itself as a system that requires monitoring and maintenance.

**Health Check Protocol:**

1. **After Unexpected Errors:** Always perform a health check when operations fail in unexpected ways
2. **After Cancellations:** If a command is cancelled or interrupted, verify the agent's internal state
3. **Visual Indicators:** Check the UI for error indicators (e.g., "X 2 errors" in status bars)
4. **Tool Responsiveness:** Test basic commands (`echo "test"`) to confirm tools are working

**Checkpoint Strategy:**

1. **Success Points:** Save a checkpoint (`/chat save`) after every successful VERIFY step
2. **Before Risky Operations:** Always save before operations known to be potentially problematic
3. **Naming Convention:** Use descriptive checkpoint names: "pre_database_migration", "after_file_processing"

**Recovery Protocol:**

1. **Detection:** Health check reveals agent corruption or tool failures
2. **Assessment:** Determine if the issue is temporary (retry) or persistent (recovery needed)
3. **Restoration:** Load the most recent known-good checkpoint (`/chat resume`)
4. **Alternative Approach:** If the same operation fails repeatedly, implement workarounds

**State Management Example:**

```
EXECUTE: Running pytest tests/
[Command hangs, user cancels operation]

HEALTH CHECK: Checking for error indicators... Found "X 1 error" in status
HEALTH CHECK: Testing basic shell command... `echo test` → No response
ASSESSMENT: Agent state corrupted, tools unresponsive
RECOVERY: Loading checkpoint "pre_test_execution"
WORKAROUND: Moving pytest execution to external terminal
```

### Tool Instability and Workarounds

**The Problem with Tool Reliability Assumptions**

The original framework assumed that the agent's built-in tools (`shell`, `write_file`, `python`) would either succeed or fail gracefully. In practice, some commands can trigger bugs in the host application that cause freezes, crashes, or permanent corruption.

**The Solution: External Execution Environment**

When the agent's own tools become unreliable, the protocol must provide escape routes to external, stable environments.

**Tool Instability Protocol:**

1. **Pattern Recognition:** If a specific command consistently freezes or crashes the host application, flag it as "unstable"
2. **External Execution:** Move problematic commands to a standard system terminal outside the agent
3. **Result Integration:** Manually feed results back to the agent for analysis and continuation
4. **Documentation:** Keep a running list of known problematic commands and their workarounds

**External Execution Workflow:**

```
IDENTIFIED ISSUE: `pytest --timeout=30` reliably freezes Gemini CLI
WORKAROUND PROTOCOL:
1. Execute `pytest --timeout=30` in standard terminal
2. Copy output/results
3. Provide results to agent: "DIRECTIVE: The external pytest run completed with output: [paste results]"
4. Continue with normal VERIFY step using provided data
```

**Common Unstable Operations:**

- Long-running commands with complex output parsing
- Operations involving timeouts or interrupts  
- Commands that interact with unstable external services
- Resource-intensive operations that may trigger memory issues

### The Complete IPEV 2.0 Protocol Template

```markdown
# Mission: [Your High-Level Goal]

## 1. Core Protocol: The IPEV Loop with Resilience Extensions

For every state-changing action, follow this enhanced protocol:

### Happy Path (Standard IPEV):
1. **INTENT:** State your immediate objective
2. **PLAN:** Propose precise, unambiguous commands with exact parameters  
3. **EXECUTE:** Run the exact command from your plan
4. **VERIFY:** Perform a check to prove success

### Resilience Extensions:
- **Diagnostic Mode:** If VERIFY fails 2+ times, pivot to diagnosing the verification tool itself
- **Health Checks:** After unexpected failures, verify agent and tool responsiveness
- **Checkpointing:** Save state after every successful VERIFY step

## 2. Directive Protocol

Commands prefixed with `DIRECTIVE:` are executed immediately without triggering VERIFY steps.
Use for inspection, debugging, and manual overrides.

## 3. Mission Parameters

- **Input(s):** [Describe your source data, files, APIs, etc.]
- **Output(s):** [Describe the desired final state, output files, etc.]
- **Critical Constraints:** [List any "hard rules"]
- **Known Unstable Commands:** [List any commands requiring external execution]

## 4. Execution Flow

1. Acknowledge these instructions and perform initial health check
2. Save initial checkpoint
3. Begin IPEV loop for first task
4. Continue with full protocol until mission complete
5. Signal completion and save final checkpoint

Now, begin.
```

## Beyond Files: Where to Use IPEV 2.0

The enhanced framework provides reliability for any domain where mistakes have consequences and tools can be unpredictable:

- **DevOps & Cloud Management:** Handle `terraform apply` with diagnostic modes for plan failures and health checks for provider API issues
- **Code Refactoring:** Use checkpointing before major changes and external execution for resource-intensive test suites
- **Data Analysis & ETL:** Implement recovery protocols for database connection failures and external execution for memory-intensive operations
- **Automated Testing:** Use directive protocol for debugging test failures and diagnostic mode for flaky test isolation

## Conclusion: From Agent Architect to Agent Reliability Engineer

The evolution from IPEV 1.0 to 2.0 reflects the maturation of agentic AI from research curiosity to production reality. We are no longer just designing protocols for ideal agents in controlled environments—we are building resilient systems that can handle the chaos, instability, and unpredictability of bleeding-edge AI tools.

The IPEV Loop 2.0 acknowledges that in the real world, agents fail, tools break, and sessions get corrupted. Rather than viewing these as insurmountable problems, it provides systematic approaches to diagnose, recover, and work around these issues while still achieving reliable results.

By embedding these enhanced protocols into your instructions, you move beyond the frustrating cycle of trial-and-error and build robust, genuinely resilient AI agents that can deliver consistent results even in unstable environments. This is the foundation for the next generation of agentic AI applications—systems that are not just powerful, but dependable.
