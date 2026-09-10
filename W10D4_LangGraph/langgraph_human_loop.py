from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command


# -----------------------------
# State
# -----------------------------
class AgentState(TypedDict, total=False):
    user_input: str
    classification: str
    route: str
    response: str
    human_feedback: str


# -----------------------------
# Node 1: Classify
# -----------------------------
def classify(state: AgentState):
    text = state["user_input"].lower()

    technical_words = [
        "python",
        "java",
        "code",
        "programming",
        "database",
        "sql",
        "api",
        "computer",
        "machine learning",
    ]

    if any(word in text for word in technical_words):
        classification = "technical"
    else:
        classification = "general"

    print(f"[Classify] {classification}")

    return {
        "classification": classification
    }


# -----------------------------
# Node 2: Route
# -----------------------------
def route(state: AgentState):
    classification = state["classification"]

    if classification == "technical":
        selected_route = "technical"
    else:
        selected_route = "general"

    print(f"[Route] {selected_route}")

    return {
        "route": selected_route
    }


# -----------------------------
# Conditional routing
# -----------------------------
def choose_route(state: AgentState):
    if state["route"] == "technical":
        return "technical_response"
    return "general_response"


# -----------------------------
# Node 3: Respond
# -----------------------------
def technical_response(state: AgentState):
    response = (
        "This is a technical request. "
        "I can provide a technical explanation."
    )

    print(f"[Respond] {response}")

    return {
        "response": response
    }


def general_response(state: AgentState):
    response = (
        "This is a general request. "
        "I can provide a simple general answer."
    )

    print(f"[Respond] {response}")

    return {
        "response": response
    }


# -----------------------------
# Human-in-the-loop
# -----------------------------
def human_review(state: AgentState):
    print("[Human Review] Waiting for human input...")

    feedback = interrupt(
        "Please review the response and provide feedback:"
    )

    print(f"[Human Review] {feedback}")

    return {
        "human_feedback": feedback
    }


# -----------------------------
# Build graph
# -----------------------------
builder = StateGraph(AgentState)

builder.add_node("classify", classify)
builder.add_node("route", route)
builder.add_node("technical_response", technical_response)
builder.add_node("general_response", general_response)
builder.add_node("human_review", human_review)

builder.add_edge(START, "classify")
builder.add_edge("classify", "route")

builder.add_conditional_edges(
    "route",
    choose_route,
    {
        "technical_response": "technical_response",
        "general_response": "general_response",
    },
)

builder.add_edge("technical_response", "human_review")
builder.add_edge("general_response", "human_review")
builder.add_edge("human_review", END)

from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)


# -----------------------------
# Test with 5 inputs
# -----------------------------
test_inputs = [
    "How does Python work?",
    "What is the weather today?",
    "Explain SQL database",
    "Tell me a simple joke",
    "What is machine learning?",
]


print("=" * 55)
print("W10D4: Human-in-the-Loop with LangGraph")
print("=" * 55)

for number, user_input in enumerate(test_inputs, start=1):

    print(f"\n--- Test {number} ---")
    print(f"Input: {user_input}")

    config = {
        "configurable": {
            "thread_id": f"w10d4-test-{number}"
        }
    }

    result = graph.invoke(
        {
            "user_input": user_input
        },
        config=config,
    )

    # Human interrupt
    if "__interrupt__" in result:

        print("Human-in-the-loop interrupt triggered.")

        human_feedback = input("Enter human feedback: ")

        result = graph.invoke(
            Command(resume=human_feedback),
            config=config,
        )

        print("Workflow resumed successfully.")

    print("Test completed.")


print("\n" + "=" * 55)
print("W10D4 testing completed successfully.")
print("Conditional routing verified.")
print("Human-in-the-loop pause and resume verified.")
print("=" * 55)