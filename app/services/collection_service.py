from sqlalchemy.orm import Session

from app.repositories.collection_repository import CollectionRepository


class CollectionService:

    def __init__(self, db: Session):
        self.repo = CollectionRepository(db)

    def create(self, data):
        return self.repo.create(
            data.name,
            data.description,
        )

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, collection_id):
        return self.repo.get_by_id(collection_id)

    def delete(self, collection):
        self.repo.delete(collection)
