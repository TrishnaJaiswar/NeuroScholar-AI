from functools import lru_cache
from pathlib import Path

from graph.state import (
    ResearchState,
    RetrievalOutput,
    RetrievedChunk,
)
from rag.Hybrid_pipeline import build_hybrid_pipeline


@lru_cache(maxsize=1)
def get_retriever():
    return build_hybrid_pipeline()


def retrieval_node(state: ResearchState):
    print("\n========== RETRIEVAL ==========")
    print("Question:", state["question"])

    retriever = get_retriever()
    docs = retriever.invoke(state["question"])

    print("Retrieved before filter:", len(docs))

    selected = state.get("selected_documents", [])
    print("Selected PDFs:", selected)

    if selected:
        selected_names = {Path(name).name for name in selected}
        docs = [
            d for d in docs
            if Path(d.metadata.get("source", "")).name in selected_names
        ]

    print("Retrieved after filter:", len(docs))

    if docs:
        print("First source:", docs[0].metadata.get("source"))

    chunks = [
        RetrievedChunk(
            document_id=d.metadata.get("document_id", ""),
            source=Path(d.metadata.get("source", "Unknown")).name,
            page=d.metadata.get("page", 1),
            content=d.page_content,
            score=float(d.metadata.get("score", 0.0)),
            metadata=d.metadata,
        )
        for d in docs
    ]

    print("================================\n")

    return {
        "retrieval": RetrievalOutput(
            query=state["question"],
            chunks=chunks,
        )
    }
