

# **Adapting IDE-Native AI Pedagogy for the Command Line: A Practical Implementation Framework for Gemini CLI**

## **Executive Summary**

The proliferation of IDE-native AI assistants has catalyzed a paradigm shift in programming education, moving from rote memorization of syntax to a collaborative, context-aware learning model. The "IDE-Native AI for Accelerated Programming Education" methodology, detailed in "The Frictionless Code" report, exemplifies this shift by leveraging a multi-agent system within the Integrated Development Environment (IDE) to provide a seamless, scaffolded learning experience. However, a significant portion of professional software development and a growing segment of programming education occur within the terminal, or Command-Line Interface (CLI). This environment, prized for its power and efficiency, traditionally lacks the rich, persistent context and real-time awareness of an IDE, posing a significant challenge to adapting modern AI-driven pedagogy.

This report presents an exhaustive investigation into practical implementation strategies for adapting this advanced educational methodology to Google's Gemini CLI tool. The central finding is that a terminal-based workflow can achieve educational effectiveness equivalent to its IDE counterpart, not by mimicking the IDE's graphical interface, but by replicating its core pedagogical functions through a multi-layered architecture of emerging technologies and structured interaction patterns.

The recommended solution architecture is composed of three primary pillars:

1. **Real-Time State Synchronization via the Model Context Protocol (MCP):** MCP serves as the foundational technology to create an educational "shared-view," enabling both the student's IDE and the terminal-based Gemini CLI to access and reason over the same workspace state. The integration of Filesystem, Git, and particularly Language Server Protocol (LSP) based MCP servers allows the AI to achieve a deep, semantic understanding of the student's code, mirroring the contextual awareness of an IDE-native tool.  
2. **Multi-Agent Orchestration with LangGraph:** The report's conceptual Planner-Executor-Tutor model can be practically implemented in a terminal environment using a stateful, graph-based framework like LangGraph. This allows for the creation of a robust learning loop where a Planner agent collaborates with the student to define tasks, an Executor agent attempts implementation, and a Tutor agent provides Socratic guidance upon failure, computationally operationalizing proven pedagogical theories like Vygotsky's Zone of Proximal Development.  
3. **Persistent Memory and Learning Analytics:** Persistent context, crucial for tracking learning progress, can be achieved through a two-tiered memory system. Project-specific GEMINI.md files serve as the AI's long-term, declarative memory for pedagogical rules, while conversational checkpointing commands provide a mechanism for saving and resuming the short-term, episodic memory of a learning session. Furthermore, by adapting established terminal monitoring techniques, a custom analytics wrapper can be developed to capture quantitative "Learning Velocity" metrics, such as time-to-milestone and intervention rates, providing objective measures of student progress.

Ultimately, this report concludes that the transition from IDE to CLI does not necessitate a loss of pedagogical fidelity. By leveraging the agentic capabilities of modern CLI tools like Gemini, adhering to structured interaction cycles such as "Plan-Act-Review-Repeat," and integrating a robust technical backend with MCP and LangGraph, it is possible to construct a powerful, effective, and accelerated programming education workflow entirely within the terminal.

## **I. Replicating IDE-Native Educational Workflows in the Terminal**

The foundational challenge in adapting the IDE-native methodology lies in translating the interactive, visually integrated learning experience of an IDE to the text-based, command-driven terminal. A successful adaptation hinges not on recreating the IDE's user interface, but on replicating its core pedagogical functions: providing contextual assistance, scaffolding complex tasks, and facilitating a structured learning process. This requires leveraging established workflow patterns of modern agentic CLI tools and framing them within a robust pedagogical cycle.

### **1.1. Analysis of Established AI-Assisted Terminal Workflow Patterns**

The landscape of AI-powered command-line tools has undergone a significant evolution. Initial tools were primarily command generators, translating natural language into shell commands.1 The current state-of-the-art, however, embodies a "pair programmer" or "pair engineer" paradigm, where the AI acts as a conversational agent capable of understanding project context, executing multi-step tasks, and collaborating with the developer directly in their terminal environment.2 This agentic shift is fundamental to enabling a rich educational workflow, with several distinct patterns emerging from leading tools.

* **Git-Native Workflows:** Tools like **Aider** exemplify a workflow deeply integrated with version control. The typical interaction involves the user adding relevant project files to the AI's chat context, describing a desired change in natural language, and then Aider generates the necessary code modifications and automatically creates a Git commit.2 This pattern is exceptionally valuable from an educational standpoint as it inherently reinforces professional software engineering best practices. Students learn to think in terms of small, logical changes, articulate their intent clearly for each change, and maintain a clean version history—skills that are crucial in collaborative development environments.6  
* **Conversational & Vibe-Based Workflows:** **Claude Code** promotes a more fluid, conversational interaction style often referred to as "vibe coding".4 In this model, the developer dictates high-level goals or concepts, and the agent iterates on the implementation through a dialogue. For a student, this workflow is powerful for the initial stages of a project, such as brainstorming and rapid prototyping. It teaches the critical skill of translating abstract requirements into concrete technical plans and encourages an exploratory, iterative approach to problem-solving. The emphasis is less on precise commands and more on collaborative refinement of an idea.7  
* **Tool-Centric Workflows:** Tools such as **Gemini CLI** and the **Warp** terminal are designed around the agent's ability to orchestrate a suite of built-in and extensible tools—including file system operations, web search, and shell command execution—to accomplish complex tasks.8 This workflow teaches students a modular approach to problem-solving. They learn to decompose a large goal into smaller sub-tasks and identify the appropriate tool for each step. This mirrors how experienced developers work, leveraging a combination of utilities to build, debug, and deploy software.

These patterns are not mutually exclusive but represent different facets of the modern AI-assisted terminal experience. A comprehensive educational methodology for Gemini CLI should draw upon all three: using a conversational, tool-centric approach to develop solutions that are then committed and managed through a Git-native lens.

### **1.2. The "Plan-Act-Review-Repeat" Cycle as a Pedagogical Framework**

The most effective AI-assisted development follows a structured, iterative cycle: Plan → Act → Review → Repeat.11 This professional workflow provides a powerful and robust pedagogical framework for programming education in the terminal, shifting the focus from mere code generation to a deliberate process of critical thinking and refinement.

* **The Planning Phase:** This initial stage involves keeping the AI agent in a "discussion mode," where it formulates a comprehensive strategy without executing any code.7 For a student, this phase is paramount. It compels them to articulate their intent clearly, define the problem's scope and constraints, and think critically about the solution's architecture  
  *before* writing a single line of code. This deliberate planning step helps prevent the common novice pitfall of jumping directly into implementation without a clear strategy, leading to more robust and well-structured solutions. Tools like Claude Code's "Plan Mode" explicitly enforce this separation, creating a safe, read-only environment for strategic formulation.7  
* **The Acting Phase:** Once the plan is approved by the student, the AI agent executes it, making file edits, running commands, and generating code.11 This phase acts as a powerful scaffolding mechanism. The student observes how their high-level, abstract plan is translated into low-level, concrete implementation details. This direct connection between intent and execution provides a tangible learning experience, demystifying complex coding tasks and demonstrating how architectural decisions manifest in the codebase.  
* **The Reviewing Phase:** After the agent has acted, the student must engage in a thorough review of the generated output. This is arguably the most crucial phase for learning. The student is not a passive recipient of code; they are an active critic responsible for validating its correctness, quality, and alignment with the original plan.11 This process fosters essential skills in critical thinking, code comprehension, debugging, and quality assurance. The central pedagogical principle of this phase is the professional maxim: "Never commit code you don't understand".11

### **1.3. Adaptation for Gemini CLI**

Google's Gemini CLI is architecturally well-suited to support this pedagogical cycle. Its core operation is based on a **Reason and Act (ReAct) loop**, where the model first reasons about a problem to create a plan and then acts on that plan using its available tools.13 This internal process can be surfaced and controlled by the user through structured prompting.

A GEMINI.md file can be configured to enforce a planning-first approach, instructing the agent to always present a plan for approval before making any file modifications.15 Furthermore, Gemini CLI's support for

**custom slash commands** allows for the creation of explicit modes. For example, an educator could define a /plan "my task" command that instructs the AI to only generate a plan, and an /implement command that tells it to execute the previously approved plan, thus creating a structured, gated workflow for the student.17

The rise of such agentic CLI tools and structured workflows represents a profound pedagogical opportunity. The learning process is elevated from the mastery of syntax (the "how") to the mastery of intent and structure (the "what" and "why"). Traditionally, programming education has focused heavily on teaching students the precise syntax, keywords, and library functions required to perform a task. Agentic tools abstract away much of this low-level implementation; a student can express a high-level goal like "refactor this function to handle edge cases" instead of manually writing the conditional logic.2 This abstraction shifts the student's role from that of a "coder" to that of a "director" or "architect." Their primary cognitive load is no longer on recalling syntax but on the higher-order skills of problem decomposition, clear communication of intent (i.e., prompt engineering), and the critical evaluation of the agent's output. The terminal, therefore, transforms from a simple execution environment into a Socratic dialogue space, where learning is driven by planning, collaboration, and critical review.

