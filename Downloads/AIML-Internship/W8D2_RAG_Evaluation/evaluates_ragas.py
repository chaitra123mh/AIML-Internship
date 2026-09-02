from ragas import EvaluationDataset, evaluate
from ragas.metrics import (
    Faithfulness,
    ResponseRelevancy,
    ContextPrecision,
    ContextRecall,
)

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings

from rag_pipeline import retriever


qa_pairs = [
    {
        "question": "What is Artificial Intelligence?",
        "answer": "Artificial Intelligence is the field of creating machines that can perform tasks requiring human intelligence.",
    },
    {
        "question": "What is Machine Learning?",
        "answer": "Machine Learning is a subset of Artificial Intelligence where computers learn patterns from data.",
    },
    {
        "question": "What is Deep Learning?",
        "answer": "Deep Learning uses neural networks with multiple layers to learn complex patterns.",
    },
    {
        "question": "What is Natural Language Processing?",
        "answer": "Natural Language Processing enables computers to understand and process human language.",
    },
    {
        "question": "What is Computer Vision?",
        "answer": "Computer Vision allows computers to understand and analyze images and videos.",
    },
    {
        "question": "How does Machine Learning relate to AI?",
        "answer": "Machine Learning is a subset of Artificial Intelligence.",
    },
    {
        "question": "What does Deep Learning use?",
        "answer": "Deep Learning uses neural networks with multiple layers.",
    },
    {
        "question": "What does NLP process?",
        "answer": "NLP processes and understands human language.",
    },
    {
        "question": "What can Computer Vision analyze?",
        "answer": "Computer Vision can analyze images and videos.",
    },
    {
        "question": "What is the purpose of Artificial Intelligence?",
        "answer": "The purpose of Artificial Intelligence is to create machines that can perform tasks requiring human intelligence.",
    },
]


dataset = []

for item in qa_pairs:
    results = retriever.invoke(item["question"])

    contexts = [doc.page_content for doc in results]

    dataset.append(
        {
            "user_input": item["question"],
            "response": item["answer"],
            "retrieved_contexts": contexts,
            "reference": item["answer"],
        }
    )


evaluation_dataset = EvaluationDataset.from_list(dataset)


# Local Ollama LLM
ollama_llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
)

evaluator_llm = LangchainLLMWrapper(ollama_llm)


# Local HuggingFace embeddings
hf_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

evaluator_embeddings = LangchainEmbeddingsWrapper(
    hf_embeddings
)


print("\nStarting RAGAS evaluation...")
print("=" * 50)


result = evaluate(
    dataset=evaluation_dataset,
    metrics=[
        Faithfulness(llm=evaluator_llm),
        ResponseRelevancy(llm=evaluator_llm),
        ContextPrecision(llm=evaluator_llm),
        ContextRecall(llm=evaluator_llm),
    ],
    embeddings=evaluator_embeddings,
)


print("\nRAGAS EVALUATION RESULTS")
print("=" * 50)
print(result)