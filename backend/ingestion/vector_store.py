from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


@lru_cache(maxsize=1)
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def vector_store(chunks):
    if not chunks:
        raise ValueError("Cannot create FAISS index: no document chunks found.")

    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embeddings)
