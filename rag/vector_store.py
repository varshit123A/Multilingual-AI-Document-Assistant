import uuid
from chromadb import PersistentClient


class VectorStore:
    """
    Handles storage and retrieval of document embeddings using ChromaDB.
    """

    def __init__(self, db_path="vector_db", collection_name="documents"):
        self.client = PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, chunks, embeddings):
        """
        Add document chunks to ChromaDB.
        """

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
            metadatas=metadatas,
        )

    def document_exists(self, filename):
        """
        Check whether a document has already been indexed.
        """

        results = self.collection.get(
            where={"source": filename}
        )

        return len(results["ids"]) > 0

    def similarity_search(self, query_embedding, k=5):
        """
        Retrieve the top-k most similar documents.
        """

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k,
            include=["documents", "metadatas", "distances"],
        )

        return results

    def count(self):
        """
        Return the total number of stored chunks.
        """

        return self.collection.count()