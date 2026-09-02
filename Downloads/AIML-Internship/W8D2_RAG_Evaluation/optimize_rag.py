from rag_pipeline import retriever

questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is Natural Language Processing?",
    "What is Computer Vision?",
]

print("W8D2 RAG Optimization")
print("\n" + "=" * 50)
print("W8D2 RAG OPTIMIZATION TEST")
print("=" * 50)

test_questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is Natural Language Processing?",
    "What is Computer Vision?",
]

for question in test_questions:
    print(f"\nQuestion: {question}")

    results = retriever.invoke(question)

    print(f"Number of retrieved documents: {len(results)}")

    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc.page_content}")