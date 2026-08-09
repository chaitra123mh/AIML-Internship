import chromadb

# Create a local ChromaDB client
client = chromadb.PersistentClient(path="./chroma_data")

# Create a collection
collection = client.get_or_create_collection(
    name="aiml_documents",
    configuration={"hnsw": {"space": "cosine"}}
)

# 20 sample AI/ML documents
documents = [
    "Machine learning allows computers to learn patterns from data.",
    "Supervised learning uses labeled training data.",
    "Unsupervised learning finds patterns in unlabeled data.",
    "Classification is used to predict categories or classes.",
    "Regression is used to predict continuous numerical values.",
    "Decision trees make predictions using a tree-like structure.",
    "Random forests combine multiple decision trees.",
    "Logistic regression is commonly used for classification.",
    "Linear regression predicts a continuous target variable.",
    "Overfitting happens when a model learns training data too closely.",
    "Underfitting happens when a model is too simple to learn patterns.",
    "Feature engineering creates useful features from raw data.",
    "Data preprocessing prepares data for machine learning models.",
    "Precision measures how many predicted positives are actually positive.",
    "Recall measures how many actual positives are correctly identified.",
    "Deep learning uses neural networks with multiple layers.",
    "Natural language processing helps computers understand human language.",
    "Generative AI can create text, images, audio, and other content.",
    "Large language models generate text based on learned patterns.",
    "Model evaluation helps determine how well a machine learning model performs."
]

# Metadata for each document
metadatas = [
    {"topic": "machine_learning"},
    {"topic": "supervised_learning"},
    {"topic": "unsupervised_learning"},
    {"topic": "classification"},
    {"topic": "regression"},
    {"topic": "decision_tree"},
    {"topic": "random_forest"},
    {"topic": "logistic_regression"},
    {"topic": "linear_regression"},
    {"topic": "overfitting"},
    {"topic": "underfitting"},
    {"topic": "feature_engineering"},
    {"topic": "preprocessing"},
    {"topic": "evaluation"},
    {"topic": "evaluation"},
    {"topic": "deep_learning"},
    {"topic": "nlp"},
    {"topic": "generative_ai"},
    {"topic": "llm"},
    {"topic": "evaluation"}
]

ids = [f"doc{i}" for i in range(1, 21)]

# Add documents to ChromaDB
collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("ChromaDB collection created successfully!")
print("Collection name:", collection.name)
print("Number of documents:", collection.count())