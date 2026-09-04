from graph.state import ResearchState, AnalysisOutput
from core.llm import llm

analysis_llm = llm.with_structured_output(AnalysisOutput)

# ---------- Structured Analysis ----------
ANALYSIS_PROMPT = """
You are the Analysis Agent of NeuroScholar AI.

Analyze multiple research papers and return ONLY an AnalysisOutput object.

If fewer than two papers exist:

comparisons = []
trends = []
conclusion = "Comparative analysis was not performed because only one research document was available. Multiple papers are required for evidence-based comparison."
"""

# ---------- Compare Papers ----------
COMPARE_PROMPT = """
You are NeuroScholar AI's Compare Papers Agent.

Return ONLY Markdown.

# Paper Comparison

## Executive Summary

## Comparison Table

| Criteria | Paper 1 | Paper 2 |
|---|---|---|
| Research Objective | | |
| Methodology | | |
| Dataset | | |
| Model | | |
| Results | | |

## Strengths

### Paper 1

### Paper 2

## Limitations

### Paper 1

### Paper 2

## Best Overall

If only one paper exists, clearly state that comparison requires multiple papers.
"""

# ---------- Trend Analysis ----------
TREND_PROMPT = """
You are NeuroScholar AI's Trend Analysis Agent.

Return ONLY Markdown.

# Research Trend Analysis

## Overview

## Recurring Methodologies

## Popular Datasets

## Emerging Architectures

## Research Gaps

## Future Trends
"""

def analysis_node(state: ResearchState):

    task = state["planner"].task

    # -------- QA --------
    if task == "qa":
        return {
            "answer": state["answer"]
        }

    # -------- Compare Papers --------
    if task == "compare_papers":
        response = llm.invoke([
            {"role": "system", "content": COMPARE_PROMPT},
            {
                "role": "user",
                "content": f"""
Question:
{state["question"]}

Research Summary:
{state["research"].summary}

Retrieved Chunks:
{state["retrieval"].chunks}
"""
            }
        ])

        return {
            "answer": response.content
        }

    # -------- Trend Analysis --------
    if task == "trend_analysis":
        response = llm.invoke([
            {"role": "system", "content": TREND_PROMPT},
            {
                "role": "user",
                "content": f"""
Question:
{state["question"]}

Research Summary:
{state["research"].summary}

Retrieved Chunks:
{state["retrieval"].chunks}
"""
            }
        ])

        return {
            "answer": response.content
        }

    # -------- Literature Review / Report --------
    analysis = analysis_llm.invoke([
        {"role": "system", "content": ANALYSIS_PROMPT},
        {
            "role": "user",
            "content": str(state["research"])
        }
    ])

    return {
        "analysis": analysis
    }