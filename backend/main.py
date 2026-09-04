from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from schemas import (
    ChatRequest,
    ChatResponse,
    SessionCreate,
    SessionOut,
)

from graph.workflow import graph
from utils.pdf_generator import create_pdf

from routes.upload import router as upload_router
from routes.documents import router as documents_router

from database import Base, engine, SessionLocal
from models import ChatSession

import json

# ---------------- FastAPI ----------------

app = FastAPI(
    title="NeuroScholar AI",
    version="1.0.0"
)

# Create SQLite tables
Base.metadata.create_all(bind=engine)

# ---------------- Routers ----------------

app.include_router(upload_router)
app.include_router(documents_router)

# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Health ----------------

@app.get("/")
def root():
    return {"message": "NeuroScholar AI Backend Running"}

# ---------------- Chat ----------------

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    result = graph.invoke({
        "question": req.question,
        "forced_task": req.task,
        "selected_documents": req.documents,
    })

    citations = []

    if result.get("citation"):
        citations = [
            {
                "source": c.source,
                "page": c.page,
                "quote": c.quote,
            }
            for c in result["citation"].citations
        ]

    return ChatResponse(
        answer=result["answer"],
        task=result["planner"].task,
        citations=citations,
    )

# ---------------- Export PDF ----------------

@app.post("/export")
def export_report(req: ChatRequest):

    result = graph.invoke({
        "question": req.question,
        "forced_task": "report_generation",
        "selected_documents": req.documents,
    })

    pdf = create_pdf(result["report"])

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=NeuroScholar_Report.pdf"
        },
    )

# ==========================================================
#                 CHAT SESSION PERSISTENCE
# ==========================================================

# Save new session
@app.post("/sessions")
def save_session(req: SessionCreate):

    db = SessionLocal()

    session = ChatSession(
        title=req.title,
        task=req.task,
        messages=json.dumps(req.messages),
    )

    db.add(session)
    db.commit()
    db.refresh(session)
    db.close()

    return {"id": session.id}

# Get all sessions
@app.get("/sessions")
def get_sessions():

    db = SessionLocal()

    sessions = db.query(ChatSession).all()

    data = [
        {
            "id": s.id,
            "title": s.title,
            "task": s.task,
        }
        for s in sessions
    ]

    db.close()

    return data

# Load one session
@app.get("/sessions/{session_id}")
def load_session(session_id: int):

    db = SessionLocal()

    session = (
        db.query(ChatSession)
        .filter(ChatSession.id == session_id)
        .first()
    )

    db.close()

    if not session:
        return {"error": "Session not found"}

    return {
        "id": session.id,
        "title": session.title,
        "task": session.task,
        "messages": json.loads(session.messages),
    }

# Delete session
@app.delete("/sessions/{session_id}")
def delete_session(session_id: int):

    db = SessionLocal()

    session = (
        db.query(ChatSession)
        .filter(ChatSession.id == session_id)
        .first()
    )

    if session:
        db.delete(session)
        db.commit()

    db.close()

    return {"message": "Session deleted"}