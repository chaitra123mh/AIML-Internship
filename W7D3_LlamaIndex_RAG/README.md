# W7D3: LlamaIndex — Document Indexing & Querying

## Objective

Implement document indexing and querying using LlamaIndex with Ollama embeddings and compare a basic VectorStoreIndex with ChromaDB.

## Technologies

- Python
- LlamaIndex
- Ollama
- nomic-embed-text
- Qwen 2.5 3B
- ChromaDB

## Documents

Five text documents were used:

1. Artificial Intelligence
2. Machine Learning
3. Deep Learning
4. Natural Language Processing
5. Computer Vision

## Task 1: LlamaIndex VectorStoreIndex

Documents were loaded using SimpleDirectoryReader and indexed using LlamaIndex VectorStoreIndex.

Ollama `nomic-embed-text` was used for embeddings.

A LlamaIndex QueryEngine was created and 10 queries were executed.

Results were saved in:

`outputs/query_results.txt`

## Task 2: LlamaIndex + ChromaDB

ChromaDB was connected as the vector store using ChromaVectorStore.

The same 10 queries were executed again.

Results were saved in:

`outputs/chroma_query_results.txt`

## Latency Comparison

| Pipeline | Number of Queries | Average Latency |
|---|---:|---:|
| LlamaIndex VectorStoreIndex | 10 | 126.12 seconds |
| LlamaIndex + ChromaDB | 10 | 59.20 seconds |


## Verification

The answers were verified against the source text documents.

The query results also display the source documents retrieved by LlamaIndex.

## Conclusion

LlamaIndex successfully indexed the text documents and provided a working query engine.

ChromaDB was successfully integrated as the vector store, and the same queries were executed to compare retrieval performance.

## Files

- `Llamaindex_basics.py` — Basic LlamaIndex indexing and querying
- `Llamaindex_chroma.py` — LlamaIndex with ChromaDB
- `documents/` — Source text documents
- `outputs/query_results.txt` — Basic pipeline results
- `outputs/chroma_query_results.txt` — ChromaDB results