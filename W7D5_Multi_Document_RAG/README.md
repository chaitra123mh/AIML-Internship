# W7D5: Week 7 Project - Multi-document RAG System

## Objective

Build a multi-document Retrieval-Augmented Generation (RAG) system using
LlamaIndex, ChromaDB, Ollama embeddings, and a local Ollama LLM.

## Technologies Used

- Python
- LlamaIndex
- ChromaDB
- Ollama
- nomic-embed-text
- llama3.2:3b

## System Architecture

Documents
    ↓
LlamaIndex
    ↓
Ollama Embeddings
    ↓
ChromaDB Vector Store
    ↓
Semantic Retrieval
    ↓
LlamaIndex Query Engine
    ↓
Ollama Local LLM
    ↓
Generated Answer + Source Documents

## Documents

Five text documents were used:

1. Artificial Intelligence
2. Machine Learning
3. Deep Learning
4. Natural Language Processing
5. Computer Vision

## Implementation

The `multi_document_rag.py` script:

1. Loads the five documents.
2. Creates embeddings using `nomic-embed-text`.
3. Stores document vectors in ChromaDB.
4. Creates a LlamaIndex VectorStoreIndex.
5. Creates a query engine.
6. Runs five questions.
7. Generates answers using `llama3.2:3b`.
8. Displays the source documents used for each answer.
9. Records query latency.
10. Saves the results as output evidence.

## Models

Embedding Model:

`nomic-embed-text`

LLM:

`llama3.2:3b`

## Testing

Five questions were tested covering:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Natural Language Processing
- Computer Vision

The system successfully retrieves relevant information from the indexed
documents and generates answers using the local LLM.

## Output Evidence

Query results are saved in:

`outputs/rag_results.txt`

Screenshots of successful execution are stored in:

`Screenshots/`

## Key Design Decisions

- LlamaIndex was used for document indexing and query orchestration.
- ChromaDB was used as the persistent vector store.
- Ollama was used to keep embedding and LLM inference local.
- `nomic-embed-text` was used for document embeddings.
- `llama3.2:3b` was used for local answer generation.
- Source documents were displayed to improve answer traceability.

## Conclusion

The project demonstrates a complete local multi-document RAG workflow.
The system retrieves relevant information from multiple documents and uses
a local LLM to generate answers based on the retrieved information.

## Self-Review Checklist

- [x] Multi-document RAG system implemented
- [x] Five documents loaded
- [x] Ollama embeddings configured
- [x] ChromaDB vector store configured
- [x] LlamaIndex VectorStoreIndex created
- [x] Query engine created
- [x] Five queries tested
- [x] Source documents verified
- [x] Output evidence generated
- [x] Code documented
- [ ] CIA Mentor Mode interaction 1 completed
- [ ] CIA Mentor Mode interaction 2 completed
- [ ] Git commit 1 completed
- [ ] Git commit 2 completed
- [ ] Branch pushed
- [ ] Pull Request created

## Viva Preparation

### 1. Explain what you built today and why you made your key design decisions.

I built a multi-document RAG system using LlamaIndex, ChromaDB, Ollama
embeddings, and a local llama3.2:3b model. ChromaDB was selected as the
vector store for efficient similarity-based retrieval, while Ollama allowed
the LLM and embeddings to run locally.

### 2. What was the hardest part? How did you solve it?

The challenging part was integrating the document indexing, vector store,
embeddings, and local LLM into one pipeline. I solved this by configuring
each component separately and then connecting them through LlamaIndex.

### 3. If you had one more day, what would you improve?

I would improve retrieval evaluation, add more documents and queries, measure
retrieval quality using Ragas, and improve the user interface for interacting
with the RAG system.