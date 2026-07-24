from uuid import UUID

from sqlalchemy.orm import Session

from app.models.collection_document import CollectionDocument


class CollectionDocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def add_documents(
        self,
        collection_id: UUID,
        document_ids: list[UUID]
    ):

        mappings = [
            CollectionDocument(
                collection_id=collection_id,
                document_id=document_id
            )
            for document_id in document_ids
        ]

        self.db.add_all(mappings)

        self.db.commit()
