import os
import time
import chromadb

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    Settings,
)

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore


# =========================================================
# CONFIGURATION
# =========================================================

DOCUMENT_DIR = "documents"
CHROMA_DIR = "chroma_db"

EMBED_MODEL = "nomic-embed-text"


# =========================================================
# OLLAMA EMBEDDING CONFIGURATION
# =========================================================

Settings.embed_model = OllamaEmbedding(
    model_name=EMBED_MODEL,
    base_url="http://localhost:11434"
)


# =========================================================
# LOAD DOCUMENTS
# =========================================================

documents = SimpleDirectoryReader(DOCUMENT_DIR).load_data()

print("=" * 70)
print("W7D5 - MULTI-DOCUMENT RAG SYSTEM")
print("=" * 70)

print(f"\nLoaded documents: {len(documents)}")

for document in documents:
    print(
        "-",
        os.path.basename(
            document.metadata.get("file_name", "unknown")
        )
    )


# =========================================================
# CREATE CHROMADB VECTOR STORE
# =========================================================

chroma_client = chromadb.PersistentClient(
    path=CHROMA_DIR
)

collection = chroma_client.get_or_create_collection(
    name="w7d5_multidocument_rag"
)

vector_store = ChromaVectorStore(
    chroma_collection=collection
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)


# =========================================================
# CREATE VECTOR INDEX
# =========================================================

print("\nCreating vector index...")

index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)

print("Vector index created successfully.")


# =========================================================
# CREATE RETRIEVER
# =========================================================

retriever = index.as_retriever(
    similarity_top_k=1
)

print("Retriever created successfully.")


# =========================================================
# TEST QUESTIONS
# =========================================================

questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is Natural Language Processing?",
    "What is Computer Vision?"
]


# =========================================================
# RUN RETRIEVAL
# =========================================================

results = []

for number, question in enumerate(questions, start=1):

    print("\n" + "-" * 70)
    print(f"QUESTION {number}: {question}")

    start_time = time.time()

    nodes = retriever.retrieve(question)

    latency = time.time() - start_time

    print("\nRetrieved Source:")

    source_names = set()

    for node in nodes:

        file_name = node.node.metadata.get(
            "file_name",
            "Unknown document"
        )

        source_name = os.path.basename(file_name)

        source_names.add(source_name)

        print(f"- {source_name}")

        print("\nRetrieved Content:")
        print(node.node.get_content()[:500])

    print(f"\nRetrieval latency: {latency:.2f} seconds")

    results.append(
        f"""
Question {number}: {question}

Retrieved Source Documents:
{chr(10).join('- ' + source for source in sorted(source_names))}

Retrieved Content:
{nodes[0].node.get_content()[:500] if nodes else 'No relevant content found.'}

Retrieval Latency:
{latency:.2f} seconds

{'-' * 70}
"""
    )


# =========================================================
# SAVE OUTPUT EVIDENCE
# =========================================================

os.makedirs("outputs", exist_ok=True)

output_file = "outputs/rag_results.txt"

with open(output_file, "w", encoding="utf-8") as file:

    file.write("W7D5 - Multi-document RAG System\n")
    file.write("=" * 70 + "\n")

    file.write(f"\nEmbedding Model: {EMBED_MODEL}")
    file.write(f"\nDocuments Loaded: {len(documents)}\n")

    file.write("\n".join(results))


# =========================================================
# COMPLETION MESSAGE
# =========================================================

print("\n" + "=" * 70)
print("ALL 5 RAG QUERIES COMPLETED SUCCESSFULLY")
print(f"Output saved to: {output_file}")
print("=" * 70)