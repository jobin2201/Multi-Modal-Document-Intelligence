from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA


def create_qa_chain(vectorstore):
    llm = Ollama(
        model="llama3",   # or "mistral", "phi3", etc.
        temperature=0
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True
    )

    return qa
