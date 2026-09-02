from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack import Document


# Create document store
document_store = InMemoryDocumentStore()

# Sample documents
documents = [
    Document(content="Artificial Intelligence enables computers to perform tasks that normally require human intelligence."),
    Document(content="Machine Learning is a subset of Artificial Intelligence that learns patterns from data."),
    Document(content="Deep Learning uses neural networks with multiple layers to learn complex patterns."),
    Document(content="Natural Language Processing helps computers understand and process human language."),
    Document(content="Computer Vision enables computers to understand and analyze images and videos.")
]

# Write documents to document store
document_store.write_documents(documents)

# Create BM25 retriever
retriever = InMemoryBM25Retriever(document_store=document_store, top_k=3)

# Create pipeline
pipeline = Pipeline()
pipeline.add_component("retriever", retriever)

# Connect and run a test query
query = "What is Machine Learning?"

result = pipeline.run({
    "retriever": {
        "query": query
    }
})

print("\nW8D3 Haystack BM25 Pipeline")
print("=" * 35)
print("Question:", query)
print("\nRetrieved Documents:")

for i, doc in enumerate(result["retriever"]["documents"], 1):
    print(f"{i}. {doc.content}")