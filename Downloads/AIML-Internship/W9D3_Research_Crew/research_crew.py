from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)

researcher = Agent(
    role="Researcher",
    goal="Find 2 facts about AI in healthcare.",
    backstory="You are a fast researcher.",
    llm=llm
)

writer = Agent(
    role="Writer",
    goal="Write a 3-sentence summary.",
    backstory="You are a simple technical writer.",
    llm=llm
)

reviewer = Agent(
    role="Reviewer",
    goal="Give 1 improvement suggestion.",
    backstory="You are a quick reviewer.",
    llm=llm
)

research_task = Task(
    description="Give 2 facts about AI in healthcare.",
    expected_output="2 short facts.",
    agent=researcher
)

writing_task = Task(
    description="Write a 3-sentence summary from the research.",
    expected_output="3 short sentences.",
    agent=writer
)

review_task = Task(
    description="Give 1 suggestion to improve the summary.",
    expected_output="1 short suggestion.",
    agent=reviewer
)

crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential
)

result = crew.kickoff()

print("\n===== W9D3 OUTPUT =====")
print(result)