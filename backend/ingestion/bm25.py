from langchain_community.retrievers import BM25Retriever

def bm25_index(chunks):
    bm25 = BM25Retriever.from_documents(chunks)
    bm25.k = 8
    return bm25