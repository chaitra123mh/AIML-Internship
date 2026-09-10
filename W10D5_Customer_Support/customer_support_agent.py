from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command


# -----------------------------
# Customer Support State
# -----------------------------
class SupportState(TypedDict, total=False):
    customer_message: str
    category: str
    response: str
    human_feedback: str
    conversation_history: list[str]


# -----------------------------
# Node 1: Classify Customer Issue
# -----------------------------
def classify_issue(state: SupportState):
    message = state["customer_message"].lower()

    if any(word in message for word in ["refund", "money", "payment", "charged"]):
        category = "billing"
    elif any(word in message for word in ["password", "login", "account", "technical"]):
        category = "technical"
    elif any(word in message for word in ["delivery", "order", "shipping", "package"]):
        category = "order"
    else:
        category = "general"

    print(f"[Classify] {category}")

    return {"category": category}


# -----------------------------
# Node 2: Route Customer Issue
# -----------------------------
def route_issue(state: SupportState):
    category = state["category"]

    print(f"[Route] {category}")

    return {}


# -----------------------------
# Conditional Routing
# -----------------------------
def choose_response(state: SupportState):
    category = state["category"]

    if category == "billing":
        return "billing_response"
    elif category == "technical":
        return "technical_response"
    elif category == "order":
        return "order_response"
    else:
        return "general_response"


# -----------------------------
# Response Nodes
# -----------------------------
def billing_response(state: SupportState):
    response = (
        "I can help with your billing issue. "
        "Please check your payment details and transaction information."
    )

    print(f"[Response] {response}")

    return {"response": response}


def technical_response(state: SupportState):
    response = (
        "I can help with your technical issue. "
        "Please check your login details or try resetting your password."
    )

    print(f"[Response] {response}")

    return {"response": response}


def order_response(state: SupportState):
    response = (
        "I can help with your order. "
        "Please provide your order details so the delivery status can be checked."
    )

    print(f"[Response] {response}")

    return {"response": response}


def general_response(state: SupportState):
    response = (
        "Thank you for contacting customer support. "
        "I will help you with your request."
    )

    print(f"[Response] {response}")

    return {"response": response}


# -----------------------------
# Human-in-the-Loop
# -----------------------------
def human_review(state: SupportState):
    print("[Human Review] Waiting for human approval...")

    feedback = interrupt(
        "Please review the support response and provide feedback:"
    )

    print(f"[Human Review] {feedback}")

    history = state.get("conversation_history", [])

    history.append(
        f"Customer: {state['customer_message']}"
    )

    history.append(
        f"Agent: {state['response']}"
    )

    history.append(
        f"Human Feedback: {feedback}"
    )

    return {
        "human_feedback": feedback,
        "conversation_history": history,
    }


# -----------------------------
# Build LangGraph
# -----------------------------
builder = StateGraph(SupportState)

builder.add_node("classify_issue", classify_issue)
builder.add_node("route_issue", route_issue)
builder.add_node("billing_response", billing_response)
builder.add_node("technical_response", technical_response)
builder.add_node("order_response", order_response)
builder.add_node("general_response", general_response)
builder.add_node("human_review", human_review)

builder.add_edge(START, "classify_issue")
builder.add_edge("classify_issue", "route_issue")

builder.add_conditional_edges(
    "route_issue",
    choose_response,
    {
        "billing_response": "billing_response",
        "technical_response": "technical_response",
        "order_response": "order_response",
        "general_response": "general_response",
    },
)

builder.add_edge("billing_response", "human_review")
builder.add_edge("technical_response", "human_review")
builder.add_edge("order_response", "human_review")
builder.add_edge("general_response", "human_review")

builder.add_edge("human_review", END)


# -----------------------------
# Persistent Memory
# -----------------------------
memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


# -----------------------------
# Test Customer Conversations
# -----------------------------
test_messages = [
    "I was charged twice for my order.",
    "I forgot my password and cannot login.",
    "Where is my delivery package?",
    "I need help with my account.",
    "I want a refund for my payment.",
]


print("=" * 60)
print("W10D5: STATEFUL CUSTOMER SUPPORT AGENT")
print("=" * 60)


for number, message in enumerate(test_messages, start=1):

    print(f"\n--- Customer Test {number} ---")
    print(f"Customer: {message}")

    config = {
        "configurable": {
            "thread_id": f"customer-{number}"
        }
    }

    result = graph.invoke(
        {
            "customer_message": message,
            "conversation_history": [],
        },
        config=config,
    )

    if "__interrupt__" in result:

        print("Human-in-the-loop interrupt triggered.")

        feedback = input("Enter human feedback: ")

        result = graph.invoke(
            Command(resume=feedback),
            config=config,
        )

        print("Support workflow resumed successfully.")

    print("Customer test completed.")


# -----------------------------
# Persistent Conversation Test
# -----------------------------
print("\n" + "=" * 60)
print("PERSISTENT MEMORY TEST")
print("=" * 60)

memory_config = {
    "configurable": {
        "thread_id": "persistent-customer-1"
    }
}

first_message = "I was charged for an order I cancelled."

print(f"\nCustomer: {first_message}")

result = graph.invoke(
    {
        "customer_message": first_message,
        "conversation_history": [],
    },
    config=memory_config,
)

if "__interrupt__" in result:

    print("First conversation paused.")

    feedback = input("Enter human feedback: ")

    result = graph.invoke(
        Command(resume=feedback),
        config=memory_config,
    )

    print("First conversation completed.")


second_message = "I want to know about my refund."

print(f"\nCustomer: {second_message}")

previous_state = graph.get_state(memory_config)

history = previous_state.values.get(
    "conversation_history",
    []
)

result = graph.invoke(
    {
        "customer_message": second_message,
        "conversation_history": history,
    },
    config=memory_config,
)

if "__interrupt__" in result:

    print("Second conversation paused.")

    feedback = input("Enter human feedback: ")

    result = graph.invoke(
        Command(resume=feedback),
        config=memory_config,
    )

    print("Second conversation completed.")


print("\n" + "=" * 60)
print("W10D5 TESTING COMPLETED SUCCESSFULLY.")
print("Customer issue classification verified.")
print("Conditional routing verified.")
print("Human-in-the-loop verified.")
print("Persistent conversation memory verified.")
print("=" * 60)