| Feature / Tool | Aider | Claude Code | Gemini CLI | Warp | Continue CLI |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Core Interaction Model** | Git-native, conversational. Edits are automatically committed. | Conversational, REPL-like "vibe coding." Focus on iteration. | Tool-centric, conversational. Uses a ReAct loop to reason and act. | Agentic terminal environment. Manages multiple parallel agents. | IDE-class editing in the terminal with slash commands. |
| **Context Handling** | User-manually adds files to chat (/add). Uses ctags for repository mapping. | Full codebase awareness. Maintains context across sessions. | 1M token context window. Project-level context via GEMINI.md. | Context from multi-repo codebases, MCP servers, and rules. | IDE-native context indexing and Retrieval-Augmented Generation (RAG). |
| **Agentic Capabilities** | Multi-file edits, auto-commits, linting, and test execution. | Multi-step tasks, file edits, command execution, bug fixing. | Multi-step tasks, file manipulation, shell execution, web search. | Parallel agent execution, code generation, debugging, PR creation. | Asynchronous workflows, code generation, refactoring. |
| **Customization** | Model selection (OpenAI, Anthropic, local). | Model selection via Claude Bridge. Custom prompts and workflows. | Custom system prompts (GEMINI.md), custom slash commands, MCP extensions. | Configurable agent autonomy, custom rules, and MCP integration. | Custom models, custom rules, and MCP integration. |
| **Pricing Model** | Pay-per-token (BYO API key). | Pay-per-token (Anthropic API). Can be expensive. | Generous free tier for individuals. Usage-based for enterprise. | Freemium model with Enterprise plans available. | Open source, pay-per-token (BYO API key). |
| **Open Source** | Yes | No | Yes | No | Yes |

## **II. Achieving Real-Time State Synchronization Between IDE and CLI**

To replicate the "shared-view" educational experience—where the AI mentor possesses the same level of contextual awareness as an IDE-native tool—a robust mechanism for real-time state synchronization is required. This section details the critical technology that enables this bridge: the Model Context Protocol (MCP). It provides a technical deep dive into the protocol's architecture and identifies the key server implementations necessary to endow a terminal-based agent like Gemini CLI with full workspace awareness.

### **2.1. Technical Deep Dive: The Model Context Protocol (MCP) Architecture**

The Model Context Protocol (MCP) is an open standard designed to solve the problem of AI context fragmentation. It provides a standardized way for Large Language Model (LLM) applications to connect with and utilize external data sources and tools, functioning as a "universal remote" for AI.18 Instead of building bespoke integrations for every combination of AI model and external service, developers can use MCP to create a plug-and-play ecosystem.

The protocol's architecture is inspired by the highly successful Language Server Protocol (LSP) and is based on a client-server model 18:

* **MCP Client:** This component is integrated within the host application, such as an IDE (VS Code, Visual Studio) or a CLI tool (Gemini CLI). Its responsibility is to manage connections to MCP servers and translate the AI's needs into standardized protocol messages.18  
* **MCP Server:** This is a standalone process that exposes a specific functionality or data source as a set of "tools" that the MCP client can discover and invoke. Each server is typically focused on a single integration, such as interacting with a Git repository, a PostgreSQL database, or the local filesystem.18  
* **Transport Layer:** Communication between the client and server is handled by a transport layer. MCP supports two primary methods: stdio (standard input/output) for local integrations where the server runs as a subprocess, and HTTP+SSE (Server-Sent Events) for connecting to remote servers. All messages conform to the JSON-RPC 2.0 standard, ensuring a consistent and well-defined communication structure.18

### **2.2. Key MCP Servers for Creating a "Shared-View"**

To construct a true "shared-view" where the terminal-based AI has parity with an IDE, a combination of MCP servers is necessary. Each server provides a different layer of contextual understanding.

* **Filesystem Server:** This is the most fundamental component for workspace awareness. The official reference implementation of the Filesystem server provides the AI agent with secure, configurable access to read, write, and edit local files.22 By configuring this server to point to the student's project directory, the Gemini CLI agent can "see" the project's file structure, read source code, and propose changes, directly mirroring the file access an IDE possesses.  
* **Git Server:** The reference Git server exposes tools to read, search, and manipulate Git repositories.22 This is crucial for educational workflows that emphasize version control. It allows the AI tutor to understand the project's history, view pending changes (diffs), and analyze different branches, aligning its context with the dynamic state of the student's work.  
* **Language Server Protocol (LSP) Server:** This is the most advanced and critical component for achieving a deep, semantic "shared-view." An LSP-MCP server, such as the community-driven lsp-mcp project, acts as a bridge, exposing the powerful capabilities of a language server (e.g., gopls for Go, pyright-langserver for Python) as MCP tools for the AI.26 This elevates the AI's understanding from raw text to a structured, semantic model of the code. Instead of simple text search, the AI can now use tools for:  
  * **definition:** To find the precise location where a function or variable is defined.  
  * **references:** To locate all usages of a symbol throughout the codebase.  
  * **diagnostics:** To identify syntax errors and code quality warnings.  
  * **hover:** To retrieve documentation and type hints for a piece of code.

The ability to reason about the code's meaning, not just its text, is the true essence of the "shared-view" concept. It transforms the AI from a text-processor into a knowledgeable collaborator that understands the code's structure and logic, just like the IDE itself.

### **2.3. Implementation Patterns for IDE-CLI Synchronization**

The synchronization between the student's IDE and the Gemini CLI in the integrated terminal is achieved by configuring both environments to communicate with the same set of MCP servers.

* **Native IDE and CLI Support for MCP:** Modern development environments, including VS Code and Visual Studio, now ship with native MCP client support.20 Developers can install and manage MCP servers through the IDE's interface or by editing a configuration file (e.g.,  
  .vscode/mcp.json). Concurrently, Gemini CLI is also a first-class MCP client, configurable via its own settings file (\~/.gemini/settings.json).8  
* **The "Shared-View" Bridge:** The bridge is formed when both the IDE and the Gemini CLI process are pointed to the same server instances. For example, a single Filesystem MCP server process running locally can be registered in both the VS Code configuration and the Gemini CLI configuration. This ensures that when the student edits a file in the IDE and then asks a question in the terminal, the AI sees the most up-to-date version of the file because both clients are querying the same source of truth.  
* **Gemini CLI \+ VS Code Companion Extension:** Recognizing the power of this integration, Google has released a dedicated companion extension for VS Code that deepens this synergy.33 When Gemini CLI is run from within the VS Code integrated terminal, this extension allows it to become aware of which files are currently open and what text is selected. Furthermore, it enables Gemini CLI to trigger native in-editor diff views, allowing the student to review and even modify the AI's proposed changes in a rich, graphical interface before applying them. This provides a seamless and powerful implementation of the "shared-view" concept, blending the power of the CLI with the user-friendliness of the IDE.

The LSP-MCP server acts as a "Rosetta Stone," translating between the human-centric, semantic view of an IDE and the agent-centric, tool-based view of a CLI. The methodology outlined in "The Frictionless Code" depends on the AI having real-time, deep workspace awareness. A naive approach might involve simply reading file contents into the AI's context window, which is inefficient and lacks the structural understanding an IDE provides. MCP offers the protocol for sharing this context, and a Filesystem server provides the raw file data. However, the true power of an IDE lies in its semantic comprehension, which is powered by a Language Server (LSP). The lsp-mcp project bridges these two worlds by wrapping an LSP server and exposing its semantic functions as MCP tools. Consequently, when Gemini CLI utilizes this server, it can ask "find all references to the calculate\_total() function" instead of merely performing a text search for the string "calculate\_total". This represents a monumental leap in contextual understanding. The "shared-view" is thus not just about the student and the AI looking at the same screen of text; it is about them sharing the same underlying semantic graph of the code, enabling high-level collaboration on architecture and logic, which is the core goal of the educational methodology.

| Server Name | Core Functionality | Contribution to "Shared-View" | Example Educational Use Case | Implementation Status |
| :---- | :---- | :---- | :---- | :---- |
| **Filesystem** | Provides secure, configurable access to read, write, and edit local files and directories. | **Fundamental Workspace Awareness:** Allows the AI to see the project's file structure and content, mirroring the IDE's file explorer. | The student asks, "Where is the configuration for the database connection?" The AI uses the read\_directory and read\_file tools to locate and display the relevant config file. | Reference 22 |
| **Git** | Exposes tools to read, search, and manipulate Git repositories (e.g., view diffs, list branches, check history). | **Project State Awareness:** Enables the AI to understand the version control state, including pending changes and historical context. | The AI tutor reviews a student's proposed changes and states, "I see in the diff that you removed the error handling. Can you explain your reasoning for that?" | Reference 22 |
| **LSP-mcp** | Bridges the Language Server Protocol (LSP) to MCP, exposing semantic code analysis tools. | **Deep Semantic Awareness:** Provides the AI with IDE-level understanding of code (definitions, references, diagnostics, types). | A student's code has a subtle type mismatch error. The AI uses the diagnostics tool to identify the error and the hover tool to explain the expected vs. actual types. | Community 26 |
| **PostgreSQL** | Allows for read-only interaction with PostgreSQL databases, including schema inspection and query execution. | **Data Layer Awareness:** Gives the AI context about the application's database schema and state. | The student is writing a data access layer. The AI tutor can use the get\_schema tool to provide context-aware suggestions that match the actual database table structure. | Archived Reference 22 |
| **Web Search** | Provides tools to perform web searches and fetch content from URLs. | **External Knowledge Awareness:** Allows the AI to look up documentation, error messages, or examples from the web. | The student encounters an obscure library error. The AI uses the web\_search tool to find a Stack Overflow post explaining the issue and then guides the student to a solution. | Official (Brave, Tavily) 22 |

