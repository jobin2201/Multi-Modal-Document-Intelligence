from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def build_vector_store(chunks):
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    texts = [c["content"] for c in chunks]
    metadatas = [{"source": c["source"]} for c in chunks]

    vectorstore = FAISS.from_texts(texts, embedding, metadatas=metadatas)
    return vectorstore
