from pathlib import Path

from app.chunking.splitter import ChunkSplitter
from app.core.config import settings
from app.loaders.loader_factory import LoaderFactory
from app.services.s3_service import S3Service


class IngestionService:

    def __init__(self):

        self.s3 = S3Service()

        self.splitter = ChunkSplitter()

    def ingest(self, s3_key: str):

        """
        Download document from S3,
        load it,
        split it,
        return chunks.
        """

        filename = Path(s3_key).name

        local_path = Path(settings.TEMP_DIR) / filename

        # Download file
        self.s3.download_file(
            s3_key,
            str(local_path)
        )

        try:

            # Select appropriate loader
            loader = LoaderFactory.get_loader(
                str(local_path)
            )

            # Read document
            documents = loader.load(
                str(local_path)
            )

            # Split document
            chunks = self.splitter.split(
                documents
            )

            return {

                "pages": len(documents),

                "chunks": len(chunks),

                "documents": documents,

                "chunk_documents": chunks
            }

        finally:

            if local_path.exists():

                local_path.unlink()
