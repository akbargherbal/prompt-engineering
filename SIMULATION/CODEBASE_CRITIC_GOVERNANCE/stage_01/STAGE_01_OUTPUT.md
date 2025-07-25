### Core Principles Checklist

---

### 1. The Prime Directive

The single, quantifiable mission that defines success or failure for the project.

- [ ] **Achieve the "8-Hour-to-1-Hour" Transformation:** The framework must reduce the time to create a "Gold Standard" collaboration framework from a full day (~8 hours) of manual work to approximately 1 hour of focused, manual fine-tuning built upon a 5-minute generated scaffolding.
- [ ] **Act as an Accelerant, Not a Replacement:** The project's sole purpose is to be a powerful force multiplier for a high-quality, manual process. It must accelerate the "Artisan Engineer," not attempt to replace their final, value-add craftsmanship.
- [ ] **Systematize Expertise (The DRY Principle):** The engine must solve the "Don't Repeat Yourself" problem for prompt engineering by codifying successful patterns into a reliable, generative, and scalable process.

---

### 2. The Target Audience Needs

The non-negotiable requirements for the "Artisan Engineer" user persona.

- [ ] **Provide a "Good Enough" First Draft:** The generated output must be structurally sound and approximately 80% of the way to the final goal, serving as a draft from a competent junior partner.
- [ ] **Eliminate the "Blank Page" Problem:** The framework's primary value is overcoming the activation energy of starting from scratch. It must always provide a strong, tangible starting point.
- [ ] **Leave Room for the Artisan:** The generated framework must be "humble"—easy to edit, modify, and refine. Its goal is to get the user to the high-value manual fine-tuning stage as quickly as possible.
- [ ] **Ensure True Flexibility:** The system must be a true meta-framework, capable of generating novel frameworks for diverse tasks (e.g., technical execution, strategic planning) via its orchestrator and component library.

---

### 3. Guiding Philosophies & Anti-Patterns

The core values that guide development and the negative outcomes the project must explicitly avoid.

#### **Guiding Philosophies to Uphold**

- [ ] **Configuration Over Code:** The engine's logic (the "what") must be separated from its execution (the "how"). The system's behavior must be configurable via external files (e.g., `goal_map.json`) without requiring changes to the core Python script.
- [ ] **User Has Ultimate Control:** The system's "brains" must be fully exposed, transparent, and editable. The user is the master of the system, not a passive operator.
- [ ] **Simplicity and Elegance:** The system should be powerful but not over-engineered, using simple solutions that match the scale of the problem.
- [ ] **Resilience and Graceful Degradation:** The engine must not crash or block the user on failure (e.g., a failed API call). It should enter a "degraded mode," log the issue, insert a placeholder, and allow the user to complete the workflow manually.

#### **Anti-Patterns to Avoid**

- [ ] **The "Magic Black Box":** A system that produces a "perfect" but opaque or un-editable output is a failure.
- [ ] **Brittle Scaffolding:** A generated output so flawed that it takes more time to fix than to write from scratch is a failure.
- [ ] **The Illusion of Choice:** A system that appears flexible but can only produce slight variations of a single, pre-defined framework is a failure.
- [ ] **Hard-Coded Logic:** Any requirement to modify the `orchestrator.py` script to add new goals or components is a critical design failure.
