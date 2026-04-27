# LLM Chat & RAG with GitHub Models

A comprehensive demonstration of Large Language Models (LLM), embeddings, and Retrieval-Augmented Generation (RAG) techniques using **free GitHub AI models** and various Python libraries.

## 🎯 Project Overview

This project showcases multiple approaches to building intelligent AI applications:

- **LLM Chat**: Direct interaction with language models using the OpenAI SDK
- **Text Embeddings**: Converting text into vector representations
- **RAG (Simple)**: Keyword-based search using Lunr for retrieval
- **RAG (Advanced)**: Vector-based retrieval using Chroma and LangChain

All examples use GitHub's free AI model inference endpoint, making this a cost-effective learning resource.

## 📋 Prerequisites

- Python >= 3.12
- GitHub account with AI Models access
- API key from [GitHub AI Models](https://github.com/marketplace/models)

## 🚀 Quick Start

### 1. Setup

Clone the repository and install dependencies:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Or using pip
pip install -r requirements.txt
```

### 2. Configure API Key

Add your GitHub AI Models API key to [util.py](util.py):

```python
API_KEY="your_github_model_api_key_here"
```

### 3. Run Examples

```bash
# Basic LLM chat
uv run 00-llm-chat.py

# Text embeddings
uv run 02-embedding.py

# Simple RAG with CSV
uv run 03-rag-simple-csv.py

# Advanced RAG with Chroma + LangChain
uv run 04-rag-chroma-langchain.py
```

## 📁 Project Structure

| File | Purpose |
|------|---------|
| [00-llm-chat.py](00-llm-chat.py) | Basic chat interaction with GitHub models |
| [02-embedding.py](02-embedding.py) | Text-to-vector conversion examples |
| [03-rag-simple-csv.py](03-rag-simple-csv.py) | Keyword-based RAG using Lunr search |
| [04-rag-chroma-langchain.py](04-rag-chroma-langchain.py) | Vector-based RAG with Chroma + LangChain |
| [main.py](main.py) | Main entry point (optional) |
| [util.py](util.py) | Shared utilities and configuration |
| [util-demo-show.py](util-demo-show.py) | Demo utilities |
| [books.csv](books.csv) | Sample dataset for RAG examples |

## 🔧 Core Components

### Configuration ([util.py](util.py))

```python
BASE_URL = "https://models.github.ai/inference"
MODEL_NAME = "openai/gpt-4o"
EMBEDDING_MODEL_NAME = "openai/text-embedding-3-small"
```

### Key Dependencies

- **openai**: OpenAI SDK for model access
- **lunr**: Full-text search engine
- **sentence-transformers**: Embedding models
- **langchain**: RAG orchestration framework
- **chromadb**: Vector database
- **pymupdf4llm**: PDF processing utilities

## 💡 Concepts

### What is RAG (Retrieval-Augmented Generation)?

RAG is a technique that:
1. Retrieves relevant documents/data based on a query
2. Augments the query with retrieved context
3. Generates responses using an LLM informed by that context

**Benefits:**
- More accurate, up-to-date responses
- Can work with private/custom data
- Reduces hallucinations

### Two RAG Approaches in This Project

#### Simple RAG (Lunr)
- Uses keyword-based full-text search
- Good for: Smaller datasets, simple queries, fast searches
- See: [03-rag-simple-csv.py](03-rag-simple-csv.py)

#### Advanced RAG (Chroma + LangChain)
- Uses vector embeddings for semantic search
- Good for: Large datasets, semantic similarity, complex queries
- See: [04-rag-chroma-langchain.py](04-rag-chroma-langchain.py)

## 📊 Example: Books Dataset

The [books.csv](books.csv) file contains book records with fields:
- Title
- Author
- Genre
- Language

Used by RAG examples to answer queries like: *"Suggest me some adventure books"*

## 🔑 API Keys & Authentication

### GitHub Models API

1. Go to [GitHub Marketplace Models](https://github.com/marketplace/models)
2. Authenticate with your GitHub account
3. Create a personal access token with appropriate scopes
4. Add to [util.py](util.py):

```python
API_KEY = "your_token_here"
```

## 📝 Example Usage

### Basic Chat
```python
response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### Text Search with RAG
```python
results = index.search("adventure books")
# Format results as markdown table
# Send to LLM with context for generation
```

### Vector-Based RAG
```python
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(...),
    chain_type="stuff",
    retriever=db.as_retriever()
)
response = qa_chain.invoke("Your question here")
```

## 🛠️ Customization

### Use Your Own Data

Replace [books.csv](books.csv) with your own CSV file, or modify the loaders in:
- [03-rag-simple-csv.py](03-rag-simple-csv.py) for keyword search
- [04-rag-chroma-langchain.py](04-rag-chroma-langchain.py) for vector search

### Change Models

Update [util.py](util.py) to use different models:
```python
MODEL_NAME = "openai/gpt-4o"  # Or other available models
EMBEDDING_MODEL_NAME = "openai/text-embedding-3-small"
```

## 📚 Learning Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com)
- [GitHub Models Documentation](https://docs.github.com/en/github-models)
- [RAG Best Practices](https://github.com/langchain-ai/rag-from-scratch)

## 🐛 Troubleshooting

### "API Key Invalid" Error
- Check that your GitHub Models API key is correctly set in [util.py](util.py)
- Verify the key has appropriate permissions

### Embedding Model Issues
- Ensure the embedding model dimensions match your configuration
- Check network connectivity to the models endpoint

### Out of Memory
- Reduce `chunk_size` in text splitter
- Use streaming for large documents
- Reduce batch size in embeddings

## 📄 License

This project is provided as-is for educational purposes.

## 🤝 Contributing

Feel free to extend this project with:
- Additional RAG patterns
- Different data sources (PDF, web, databases)
- Performance optimizations
- Additional examples

---

**Happy Learning! 🚀**
