# W10D4: Human-in-the-Loop with LangGraph

## Objective

Build and test a LangGraph workflow with conditional routing and a human-in-the-loop interrupt.

## Technologies Used

- Python
- LangGraph
- StateGraph
- Human-in-the-loop interrupt

## Workflow

The application contains these stages:

1. **Classify** – Identifies the input as technical or general.
2. **Route** – Selects the appropriate route based on classification.
3. **Respond** – Generates a response for the selected route.
4. **Human Review** – Pauses the workflow and waits for human feedback.

## Conditional Routing

Conditional edges are used after the route node.

- Technical input → Technical response
- General input → General response

## Human-in-the-Loop

LangGraph's `interrupt()` function pauses the workflow and requests human feedback.

After feedback is provided, `Command(resume=...)` resumes the workflow.

## Testing

The workflow was tested with five inputs:

1. How does Python work?
2. What is the weather today?
3. Explain SQL database.
4. Tell me a simple joke.
5. What is machine learning?

For each test, conditional routing and human feedback were verified.

## Result

The LangGraph workflow executed successfully.

Conditional routing was verified and the human-in-the-loop workflow successfully paused, received human feedback, and resumed.