from fastapi import APIRouter

from app.models.query import QueryRequest
from app.models.query_response import QueryResponse
from app.services.query_service import QueryService
from app.db.session import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/query",
    tags=["Query"]
)



@router.post("/", response_model=QueryResponse)
def query_document(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    query_service = QueryService(db)

    return query_service.ask(request.question)

# @router.post("/query")
# def query_document(request: QueryRequest):

#     results = retriever.retrieve(request.question)

#     return results