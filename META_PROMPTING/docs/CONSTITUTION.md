### **The Constitution of the META_PROMPTING Framework (v1.0)**

#### **Preamble**

This document defines the unalterable principles of the META_PROMPTING framework. All design decisions, architectural changes, and quality assessments, whether made by a human or an LLM agent, must be measured against this constitution.

---

### **Article I: The Prime Directive**

_The mission that defines success or failure._

1.  **The "8-Hour-to-1-Hour" Transformation:** The framework's sole purpose is to reduce the time required to create a "Gold Standard" collaboration framework from a full day (~8 hours) of manual effort to approximately one hour of focused, high-value fine-tuning.
2.  **Be an Accelerant, Not a Replacement:** The engine is a power tool for an expert. It must accelerate the "Artisan Engineer's" workflow, not attempt to replace their final, nuanced craftsmanship.
3.  **Codify and Scale Expertise:** The framework must solve the "Don't Repeat Yourself" problem for prompt engineering by capturing successful patterns as reusable components, making that expertise scalable and reliable.

---

### **Article II: The User Bill of Rights**

_The non-negotiable requirements of the "Artisan Engineer" persona._

1.  **The Right to a Competent First Draft:** The generated output must be structurally sound and approximately 80% complete. It must feel like a draft prepared by a competent junior partner, ready for senior-level review and refinement.
2.  **The Right to Overcome Inertia:** The framework must eliminate the "blank page problem" by always providing a strong, tangible, and well-structured starting point.
3.  **The Right to Be the Artisan:** The generated framework must be "humble" by design. It must be transparent, easy to understand, and easy to modify, empowering the user to begin the high-value manual fine-tuning stage immediately.
4.  **The Right to a True Meta-Framework:** The system must be genuinely versatile. It must be capable of generating novel frameworks for functionally diverse goals (e.g., technical debugging, strategic planning), proving it is more than a single-purpose template.

---

### **Article III: Foundational Philosophies & Prohibited Actions**

_The core values that guide development and the anti-patterns that define failure._

#### **Section 1: Philosophies to Uphold**

1.  **Configuration Over Code:** The engine's behavior (the "what") must be defined in external, human-readable configuration files. The core script (`orchestrator.py`) is for execution logic (the "how").
2.  **User Supremacy:** The system's "brains" must be fully transparent and editable. The user is the master of the system and has ultimate control.
3.  **Simplicity and Elegance:** The system must be powerful but not over-engineered. We will always prefer the simplest solution that effectively solves the problem at hand.
4.  **Resilience by Design:** The engine must handle failures gracefully. A failed API call or a missing component must not crash the system but trigger a "degraded mode" that informs the user and allows them to proceed.

#### **Section 2: Anti-Patterns to Forbid**

1.  **The "Magic Black Box":** An output that is opaque, un-editable, or difficult to understand is a failure, regardless of its quality.
2.  **Brittle Scaffolding:** A generated output so flawed that it requires more time to fix than to create from scratch is a total failure.
3.  **The Illusion of Choice:** A system that appears flexible but can only produce minor variations of one core template is a design failure.
4.  **External and Evolvable Configuration:** The mapping of goals to components **must** be defined in an external, human-readable file (`goal_map.json`), not embedded within the Python script's logic. **However, the _schema_ of this configuration file is not sacred.** You are free, and indeed encouraged, to critique the current schema and propose improvements to it if you believe a different structure would better serve the project's Prime Directive.
