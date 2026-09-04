# 🧠 NeuroScholar AI

### Agentic Multi-Document Research Intelligence Platform

NeuroScholar AI is a full-stack **Agentic AI** platform that enables researchers to interact with multiple scientific papers using **Hybrid RAG**, **LangGraph Multi-Agent workflows**, **FAISS vector search**, and **citation-grounded report generation**.

It supports research chat, literature reviews, paper comparison, trend analysis, persistent research sessions, and PDF export—all within a modern React dashboard.

---

## 🚀 Features

* 💬 **Research Chat** with Hybrid RAG
* 📚 **Literature Review** generation
* 📄 **Compare Papers** side-by-side
* 📈 **Trend Analysis** across multiple papers
* 🔍 **Hybrid Retrieval** (FAISS + BM25 + Multi-Query)
* ✅ **Citation Verification** with grounded evidence
* 📑 **Multi-PDF Knowledge Base**
* 🤖 **LangGraph Multi-Agent Workflow**
* 🗂️ **Persistent Chat History** using SQLite
* 📤 **Export Academic Reports as PDF**

---

## 🏗️ Architecture

```text
                   React + Zustand Frontend
        ┌─────────────────────────────────────────┐
        │ Landing • Dashboard • Workspace • Chat │
        └──────────────────┬──────────────────────┘
                           │
                     FastAPI Backend
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
  LangGraph Multi-Agent                 Session Storage
        │                                     │
  Planner Agent                        SQLite Database
        │
  Retrieval Agent
        │
 Hybrid RAG (FAISS + BM25)
        │
 Research Agent
        │
 Analysis Agent
        │
 Citation Agent
        │
 Report Agent
        │
  Academic PDF Generator
```

---

## 🤖 Multi-Agent Workflow

| Agent     | Responsibility                                   |
| --------- | ------------------------------------------------ |
| Planner   | Detects workflow and creates execution plan      |
| Retrieval | Hybrid retrieval using FAISS + BM25              |
| Research  | Extracts research insights from retrieved chunks |
| Analysis  | Compares papers & identifies trends              |
| Citation  | Generates grounded source citations              |
| Report    | Produces publication-style academic report       |

---

## 🖥️ Dashboard Workflows

| Workflow             | Description                             |
| -------------------- | --------------------------------------- |
| 💬 Research Chat     | Ask questions across uploaded papers    |
| 📚 Literature Review | Generate structured literature reviews  |
| 📄 Compare Papers    | Compare methodology, datasets & results |
| 📈 Trend Analysis    | Discover emerging research trends       |

---

## 🧠 Tech Stack

| Layer            | Technology                           |
| ---------------- | ------------------------------------ |
| Frontend         | React, Tailwind CSS                  |
| State Management | Zustand                              |
| Backend          | FastAPI                              |
| AI Framework     | LangGraph                            |
| LLM              | Groq                                 |
| RAG              | LangChain                            |
| Retrieval        | FAISS + BM25 + Multi-Query Retriever |
| Embeddings       | HuggingFace (all-MiniLM-L6-v2)       |
| Database         | SQLite                               |
| PDF Export       | ReportLab                            |

---

## 📂 Project Structure

```text
NeuroScholar-AI
│
├── backend
│   ├── agents
│   │   ├── planner_agent.py
│   │   ├── retrieval_agent.py
│   │   ├── research_agent.py
│   │   ├── analysis_agent.py
│   │   ├── citation_agent.py
│   │   └── report_agent.py
│   │
│   ├── graph
│   │   ├── workflow.py
│   │   └── state.py
│   │
│   ├── rag
│   │   └── Hybrid_pipeline.py
│   │
│   ├── routes
│   │   ├── upload.py
│   │   └── documents.py
│   │
│   ├── utils
│   │   └── pdf_generator.py
│   │
│   ├── main.py
│   ├── schemas.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── layouts
│   │   ├── pages
│   │   ├── services
│   │   └── store
│   │
│   └── package.json
│
└── README.md
```

---

## ✨ Core Capabilities

### 1. Hybrid RAG

* FAISS semantic retrieval
* BM25 keyword retrieval
* Ensemble retriever
* Multi-query expansion
* Cross-document reasoning

### 2. Multi-PDF Intelligence

* Upload multiple research papers
* Select specific PDFs
* Retrieve only selected documents
* Source-aware citations

### 3. Persistent Research Sessions

* SQLite chat history
* Restore previous conversations
* Workflow-specific memory
* Dashboard research history

### 4. Academic Report Generation

* Abstract
* Introduction
* Key Findings
* Comparative Analysis
* Limitations
* Conclusion
* References
* PDF Export

---

## 📡 API Endpoints

| Method | Endpoint         | Description           |
| ------ | ---------------- | --------------------- |
| GET    | `/`              | Health check          |
| POST   | `/chat`          | Agentic research chat |
| POST   | `/upload`        | Upload PDF            |
| GET    | `/documents`     | List indexed PDFs     |
| GET    | `/sessions`      | Research history      |
| POST   | `/sessions`      | Create session        |
| PUT    | `/sessions/{id}` | Update session        |
| POST   | `/export`        | Export PDF report     |

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/NeuroScholar-AI.git

cd NeuroScholar-AI
```

### 2. Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\\Scripts\\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

### 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## 🔑 Environment Variables

Create `backend/.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 📸 Screenshots

> Add these images inside `/assets`

```text
assets/
├── landing.png
├── dashboard.png
├── literature_review.png
├── compare_papers.png
├── trend_analysis.png
└── architecture.png
```

Then reference them:

```md
<img width="898" height="411" alt="image" src="https://github.com/user-attachments/assets/e487100b-7a5f-4350-b4c2-d816881d431c" />


<img width="950" height="414" alt="image" src="https://github.com/user-attachments/assets/4f2b0dcb-dc33-4e6e-bc9c-1b1d36531052" />

```

---

## 🎯 Resume Highlights

* Built a **6-Agent LangGraph workflow** for scientific research automation.
* Implemented **Hybrid RAG** using FAISS, BM25, and Multi-Query Retrieval.
* Developed **multi-document reasoning** with citation-grounded responses.
* Designed a **React + FastAPI** full-stack architecture with persistent SQLite sessions.
* Generated publication-style research reports with automatic PDF export.

---

## 👩‍💻 Author

**Trishna Jaiswar**

AI Engineer | Agentic AI • RAG • LangGraph • FastAPI • React

GitHub: `https://github.com/TrishnaJaiswar`

LinkedIn: `linkedin.com/in/trishna-jaiswar-a6a230322`

---

## 📜 License

This project is licensed under the **MIT License**.
