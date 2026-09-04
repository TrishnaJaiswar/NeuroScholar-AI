from pydantic import BaseModel
from typing import List, Optional, Any


# ---------- Citations ----------

class CitationItem(BaseModel):
    source: str
    page: int
    quote: str


# ---------- Chat ----------

class ChatRequest(BaseModel):
    question: str
    task: Optional[str] = None
    documents: List[str] = []      # Selected PDF filenames


class ChatResponse(BaseModel):
    answer: str
    task: str
    citations: List[CitationItem] = []


# ---------- Chat Sessions ----------

class SessionCreate(BaseModel):
    title: str
    task: str
    messages: List[Any] = []


class SessionOut(BaseModel):
    id: int
    title: str
    task: str
    messages: List[Any]

    class Config:
        from_attributes = True