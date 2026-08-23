from pathlib import Path

from haystack.components.converters import PyPDFToDocument
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore


# ============================================================
# W7D2 - BM25 Retrieval Pipeline
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
# STEP 2: Convert PDFs to Haystack Documents
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

document_store.write_documents(documents)

print(
    f"Documents stored: "
    f"{document_store.count_documents()}"
)


# ------------------------------------------------------------
# STEP 4: Create BM25 Retriever
# ------------------------------------------------------------

retriever = InMemoryBM25Retriever(
    document_store=document_store
)

print("\nBM25 Retriever created successfully!")


# ------------------------------------------------------------
# STEP 5: Ten Questions
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
# STEP 6: Run BM25 Retrieval
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("W7D2 - BM25 RETRIEVAL RESULTS")
print("=" * 70)


for i, question in enumerate(questions, start=1):

    print(f"\nQuestion {i}: {question}")

    result = retriever.run(
        query=question,
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
print("W7D2 BM25 PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 70)