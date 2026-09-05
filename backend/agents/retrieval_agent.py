from pathlib import Path

from graph.state import (
    ResearchState,
    RetrievalOutput,
    RetrievedChunk,
)
from rag.Hybrid_pipeline import build_hybrid_pipeline


def retrieval_node(state: ResearchState):

    print("\n========== RETRIEVAL ==========")
    print("Question:", state["question"])

    # Retrieve from Hybrid RAG
    retriever = build_hybrid_pipeline()
    docs = retriever.invoke(state["question"])

    print("Retrieved before filter:", len(docs))

    # Selected PDFs from frontend
    selected = state.get("selected_documents", [])
    print("Selected PDFs:", selected)

    # Compare only filename, not full path
    if selected:
        docs = [
            d for d in docs
            if Path(d.metadata.get("source", "")).name in selected
        ]

    print("Retrieved after filter:", len(docs))

    if docs:
        print("First source:", docs[0].metadata.get("source"))

    chunks = []

    for d in docs:
        chunks.append(
            RetrievedChunk(
                document_id=d.metadata.get("document_id", ""),
                source=Path(
                    d.metadata.get("source", "Unknown")
                ).name,
                page=d.metadata.get("page", 1),
                content=d.page_content,
                score=float(d.metadata.get("score", 0.0)),
                metadata=d.metadata,
            )
        )

    print("================================\n")

    return {
        "retrieval": RetrievalOutput(
            query=state["question"],
            chunks=chunks,
        )
    }