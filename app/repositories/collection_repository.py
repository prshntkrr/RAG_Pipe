from sqlalchemy.orm import Session

from app.models.collection import Collection


class CollectionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, description: str | None):
        collection = Collection(
            name=name,
            description=description,
        )

        self.db.add(collection)
        self.db.commit()
        self.db.refresh(collection)

        return collection

    def get_all(self):
        return self.db.query(Collection).all()

    def get_by_id(self, collection_id):
        return (
            self.db.query(Collection)
            .filter(Collection.id == collection_id)
            .first()
        )

    def delete(self, collection):
        self.db.delete(collection)
        self.db.commit()
