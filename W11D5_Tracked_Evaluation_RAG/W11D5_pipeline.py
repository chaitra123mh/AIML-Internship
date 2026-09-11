import os
import mlflow
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from crewai import Agent, Task, Crew


# ============================================================
# W11D5: TRACKED & EVALUATED RAG PIPELINE
# ============================================================

print("=" * 60)
print("W11D5: TRACKED & EVALUATED RAG PIPELINE")
print("=" * 60)


# ------------------------------------------------------------
# 1. LOAD KNOWLEDGE BASE
# ------------------------------------------------------------

knowledge_file = "../W11D4_Ragas/knowledge_base.txt"

if not os.path.exists(knowledge_file):
    knowledge_file = "knowledge_base.txt"

with open(knowledge_file, "r", encoding="utf-8") as file:
    knowledge = file.read()

print("\n[1] Knowledge base loaded successfully.")


# ------------------------------------------------------------
# 2. CREATE DOCUMENT CHUNKS
# ------------------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

documents = splitter.create_documents([knowledge])

print(f"[2] Number of document chunks: {len(documents)}")


# ------------------------------------------------------------
# 3. CREATE CHROMADB VECTOR STORE
# ------------------------------------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vectorstore = Chroma.from_documents(
    documents,
    embedding=embeddings,
    collection_name="w11d5_rag"
)

print("[3] ChromaDB vector store created.")


# ------------------------------------------------------------
# 4. LOCAL LLM
# ------------------------------------------------------------

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

print("[4] Ollama LLM initialized.")


# ------------------------------------------------------------
# 5. LANGGRAPH STATE
# ------------------------------------------------------------

class RAGState(TypedDict):
    question: str
    context: str
    answer: str


# ------------------------------------------------------------
# 6. LANGGRAPH RETRIEVAL NODE
# ------------------------------------------------------------

def retrieve(state: RAGState):

    results = vectorstore.similarity_search(
        state["question"],
        k=2
    )

    context = "\n".join(
        document.page_content for document in results
    )

    return {
        "context": context
    }


# ------------------------------------------------------------
# 7. LANGGRAPH GENERATION NODE
# ------------------------------------------------------------

def generate(state: RAGState):

    prompt = f"""
Answer the question using only the provided context.

Context:
{state['context']}

Question:
{state['question']}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# ------------------------------------------------------------
# 8. BUILD LANGGRAPH
# ------------------------------------------------------------

graph = StateGraph(RAGState)

graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)

graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)

rag_graph = graph.compile()

print("[5] LangGraph RAG workflow created.")


# ------------------------------------------------------------
# 9. CREWAI AGENT
# ------------------------------------------------------------

research_agent = Agent(
    role="RAG Research Assistant",
    goal="Review and summarize the retrieved information.",
    backstory="An AI assistant that checks retrieved knowledge.",
    llm="ollama/llama3.2:3b",
    verbose=False
)

research_task = Task(
    description=(
        "Review the RAG answer and provide a short quality summary."
    ),
    expected_output="A short quality summary of the RAG answer.",
    agent=research_agent
)

crew = Crew(
    agents=[research_agent],
    tasks=[research_task],
    verbose=False
)

print("[6] CrewAI research agent created.")


# ------------------------------------------------------------
# 10. MLflow TRACKING
# ------------------------------------------------------------

mlflow.set_experiment("W11D5_Tracked_Evaluated_RAG")

question = "What is MLflow?"

with mlflow.start_run():

    mlflow.log_param("chunk_size", 500)
    mlflow.log_param("chunk_overlap", 100)
    mlflow.log_param("retrieval_k", 2)
    mlflow.log_param("embedding_model", "nomic-embed-text")
    mlflow.log_param("llm_model", "llama3.2:3b")

    print("\n[7] Running LangGraph RAG...")

    result = rag_graph.invoke({
        "question": question,
        "context": "",
        "answer": ""
    })

    answer = result["answer"]

    print("\nQuestion:")
    print(question)

    print("\nRetrieved Context:")
    print(result["context"])

    print("\nGenerated Answer:")
    print(answer)

    mlflow.log_text(
        result["context"],
        "retrieved_context.txt"
    )

    mlflow.log_text(
        answer,
        "generated_answer.txt"
    )

    mlflow.log_metric("answer_length", len(answer))

    print("\n[8] MLflow parameters and metrics logged.")


# ------------------------------------------------------------
# 11. CREWAI QUALITY REVIEW
# ------------------------------------------------------------

print("\n[9] Running CrewAI quality review...")

try:
    crew_result = crew.kickoff()

    print("\nCrewAI Review:")
    print(crew_result)

except Exception as error:
    print("\nCrewAI review could not be completed.")
    print("RAG pipeline execution is still successful.")
    print("Reason:", error)


# ------------------------------------------------------------
# 12. FINAL RESULT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("W11D5 PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)

print("""
Technologies demonstrated:
1. CrewAI      - Quality review agent
2. LangGraph   - RAG workflow
3. MLflow      - Experiment tracking
4. RAG         - Retrieval and generation
5. MLOps       - Logging and reproducibility
""")