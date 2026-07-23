from pathlib import Path

from app.chunking.splitter import ChunkSplitter
from app.core.config import settings
from app.embeddings.embedding_factory import EmbeddingFactory
from app.loaders.loader_factory import LoaderFactory
from app.services.s3_service import S3Service
from app.vectordb.vectordb_factory import VectorDBFactory


class IngestionService:

    def __init__(self):

        self.s3 = S3Service()

        self.splitter = ChunkSplitter()

        self.embedding_service = (
            EmbeddingFactory.get_embedding()
        )

        self.vectordb = (
            VectorDBFactory.get_vectordb()
        )

    def ingest(self, s3_key: str):

        """
        Download document from S3,
        load it,
        split it,
        generate embeddings,
        store them in Vector DB.
        """

        filename = Path(s3_key).name

        local_path = Path(settings.TEMP_DIR) / filename

        self.s3.download_file(
            s3_key,
            str(local_path)
        )

        try:

            # -----------------------
            # Load Document
            # -----------------------

            loader = LoaderFactory.get_loader(
                str(local_path)
            )

            documents = loader.load(
                str(local_path)
            )

            # -----------------------
            # Split into Chunks
            # -----------------------

            chunks = self.splitter.split(
                documents
            )

            # -----------------------
            # Generate Embeddings
            # -----------------------

            embeddings = (
                self.embedding_service.embed_documents(
                    chunks
                )
            )

            # -----------------------
            # Store in Vector DB
            # -----------------------

            self.vectordb.add_documents(
                documents=chunks,
                embeddings=embeddings
            )

            return {
                "status": "success",
                "pages": len(documents),
                "chunks": len(chunks),
                "vectors": len(embeddings)
            }

        finally:

            if local_path.exists():
                local_path.unlink()