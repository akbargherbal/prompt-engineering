**You are a senior test engineer specializing in Pytest and Playwright.** Your task is to create a comprehensive end-to-end test suite for a web application based on the provided project context, feature list, and HTML mockup.

**Project Context:**

```

## Tech Stack
*   Backend Framework: FastAPI (Python)
*   Frontend Approach: HTMX for server-driven HTML.
*   Client-side Interactivity: AlpineJS for small, in-page dynamic behaviors.
*   Styling: Tailwind CSS
*   Testing Framework: Pytest with Playwright.
```

**Feature Specification:**

```
current_features.json
```

**UI Structure:**

```
STATIC_MOCKUP.html
```

**Your Task:**
Create a single Python file named `tests/test_app_features.py`. This file must contain a complete test suite that validates **every feature** listed in `current_features.json`.

**Requirements for the Test Suite:**

1.  For each feature in the JSON file, generate one distinct `test_` function.
2.  Use descriptive function names that match the feature (e.g., `test_select_chat_model_flash`).
3.  Use Playwright locators to interact with the elements defined in `STATIC_MOCKUP.html`.
4.  Add assertions that directly verify the "behavior" and "feedback" described for each feature in the JSON file.
5.  Add a comment above each test function referencing the original `featureName` from the JSON for traceability.

**Now, generate the complete `tests/test_app_features.py` file.**
