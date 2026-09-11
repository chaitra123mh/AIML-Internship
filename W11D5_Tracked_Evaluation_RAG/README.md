# W11D5: Tracked & Evaluated RAG Pipeline

## Objective

The objective of W11D5 is to implement an integrated RAG pipeline using the approved AI/ML stack:

- CrewAI
- LangGraph
- MLflow
- Ragas
- MLOps

## Implementation

The project integrates the following components:

### CrewAI
A RAG research agent is used to review the generated answer.

### LangGraph
LangGraph controls the RAG workflow using two nodes:

1. Retrieve
2. Generate

### ChromaDB

ChromaDB stores document embeddings and retrieves relevant knowledge from the knowledge base.

### Ollama

The local `nomic-embed-text` model is used for embeddings and `llama3.2:3b` is used as the language model.

### MLflow

MLflow tracks:

- Chunk size
- Chunk overlap
- Retrieval k
- Embedding model
- LLM model
- Answer length

## RAG Workflow

```text
Knowledge Base
      |
      v
Document Chunking
      |
      v
Ollama Embeddings
      |
      v
ChromaDB
      |
      v
LangGraph
      |
      +--> Retrieve
      |
      +--> Generate
      |
      v
Generated Answer
      |
      v
CrewAI Quality Review
      |
      v
MLflow Tracking
## Final Review

W11D5 integrates RAG workflow concepts with retrieval, evaluation, experiment tracking, optimization, and MLOps practices. The implementation was tested successfully and output evidence was recorded.

Status: Completed successfully.