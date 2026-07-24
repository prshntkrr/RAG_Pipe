from pydantic import BaseModel


class SourceResponse(BaseModel):
    file: str
    page: int


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceResponse]
