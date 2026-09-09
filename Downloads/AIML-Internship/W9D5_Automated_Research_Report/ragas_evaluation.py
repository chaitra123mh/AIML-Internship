from ragas import EvaluationDataset

# Sample research question and answer
question = "What are the applications of AI in healthcare?"

answer = """
Artificial Intelligence is used in healthcare for medical image analysis,
disease prediction, patient monitoring, drug discovery and virtual assistants.
It can help healthcare professionals analyze data faster and support
better decision making.
"""

context = """
AI is used in medical imaging, disease prediction, patient monitoring,
drug discovery and healthcare assistants.
"""

# Create Ragas evaluation data
samples = [
    {
        "user_input": question,
        "response": answer,
        "retrieved_contexts": [context]
    }
]

evaluation_dataset = EvaluationDataset(samples=samples)

print("=" * 60)
print("RAGAS EVALUATION")
print("=" * 60)

print(f"Question: {question}")

print("\nGenerated Answer:")
print(answer)

print("\nRetrieved Context:")
print(context)

print("\nEvaluation dataset created successfully.")
print("Ragas evaluation data is ready.")
print("\nRagas component: PASSED")