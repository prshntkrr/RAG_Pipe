from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseVectorDB(ABC):

    @abstractmethod
    def add_documents(
        self,
        documents: list[Document],
        embeddings: list[list[float]]
    ) -> None:
        pass

    @abstractmethod
    def similarity_search(
        self,
        embedding: list[float],
        k: int = 5
    ):
        pass

    @abstractmethod
    def delete(
        self,
        ids: list[str]
    ) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass