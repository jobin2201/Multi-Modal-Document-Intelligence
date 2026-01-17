import streamlit as st 
from dotenv import load_dotenv
import os
from pathlib import Path

# Get the directory where app.py is located
APP_DIR = Path(__file__).parent
ENV_FILE = APP_DIR / ".env"

# Load environment variables from .env file FIRST (explicit path)
load_dotenv(dotenv_path=ENV_FILE, override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
st.set_page_config(page_title="Multi-Modal RAG QA")

# Check OpenAI API key BEFORE importing other modules
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("⚠️ **OPENAI_API_KEY not found!**")
    st.markdown("""
    **Please create a `.env` file in your project root with:**
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```
    
    **Steps:**
    1. Create a file named `.env` in the same folder as `app.py`
    2. Add your OpenAI API key: `OPENAI_API_KEY=sk-...`
    3. Get your API key from: https://platform.openai.com/api-keys
    4. Reload this page after creating the file
    """)
    st.stop()

# Now import other modules that need the API key
from ingest import extract_text, extract_tables, extract_images_ocr
from chunking import chunk_documents
from embeddings import build_vector_store
from rag_qa import create_qa_chain

st.title("📄 Multi-Modal Document Intelligence (RAG)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Processing document...")

    text_docs = extract_text("temp.pdf")
    table_docs = extract_tables("temp.pdf")
    image_docs = extract_images_ocr("temp.pdf")

    all_docs = text_docs + table_docs + image_docs
    chunks = chunk_documents(all_docs)
    vectorstore = build_vector_store(chunks)
    qa_chain = create_qa_chain(vectorstore)

    st.success("Document indexed successfully!")

    query = st.text_input("Ask a question")

    if query:
        result = qa_chain.invoke({qa_chain.input_key: query})

        st.subheader("Answer")
        st.write(result["result"])

        st.subheader("Sources")
        for doc in result["source_documents"]:
            st.write(doc.metadata["source"])

