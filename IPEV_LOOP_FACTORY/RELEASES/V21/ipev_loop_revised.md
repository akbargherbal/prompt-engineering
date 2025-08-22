# The IPEV Loop 2.1: A Practical & Resilient Framework for Agentic AI

## Introduction

If you've used an Agentic LLM like Gemini CLI for a complex task, you have likely felt the frustration of watching it fail in baffling ways—getting stuck in logic loops or silently overwriting its own work.

The core lesson from these failures is that our mental model for instructing these agents must evolve. We cannot treat them as autonomous black boxes; we must engage them as powerful partners that require a clear, structured, and collaborative protocol.

This guide provides that battle-tested strategy. It introduces the **Intent-Plan-Execute-Verify (IPEV) Loop 2.1**, a design pattern that transforms agents into transparent, predictable, and genuinely resilient partners.

## Part I: The Core Concepts

### The Two-Party System

Effective agentic workflow requires understanding that there are two distinct parties involved:

- **The User:** You, the developer. You are the operator and strategist. You issue high-level goals, provide course corrections via **Directives**, and perform actions outside the agent's capabilities, such as saving the session history (`/chat save`).
- **The Agent:** The Gemini CLI process. The agent is the tactical executor. It can write code, run shell commands, and edit files. It operates within a strict loop and follows the protocols you provide. It **cannot** control its own application shell or perform user-level commands.

### The Core IPEV Loop

The IPEV loop is the fundamental protocol that governs the agent's actions for every significant step it takes.

#### 1. **Intent (The "What")**

The agent begins by stating its high-level objective for the immediate next step.

- **Purpose:** To set the context and confirm it understands the goal.
- **Example:** `"My intent is to process '01-intro.md' and append the result to 'output.md'."`

#### 2. **Plan (The "How")**

This is the heart of the framework. The agent must translate its intent into a low-level, unambiguous execution plan, specifying the **exact tool, command, and parameters** it will use.

- **Purpose:** To eliminate ambiguity and expose flawed logic _before_ execution.
- **Good Plan (Unambiguous):** `"PLAN: I will call the `edit` tool to modify 'output.md', ensuring my change appends the new text to the end of the file."`
- **Bad Plan (Ambiguous):** `"PLAN: I will save the output to the file."`

#### 3. **Execute (The "Do")**

The agent executes the _exact_ plan it just declared.

- **Purpose:** To perform the state-changing action in a predictable way.

#### 4. **Verify (The "Proof")**

After execution, the agent must perform a check to confirm the action had the intended effect. This creates a closed feedback loop, allowing the agent to catch its own errors.

- **Purpose:** To confirm success and detect failure immediately.
- **Example:** `"VERIFY: I will now run `ls -l output.md` and confirm its file size has increased."`

## Part II: The Resilient System Protocols

The core loop provides clarity, but resilience comes from handling failure. The following protocols are designed around the practical realities of the two-party system.

### 1. The Collaborative Checkpointing Protocol

The agent cannot save its own session history, but it can—and must—save the state of the codebase. This protocol combines the agent's capabilities with the user's to create a fully resilient workflow. It MUST be performed after every successful `VERIFY` step.

**Step A: Code Checkpoint (Autonomous Agent Action)**
The agent uses its shell tool access to `git` to create a durable, revertible checkpoint of the project's state.

- **Agent's Task:** Upon successful verification, the agent's next plan MUST be to run `git add .` and `git commit -m "Verified: [description of the completed step]"`.

**Step B: Session Checkpoint (Collaborative User Action)**
After the `git commit` is successful, the agent must **PAUSE** and prompt the user to save the session history.

- **Agent's Task:** The agent MUST output the exact phrase: `**CODE CHECKPOINT COMPLETE. Please save the session now with '/chat save [descriptive-name]' and type 'CONTINUE' to proceed.**`
- **User's Task:** The user then executes the `/chat save` command in the CLI and replies with `CONTINUE` to the agent.

### 2. The Directive Protocol: The User's Control Channel

The Directive Protocol is the formal mechanism for the **User** to interrupt, inspect, or override the **Agent's** current task flow. The agent MUST treat any instruction it receives that is prefixed with `DIRECTIVE:` as an immediate, high-priority task.

- **Primary Uses:** Inspection (`DIRECTIVE: Show me...`), state checks (`DIRECTIVE: Run 'git status'...`), and manual overrides.
- **Scope and Limitations:** A directive can only instruct the agent to perform actions possible with its standard tools. It does not grant the agent new capabilities. The user must translate their intent into an actionable command.

### 3. Diagnostic Mode: Intelligent Meta-Debugging

When a `VERIFY` step fails unexpectedly, the agent's mission should pivot to diagnosing the verification process itself. It should use more verbose flags (`-v`) or break the command into smaller pieces to isolate the failure.

### 4. Tool Instability & External Execution

If a specific command consistently freezes the agent's environment, the protocol is to ask the user to run it externally. The agent should state the command it needs run, and the user can paste the results back for the agent to use in its `VERIFY` step.

---

## Part III: The Complete IPEV 2.1 Prompt Template

This is a ready-to-use template. Copy this into the start of your mission file (e.g., `mission.md`).

```markdown
# Mission: [Your High-Level Goal]

## 1. Core Protocol: The IPEV Loop with Collaborative Checkpointing

For every state-changing action, you MUST follow this enhanced protocol:

1.  **INTENT:** State your immediate objective.
2.  **PLAN:** Propose precise, unambiguous commands with exact parameters.
3.  **EXECUTE:** Run the exact command from your plan.
4.  **VERIFY:** Perform a check to prove success.

### **CRITICAL** Checkpointing Protocol (After a successful VERIFY):

5.  **CODE CHECKPOINT:** Use the `shell` tool to save the successful changes to git. Your plan must include `git add .` and `git commit -m "Verified: [brief description of change]"`.
6.  **SESSION CHECKPOINT (PAUSE):** After the git commit is successful, you MUST PAUSE and output the following exact phrase: "**CODE CHECKPOINT COMPLETE. Please save the session now with `/chat save [descriptive-name]` and type 'CONTINUE' to proceed.**" You will not proceed until I respond with "CONTINUE".

## 2. Directive Protocol

I (The User) may interrupt you with a `DIRECTIVE:` prefix. You must execute my instruction immediately and then return to your previous task.

## 3. Mission Parameters

- **Input(s):** [Describe source data, files, APIs]
- **Output(s):** [Describe the desired final state]
- **Known Unstable Commands:** [List any commands requiring external execution]

## 4. Execution Flow

1.  **Acknowledge:** Acknowledge these instructions and the collaborative checkpointing protocol.
2.  **Survey:** Perform an initial survey of the environment (`ls -F`, `git status`).
3.  **Execute:** Begin the first IPEV loop.
4.  **Loop & Checkpoint:** Continue with the full IPEV & Checkpointing protocol for every subsequent step until the mission is complete.
5.  **Complete:** Signal completion and perform a final checkpoint.

Now, begin.
```