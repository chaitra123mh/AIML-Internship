import ollama
import time

MODEL = "llama3.2:3b"

SYSTEM_PROMPT = """
You are a helpful AI/ML mentor.
Give clear, concise, beginner-friendly answers.
Use simple technical explanations and examples when useful.
"""

prompts = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is RAG?",
    "What is a vector database?",
    "What is the purpose of Ollama?"
]

print("=" * 60)
print("W7D4 - Ollama Local LLM Inference")
print("=" * 60)
print(f"Model: {MODEL}")
print("\nCustom System Prompt:")
print(SYSTEM_PROMPT)

results = []

for i, prompt in enumerate(prompts, start=1):
    print("\n" + "-" * 60)
    print(f"Prompt {i}: {prompt}")

    start_time = time.time()

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    latency = time.time() - start_time
    answer = response["message"]["content"]

    print("Answer:")
    print(answer)
    print(f"Latency: {latency:.2f} seconds")

    results.append(
        f"\nPrompt {i}: {prompt}\n"
        f"Answer: {answer}\n"
        f"Latency: {latency:.2f} seconds\n"
    )

with open("outputs/ollama_5_prompts.txt", "w", encoding="utf-8") as file:
    file.write("W7D4 - Ollama Local LLM Inference\n")
    file.write("=" * 60 + "\n")
    file.write(f"Model: {MODEL}\n")
    file.write("\nSystem Prompt:\n")
    file.write(SYSTEM_PROMPT + "\n")
    file.write("\n".join(results))

print("\n" + "=" * 60)
print("All 5 prompts completed successfully.")
print("Output saved to outputs/ollama_5_prompts.txt")
print("=" * 60)