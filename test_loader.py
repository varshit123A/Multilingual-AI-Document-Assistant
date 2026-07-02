from rag.loader import PDFLoader

loader = PDFLoader("uploads/sample.pdf")

documents = loader.load()

print(f"Pages Loaded: {len(documents)}")

print()

print(documents[0].page_content[:500])

print()

print(documents[0].metadata)