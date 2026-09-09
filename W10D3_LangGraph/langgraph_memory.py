from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command


# -----------------------------
# State
# -----------------------------
class AgentState(TypedDict, total=False):
    user_input: str
    classification: str
    route: str
    response: str
    human_decision: str


# -----------------------------
# Node 1: Classify
# -----------------------------
def classify(state: AgentState):
    text = state["user_input"].lower()

    if any(word in text for word in [
        "python", "java", "code", "programming",
        "database", "sql", "api", "machine learning"
    ]):
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
# Node 3: Respond
# -----------------------------
def respond(state: AgentState):
    if state["route"] == "technical":
        response = (
            "This is a technical question. "
            "I can provide a technical explanation."
        )
    else:
        response = (
            "This is a general question. "
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

    decision = interrupt(
        "Please enter human approval or feedback:"
    )

    print(f"[Human Review] {decision}")

    return {
        "human_decision": decision
    }


# -----------------------------
# Build Graph
# -----------------------------
builder = StateGraph(AgentState)

builder.add_node("classify", classify)
builder.add_node("route", route)
builder.add_node("respond", respond)
builder.add_node("human_review", human_review)

builder.add_edge(START, "classify")
builder.add_edge("classify", "route")
builder.add_edge("route", "respond")
builder.add_edge("respond", "human_review")
builder.add_edge("human_review", END)


# -----------------------------
# Persistent Memory
# -----------------------------
memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


# -----------------------------
# Test Conversation
# -----------------------------
if __name__ == "__main__":

    print("\n===== W10D3: LangGraph + Memory =====\n")

    config = {
        "configurable": {
            "thread_id": "conversation-1"
        }
    }

    inputs = [
        "What is Python?",
        "Explain SQL database",
        "How can I improve my communication?",
        "What is machine learning?",
        "Tell me a simple study tip"
    ]

    for i, user_input in enumerate(inputs, start=1):

        print(f"\n--- Test {i} ---")
        print(f"User: {user_input}")

        result = graph.invoke(
            {
                "user_input": user_input
            },
            config
        )

        if "__interrupt__" in result:
            print("Graph paused for human review.")

            human_input = input(
                "Enter human feedback: "
            )

            result = graph.invoke(
                Command(resume=human_input),
                config
            )

        print(f"Final response: {result.get('response')}")
        print(f"Human decision: {result.get('human_decision')}")

    print("\n===== Conversation Memory Test =====")

    memory_config = {
        "configurable": {
            "thread_id": "conversation-memory-test"
        }
    }

    first_message = graph.invoke(
        {
            "user_input": "I am learning Python."
        },
        memory_config
    )

    if "__interrupt__" in first_message:
        print("First conversation paused.")

        feedback = input(
            "Enter human feedback: "
        )

        first_message = graph.invoke(
            Command(resume=feedback),
            memory_config
        )

    print("First interaction completed.")

    second_message = graph.invoke(
        {
            "user_input": "I want to continue learning it."
        },
        memory_config
    )

    if "__interrupt__" in second_message:
        print("Second conversation paused.")

        feedback = input(
            "Enter human feedback: "
        )

        second_message = graph.invoke(
            Command(resume=feedback),
            memory_config
        )

    print("Second interaction completed.")

    print("\nPersistent conversation test completed successfully.")