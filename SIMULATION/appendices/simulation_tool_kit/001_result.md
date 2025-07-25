### **Worksheet 1: The Pain Journal**

#### **Phase 1 of 4: Your Developer's Mise en Place**

Welcome to the Simulation Starter Kit! This first worksheet, **The Pain Journal**, is the most critical part of the entire process. Before we can ask an LLM to design a better system, we first need a brutally honest account of the system we're stuck with today.

The goal here isn't just to list tasks; it's to capture the _frustration_. The tedious copy-pasting, the one-off scripts you write and delete, the mental juggling—this "pain" contains the hidden requirements and unspoken inefficiencies. By documenting it, you're not just complaining; you're providing the LLM with a rich, detailed map of the problem space it needs to navigate.

Let's get started.

---

##### **Step 1: Define the Core Task**

**Why we do this:** We need to anchor your pain to a specific, recurring mission. LLM simulators work best when they have a clear, high-level goal to optimize for. Defining this first gives us a "north star" for the entire exercise. It's the "job to be done" that triggers your manual, tedious process.

**What is the high-level goal you are trying to accomplish when you start this process?** Think in terms of the outcome, not the steps.

- _Example: I need to reliably re-process a batch of specific failed API calls that were identified in our server logs from the previous night._

> **Your Answer:**
>
> ---

##### **Step 2: Chronicle the Manual Steps**

**Why we do this:** A system isn't just a set of scripts; it's also the human "connective tissue" between them. This is where the most significant friction lives—the `grep`, the `cat`, the copy-paste from your terminal to a text file, the manual check in a UI. Detailing every single step, no matter how small, exposes the full scope of the manual labor that the LLM needs to simulate and ultimately replace.

**List every single manual action you take to accomplish the core task, from the very first command to the final "all clear."** Be painfully specific. What do you click? What commands do you run? What do you look for? Don't gloss over anything.

- _Example:_
  1.  _SSH into the production server._
  2.  _`cd` into the `/var/log` directory._
  3.  _`grep` the logs for `"ERROR: Failed processing for item_id"` to find the failures._
  4.  _Manually copy the list of `item_id`s from my terminal._
  5.  _Paste the IDs into a new local file called `rerun.txt`._
  6.  _Write a new one-off script called `temp_fix.py`._
  7.  _In the script, write code to open `rerun.txt`, loop through the IDs, and call our `reprocess_item()` API for each one._
  8.  _Run `python temp_fix.py`._
  9.  _Go back to the server and `grep` the logs again to see if the reprocessing worked._
  10. _Delete `temp_fix.py` and `rerun.txt` from my machine._

> **Your Answer:**
>
> ---

##### **Step 3: Pinpoint the Exact Pain**

**Why we do this:** A list of steps is just data; a list of _frustrations_ is a design brief. By explicitly calling out what's annoying, error-prone, or time-consuming, you're telling the LLM simulator what to prioritize. This step turns your process description into a set of problems to be actively solved, guiding the simulation toward a solution that addresses what actually matters to you.

**Looking back at your list of steps, which parts are the most tedious, repetitive, or risky?** Where do you feel your time is being wasted? Where do mistakes happen?

- _Example: Writing that `temp_fix.py` script every single time is a massive waste of energy; I'm basically rewriting the same logic with minor changes. Also, manually copy-pasting the IDs from my terminal into a text file is tedious, and I've occasionally missed an ID or copied a line twice, which corrupts the whole process._

> **Your Answer:**
>
> ---

##### **Step 4: State the Systemic Problem**

**Why we do this:** This is where we synthesize everything. We transform the detailed actions and frustrations into a single, powerful problem statement. By framing the issue as a _missing capability_ in your current system (e.g., "The system lacks..."), you elevate the goal from "make my personal steps easier" to "design a better system for everyone." This is the precise framing an LLM simulator needs to start thinking about a robust, systemic solution.

**Based on your answers above, summarize the core, underlying problem in one or two sentences.** What is your current workflow or system fundamentally lacking?

- _Example: Our current workflow lacks an automated, idempotent way to identify, isolate, and re-run failed jobs from our logs, which forces developers into slow, error-prone manual scripting for every recovery incident._

> **Your Answer:**
>
> ---

**Excellent work.** You've successfully documented the problem and translated your frustration into a clear, systemic challenge. This "Pain Journal" is the foundation for everything that follows.

**Next Up: [Worksheet 2: The Evidence Locker](./worksheet-2-evidence-locker.md)**, where we'll gather the concrete artifacts the LLM needs to understand the technical context of this problem.