## **III. Implementing Multi-Agent Orchestration in a Terminal Environment**

The "Frictionless Code" report's conceptual Planner-Executor-Tutor model provides a sophisticated framework for educational interaction. To translate this model into a functional terminal-based system, a robust multi-agent orchestration framework is required. This section explores how to map the conceptual model to concrete, terminal-friendly frameworks, providing a practical blueprint for structuring the interaction between the student and a team of specialized AI agents.

### **3.1. Mapping the Planner-Executor-Tutor Model to Agentic Frameworks**

The proposed educational model consists of a three-agent system, each with a distinct role:

* **The Planner:** This agent collaborates with the student at a high level. It takes a broad goal (e.g., "add authentication to the web app") and decomposes it into a logical, sequential plan of smaller, executable steps. Its role is strategic, focusing on problem decomposition and architectural thinking.  
* **The Executor:** This agent is a tactical specialist. It receives a single, well-defined step from the plan (e.g., "create a new file for the login component") and attempts to implement it by writing code, modifying files, or running commands.  
* **The Tutor:** This agent serves as the pedagogical safety net. It is invoked when the Executor fails to complete a task or when the student is demonstrably struggling. Its purpose is not to solve the problem but to provide Socratic guidance—asking probing questions, explaining underlying concepts, or offering hints—to help the student overcome the obstacle themselves.

To implement this model, an orchestration framework must support three key features: **state management** (to pass the plan, code, and feedback between agents), **conditional routing** (to decide whether to proceed to the next step, invoke the tutor, or finish), and **cycles** (to allow for repeated attempts at a task after receiving tutoring).

### **3.2. Comparative Analysis of Orchestration Tools**

Several open-source frameworks exist for building multi-agent systems, each with different strengths and abstractions.

* **LangGraph:** An extension of the popular LangChain library, LangGraph is specifically designed for creating stateful, multi-agent applications that may contain cycles.35 It represents workflows as graphs, where nodes are agents (or simple functions) and edges define the control flow. Its explicit state management, support for conditional edges, and built-in memory make it an exceptionally strong fit for the Planner-Executor-Tutor model, which is inherently cyclical and state-dependent.37 It is considered a lower-level framework, offering developers a high degree of control over the agentic architecture.36  
* **AutoGen (Microsoft):** This framework is designed for building multi-agent systems that collaborate through conversation.39 It frames interactions as a "conversation" between different agent personas. While powerful for simulating collaborative environments, its conversational abstraction can make it less intuitive to define the rigid, state-based transitions and explicit failure-recovery loops required by the Planner-Executor-Tutor model compared to LangGraph's more explicit graph-based approach.36  
* **CrewAI:** CrewAI is a higher-level framework focused on orchestrating autonomous agents assigned to specific roles and goals within a "crew".39 It simplifies the process of defining these agent teams but, as a higher-level abstraction, offers less granular control over the intricate state transitions and conditional logic needed for the pedagogical feedback loop, making LangGraph a more suitable choice for this specific, highly controlled workflow.36  
* **CAMEL:** A research-oriented framework designed for the large-scale simulation of up to one million agents to study emergent social behaviors and scaling laws.43 Its focus on massive-scale simulation and data generation makes it less ideal for building a controlled, single-user educational application, which requires precise orchestration rather than emergent behavior.

Based on this analysis, LangGraph emerges as the most suitable framework due to its explicit support for stateful, cyclical graphs, which directly map to the requirements of the Planner-Executor-Tutor learning loop.

| Framework | Core Abstraction | State Management | Support for Cycles | Controllability | Suitability for Planner-Executor-Tutor Model |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **LangGraph** | State Machine / Graph | Explicit, centralized state object | Native support via conditional edges | High (low-level primitives) | **Excellent:** Directly models the required state transitions, feedback loops, and conditional logic. |
| **AutoGen** | Conversation | Implicit, managed through conversation history | Possible, but less explicit | Medium (conversation-driven) | **Good:** Can simulate the roles, but the control flow is less direct than a graph model. |
| **CrewAI** | Agent Crew / Team | Managed within the framework | Limited (more sequential/delegative) | Low (high-level framework) | **Fair:** Good for defining roles, but less suited for the specific pedagogical feedback cycle. |
| **CAMEL** | Agent Society | Stateful agents in a simulated environment | Yes, for simulation | Medium (focused on simulation rules) | **Poor:** Designed for large-scale simulation, not controlled, single-user application workflows. |

### **3.3. A Practical Blueprint using LangGraph and Gemini**

A complete terminal-based educational system can be implemented as a Python script that uses LangGraph to orchestrate interactions with the Gemini API or Gemini CLI.

1. **Define the State:** The first step is to define a shared state object using Python's TypedDict. This object will be passed between all nodes in the graph and will track the entire learning process.38  
   Python  
   class EducationalWorkflowState(TypedDict):  
       student\_goal: str  
       plan: List\[str\]  
       executed\_steps: List\[dict\]  
       current\_task\_index: int  
       task\_output: str  
       task\_success: bool  
       tutor\_feedback: str  
       student\_metrics: dict

