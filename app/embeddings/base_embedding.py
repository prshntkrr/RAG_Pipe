from abc import ABC, abstractmethod

from langchain_core.documents import Document

from app.models.embedding_record import EmbeddingRecord


class BaseEmbedding(ABC):
    """
    Base class for embedding providers.
    """

    @abstractmethod
    def embed_documents(
        self,
        documents: list[Document]
    ) -> list[EmbeddingRecord]:
        """
        Embed multiple documents.
        """
        pass

    @abstractmethod
    def embed_query(
        self,
        query: str
    ) -> list[float]:
        """
        Embed a user query.
        """
        pass
