# Gemini CLI: Quick Start

Welcome to the Gemini CLI! This guide will help you get up and running in just a few minutes.

## 1. Introduction: What is Gemini CLI?

Gemini CLI is an interactive command-line tool that brings the power of Google's Gemini models directly to your terminal. Think of it as a smart assistant that lives where you code.

At its core, the CLI provides a conversational "Read-Eval-Print Loop" (REPL) to chat with the AI. However, its real power comes from its ability to use **tools**. These tools allow the Gemini model to go beyond just answering questions and actively help you with your development tasks by:

*   **Interacting with your local file system:** Read, write, and search through your project files.
*   **Executing shell commands:** Run scripts, use git, and manage your development environment.
*   **Fetching web content:** Summarize articles or pull in information from the internet.

Whether you want to understand a new codebase, refactor a function, write documentation, or automate a workflow, the Gemini CLI is designed to be your go-to partner in the terminal. Let's get started!

## 2. Installation

You can run the Gemini CLI instantly without a permanent installation using `npx`. This is the quickest way to get started.

Open your terminal and run:
```bash
npx @google/gemini-cli
```

For a permanent installation that you can run from anywhere using the `gemini` command, you can install it globally:
```bash
npm install -g @google/gemini-cli
```

## 3. Authentication

To use the Gemini CLI, you'll need an API key.

1.  **Get your key:** Obtain your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  **Set the environment variable:** You need to make this key available to the CLI through an environment variable. For your current terminal session, run:

    ```bash
    export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    (Replace `YOUR_GEMINI_API_KEY` with the key you just obtained).

    For a more permanent solution, you can add this line to your shell's startup file (like `~/.bashrc` or `~/.zshrc`) or create a `.env` file in your project directory.

## 4. Your First Prompt: Interacting with the AI

You can interact with Gemini in two main ways.

### Non-Interactive Mode
For quick, one-off questions, you can pass a prompt directly to the CLI. It will print the answer and exit.

```bash
gemini -p "What is a pure function in JavaScript?"
```
or pipe your question to it:
```bash
echo "What is a pure function in JavaScript?" | gemini
```

### Interactive Mode (REPL)
For a conversational experience, start the CLI in interactive mode. This is where the magic happens.

```bash
gemini
```

This will open a prompt where you can chat with the AI, ask follow-up questions, and use tools. Try asking it to write some code:

> `> write a node.js function that returns a random quote from an array`

You can exit the interactive session at any time by typing `/quit` or pressing `Ctrl+D`.

## 5. Providing Context: Working with Local Files

The most powerful feature of the Gemini CLI is its ability to understand your code. You can provide file or directory contents as context for your prompts using the `@` command.

Start an interactive session (`gemini`) and try the following:

*   **Ask about a single file:**
    > `> @README.md what is the purpose of this project?`

*   **Ask about a whole directory:**
    > `> @src/ summarize the code in this directory`

The CLI will read the file(s) and feed their content to the model along with your question. By default, it intelligently ignores files listed in your `.gitignore`.

## 6. Executing Commands: Using Tools

Gemini can also execute shell commands on your behalf. This is useful for running scripts, checking git status, or listing files.

You can run any shell command directly by prefixing it with `!`.

*   **List files in the current directory:**
    > `> !ls -l`

*   **Check your git status:**
    > `> !git status`

The model can also decide to use the shell tool on its own. For example, you could ask:
> `> what files are in the current directory?`

The model will likely respond by asking for your permission to run `ls`. This user-approval step is a key safety feature for any tool that can have side effects.

## 7. Basic Customization

You can tailor the Gemini CLI to fit your workflow and preferences.

### Change the Theme
The CLI comes with several built-in color schemes. To change them, just type `/theme` in an interactive session and choose from the list.

> `> /theme`

Your selection is saved automatically for future sessions.

### Set Project-Specific Instructions
You can give the AI specific instructions for your project by creating a `GEMINI.md` file in your project's root directory. The CLI automatically loads this file and uses its content as context for all your prompts.

For example, create a `GEMINI.md` file with the following content:

```markdown
# Project Instructions

- Always use TypeScript.
- Generate code comments in JSDoc format.
- Avoid introducing external dependencies.
```

Now, when you ask Gemini to write code in this project, it will follow your rules.
