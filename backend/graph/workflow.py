from langgraph.graph import StateGraph, START, END

from graph.state import ResearchState

from agents.planner_agent import planner_node
from agents.retrieval_agent import retrieval_node
from agents.research_agent import research_node
from agents.analysis_agent import analysis_node
from agents.critic_agent import critic_node
from agents.citation_agent import citation_node
from agents.report_agent import report_node

# ---------- Planner Router ----------

def route_planner(state: ResearchState):
    return state["planner"].task


# ---------- Build Graph ----------

builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("retrieval", retrieval_node)
builder.add_node("research", research_node)
builder.add_node("analysis", analysis_node)
builder.add_node("critic", critic_node)
builder.add_node("citation", citation_node)
builder.add_node("report", report_node)


# ---------- Start ----------

builder.add_edge(START, "planner")


# ---------- Planner Routing ----------

builder.add_conditional_edges(
    "planner",
    route_planner,
    {
        "qa": "retrieval",
        "compare_papers": "retrieval",
        "literature_review": "retrieval",
        "trend_analysis": "retrieval",
        "summarize": "retrieval",
        "report_generation": "retrieval",
    },
)


# ---------- Common Pipeline ----------

builder.add_edge("retrieval", "research")


# ---------- Research Routing ----------

def route_after_research(state: ResearchState):
    if state["planner"].task == "summarize":
        return "end"
    return "analysis"


builder.add_conditional_edges(
    "research",
    route_after_research,
    {
        "analysis": "analysis",
        "end": END,
    },
)


# ---------- Analysis Routing ----------

def route_after_analysis(state: ResearchState):
    task = state["planner"].task

    # Compare Papers → Citation
    if task == "compare_papers":
        return "citation"

    # Literature Review → Citation
    if task == "literature_review":
        return "citation"

    # Trend Analysis → Citation
    if task == "trend_analysis":
        return "citation"

    # QA → Citation
    return "citation"


builder.add_conditional_edges(
    "analysis",
    route_after_analysis,
    {
        "citation": "citation",
    },
)


# ---------- Citation Routing ----------

def route_after_citation(state: ResearchState):
    task = state["planner"].task

    if task == "qa":
        return "end"

    return "report"


builder.add_conditional_edges(
    "citation",
    route_after_citation,
    {
        "end": END,
        "report": "report",
    },
)


# ---------- Final Paths ----------

builder.add_edge("critic", "citation")
builder.add_edge("report", END)


graph = builder.compile()