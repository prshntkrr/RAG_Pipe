from pathlib import Path

from app.loaders.pdf_loader import PDFLoader
from app.loaders.csv_loader import CSVLoader
from app.loaders.excel_loader import ExcelLoader


class LoaderFactory:

    _loaders = {
        ".pdf": PDFLoader,
        ".csv": CSVLoader,
        ".xlsx": ExcelLoader,
    }

    @classmethod
    def get_loader(cls, file_path: str):

        extension = Path(file_path).suffix.lower()

        loader_class = cls._loaders.get(extension)

        if loader_class is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loader_class()