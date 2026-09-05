from graph.state import ResearchState, ReportOutput
from core.llm import llm

report_llm = llm.with_structured_output(ReportOutput)

REPORT_PROMPT = """
You are the Report Agent of NeuroScholar AI.

Generate a publication-quality research report using ONLY the supplied
research findings, analysis, and citations.

Rules:
- Never use external knowledge.
- If analysis is unavailable, omit comparative reasoning.
- If evidence is insufficient, say "I don't know."
- Return ONLY ReportOutput.
"""

def report_node(state: ResearchState):

    task = state["planner"].task

    # Literature Review already returns final markdown
    if task == "literature_review":
        return {
            "answer": state["answer"]
        }

    # Safe state access (prevents KeyError)
    research = state.get("research")
    analysis = state.get("analysis")
    citation = state.get("citation")

    research_text = (
        research.model_dump_json(indent=2) if research else "{}"
    )

    analysis_text = (
        analysis.model_dump_json(indent=2) if analysis else "{}"
    )

    citation_text = (
        citation.model_dump_json(indent=2) if citation else "{}"
    )

    report = report_llm.invoke([
        {"role": "system", "content": REPORT_PROMPT},
        {
            "role": "user",
            "content": f"""
Question:
{state["question"]}

Research:
{research_text}

Analysis:
{analysis_text}

Citations:
{citation_text}
"""
        }
    ])

    return {
        "report": report,
        "answer": f"""# {report.title}

## Abstract
{report.abstract}

## Introduction
{report.introduction}

## Key Findings
{chr(10).join(f"- {x}" for x in report.key_findings)}

## Comparative Analysis
{report.comparative_analysis}

## Limitations
{report.limitations}

## Conclusion
{report.conclusion}

## References
{chr(10).join(f"- {r}" for r in report.references)}
"""
    }