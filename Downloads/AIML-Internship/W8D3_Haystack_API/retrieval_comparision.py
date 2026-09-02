from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack.components.retrievers.in_memory import (
    InMemoryBM25Retriever,
    InMemoryEmbeddingRetriever
)
from haystack_integrations.components.embedders.sentence_transformers import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder
)

# -----------------------------
# 1. Create document store
# -----------------------------
document_store = InMemoryDocumentStore(
    embedding_similarity_function="cosine"
)

converter = PyPDFToDocument()
writer = DocumentWriter(document_store=document_store)

pdf_files = [
    "documents/ai.pdf",
    "documents/machine_learning.pdf",
    "documents/deep_learning.pdf",
    "documents/nlp.pdf",
    "documents/computer_vision.pdf"
]

# -----------------------------
# 2. Load PDFs
# -----------------------------
all_documents = []

for pdf_file in pdf_files:
    result = converter.run(sources=[pdf_file])
    all_documents.extend(result["documents"])

# -----------------------------
# 3. Create embeddings
# -----------------------------
document_embedder = SentenceTransformersDocumentEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document_embedder.warm_up()

embedded = document_embedder.run(
    documents=all_documents
)

writer.run(documents=embedded["documents"])

# -----------------------------
# 4. Create retrievers
# -----------------------------
bm25 = InMemoryBM25Retriever(
    document_store=document_store,
    top_k=1
)

dense = InMemoryEmbeddingRetriever(
    document_store=document_store,
    top_k=1
)

text_embedder = SentenceTransformersTextEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text_embedder.warm_up()

# -----------------------------
# 5. Ten questions
# -----------------------------
questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is Natural Language Processing?",
    "What is Computer Vision?",
    "What field helps computers understand human language?",
    "What technique uses neural networks with multiple layers?",
    "What allows computers to learn patterns from data?",
    "What enables computers to analyze images and videos?",
    "What is a branch of Artificial Intelligence?"
]

# Expected correct documents
expected = [
    "ai.pdf",
    "machine_learning.pdf",
    "deep_learning.pdf",
    "nlp.pdf",
    "computer_vision.pdf",
    "nlp.pdf",
    "deep_learning.pdf",
    "machine_learning.pdf",
    "computer_vision.pdf",
    "machine_learning.pdf"
]

bm25_correct = 0
dense_correct = 0

print("========== BM25 vs DENSE RETRIEVAL ==========")

for i, (question, expected_file) in enumerate(
    zip(questions, expected), 1
):

    # BM25
    bm25_result = bm25.run(query=question)
    bm25_doc = bm25_result["documents"][0]

    # Dense
    query_embedding = text_embedder.run(text=question)

    dense_result = dense.run(
        query_embedding=query_embedding["embedding"]
    )

    dense_doc = dense_result["documents"][0]

    bm25_file = bm25_doc.meta.get("file_path", "")
    dense_file = dense_doc.meta.get("file_path", "")

    bm25_match = expected_file in bm25_file
    dense_match = expected_file in dense_file

    if bm25_match:
        bm25_correct += 1

    if dense_match:
        dense_correct += 1

    print(f"\nQuestion {i}: {question}")
    print(f"Expected: {expected_file}")
    print(f"BM25:   {bm25_file}")
    print(f"Dense:  {dense_file}")

# -----------------------------
# 6. Precision
# -----------------------------
bm25_precision = bm25_correct / len(questions)
dense_precision = dense_correct / len(questions)

print("\n========== FINAL COMPARISON ==========")
print(f"BM25 Correct: {bm25_correct}/10")
print(f"BM25 Precision: {bm25_precision:.2f}")

print(f"Dense Correct: {dense_correct}/10")
print(f"Dense Precision: {dense_precision:.2f}")