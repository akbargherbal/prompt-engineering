Here is the complete, user-ready Markdown content for "The Rulebook" worksheet.

***

### **The Rulebook**

You've documented the pain and gathered your evidence. Now it's time to define the laws of physics for your simulation. This is where you set the boundaries for the AI, ensuring its proposed solution is not just clever, but also practical, safe, and viable within the reality of your codebase.

---

#### **Step 1: Establish Your Constraints (The Physics of Your System)**

**Why this is critical:** An LLM, left to its own devices, doesn't understand your project's specific limitations. It might suggest using a library you can't import, a language version you don't support, or a design pattern that violates your team's style guide. By defining constraints upfront, you are grounding the simulation in reality. You're telling the AI, "Don't break these fundamental laws when you design a solution."

**1. What are the absolute, non-negotiable technical constraints the solution must adhere to?** Think about programming languages, frameworks, specific library versions, or environment limitations.

*   _Example: The refactoring script must be written in Python 3.9+. It cannot introduce any new third-party dependencies besides the target `super-logger` library. The solution must run within our existing Docker-based development environment without requiring changes to the Dockerfile._

> **Your Answer:**
>
>

**2. Are there any performance, security, or coding style constraints that are inviolable?** This is where you encode your team's standards and non-functional requirements.

*   _Example: The new logging initialization must not add more than 5ms to the application's startup time. All new code must be formatted with the `black` code formatter. The solution must not require any changes to our production IAM roles._

> **Your Answer:**
>
>

---

#### **Step 2: Define Your Success Criteria (The Definition of 'Done')**

**Why this is critical:** A vague goal leads to a vague solution. Asking an LLM to "fix the logging" is an invitation for a meandering, unhelpful response. By defining a precise, measurable 'Definition of Done,' you give the simulation a clear target. This transforms the AI from a brainstormer into a focused problem-solver aiming for a specific, verifiable outcome.

**1. Functionally, what is the single most important outcome?** If the final solution does only one thing perfectly, what is it?

*   _Example: The primary outcome is that all instances of `from old_service import api_client` are replaced with `from new_sdk.client import NewApiClient`, and all `api_client.call()` methods are correctly updated to the new `NewApiClient().make_request()` signature._

> **Your Answer:**
>
>

**2. How will you objectively measure or verify that the solution is successful?** What specific commands would you run or what would you look for to know, without a doubt, that it worked?

*   _Example: Success will be confirmed if: 1) The application's full test suite passes with a `pytest` command. 2) A static analysis search for `"from old_service"` returns zero results in our primary application directory. 3) The refactored code successfully makes a test API call to the staging environment._

> **Your Answer:**
>
>

---

#### **Step 3: State Your Anti-Goals (The Minefield)**

**Why this is critical:** Sometimes, a solution can be technically correct but strategically wrong. It might solve the immediate problem while creating a new, bigger one. Anti-goals help the AI avoid these traps. You are explicitly mapping out the 'undesirable solutions' and 'negative side-effects,' thereby steering the simulation away from paths that lead to technical debt, security holes, or operational nightmares.

**1. What are some 'technically correct' but undesirable approaches you want to explicitly forbid?** Think about shortcuts or "clever" solutions that would violate the spirit of the task.

*   _Example: DO NOT simply create a wrapper class that makes the new SDK mimic the old API client's interface. The goal is to fully migrate to the new SDK's patterns, not to hide the old patterns behind another layer of abstraction. DO NOT just comment out the failing code._

> **Your Answer:**
>
>

**2. What potential negative side-effects must the solution avoid at all costs?** Think about what could go wrong in the code or the system as a result of this change.

*   _Example: The solution must not change any public-facing API endpoints or their JSON response structures. It must not alter the core business logic contained within the functions being refactored. It absolutely must not introduce any changes that would cause database schema migrations to be required._

> **Your Answer:**
>
>

***

Great work. You've now established a clear, bounded problem space. With these rules, constraints, and definitions of success, you've built the guardrails that will guide the LLM toward a high-quality, relevant solution. You're ready for the final step: **The Assembly Line.**