# W9D2 — CrewAI Tools: Web Search

## Project Title

**Multi-Agent Research Crew with Web Search using CrewAI**

## Objective

The objective of this task is to understand how CrewAI tools can be integrated into a multi-agent system.

In this project, three specialized agents work together:

* **Researcher** — searches the web and collects information
* **Technical Writer** — converts research findings into a structured article
* **Content Reviewer** — reviews the article and suggests improvements

The Researcher agent uses the **Serper Web Search tool** to obtain current information from the web.

---

## Agents

### 1. Researcher

**Role:** Web Researcher

**Goal:**
Research the given topic using web search and collect accurate, current, and useful information.

**Tool:**
SerperDevTool

---

### 2. Technical Writer

**Role:** Technical Writer

**Goal:**
Transform research findings into a clear, well-structured and easy-to-understand article.

**Tool:**
Local Ollama LLM

---

### 3. Content Reviewer

**Role:** Content Reviewer

**Goal:**
Review the generated article for accuracy, clarity, completeness, organization and overall quality.

**Tool:**
Local Ollama LLM

---

## Tasks

### Task 1 — Web Research

The Researcher searches the web for information about:

**"Generative AI in Healthcare"**

The research focuses on:

* Applications
* Benefits
* Challenges
* Risks
* Recent developments
* Future scope

---

### Task 2 — Article Writing

The Writer receives the Researcher's findings and creates a structured article.

The article contains:

* Introduction
* Applications
* Benefits
* Challenges
* Risks
* Recent developments
* Future scope
* Conclusion

---

### Task 3 — Content Review

The Reviewer checks the article for:

* Accuracy
* Clarity
* Completeness
* Organization
* Relevance
* Missing information

The Reviewer also provides specific suggestions for improvement.

---

## Crew Workflow

The agents communicate in a sequential workflow:

```text
Researcher
    ↓
Serper Web Search
    ↓
Research Findings
    ↓
Technical Writer
    ↓
Article
    ↓
Content Reviewer
    ↓
Review & Suggestions
```

The CrewAI process used is:

```python
Process.sequential
```

This means the tasks are executed one after another.

---

## Web Search Tool

The project uses:

**SerperDevTool**

The tool allows the Researcher agent to search the web for real and current information.

The Serper API key is stored as an environment variable:

```text
SERPER_API_KEY
```

The API key is **not stored in the source code or GitHub repository**.

---

## Local LLM

The project uses the local Ollama model:

```text
llama3.2:3b
```

Ollama runs locally at:

```text
http://localhost:11434
```

Using a local LLM avoids sending the agent's main generation requests to a cloud LLM provider.

---

## Technologies Used

* Python
* CrewAI
* CrewAI Tools
* Serper Web Search
* Ollama
* Llama 3.2 3B
* Multi-Agent Systems

---

## Files

```text
W9D2_CrewAI_Tools/
│
├── basic_crew.py
├── web_search_crew.py
├── crew_tools.py
├── requirements.txt
├── README.md
├── self_review.md
│
└── outputs/
    ├── basic_output.txt
    └── web_search_output.txt
```

### File Description

| File                 | Purpose                                      |
| -------------------- | -------------------------------------------- |
| `basic_crew.py`      | Runs the multi-agent crew without web search |
| `web_search_crew.py` | Runs the crew with Serper web search         |
| `crew_tools.py`      | CrewAI tools implementation/testing          |
| `requirements.txt`   | Python dependencies                          |
| `README.md`          | Project documentation                        |
| `self_review.md`     | Self-review checklist                        |
| `outputs/`           | Stores execution evidence                    |

---

## Installation

Install the required packages:

```bash
pip install crewai==1.15.18 crewai-tools==1.15.18
```

Make sure Ollama is installed and the model is available:

```bash
ollama list
```

The required model is:

```text
llama3.2:3b
```

---

## Configure Web Search

Set the Serper API key as an environment variable.

### Windows CMD

```cmd
set "SERPER_API_KEY=YOUR_API_KEY"
```

Verify that the key is available without displaying it:

```cmd
python -c "import os; print('SERPER:', bool(os.getenv('SERPER_API_KEY')))"
```

Expected output:

```text
SERPER: True
```

**Never commit the API key to GitHub.**

---

## Running the Project

### Basic Crew

Run the crew without web search:

```bash
python basic_crew.py
```

This provides a baseline result using the local LLM.

### Web Search Crew

Run the crew with real web search:

```bash
python web_search_crew.py
```

The Researcher uses Serper to collect information from the web before passing the findings to the Writer.

---

## Before vs After Web Search

### Before Web Search

The Researcher mainly depends on the knowledge available through the local LLM.

**Limitations:**

* Information may not be current
* No direct web research
* Limited access to recent developments
* Fewer external sources

### After Web Search

The Researcher uses Serper Web Search to obtain information from online sources.

**Improvements:**

* More current information
* Real web-based research
* Better research coverage
* More relevant information
* Better context for the Writer
* Improved review quality

---

## Example Research Topic

```text
Generative AI in Healthcare
```

The Researcher searches for information related to:

```text
Applications
Benefits
Challenges
Risks
Recent Developments
Future Scope
```

---

## Output

The final output contains:

1. Research findings
2. Generated article
3. Content review
4. Improvement suggestions

Example workflow:

```text
Researcher → Web Search → Research
                         ↓
                       Writer
                         ↓
                       Article
                         ↓
                      Reviewer
                         ↓
                  Final Review
```

---

## Learning Outcomes

After completing this task, the following concepts are understood:

* CrewAI agents
* Agent roles and goals
* Agent backstories
* CrewAI tasks
* Task context
* Sequential process
* CrewAI tools
* Web search integration
* Multi-agent communication
* Local LLM integration
* Research automation
* Content review using AI agents

---

## Conclusion

This project demonstrates a practical multi-agent research workflow using CrewAI.

The Researcher collects information using real web search, the Writer converts the findings into a structured article, and the Reviewer evaluates the final content.

Adding web search improves the system by providing access to current external information instead of relying only on the local LLM's existing knowledge.
