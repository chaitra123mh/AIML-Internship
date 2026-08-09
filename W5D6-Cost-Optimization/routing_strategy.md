# W5D6 Model Routing Strategy

## Local Model

Use Ollama llama3.2:3b for:
- Simple questions
- Basic explanations
- Short summaries
- General AI/ML questions

## API Model

Use a cloud API for:
- Complex reasoning
- Long documents
- High-quality generation
- Tasks requiring stronger model capability

## Routing Rule

Simple queries → Local LLM

Complex queries → Cloud API

This strategy reduces API usage and helps control inference cost.