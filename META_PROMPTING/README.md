# META_PROMPTING: The LLM Orchestration Engine

![Project Status](https://img.shields.io/badge/status-v0.1.0%20%7C%20Auditing-orange)![Language](https://img.shields.io/badge/Python-3.10%2B-blue)![License](https://img.shields.io/badge/license-MIT-green)

An interactive command-line tool for generating expert-level, reusable LLM collaboration frameworks. This project is a "meta-framework"—a system designed to build other systems.

---

## The Core Philosophy: A Force Multiplier for Prompt Engineering

In complex, multi-turn collaborations with Large Language Models (LLMs), the quality of the initial setup is critical. Manually creating and refining persona files and prompt templates for every new project is repetitive and inefficient. This violates the "Don't Repeat Yourself" (DRY) principle.

The **META_PROMPTING** project solves this problem by creating an **Orchestration Engine**. This engine acts as a "factory" that manufactures bespoke, high-quality collaboration frameworks on demand, turning a manual, hours-long process into an automated, seconds-long one. It is a non-linear force multiplier for expert-level LLM interaction.

## How It Works: The Factory Analogy

The engine is composed of three distinct parts:

1.  **The Component Library (`/components`) - The "Parts Bin"**
    A collection of standardized, pre-written text snippets. Each snippet represents a single, reusable pattern—a persona trait, an interaction protocol, or a critical constraint.

2.  **The Orchestrator (`orchestrator.py`) - The "Assembly Line"**
    The core of the project. This is an interactive Python script that acts as a wizard. It asks the user high-level questions about the desired collaboration and then reads the necessary snippets from the Component Library.

3.  **The Generated Framework (`/output`) - The "Final Product"**
    The orchestrator assembles the chosen components into two complete, ready-to-use Markdown files: `00_PERSONA.md` and `01_PROMPT_TEMPLATE.md`. This is the final, tailored framework that the user can immediately use to start a new, expert-level LLM session.

## Project Status & Roadmap

The project has achieved its initial goal of creating a functional `v0.1.0` Orchestration Engine. We are now in a formal, deep-dive audit and refinement phase.

The strategic plan is now divided into five phases:

- [x] **Phase 1: Strategic Planning** - Define the problem, target audience, and core philosophy.
- [x] **Phase 2: System Architecture & Design** - Design the JIT workflow and finalize the initial `goal_map.json` architecture.
- [x] **Phase 3: Build the Orchestrator (v0.1.0)** - Write the `orchestrator.py` script based on the finalized design.
- [ ] **Phase 4: Qualitative Audit (Current Phase)** - Conduct a formal audit using a "Tiger Team" of specialized LLM agents to analyze why the `v0.1.0` output does not yet meet the "80-90% solution" standard.
- [ ] **Phase 5: Framework Evolution (v0.2.0)** - Implement the findings from the audit to evolve the framework's architecture and component generation process.

## Usage (The Final Vision)

Once complete, the engine will be run from the command line.

```bash
# From the root of the META_PROMPTING project
python orchestrator.py
```

This will launch an interactive wizard that guides the user through the configuration process:

```
Welcome to the LLM Orchestration Engine.

What is the PRIMARY GOAL of this task? Choose the workflow that best fits.

--- Technical & Execution ---
 TEACH_OR_EXPLAIN         (Purpose: To teach a concept or document something.)
 DIAGNOSE_ROOT_CAUSE      (Purpose: To find the underlying cause of a problem.)
 REVIEW_AGAINST_STANDARDS (Purpose: To evaluate a piece of work against a set of rules.)
...

--- Strategic & Developmental ---
 DECONSTRUCT_AN_IDEA      (Purpose: Explore a new concept to test its viability and principles.)
...

Your choice: 3

Enter a title for the Persona: The Django Standards Advocate
...

Generating framework files in directory: ./output/Django_Standards_Advocate/
  - SUCCESS: Created 00_PERSONA.md
  - SUCCESS: Created 01_PROMPT_TEMPLATE.md
```

## The Component Library

The library is organized into three categories to ensure a clean and scalable architecture:

- `/components/personas/`: Defines the LLM's role, tone, and identity.
- `/components/protocols/`: Defines the rules of engagement and the interaction model.
- `/components/constraints/`: Defines non-negotiable rules to protect output integrity.

### How to Add a New Component

The framework is designed to be extensible. To add a new component (e.g., a new persona trait):

1.  **Define the Job:** Add a new JSON object to the `docs/generation_jobs.json` file, specifying the new component's category, name, and description.
2.  **Generate the Component:** Run the component generation script, which will call the LLM API to write the new snippet file.
3.  **Integrate into the Orchestrator:** If the component is part of a new goal, update `goal_map.json`. The `orchestrator.py` script will automatically pick it up without code changes.

## License

This project is distributed under the MIT License.

```

---

### **Summary of Final Actions**

Now that you have the final `README.md`, here is the complete checklist of actions to finalize this phase:

1.  **Update `README.md`:** Replace the content of your `README.md` with the final version provided above.
2.  **Archive Obsolete Files:** Move the following list of documents into a `LEGACY/` or `archive/` directory:
    *   `docs/DESIGN_PHILOSOPHY.md`
    *   `docs/STRATEGIC_PLAN.md`
    *   `SIMULATIONS/SESSION_03/synthesis_report.md`
    *   `docs/PROMPT_SNIPPET_GENERATOR.md`
    *   `docs/generation_jobs.json`
    *   `docs/AB_TESTING.md`

Once these two actions are complete, your project documentation will be perfectly synchronized with our current strategy. We are then ready for you to generate the smoke test examples for the Audit Committee.
```
