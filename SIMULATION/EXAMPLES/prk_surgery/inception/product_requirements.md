# Gemini CLI Bridge - Problem Statement

## The Challenge

I recently had PRK surgery and need to reduce eye strain while coding. I'm using Google's Gemini CLI as an agentic code mentor, but its terminal interface creates too much context switching and strain. I want to work entirely within VSCode—writing prompts in one file, getting responses in another—both located inside my chosen repository, all in a comfortable, readable format.

## What I Want

**A background service that watches my `prompt.md` file (in my repository) and automatically feeds it to Gemini CLI, then saves the response in `TUTORIALS/output.md` (in the same repository), where I can read it comfortably.**

### My Ideal Workflow

1. Open `prompt.md` (inside my repo) in VSCode and type my question
2. Save the file (Ctrl+S)
3. Bridge detects the save and sends content to Gemini CLI running in background
4. Gemini processes and responds
5. Response gets written to `TUTORIALS/output.md` (also inside my repo) in pure Markdown
6. I manually open the output file in VSCode preview or Chrome to read it
7. Repeat for next prompt

### Key Requirements

**Must Have:**

- Both `prompt.md` and `TUTORIALS/output.md` live inside the same repository I choose during setup
- All responses append `TUTORIALS/output.md`
- Output is pure Markdown—no HTML whatsoever
- Gemini CLI runs in the background inside my chosen repository
- File watching that responds immediately when I save
- Zero-to-minimum terminal interaction after initial setup
- Everything readable and editable in VSCode

**Must Not Have:**

- Auto-refreshing output (I read at my own pace)
- HTML formatting in output
- Complex UI elements

**Safety:**

- Don’t let me accidentally run this in system directories
- Basic validation that the target directory is actually a code repository

## Current Problem

The v0.0.4 I have now:

```
See actual codebase
```

## Success Looks Like

I can work for hours just switching between two VSCode tabs—`prompt.md` for writing prompts, `TUTORIALS/output.md` for reading responses. No terminal windows, no external browsers (unless I choose), no auto-updating content. Just clean, readable Markdown responses that help me understand my codebase better while being gentle on my recovering eyes.

The bridge runs silently in the background, I forget it exists, and it just works every time I save a prompt.
