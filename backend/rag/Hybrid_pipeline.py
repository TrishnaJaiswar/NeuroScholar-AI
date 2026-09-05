from langchain_classic.retrievers import EnsembleRetriever
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

from core.llm import llm
from ingestion.loaders import load_documents
from ingestion.splitter import splitter
from ingestion.vector_store import vector_store
from ingestion.bm25 import bm25_index


def build_hybrid_pipeline():
    """
    Builds a fresh Hybrid RAG pipeline using ALL uploaded PDFs.
    This is called on every query so newly uploaded papers are indexed.
    """

    # ---------- Load every uploaded PDF ----------
    docs = load_documents()

    # ---------- Chunk ----------
    chunks = splitter(docs)

    print("\n========== HYBRID RAG ==========")
    print(f"Indexed PDFs : {len(docs)}")
    print(f"Total Chunks : {len(chunks)}")

    # ---------- Vector Store ----------
    faiss = vector_store(chunks)

    # ---------- BM25 ----------
    bm25 = bm25_index(chunks)

    # ---------- Dense Retriever ----------
    vector_retriever = faiss.as_retriever(
        search_kwargs={"k": 4}
    )

    # ---------- Hybrid Retrieval ----------
    ensemble = EnsembleRetriever(
        retrievers=[bm25, vector_retriever],
        weights=[0.4, 0.6]
    )

    # ---------- Cross Encoder Reranker ----------
    reranker = CrossEncoderReranker(
        model=HuggingFaceCrossEncoder(
            model_name="BAAI/bge-reranker-base"
        ),
        top_n=4
    )

    # ---------- Context Compression ----------
    compression = ContextualCompressionRetriever(
        base_retriever=ensemble,
        base_compressor=reranker
    )

    # ---------- Multi Query ----------
    retriever = MultiQueryRetriever.from_llm(
        retriever=compression,
        llm=llm
    )

    print("Hybrid RAG Ready")
    print("===============================\n")

    return retriever