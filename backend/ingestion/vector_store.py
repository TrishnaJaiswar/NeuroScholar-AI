from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore