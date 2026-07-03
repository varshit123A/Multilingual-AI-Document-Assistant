from langchain_google_genai import GoogleGenerativeAIEmbeddings


class EmbeddingModel:
    """
    Generates embeddings using Google's embedding model.
    """

    def __init__(self):
        self.model = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004"
        )

    def embed_documents(self, documents):

        if len(documents) > 0 and hasattr(documents[0], "page_content"):
            texts = [doc.page_content for doc in documents]
        else:
            texts = documents

        return self.model.embed_documents(texts)

    def embed_query(self, query):

        return self.model.embed_query(query)