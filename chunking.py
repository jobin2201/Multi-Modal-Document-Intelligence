from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []
    for d in docs:
        split_texts = splitter.split_text(d["text"])
        for text in split_texts:
            chunks.append({
                "content": text,
                "source": f"page {d.get('page', 'N/A')}"
            })
    return chunks
