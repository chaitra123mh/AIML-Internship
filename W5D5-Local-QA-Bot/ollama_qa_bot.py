import ollama

system_prompt = """
You are a helpful AI assistant.
Answer questions clearly and simply.
"""

questions = [
    "What is machine learning?",
    "What is Python?",
    "What is an API?",
    "What is overfitting?",
    "What is data preprocessing?"
]

for i, question in enumerate(questions, 1):

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    print("\n" + "=" * 60)
    print("QUESTION", i)
    print(question)
    print("\nANSWER:")
    print(response["message"]["content"])

print("\nW5D5 Local Q&A Bot completed successfully!")