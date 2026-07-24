from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.collection import (
    CollectionCreate,
    CollectionResponse,
)
from uuid import UUID

from app.schemas.collection_document import AddDocumentsRequest
from app.services.collection_document_service import (
    CollectionDocumentService,
)
from app.services.collection_service import CollectionService

router = APIRouter(prefix="/collections", tags=["Collections"])


@router.post("/{collection_id}/documents")
def add_documents(
    collection_id: UUID,
    request: AddDocumentsRequest,
    db: Session = Depends(get_db),
):

    service = CollectionDocumentService(db)

    service.add_documents(
        collection_id,
        request.document_ids,
    )

    return {
        "message": "Documents added successfully."
    }

@router.post("", response_model=CollectionResponse)
def create_collection(
    request: CollectionCreate,
    db: Session = Depends(get_db),
):
    service = CollectionService(db)
    return service.create(request)


@router.get("", response_model=list[CollectionResponse])
def get_collections(
    db: Session = Depends(get_db),
):
    service = CollectionService(db)
    return service.get_all()


@router.get("/{collection_id}", response_model=CollectionResponse)
def get_collection(
    collection_id: str,
    db: Session = Depends(get_db),
):
    service = CollectionService(db)

    collection = service.get_by_id(collection_id)

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found",
        )

    return collection


@router.delete("/{collection_id}")
def delete_collection(
    collection_id: str,
    db: Session = Depends(get_db),
):
    service = CollectionService(db)

    collection = service.get_by_id(collection_id)

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found",
        )

    service.delete(collection)

    return {
        "message": "Collection deleted successfully."
    }
