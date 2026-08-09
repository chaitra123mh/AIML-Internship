import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

qa_pairs = [
    ("What is machine learning?", "Machine learning allows computers to learn from data."),
    ("What is artificial intelligence?", "AI enables machines to perform tasks requiring intelligence."),
    ("What is overfitting?", "Overfitting happens when a model learns training data too closely."),
    ("What is a REST API?", "A REST API allows applications to communicate over HTTP."),
    ("What is ChromaDB?", "ChromaDB is a vector database used for storing and searching embeddings.")
]

questions = [x[0] for x in qa_pairs]
answers = [x[1] for x in qa_pairs]

embeddings = model.encode(questions)

query = "Explain machine learning"

query_embedding = model.encode([query])[0]

similarities = np.dot(embeddings, query_embedding) / (
    np.linalg.norm(embeddings, axis=1) *
    np.linalg.norm(query_embedding)
)

best_index = np.argmax(similarities)
best_score = similarities[best_index]

print("=" * 60)
print("W5D6 SEMANTIC CACHE")
print("=" * 60)

print("Query:", query)
print("Best match:", questions[best_index])
print("Similarity:", round(float(best_score), 4))

if best_score >= 0.92:
    print("\nCACHE HIT")
    print("Cached answer:", answers[best_index])
else:
    print("\nCACHE MISS")
    print("LLM call required.")