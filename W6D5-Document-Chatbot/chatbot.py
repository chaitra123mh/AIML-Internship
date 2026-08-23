import requests
from PyPDF2 import PdfReader

print("W6D5 - Document Chatbot")

# Load PDF
reader = PdfReader("sample.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text() or ""

print("PDF loaded successfully.")

# Keep relevant context
context = text[:3000]

# Ask question
question = "What is the main topic of this document?"

prompt = f"""
Answer using only the document below.

Document:
{context}

Question: {question}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()

print("\nQuestion:", question)
print("\nAnswer:")

if "response" in data:
    print(data["response"])
else:
    print(data)