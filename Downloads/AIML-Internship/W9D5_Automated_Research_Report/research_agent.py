from crewai import Agent, Task, Crew, Process, LLM

# Local Ollama LLM
llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)

# -------------------------------------------------
# Agent 1: Researcher
# -------------------------------------------------
researcher = Agent(
    role="Researcher",
    goal="Collect accurate and useful information about the given topic.",
    backstory=(
        "You are an AI research specialist. "
        "You analyze a topic and provide clear, factual information "
        "that can be used in a research report."
    ),
    llm=llm,
    verbose=False
)

# -------------------------------------------------
# Agent 2: Report Writer
# -------------------------------------------------
writer = Agent(
    role="Research Report Writer",
    goal="Create a well-structured research report from the research findings.",
    backstory=(
        "You are an experienced technical writer. "
        "You convert research information into a clear and readable report "
        "with an introduction, key findings, benefits, challenges and conclusion."
    ),
    llm=llm,
    verbose=False
)

# -------------------------------------------------
# Agent 3: Reviewer
# -------------------------------------------------
reviewer = Agent(
    role="Report Reviewer",
    goal="Review the research report and improve its accuracy and clarity.",
    backstory=(
        "You are a strict quality reviewer. "
        "You check reports for clarity, completeness, consistency and "
        "well-organized information."
    ),
    llm=llm,
    verbose=False
)


# -------------------------------------------------
# Research Task
# -------------------------------------------------
research_task = Task(
    description=(
        "Research the topic: Artificial Intelligence in Healthcare. "
        "Provide important facts, applications, benefits, challenges "
        "and future possibilities."
    ),
    expected_output=(
        "A detailed research summary containing facts, applications, "
        "benefits, challenges and future possibilities."
    ),
    agent=researcher
)


# -------------------------------------------------
# Writing Task
# -------------------------------------------------
writing_task = Task(
    description=(
        "Using the researcher's findings, create a professional research "
        "report about Artificial Intelligence in Healthcare. "
        "Include Introduction, Applications, Benefits, Challenges, "
        "Future Scope and Conclusion."
    ),
    expected_output="A structured research report.",
    agent=writer
)


# -------------------------------------------------
# Review Task
# -------------------------------------------------
review_task = Task(
    description=(
        "Review the research report created by the writer. "
        "Correct unclear statements and improve the organization. "
        "Return the final improved report."
    ),
    expected_output="A polished final research report.",
    agent=reviewer
)


# -------------------------------------------------
# Create Crew
# -------------------------------------------------
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=False
)


# -------------------------------------------------
# Run the Research Agent
# -------------------------------------------------
print("=" * 60)
print("AUTOMATED RESEARCH REPORT AGENT")
print("=" * 60)

result = crew.kickoff()

print("\nFINAL RESEARCH REPORT")
print("=" * 60)
print(result)

# Save output
with open("research_report.txt", "w", encoding="utf-8") as file:
    file.write(str(result))

print("\nReport saved to: research_report.txt")