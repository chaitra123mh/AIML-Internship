from crewai import Agent, Task, Crew, Process, LLM

# Local Ollama LLM
llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)

# Agent 1: Researcher
researcher = Agent(
    role="Researcher",
    goal="Research the given topic and provide accurate and useful information.",
    backstory="You are a careful researcher who collects important facts and explains them clearly.",
    llm=llm,
    verbose=True
)

# Agent 2: Writer
writer = Agent(
    role="Writer",
    goal="Convert the research findings into a clear and well-structured article.",
    backstory="You are a professional technical writer who creates simple and informative content.",
    llm=llm,
    verbose=True
)

# Agent 3: Reviewer
reviewer = Agent(
    role="Reviewer",
    goal="Review the article for accuracy, clarity, completeness, and quality.",
    backstory="You are a strict reviewer who checks content and suggests improvements.",
    llm=llm,
    verbose=True
)

# Tasks
research_task = Task(
    description="Research the topic: Artificial Intelligence in Healthcare. "
                "Provide key facts, applications, benefits, and challenges.",
    expected_output="A clear research summary containing important facts and examples.",
    agent=researcher
)

writing_task = Task(
    description="Using the research provided by the researcher, write a clear "
                "and simple article about Artificial Intelligence in Healthcare.",
    expected_output="A well-structured article with introduction, applications, benefits, and challenges.",
    agent=writer
)

review_task = Task(
    description="Review the writer's article. Identify missing information, "
                "unclear statements, and areas that can be improved.",
    expected_output="A review containing strengths, weaknesses, and improvement suggestions.",
    agent=reviewer
)

# Create Crew
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)

# Run crew
result = crew.kickoff()

print("\n========== FINAL CREW OUTPUT ==========\n")
print(result)