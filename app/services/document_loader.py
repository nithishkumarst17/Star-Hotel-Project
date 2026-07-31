from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:

    def __init__(self):
        self.pdf_path = Path("data") / "star hotel.pdf"

    def load_documents(self):
        loader = PyPDFLoader(str(self.pdf_path))
        documents = loader.load()
        return documents