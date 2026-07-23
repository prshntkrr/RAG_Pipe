import uuid

import chromadb
from langchain_core.documents import Document

from app.core.config import settings
from app.vectordb.base_vectordb import BaseVectorDB


class ChromaService(BaseVectorDB):
    """
    ChromaDB implementation of BaseVectorDB.

    Responsibilities:
    - Connect to Chroma
    - Create/Open collection
    - Store embeddings
    - Search embeddings
    - Delete embeddings
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION
        )

    def add_documents(
        self,
        documents: list[Document],
        embeddings: list[list[float]]
    ) -> None:
        """
        Store documents and embeddings in Chroma.
        """

        if len(documents) != len(embeddings):
            raise ValueError(
                "Documents count and embeddings count must be equal."
            )

        ids = [
            str(uuid.uuid4())
            for _ in documents
        ]

        texts = [
            doc.page_content
            for doc in documents
        ]

        metadatas = [
            doc.metadata
            for doc in documents
        ]

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )

    def similarity_search(
        self,
        embedding: list[float],
        k: int = 5
    ):
        """
        Search similar vectors.
        """

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=k,
            include=[
                "documents",
                "metadatas",
                "distances",
            ]
        )

    def delete(
        self,
        ids: list[str]
    ) -> None:
        """
        Delete vectors from Chroma.
        """

        self.collection.delete(ids=ids)

    def count(self) -> int:
        """
        Returns number of stored vectors.
        """

        return self.collection.count()

    def reset(self):
        """
        Deletes all vectors from the collection.
        Useful during development.
        """

        self.client.delete_collection(
            settings.CHROMA_COLLECTION
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION
        )