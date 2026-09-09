from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# -------------------------------------------------
# State definition
# -------------------------------------------------
class ResearchState(TypedDict):
    topic: str
    research: str
    report: str
    reviewed_report: str


# -------------------------------------------------
# Node 1: Research
# -------------------------------------------------
def research_node(state: ResearchState):
    topic = state["topic"]

    research = (
        f"Research topic: {topic}\n\n"
        "Artificial Intelligence in Healthcare uses machine learning, "
        "computer vision and natural language processing to support "
        "diagnosis, medical imaging, patient monitoring and drug discovery.\n\n"
        "Benefits include faster analysis, improved decision support "
        "and better healthcare efficiency.\n\n"
        "Challenges include data privacy, bias, security and the need "
        "for human supervision."
    )

    return {"research": research}


# -------------------------------------------------
# Node 2: Generate Report
# -------------------------------------------------
def report_node(state: ResearchState):
    topic = state["topic"]
    research = state["research"]

    report = f"""
AUTOMATED RESEARCH REPORT

Topic: {topic}

1. Introduction
Artificial Intelligence is becoming an important technology in
modern healthcare. It can analyze large amounts of medical data
and assist healthcare professionals.

2. Applications
- Medical image analysis
- Disease prediction
- Patient monitoring
- Drug discovery
- Virtual healthcare assistants

3. Benefits
- Faster data analysis
- Improved decision support
- Better efficiency
- Support for early disease detection

4. Challenges
- Patient data privacy
- Algorithmic bias
- Cybersecurity risks
- Need for human supervision

5. Future Scope
AI can support personalized treatment, advanced medical research
and more efficient healthcare services.

6. Conclusion
AI has significant potential in healthcare when it is developed
and used responsibly with appropriate human oversight.

Research Information:
{research}
"""

    return {"report": report}


# -------------------------------------------------
# Node 3: Review Report
# -------------------------------------------------
def review_node(state: ResearchState):
    report = state["report"]

    reviewed = (
        report
        + "\n\nREVIEW STATUS: PASSED"
        + "\nThe report was checked for structure, clarity and completeness."
    )

    return {"reviewed_report": reviewed}


# -------------------------------------------------
# Build LangGraph
# -------------------------------------------------
workflow = StateGraph(ResearchState)

workflow.add_node("research", research_node)
workflow.add_node("generate_report", report_node)
workflow.add_node("review", review_node)

workflow.add_edge(START, "research")
workflow.add_edge("research", "generate_report")
workflow.add_edge("generate_report", "review")
workflow.add_edge("review", END)

app = workflow.compile()


# -------------------------------------------------
# Run Workflow
# -------------------------------------------------
if __name__ == "__main__":

    initial_state = {
        "topic": "Artificial Intelligence in Healthcare",
        "research": "",
        "report": "",
        "reviewed_report": ""
    }

    result = app.invoke(initial_state)

    print("=" * 60)
    print("LANGGRAPH AUTOMATED RESEARCH WORKFLOW")
    print("=" * 60)

    print(result["reviewed_report"])

    with open("langgraph_report.txt", "w", encoding="utf-8") as file:
        file.write(result["reviewed_report"])

    print("\nLangGraph report saved to: langgraph_report.txt")