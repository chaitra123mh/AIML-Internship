from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser

# Prompt
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words with one example."
)

# Local Ollama model
llm = OllamaLLM(model="llama3.2:3b")

# Output parser
parser = StrOutputParser()

# LangChain chain
chain = prompt | llm | parser

# Test 5 inputs
topics = [
    "Artificial Intelligence",
    "Machine Learning",
    "Overfitting",
    "REST API",
    "ChromaDB"
]

print("=" * 60)
print("W6D1 - LANGCHAIN CHAIN")
print("=" * 60)

for i, topic in enumerate(topics, 1):
    result = chain.invoke({"topic": topic})

    print(f"\nTEST {i}")
    print("Topic:", topic)
    print("Answer:", result)

print("\nChain completed successfully!")