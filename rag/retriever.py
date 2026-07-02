from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()
        self.vector_db = VectorStore()

    def retrieve(self, query, k=3):

        query_embedding = self.embedding_model.embed_query(query)

        results = self.vector_db.similarity_search(
            query_embedding=query_embedding,
            k=k
        )

        return results