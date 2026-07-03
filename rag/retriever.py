from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def retrieve(self, query, k=5):

        embedding = self.embedding_model.embed_query(query)

        return self.vector_store.similarity_search(
            embedding,
            k=k
        )