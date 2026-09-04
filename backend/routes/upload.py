from fastapi import APIRouter, UploadFile, File, HTTPException
import os

# from rag.Hybrid_pipeline import ingest_pdf   # ← ADD

router = APIRouter()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    # ingest_pdf(path)      # ← ADD (indexes into RAG)

    return {
        "filename": file.filename,
        "status": "uploaded"
    }