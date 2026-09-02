# W8D5: Local AI Research Assistant

## Objective

The objective of this project is to build a simple local AI research
assistant using an AI/ML workflow.

## Technologies Used

- Python
- LangGraph
- Ollama
- Llama 3.2:3b
- ChromaDB

## Architecture

User Question
      |
      v
Information Retrieval
      |
      v
Local Ollama LLM
      |
      v
Generated Research Answer

## Key Features

- Runs AI inference locally using Ollama.
- Uses LangGraph to manage the workflow.
- Retrieves relevant research information.
- Generates a simple research answer.
- Saves the generated output in output.txt.
- Includes unit tests.

## Testing

Three unit tests were created to verify information retrieval for:

1. Artificial Intelligence
2. Machine Learning
3. Natural Language Processing

All tests passed successfully.

## Conclusion

The Local AI Research Assistant demonstrates how LangGraph and
local LLM inference can be combined to create a simple research
assistant without depending on a cloud-based AI model.