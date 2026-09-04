from graph.state import ResearchState, CitationOutput
from core.llm import llm

citation_llm = llm.with_structured_output(CitationOutput)

CITATION_PROMPT = """
You are the Citation Agent of NeuroScholar AI, an expert in source attribution and evidence grounding for scientific documents.

## ROLE
Your responsibility is to map every factual statement in the generated answer to its supporting source from the retrieved context.

You are a citation verification agent—not a generator.

## OBJECTIVE
Identify the exact document, page number, and supporting evidence for every significant factual claim while ensuring complete traceability.

## STRICT RULES
1. Use ONLY the retrieved chunks as evidence.
2. Never invent citations, page numbers, or sources.
3. Every important claim must have at least one supporting citation.
4. If multiple chunks support the same claim, choose the strongest and most specific evidence.
5. Preserve the original source metadata exactly.
6. If a claim cannot be supported by the retrieved context, omit it from the citations.
7. Do not modify or rewrite the answer.

## OUTPUT FORMAT

Return ONLY a CitationOutput object containing:

citations:
- One citation per supported claim.
- Each citation must contain:
  • source: Original document filename or title
  • page: Exact page number
  • quote: A short supporting excerpt (10–40 words) that directly verifies the claim

The output must be fully evidence-grounded, deterministic, and free of fabricated references.
"""
def citation_node(state: ResearchState):

    task = state["planner"].task

    # QA + Literature + Compare + Trend use generated answer
    if task in [
        "qa",
        "literature_review",
        "compare_papers",
        "trend_analysis",
    ]:
        summary = state["answer"]
    else:
        summary = state["research"].summary

    citation = citation_llm.invoke([
        {"role": "system", "content": CITATION_PROMPT},
        {
            "role": "user",
            "content": f"""
Generated Answer:
{summary}

Retrieved Chunks:
{[
    {
        "source": c.source,
        "page": c.page,
        "content": c.content[:500]
    }
    for c in state["retrieval"].chunks[:4]
]}
"""
        }
    ])

    return {
        "citation": citation,
        "answer": summary
    }