# Multi-Modal-Document-Intelligence
This project implements a Multi-Modal Retrieval-Augmented Generation (RAG) system designed to answer questions from complex, real-world documents such as financial and policy reports. Unlike traditional text-only QA systems, this solution processes text, tables, and scanned images (OCR) to deliver accurate, context-grounded answers with source attribution.


## Project Objective 
Modern documents contain diverse information formats that standard LLM pipelines often overlook. This project aims to build an intelligent document QA system capable of understanding and reasoning over multiple data modalities.


## 🚀 Key Features

### 🔹 Multi-Modal Ingestion
- Extracts **text**, **tables**, and **images** (via OCR)
- Supports both **scanned** and **structured** PDF documents

### 🔹 Smart Chunking & Embeddings
- Semantic and structural document segmentation
- Unified embedding space across multiple modalities

### 🔹 Vector-Based Retrieval
- Efficient similarity search over multi-modal content
- Context-aware document retrieval for accurate grounding

### 🔹 RAG-Powered QA Chatbot
- Interactive question-answering interface
- Responses generated using retrieved document context

### 🔹 Source Attribution
- Page-level or section-level citations for transparency and traceability

### 🔹 Evaluation Ready
- Supports benchmarking across **text**, **table**, and **image** queries



## 🤖 Model Choice

Initially, this project was implemented using **OpenAI (ChatGPT) models** via API. However, during development and testing, I repeatedly encountered **rate limit and quota exhaustion errors**, which significantly impacted usability and iteration speed.

### 🚨 Issues Faced with OpenAI API

- Frequent RateLimitError due to limited quota
- Even small queries failed once the free tier limit was exceeded
- Response generation would stall or fail entirely during QA
- Dependency on billing and API availability slowed development
- Large documents and RAG pipelines consumed tokens very quickly

These limitations made it difficult to reliably test and demonstrate the system.

---

## 🔄 Why  Ollama + LLaMA 3

To overcome these issues, I migrated the QA component to **Ollama using the LLaMA 3 model**, running fully locally.

### ✅ Benefits from My Perspective

- **No API key required** – eliminates quota and billing issues
- **No rate limits** – consistent and predictable responses
- **Fully local execution** – documents never leave the system
- **Faster iteration** during development and debugging
- **Cost-effective** for large PDFs and multi-modal RAG workflows

This change allowed the system to generate answers reliably without interruptions.

---

## 🎥 Live Demo

🎬 **Project Demonstration Video**

[▶️ Click here to watch the live demo](Multi-Modal-Document-Intelligence/Final%20Project%20.mp4)


## 🧠 Outcome
This project reflects real-world challenges in multi-modal document intelligence, emphasizing system design, reasoning, and engineering rigor over simple model usage. The solution demonstrates how complex requirements can be translated into an efficient and extensible RAG-based architecture.
