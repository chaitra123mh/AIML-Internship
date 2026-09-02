"""
W8D5: Local AI Research Assistant

This prototype uses:
- LangGraph for workflow management
- Ollama for local LLM inference
- ChromaDB for local document storage
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama


# ---------------------------------------------------------
# 1. Define the state used by the LangGraph workflow
# ---------------------------------------------------------

class ResearchState(TypedDict):
    question: str
    context: str
    answer: str


# ---------------------------------------------------------
# 2. Local research knowledge
# ---------------------------------------------------------

DOCUMENTS = {
    "Artificial Intelligence": """
Artificial Intelligence (AI) is a field of computer science
that develops systems capable of performing tasks that normally
require human intelligence. Examples include learning,
reasoning, problem solving and decision making.
""",

    "Machine Learning": """
Machine Learning (ML) is a subset of Artificial Intelligence.
It allows computers to learn patterns from data and make
predictions or decisions without being explicitly programmed
for every task.
""",

    "Deep Learning": """
Deep Learning is a branch of machine learning that uses
multi-layer neural networks. It is widely used for image
recognition, speech processing and natural language processing.
""",

    "Natural Language Processing": """
Natural Language Processing (NLP) enables computers to
understand, process and generate human language. Applications
include chatbots, translation and sentiment analysis.
"""
}


# ---------------------------------------------------------
# 3. Retrieve relevant local information
# ---------------------------------------------------------

def retrieve_information(state: ResearchState):
    question = state["question"].lower()

    relevant_information = []

    for topic, document in DOCUMENTS.items():
        if any(word in question for word in topic.lower().split()):
            relevant_information.append(
                f"{topic}:\n{document}"
            )

    # If no exact topic is found, provide all local knowledge
    if not relevant_information:
        relevant_information = list(DOCUMENTS.values())

    return {
        "context": "\n".join(relevant_information)
    }


# ---------------------------------------------------------
# 4. Generate answer using local Ollama model
# ---------------------------------------------------------

def generate_answer(state: ResearchState):

    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    prompt = f"""
You are a local AI research assistant.

Answer the user's question using the provided research context.

Research context:
{state["context"]}

User question:
{state["question"]}

Give a clear and simple answer.
Do not invent information that is not supported by the context.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# ---------------------------------------------------------
# 5. Build LangGraph workflow
# ---------------------------------------------------------

workflow = StateGraph(ResearchState)

workflow.add_node("retrieve", retrieve_information)
workflow.add_node("generate", generate_answer)

workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

research_graph = workflow.compile()


# ---------------------------------------------------------
# 6. Run the research assistant
# ---------------------------------------------------------

if __name__ == "__main__":

    question = input("Enter your research question: ")

    result = research_graph.invoke({
        "question": question,
        "context": "",
        "answer": ""
    })

    print("\n--- AI Research Assistant ---")
    print("Question:", question)
    print("\nAnswer:")
    print(result["answer"])

    # Save output evidence
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("W8D5 Local AI Research Assistant\n")
        file.write("--------------------------------\n")
        file.write(f"Question: {question}\n\n")
        file.write("Answer:\n")
        file.write(result["answer"])

    print("\nOutput saved to output.txt")