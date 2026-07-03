import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


class EmbeddingModel:
    """
    Generates embeddings using Google's Gemini Embedding model.
    """

    def __init__(self):
        self.model = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    def embed_documents(self, documents):

        if len(documents) > 0 and hasattr(documents[0], "page_content"):
            texts = [doc.page_content for doc in documents]
        else:
            texts = documents

        return self.model.embed_documents(texts)

    def embed_query(self, query):

        return self.model.embed_query(query)