# W9D1 — CrewAI Fundamentals

## Project Title

**Multi-Agent Research Crew using CrewAI**

## Objective

The objective of this task is to understand the fundamentals of CrewAI by creating a multi-agent system with specialized agents, tasks, and a crew.

The system uses three agents:

**Researcher → Writer → Reviewer**

The agents work sequentially to research a topic, create an article, and review the generated content.

## Technologies Used

* Python
* CrewAI
* CrewAI Tools
* Ollama
* Llama 3.2
* Serper Web Search

## Agents

### 1. Researcher

**Role:** Researcher

**Goal:** Research the given topic and provide accurate and useful information.

**Responsibility:** Collect relevant information, facts, applications, benefits, challenges, and examples.

### 2. Writer

**Role:** Writer

**Goal:** Convert the research findings into a clear and well-structured article.

**Responsibility:** Organize the research information and create an easy-to-understand article.

### 3. Reviewer

**Role:** Reviewer

**Goal:** Review the article for accuracy, clarity, completeness, and quality.

**Responsibility:** Identify problems, missing information, and areas that can be improved.

## Tasks

### Research Task

The Researcher investigates the topic **"Generative AI in Healthcare"** and collects useful information.

### Writing Task

The Writer uses the research findings to create a structured article covering applications, benefits, challenges, and future scope.

### Review Task

The Reviewer checks the generated article and provides feedback and improvement suggestions.

## Workflow

```text
Researcher
    ↓
Writer
    ↓
Reviewer
    ↓
Final Reviewed Output
```

The crew uses the **sequential process**, where each task is executed one after another.

## Local LLM

The project uses **Ollama with Llama 3.2:3b** as the local language model.

This allows the agents to generate responses using a locally running LLM.

## Web Search

A web search tool was added to the Researcher agent using **SerperDevTool**.

The Researcher can search the web and use current information while performing the research task.

## Topic

**Generative AI in Healthcare**

The research covers:

* Applications
* Benefits
* Challenges
* Future scope

## Expected Result

The CrewAI system successfully:

1. Researches the given topic.
2. Uses research findings to create an article.
3. Reviews the generated article.
4. Produces a final reviewed output.

## Learning Outcomes

Through this task, I learned:

* How to create CrewAI agents.
* How to define agent roles, goals, and backstories.
* How to create and assign tasks.
* How to create a Crew.
* How sequential processing works.
* How agents can use external tools.
* How web search improves research quality.
* How multiple specialized agents can work together.

## Conclusion

This project demonstrates a basic multi-agent research workflow using CrewAI. By separating research, writing, and reviewing responsibilities between different agents, the system provides a structured approach to generating and checking information.
