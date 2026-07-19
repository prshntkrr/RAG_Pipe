from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseVectorDB(ABC):

    @abstractmethod
    def add_documents(
        self,
        documents: list[Document]
    ):
        """
        Store documents in the vector database.
        """
        pass

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        k: int = 5
    ):
        """
        Search similar documents.
        """
        pass

    @abstractmethod
    def delete(
        self,
        ids: list[str]
    ):
        """
        Delete documents by IDs.
        """
        pass
