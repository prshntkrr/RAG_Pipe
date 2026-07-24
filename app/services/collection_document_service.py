from sqlalchemy.orm import Session

from app.repositories.collection_document_repository import (
    CollectionDocumentRepository,
)


class CollectionDocumentService:

    def __init__(self, db: Session):
        self.repo = CollectionDocumentRepository(db)

    def add_documents(
        self,
        collection_id,
        document_ids,
    ):
        self.repo.add_documents(
            collection_id,
            document_ids,
        )
