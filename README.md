# 📚 arXplorer: Research Paper Q&A with RAG

**arXplorer** is a Retrieval-Augmented Generation (RAG) pipeline that allows users to ask questions about research papers. It integrates the arXiv API, Pinecone vector database, HuggingFace embeddings, and Mistral-7B to provide accurate and contextual answers based on research content.

---

## ✨ Features

- 🔍 Semantic search on research papers using sentence-transformer embeddings
- 📑 Automatic ingestion of papers from arXiv
- 💾 Vector storage and retrieval via Pinecone
- 🧠 Mistral-7B LLM for natural language answers
- 🛠️ Fully modular, extendable RAG pipeline

---

## 📁 Project Structure

```
arXplorer/
├── arxiv_scraper.py         # Fetches and processes papers from arXiv
├── qa_pipeline.py           # Query engine for asking questions
├── requirements.txt         # Python dependencies
└── README.md                # You're reading this!
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/arXplorer.git
cd arXplorer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API keys

Ensure you have the following API keys:

- Pinecone API key
- Mistral API key (via OpenAccess)

Add them directly in the script or manage via environment variables.

---

## 📥 Ingest Papers from arXiv

Use `arxiv_scraper.py` to fetch and embed papers.

Ensure each record you insert into Pinecone looks like this:

```python
pinecone.upsert([
    {
        "id": "unique-id",
        "values": vector,
        "metadata": {
            "_node_content": "Full paper content goes here",
            "title": "Paper Title",
            "source": "arXiv"
        }
    }
])
```

> ⚠️ **Note:** The `_node_content` field is **essential** for LlamaIndex to function correctly.

---

## ❓ Ask Questions

Run the QA pipeline:

```bash
python qa_pipeline.py
```

Sample interaction:

```
Your question: What is self-attention in transformers?
Answer: [generated answer from LLM]
--------------------------------------------------
```

---

## 💡 Example Questions

- What problem does the Transformer model solve?
- How does self-attention differ from RNNs?
- What are the key takeaways from "Attention is All You Need"?

---

## 🛠️ Future Improvements

- Add citations or source highlighting
- Add web interface using Streamlit or Gradio
- Extend to more paper sources (e.g., Semantic Scholar)
- Add Docker support

---

## 📜 License

MIT License

---

## 🙏 Acknowledgments

- [arXiv API](https://arxiv.org/help/api/)
- [Pinecone](https://www.pinecone.io/)
- [LlamaIndex](https://www.llamaindex.ai/)
- [Mistral AI](https://docs.mistral.ai/)
- [HuggingFace Transformers](https://huggingface.co/)
