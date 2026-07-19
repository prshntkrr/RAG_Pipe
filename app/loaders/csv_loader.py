from langchain_core.documents import Document

from app.loaders.base_loader import BaseLoader


class CSVLoader(BaseLoader):

    def load(self, file_path: str) -> list[Document]:
        raise NotImplementedError(
            "CSV Loader will be implemented later."
        )