# W9D1 — Web Search Improvement

## Before Adding Web Search

Initially, the CrewAI system used three agents:

1. Researcher
2. Writer
3. Reviewer

The Researcher generated research information using the configured local LLM. The Writer converted the research into an article, and the Reviewer checked the generated content.

However, the Researcher was mainly dependent on the knowledge available through the language model.

## After Adding Web Search

Web search was added to the Researcher agent using **SerperDevTool**.

This allows the Researcher to search the internet and use current web information while researching the topic.

## Improvements Observed

### 1. More Up-to-Date Information

The Researcher can access current information from web search results instead of relying only on the model's existing knowledge.

### 2. Better Research

The Researcher can collect information from multiple relevant web sources.

### 3. More Relevant Content

The Writer receives richer research findings, which helps produce a more detailed and relevant article.

### 4. Better Review

The Reviewer receives improved content and can identify missing information or areas that require improvement.

### 5. Real-World Data

The system can incorporate information obtained from real web sources into the research workflow.

## Comparison

| Without Web Search              | With Web Search                |
| ------------------------------- | ------------------------------ |
| Mainly uses LLM knowledge       | Uses LLM + web information     |
| Information may be less current | Can access current information |
| Limited external research       | Searches multiple web sources  |
| Basic research output           | Richer research output         |
| Less real-world context         | More real-world context        |

## Web Search Test

The Researcher searched for:

**"Generative AI in Healthcare uses benefits challenges future scope"**

The search successfully returned relevant web results from sources related to healthcare and Generative AI.

## Conclusion

Adding web search improved the CrewAI research workflow by giving the Researcher access to current web information. This resulted in richer research that could be passed to the Writer and Reviewer.

Therefore, integrating an external search tool makes the multi-agent research system more useful for real-world research tasks.
