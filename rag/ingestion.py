from pathlib import Path

from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class DocumentIngestion:
    """
    Complete ingestion pipeline:
    PDF → Chunks → Embeddings → ChromaDB
    """

    def __init__(self):
        self.splitter = DocumentSplitter()
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def ingest(self, pdf_path):
        filename = Path(pdf_path).name

        # Skip if already indexed
        if self.vector_store.document_exists(filename):
            print(f"{filename} is already indexed.")
            return 0

        # Load PDF
        loader = PDFLoader(pdf_path)
        documents = loader.load()

        # Split into chunks
        chunks = self.splitter.split(documents)

        # Add filename to metadata
        for chunk in chunks:
            chunk.metadata["source"] = filename

        # Generate embeddings
        embeddings = self.embedding_model.embed_documents(chunks)

        # Store in ChromaDB
        self.vector_store.add_documents(chunks, embeddings)

        return len(chunks)