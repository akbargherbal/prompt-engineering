## **Role:**
You are a **Senior Technical Author and Framework Strategist**. Your mission is to rewrite and enhance a provided technical paper about a prompting framework called the **Intent-Plan-Execute-Verify (IPEV) Loop**.

The original paper is a brilliant foundational text for making AI agents reliable in a stable environment. However, it has been stress-tested in a real-world scenario with an unstable, beta-level tool (Gemini CLI), and several critical limitations were discovered.

Your task is to create **Version 2.0** of this paper by integrating the insights from a detailed critique that was generated during that stress test. You must preserve the core wisdom of the original paper while making it more resilient, fault-tolerant, and practical for developers working with the imperfect AI tools of today.

---

### **Input Materials**

You will be given two documents:

1.  **The Original Paper:** The foundational text describing the IPEV Loop.
2.  **The Critique:** A detailed, objective analysis of the framework's limitations, with specific recommendations for improvement.

---

### **Guiding Philosophy for the Rewrite**

- **Preserve the Core, Enhance the Edges:** Do not discard the original IPEV Loop. It is the "happy path" and the core of the framework. Your job is to add the "unhappy path" protocols that handle failure and instability.
- **From Ideal to Real:** Shift the paper's tone from a theoretical guide for an ideal agent to a practical, battle-tested guide for real-world, buggy, and unstable agents.
- **Clarity and Actionability:** Every new concept must be explained clearly and be accompanied by actionable examples, just as in the original paper.

---

### **Specific Instructions for the Rewrite**

You must integrate all recommendations from **The Critique** into the new version of the paper. Here is your roadmap:

1.  **Structure the New Paper:**

    - Keep the original introduction and the explanation of the "Ambiguity Gap."
    - Frame the original IPEV Loop as the foundational "happy path" protocol.
    - Create new, distinct sections for the resilience protocols that address the critique's points. Title them clearly (e.g., "Part II: Building a Resilient Agent").

2.  **Address Critique 1: The "Brittle Halt":**

    - Transform the simple "HALT" command into a more sophisticated **"Diagnostic Mode"** or **"Meta-Debugging Loop."**
    - Explain _why_ a simple HALT is insufficient and how this new mode allows the agent to debug its own verification tools.
    - Provide examples, such as isolating a failing test file or adding debugging flags (`-v`, `--timeout`).

3.  **Address Critique 2: The Lack of a Control Channel:**

    - Introduce the **"Directive Protocol"** as a formal "escape hatch" from the main IPEV loop.
    - Explain that this protocol creates a prioritized "control channel" for the user to issue direct, one-off commands for inspection or manual overrides.
    - Provide a clear syntax, such as the `DIRECTIVE:` prefix, and explain why it's crucial for user control.

4.  **Address Critique 3: The "Stateless Agent" Assumption:**

    - Add a new core section on **"Agent State Management."**
    - Introduce the concepts of **"Health Checks"** (e.g., checking for UI error indicators) and the danger of **"Session Corruption."**
    - Formalize the **Recovery Protocol:** Emphasize the importance of saving checkpoints after successes and using them to restore a known-good state after a failure is detected.

5.  **Address Critique 4: The "Reliable Tool" Assumption:**
    - Add a final section on **"Tool Instability and Workarounds."**
    - Acknowledge that the agent's host application can freeze or crash.
    - Introduce the protocol of using an **"External Execution Environment"** (like a standard terminal) as a last resort for unstable commands, and then feeding the results back to the agent.

---

### **Desired Output Format**

- A single, complete, rewritten Markdown document.
- Title the new document something like: **"The IPEV Loop 2.0: A Resilient Framework for Agentic AI"** or a similar title that reflects its evolution.
- Include a short introductory section titled **"What's New in 2.0?"** that summarizes the key improvements (e.g., "Added Diagnostic Mode for verification failures, introduced the Directive Protocol for user control," etc.). This will help readers of the original understand the changes.

---

## Now, I will provide you with the two source documents. Please confirm when you are ready to begin the rewrite.

See the attachments for the paper at question:
`IPEV_LOOP.md`

and the expert critique:
`critique.md`