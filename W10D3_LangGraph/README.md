# W10D3: LangGraph + Memory — Persistent Conversations

## Objective

The objective of this task is to implement a stateful LangGraph agent with persistent conversation memory and human-in-the-loop feedback.

## Technologies Used

- Python
- LangGraph
- LangGraph MemorySaver
- Human-in-the-loop interrupt
- TypedDict

## Implementation

The LangGraph workflow contains the following stages:

1. **Classify** – Classifies the user input as technical or general.
2. **Route** – Routes the request according to its classification.
3. **Respond** – Generates an appropriate response.
4. **Human Review** – Pauses the workflow and waits for human feedback before continuing.

## Persistent Memory

`MemorySaver` is used as the checkpointer for the LangGraph workflow.

A `thread_id` is used to maintain conversation state. Messages using the same thread can continue the same conversation.

## Human-in-the-Loop

The workflow uses LangGraph's `interrupt()` function to pause execution and request human feedback.

The workflow resumes using `Command(resume=...)` after human feedback is provided.

## Testing

The application was tested with five different inputs.

The following were verified:

- Classification of user inputs
- Correct routing
- Response generation
- Human feedback interruption
- Resuming the workflow after human feedback
- Conversation state using a thread ID

## Result

The LangGraph stateful agent executed successfully.

The human-in-the-loop workflow was tested successfully by pausing the graph, providing human feedback, and resuming execution.

## Deliverables

- `langgraph_memory.py` – LangGraph implementation
- `README.md` – Task documentation
- `self_review.md` – Self-review checklist
- `output.txt` – Test output evidence
- `output.png` – Screenshot evidence