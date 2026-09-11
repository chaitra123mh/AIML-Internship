# W11D4 Self Review

## Task
RAG Evaluation with Ragas — Metrics & Benchmarks

## What I Implemented

- Built a RAG pipeline using LangChain and ChromaDB.
- Loaded the knowledge base from `knowledge_base.txt`.
- Split the knowledge base into document chunks.
- Created embeddings using Ollama `nomic-embed-text`.
- Created a ChromaDB vector store.
- Prepared 10 question-answer pairs.
- Evaluated the RAG pipeline using:
  - Faithfulness
  - Answer Relevancy
  - Context Precision
  - Context Recall
- Compared baseline retrieval with optimized retrieval.
- Changed retrieval `k` from 2 to 4 for optimization.
- Recorded the output as evidence.

## What I Learned

I learned how RAG systems retrieve relevant information from a knowledge base and how retrieval quality can be evaluated using different metrics.

I also learned that changing the retrieval `k` value can affect the quality of retrieved context and the final RAG performance.

## Optimization

The baseline configuration used:

`k = 2`

The optimized configuration used:

`k = 4`

The optimized configuration showed better evaluation results in the recorded output.

## Challenges

- Setting up the required LangChain and ChromaDB packages.
- Configuring the local Ollama embedding model.
- Understanding Ragas evaluation metrics.
- Reducing evaluation time for faster execution.

## Final Status

The W11D4 RAG evaluation task was completed successfully.

The implementation includes the RAG pipeline, 10 Q&A pairs, evaluation metrics, optimization comparison, output evidence, and documentation.