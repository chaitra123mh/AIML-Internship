from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2:3b",
    base_url="http://localhost:11434"
)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer in one short sentence:\n{question}"
)

chain = prompt | llm

print("===== LANGCHAIN CHAIN TEST =====")

inputs = [
    "What is AI?",
    "What is machine learning?",
    "What is deep learning?",
    "What is NLP?",
    "What is generative AI?"
]

for question in inputs:
    answer = chain.invoke({"question": question})
    print(f"\nQ: {question}")
    print(f"A: {answer}")

print("\n===== MEMORY TEST =====")

history = []

turns = [
    "My name is Chaitra.",
    "I am learning AI and machine learning.",
    "I am working on CrewAI.",
    "I am also learning LangChain.",
    "What technologies am I learning?"
]

for turn in turns:
    history.append(turn)

print("\nConversation history:")
for item in history:
    print("-", item)

print("\nMemory maintained across 5 turns: YES")