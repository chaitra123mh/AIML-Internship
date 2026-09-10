from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command


# State shared between all nodes
class AgentState(TypedDict):
    user_input: str
    classification: str
    route: str
    response: str
    human_decision: str


# Node 1: Classify the input
def classify(state: AgentState):
    text = state["user_input"].lower()

    technical_words = [
        "python", "java", "sql", "code", "programming",
        "api", "docker", "database", "machine learning"
    ]

    if any(word in text for word in technical_words):
        classification = "technical"
    else:
        classification = "general"

    print(f"Classification: {classification}")

    return {"classification": classification}


# Node 2: Decide the route
def route(state: AgentState):
    classification = state["classification"]

    if classification == "technical":
        selected_route = "technical_response"
    else:
        selected_route = "general_response"

    print(f"Route selected: {selected_route}")

    return {"route": selected_route}


# Node 3A: Technical response
def technical_response(state: AgentState):
    response = (
        "This is a technical question. "
        "I can provide a technical explanation or coding solution."
    )

    return {"response": response}


# Node 3B: General response
def general_response(state: AgentState):
    response = (
        "This is a general question. "
        "I can provide a simple and helpful answer."
    )

    return {"response": response}


# Human-in-the-loop node
def human_review(state: AgentState):
    decision = interrupt(
        {
            "message": "Human review required.",
            "response": state["response"],
            "instruction": "Type approve or reject."
        }
    )

    return {"human_decision": decision}


# Build the graph
builder = StateGraph(AgentState)

builder.add_node("classify", classify)
builder.add_node("route", route)
builder.add_node("technical_response", technical_response)
builder.add_node("general_response", general_response)
builder.add_node("human_review", human_review)

builder.add_edge(START, "classify")
builder.add_edge("classify", "route")


# Conditional edge based on classification
def classification_router(state: AgentState):
    if state["classification"] == "technical":
        return "technical_response"
    return "general_response"


builder.add_conditional_edges(
    "route",
    classification_router,
    {
        "technical_response": "technical_response",
        "general_response": "general_response"
    }
)

builder.add_edge("technical_response", "human_review")
builder.add_edge("general_response", "human_review")
builder.add_edge("human_review", END)


# Memory allows the graph to pause and resume
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)


# Test 5 inputs
test_inputs = [
    "How do I write Python code?",
    "What is your favorite food?",
    "Explain SQL database.",
    "How can I improve my communication?",
    "What is Docker?"
]


print("\n===== W10D2 LANGGRAPH STATE MACHINE =====\n")

for i, user_input in enumerate(test_inputs, 1):

    print(f"\n--- Test {i} ---")
    print(f"Input: {user_input}")

    config = {
        "configurable": {
            "thread_id": f"test-{i}"
        }
    }

    initial_state = {
        "user_input": user_input,
        "classification": "",
        "route": "",
        "response": "",
        "human_decision": ""
    }

    result = graph.invoke(initial_state, config)

    # Check whether execution paused for human review
    if "__interrupt__" in result:

        print("Graph paused for human review.")

        decision = "approve"

        result = graph.invoke(
            Command(resume=decision),
            config
        )

        print(f"Human decision: {decision}")

    print(f"Final response: {result.get('response', '')}")

print("\n===== TESTING COMPLETED =====")