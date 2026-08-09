import chromadb

# --------------------------------------------------
# Connect to existing ChromaDB
# --------------------------------------------------

client = chromadb.PersistentClient(path="./chroma_data")

# Load the existing collection
collection = client.get_collection(name="aiml_documents")

print("ChromaDB collection loaded successfully!")
print("Total documents:", collection.count())


# --------------------------------------------------
# 1. Semantic Search using Cosine Similarity
# --------------------------------------------------

query = "How does overfitting affect the performance of a machine learning model?"

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\n" + "=" * 70)
print("W5D4 - SEMANTIC SEARCH USING COSINE SIMILARITY")
print("=" * 70)

print("\nSearch Query:")
print(query)

print("\nTop 3 Semantic Search Results:")

for i, document in enumerate(results["documents"][0], start=1):

    print("\n" + "-" * 70)
    print(f"Result {i}:")
    print(document)

    # Display distance if available
    if "distances" in results:
        print("Cosine Distance:", results["distances"][0][i - 1])


# --------------------------------------------------
# 2. Metadata Filtering
# --------------------------------------------------

filtered_results = collection.get(
    where={"topic": "evaluation"}
)

print("\n" + "=" * 70)
print("W5D4 - METADATA FILTERING")
print("=" * 70)

print("\nFilter Used:")
print("topic = evaluation")

for i, document in enumerate(filtered_results["documents"], start=1):

    print("\n" + "-" * 70)
    print(f"Filtered Result {i}:")
    print(document)


# --------------------------------------------------
# Completion Message
# --------------------------------------------------

print("\n" + "=" * 70)
print("W5D4 SEMANTIC SEARCH COMPLETED SUCCESSFULLY!")
print("=" * 70)