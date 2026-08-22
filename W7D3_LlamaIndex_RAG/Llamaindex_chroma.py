from pathlib import Path
import time

import chromadb

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    Settings
)

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

from llama_index.vector_stores.chroma import ChromaVectorStore


# --------------------------------------------------
# 1. Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).parent
DOCUMENTS_DIR = BASE_DIR / "documents"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 2. Configure Ollama
# --------------------------------------------------

Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text",
    base_url="http://localhost:11434"
)

Settings.llm = Ollama(
    model="qwen2.5:3b",
    base_url="http://localhost:11434",
    request_timeout=600.0
)


# --------------------------------------------------
# 3. Load documents
# --------------------------------------------------

documents = SimpleDirectoryReader(
    input_dir=str(DOCUMENTS_DIR)
).load_data()

print(f"Loaded {len(documents)} documents.")


# --------------------------------------------------
# 4. Create ChromaDB client
# --------------------------------------------------

chroma_client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

chroma_collection = chroma_client.get_or_create_collection(
    name="w7d3_documents"
)

print("ChromaDB collection created successfully.")


# --------------------------------------------------
# 5. Connect ChromaDB with LlamaIndex
# --------------------------------------------------

vector_store = ChromaVectorStore(
    chroma_collection=chroma_collection
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)


# --------------------------------------------------
# 6. Create VectorStoreIndex
# --------------------------------------------------

index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)

print("LlamaIndex + ChromaDB index created successfully.")


# --------------------------------------------------
# 7. Create Query Engine
# --------------------------------------------------

query_engine = index.as_query_engine(
    similarity_top_k=2
)

print("ChromaDB query engine created successfully.")


# --------------------------------------------------
# 8. Ten test queries
# --------------------------------------------------

queries = [
    "What is Artificial Intelligence?",
    "What are the main types of Machine Learning?",
    "What is Deep Learning?",
    "What is Natural Language Processing?",
    "What is Computer Vision?",
    "What are some applications of Artificial Intelligence?",
    "What is supervised learning?",
    "Why are transformer models important in NLP?",
    "What are Convolutional Neural Networks used for?",
    "What are some applications of Computer Vision?"
]


# --------------------------------------------------
# 9. Run queries and measure latency
# --------------------------------------------------

output_file = OUTPUTS_DIR / "chroma_query_results.txt"

latencies = []

with open(output_file, "w", encoding="utf-8") as f:

    f.write("W7D3 LlamaIndex + ChromaDB Query Results\n")
    f.write("=" * 60 + "\n\n")

    for i, question in enumerate(queries, start=1):

        print(f"\n{'=' * 60}")
        print(f"ChromaDB Query {i}/10")
        print(f"Question: {question}")

        start_time = time.perf_counter()

        response = query_engine.query(question)

        latency = time.perf_counter() - start_time
        latencies.append(latency)

        print(f"Answer: {response}")
        print(f"Latency: {latency:.2f} seconds")

        print("Source documents:")

        source_files = []

        for source in response.source_nodes:

            file_name = source.node.metadata.get(
                "file_name",
                "Unknown"
            )

            if file_name not in source_files:
                source_files.append(file_name)

            print(f"- {file_name}")

        # Save results
        f.write(f"Query {i}\n")
        f.write(f"Question: {question}\n")
        f.write(f"Answer: {response}\n")
        f.write(f"Latency: {latency:.2f} seconds\n")
        f.write("Source documents:\n")

        for file_name in source_files:
            f.write(f"- {file_name}\n")

        f.write("\n" + "-" * 60 + "\n\n")

    # Average latency
    average_latency = sum(latencies) / len(latencies)

    f.write(f"\nAverage ChromaDB latency: {average_latency:.2f} seconds\n")

print("\nAll 10 ChromaDB queries completed successfully.")

print(
    f"Average ChromaDB latency: "
    f"{sum(latencies) / len(latencies):.2f} seconds"
)

print(f"Results saved to: {output_file}")