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

    # ---------- Ingestion ----------
    docs = load_documents()
    chunks = splitter(docs)

    # ---------- Indexes ----------
    faiss = vector_store(chunks)
    bm25 = bm25_index(chunks)

    # ---------- Retrievers ----------
    vector_retriever = faiss.as_retriever(
        search_kwargs={"k": 8}
    )

    ensemble = EnsembleRetriever(
        retrievers=[bm25, vector_retriever],
        weights=[0.4, 0.6]
    )

    # ---------- Reranker ----------
    reranker = CrossEncoderReranker(
        model=HuggingFaceCrossEncoder(
            model_name="BAAI/bge-reranker-base"
        ),
        top_n=4
    )

    compression = ContextualCompressionRetriever(
        base_retriever=ensemble,
        base_compressor=reranker
    )

    # ---------- Multi Query ----------
    retriever = MultiQueryRetriever.from_llm(
        retriever=compression,
        llm=llm
    )

    return retriever


# Create once
hybrid_retriever = build_hybrid_pipeline()