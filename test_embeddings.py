from rag.embeddings import EmbeddingModel

embedding_model = EmbeddingModel()

documents = [
    "Artificial Intelligence is changing the world.",
    "Machine Learning is a subset of AI.",
    "Python is a programming language."
]

embeddings = embedding_model.embed_documents(documents)

print("Total Embeddings:", len(embeddings))

print()

print("Embedding Dimension:", len(embeddings[0]))

print()

print("First 10 values:")

print(embeddings[0][:10])