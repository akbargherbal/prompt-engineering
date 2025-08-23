# A-HIRD Framework: A Testing & Debugging Approach for AI Code Assistants

## Why Existing Frameworks Don't Work for Testing

Most AI agent frameworks are designed around **execution tasks** - scenarios where you know exactly what you want to accomplish and need to prevent the AI from misinterpreting your instructions. The popular IPEV framework (Intent-Plan-Execute-Verify) exemplifies this approach: it requires agents to explicitly state their plan before taking any action, then verify the results afterward.

IPEV works great for tasks like "process these files and generate a report" or "deploy this code to production." But it fails for testing and debugging because:

- **Testing is exploratory** - you don't know what you'll find until you look
- **Debugging requires speed** - slow iteration kills your problem-solving flow
- **Investigation branches unpredictably** - you can't plan a linear sequence when each discovery changes your next move

What we need is a framework designed specifically for **discovery-driven work** where learning and understanding are the primary goals.

---

## The A-HIRD Framework: Built for Discovery

A-HIRD (Anticipate-Hypothesis-Investigate-Reflect-Decide) structures the natural thought process of effective debugging. Instead of forcing predetermined plans, it organizes the cycle of orienting, forming theories, testing them quickly, and adapting based on what you learn.

---

## The Five-Phase Cycle

### 1. **ANTICIPATE** (The "Context Scan")

**Purpose:** Briefly scan the immediate context to identify key technologies and potential patterns before forming a hypothesis.

**Format:** "The core technology is [library/framework]. I anticipate this involves [common pattern/constraint], such as [specific example]."

**Examples:**

- "The core library is `crewai`. I anticipate this involves Pydantic models, which means strict type validation and potentially immutable objects."
- "I'm working with React Hooks. I anticipate issues related to dependency arrays and stale closures."
- "This involves async functions in Python. I anticipate the need to handle event loops and use `await` correctly."

**Key:** This proactive step primes the debugging process, shifting from a purely reactive stance to one of informed caution.

### 2. **HYPOTHESIS** (The "Theory")

**Purpose:** Articulate your current best guess about what's happening, including a measurable success criterion.

**Format:** "I suspect [specific theory] because [observable evidence], and the expected outcome is [specific, measurable result]."

**Examples:**

- "I suspect the API timeout is caused by a database lock because the error only happens during high-traffic periods, and the expected outcome is that the query time will exceed 5 seconds."
- "I think this React component isn't re-rendering because the state object reference hasn't changed. The expected outcome is that logging the object's ID before and after the state update will show the same ID."
- "The memory leak might be from event listeners not being cleaned up in useEffect. The expected outcome is that the test will pass with a `1 passed` message."

**Key:** Keep hypotheses **specific and testable**, with a clear definition of success.

---

### 3. **INVESTIGATE** (The "Quick Test")

**Purpose:** Design the minimal experiment to test your hypothesis.

**Characteristics:**

- **Fast:** Should take seconds to minutes, not hours
- **Focused:** Tests one specific aspect of your hypothesis
- **Reversible:** Easy to undo if it breaks something
- **Observable:** Produces clear, interpretable results

**Common Investigation Techniques:**

- Add logging statements to trace execution flow
- Write throwaway test cases for specific scenarios
- Use debugger breakpoints at critical points
- Make isolated code changes to test theories
- Query databases/APIs with specific parameters
- Run focused subsets of your test suite
- Create minimal reproduction cases

**Example Investigation Plans:**

- "Add console.log to track when useEffect cleanup runs."
- "Write a unit test that simulates the timeout condition."
- "Check database query execution time with EXPLAIN."
- "Create minimal reproduction with just the problematic component."

---

### 4. **REFLECT** (The "What Did We Learn?")

**Purpose:** Interpret results, update your understanding, and extract reusable knowledge.

**Questions to Answer:**

- Did this confirm or contradict my hypothesis?
- What new information did I discover?
- What does this tell me about the broader system?
- If there was a failure, what is the single, memorable "Key Learning"?

