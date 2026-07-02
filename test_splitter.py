from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter

loader = PDFLoader("uploads/sample.pdf")
documents = loader.load()

print("Documents:", len(documents))
print("Characters:", len(documents[0].page_content))
print(repr(documents[0].page_content[:200]))

splitter = DocumentSplitter()

chunks = splitter.split(documents)

print("Chunks:", len(chunks))