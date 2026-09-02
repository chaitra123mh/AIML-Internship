from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# Sample knowledge base
documents = [
    Document(page_content="Artificial Intelligence is the field of creating machines that can perform tasks requiring human intelligence."),
    Document(page_content="Machine Learning is a subset of Artificial Intelligence where computers learn patterns from data."),
    Document(page_content="Deep Learning uses neural networks with multiple layers to learn complex patterns."),
    Document(page_content="Natural Language Processing enables computers to understand and process human language."),
    Document(page_content="Computer Vision allows computers to understand and analyze images and videos."),
]


# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store embeddings in ChromaDB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="w8d2_rag"
)

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})


# Test questions
questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is Natural Language Processing?",
    "What is Computer Vision?"
]

print("W8D2 RAG Pipeline")
print("=" * 40)

for question in questions:
    results = retriever.invoke(question)

    print(f"\nQuestion: {question}")
    print("Retrieved Context:")

    for result in results:
        print("-", result.page_content)