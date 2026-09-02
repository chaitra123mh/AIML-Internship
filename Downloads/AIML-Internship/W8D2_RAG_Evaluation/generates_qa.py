from rag_pipeline import retriever


qa_pairs = [
    {
        "question": "What is Artificial Intelligence?",
        "answer": "Artificial Intelligence is the field of creating machines that can perform tasks requiring human intelligence."
    },
    {
        "question": "What is Machine Learning?",
        "answer": "Machine Learning is a subset of Artificial Intelligence where computers learn patterns from data."
    },
    {
        "question": "What is Deep Learning?",
        "answer": "Deep Learning uses neural networks with multiple layers to learn complex patterns."
    },
    {
        "question": "What is Natural Language Processing?",
        "answer": "Natural Language Processing enables computers to understand and process human language."
    },
    {
        "question": "What is Computer Vision?",
        "answer": "Computer Vision allows computers to understand and analyze images and videos."
    },
    {
        "question": "How does Machine Learning relate to AI?",
        "answer": "Machine Learning is a subset of Artificial Intelligence."
    },
    {
        "question": "What does Deep Learning use?",
        "answer": "Deep Learning uses neural networks with multiple layers."
    },
    {
        "question": "What does NLP process?",
        "answer": "NLP processes and understands human language."
    },
    {
        "question": "What can Computer Vision analyze?",
        "answer": "Computer Vision can analyze images and videos."
    },
    {
        "question": "What is the purpose of Artificial Intelligence?",
        "answer": "The purpose of Artificial Intelligence is to create machines that can perform tasks requiring human intelligence."
    }
]


with open("qa_dataset.txt", "w", encoding="utf-8") as file:

    for i, item in enumerate(qa_pairs, start=1):

        contexts = retriever.invoke(item["question"])

        context_text = "\n".join(
            [doc.page_content for doc in contexts]
        )

        file.write(f"Question {i}: {item['question']}\n")
        file.write(f"Answer {i}: {item['answer']}\n")
        file.write(f"Context {i}: {context_text}\n")
        file.write("-" * 70 + "\n")


print("Successfully generated 10 Q&A pairs.")
print("Saved to qa_dataset.txt")