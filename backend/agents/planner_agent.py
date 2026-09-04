from graph.state import ResearchState, PlannerOutput
from core.llm import llm

planner_llm = llm.with_structured_output(PlannerOutput)

PLANNER_PROMPT = """
You are the Planner Agent of NeuroScholar AI.

Your ONLY job is to create an execution plan.

AVAILABLE TASKS
- qa
- compare_papers
- literature_review
- trend_analysis
- summarize
- report_generation

AVAILABLE AGENTS
- retrieval
- research
- analysis
- critic
- citation
- report

RULES
1. Select exactly one task.
2. Choose the required agents in execution order.
3. Enable use_rag=True whenever document evidence is required.
4. Use retrieval_mode="hybrid".
5. Set top_k:
   - qa → 4
   - summarize → 6
   - compare_papers → 8
   - literature_review → 8
   - trend_analysis → 8
   - report_generation → 10
6. Return ONLY PlannerOutput.
"""

def planner_node(state: ResearchState):

    forced_task = state.get("forced_task")

    if forced_task:
        topk_map = {
            "qa": 4,
            "summarize": 6,
            "compare_papers": 8,
            "literature_review": 8,
            "trend_analysis": 8,
            "report_generation": 10,
        }

        planner = PlannerOutput(
            task=forced_task,
            agents=[
                "retrieval",
                "research",
                "analysis",
                "citation",
                "report",
            ],
            use_rag=True,
            retrieval_mode="hybrid",
            use_metadata_filter=False,
            top_k=topk_map.get(forced_task, 4),
            reasoning=f"Workflow selected from dashboard: {forced_task}",
        )

    else:
        planner = planner_llm.invoke([
            {"role": "system", "content": PLANNER_PROMPT},
            {"role": "user", "content": state["question"]},
        ])

    if planner.task == "literature_review":
        document_count = state.get("document_count", 1)

        if document_count < 2:
            planner.reasoning = (
                "Only one document is available. Literature review quality will be limited."
            )

    return {
        "planner": planner,
        "selected_documents": state.get("selected_documents", []),
    }