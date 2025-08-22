# HIRD Framework: A Testing & Debugging Approach for AI Code Assistants

## Why Existing Frameworks Don't Work for Testing

Most AI agent frameworks are designed around **execution tasks** - scenarios where you know exactly what you want to accomplish and need to prevent the AI from misinterpreting your instructions. The popular IPEV framework (Intent-Plan-Execute-Verify) exemplifies this approach: it requires agents to explicitly state their plan before taking any action, then verify the results afterward.

IPEV works great for tasks like "process these files and generate a report" or "deploy this code to production." But it fails for testing and debugging because:

- **Testing is exploratory** - you don't know what you'll find until you look
- **Debugging requires speed** - slow iteration kills your problem-solving flow  
- **Investigation branches unpredictably** - you can't plan a linear sequence when each discovery changes your next move

What we need is a framework designed specifically for **discovery-driven work** where learning and understanding are the primary goals.

---

## The HIRD Framework: Built for Discovery

HIRD (Hypothesis-Investigate-Reflect-Decide) structures the natural thought process of effective debugging. Instead of forcing predetermined plans, it organizes the cycle of forming theories, testing them quickly, and adapting based on what you learn.

---

## The Four-Phase Cycle

### 1. **HYPOTHESIS** (The "Theory")
**Purpose:** Articulate your current best guess about what's happening

**Format:** "I suspect [specific theory] because [observable evidence]"

**Examples:**
- "I suspect the API timeout is caused by a database lock because the error only happens during high-traffic periods"
- "I think this React component isn't re-rendering because the state object reference hasn't changed"
- "The memory leak might be from event listeners not being cleaned up in useEffect"

**Key:** Keep hypotheses **specific and testable**, not vague hunches.

---

### 2. **INVESTIGATE** (The "Quick Test")
**Purpose:** Design the minimal experiment to test your hypothesis

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
- "Add console.log to track when useEffect cleanup runs"
- "Write a unit test that simulates the timeout condition"
- "Check database query execution time with EXPLAIN"
- "Create minimal reproduction with just the problematic component"

---

### 3. **REFLECT** (The "What Did We Learn?")
**Purpose:** Interpret results and update your understanding

**Questions to Answer:**
- Did this confirm or contradict my hypothesis?
- What new information did I discover?
- What does this tell me about the broader system?
- What new questions does this raise?

**Result Categories:**
- ✅ **Confirmed:** "The timeout IS caused by database locks - query time jumps from 50ms to 30s during peak hours"
- ❌ **Refuted:** "Event listeners ARE being cleaned up properly - the leak must be elsewhere"  
- 🤔 **Partial:** "State object reference is changing, but component still not re-rendering - need to check memo dependencies"
- 🆕 **New Discovery:** "Found unexpected N+1 query pattern that explains the performance issue"

---

### 4. **DECIDE** (The "Next Move")
**Purpose:** Choose your next action based on what you learned

**Decision Types:**

**Continue Investigating:**
- Dive deeper into the same area
- Test a refined version of your hypothesis
- Explore related components or systems

**Pivot Investigation:**
- Switch to investigating a different theory
- Follow newly discovered leads
- Try a completely different debugging approach

**Implement Solution:**
- Apply the fix you've identified
- Write proper tests to prevent regression
- Refactor code based on your new understanding

**Escalate or Document:**
- Get help from a domain expert
- Document findings for future reference
- File detailed bug reports with your evidence

---

## HIRD in Practice: A Real Example

**Problem:** React app becomes unresponsive after user interactions

### Cycle 1
**HYPOTHESIS:** Memory leak from components not unmounting properly

**INVESTIGATE:** Add memory profiling and component lifecycle logging
```javascript
useEffect(() => {
  console.log('Component mounted:', componentName);
  return () => console.log('Component unmounted:', componentName);
}, []);
```

**REFLECT:** ✅ **Confirmed** - Components mounting but not unmounting when expected

**DECIDE:** Continue investigating - dive deeper into what's preventing unmounting

### Cycle 2  
**HYPOTHESIS:** Parent component holding references preventing unmount

**INVESTIGATE:** Check React DevTools component tree and add ref tracking

**REFLECT:** ❌ **Refuted** - Parent is correctly removing child from render tree

**DECIDE:** Pivot investigation - look for event listeners or timers

### Cycle 3
**HYPOTHESIS:** Event listeners attached to window/document not being cleaned up

**INVESTIGATE:** Add logging to all addEventListener/removeEventListener calls

**REFLECT:** 🆕 **New Discovery** - Found interval timer in useEffect without cleanup

**DECIDE:** Implement solution - add proper cleanup to useEffect

---

## Implementation Guide for AI Assistants

### Session Setup Template
```markdown
# Debug Session: [Brief Problem Description]

**Context:** [Codebase area, recent changes, error symptoms]
**Time Budget:** [How long before escalating/taking break]  
**Risk Level:** [Can we safely experiment? Need to be careful?]

**Initial Hypothesis:** [Your starting theory]

---
## Investigation Log
```

### Cycle Documentation
```markdown
### Cycle N: [Timestamp]

**HYPOTHESIS:** [Specific, testable theory]

**INVESTIGATE:** 
- Action: [What I'll do]
- Expected Result: [What I expect if hypothesis is correct]
- Implementation: [Actual code/commands]

**REFLECT:**
- Actual Result: [What really happened]
- Interpretation: [What this means]
- Status: ✅Confirmed | ❌Refuted | 🤔Partial | 🆕Discovery

**DECIDE:** [Next action and reasoning]

---
```

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

## Advanced HIRD Techniques

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

## When to Use HIRD

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

HIRD succeeds when you achieve:

**Fast Learning Cycles:** You quickly build accurate mental models of your system

**Efficient Investigation:** High ratio of useful discoveries to time invested

**Quality Hypotheses:** Your theories increasingly predict what you'll find

**Actual Problem Resolution:** You don't just understand the issue - you fix it

**Knowledge Transfer:** You emerge with insights that help solve future problems

Unlike frameworks focused on preventing mistakes, HIRD optimizes for the speed of discovery and depth of understanding that make debugging effective.

---

## Getting Started

1. **Pick a Current Bug:** Choose something you're actively trying to solve
2. **Form Your First Hypothesis:** What's your best guess right now?
3. **Design a Quick Test:** What's the fastest way to check your theory?
4. **Document Your Process:** Keep a simple log of what you learn
5. **Iterate Rapidly:** Don't overthink - the framework works through practice

The goal isn't perfect process adherence - it's structured thinking that helps you debug more effectively and learn faster from every investigation.