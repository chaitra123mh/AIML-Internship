from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command


# -----------------------------
# State
# -----------------------------
class AgentState(TypedDict):
    user_input: str
    classification: str
    route: str
    response: str


# -----------------------------
# Node 1: Classify
# -----------------------------
def classify_node(state: AgentState):
    text = state["user_input"].lower()

    if any(word in text for word in [
        "python", "java", "code", "programming",
        "api", "database", "docker", "machine learning"
    ]):
        classification = "technical"

    elif any(word in text for word in [
        "approve", "delete", "send", "payment",
        "account", "important"
    ]):
        classification = "human_review"

    else:
        classification = "general"

    return {
        "classification": classification
    }


# -----------------------------
# Node 2: Route
# -----------------------------
def route_node(state: AgentState):
    classification = state["classification"]

    if classification == "technical":
        route = "technical_response"

    elif classification == "human_review":
        route = "human_review"

    else:
        route = "general_response"

    return {
        "route": route
    }


# -----------------------------
# Conditional routing
# -----------------------------
def conditional_route(state: AgentState):
    return state["route"]


# -----------------------------
# Technical response
# -----------------------------
def technical_response(state: AgentState):
    response = (
        f"Technical response: Your question is related to "
        f"technology or programming. Input: {state['user_input']}"
    )

    return {
        "response": response
    }


# -----------------------------
# General response
# -----------------------------
def general_response(state: AgentState):
    response = (
        f"General response: I can help with this general question. "
        f"Input: {state['user_input']}"
    )

    return {
        "response": response
    }


# -----------------------------
# Human-in-the-loop
# -----------------------------
def human_review_node(state: AgentState):

    human_decision = interrupt(
        {
            "message": "Human approval required.",
            "input": state["user_input"],
            "question": "Approve this request? Enter APPROVE or REJECT."
        }
    )

    return {
        "response": (
            f"Human decision: {human_decision}"
        )
    }


# -----------------------------
# Build graph
# -----------------------------
builder = StateGraph(AgentState)

builder.add_node("classify", classify_node)
builder.add_node("route", route_node)
builder.add_node("technical_response", technical_response)
builder.add_node("general_response", general_response)
builder.add_node("human_review", human_review_node)

builder.add_edge(START, "classify")
builder.add_edge("classify", "route")

builder.add_conditional_edges(
    "route",
    conditional_route,
    {
        "technical_response": "technical_response",
        "general_response": "general_response",
        "human_review": "human_review"
    }
)

builder.add_edge("technical_response", END)
builder.add_edge("general_response", END)
builder.add_edge("human_review", END)


# Memory/checkpointing is required for interrupt/resume
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)


# -----------------------------
# Test 1-4: Normal routing
# -----------------------------
test_inputs = [
    "How can I learn Python?",
    "What is the capital of India?",
    "Explain Docker containers.",
    "What is your favorite food?"
]

print("\n========== W10D1 TEST RESULTS ==========\n")

for i, user_input in enumerate(test_inputs, start=1):

    config = {
        "configurable": {
            "thread_id": f"test-{i}"
        }
    }

    result = graph.invoke(
        {
            "user_input": user_input,
            "classification": "",
            "route": "",
            "response": ""
        },
        config
    )

    print(f"Test {i}")
    print(f"Input          : {user_input}")
    print(f"Classification : {result['classification']}")
    print(f"Route          : {result['route']}")
    print(f"Response       : {result['response']}")
    print("-" * 60)


# -----------------------------
# Test 5: Human interrupt
# -----------------------------
print("\n========== HUMAN-IN-THE-LOOP TEST ==========\n")

human_input = "Please approve this important account request."

config = {
    "configurable": {
        "thread_id": "human-test-1"
    }
}

result = graph.invoke(
    {
        "user_input": human_input,
        "classification": "",
        "route": "",
        "response": ""
    },
    config
)

print("Graph paused for human approval.")
print("Input:", human_input)
print("Classification:", result["classification"])
print("Route:", result["route"])

print("\nHuman decision required.")
decision = input("Enter APPROVE or REJECT: ")

resumed_result = graph.invoke(
    Command(resume=decision),
    config
)

print("\nGraph resumed successfully.")
print("Human decision:", decision)
print("Final response:", resumed_result["response"])