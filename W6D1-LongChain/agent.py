from langchain_core.tools import tool


@tool
def web_search(query: str) -> str:
    """Search the web using a simple stub."""
    return f"Web search result for: {query}"


@tool
def calculator(expression: str) -> str:
    """Calculate a simple mathematical expression."""
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"


tools = [web_search, calculator]

print("=" * 60)
print("W6D1 - SIMPLE AGENT TOOLS")
print("=" * 60)

tasks = [
    ("web_search", "Latest information about machine learning"),
    ("calculator", "25 * 4"),
    ("web_search", "What is ChromaDB?")
]

for i, (tool_name, task) in enumerate(tasks, 1):

    print(f"\nTASK {i}")

    if tool_name == "web_search":
        result = web_search.invoke(task)
    else:
        result = calculator.invoke(task)

    print("Task:", task)
    print("Result:", result)

print("\nAgent tools completed successfully!")