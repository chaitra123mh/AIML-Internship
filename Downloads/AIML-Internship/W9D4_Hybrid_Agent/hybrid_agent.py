from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool


@tool("Web Search Stub")
def web_search_stub(query: str) -> str:
    """Returns a simulated web search result."""
    return f"Web search result for '{query}': AI is widely used in healthcare, finance and education."


@tool("Calculator")
def calculator(expression: str) -> str:
    """Calculate a basic mathematical expression."""
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception:
        return "Invalid calculation."


llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)

agent = Agent(
    role="Hybrid Assistant",
    goal="Use the correct tool to solve user tasks.",
    backstory="You are a helpful AI assistant using web search and calculation tools.",
    tools=[web_search_stub, calculator],
    llm=llm,
    verbose=False,
    max_iter=2
)

tasks = [
    Task(
        description="Use the web search tool to find one fact about artificial intelligence.",
        expected_output="One short AI fact.",
        agent=agent
    ),
    Task(
        description="Use the calculator tool to calculate 25 * 4 + 10.",
        expected_output="The numerical answer.",
        agent=agent
    ),
    Task(
        description="Use the web search tool to give one benefit of AI in healthcare.",
        expected_output="One short benefit.",
        agent=agent
    )
]

crew = Crew(
    agents=[agent],
    tasks=tasks,
    process=Process.sequential,
    verbose=False
)

result = crew.kickoff()

print("\n===== HYBRID AGENT OUTPUT =====")
print(result)
print("\n===== 3 TASKS COMPLETED =====")