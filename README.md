# LegalAid-RAG ⚖️

An AI-powered Legal Research Assistant built using Retrieval-Augmented Generation (RAG). The application allows users to upload legal PDF documents and legal web pages, creates a vector knowledge base using FAISS and HuggingFace embeddings, and answers legal questions with source references.

> **Disclaimer:** This tool is for educational and research purposes only and does not constitute professional legal advice.

---

## Features

* Upload multiple legal PDF documents
* Process legal information from URLs
* Create a searchable legal knowledge base
* Ask natural language legal questions
* Source-backed responses using RAG
* Powered by Groq LLMs for fast inference
* Interactive Streamlit interface

---

## Tech Stack

* Python
* Streamlit
* LangChain
* FAISS Vector Store
* HuggingFace Embeddings
* Groq LLM
* Selenium URL Loader
* PyPDF2
* Retrieval-Augmented Generation (RAG)

---

## Project Architecture

```text
PDFs / URLs
      │
      ▼
Document Loading
      │
      ▼
Text Chunking
(RecursiveCharacterTextSplitter)
      │
      ▼
Embeddings
(HuggingFace MiniLM)
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Groq LLM
      │
      ▼
Answer + Sources
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/LegalAid-RAG.git
cd LegalAid-RAG
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
Groq_API_Key=YOUR_GROQ_API_KEY
```

Get your API key from Groq.

---

## Run Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Usage

### Step 1: Upload Documents

Upload one or more legal PDF documents.

### Step 2: Add URLs (Optional)

Provide legal article URLs or legal information pages.

### Step 3: Build Knowledge Base

Click **Process Documents**.

The application will:

* Extract document text
* Split text into chunks
* Generate embeddings
* Create a FAISS vector index

### Step 4: Ask Questions

Example:

```text
What penalties can be imposed under Section 20 of the RTI Act?
```

```text
Summarize the provisions of Section 7 of the RTI Act.
```

```text
What exemptions are listed under Section 8?
```

The system retrieves relevant context and generates an answer with source references.

---

## Dependencies

```text
streamlit
langchain==0.3.26
langchain-community
langchain-text-splitters
langchain-huggingface
langchain-groq
python-dotenv
faiss-cpu
sentence-transformers
selenium
unstructured
PyPDF2
```

---

## Future Improvements

* Citation highlighting
* Better legal document chunking
* Support for DOCX and TXT files
* Conversational memory
* Hybrid search (BM25 + Vector Search)
* Legal case law retrieval
* Deployment on Streamlit Cloud

---

## Project Structure

```text
LegalAid-RAG/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── faiss-store-legal.pkl
```

---

## License

This project is released under the MIT License.

---

## Author

Utkarsh Pandey
