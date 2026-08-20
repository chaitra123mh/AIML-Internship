# W7D1 - Haystack Pipeline Architecture

## Objective

Build and compare BM25 and Dense retrieval pipelines using Haystack.

## Technologies

- Python
- Haystack 3.0.0
- Sentence Transformers
- InMemoryDocumentStore
- BM25 Retriever
- Dense Embedding Retriever

## Project Structure

W7D1_Haystack_Pipeline/

├── documents/
│   ├── 01_Artificial_Intelligence.pdf
│   ├── 02_Machine_Learning.pdf
│   ├── 03_Deep_Learning.pdf
│   ├── 04_Natural_Language_Processing.pdf
│   └── 05_Generative_AI.pdf
│
├── bm25_pipeline.py
├── dense_pipeline.py
├── evaluation.md
├── self_review.md
└── README.md

## Pipeline 1 - BM25

PDF Documents
→ PyPDFToDocument
→ InMemoryDocumentStore
→ InMemoryBM25Retriever
→ Retrieved Documents

## Pipeline 2 - Dense Retrieval

PDF Documents
→ PyPDFToDocument
→ Sentence Transformers
→ InMemoryDocumentStore
→ InMemoryEmbeddingRetriever
→ Retrieved Documents

## Documents

Five PDF documents were used:

1. Artificial Intelligence
2. Machine Learning
3. Deep Learning
4. Natural Language Processing
5. Generative AI

## Evaluation

Both BM25 and Dense retrieval were tested using the same 10 questions.

BM25 performs keyword-based retrieval, while Dense retrieval uses semantic similarity through embeddings.

The retrieval results were manually inspected and compared.

## How to Run

### BM25

```bash
python bm25_pipeline.py