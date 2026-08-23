import ollama
import time

models = [
    "llama3.2:3b",
    "qwen2.5:3b"
]

questions = [
    "What is Artificial Intelligence?",
    "What is Retrieval Augmented Generation (RAG)?",
    "What is the difference between Machine Learning and Deep Learning?"
]

system_prompt = """
You are an AI/ML mentor.
Answer clearly and accurately.
Keep answers beginner-friendly and concise.
"""

print("=" * 70)
print("W7D4 - Llama 3.2 vs Qwen 2.5 Comparison")
print("=" * 70)

all_results = []

for question_number, question in enumerate(questions, start=1):

    print(f"\nQUESTION {question_number}: {question}")
    print("-" * 70)

    for model in models:

        start_time = time.time()

        response = ollama.chat(
            model=model,
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

        latency = time.time() - start_time
        answer = response["message"]["content"]

        print(f"\nMODEL: {model}")
        print(f"Answer:\n{answer}")
        print(f"Latency: {latency:.2f} seconds")

        all_results.append(
            f"\nQuestion {question_number}: {question}\n"
            f"Model: {model}\n"
            f"Answer:\n{answer}\n"
            f"Latency: {latency:.2f} seconds\n"
        )

with open("outputs/model_comparison.txt", "w", encoding="utf-8") as file:
    file.write("W7D4 - Llama 3.2 vs Qwen 2.5\n")
    file.write("=" * 70 + "\n")
    file.write("\n".join(all_results))

print("\n" + "=" * 70)
print("Model comparison completed successfully.")
print("Output saved to outputs/model_comparison.txt")
print("=" * 70)