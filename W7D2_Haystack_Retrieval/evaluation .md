# W7D2 Retrieval Evaluation

## Objective

Compare BM25 retrieval and Dense retrieval using the same 5 PDF documents and the same 10 questions.

## Retrieval Methods

### BM25

BM25 is a keyword-based retrieval method. It ranks documents based on the occurrence and importance of query terms.

### Dense Retrieval

Dense retrieval uses sentence embeddings to find documents based on semantic similarity.

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

## Manual Comparison

| Q.No | BM25 Relevant | Dense Relevant | Observation |
|---|---|---|---|
| 1 | Yes | Yes | Both retrieved relevant information |
| 2 | Yes | Yes | Both retrieved relevant information |
| 3 | Yes | Yes | Both retrieved relevant information |
| 4 | Yes | Yes | Both retrieved relevant information |
| 5 | Yes | Yes | Both retrieved relevant information |
| 6 | Yes | Yes | Both retrieved relevant information |
| 7 | Yes | Yes | Both retrieved relevant information |
| 8 | Yes | Yes | Both retrieved relevant information |
| 9 | Yes | Yes | Both retrieved relevant information |
| 10 | Yes | Yes | Both retrieved relevant information |

## Observations

BM25 performs keyword-based matching and works well when the important terms in the question appear in the documents.

Dense retrieval uses embeddings and focuses on semantic similarity. It can retrieve conceptually related information even when the exact words differ.

Both methods were tested using the same documents and questions for a fair comparison.

## Conclusion

The experiment demonstrates the difference between lexical retrieval using BM25 and semantic retrieval using Dense embeddings.

BM25 is useful for exact keyword matching, while Dense retrieval is useful for understanding the semantic meaning of queries.