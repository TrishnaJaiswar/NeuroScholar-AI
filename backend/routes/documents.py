from fastapi import APIRouter
import os

router = APIRouter()

UPLOAD_DIR = "data"

@router.get("/documents")
def get_documents():
    files = []

    if os.path.exists(UPLOAD_DIR):
        for file in os.listdir(UPLOAD_DIR):
            if file.endswith(".pdf"):
                files.append({"name": file})

    return files