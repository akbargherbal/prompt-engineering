# Mission: Autonomously Translate Django Testing to FastAPI

## 1. Your Primary Objective
Your goal is to create a comprehensive testing guide by translating principles from a series of source markdown files and appending the results to a single output file.

## 2. The IPEV Protocol (Intent-Plan-Execute-Verify)
For every file you process, you MUST follow this four-step loop. This is your primary operational directive.

1.  **INTENT:** State the high-level goal for the current file (e.g., "Process `01_the-why-of-testing-in-django.md`").
2.  **PLAN:** Propose the precise, low-level commands you will execute.
    *   For file I/O, you MUST specify the function and mode (e.g., `open('path', 'a')` for appending).
    *   **Crucially, you must state how you will append the content. Your default file-writing tool may overwrite; you must explicitly use an append method.**
3.  **EXECUTE:** Run the exact commands from your plan.
4.  **VERIFY:** After execution, perform a check to confirm the operation was successful.
    *   For an append operation, a suitable verification is to check that the output file's size has increased.
    *   If verification fails, you must halt and report the failure.

## 3. Mission Parameters
*   **Source Directory:** `django-testing-with-pytest-from-zero-to-confident/`
*   **Output File:** `From_Django_Testing_to_FastAPI_Testing.md`
*   **File Processing Order:** Process files in strict numerical order, starting with `00_front-matters.md`.

## 4. Execution Flow
1.  Acknowledge these instructions.
2.  Initialize the process by creating the output file if it doesn't exist.
3.  Begin the IPEV loop, starting with the first file.
4.  Continue the loop for all subsequent files in numerical order until completion.
5.  Signal when the mission is complete.

## 5. Content Generation Schema
For each chapter, your appended output *must* follow this exact markdown structure.

---
# Chapter X: [Original Django Chapter Title] → FastAPI Translation

## Core Concepts & FastAPI Translation
(Analysis of concepts, addressing async, dependency injection, etc.)

## Practical FastAPI Examples
(Complete, runnable FastAPI code examples.)

## Key Takeaways
(A concise bulleted list.)

---

Now, begin.