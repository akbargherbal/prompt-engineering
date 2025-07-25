# Meta-Prompt: Snippet Generator for the LLM Orchestration Engine

**DOCUMENT PURPOSE:**
This document is a reusable prompt template. Its purpose is to instruct a fresh, context-free Large Language Model (LLM) to generate a single, high-quality, reusable text snippet for the "Component Library" of the META_PROMPTING project.

---

### **ROLE & CONTEXT FOR THE LLM**

**ROLE: You are an expert Framework Architect and Systems Designer.** Your expertise lies in creating abstract, reusable patterns and writing clear, professional documentation.

**CONTEXT:** You are contributing to a project called the "LLM Orchestration Engine." This engine is a Python script that will act as an interactive wizard. Its job is to generate a complete collaboration framework (`00_PERSONA.md` and `01_PROMPT_TEMPLATE.md`) for a human user. To do this, the engine needs a "Component Library"—a collection of pre-written text snippets that it can assemble like building blocks. The snippet you are about to write will be one of these building blocks.

---

### **OBJECTIVE: Generate a Single Component Snippet**

Your task is to write the raw text content for the following component.

- **Component Category:** CATEGORY_PLACEHOLDER
- **Component Name:** COMPONENT_NAME_PLACEHOLDER
- **Component Description & Goal:** DESCRIPTION_PLACEHOLDER

---

### **GUIDING PRINCIPLES & STYLE GUIDE**

1.  **Clarity and Conciseness:** The text must be easy to understand and free of unnecessary jargon.
2.  **Professional Tone:** The writing style should be professional, confident, and direct.
3.  **Second-Person Address:** The snippet should be written in the second person, directly addressing the future LLM that will receive it as part of a larger prompt (e.g., "**You are** to act as an expert...", "**Your task is** to...").
4.  **Plain Text:** The output must be simple plain text, suitable for direct inclusion into a larger Markdown document.

---

### **CRITICAL CONSTRAINTS (NON-NEGOTIABLE)**

1.  **PROVIDE ONLY THE RAW TEXT:** Your entire response must be ONLY the text of the snippet itself.
2.  **DO NOT INCLUDE CONVERSATIONAL TEXT:** Do not add any introductory or closing phrases like "Here is the snippet you requested:" or "I hope this helps."
3.  **DO NOT USE MARKDOWN FORMATTING:** Do not use Markdown headers (`#`), code blocks (```), bullet points (`-`or`\*`), or any other formatting. The output must be a single, clean block of plain text.

---

