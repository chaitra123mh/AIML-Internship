import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

prompts = [
    "What is AI?",
    "Explain machine learning.",
    "Explain supervised and unsupervised learning with examples.",
    "Explain overfitting, underfitting, bias and variance.",
    "Explain how a RAG system works using ChromaDB and Ollama."
]

input_price = 5
output_price = 15

print("=" * 60)
print("W5D6 TOKEN COST AUDIT")
print("=" * 60)

total_tokens = 0
total_cost = 0

for i, prompt in enumerate(prompts, 1):

    tokens = len(enc.encode(prompt))

    # Simple estimated output assumption
    output_tokens = 50

    cost = (
        tokens / 1_000_000 * input_price
        + output_tokens / 1_000_000 * output_price
    )

    total_tokens += tokens
    total_cost += cost

    print(f"\nPrompt {i}")
    print("Prompt:", prompt)
    print("Input tokens:", tokens)
    print("Estimated output tokens:", output_tokens)
    print(f"Estimated cost: ${cost:.6f}")

print("\n" + "=" * 60)
print("TOTAL INPUT TOKENS:", total_tokens)
print(f"TOTAL ESTIMATED COST: ${total_cost:.6f}")
print("=" * 60)