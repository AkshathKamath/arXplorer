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
