from pathlib import Path

from langchain_community.document_loaders import (
    CSVLoader,
    JSONLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredExcelLoader,
    UnstructuredMarkdownLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)

LOADERS = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
    ".csv": CSVLoader,
    ".docx": UnstructuredWordDocumentLoader,
    ".pptx": UnstructuredPowerPointLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".md": UnstructuredMarkdownLoader,
    ".json": lambda p: JSONLoader(
        file_path=str(p),
        jq_schema=".",
        text_content=False,
    ),
}

def load_documents(data_dir: str = "data"):
    docs = []

    for file in Path(data_dir).iterdir():
        if not file.is_file():
            continue

        ext = file.suffix.lower()

        if ext in LOADERS:
            loader = LOADERS[ext](str(file))
            docs.extend(loader.load())

    return docs