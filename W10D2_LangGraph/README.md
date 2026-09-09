# W10D2: LangGraph State Machines & Conditional Edges

## Objective

Build and test a LangGraph state machine using conditional edges,
routing logic, and human-in-the-loop interruption.

## Implementation

The workflow contains:

1. Classify node
2. Route node
3. Technical response node
4. General response node
5. Human review node

## Workflow

User Input → Classify → Route → Response → Human Review → End

## Conditional Routing

Technical inputs are routed to the technical response node.

General inputs are routed to the general response node.

## Human-in-the-Loop

The graph uses LangGraph `interrupt()` to pause execution for
human review. The workflow is resumed using `Command(resume=...)`.

## Testing

Five different inputs were tested to verify classification and routing.

## Result

The LangGraph state machine successfully classified inputs,
selected the appropriate route, paused for human review,
and resumed execution after receiving human input.

## Self-Review Checklist

- [x] LangGraph state machine created
- [x] Classification implemented
- [x] Conditional edges implemented
- [x] Five inputs tested
- [x] Human-in-the-loop interrupt implemented
- [x] Human resume tested
- [x] Output evidence captured
- [x] Code reviewed