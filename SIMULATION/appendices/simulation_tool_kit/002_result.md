### Step 2: The Evidence Locker

##### Gather the Raw Materials for Your Simulation

Welcome to the second phase of your "Mise en Place." In the _Pain Journal_, you articulated the problem in your own words. Now, it’s time to gather the actual evidence. Think of the LLM as a brilliant consultant who has been teleported into your project but is completely blindfolded. They can’t see your screen, your files, or your terminal. The Evidence Locker is where you meticulously collect and label every piece of code, data, and log file they need to "see" your system. By providing this high-fidelity context, you enable the LLM to build an accurate mental model, which is the foundation of any successful simulation.

---

##### 2.1 The Code at the Scene

**Why this is important:** The code is the central actor in our drama. For the LLM to understand the system's behavior, it must first understand the logic, structure, and intent of the primary script or functions involved. This isn't just about finding a bug; it's about understanding the entire process the code is trying to execute.

**Your Task:**
Can you paste the most relevant code snippet(s) that are at the heart of the manual process? Include the main function, class, or script that you have to run or interact with. Don't worry about it being perfect; the raw material is what matters.

> _Example: A Python script that iterates through a directory of log files, uses regex to find lines containing 'ERROR', and writes them to a new file._
>
> ```python
> import os
> import re
>
> def process_log_files(source_dir, output_file):
>     error_pattern = re.compile(r".*ERROR: Task failed for prompt_id: (\w+)")
>     failed_prompts = []
>
>     with open(output_file, 'w') as out_f:
>         for filename in os.listdir(source_dir):
>             if filename.endswith(".log"):
>                 with open(os.path.join(source_dir, filename), 'r') as log_f:
>                     for line in log_f:
>                         match = error_pattern.search(line)
>                         if match:
>                             prompt_id = match.group(1)
>                             out_f.write(f"{prompt_id}\n")
>                             failed_prompts.append(prompt_id)
>     print(f"Found {len(failed_prompts)} failed prompts.")
> ```

> **(Paste your core code here.)**
>
> ```
>
> ```

---

##### 2.2 Inputs and Outputs: The Data's Journey

**Why this is important:** Code doesn't exist in a vacuum; it transforms data. The LLM needs to see the "before" and "after" picture. Providing samples of your input files (the raw material) and the current output files (the flawed result) gives the simulation a clear start and end point. This helps the LLM understand the _shape_ of your data and the _nature_ of the current failure.

**Your Tasks:**

1.  What does a typical input look like? This could be a few lines from a log file, a sample row from a CSV, or a JSON object from an API call.

    > _Example: A few representative lines from one of the `production_app-2023-10-26.log` files._
    >
    > ```log
    > 2023-10-26 14:22:01,123 INFO: Task started for prompt_id: abc-123
    > 2023-10-26 14:22:02,456 DEBUG: Processing data chunk 1 of 5
    > 2023-10-26 14:22:03,789 ERROR: Task failed for prompt_id: def-456 due to upstream timeout.
    > 2023-10-26 14:22:05,123 INFO: Task completed for prompt_id: ghi-789
    > ```

    > **(Paste your input data sample here.)**
    >
    > ```
    >
    > ```

2.  What does the current, problematic output look like? This could be a manually created file, an incomplete report, or simply an error message printed to the console.

    > _Example: The contents of the `manually_extracted_failures.txt` file I have to create each time._
    >
    > ```text
    > def-456
    > jkl-012
    > mno-345
    > ```

    > **(Paste your current output sample here.)**
    >
    > ```
    >
    > ```

---

##### 2.3 The Environment: The Laws of Physics

**Why this is important:** A script that works on your MacBook might fail inside a Docker container. The execution environment defines the "laws of physics" for your code. The LLM needs to know about the operating system, critical dependencies, and any containerization. This prevents it from suggesting a solution that is impossible in your specific context (e.g., using a library you don't have installed).

**Your Tasks:**

1.  How and where is this code executed? Describe the environment.

    > _Example: The script is run manually on my local machine (macOS Sonoma). I have Python 3.11 installed via Homebrew. The log files are pulled from an S3 bucket into a local `./logs` directory before running._

    > **(Describe your execution environment here.)**

2.  What are the key libraries or dependencies? If you have a `requirements.txt`, `package.json`, or `pom.xml`, listing the most relevant packages is perfect.

    > _Example: This is a simple script with no external libraries, just the standard `os` and `re` modules that come with Python._
    >
    > _Alternate Example: Key dependencies from requirements.txt are `pandas==2.1.1`, `boto3==1.28.77`, `requests==2.31.0`._

    > **(List your key dependencies here.)**

---

##### 2.4 The Paper Trail: Logs and Error Messages

**Why this is important:** If your code is the actor and the data is the plot, then logs and errors are the narrator, telling you exactly what went wrong and where. These are the most direct clues you can give the LLM. A full stack trace or a verbose error log is a goldmine of information that allows the simulation to pinpoint the root cause of the system's failure.

**Your Task:**
Can you capture the exact output, including any stack traces or error messages, that you see when the process fails or behaves incorrectly?

> _Example: When I accidentally point the script to a malformed log file, it doesn't fail gracefully. It just stops and produces an empty output file with no error message. The *lack* of an error IS the evidence._
>
> _Alternate Example: If a file is locked, I get the following Python stack trace:_
>
> ```traceback
> Traceback (most recent call last):
>   File "process_logs.py", line 18, in <module>
>     process_log_files("./logs", "failures.txt")
>   File "process_logs.py", line 11, in process_log_files
>     with open(os.path.join(source_dir, filename), 'r') as log_f:
> PermissionError: [Errno 13] Permission denied: './logs/production_app-2023-10-26.log'
> ```

> **(Paste your relevant logs and error messages here.)**
>
> ```
>
> ```

---

**Locker Secured.** You have now gathered all the physical evidence. The scene is set, and the key artifacts are tagged and ready for inspection. In the next worksheet, **The Rulebook**, we will define the rules of the game—establishing the constraints, goals, and success criteria for our simulation.