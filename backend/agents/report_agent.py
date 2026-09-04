from graph.state import ResearchState, ReportOutput
from core.llm import llm

report_llm = llm.with_structured_output(ReportOutput)


REPORT_PROMPT = """
You are the Report Agent of NeuroScholar AI, an expert in scientific writing, literature synthesis, and technical report generation.

## ROLE
Your responsibility is to transform verified research findings into a publication-quality research report.

You are a report generation agent—not a retrieval or reasoning agent.

## OBJECTIVE
Produce a clear, logically structured, and academically professional report using ONLY the validated research, comparative analysis, and citations provided.

## STRICT RULES
1. Use only the supplied research, analysis, and citations.
2. Never introduce external knowledge or unsupported claims.
3. Present information objectively and with technical precision.
4. Organize the report using clear academic structure.
5. Every factual statement should be traceable to the provided citations.
6. Do not mention the retrieval process or AI workflow.
7. If evidence is insufficient, explicitly state "I don't know."

## OUTPUT FORMAT

Return ONLY a ReportOutput object containing:

title:
- A concise and descriptive research title.

abstract:
- 150–250 words summarizing the objective, methodology, key findings, and conclusion.

sections:
- Include the following sections in order:
  1. Introduction
  2. Key Findings
  3. Comparative Analysis
  4. Limitations
  5. Conclusion

- Each section must contain well-structured technical content.

references:
- List all cited source documents in the order they appear.
- Use the provided citation metadata only.
"""

def report_node(state: ResearchState):

    task = state["planner"].task

    # Literature Review already produced the final Markdown
    if task == "literature_review":
        return {
            "answer": state["answer"]
        }

    # Compare Papers & Trend Analysis
    report = report_llm.invoke([
        {"role": "system", "content": REPORT_PROMPT},
        {
            "role": "user",
            "content": f"""
Question:
{state["question"]}

Research:
{state["research"]}

Analysis:
{state["analysis"]}

Citations:
{state["citation"]}
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