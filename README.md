# arXplorer

A RAG pipeline for Q&A on research papers. Ask questions, get answers backed by actual paper content.

## What it does

arXplorer lets you query research papers using natural language. It pulls papers from arXiv, chunks them up, stores them in a vector database, and uses an LLM to answer your questions with proper context. Also includes a summarizer with a fine-tuned T5-small model for generating paper summaries.

## Project structure

arXplorer/

- arXplorer-arxivapi/ # arXiv API integration
- arXplorer-frontend/ # Web interface
- arXplorer-rag-branch/ # Core RAG implementation
- arXplorer-summarizer/ # Paper summarization module
- .gitignore
- LICENSE
- README.md

## Tech stack

- **Vector DB**: Pinecone for storing paper embeddings
- **Embeddings**: HuggingFace sentence-transformers
- **LLM**: Mistral-7B for generating answers
- **Summarizer**: Fine-tuned T5-small transformer
- **Framework**: LlamaIndex for the RAG pipeline
- **Data source**: arXiv API

## How it works

1. Fetch papers from arXiv based on your search criteria
2. Break them into chunks and generate embeddings
3. Store in Pinecone for fast retrieval
4. When you ask a question, find relevant chunks
5. Feed those chunks to Mistral-7B as context
6. Get an answer that actually references the papers
7. Generate summaries using the fine-tuned T5 model (when needed)

## Deployment

All components are deployed independently and communicate via REST APIs:

- **Frontend**: Deployed on Vercel
- **Backend APIs**: Deployed on Railway
- **Summarizer**: Running on CPU instances (free tier, so expect higher inference latency)

## Getting started

Check individual module READMEs for setup instructions. You'll need API keys for Pinecone and whatever LLM provider you're using.

## License

MIT

## Credits

Built on top of arXiv's API, Pinecone, LlamaIndex, and Mistral. Nothing fancy, just connecting good tools together.