2. **Define the Nodes (Agents):** Each agent is implemented as a Python function that takes the current state as input and returns a dictionary of updates to the state.  
   * **planner\_node:** This function is the entry point. It takes the student\_goal from the state and makes a call to the Gemini model with a carefully crafted prompt to generate a structured plan. It then updates the plan field in the state.  
   * **executor\_node:** This function takes the task at the current\_task\_index from the plan. It invokes the Gemini CLI in a subprocess (or uses the Gemini API's tool-calling features) to execute the task.13 It captures the output and success/failure status, updating  
     task\_output and task\_success.  
   * **tutor\_node:** This function is called on failure. It takes the failed task and its output from the state and calls the Gemini model with a pedagogical prompt (e.g., "You are a Socratic tutor. The student's code failed with this error. Ask a question to guide them to the solution."). It updates the tutor\_feedback field.  
3. **Define the Edges (Control Flow):** The logic of the workflow is defined by the edges connecting the nodes.  
   * The graph's entry point is the planner\_node.  
   * After the planner, a regular edge transitions to the executor\_node.  
   * A **conditional edge** after the executor\_node is the core of the learning loop. It inspects the task\_success field in the state:  
     * If True and there are more tasks in the plan, it loops back to the executor\_node for the next task.  
     * If True and the plan is complete, it transitions to the END of the graph.  
     * If False, it transitions to the tutor\_node.  
   * After the tutor\_node provides feedback, an edge routes back to the executor\_node, allowing the student to retry the same task, now equipped with the tutor's guidance. This creates the essential learning cycle.

This entire architecture can be encapsulated in a single, runnable Python script, providing a powerful and extensible terminal-based tutoring system.38

The Planner-Executor-Tutor model is more than just a clever agent architecture; it is a computational representation of a cornerstone of educational psychology: Lev Vygotsky's theory of the **Zone of Proximal Development (ZPD)**. The ZPD defines the conceptual space where a learner can perform a task with guidance that they cannot yet perform independently. The multi-agent system operationalizes this theory. The Planner helps the student structure their thinking, preparing them to enter the ZPD. The Executor attempts the task, effectively probing the boundary of the student's current ability. When the Executor fails, it signals that the task lies outside the student's independent capabilities but within their ZPD. At this critical juncture, the Tutor intervenes, providing the targeted "scaffolding" — the Vygotskian concept of a "More Knowledgeable Other" — through hints and guiding questions. The cyclical nature of the LangGraph implementation, which allows for repeated, scaffolded attempts (Executor \-\> Tutor \-\> Executor), enables the student to traverse the ZPD and master the skill. By implementing this system, the methodology moves beyond simple AI assistance to create a terminal-based environment that is grounded in and actively facilitates a proven pedagogical theory.

## **IV. Strategies for Persistent Context and Memory in CLI Tools**

A defining feature of modern IDEs is their inherent statefulness; they maintain a persistent understanding of the project's context across work sessions. Replicating this in the traditionally stateless command-line environment is critical for building an effective educational tool that can track progress and maintain consistency over time. This section details practical strategies for implementing persistent context and memory in Gemini CLI, providing functional alternatives to IDE-native configuration files like .clinerules.

### **4.1. Modern Approaches to CLI Context Management**

The stateless nature of traditional CLI tools presents a significant usability challenge for AI agents. Each invocation is isolated, forcing the user to repeatedly supply the same context, which is inefficient and leads to high token consumption.47 Modern agentic CLIs address this through several layers of context management.

* **Project-Level Context Files (GEMINI.md):** The most powerful pattern for establishing persistent, long-term context is the use of a dedicated markdown file within the root of a project directory. Gemini CLI has native support for a file named GEMINI.md.8 This file acts as a "constitution" or a permanent system prompt for the AI agent. It is automatically loaded into the context for every interaction within that project, allowing developers to define a consistent persona, enforce coding standards, outline architectural principles, and provide project-specific rules and constraints.16  
* **Modular Context with Imports:** To prevent the GEMINI.md file from becoming monolithic and unmanageable, Gemini CLI supports a simple import syntax. A line like @./docs/style-guide.md within the main GEMINI.md will cause the contents of the specified file to be loaded into the context as well.49 This allows for a clean, modular, and highly maintainable context architecture, where different aspects of the project's "memory" (e.g., style guides, API documentation, testing protocols) can be kept in separate, dedicated files.  
* **User-Level Global Context:** In addition to project-specific context, global instructions that should apply to all of a user's projects can be defined in a GEMINI.md file located in the user's home configuration directory (\~/.gemini/GEMINI.md).50 This allows for personalization of the AI's behavior across all interactions.

### **4.2. Implementing Persistent Instructions: GEMINI.md as a .clinerules Alternative**

The GEMINI.md file is the direct conceptual and functional equivalent of the .clinerules file mentioned in the background context. It provides a robust mechanism for storing persistent, human-readable instructions that govern the AI's behavior, making it the ideal tool for embedding pedagogical rules into an educational workflow.

An educator can create a GEMINI.md file for a specific programming assignment that tailors the AI's behavior to be that of a tutor rather than a simple code generator.

**Example GEMINI.md for a Python Data Structures Assignment:**

# **Python Data Structures \- Socratic Tutor Rules**

## **General Instructions**

* Your persona is a Socratic tutor. Your primary goal is to guide the student to discover the answer themselves, not to provide the solution directly.  
* When the student's code produces an error, first ask them to explain what they *think* the code is doing line-by-line. Then, ask a probing question that directs their attention to the logical flaw or syntax error.  
* Never write more than 5 lines of code in a single response. Instead of writing a full function, provide a high-level structural hint or a small, illustrative snippet.  
* All Python code you suggest MUST be PEP 8 compliant and include type hints.

## **Topic-Specific Rules: Linked Lists**

* If the student is struggling with pointer manipulation, use an analogy of a train, where each car (Node) has a value and a next coupling to the next car.  
* Before allowing the student to implement a delete method, you MUST ensure they have successfully implemented and tested insert and search methods.  
  This configuration file, placed in the student's assignment folder, transforms Gemini CLI from a general-purpose coding assistant into a specialized educational tool with a clear pedagogical mandate.16

Furthermore, **custom slash commands**, defined in .toml files, can be used to create pre-canned pedagogical prompts. For instance, a /hint command could be created that loads a specific prompt instructing the AI to provide a small, non-obvious clue related to the student's last error.17

### **4.3. Utilizing Conversational Checkpointing for Learning Progress Management**

While GEMINI.md provides long-term memory, students also need a way to manage the short-term memory of their learning sessions, especially for multi-day assignments.

* **The Need for Session Persistence:** Long-form educational projects require the ability for a student to stop their work and resume later without losing the entire conversational history and context of their interaction with the AI tutor.  
* **Gemini CLI's Checkpointing Feature:** Gemini CLI directly addresses this need with a set of built-in commands for managing conversational state, effectively creating save points or checkpoints.32  
  * /chat save \<tag\>: Saves the entire current conversation history to persistent storage under a user-defined tag.  
  * /chat resume \<tag\>: Restores a previously saved conversation, reloading its full history into the current session.  
  * /chat list: Lists all available saved checkpoints.  
  * /chat delete \<tag\>: Removes a saved checkpoint.

    50

This feature acts as a digital lab notebook or a versioned portfolio of the student's learning journey. A student can save their session at the end of a study period and resume it the next day, preserving the full learning trajectory. This is critical not only for the student's own continuity but also for assessment and review, as an instructor could ask the student to share their saved session files to see the entire problem-solving process.

The combination of GEMINI.md for persistent rules and conversational checkpointing for session history creates a powerful, two-tiered memory system. GEMINI.md functions as the agent's **long-term, declarative memory**—it contains the stable, foundational principles and rules of the course. The saved chat history, managed through checkpointing, represents the agent's **short-term, episodic memory**—the specific, contextual history of a single learning interaction. This architecture allows the AI to operate much more like a human tutor, who draws upon both a deep, stable understanding of the subject matter (long-term memory) and the specific history of their dialogue with a student (episodic memory). This dual-memory system is what enables the AI to be a more effective, consistent, and contextually aware educational partner over extended periods.

## **V. Measuring Learning Velocity and Educational Efficacy in Terminal-Based Workflows**

To validate the effectiveness of the terminal-based educational methodology, it is essential to move beyond anecdotal evidence and capture objective, quantitative metrics of student progress. This requires a clear distinction between standard developer productivity metrics and true measures of learning. This section proposes a methodology for capturing "Learning Velocity" in a terminal environment, adapting proven techniques from educational research and testbed monitoring to create a practical analytics framework.

### **5.1. Distinguishing Developer Velocity from Learning Velocity**

In professional software development, **Developer Velocity** is an agile metric used to estimate the amount of work (often measured in abstract "story points" or features delivered) a team can complete in a given iteration.52 It is a measure of output and is often misused as a proxy for productivity or efficiency; it can be easily "gamed" by inflating estimates or sacrificing quality.52

**Learning Velocity**, in contrast, is a pedagogical concept focused on the *rate of knowledge and skill acquisition*. The goal is not to measure how much code a student produces, but rather how quickly they master concepts, overcome challenges, and reduce their reliance on external assistance. This requires a fundamentally different set of metrics, such as reductions in task completion time, improvements in performance scores on assessments, and a decrease in error rates over time.58

The critical gap is that standard developer metrics are poor, and often inverse, proxies for learning. A student might struggle for hours on a single problem, producing very little code but experiencing a significant conceptual breakthrough. Conversely, an AI could generate thousands of lines of correct code for a student, resulting in high "developer velocity" but zero actual learning. Therefore, a new set of metrics tailored to the educational process is required.

### **5.2. Quantitative Metrics: Adapting the ACSLE Model**

The **ACSLE (Automatic System for Monitoring and Analyzing Student Progress)** system provides a proven blueprint for monitoring and analyzing student progress in terminal-based learning environments.60 The core methodology involves logging all terminal input and output and matching these logs against a set of predefined "milestones" that represent key learning objectives for a given assignment.

* **Defining Educational Milestones:** For a typical programming assignment, these milestones are discrete, verifiable achievements in the development process. Examples include:  
  * milestone\_project\_setup: "Student successfully creates a Python virtual environment and installs dependencies using pip."  
  * milestone\_first\_compile: "Student's code compiles or runs without syntax errors for the first time."  
  * milestone\_first\_test\_pass: "Student successfully runs the provided unit tests, and at least one test passes."  
  * milestone\_all\_tests\_pass: "All provided unit tests pass successfully."  
  * milestone\_git\_commit: "Student makes their first successful Git commit with a non-default message."  
  * milestone\_bug\_fix: "Student resolves a specific, known runtime error (e.g., NullPointerException or IndexError)."  
* **Metrics to Capture:** By logging the entire terminal session and parsing the transcript for these milestones, a rich set of quantitative learning metrics can be captured:  
  * **Time-to-Milestone:** The duration from the start of the session (or the previous milestone) to the achievement of the current one. A decreasing time-to-milestone on subsequent, similar tasks is a strong indicator of learning and increased fluency.  
  * **Attempt Count:** The number of failed attempts before successfully achieving a milestone. For example, counting the number of times a build command fails before it succeeds provides a direct measure of a student's struggle and perseverance.  
  * **Intervention Rate:** The frequency with which the student explicitly requests help from the AI tutor (e.g., using commands like /explain\_error, /fix\_bug, or /hint). A decreasing intervention rate over the course of an assignment or across multiple assignments is a powerful indicator of growing independence and mastery.  
  * **Command Sequence Analysis:** Analyzing the patterns and frequency of commands can reveal a student's problem-solving strategies. For instance, frequent use of navigation (ls, cd) and inspection (cat, head) commands might indicate initial exploration or uncertainty, while a shift to more focused build-test-commit cycles indicates a more mature workflow.

### **5.3. Qualitative Metrics: Assessing Deeper Comprehension**

Quantitative data provides the "what," but qualitative measures are needed to understand the "why" behind student performance. These can be gathered through surveys or direct interaction.

* **Self-Efficacy:** A validated scale can be administered before and after an assignment to measure changes in a student's confidence in their programming abilities. An effective AI tutoring system should lead to a measurable increase in self-efficacy.61  
* **Flow Experience:** This psychological concept describes a state of deep immersion, focus, and enjoyment in an activity. A well-designed learning environment should facilitate this state. The flow experience can be measured using established questionnaires, providing insight into student engagement.61  
* **Conceptual Understanding Probes:** At the conclusion of a milestone or the entire assignment, the AI tutor can be programmatically prompted to ask the student a reflective question, such as, "In your own words, can you explain the purpose of the function you just wrote and why the recursive approach was effective?" The student's natural language response, while not easily quantifiable, can be logged and provide rich qualitative data for instructors about the depth of their understanding.

### **5.4. Implementation Approach: A Logging and Analytics Framework**

A practical, non-invasive framework for capturing these metrics can be built using standard command-line utilities, requiring no modification to Gemini CLI itself.

1. **The edu-wrapper Script:** A simple shell script or Python program is created to launch the educational session. This wrapper would perform the following steps:  
   * Initialize a session by recording the start time and loading a milestones.json file specific to the current assignment.  
   * Start a terminal session logger, such as the standard Unix script command or ttylog, which captures all input and output to a transcript file.  
   * Launch the gemini process, allowing the student to interact with the AI tutor as usual.  
   * Upon session completion (detected when the gemini process exits), stop the logger.  
2. **The Analysis Script:** After the session ends, the wrapper invokes a second script to analyze the saved transcript file. This script would:  
   * Use regular expressions to parse the transcript, identifying timestamps, user commands, AI outputs, and matching them against the patterns defined in milestones.json.  
   * Calculate the metrics: time-to-milestone, attempt counts, intervention rates, etc.  
   * Append the structured results (e.g., as a JSON object or CSV row) to a persistent student progress log file.

This lightweight, modular approach provides a powerful system for collecting detailed learning analytics from a terminal-based environment, enabling educators to track progress, identify struggling students, and evaluate the effectiveness of the AI-driven pedagogy.

A more advanced, holistic metric for learning engagement can be derived by analyzing the **entropy** of a student's command-line interactions. This concept, drawn from information theory and applied successfully in learning analytics, uses the predictability of a student's actions as a proxy for their learning state.62 At the beginning of a project, a novice student's command usage is likely to be varied and unpredictable (high entropy) as they explore, experiment, and make mistakes. They might cycle between file navigation, editing, and failed build attempts in a chaotic pattern. As they gain mastery over the workflow and concepts, their command patterns should become more efficient, deliberate, and predictable (lower, more stable entropy), settling into a rhythm of edit-test-commit. A sudden spike in entropy mid-project could signal that they have encountered a novel, challenging problem and are struggling. Conversely, persistently low entropy could indicate either complete mastery or disengagement. By tracking the Shannon entropy of the student's command distribution over time, an educator can gain a high-level, quantitative view of the student's cognitive state, identifying moments of struggle or fluency and enabling more timely and effective interventions.

## **VI. A Framework for the Comparative Analysis of AI Educational Tools**

The selection of an AI tool for an educational setting requires a rigorous evaluation framework that prioritizes pedagogical value over raw technical performance or developer productivity. Standard industry comparisons and benchmarks are often ill-suited for this purpose, as their goals are fundamentally different from those of education. This section proposes a comprehensive framework for the systematic comparison of AI development tools, adapted from established educational research, to assess their true effectiveness as learning aids.

### **6.1. Limitations of Productivity-Focused Benchmarks**

Most contemporary comparisons of AI coding assistants focus on criteria relevant to professional developers: coding speed, language support, IDE integration, context window size, and pricing.63 While important, these metrics fail to capture the nuances of the learning process.

* **The "Correctness" Trap:** Technical benchmarks like SWE-Bench measure an agent's ability to autonomously solve a software engineering problem. This is, in fact, antithetical to the educational objective. A tool that solves every problem perfectly for the student may provide zero learning value, fostering dependency rather than competence. The goal of an educational tool is to enhance the *student's* ability to solve the problem, not to solve it for them.  
* **The Gemini vs. Copilot Dilemma:** A recurring theme in comparisons is that Gemini tends to be more "verbose," "explanatory," and "teacher-like," whereas GitHub Copilot is more "concise," "direct," and "production-ready".67 For a professional developer on a deadline, Gemini's explanatory nature can be perceived as unnecessary noise. For a student learning a new concept, that explanation  
  *is the core value proposition*. This fundamental difference in user goals necessitates a distinct evaluation lens.

### **6.2. Developing an Education-Centric Evaluation Rubric**

Instead of inventing new criteria, a robust evaluation framework can be built by adapting established pedagogical and ethical frameworks for AI in education.

* **The UNESCO AI Competency Framework for Students:** This globally recognized framework provides a comprehensive set of learning objectives for AI education. It is structured around dimensions such as developing a "Human-centred mindset," understanding the "Ethics of AI," and acquiring "AI techniques and applications".71 These dimensions provide high-level categories for evaluating whether a tool supports holistic and responsible learning.  
* **The Processual Assessment Integration Model (P-AI-M):** This model offers a more granular view, analyzing how AI can be integrated into different phases of the educational process, including assessment design, data analysis, performance prediction, and, most relevantly, **feedback provision**.74  
* **Synthesized Rubric Categories:** Drawing from these frameworks and other educational technology evaluation criteria 75, a comprehensive rubric can be constructed around four primary domains:  
  1. **Pedagogical Effectiveness:** How well does the tool actively support and enhance the learning process?  
  2. **Human-AI Collaboration & Agency:** How does the tool structure the relationship between the student and the AI, and who is in control?  
  3. **Ethical & Responsible AI Integration:** Does the tool model and teach the principles of ethical and responsible engineering?  
  4. **Technical & Functional Suitability:** Is the tool accessible, reliable, and practical for use in a typical educational setting?

### **6.3. A Rubric for Evaluating AI Programming Tutors**

The following table provides a detailed rubric for evaluating AI programming tools. Each criterion is derived from the principles discussed above and is designed to be assessed on a four-point scale from "Hinders Learning" to "Accelerates Learning."

| Category | Criterion | 1 \- Hinders Learning | 2 \- Basic Functionality | 3 \- Supports Learning | 4 \- Accelerates Learning |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Pedagogical Effectiveness** | **Scaffolding & Guidance** | Provides direct solutions, discouraging student effort and critical thinking. | Offers code completions and basic fixes but provides little to no guidance on the process. | Breaks down complex problems into manageable steps and provides hints upon request. | Proactively offers a structured plan (e.g., Plan-Act-Review) and provides Socratic, guiding questions when the student struggles. |
|  | **Feedback Quality** | Feedback is generic, non-actionable, or simply points out syntax errors without explanation. | Identifies errors correctly but provides minimal explanation of the root cause. | Explains *why* an error occurred and suggests specific, actionable steps for the student to take. | Provides multi-faceted feedback, explaining the error, linking it to a core programming concept, and suggesting alternative approaches with trade-offs. |
|  | **Concept Reinforcement** | Abstracts away all underlying concepts, presenting code as "magic." | Mentions concepts by name but does not explain them (e.g., "Use recursion"). | Explains relevant programming concepts in the context of the student's specific problem. | Uses analogies, visualizations, or interactive examples to ensure deep conceptual understanding before proceeding. |
| **Human-AI Collaboration & Agency** | **Human Agency & Control** | Operates autonomously, making changes without explicit user approval. Creates dependency. | Requires user approval for changes but presents them in a way that encourages blind acceptance. | Provides clear diffs and requires explicit confirmation for all actions, keeping the student in control. | Facilitates a true collaboration where the AI proposes plans and options, and the student directs, edits, and approves the final implementation. |
|  | **Transparency & Explainability** | Operates as a "black box," providing code with no explanation of its reasoning or how it works. | Can explain code upon request, but the explanation is a separate, post-hoc action. | The AI's reasoning process (e.g., its ReAct loop) is visible, showing the steps it's taking. | Natively explains its thought process as it works, articulating its plan, the tools it selects, and the rationale for its code generation. |
|  | **Problem Scoping** | Encourages vague, one-shot prompts and attempts to solve the entire problem at once. | Requires the user to break down the problem manually into smaller prompts. | Provides tools and prompts that encourage the student to define the problem, constraints, and success criteria upfront. | Actively guides the student through a problem-scoping phase, asking clarifying questions to co-create a detailed project specification. |
| **Ethical & Responsible AI** | **Ethics by Design** | Ignores ethical considerations like bias, privacy, or security in generated code. | Includes basic security scanners but does not explain the vulnerabilities to the student. | Highlights potential security vulnerabilities or data privacy issues in the student's code and explains the risks in simple terms. | Integrates ethical checkpoints into the workflow, prompting the student to consider fairness, bias, and societal impact of their design choices. |
|  | **Data Privacy** | Has an opaque data policy or uses student code and prompts for model training by default. | Allows users to opt-out of data collection in settings, but it is opt-in by default. | Is private-by-default, with clear, accessible policies explaining that student data is not used for training. | Provides fully local or on-premise deployment options, ensuring no data ever leaves the student's or institution's environment. |
| **Technical & Functional Suitability** | **Ease of Use & Accessibility** | Requires complex, multi-step installation and configuration that is a barrier for novice users. | Can be installed via standard package managers but requires manual configuration of API keys and settings files. | Provides a simple, one-command installation and a guided setup process for authentication and configuration. | Offers a pre-configured environment (e.g., via Google Cloud Shell Editor or Docker) that requires zero local setup. |
|  | **Cost & Openness** | Requires an expensive commercial subscription, making it inaccessible for many students and institutions. | Is proprietary but offers a limited free tier that is insufficient for completing a full course. | Is open source and/or offers a generous free tier that is sufficient for educational use cases. | Is fully open source (Apache 2.0 or MIT license), allowing for community inspection, modification, and custom deployment. |

The most educationally effective AI tool is not necessarily the one with the most powerful underlying model, but rather the one that embodies the most thoughtfully designed **interaction paradigm**. A less powerful model constrained by a strong pedagogical framework, such as the Planner-Executor-Tutor model, is likely to produce superior learning outcomes compared to a frontier model that operates as an unconstrained "oracle." The goal of education is not simply to produce a correct artifact (the code), but to build the student's internal capacity to produce such artifacts independently in the future. An "oracle" AI, which provides the correct answer on the first attempt, short-circuits this crucial learning process and fosters dependency. In contrast, a tool that enforces a deliberate cycle of planning, acting, and reviewing, and that provides Socratic feedback upon failure, actively engages the student's higher-order cognitive processes. It is this structured struggle—the process of planning, predicting, reviewing, and debugging—that is the engine of learning. Therefore, when evaluating tools like Gemini CLI for educational use, the primary question is not "Which one writes the best code?" but "Which one provides the best primitives for constructing a pedagogically sound interaction loop?" Features like customizable system prompts (GEMINI.md), an explicit tool-use loop, and amenability to orchestration by frameworks like LangGraph are far more important indicators of educational potential than any raw performance benchmark. This re-frames the entire basis of comparison away from model-centric metrics to interaction-centric ones.

## **VII. Synthesis and Strategic Recommendations for Gemini CLI Implementation**

The analysis conducted throughout this report demonstrates that adapting the sophisticated, context-aware "IDE-Native AI for Accelerated Programming Education" methodology to a terminal-first environment with Gemini CLI is not only feasible but also offers unique pedagogical advantages. A successful implementation requires a strategic integration of existing tools, targeted custom development, and a commitment to a structured, educationally-focused interaction pattern. This final section synthesizes the findings into a unified architectural blueprint and provides a clear, actionable roadmap for implementation.

### **7.1. A Unified Architecture for the Gemini CLI Educational Workflow**

The proposed system is a multi-layered architecture designed to replicate the core pedagogical functions of the IDE-native model within the terminal.

1. **The Core Interaction Engine: Gemini CLI**  
   * At the center is Gemini CLI, serving as the primary interface between the student and the AI system. Its native capabilities—including the ReAct loop, large context window, tool-use proficiency, and extensibility—form the foundation of the educational experience.  
2. **The Pedagogical Layer: Multi-Agent Orchestration with LangGraph**  
   * A Python application built with LangGraph will run in the background or be invoked by a wrapper script. This application implements the **Planner-Executor-Tutor** cognitive architecture.  
   * It will manage the state of the learning session and orchestrate calls to the Gemini API/CLI, routing tasks to the appropriate agent (Planner, Executor, or Tutor) based on the student's progress and the success of their actions. This layer enforces the pedagogical logic of the system.  
3. **The Context & Synchronization Layer: Model Context Protocol (MCP)**  
   * A set of locally running MCP servers will act as the bridge between the AI agents and the student's development environment. This layer is crucial for creating the "shared-view."  
   * **Essential Servers:**  
     * **Filesystem Server:** To provide real-time access to the project's file structure and content.  
     * **Git Server:** To maintain awareness of the project's version control state.  
     * **LSP-mcp Server:** To provide deep, semantic understanding of the code itself.  
   * Both the student's IDE (e.g., VS Code with the Gemini companion extension) and the Gemini CLI will be configured to connect to these same servers, ensuring consistent context.  
4. **The Memory Layer: Persistent Context and Session Management**  
   * **Long-Term Memory:** A project-specific GEMINI.md file will define the persistent pedagogical rules, AI persona (Socratic tutor), and assignment-specific constraints.  
   * **Short-Term Memory:** The Gemini CLI's native /chat save and /chat resume commands will be used to manage session state, allowing students to pause and continue their work across multiple sessions.  
5. **The Analytics Layer: Learning Velocity Measurement**  
   * A wrapper script (edu-wrapper) will launch the Gemini CLI session within a logger (e.g., script).  
   * An assignment-specific milestones.json file will define the key learning objectives to be tracked.  
   * Upon session completion, an analysis script will parse the session transcript, calculate key learning velocity metrics (time-to-milestone, intervention rate, attempt count), and log them for instructor review.

### **7.2. Roadmap for Implementation: Phased Approach**

A phased implementation is recommended to manage complexity and validate each component of the architecture.

**Phase 1: Foundational Setup and Workflow (1-2 Months)**

* **Objective:** Establish the core student-AI interaction loop in the terminal.  
* **Tasks:**  
  1. **Develop Standardized GEMINI.md Templates:** Create a library of GEMINI.md files for different course types and pedagogical styles (e.g., Socratic Tutor, Pair Programmer).  
  2. **Implement the "Plan-Act-Review" Workflow:** Use custom slash commands (/plan, /implement) in Gemini CLI to train students on the structured interaction cycle.  
  3. **Basic Session Management:** Instruct students on using /chat save and /chat resume to manage their work on long-form assignments.  
  4. **Initial Tool Integration:** Deploy and configure the reference Filesystem and Git MCP servers to provide basic workspace awareness.  
* **Outcome:** A functional, manually-orchestrated educational workflow that establishes best practices for interaction and provides basic context awareness.

**Phase 2: Automated Orchestration and Deep Context (3-4 Months)**

* **Objective:** Automate the pedagogical loop and introduce semantic code understanding.  
* **Tasks:**  
  1. **Develop the LangGraph Orchestrator:** Build the core Python application that implements the Planner-Executor-Tutor state machine.  
  2. **Integrate the Orchestrator with Gemini CLI:** The LangGraph application will invoke Gemini CLI (or the Gemini API) to run the Planner, Executor, and Tutor agents.  
  3. **Deploy the LSP-mcp Server:** Integrate and configure the lsp-mcp server for the primary teaching language (e.g., Python or TypeScript). This is the most technically challenging but highest-value step for achieving deep context.  
* **Outcome:** A fully automated multi-agent tutoring system that can guide students through complex tasks with deep, semantic understanding of their code.

**Phase 3: Learning Analytics and Evaluation (2-3 Months)**

* **Objective:** Implement the system for capturing and analyzing learning metrics.  
* **Tasks:**  
  1. **Develop the edu-wrapper and Analysis Scripts:** Create the logging and parsing framework for capturing terminal sessions.  
  2. **Define Milestone Sets:** For a pilot course, create milestones.json files for each assignment.  
  3. **Data Collection and Analysis:** Deploy the system with a cohort of students and begin collecting learning velocity data.  
  4. **Qualitative Feedback:** Supplement quantitative data with student surveys on self-efficacy and flow experience.  
* **Outcome:** A complete end-to-end system with a data-driven feedback loop for evaluating both student performance and the effectiveness of the AI tutor itself.

### **7.3. Future Research Directions and Potential Challenges**

* **The "Tutor" Agent's Sophistication:** The greatest challenge lies in prompting the Tutor agent. Creating a prompt that consistently provides effective Socratic guidance without being too cryptic or too revealing is a significant prompt engineering challenge that will require extensive iteration and testing with real students.  
* **Scalability of Analytics:** While the proposed analytics wrapper is suitable for classroom-scale deployments, a larger-scale implementation would require a more robust data pipeline, potentially logging to a centralized database for longitudinal analysis across courses and student populations.  
* **Cognitive Load:** The terminal environment, even with AI assistance, can have a high cognitive load for absolute beginners. Research should be conducted to determine the ideal onboarding process and to identify at what stage of a student's journey this powerful environment is most effective.  
* **Multi-Modal Integration:** The current framework is text-based. Future work could explore integrating Gemini's multi-modal capabilities, allowing students to, for example, submit a photo of a hand-drawn architecture diagram to the Planner agent for discussion and refinement.

In conclusion, the path to adapting advanced AI-driven pedagogy for the command line is clear. It requires moving beyond the notion of a single, monolithic AI and embracing a modular, multi-agent system built on open standards like MCP and orchestrated by flexible frameworks like LangGraph. By focusing on replicating pedagogical function rather than IDE features, and by building a system to objectively measure learning outcomes, it is possible to create a terminal-based educational experience that is not just a substitute for an IDE, but a uniquely powerful learning environment in its own right.

#### **Works cited**

1. jamesmurdza/awesome-ai-devtools: Curated list of AI-powered developer tools. \- GitHub, accessed August 20, 2025, [https://github.com/jamesmurdza/awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools)  
2. Compare the Top 5 Agentic CLI Coding Tools \- Stream, accessed August 20, 2025, [https://getstream.io/blog/agentic-cli-tools/](https://getstream.io/blog/agentic-cli-tools/)  
3. AI Coding Assistants for Terminal: Claude Code, Gemini CLI & Qodo Compared, accessed August 20, 2025, [https://www.prompt.security/blog/ai-coding-assistants-make-a-cli-comeback](https://www.prompt.security/blog/ai-coding-assistants-make-a-cli-comeback)  
4. Agentic CLI Tools Compared: Claude Code vs Cline vs Aider \- Research AIMultiple, accessed August 20, 2025, [https://research.aimultiple.com/agentic-cli/](https://research.aimultiple.com/agentic-cli/)  
5. Best terminal-based AI pair programmers in 2024 \- Aider vs Plandex vs OpenHands \- Reddit, accessed August 20, 2025, [https://www.reddit.com/r/LocalLLaMA/comments/1hok4h4/best\_terminalbased\_ai\_pair\_programmers\_in\_2024/](https://www.reddit.com/r/LocalLLaMA/comments/1hok4h4/best_terminalbased_ai_pair_programmers_in_2024/)  
6. Claude Code Best Practices: Advanced Command Line AI Development in 2025 \- Collabnix, accessed August 20, 2025, [https://collabnix.com/claude-code-best-practices-advanced-command-line-ai-development-in-2025/](https://collabnix.com/claude-code-best-practices-advanced-command-line-ai-development-in-2025/)  
7. Claude Code: The Future of Terminal-Based AI Development | by ..., accessed August 20, 2025, [https://medium.com/@avilevin23/claude-code-the-future-of-terminal-based-ai-development-bb44091c3f5a](https://medium.com/@avilevin23/claude-code-the-future-of-terminal-based-ai-development-bb44091c3f5a)  
8. Gemini CLI: your open-source AI agent \- Google Blog, accessed August 20, 2025, [https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)  
9. Warp: The Agentic Development Environment, accessed August 20, 2025, [https://www.warp.dev/](https://www.warp.dev/)  
10. Gemini CLI Full Tutorial \- DEV Community, accessed August 20, 2025, [https://dev.to/proflead/gemini-cli-full-tutorial-2ab5](https://dev.to/proflead/gemini-cli-full-tutorial-2ab5)  
11. A Practical Guide on Effective AI Use \- AI as Your Peer Programmer ..., accessed August 20, 2025, [https://nx.dev/blog/practical-guide-effective-ai-coding](https://nx.dev/blog/practical-guide-effective-ai-coding)  
12. Claude Code: Best practices for agentic coding \- Anthropic, accessed August 20, 2025, [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)  
13. Gemini CLI | Gemini for Google Cloud, accessed August 20, 2025, [https://cloud.google.com/gemini/docs/codeassist/gemini-cli](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)  
14. How to Use Gemini CLI: Complete Guide for Developers and Beginners \- MPG ONE, accessed August 20, 2025, [https://mpgone.com/how-to-use-gemini-cli-complete-guide-for-developers-and-beginners/](https://mpgone.com/how-to-use-gemini-cli-complete-guide-for-developers-and-beginners/)  
15. Practical Gemini CLI: Structured approach to bloated GEMINI.md | by Prashanth Subrahmanyam | Google Cloud \- Community | Jul, 2025 | Medium, accessed August 20, 2025, [https://medium.com/google-cloud/practical-gemini-cli-structured-approach-to-bloated-gemini-md-360d8a5c7487](https://medium.com/google-cloud/practical-gemini-cli-structured-approach-to-bloated-gemini-md-360d8a5c7487)  
16. Mastering the Gemini CLI. The Complete Guide to AI-Powered… | by Kristopher Dunham \- Medium, accessed August 20, 2025, [https://medium.com/@creativeaininja/mastering-the-gemini-cli-cb6f1cb7d6eb](https://medium.com/@creativeaininja/mastering-the-gemini-cli-cb6f1cb7d6eb)  
17. Gemini CLI: Custom slash commands | Google Cloud Blog, accessed August 20, 2025, [https://cloud.google.com/blog/topics/developers-practitioners/gemini-cli-custom-slash-commands](https://cloud.google.com/blog/topics/developers-practitioners/gemini-cli-custom-slash-commands)  
18. What Is the Model Context Protocol (MCP) and How It Works, accessed August 20, 2025, [https://www.descope.com/learn/post/mcp](https://www.descope.com/learn/post/mcp)  
19. Model Context Protocol: Introduction, accessed August 20, 2025, [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)  
20. Use Model Context Protocol with Amazon Q Developer for context-aware IDE workflows, accessed August 20, 2025, [https://aws.amazon.com/blogs/devops/use-model-context-protocol-with-amazon-q-developer-for-context-aware-ide-workflows/](https://aws.amazon.com/blogs/devops/use-model-context-protocol-with-amazon-q-developer-for-context-aware-ide-workflows/)  
21. Use MCP servers \- Visual Studio (Windows) | Microsoft Learn, accessed August 20, 2025, [https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=vs-2022](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers?view=vs-2022)  
22. modelcontextprotocol/servers: Model Context Protocol ... \- GitHub, accessed August 20, 2025, [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)  
23. Setting Up MCP Servers in Claude Code: A Tech Ritual for the Quietly Desperate \- Reddit, accessed August 20, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1jf4hnt/setting\_up\_mcp\_servers\_in\_claude\_code\_a\_tech/](https://www.reddit.com/r/ClaudeAI/comments/1jf4hnt/setting_up_mcp_servers_in_claude_code_a_tech/)  
24. How to Use Local Filesystem MCP Server \- DEV Community, accessed August 20, 2025, [https://dev.to/furudo\_erika\_7633eee4afa5/how-to-use-local-filesystem-mcp-server-363e](https://dev.to/furudo_erika_7633eee4afa5/how-to-use-local-filesystem-mcp-server-363e)  
25. Setting up Claude Filesystem MCP \- Medium, accessed August 20, 2025, [https://medium.com/@richardhightower/setting-up-claude-filesystem-mcp-80e48a1d3def](https://medium.com/@richardhightower/setting-up-claude-filesystem-mcp-80e48a1d3def)  
26. jonrad/lsp-mcp: An Model Context Protocol (MCP) server ... \- GitHub, accessed August 20, 2025, [https://github.com/jonrad/lsp-mcp](https://github.com/jonrad/lsp-mcp)  
27. isaacphi/mcp-language-server \- GitHub, accessed August 20, 2025, [https://github.com/isaacphi/mcp-language-server](https://github.com/isaacphi/mcp-language-server)  
28. Use MCP servers in VS Code, accessed August 20, 2025, [https://code.visualstudio.com/docs/copilot/chat/mcp-servers](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)  
29. Visual Studio Code \+ Model Context Protocol (MCP) Servers Getting Started Guide | What, Why, How \- YouTube, accessed August 20, 2025, [https://www.youtube.com/watch?v=iS25RFups4A](https://www.youtube.com/watch?v=iS25RFups4A)  
30. Gemini CLI: Coding with a Million-Token Context in Your IDE \- Medium, accessed August 20, 2025, [https://medium.com/aimonks/gemini-cli-coding-with-a-million-token-context-in-your-ide-0f483753d6f0](https://medium.com/aimonks/gemini-cli-coding-with-a-million-token-context-in-your-ide-0f483753d6f0)  
31. How do I extend Gemini CLI with custom tools? \- Milvus, accessed August 20, 2025, [https://milvus.io/ai-quick-reference/how-do-i-extend-gemini-cli-with-custom-tools](https://milvus.io/ai-quick-reference/how-do-i-extend-gemini-cli-with-custom-tools)  
32. google-gemini/gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal. \- GitHub, accessed August 20, 2025, [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)  
33. Gemini CLI \+ VS Code: Native diffing and context-aware workflows, accessed August 20, 2025, [https://developers.googleblog.com/en/gemini-cli-vs-code-native-diffing-context-aware-workflows/](https://developers.googleblog.com/en/gemini-cli-vs-code-native-diffing-context-aware-workflows/)  
34. wong2/awesome-mcp-servers \- GitHub, accessed August 20, 2025, [https://github.com/wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)  
35. How to Build the Ultimate AI Automation with Multi-Agent Collaboration, accessed August 20, 2025, [https://blog.langchain.com/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration/](https://blog.langchain.com/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration/)  
36. LangGraph: Multi-Agent Workflows \- LangChain Blog, accessed August 20, 2025, [https://blog.langchain.com/langgraph-multi-agent-workflows/](https://blog.langchain.com/langgraph-multi-agent-workflows/)  
37. LangGraph \- LangChain, accessed August 20, 2025, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)  
38. ReAct agent from scratch with Gemini 2.5 and LangGraph | Gemini ..., accessed August 20, 2025, [https://ai.google.dev/gemini-api/docs/langgraph-example](https://ai.google.dev/gemini-api/docs/langgraph-example)  
39. Top 13 Frameworks for Building AI Agents in 2025 \- Bright Data, accessed August 20, 2025, [https://brightdata.com/blog/ai/best-ai-agent-frameworks](https://brightdata.com/blog/ai/best-ai-agent-frameworks)  
40. e2b-dev/awesome-ai-agents: A list of AI autonomous agents \- GitHub, accessed August 20, 2025, [https://github.com/e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)  
41. Top AI agent builders and frameworks for various use cases : r/AI\_Agents \- Reddit, accessed August 20, 2025, [https://www.reddit.com/r/AI\_Agents/comments/1jfk4rz/top\_ai\_agent\_builders\_and\_frameworks\_for\_various/](https://www.reddit.com/r/AI_Agents/comments/1jfk4rz/top_ai_agent_builders_and_frameworks_for_various/)  
42. Building agents with Google Gemini and open source frameworks, accessed August 20, 2025, [https://developers.googleblog.com/en/building-agents-google-gemini-open-source-frameworks/](https://developers.googleblog.com/en/building-agents-google-gemini-open-source-frameworks/)  
43. camel-ai/camel: CAMEL: The first and the best multi-agent ... \- GitHub, accessed August 20, 2025, [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel)  
44. Building Multi-Agent Systems with LangGraph: A Step-by-Step Guide | by Sushmita Nandi, accessed August 20, 2025, [https://medium.com/@sushmita2310/building-multi-agent-systems-with-langgraph-a-step-by-step-guide-d14088e90f72](https://medium.com/@sushmita2310/building-multi-agent-systems-with-langgraph-a-step-by-step-guide-d14088e90f72)  
45. Plan-and-Execute \- GitHub Pages, accessed August 20, 2025, [https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/)  
46. Get started with building Fullstack Agents using Gemini 2.5 and LangGraph \- GitHub, accessed August 20, 2025, [https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart)  
47. \[Feature Request\] Persistent memory or session-level context ..., accessed August 20, 2025, [https://github.com/aws/amazon-q-developer-cli/issues/1343](https://github.com/aws/amazon-q-developer-cli/issues/1343)  
48. Using Gemini CLI to Create a Gemini CLI Config Repo | by Dazbo (Darren Lester) | Google Cloud \- Community | Aug, 2025 | Medium, accessed August 20, 2025, [https://medium.com/google-cloud/using-gemini-cli-to-create-a-gemini-cli-config-repo-519399e25d9a](https://medium.com/google-cloud/using-gemini-cli-to-create-a-gemini-cli-config-repo-519399e25d9a)  
49. Master Context Engineering with Gemini CLI: How to Build Smarter AI-Powered Workflows, accessed August 20, 2025, [https://faraazmohdkhan.medium.com/master-context-engineering-with-gemini-cli-how-to-build-smarter-ai-powered-workflows-3445814f5968](https://faraazmohdkhan.medium.com/master-context-engineering-with-gemini-cli-how-to-build-smarter-ai-powered-workflows-3445814f5968)  
50. Google Gemini CLI Cheatsheet \- Philschmid, accessed August 20, 2025, [https://www.philschmid.de/gemini-cli-cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)  
51. Gemini CLI Tutorial Series — Part 9: Understanding Context, Memory and Conversational Branching | by Romin Irani | Google Cloud \- Medium, accessed August 20, 2025, [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-9-understanding-context-memory-and-conversational-branching-095feb3e5a43)  
52. Velocity (software development) \- Wikipedia, accessed August 20, 2025, [https://en.wikipedia.org/wiki/Velocity\_(software\_development)](https://en.wikipedia.org/wiki/Velocity_\(software_development\))  
53. Developer Velocity: How to Measure and 4 Steps to Improving It ..., accessed August 20, 2025, [https://swimm.io/learn/developer-experience/developer-velocity-how-to-measure-and-4-steps-to-improve-it](https://swimm.io/learn/developer-experience/developer-velocity-how-to-measure-and-4-steps-to-improve-it)  
54. What Is Development Velocity and How Do You Measure It? \- Bunnyshell, accessed August 20, 2025, [https://www.bunnyshell.com/blog/what-development-velocity/](https://www.bunnyshell.com/blog/what-development-velocity/)  
55. Developer Velocity: What It is, How to Measure & Improve It \- Spacelift, accessed August 20, 2025, [https://spacelift.io/blog/developer-velocity](https://spacelift.io/blog/developer-velocity)  
56. What Is Developer Velocity (and How to Realistically Measure It) \- Uplevel, accessed August 20, 2025, [https://uplevelteam.com/blog/measuring-developer-velocity](https://uplevelteam.com/blog/measuring-developer-velocity)  
57. Innovation Metric \- In Defense of Experiment Velocity \- Kromatic, accessed August 20, 2025, [https://kromatic.com/blog/defense-experiment-velocity/](https://kromatic.com/blog/defense-experiment-velocity/)  
58. The Influence of Artificial Intelligence Tools on Learning Outcomes ..., accessed August 20, 2025, [https://www.mdpi.com/2073-431X/14/5/185](https://www.mdpi.com/2073-431X/14/5/185)  
59. Quantitative Evaluation of Software Methodology. \- DTIC, accessed August 20, 2025, [https://apps.dtic.mil/sti/tr/pdf/ADA160202.pdf](https://apps.dtic.mil/sti/tr/pdf/ADA160202.pdf)  
60. Measuring Student Learning On Network Testbeds \- Information ..., accessed August 20, 2025, [https://www.isi.edu/people-mirkovic/wp-content/uploads/sites/52/2023/10/MERIT5.pdf](https://www.isi.edu/people-mirkovic/wp-content/uploads/sites/52/2023/10/MERIT5.pdf)  
61. Full article: The effectiveness of ChatGPT in assisting high school students in programming learning: evidence from a quasi-experimental research \- Taylor & Francis Online, accessed August 20, 2025, [https://www.tandfonline.com/doi/full/10.1080/10494820.2025.2450659](https://www.tandfonline.com/doi/full/10.1080/10494820.2025.2450659)  
62. Students' Learning Behaviour in Programming Education Analysis: Insights from Entropy and Community Detection \- PMC, accessed August 20, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10453761/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10453761/)  
63. 20 Best AI Code Assistants Reviewed and Tested \[August 2025\], accessed August 20, 2025, [https://www.qodo.ai/blog/best-ai-coding-assistant-tools/](https://www.qodo.ai/blog/best-ai-coding-assistant-tools/)  
64. Best AI Coding Assistants as of August 2025 \- Shakudo, accessed August 20, 2025, [https://www.shakudo.io/blog/best-ai-coding-assistants](https://www.shakudo.io/blog/best-ai-coding-assistants)  
65. Best AI Code Assistants Reviews 2025 | Gartner Peer Insights, accessed August 20, 2025, [https://www.gartner.com/reviews/market/ai-code-assistants](https://www.gartner.com/reviews/market/ai-code-assistants)  
66. Best AI Code Assistant: Top Tools for 2025 \- BytePlus, accessed August 20, 2025, [https://www.byteplus.com/en/topic/416162](https://www.byteplus.com/en/topic/416162)  
67. Gemini vs. Copilot: Which AI Assistant Delivers? \- G2 Learning Hub, accessed August 20, 2025, [https://learn.g2.com/gemini-vs-copilot](https://learn.g2.com/gemini-vs-copilot)  
68. I tested Copilot vs Gemini with 10 coding prompts \- Techpoint Africa, accessed August 20, 2025, [https://techpoint.africa/guide/copilot-vs-gemini/](https://techpoint.africa/guide/copilot-vs-gemini/)  
69. Comparison of GitHub Copilot Free and Gemini Code Assist for Individuals in VSCode, accessed August 20, 2025, [https://medium.com/@able\_wong/comparison-of-github-copilot-free-and-gemini-code-assist-for-individuals-in-vscode-c66d6607548a](https://medium.com/@able_wong/comparison-of-github-copilot-free-and-gemini-code-assist-for-individuals-in-vscode-c66d6607548a)  
70. GitHub Copilot vs Gemini Code Assist: Head-to-Head Comparison \- Scaler, accessed August 20, 2025, [https://www.scaler.com/blog/github-copilot-vs-gemini-code-assist/](https://www.scaler.com/blog/github-copilot-vs-gemini-code-assist/)  
71. AI competency framework for students \- NET, accessed August 20, 2025, [https://newmoesitev2.blob.core.windows.net/files/uploads/391105eng.pdf](https://newmoesitev2.blob.core.windows.net/files/uploads/391105eng.pdf)  
72. What you need to know about UNESCO's new AI competency frameworks for students and teachers, accessed August 20, 2025, [https://www.unesco.org/en/articles/what-you-need-know-about-unescos-new-ai-competency-frameworks-students-and-teachers](https://www.unesco.org/en/articles/what-you-need-know-about-unescos-new-ai-competency-frameworks-students-and-teachers)  
73. AI competency framework for teachers \- UNESCO Digital Library, accessed August 20, 2025, [https://unesdoc.unesco.org/ark:/48223/pf0000391104](https://unesdoc.unesco.org/ark:/48223/pf0000391104)  
74. Beyond Automation: A Conceptual Framework for AI in Educational Assessment, accessed August 20, 2025, [https://digital-pedagogy.eu/conceptual-framework-for-ai-in-educational-assessment/](https://digital-pedagogy.eu/conceptual-framework-for-ai-in-educational-assessment/)  
75. Rubric for Evaluating AI Tools: Fundamental Criteria \- eCampusOntario Pressbooks, accessed August 20, 2025, [https://ecampusontario.pressbooks.pub/app/uploads/sites/3696/2024/02/Rubric-for-AI-Tool-Evaluation-Fundamental.pdf](https://ecampusontario.pressbooks.pub/app/uploads/sites/3696/2024/02/Rubric-for-AI-Tool-Evaluation-Fundamental.pdf)  
76. A Teacher Rubric and Checklist for Assessing AI Tools \- TCEA Blog, accessed August 20, 2025, [https://blog.tcea.org/rubric-checklist-assessing-ai-tools/](https://blog.tcea.org/rubric-checklist-assessing-ai-tools/)