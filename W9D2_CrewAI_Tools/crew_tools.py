from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

# Local Ollama LLM
llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)

print("CrewAI W9D2 setup started successfully!")

# Web search tool
search_tool = SerperDevTool()

# Agent 1: Researcher
researcher = Agent(
    role="Researcher",
    goal="Research the given topic using accurate and current information from the web.",
    backstory=(
        "You are a careful AI researcher. "
        "You collect useful facts from reliable sources "
        "and present them clearly."
    ),
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

print("Researcher agent created successfully!")

# Agent 2: Writer
writer = Agent(
    role="Technical Writer",
    goal="Convert the research findings into a clear, accurate, and well-structured article.",
    backstory=(
        "You are a professional technical writer who can "
        "transform complex research into simple and readable content."
    ),
    verbose=True,
    llm=llm
)

print("Writer agent created successfully!")

# Agent 3: Reviewer
reviewer = Agent(
    role="Content Reviewer",
    goal="Review the written article for accuracy, clarity, completeness, and overall quality.",
    backstory=(
        "You are a strict and careful reviewer. "
        "You check whether the content is accurate, clear, complete, "
        "and well organized. You also suggest useful improvements."
    ),
    verbose=True,
    llm=llm
)

print("Reviewer agent created successfully!")

# Task 1: Research
research_task = Task(
    description=(
        "Research the topic 'Generative AI in Healthcare'. "
        "Use the web search tool to find current and reliable information. "
        "Focus on applications, benefits, challenges, risks, and future scope."
    ),
    expected_output=(
        "Detailed research notes covering applications, benefits, "
        "challenges, risks, future scope, and relevant examples."
    ),
    agent=researcher
)

print("Research task created successfully!")

# Task 2: Writing
writing_task = Task(
    description=(
        "Using the research findings provided by the Researcher, "
        "write a clear and well-structured article about Generative AI in Healthcare. "
        "Include an introduction, applications, benefits, challenges, risks, "
        "future scope, and conclusion."
    ),
    expected_output=(
        "A well-structured article about Generative AI in Healthcare "
        "with clear sections, accurate information, and a conclusion."
    ),
    agent=writer,
    context=[research_task]
)

print("Writing task created successfully!")

# Task 3: Review
review_task = Task(
    description=(
        "Review the article created by the Writer about Generative AI in Healthcare. "
        "Check the content for accuracy, clarity, completeness, organization, "
        "and missing important information. Provide specific improvement suggestions."
    ),
    expected_output=(
        "A detailed review containing strengths, issues, missing information, "
        "and specific suggestions for improving the article."
    ),
    agent=reviewer,
    context=[writing_task]
)

print("Review task created successfully!")

# Create the Crew
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)

print("Crew created successfully!")

# Run the Crew
print("\n========== STARTING CREW ==========\n")

result = crew.kickoff()

print("\n========== FINAL RESULT ==========\n")
print(result)