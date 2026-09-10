# W10D5: Stateful Customer Support Agent

## Objective

Implement a stateful customer support agent using LangGraph with conditional routing, human-in-the-loop feedback, and persistent conversation memory.

## Technologies Used

- Python
- LangGraph
- MemorySaver
- Human-in-the-loop
- MLOps concepts

## Workflow

Customer Message → Classify → Route → Response → Human Review

## Features

### 1. Issue Classification

Customer messages are classified into:

- Billing
- Technical
- Order
- General

### 2. Conditional Routing

The classified customer issue is routed to the appropriate response node.

### 3. Customer Support Response

The agent provides a suitable response based on the customer's issue.

### 4. Human-in-the-Loop

The workflow pauses using LangGraph's `interrupt()` function.

A human reviews the response and provides feedback.

The workflow then resumes using `Command(resume=...)`.

### 5. Persistent Conversation Memory

`MemorySaver` is used as the LangGraph checkpointer.

A `thread_id` is used to maintain conversation state.

The persistent memory test verifies that the conversation can continue using previously stored state.

## Testing

Five customer-support cases were tested:

1. Billing issue
2. Technical/login issue
3. Delivery/order issue
4. Account issue
5. Refund issue

The persistent conversation test was also completed successfully.

## Result

The stateful customer support agent executed successfully.

Classification, conditional routing, human-in-the-loop interaction, workflow resume, and persistent conversation memory were verified successfully.
