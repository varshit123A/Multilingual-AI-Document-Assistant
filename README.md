# 📄 Multilingual AI Document Assistant

An AI-powered document assistant that allows users to upload PDF documents, ask natural language questions, generate summaries, translate responses into multiple Indian languages, and listen to answers using text-to-speech.

Built using **Streamlit**, **LangChain**, **Google Gemini**, **ChromaDB**, and **Sentence Transformers**.

---

## 🚀 Features

- 📂 Upload PDF documents
- 📑 Automatic document ingestion and indexing
- 🔍 Semantic search using vector embeddings
- 🤖 Ask questions about uploaded documents (RAG)
- 📝 AI-powered document summarization
- 🌐 Translate answers into multiple Indian languages
- 🔊 Text-to-Speech support
- 💾 Persistent vector database using ChromaDB
- ⚡ Fast semantic retrieval

---

## 🏗️ Architecture

```
                PDF Upload
                     │
                     ▼
          Document Extraction
                     │
                     ▼
           Text Chunking
                     │
                     ▼
      Sentence Transformer Embeddings
                     │
                     ▼
             ChromaDB Vector Store
                     │
                     ▼
         Semantic Similarity Search
                     │
                     ▼
      Google Gemini (LangChain)
                     │
                     ▼
     Answer • Summary • Translation
                     │
                     ▼
              Text-to-Speech
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangChain

### AI Model
- Google Gemini 2.5 Flash

### Embeddings
- Sentence Transformers

### Vector Database
- ChromaDB

### PDF Processing
- PyPDF2
- PyMuPDF

### Translation
- Google Gemini

### Text-to-Speech
- gTTS

---

## 📁 Project Structure

```
multilingual-ai-document-assistant/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── uploads/
│
├── vector_db/
│
└── rag/
    ├── ingestion.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retriever.py
    ├── qa_chain.py
    └── prompt.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/multilingual-ai-document-assistant.git

cd multilingual-ai-document-assistant
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📚 Workflow

1. Upload a PDF document.
2. Extract text from the document.
3. Split the text into smaller chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in ChromaDB.
6. Ask questions in natural language.
7. Retrieve relevant chunks using semantic search.
8. Send retrieved context to Gemini.
9. Display the generated answer.
10. Translate or convert the response into speech.

---

## 🌍 Supported Languages

- English
- Telugu
- Hindi
- Tamil
- Kannada
- Malayalam

---

## 📦 Major Libraries

- Streamlit
- LangChain
- LangChain Google GenAI
- ChromaDB
- Sentence Transformers
- Transformers
- PyPDF2
- PyMuPDF
- gTTS
- Torch
- NumPy
- Pandas

---

## 💡 Future Improvements

- Support for Word and PowerPoint documents
- OCR for scanned PDFs
- Conversation history
- Multi-document querying
- User authentication
- Cloud database integration
- Voice input
- Citation-based responses
- Document highlighting
- Chat history export

---

## 👨‍💻 Author

**Varshit Sai Akkala**

GitHub:
https://github.com/varshit123A

---

## 📜 License

This project is licensed under the MIT License.
