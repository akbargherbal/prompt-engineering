Here is the complete, user-ready Markdown content for "The Evidence Locker" worksheet.

***

# Step 2: The Evidence Locker

Welcome to the second phase of your "Mise en Place." In the **Pain Journal**, you articulated the *what* and the *why* of your problem. Now, in **The Evidence Locker**, we'll gather the *how*.

For an LLM to act as a world-class systems simulator, it needs the same context a senior developer would demand before tackling a problem. It can't see your screen, access your codebase, or read your logs. We must meticulously collect and present this "evidence." Think of yourself as a detective building a case file. Every artifact you gather here helps the LLM build a high-fidelity mental model of your system, which is the absolute key to a successful simulation.

---

### 2.1 The Code: Your System's DNA

First, let's gather the code. The code contains the explicit logic, the functions, and the "rules of physics" for your specific system. Providing the right snippets is the most direct way to show the LLM *how* your application is designed to behave. We don't need the whole application, just the pieces directly related to the pain point.

**What are the most relevant code snippets (functions, classes, methods) that are directly involved in the process you're trying to simulate or fix?**
*Focus on the code that 'touches' the pain point you identified in your Pain Journal.*

> _Example: The `process_log_file(file_path)` function that opens a file, reads it line by line, and attempts to parse a JSON object from each line. It also contains the `try...except` block where the error occurs._
>
> ```python
> def process_log_file(file_path):
>     with open(file_path, 'r') as f:
>         for i, line in enumerate(f):
>             try:
>                 data = json.loads(line)
>                 # ... further processing ...
>             except json.JSONDecodeError as e:
>                 print(f"Error on line {i}: {e}")
>                 # ... error handling logic ...
> ```
>
> **[Paste your relevant code snippets here. Use Markdown for formatting.]**

**How is this code invoked? What are the key function signatures, API endpoints, or command-line arguments that trigger this process?**
*This helps the simulator understand the entry point and the initial state of the system.*

> _Example: The script is run from the command line like this: `python process_logs.py --source s3://my-log-bucket/2023-10-26/`. The `main()` function uses `argparse` to handle the arguments and then calls `process_log_file()` for each file found._
>
> **[Describe the entry point and invocation method here.]**

---

### 2.2 The Data & Logs: Eyewitness Testimony

If your code is the system's DNA, then your data and logs are the eyewitness accounts. They show what *actually happened* when the code was executed. This includes the inputs that caused the problem and the outputs (or errors) that resulted. This is often the most critical evidence you can provide.

**What does a small, representative sample of the INPUT data look like?**
*If it's structured (like JSON or CSV), include the schema or headers if possible.*

> _Example: A single valid line from an input log file might be `{"timestamp": "2023-10-26T10:00:05Z", "level": "INFO", "user_id": "abc-123", "event": "login_success"}`. A line that causes an error might be truncated or have malformed JSON, like `{"timestamp": "2023-10-26T10:00:06Z", "level": "ERROR",`._
>
> **[Paste a sample of your input data here.]**

**What do the logs or error messages look like when the process fails?**
*Provide the full traceback if available. This is a roadmap that points directly to the scene of the crime.*

> _Example: The console output shows a clear decoding error and traceback._
>
> ```
> ERROR:root:Failed to process line 1138 in file_x.log.
> Traceback (most recent call last):
>   File "process_logs.py", line 42, in process_log_file
>     data = json.loads(line)
>   File "/usr/lib/python3.9/json/__init__.py", line 346, in loads
>     return _default_decoder.decode(s)
>   File "/usr/lib/python3.9/json/decoder.py", line 337, in decode
>     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
> json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
> ```
>
> **[Paste your error logs and tracebacks here.]**

**Can you provide a clear example of a "good" input that processes correctly AND a "bad" input that causes the failure?**
*This contrast is extremely valuable for the LLM. It allows it to pattern-match the difference between success and failure.*

> _Example:_
> *   _**Good Input:** `{"id": 1, "status": "complete", "payload": {"value": 100}}`_
> *   _**Bad Input:** `{"id": 2, "status": "` (truncated file causes invalid JSON)_
>
> **[Provide your 'good' vs. 'bad' input examples here.]**

---

### 2.3 The Environment: The Scene of the Crime

Code doesn't run in a vacuum. The environment—its libraries, OS, cloud services, and configurations—can fundamentally change behavior. This information helps the LLM understand external factors and constraints that aren't visible in the code itself.

**What is the execution environment?**
*Include the programming language version, key libraries and their versions, and the operating system or container base image.*

> _Example: Python 3.9.12, running in a Docker container based on `python:3.9-slim-buster`. Key libraries: `boto3==1.26.0`, `pandas==1.5.3`._
>
> **[Describe your runtime environment and key dependencies here.]**

**What is the high-level system architecture?**
*Where does this code run, and what external services does it interact with? (e.g., AWS Lambda, a specific database, a third-party API, a local file system).*

> _Example: The Python script is deployed as an AWS Lambda function. It's triggered by an S3 "Object Created" event. It reads the new file from the trigger bucket (`raw-logs`) and, on success, writes a summary file to a different bucket (`processed-summaries`)._
>
> **[Describe the system architecture and external interactions here.]**

**Are there any important configuration settings, environment variables, or resource limits?**
*Think about things like timeouts, memory limits, API keys (names only, not secrets!), or feature flags that could affect the process.*

> _Example: The Lambda function has a 128MB memory limit and a 30-second execution timeout. It uses an environment variable `TARGET_BUCKET=processed-summaries`._
>
> **[List relevant configuration, environment variables, or resource limits here.]**