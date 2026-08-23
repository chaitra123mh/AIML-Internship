import chromadb

print("W6D4 - RAG Pipeline with ChromaDB")

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="w6d4_rag"
)

documents = [
    "Artificial Intelligence enables machines to perform intelligent tasks.",
    "Machine Learning allows computers to learn from data.",
    "Deep Learning uses neural networks with multiple layers.",
    "Python is widely used for artificial intelligence.",
    "RAG combines retrieval with language generation.",
    "ChromaDB is a vector database.",
    "Embeddings represent text as numerical vectors.",
    "Semantic search finds documents by meaning.",
    "LangChain helps build LLM applications.",
    "Ollama runs language models locally.",
    "Natural Language Processing works with human language.",
    "Supervised learning uses labelled data.",
    "Unsupervised learning finds patterns in data.",
    "Classification predicts categories.",
    "Regression predicts numerical values.",
    "Vector databases store embeddings.",
    "Cosine similarity compares vector directions.",
    "Retrieval finds relevant information.",
    "A chatbot can use RAG to answer questions.",
    "RAG can reduce hallucinations by using retrieved context."
]

ids = [f"doc{i}" for i in range(20)]

collection.add(
    documents=documents,
    ids=ids
)

print("\n20 documents added successfully.")

result = collection.query(
    query_texts=["What is RAG?"],
    n_results=3
)

print("\nTop 3 Similar Results:")
for doc in result["documents"][0]:
    print("-", doc)

print("\nMetadata filtering example:")

collection.add(
    documents=["Python is useful for AI applications."],
    ids=["python_doc"],
    metadatas=[{"topic": "AI"}]
)

filtered = collection.get(
    where={"topic": "AI"}
)

print(filtered["documents"])

print("\nRAG pipeline completed successfully!")
from PyPDF2 import PdfReader
import requests

print("\nPDF + Ollama RAG")

reader = PdfReader("sample.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text() or ""

chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

print("PDF loaded.")
print("Top 3 chunks retrieved:")

top_chunks = chunks[:3]

for i, chunk in enumerate(top_chunks, 1):
    print(f"\nChunk {i}:", chunk[:200])

context = "\n".join(top_chunks)

prompt = f"""Answer the question using the following PDF context.

Context:
{context}

Question: What is the main topic of this document?
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }
)

print("\nOllama Answer:")
print(response.json())
