from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever

# Create document store
document_store = InMemoryDocumentStore()

# Converter and writer
converter = PyPDFToDocument()
writer = DocumentWriter(document_store=document_store)

# PDF files
pdf_files = [
    "ai.pdf",
    "machine_learning.pdf",
    "deep_learning.pdf",
    "nlp.pdf",
    "computer_vision.pdf"
]

# Index PDFs
for pdf_file in pdf_files:
    documents = converter.run(sources=[pdf_file])
    writer.run(documents=documents["documents"])

# BM25 retriever
retriever = InMemoryBM25Retriever(
    document_store=document_store,
    top_k=1
)

# 10 questions
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

print("========== BM25 EVALUATION ==========")

for i, question in enumerate(questions, 1):
    result = retriever.run(query=question)
    documents = result["documents"]

    print(f"\nQuestion {i}: {question}")

    if documents:
        print("Retrieved document:")
        print(documents[0].content)
    else:
        print("No document retrieved.")