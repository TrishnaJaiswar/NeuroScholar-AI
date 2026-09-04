from graph.state import ResearchState, RetrievalOutput, RetrievedChunk
from rag.Hybrid_pipeline import hybrid_retriever


def retrieval_node(state: ResearchState):

    # Retrieve documents
    docs = hybrid_retriever.invoke(state["question"])

    # PDFs selected from frontend
    selected = state.get("selected_documents", [])

    # Filter only selected PDFs
    if selected:
        docs = [
            d for d in docs
            if d.metadata.get("source") in selected
        ]

    chunks = []

    for d in docs:
        chunks.append(
            RetrievedChunk(
                document_id=d.metadata.get("document_id", ""),
                source=d.metadata.get("source", "Unknown"),
                page=d.metadata.get("page", 1),
                content=d.page_content,
                score=float(d.metadata.get("score", 0.0)),
                metadata=d.metadata,
            )
        )

    return {
        "retrieval": RetrievalOutput(
            query=state["question"],
            chunks=chunks,
        )
    }