from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool


# ==========================================
# 1. Local Ollama LLM
# ==========================================

llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)


# ==========================================
# 2. Web Search Tool
# ==========================================

search_tool = SerperDevTool()


# ==========================================
# 3. Researcher Agent
# ==========================================

researcher = Agent(
    role="Web Researcher",

    goal=(
        "Research the given topic using web search and "
        "collect accurate, current, and useful information "
        "from reliable online sources."
    ),

    backstory=(
        "You are an experienced AI research assistant. "
        "You search the web carefully, identify useful information, "
        "and provide clear research findings."
    ),

    verbose=True,
    llm=llm,
    tools=[search_tool]
)


# ==========================================
# 4. Writer Agent
# ==========================================

writer = Agent(
    role="Technical Writer",

    goal=(
        "Transform the research findings into a clear, "
        "well-structured and easy-to-understand article."
    ),

    backstory=(
        "You are a professional technical writer. "
        "You convert complex research information into "
        "simple, organized and readable content."
    ),

    verbose=True,
    llm=llm
)


# ==========================================
# 5. Reviewer Agent
# ==========================================

reviewer = Agent(
    role="Content Reviewer",

    goal=(
        "Review the article for accuracy, clarity, completeness, "
        "organization and overall quality."
    ),

    backstory=(
        "You are a strict content reviewer. "
        "You identify incorrect information, missing points, "
        "weak explanations and areas that need improvement."
    ),

    verbose=True,
    llm=llm
)


# ==========================================
# 6. Research Task
# ==========================================

research_task = Task(

    description=(
        "Research the topic 'Generative AI in Healthcare'. "
        "Use the web search tool to find current and reliable "
        "information. Focus on applications, benefits, "
        "challenges, risks, recent developments and future scope."
    ),

    expected_output=(
        "Detailed research notes about Generative AI in Healthcare "
        "including applications, benefits, challenges, risks, "
        "recent developments and future scope. "
        "Mention important information found from web sources."
    ),

    agent=researcher
)


# ==========================================
# 7. Writing Task
# ==========================================

writing_task = Task(

    description=(
        "Using the research findings provided by the Researcher, "
        "write a clear and well-structured article about "
        "Generative AI in Healthcare. Include an introduction, "
        "applications, benefits, challenges, risks, recent "
        "developments, future scope and conclusion."
    ),

    expected_output=(
        "A professional and easy-to-understand article about "
        "Generative AI in Healthcare with clear headings "
        "and a conclusion."
    ),

    agent=writer,

    context=[research_task]
)


# ==========================================
# 8. Review Task
# ==========================================

review_task = Task(

    description=(
        "Review the article created by the Writer. "
        "Check its accuracy, clarity, completeness, organization "
        "and relevance. Identify missing information and provide "
        "specific suggestions for improvement."
    ),

    expected_output=(
        "A detailed review containing strengths, weaknesses, "
        "missing information and specific improvement suggestions."
    ),

    agent=reviewer,

    context=[writing_task]
)


# ==========================================
# 9. Create Crew
# ==========================================

crew = Crew(

    agents=[
        researcher,
        writer,
        reviewer
    ],

    tasks=[
        research_task,
        writing_task,
        review_task
    ],

    process=Process.sequential,

    verbose=True
)


# ==========================================
# 10. Run Crew
# ==========================================

print("\n")
print("=" * 60)
print("      CREWAI WEB SEARCH CREW STARTED")
print("=" * 60)
print("\n")

result = crew.kickoff()


# ==========================================
# 11. Display Final Result
# ==========================================

print("\n")
print("=" * 60)
print("              FINAL RESULT")
print("=" * 60)
print("\n")

print(result)

print("\n")
print("=" * 60)
print("          WEB SEARCH CREW COMPLETED")
print("=" * 60)