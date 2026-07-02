from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Generates embeddings for text using Sentence Transformers.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        """
        Generate embeddings for LangChain Documents or plain strings.
        """

        # If LangChain Documents are passed
        if len(documents) > 0 and hasattr(documents[0], "page_content"):
            texts = [doc.page_content for doc in documents]
        else:
            texts = documents

        return self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def embed_query(self, query):
        """
        Generate embedding for a single query.
        """

        return self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )