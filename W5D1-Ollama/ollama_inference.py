import ollama

# Custom system prompt
system_prompt = """
You are a helpful AI/ML tutor.
Explain concepts in simple language.
Use short examples.
Keep answers clear and beginner-friendly.
"""

# Same three questions for both models
questions = [
    "What is the difference between supervised and unsupervised learning?",

    "Explain overfitting with a simple example.",

    "What is the bias-variance trade-off?"
]

# Models to compare
models = [
    "llama3.2:3b",
    "qwen2.5:3b"
]

# Run the same questions on both models
for model_name in models:

    print("\n" + "=" * 70)

    print("MODEL:", model_name)

    print("=" * 70)

    for number, question in enumerate(
        questions,
        start=1
    ):

        print("\n" + "-" * 70)

        print(f"QUESTION {number}:")
        print(question)

        print("\nAI RESPONSE:\n")

        # Call the selected local model
        response = ollama.chat(
            model=model_name,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        # Print the model response
        print(
            response["message"]["content"]
        )

print(
    "\nModel comparison completed successfully!"
)