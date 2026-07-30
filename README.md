# 🩺 Medical Chatbot using Generative AI (Llama-2)

[](https://www.python.org/)
[](https://flask.palletsprojects.com/)
[](https://www.langchain.com/)
[](https://www.pinecone.io/)

A state-of-the-art Medical Chatbot that leverages **Retrieval-Augmented Generation (RAG)**. The system processes medical literature to provide context-aware answers to user health queries using the **Llama-2** large language model.

-----

## 📖 Overview

Most generic LLMs suffer from "hallucinations" when asked specific medical questions. This project solves that by grounding the model's responses in verified medical data. By using **Pinecone** as a vector database and **LangChain** for orchestration, the chatbot retrieves relevant snippets from medical textbooks before generating a response.

## 🏗️ Architecture

1.  **PDF Loading:** Extracts text from specialized medical books.
2.  **Text Splitting:** Breaks down text into small, semantic chunks.
3.  **Embedding Generation:** Converts text chunks into vector representations using HuggingFace.
4.  **Vector Storage:** Indexes embeddings in **Pinecone** for lightning-fast similarity search.
5.  **RAG Pipeline:** When a user asks a question, the system retrieves the top "K" relevant chunks and passes them to **Llama-2** to formulate an answer.

-----

## 🛠️ Project Structure

```text
.
├── data/                 # PDF medical books
├── model/                # Llama-2 quantised models (.bin files)
├── static/               # Frontend assets (CSS, Images)
├── templates/            # HTML interface
├── app.py                # Main Flask Application
├── helper.py             # Text processing & Embedding logic
├── prompt.py             # Custom System Prompts
├── store_index.py        # Vector Database Ingestion Script
├── requirements.txt      # Python dependencies
└── setup.py              # Packaging configuration
```

-----

## 🚀 Getting Started

### 1\. Prerequisites

  * Python 3.9 or higher
  * Pinecone API Key
  * Llama-2 Model weights (GGUF/GGML format)

### 2\. Installation

```bash
# Clone the repo
git clone https://github.com/Sv2972/Medical-Chatbot-using-LLMs.git

# Navigate to the specific project folder
cd Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS-main

# Install dependencies
pip install -r requirements.txt
```

### 3\. Environment Setup

Create a `.env` file in the root directory:

```env
PINECONE_API_KEY = "your-api-key"
PINECONE_API_ENV = "your-environment-region"
```

### 4\. Data Ingestion

Push your medical data to the Pinecone Cloud:

```bash
python store_index.py
```

### 5\. Run the Application

```bash
python app.py
```

Visit `http://localhost:8080` in your browser.

-----

## 🧠 Key Features

  * **Quantized LLM Support:** Uses CTransformers to run Llama-2 efficiently on consumer hardware (CPU/GPU).
  * **Persistent Memory:** The chatbot retains context for the duration of the session.
  * **Custom Prompting:** Tailored system prompts to ensure the bot behaves like a professional medical assistant.

## 🛡️ Disclaimer

*This chatbot is for educational purposes only. The information provided should not be considered professional medical advice. Always consult with a qualified healthcare provider for medical concerns.*

-----

## 📜 License

Distributed under the Apache License. See `LICENSE` for more information.

-----

**Author:** [Sv2972](https://www.google.com/search?q=https://github.com/Sv2972)
