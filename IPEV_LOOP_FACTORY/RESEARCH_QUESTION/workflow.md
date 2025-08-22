The workflow is based on the IPEV Loop Framework.
First, the IPEV Loop toolkit is required, which consists of two parts:

1. The IPEV Loop Paper
2. The prompt factory that follows the IPEV Loop Framework

The process begins by introducing an LLM—ChatGPT, Claude, or Gemini—to the IPEV Loop Framework, allowing it to study the framework thoroughly and informing it that the framework will be applied to a specific project.

After the study phase, a problem statement is provided. The LLM then uses the IPEV Loop prompt factory to generate a prompt in the correct format.

That prompt becomes the input to GCLI, often named `mission.md`.

In the terminal, navigate to the repository and start GCLI with:

```
gemini -m "gemini-2.5-pro" -y
```

The `-y` flag stands for "yolo" mode, which allows automatic approval.

Inside GCLI, enter:

```
Read @mission.md and follow its instructions.
```

From this point, the process runs automatically.

Sample materials from IPEV Loop V10 and V21 can be found in the attachments: `v10.txt` and `v21.txt`.
