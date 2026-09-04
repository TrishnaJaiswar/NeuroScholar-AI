from sqlalchemy import Column, Integer, String, Text
from database import Base

class ChatSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    task = Column(String, nullable=False)
    messages = Column(Text, nullable=False)