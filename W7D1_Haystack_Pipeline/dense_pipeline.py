from pathlib import Path

from haystack.components.converters import PyPDFToDocument
from haystack_integrations.components.embedders.sentence_transformers import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder,
)
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.document_stores.in_memory import InMemoryDocumentStore


# ============================================================
# W7D1 - Dense Retrieval Pipeline
# ============================================================

PDF_FOLDER = Path("documents")


# ------------------------------------------------------------
# STEP 1: Find PDF files
# ------------------------------------------------------------

pdf_files = list(PDF_FOLDER.glob("*.pdf"))

print(f"Found {len(pdf_files)} PDF files")

if len(pdf_files) == 0:
    print("ERROR: No PDF files found.")
    print("Make sure the PDF files are inside the documents folder.")
    exit()


# ------------------------------------------------------------
# STEP 2: Convert PDFs
# ------------------------------------------------------------

converter = PyPDFToDocument()

documents = []

for pdf_file in pdf_files:

    print(f"Loading: {pdf_file.name}")

    result = converter.run(
        sources=[pdf_file]
    )

    documents.extend(result["documents"])


print(f"\nLoaded {len(documents)} PDF documents")


# ------------------------------------------------------------
# STEP 3: Create DocumentStore
# ------------------------------------------------------------

document_store = InMemoryDocumentStore()


# ------------------------------------------------------------
# STEP 4: Create document embedder
# ------------------------------------------------------------

print("\nLoading embedding model...")

document_embedder = SentenceTransformersDocumentEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document_embedder.warm_up()


# ------------------------------------------------------------
# STEP 5: Create embeddings
# ------------------------------------------------------------

print("Creating document embeddings...")

result = document_embedder.run(
    documents=documents
)

embedded_documents = result["documents"]


# ------------------------------------------------------------
# STEP 6: Store embedded documents
# ------------------------------------------------------------

document_store.write_documents(
    embedded_documents
)

print(
    f"Documents stored: "
    f"{document_store.count_documents()}"
)


# ------------------------------------------------------------
# STEP 7: Create dense retriever
# ------------------------------------------------------------

retriever = InMemoryEmbeddingRetriever(
    document_store=document_store
)


# ------------------------------------------------------------
# STEP 8: Create text embedder
# ------------------------------------------------------------

text_embedder = SentenceTransformersTextEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text_embedder.warm_up()

print("\nDense Retriever created successfully!")


# ------------------------------------------------------------
# STEP 9: Ten test questions
# ------------------------------------------------------------

questions = [
    "What is artificial intelligence?",
    "What is machine learning?",
    "What is deep learning?",
    "What is natural language processing?",
    "What is generative AI?",
    "What are the applications of artificial intelligence?",
    "What is supervised learning?",
    "What are neural networks?",
    "What is a large language model?",
    "How is generative AI different from traditional AI?",
]


# ------------------------------------------------------------
# STEP 10: Run dense retrieval
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("DENSE RETRIEVAL RESULTS")
print("=" * 70)


for i, question in enumerate(questions, start=1):

    print(f"\nQuestion {i}: {question}")

    # Convert question to embedding
    query_result = text_embedder.run(
        text=question
    )

    query_embedding = query_result["embedding"]

    # Retrieve documents
    result = retriever.run(
        query_embedding=query_embedding,
        top_k=3
    )

    retrieved_documents = result["documents"]

    print(
        f"Retrieved {len(retrieved_documents)} documents"
    )

    for rank, document in enumerate(
        retrieved_documents,
        start=1
    ):

        text = document.content.replace(
            "\n",
            " "
        )

        preview = text[:250]

        print(f"\n  Result {rank}:")
        print(f"  {preview}...")


print("\n")
print("=" * 70)
print("DENSE RETRIEVAL PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 70)
