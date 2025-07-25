# Design Philosophy: The Prime Directive

**DOCUMENT PURPOSE:** This document is the constitution of the META_PROMPTING project. It defines the core "why" of our work, the user we are serving, and the ultimate test for success. All design and development decisions for the `orchestrator.py` engine and its surrounding framework must be measured against these principles.

---

### **1. The Prime Directive: The "8-Hour-to-1-Hour" Transformation**

This project exists to solve a single, expensive problem articulated in `docs/LEGACY_DOC.md`: **"It takes a full day to hand-craft a persona and prompt template like this."**

The fundamental mission of this framework is to crush this time cost.

Success for this project is not ambiguous. It is defined by a single, pass/fail test: its ability to transform the workflow.

- **The Old Way:** A full day (~8 hours) of manual, artisanal work to create a "Gold Standard" collaboration framework.
- **The New Way (Our Definition of Success):**
  1.  **5 minutes** using the Orchestration Engine to generate a "Good Enough" scaffolding (`00_PERSONA.md` and `01_PROMPT_TEMPLATE.md`).
  2.  **~1 hour** of focused, high-value **MANUAL fine-tuning** to elevate that scaffolding to Gold Standard quality.

If the framework cannot reliably achieve this "8-hour-to-1-hour" transformation, it has failed. Its sole purpose is to act as a powerful **accelerant** for a high-quality, manual process—not to replace it.

---

### **2. The Target Audience: The "Artisan Engineer"**

We are building this tool for a single user persona: the **Artisan Engineer**. Understanding this duality is critical to all design choices.

- **The Artisan:** They have exacting standards and know that the final 20% of quality—the nuance, the voice, the perfect phrasing—comes from manual craftsmanship. They value their ability to apply this final polish.
- **The Engineer:** They are a systems thinker who despises repetitive, low-value work. They view the 80% of scaffolding as a solved problem that should be automated so they can focus their creative energy where it matters most.

This framework is a power tool for the Engineer, designed to empower the Artisan.

---

### **3. User Profile: Needs, Wants, and Values**

#### **What This User NEEDS (The Non-Negotiables)**

- **A "Good Enough" First Draft:** The generated output must be structurally sound and 80% of the way there. It must feel like a competent junior partner prepared the draft for the senior artisan to perfect.
- **The Avoidance of the "Blank Page":** The framework's primary value is in overcoming the activation energy required to start from nothing. It must always provide a strong, tangible starting point.
- **A Flexible Orchestrator & A Rich Component Library:** The system must be able to generate novel frameworks for diverse tasks (e.g., technical debugging one day, strategic planning the next) to prove it is a true meta-framework, not a one-trick pony.
- **Leaving Room for the Artisan:** The generated framework must be "humble." It should be easy to edit, modify, and refine. Its goal is to get the user to the valuable manual fine-tuning stage as quickly as possible.

#### **What This User WANTS (The Quality-of-Life Features)**

- **Clarity & Intuitiveness:** The system's logic should be transparent. The file structure is clean, the configuration (`goal_map.json`) is human-readable, and the interactive wizard is unambiguous.
- **Ultimate Control:** The user wants to be the master of the system. The engine's "brains" are fully exposed and editable, giving them complete control over its behavior.
- **Domain Agnosticism:** The tool must support both technical execution and strategic thinking, reflecting the user's multi-faceted needs (the "50/50 balance").
- **Power and Trust:** The tool should be designed for an expert. It prioritizes a direct, powerful workflow over unnecessary hand-holding.

#### **What This User APPRECIATES (The Guiding Philosophies)**

- **The DRY Principle ("Don't Repeat Yourself"):** This framework is the ultimate application of DRY to prompt engineering.
- **Configuration Over Code:** The user values the separation of logic (the script) and data (the configuration files).
- **Simplicity & Elegance:** The system should be powerful but not over-engineered. We use simple solutions that match the scale of the problem.

#### **What This User FROWNS UPON (The Anti-Patterns)**

- **The "Magic Black Box":** A system that produces a "perfect" but un-editable or opaque output is useless.
- **Brittle Scaffolding:** A generated output so flawed that it takes more time to fix than to write from scratch.
- **The Illusion of Choice:** A system that appears flexible but can only produce slight variations of the `LEGACY_DOC.md`.
- **Hard-Coded Logic:** Any requirement to modify the Python script to add new goals or components would be a critical design failure.
