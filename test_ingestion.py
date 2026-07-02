from rag.ingestion import DocumentIngestion

pipeline = DocumentIngestion()

chunks = pipeline.ingest("uploads/sample.pdf")

print(f"Indexed {chunks} chunks successfully.")
