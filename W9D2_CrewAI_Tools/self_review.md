# W9D2 Self-Review – CrewAI Tools

## Task Checklist

* [x] Created three CrewAI agents: Researcher, Technical Writer, and Content Reviewer.
* [x] Defined roles, goals, and backstories for all agents.
* [x] Created research, writing, and review tasks.
* [x] Used `Process.sequential` for agent execution.
* [x] Passed research results to the Writer using task context.
* [x] Passed the Writer's output to the Reviewer using task context.
* [x] Added web search using `SerperDevTool`.
* [x] Used real web search results for research.
* [x] Created a basic crew without web search for comparison.
* [x] Created a web-search-enabled crew.
* [x] Documented the project in `README.md`.
* [x] Prepared output evidence for both approaches.

## Learning Outcomes

I learned how to create multiple agents in CrewAI and assign different responsibilities to each agent. I also learned how tasks can pass information from one agent to another using task context.

I learned how to use `SerperDevTool` to provide real web search capabilities to the Researcher agent.

## Output Quality Review

The basic crew can generate content using the available model knowledge, but it may not contain the latest information.

The web-search-enabled crew can retrieve current information from the web before generating the research. This makes the research more useful for topics where recent information is important.

## Challenges Faced

* Configuring the Serper API key correctly.
* Connecting CrewAI with the local Ollama LLM.
* Understanding how agents and tasks communicate in a sequential process.
* Handling tool execution errors during the initial setup.

## Final Status

W9D2 CrewAI Tools practical task completed successfully with multi-agent research, writing, reviewing, and web-search functionality.
