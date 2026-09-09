# W10D1: LangGraph — Stateful Agent Graphs

## Objective

Build a stateful LangGraph agent with classification, conditional routing, and human-in-the-loop approval.

## Graph Architecture

The graph follows:

START → classify → route → response → END

The response path is selected using conditional routing.

## Nodes

1. **classify**

   * Classifies the user input as technical, general, or human_review.

2. **route**

   * Determines which response node should process the request.

3. **technical_response**

   * Handles technical and programming-related questions.

4. **general_response**

   * Handles general questions.

5. **human_review**

   * Pauses execution and requests human approval.

## Conditional Routing

The graph uses conditional edges after the route node.

* technical → technical_response
* general → general_response
* human_review → human_review

## Human-in-the-Loop

The `interrupt()` function pauses graph execution when human approval is required.

The graph is resumed using `Command(resume=decision)`.

## Testing

Five test cases were performed.

1. Python question → technical route
2. General knowledge question → general route
3. Docker question → technical route
4. General question → general route
5. Account approval request → human review → interrupt → human approval → resume

## Result

The LangGraph workflow successfully demonstrated:

* Stateful graph execution
* Multiple nodes
* Conditional routing
* Human-in-the-loop interruption
* Resume after human input
* Checkpoint-based state persistence

## Self-Review

* [x] Three-node LangGraph workflow implemented
* [x] Conditional routing implemented
* [x] Five test inputs tested
* [x] Human-in-the-loop interrupt tested
* [x] Graph successfully resumed after human input
* [x] Output evidence captured
* [x] Code reviewed before commit
* [x] Git branch created
* [x] Minimum two commits planned
* [ ] Pull request raised
