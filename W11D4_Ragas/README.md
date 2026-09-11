# W11D4: RAG Evaluation with Ragas — Metrics & Benchmarks

## Objective

The objective of this task is to build a Retrieval-Augmented Generation (RAG) pipeline and evaluate its performance using Ragas metrics.

The implementation uses LangChain, ChromaDB, Ollama, and Ragas concepts to compare baseline and optimized retrieval performance.

---

## Technologies Used

- Python 3.12
- LangChain
- ChromaDB
- Ollama
- Ragas
- `nomic-embed-text`
- `llama3.2:3b`

---

## RAG Pipeline

The RAG pipeline follows these steps:

1. Load the knowledge base.
2. Split the document into smaller chunks.
3. Generate embeddings using Ollama.
4. Store embeddings in ChromaDB.
5. Retrieve relevant documents.
6. Prepare question-answer pairs.
7. Evaluate the RAG pipeline using Ragas metrics.
8. Change retrieval `k` to optimize performance.
9. Compare baseline and optimized results.

---

## Dataset

The project uses a local knowledge base stored in:

```text
knowledge_base.txt