**Result Categories:**

- ✅ **Confirmed:** "The timeout IS caused by database locks - query time jumps from 50ms to 30s during peak hours."
- ❌ **Refuted:** "Event listeners ARE being cleaned up properly - the leak must be elsewhere."
  - **Key Learning:** The memory leak is not related to component lifecycle event listeners.
- 🤔 **Partial:** "State object reference is changing, but component still not re-rendering - need to check memo dependencies."
- 🆕 **New Discovery:** "Found unexpected N+1 query pattern that explains the performance issue."
  - **Key Learning:** `crewai` Agent objects are immutable after creation; attributes cannot be set directly on an instance.

---

### 5. **DECIDE** (The "Next Move")

**Purpose:** Choose your next action based on what you learned, justifying why it's the most efficient path.

**Decision Types:**

**Continue Investigating:**

- Dive deeper into the same area
- Test a refined version of your hypothesis

**Pivot Investigation:**

- Switch to investigating a different theory
- Follow newly discovered leads

**Implement Solution:**

- Apply the fix you've identified
- Write proper tests to prevent regression

**Escalate or Document:**

- Get help from a domain expert
- Document findings for future reference

**Justification:** Briefly explain why this is the most logical next step (e.g., "Pivot to class-based mocking, as it directly addresses the immutability error discovered in the Reflect step.").

---

## A-HIRD in Practice: A Real Example

**Problem:** React app becomes unresponsive after user interactions.

### Cycle 1

**ANTICIPATE:** The code involves React component lifecycles. I anticipate potential issues with `useEffect` cleanup logic.
**HYPOTHESIS:** I suspect a memory leak from components not unmounting properly. The expected outcome is that the browser's memory profiler will show a steady increase in detached DOM nodes.
**INVESTIGATE:** Add memory profiling and component lifecycle logging.

```javascript
useEffect(() => {
  console.log("Component mounted:", componentName);
  return () => console.log("Component unmounted:", componentName);
}, []);
```

**REFLECT:** ✅ **Confirmed** - Components are mounting but not unmounting when expected, and memory usage is climbing.
**DECIDE:** Continue investigating. This is the right path, so I will dive deeper into what's preventing unmounting.

### Cycle 2

**ANTICIPATE:** I am inspecting the parent-child component relationship in React. I anticipate that state management or direct references could be preventing garbage collection.
**HYPOTHESIS:** I suspect the parent component is holding direct references to child components, preventing unmounting. The expected outcome is that React DevTools will show the "unmounted" components still present in the component tree.
**INVESTIGATE:** Check React DevTools component tree and add ref tracking.
**REFLECT:** ❌ **Refuted** - The parent is correctly removing the child from the render tree.

- **Key Learning:** The issue is not related to the React render tree itself; something external must be holding a reference.
  **DECIDE:** Pivot investigation. I will look for non-React systems like global event listeners or timers, as this directly follows from the Key Learning.

### Cycle 3

**ANTICIPATE:** The focus is now on browser APIs (`window`, `document`). I anticipate that listeners or timers created in `useEffect` might lack a cleanup function.
**HYPOTHESIS:** I suspect event listeners or timers attached to `window`/`document` are not being cleaned up. The expected outcome is that logging will show an `addEventListener` call without a corresponding `removeEventListener` call.
**INVESTIGATE:** Add logging to all `addEventListener`/`removeEventListener` calls and check for `setInterval`.
**REFLECT:** 🆕 **New Discovery** - Found an interval timer (`setInterval`) in a `useEffect` hook without a cleanup function returning `clearInterval`.
**DECIDE:** Implement solution. This is the clear root cause, so I will add the proper cleanup function to the `useEffect` hook.

---

## Implementation Guide for AI Assistants

### Session Setup Template```markdown

# Debug Session: [Brief Problem Description]

**Context:** [Codebase area, recent changes, error symptoms]
**Time Budget:** [How long before escalating/taking break]
**Risk Level:** [Can we safely experiment? Need to be careful?]

