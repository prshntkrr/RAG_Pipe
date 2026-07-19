from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from app.core.config import settings


class ChunkSplitter:
    """
    Splits LangChain Documents into smaller chunks.
    """

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            is_separator_regex=False
        )

    def split(
        self,
        documents: list[Document]
    ) -> list[Document]:

        return self.splitter.split_documents(documents)
