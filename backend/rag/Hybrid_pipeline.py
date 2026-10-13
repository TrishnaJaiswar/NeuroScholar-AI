from langchain_classic.retrievers import EnsembleRetriever
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

from core.llm import llm
from ingestion.loaders import load_documents
from ingestion.splitter import splitter
from ingestion.vector_store import vector_store
from ingestion.bm25 import bm25_index


def build_hybrid_pipeline():
    """
    Builds the Hybrid RAG pipeline using uploaded PDFs.

    Components:
    - FAISS dense retrieval
    - BM25 keyword retrieval
    - Ensemble retrieval
    - Multi-query retrieval

    Cross-encoder reranking is disabled to reduce memory usage.
    """

    # Load uploaded PDFs
    docs = load_documents()

    if not docs:
        raise ValueError(
            "No PDFs found. Upload at least one research paper."
        )

    # Split documents into chunks
    chunks = splitter(docs)

    print("\n========== HYBRID RAG ==========")
    print(f"Indexed PDFs: {len(docs)}")
    print(f"Total chunks: {len(chunks)}")

    if not chunks:
        raise ValueError("No document chunks were generated.")

    # Build FAISS vector store
    faiss = vector_store(chunks)

    # Build BM25 keyword index
    bm25 = bm25_index(chunks)

    # Dense retrieval
    vector_retriever = faiss.as_retriever(
        search_kwargs={"k": 4}
    )

    # Hybrid retrieval
    ensemble = EnsembleRetriever(
        retrievers=[bm25, vector_retriever],
        weights=[0.4, 0.6],
    )

    # Multi-query retrieval without cross-encoder reranking
    retriever = MultiQueryRetriever.from_llm(
        retriever=ensemble,
        llm=llm,
    )

    print("Hybrid RAG Ready")
    print("Reranker: Disabled to reduce memory usage")
    print("===============================\n")

    return retriever