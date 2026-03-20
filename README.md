# 🤖 RAG Pipeline — Retrieval Augmented Generation using LangChain & Groq

> A modular, production-style RAG pipeline that enables context-aware question 
> answering over custom documents using LangChain, FAISS vector store, and 
> Groq's Llama3 LLM.

---

## 📌 What This Project Does

Instead of relying on an LLM's general training knowledge, this pipeline:
1. Loads your own documents
2. Splits them into chunks
3. Converts chunks into vector embeddings
4. Stores embeddings in a FAISS vector database
5. At query time, retrieves the most relevant chunks
6. Passes retrieved context + user question to Llama3 via Groq API
7. Returns a grounded, document-specific answer

This is the core architecture behind AI-powered search, document Q&A systems, 
and intelligent content assistants used in real products.

---

## 🗂️ Project Structure
```
rag-pipeline/
│
├── load_data.py          # Document ingestion
├── split_data.py         # Text chunking & splitting
├── create_embeddings.py  # Embedding generation
├── create_vector_db.py   # FAISS vector database creation
├── get_vector_db.py      # Vector database retrieval
├── main.py               # Pipeline orchestration & query interface
└── app.py                # Application entry point
```

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| LLM | Groq API — Llama3-8b-8192 |
| Vector Store | FAISS (Facebook AI Similarity Search) |
| Framework | LangChain |
| Embeddings | LangChain Embeddings |
| Prompt Design | ChatPromptTemplate |
| Retrieval | LangChain Retrieval Chain |
| Environment | python-dotenv |

---

## 🚀 How It Works
```python
# main.py — core pipeline
llm = ChatGroq(model="llama3-8b-8192", api_key=os.environ["GROQ_API_KEY"])

prompt = ChatPromptTemplate.from_template("""
You are an assistant who will provide answers based on the provided document.
If you do not find the answer, say I do not know the answer.
context: {context}
questions: {input}
""")

document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
retriever = db.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
response = retrieval_chain.invoke({"input": question})
```

---

## ⚙️ Setup & Run
```bash
# 1. Clone the repository
git clone https://github.com/shreyavijayjadhav3/rag-pipeline.git
cd rag-pipeline

# 2. Install dependencies
pip install langchain langchain-community langchain-groq 
            faiss-cpu python-dotenv

# 3. Add your Groq API key
# Create a .env file:
GROQ_API_KEY=your_groq_api_key_here

# 4. Run the pipeline
python main.py
```

---

## 💡 Real-World Applications

This architecture directly applies to:
- **OTT platforms** — AI-powered content search and subscriber support bots
- **Media companies** — Intelligent document Q&A over editorial guidelines
- **E-commerce** — Context-aware customer support automation
- **Enterprise** — Internal knowledge base assistants

---

## 👩‍💻 Author

**Shreya Vijay Jadhav**
Data Analyst | [LinkedIn](https://www.linkedin.com/in/jadhavshreya03pune/) 
| [GitHub](https://github.com/shreyavijayjadhav3)

---

*Built to understand how AI systems retrieve and reason over 
real-world documents — not just generate from memory.*