**Initial Hypothesis:** [Your starting theory]

---

## Investigation Log

````

### Cycle Documentation
```markdown
### Cycle N: [Timestamp]

**ANTICIPATE:** [Key library/technology and its common patterns]

**HYPOTHESIS:** [Specific, testable theory with an expected, measurable outcome]

**INVESTIGATE:**
- Action: [What I'll do]
- Expected Result: [What I expect if hypothesis is correct]
- Implementation: [Actual code/commands]

**REFLECT:**
- Actual Result: [What really happened]
- Interpretation: [What this means]
- Status: ✅Confirmed | ❌Refuted | 🤔Partial | 🆕Discovery
- Key Learning: [Single, reusable rule learned from the outcome, if applicable]

**DECIDE:**
- Next Action: [The chosen next step]
- Justification: [Why this is the most efficient next step]

---
````

### Safety Protocols

**Prevent Infinite Loops:**

- If 5+ cycles without progress → Change hypothesis domain entirely
- If 10+ cycles without progress → Take a break or get help
- Set maximum time limit for investigation sessions

**Manage Scope Creep:**

- Focus on maximum 3 related hypotheses per session
- Time-box each investigation cycle (5-15 minutes)
- Do "zoom out" reviews every 30 minutes

**Protect Your Codebase:**

- Always work on feature branches for risky experiments
- Commit working state before each major investigation
- Document any system changes for easy rollback
- Keep a log of temporary debugging code to remove later

---

## Advanced A-HIRD Techniques

### Multiple Hypothesis Tracking

When you have several competing theories:

```markdown
**Primary Hypothesis:** [Most likely - investigate first]
**Backup Hypotheses:** [Test these if primary fails]
**Wildcard Theory:** [Unlikely but worth keeping in mind]
```

### Binary Search Debugging

For problems in large systems:

```markdown
**Hypothesis:** Issue exists somewhere in [large area]
**Investigate:** Test the midpoint to divide search space
**Reflect:** Is problem in first half or second half?
**Decide:** Focus investigation on the problematic half
```

### Reproduction-First Strategy

For intermittent or hard-to-trigger bugs:

```markdown
**Hypothesis:** Bug occurs under [specific conditions]
**Investigate:** Create minimal case that triggers the issue
**Reflect:** Can we reproduce it reliably now?
**Decide:** Once reproducible, start investigating the cause
```

---

## When to Use A-HIRD

### Perfect For:

- 🐛 Debugging mysterious bugs
- 🔍 Understanding unfamiliar codebases
- 📊 Performance investigations
- 🧪 Exploratory testing of new features
- 🕵️ Root cause analysis
- 📚 Learning how complex systems work

### Not Ideal For:

- 🚀 Deploying code to production
- 📋 Following established procedures
- ⚡ Bulk operations with known steps
- 💰 Situations where mistakes are expensive

---

## Success Indicators

A-HIRD succeeds when you achieve:

**Fast Learning Cycles:** You quickly build accurate mental models of your system

**Efficient Investigation:** High ratio of useful discoveries to time invested

**Quality Hypotheses:** Your theories increasingly predict what you'll find

**Actual Problem Resolution:** You don't just understand the issue - you fix it

**Knowledge Transfer:** You emerge with insights that help solve future problems

Unlike frameworks focused on preventing mistakes, A-HIRD optimizes for the speed of discovery and depth of understanding that make debugging effective.

---

## Getting Started

1. **Pick a Current Bug:** Choose something you're actively trying to solve
2. **Anticipate the Context:** What's the core technology involved?
3. **Form Your First Hypothesis:** What's your best guess and its expected outcome?
4. **Design a Quick Test:** What's the fastest way to check your theory?
5. **Document Your Process:** Keep a simple log of what you learn
6. **Iterate Rapidly:** Don't overthink - the framework works through practice

The goal isn't perfect process adherence - it's structured thinking that helps you debug more effectively and learn faster from every investigation.
