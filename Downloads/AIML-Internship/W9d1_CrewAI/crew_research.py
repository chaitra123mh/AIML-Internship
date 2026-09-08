from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

# Local Ollama LLM
llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)
#web search tool
search_tool=SerperDevTool()

# Agent 1: Researcher
researcher = Agent(
    role="Researcher",
    goal="Research the given topic and provide accurate, useful information.",
    backstory="You are a careful AI researcher who collects important facts and explains them clearly.",
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

# Agent 2: Writer
writer = Agent(
    role="Writer",
    goal="Convert research findings into a clear and well-structured article.",
    backstory="You are a professional technical writer who explains complex topics in simple language.",
    verbose=True,
    llm=llm
)

# Agent 3: Reviewer
reviewer = Agent(
    role="Reviewer",
    goal="Review the article for accuracy, clarity, completeness and quality.",
    backstory="You are a strict reviewer who checks technical content and suggests improvements.",
    verbose=True,
    llm=llm
)

# Tasks
research_task = Task(
    description="Research the topic: 'Generative AI in Healthcare'. Explain its uses, benefits, challenges and future scope.",
    expected_output="Detailed research notes with important facts and examples.",
    agent=researcher
)

writing_task = Task(
    description="Using the researcher's findings, write a clear article about Generative AI in Healthcare.",
    expected_output="A well-structured article with introduction, applications, benefits, challenges and conclusion.",
    agent=writer
)

review_task = Task(
    description="Review the written article. Identify factual issues, missing information and areas for improvement.",
    expected_output="A review containing strengths, problems and specific improvement suggestions.",
    agent=reviewer
)

# Crew
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)

# Run
result = crew.kickoff()

print("\n========== FINAL RESULT ==========\n")
print(result)