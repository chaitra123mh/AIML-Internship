print("W6D3 - LangChain Tools & Agents")

def calculator(a, b):
    return a + b

def web_search(query):
    return "Web search result for: " + query

print("\nTask 1 - Calculator")
print("10 + 20 =", calculator(10, 20))

print("\nTask 2 - Web Search")
print(web_search("What is LangChain?"))

print("\nTask 3 - Calculator")
print("50 + 25 =", calculator(50, 25))

print("\nAgent tasks completed successfully!")