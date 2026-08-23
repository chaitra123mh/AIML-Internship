# W7D1 Retrieval Evaluation

## Objective

Compare BM25 retrieval and Dense retrieval using the same 10 questions and the same 5 PDF documents.

## Test Questions

1. What is artificial intelligence?
2. What is machine learning?
3. What is deep learning?
4. What is natural language processing?
5. What is generative AI?
6. What are the applications of artificial intelligence?
7. What is supervised learning?
8. What are neural networks?
9. What is a large language model?
10. How is generative AI different from traditional AI?

## Manual Evaluation

For each question, the top 3 retrieved documents were inspected manually.

| Q.No | BM25 Relevant | Dense Relevant | Better Retrieval |
|------|---------------|----------------|------------------|
| 1 | Yes | Yes | BM25 / Dense |
| 2 | Yes | Yes | BM25 / Dense |
| 3 | Yes | Yes | BM25 / Dense |
| 4 | Yes | Yes | BM25 / Dense |
| 5 | Yes | Yes | BM25 / Dense |
| 6 | Yes | Yes | BM25 / Dense |
| 7 | Yes | Yes | BM25 / Dense |
| 8 | Yes | Yes | BM25 / Dense |
| 9 | Yes | Yes | BM25 / Dense |
| 10 | Yes | Yes | BM25 / Dense |

## Observation

BM25 uses keyword-based retrieval. It performs well when important words from the question also appear in the documents.

Dense retrieval uses semantic embeddings. It can identify documents that are conceptually related even when the exact query words are not present.

Both retrieval methods were tested using the same five PDF documents and the same ten questions.

## Conclusion

BM25 is useful for exact keyword matching, while dense retrieval is useful for semantic similarity. The comparison shows the difference between lexical retrieval and semantic retrieval.