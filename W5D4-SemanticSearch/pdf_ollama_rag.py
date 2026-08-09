import chromadb
import ollama
from pypdf import PdfReader


# --------------------------------------------------
# 1. Read the PDF
# --------------------------------------------------

pdf_path = "aiml_notes.pdf"

reader = PdfReader(pdf_path)

pdf_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        pdf_text += text + "\n"


print("PDF loaded successfully!")
print("Characters extracted:", len(pdf_text))


# --------------------------------------------------
# 2. Split the PDF into chunks
# --------------------------------------------------

chunks = [
    chunk.strip()
    for chunk in pdf_text.split("\n\n")
    if chunk.strip()
]

print("Number of chunks:", len(chunks))


# --------------------------------------------------
# 3. Store chunks in ChromaDB
# --------------------------------------------------

client = chromadb.PersistentClient(path="./chroma_data")

collection = client.get_or_create_collection(
    name="pdf_aiml_collection",
    configuration={"hnsw": {"space": "cosine"}}
)

ids = [f"pdf_chunk_{i}" for i in range(len(chunks))]

metadatas = [
    {
        "source": "aiml_notes.pdf",
        "chunk": i
    }
    for i in range(len(chunks))
]

collection.upsert(
    ids=ids,
    documents=chunks,
    metadatas=metadatas
)

print("PDF chunks stored in ChromaDB!")
print("Stored chunks:", collection.count())


# --------------------------------------------------
# 4. Ask a question and retrieve top 3 chunks
# --------------------------------------------------

question = "What is overfitting and why does it cause poor performance on new data?"

results = collection.query(
    query_texts=[question],
    n_results=3
)

retrieved_chunks = results["documents"][0]

print("\n" + "=" * 60)
print("TOP 3 RETRIEVED CHUNKS")
print("=" * 60)

for i, chunk in enumerate(retrieved_chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)


# --------------------------------------------------
# 5. Send retrieved chunks to Ollama
# --------------------------------------------------

context = "\n\n".join(retrieved_chunks)

prompt = f"""
Answer the question using only the information provided in the context.

Context:
{context}

Question:
{question}

Give a clear and simple answer.
"""

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "You are an AI/ML tutor. Answer using the provided context."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)


# --------------------------------------------------
# 6. Display final answer
# --------------------------------------------------

print("\n" + "=" * 60)
print("OLLAMA FINAL ANSWER")
print("=" * 60)

print(response["message"]["content"])

print("\nPDF + ChromaDB + Ollama process completed successfully!")