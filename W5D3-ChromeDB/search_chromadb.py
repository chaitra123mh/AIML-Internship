import chromadb

# Connect to the existing ChromaDB database
client = chromadb.PersistentClient(path="./chroma_data")

# Load the existing collection
collection = client.get_collection(name="aiml_documents")

print("Collection loaded successfully!")
print("Total documents:", collection.count())


# ----------------------------------------
# 1. Similarity Search using Cosine
# ----------------------------------------

query = "How can I prevent a machine learning model from learning the training data too closely?"

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\n" + "=" * 60)
print("SIMILARITY SEARCH RESULTS")
print("=" * 60)

print("Query:", query)

for i, document in enumerate(results["documents"][0], start=1):
    print(f"\nResult {i}:")
    print(document)


# ----------------------------------------
# 2. Metadata Filtering
# ----------------------------------------

filtered_results = collection.get(
    where={"topic": "evaluation"}
)

print("\n" + "=" * 60)
print("METADATA FILTERING RESULTS")
print("=" * 60)

print("Filter: topic = evaluation")

for i, document in enumerate(filtered_results["documents"], start=1):
    print(f"\nResult {i}:")
    print(document)