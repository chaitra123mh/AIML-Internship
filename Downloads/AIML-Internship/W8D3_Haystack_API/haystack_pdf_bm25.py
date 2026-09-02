from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever

# Create document store
document_store = InMemoryDocumentStore()

# PDF converter
converter = PyPDFToDocument()

# Document writer
writer = DocumentWriter(document_store=document_store)

# BM25 retriever
retriever = InMemoryBM25Retriever(
    document_store=document_store,
    top_k=3
)

# Create indexing pipeline
indexing_pipeline = Pipeline()

indexing_pipeline.add_component("converter", converter)
indexing_pipeline.add_component("writer", writer)

indexing_pipeline.connect("converter.documents", "writer.documents")

# PDF files
pdf_files = [
    "ai.pdf",
    "machine_learning.pdf",
    "deep_learning.pdf",
    "nlp.pdf",
    "computer_vision.pdf"
]

# Run indexing
for pdf_file in pdf_files:
    indexing_pipeline.run(
        {"converter": {"sources": [pdf_file]}}
    )

print("5 PDF documents indexed successfully!")

# Test BM25 retrieval
query = "What is Machine Learning?"

result = retriever.run(query=query)

print("\nQuery:", query)
print("\nBM25 Results:")

for i, document in enumerate(result["documents"], 1):
    print(f"\nResult {i}:")
    print(document.content)