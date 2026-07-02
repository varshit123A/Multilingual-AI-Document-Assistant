from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore

# Load PDF
loader = PDFLoader("uploads/sample.pdf")
documents = loader.load()

# Split
splitter = DocumentSplitter()
chunks = splitter.split(documents)

print("Chunks:", len(chunks))

# Generate embeddings
embedding_model = EmbeddingModel()

texts = [chunk.page_content for chunk in chunks]

embeddings = embedding_model.embed_documents(texts)

# Store
vector_db = VectorStore()

vector_db.add_documents(chunks, embeddings)

print("Documents Stored:", vector_db.count())