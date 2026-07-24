from uuid import UUID

from pydantic import BaseModel


class AddDocumentsRequest(BaseModel):
    document_ids: list[UUID]
