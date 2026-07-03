import uuid
import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE


class VectorStore:
    """
    Handles storage and retrieval of document embeddings using ChromaDB.
    """

    def __init__(self, db_path="vector_db", collection_name="documents"):

        self.client = chromadb.PersistentClient(
            path=db_path,
            tenant=DEFAULT_TENANT,
            database=DEFAULT_DATABASE
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, chunks, embeddings):

        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:
            ids.append(str(uuid.uuid4()))
            documents.append(chunk.page_content)
            metadatas.append(chunk.metadata)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def document_exists(self, filename):

        results = self.collection.get(
            where={"source": filename}
        )

        return len(results["ids"]) > 0

    def similarity_search(self, query_embedding, k=5):

        return self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k,
            include=["documents", "metadatas", "distances"]
        )

    def count(self):
        return self.collection.count()