# The Simulation Starter Kit

## Worksheet 1: The Pain Journal

---

Welcome to the first step of the **Developer's Mise en Place**. Before we can ask an LLM to design a better system, we first need to understand the current one—warts and all. The Pain Journal is a structured exercise for articulating a recurring, tedious, or inefficient process that plagues your workflow.

Think of this as a "friction log." By documenting the precise steps and frustrations of a manual task, you're not just complaining; you're gathering critical data. This narrative becomes the foundation for the LLM to understand the *systemic problem*, not just the surface-level symptoms. A well-defined problem is a half-solved problem. Let's get started.

---

### **Step 1.1: Identify the Chore**

First, let's put a name to the pain. We're looking for a task you do repeatedly that feels inefficient, risky, or just plain soul-crushing. This is the "death by a thousand cuts" task that is a perfect candidate for a systemic solution.

**What is the recurring manual task that feels like a constant source of friction in your workflow?**

> _Example: Manually recovering and re-processing failed items from a large batch job by parsing log files._
>
> > **Your Answer:**
> >

---

### **Step 1.2: Narrate the Process**

Now, let's get specific. A great simulation requires the LLM to understand the *sequence* of events and the hidden dependencies in your manual workflow. Explaining the step-by-step process reveals the subtle inefficiencies and cognitive load that a simple summary would miss.

**Walk me through the last time you performed this task. Describe the process step-by-step, as if you were explaining it to a new team member. Be painfully specific and don't leave anything out.**

> _Example:_
> _1. I get a notification that the nightly data enrichment job has completed with errors._
> _2. I SSH into the production application server._
> _3. I navigate to the `/var/log/jobs` directory._
> _4. I use `grep 'ERROR: API_TIMEOUT'` on a 5GB log file to find all the lines with failed API calls._
> _5. I manually copy the `item_id` from each error line and paste it into a local text file called `failed_ids.txt`._
> _6. I write a small, one-off Python script to read `failed_ids.txt` and format it into a JSON array._
> _7. I go to our internal admin dashboard and paste the JSON into the "Manual Re-queue" tool._
> _8. I wait for the re-queue job to finish and then check the logs again to make sure it worked._
>
> > **Your Answer (list your steps):**
> >

---

### **Step 1.3: Quantify the Pain**

Quantifying the pain isn't just about venting; it's about building the business case for a solution and defining the magnitude of the problem for the LLM. This gives the simulation a clear understanding of the stakes and what a "good" solution should improve.

**A) How much time does this process typically take each time you do it, and how often do you have to do it (e.g., daily, weekly, per-release)?**

> _Example: It takes about 30-45 minutes each time. I have to do this after every major data import, which is 2-3 times a week._
>
> > **Your Answer:**
> >

**B) What's the most frustrating or riskiest part of this manual process? Where are you most likely to make a human error?**

> _Example: The riskiest part is manually copy-pasting the `item_id`s from the log file. If I miss one, that customer's data is never enriched. It's also incredibly boring, so I'm prone to distraction._
>
> > **Your Answer:**
> >

---

### **Step 1.4: Define the Systemic Problem**

You've identified the task, detailed the steps, and quantified the cost. Now it's time to synthesize. The manual process you described is just a *symptom*. The goal here is to diagnose the underlying *disease*. This is the crucial leap that separates asking for a simple script from asking for a robust, systemic solution.

**Looking at your answers above, what is the core, systemic problem you are trying to solve? Move beyond the specific actions (like "parsing logs") and describe the underlying weakness in the current system.**

> _Example: The data processing pipeline lacks a built-in, automated dead-letter queue and retry mechanism. The system's design forces fragile, manual human intervention to handle common failure modes like API timeouts, which introduces risk of data loss and consumes significant developer time._
>
> > **Your Answer:**
> >

---
**Excellent work.** You have now documented the "before" state. This Pain Journal provides the essential narrative and problem statement that will guide the entire simulation process. You're ready to move on to the next step: **The Evidence Locker.**