conversation_history = []

turns = [
    "My name is Chaitra.",
    "I am learning AI and machine learning.",
    "I am currently learning LangChain.",
    "I want to build AI applications.",
    "What am I currently learning?"
]

print("=" * 60)
print("W6D2 - CONVERSATION HISTORY")
print("=" * 60)

for i, message in enumerate(turns, 1):
    conversation_history.append(message)

    print(f"\nTURN {i}")
    print("User:", message)

print("\n" + "=" * 60)
print("STORED CONVERSATION HISTORY")
print("=" * 60)

for message in conversation_history:
    print(message)

print("\n5-turn conversation history maintained successfully!")