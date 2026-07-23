from app.core.config import settings
from app.vectordb.chroma_service import ChromaService


class VectorDBFactory:

    _vectordbs = {
        "chroma": ChromaService,
    }

    @classmethod
    def get_vectordb(cls):

        db_class = cls._vectordbs.get(
            settings.VECTOR_DB.lower()
        )

        if not db_class:
            raise ValueError(
                f"Unsupported Vector DB: {settings.VECTOR_DB}"
            )

        return db_class()