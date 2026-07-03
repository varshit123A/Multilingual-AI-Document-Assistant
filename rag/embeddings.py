from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Generates embeddings using Sentence Transformers.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device="cpu"
        )

    def embed_documents(self, documents):

        if documents and hasattr(documents[0], "page_content"):
            texts = [doc.page_content for doc in documents]
        else:
            texts = documents

        return self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def embed_query(self, query):

        return self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )