from graph.state import ResearchState, ResearchOutput
from core.llm import llm

research_llm = llm.with_structured_output(ResearchOutput)

# ---------------- QA ----------------
QA_RESEARCH_PROMPT = """
You are NeuroScholar AI's Research Agent.

Return ONLY Markdown.

For QA tasks use this structure:

# Title

> One-sentence definition

## Architecture

Explain briefly.

## How it works

Use bullet points.

## Key Features

- Feature 1
- Feature 2
- Feature 3

## Difference (if relevant)

Use a markdown table.

Rules:
- Do NOT write Abstract, Introduction, Conclusion.
- Maximum 350 words.
- Be concise and educational.
"""

# ---------------- Literature Review ----------------
LITERATURE_REVIEW_PROMPT = """
You are NeuroScholar AI's Literature Review Agent.

Return ONLY Markdown.

This is NOT a research paper.
Do NOT write Abstract, Introduction, Conclusion, References, or Citation numbers.

Use exactly this structure:

# Literature Review

## Executive Summary
Write 120–180 words.

## Common Research Themes
Use bullet points.

## Methodologies
Create a markdown table with columns:
| Paper | Method | Dataset |

## Key Findings
List 5–8 evidence-based findings.

## Research Gaps
List the unresolved problems.

## Limitations
List limitations of the existing studies.

## Future Directions
Provide practical future research opportunities.

STRICT RULES:
- Use only retrieved context.
- Never invent citations.
- Never write "Citation 1" or "References".
- Maximum 600 words.
"""

# ---------------- Other Workflows ----------------
RESEARCH_PROMPT = """
You are the Research Agent of NeuroScholar AI, an expert in scientific literature analysis and evidence synthesis.

## ROLE
Your responsibility is to extract the most important knowledge from the retrieved context.

## OBJECTIVE
Analyze the provided context and produce a concise, technically accurate research synthesis.

Return ONLY a ResearchOutput object containing:
- summary
- insights
"""

def research_node(state: ResearchState):

    task = state["planner"].task

    context = f"""
Question:
{state["question"]}

Retrieved Context:
{state["retrieval"].chunks}
"""

    # -------- QA --------
    if task == "qa":
        response = llm.invoke([
            {"role": "system", "content": QA_RESEARCH_PROMPT},
            {"role": "user", "content": context}
        ])

        return {
            "answer": response.content
        }

    # -------- Literature Review --------
    if task == "literature_review":
        response = llm.invoke([
            {"role": "system", "content": LITERATURE_REVIEW_PROMPT},
            {"role": "user", "content": context}
        ])

        research = ResearchOutput(
            summary=response.content,
            insights=[]
        )

        return {
            "research": research,
            "answer": response.content
        }

    # -------- Compare / Trend / Report --------
    research = research_llm.invoke([
        {"role": "system", "content": RESEARCH_PROMPT},
        {"role": "user", "content": context}
    ])

    return {
        "research": research
    }