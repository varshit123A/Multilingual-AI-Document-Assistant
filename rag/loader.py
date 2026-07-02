from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader


class PDFLoader:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")

    def load(self):
        loader = PyMuPDFLoader(str(self.pdf_path))
        return loader.load()