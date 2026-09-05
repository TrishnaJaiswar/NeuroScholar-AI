from graph.state import ResearchState, ResearchOutput
from core.llm import llm

research_llm = llm.with_structured_output(ResearchOutput)

# ---------------- QA ----------------

QA_RESEARCH_PROMPT = """
You are NeuroScholar AI's Research Agent.

Answer ONLY from the retrieved PDF context.

Return Markdown using:

# Title

> One-line definition

## Architecture

## How it Works

## Key Features

## Difference (if relevant)

Never use external knowledge.
If the answer is not in the context, say "I don't know."
Maximum 350 words.
"""

# ---------------- Literature Review ----------------

LITERATURE_REVIEW_PROMPT = """
You are NeuroScholar AI's Literature Review Agent.

Your job is to SYNTHESIZE multiple uploaded research papers.

Use ONLY the retrieved context.

Return Markdown with exactly this structure:

# Literature Review

## Executive Summary

## Common Research Themes

## Methodologies

Create a markdown table:

| Paper | Method | Dataset |

## Key Findings

## Research Gaps

## Limitations

## Future Directions

Rules:
- Every finding must come from the retrieved papers.
- Mention paper names naturally.
- Do NOT invent information.
- If evidence is missing, write "I don't know."
- Maximum 700 words.
"""

# ---------------- Structured Research ----------------

RESEARCH_PROMPT = """
You are NeuroScholar AI's Research Agent.

Extract only evidence from the retrieved papers.

Return ONLY ResearchOutput with:
- summary
- insights
"""

def build_context(state: ResearchState):

    chunks = state["retrieval"].chunks

    if not chunks:
        return "NO DOCUMENTS RETRIEVED"

    text = []

    for chunk in chunks[:4]:
        content = chunk.content[:2500]

        text.append(
            f"""
Source: {chunk.source}
Page: {chunk.page}

{content}
"""
        )

    return "\n\n---\n\n".join(text)

def research_node(state: ResearchState):

    task = state["planner"].task

    context = f"""
User Question:
{state["question"]}

Retrieved Papers:

{build_context(state)}
"""

    # -------- QA --------
    if task == "qa":

        response = llm.invoke([
            {"role": "system", "content": QA_RESEARCH_PROMPT},
            {"role": "user", "content": context}
        ])

        return {"answer": response.content}

    # -------- Literature Review --------
    if task == "literature_review":

        response = llm.invoke([
            {"role": "system", "content": LITERATURE_REVIEW_PROMPT},
            {"role": "user", "content": context}
        ])

        return {
            "research": ResearchOutput(
                summary=response.content,
                insights=[]
            ),
            "answer": response.content
        }

    # -------- Compare / Trend / Report --------

    research = research_llm.invoke([
        {"role": "system", "content": RESEARCH_PROMPT},
        {"role": "user", "content": context}
    ])

    return {"research": research}