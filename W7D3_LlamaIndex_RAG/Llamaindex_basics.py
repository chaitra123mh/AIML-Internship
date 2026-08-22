from pathlib import Path
import time

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings
)
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama


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
# 4. Create VectorStoreIndex
# --------------------------------------------------

index = VectorStoreIndex.from_documents(documents)

print("LlamaIndex VectorStoreIndex created successfully.")


# --------------------------------------------------
# 5. Create Query Engine
# --------------------------------------------------

query_engine = index.as_query_engine(
    similarity_top_k=2
)

print("Query engine created successfully.")


# --------------------------------------------------
# 6. Ten test queries
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
# 7. Run queries and save results
# --------------------------------------------------

output_file = OUTPUTS_DIR / "query_results.txt"

with open(output_file, "w", encoding="utf-8") as f:

    f.write("W7D3 LlamaIndex Query Results\n")
    f.write("=" * 60 + "\n\n")

    for i, question in enumerate(queries, start=1):

        print(f"\n{'=' * 60}")
        print(f"Query {i}/10")
        print(f"Question: {question}")

        start_time = time.perf_counter()

        response = query_engine.query(question)

        latency = time.perf_counter() - start_time

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

        # Save evidence
        f.write(f"Query {i}\n")
        f.write(f"Question: {question}\n")
        f.write(f"Answer: {response}\n")
        f.write(f"Latency: {latency:.2f} seconds\n")
        f.write("Source documents:\n")

        for file_name in source_files:
            f.write(f"- {file_name}\n")

        f.write("\n" + "-" * 60 + "\n\n")


print("\nAll 10 queries completed successfully.")
print(f"Results saved to: {output_file}")