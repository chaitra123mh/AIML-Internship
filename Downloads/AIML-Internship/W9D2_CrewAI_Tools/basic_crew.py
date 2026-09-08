from crewai import Agent, Task, Crew, Process, LLM


# Local Ollama LLM
llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)


# -----------------------------
# Agent 1: Researcher
# -----------------------------
researcher = Agent(
    role="Researcher",
    goal="Research the given topic using your available knowledge and provide useful information.",
    backstory=(
        "You are a careful AI researcher who collects important facts "
        "and explains them clearly."
    ),
    verbose=True,
    llm=llm
)


# -----------------------------
# Agent 2: Writer
# -----------------------------
writer = Agent(
    role="Technical Writer",
    goal="Convert research findings into a clear and well-structured article.",
    backstory=(
        "You are a professional technical writer who can transform "
        "complex information into simple and readable content."
    ),
    verbose=True,
    llm=llm
)


# -----------------------------
# Agent 3: Reviewer
# -----------------------------
reviewer = Agent(
    role="Content Reviewer",
    goal="Review the article for accuracy, clarity, completeness, and quality.",
    backstory=(
        "You are a strict and careful reviewer. "
        "You check content for accuracy, clarity, completeness, "
        "organization, and missing information."
    ),
    verbose=True,
    llm=llm
)


# -----------------------------
# Task 1: Research
# -----------------------------
research_task = Task(
    description=(
        "Research the topic 'Generative AI in Healthcare'. "
        "Explain its applications, benefits, challenges, risks, "
        "and future scope."
    ),
    expected_output=(
        "Detailed research notes about Generative AI in Healthcare "
        "covering applications, benefits, challenges, risks, "
        "and future scope."
    ),
    agent=researcher
)


# -----------------------------
# Task 2: Writing
# -----------------------------
writing_task = Task(
    description=(
        "Using the research findings, write a clear article about "
        "Generative AI in Healthcare. Include introduction, "
        "applications, benefits, challenges, risks, future scope, "
        "and conclusion."
    ),
    expected_output=(
        "A well-structured article about Generative AI in Healthcare."
    ),
    agent=writer,
    context=[research_task]
)


# -----------------------------
# Task 3: Review
# -----------------------------
review_task = Task(
    description=(
        "Review the article created by the Writer. "
        "Check accuracy, clarity, completeness, organization, "
        "and missing important information. "
        "Give specific improvement suggestions."
    ),
    expected_output=(
        "A detailed review containing strengths, issues, "
        "missing information, and improvement suggestions."
    ),
    agent=reviewer,
    context=[writing_task]
)


# -----------------------------
# Create Crew
# -----------------------------
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)


# -----------------------------
# Run Crew
# -----------------------------
print("\n========== BASIC CREW STARTED ==========\n")

result = crew.kickoff()

print("\n========== FINAL RESULT ==========\n")
print(result)