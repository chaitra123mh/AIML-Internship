from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack_integrations.components.embedders.sentence_transformers import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder
)
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever

# Create document store
document_store = InMemoryDocumentStore(embedding_similarity_function="cosine")

# PDF converter and writer
converter = PyPDFToDocument()
writer = DocumentWriter(document_store=document_store)

pdf_files = [
    "ai.pdf",
    "machine_learning.pdf",
    "deep_learning.pdf",
    "nlp.pdf",
    "computer_vision.pdf"
]

# Load PDFs
all_documents = []

for pdf_file in pdf_files:
    result = converter.run(sources=[pdf_file])
    all_documents.extend(result["documents"])

# Create document embeddings
document_embedder = SentenceTransformersDocumentEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document_embedder.warm_up()

embedded_documents = document_embedder.run(
    documents=all_documents
)

# Store documents with embeddings
writer.run(documents=embedded_documents["documents"])

# Create text embedder
text_embedder = SentenceTransformersTextEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text_embedder.warm_up()

# Dense retriever
retriever = InMemoryEmbeddingRetriever(
    document_store=document_store,
    top_k=1
)

# Test query
query = "What is Machine Learning?"

query_embedding = text_embedder.run(text=query)

result = retriever.run(
    query_embedding=query_embedding["embedding"]
)

print("========== DENSE RETRIEVER ==========")
print("Query:", query)

for i, document in enumerate(result["documents"], 1):
    print(f"\nResult {i}:")
    print(document.content)