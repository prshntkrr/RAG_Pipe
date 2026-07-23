from fastapi import APIRouter

from app.llm.openai_service import OpenAIService
from app.models.query import QueryRequest
from app.prompts.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever

router = APIRouter()

retriever = Retriever()
llm = OpenAIService()


@router.post("/query")
def query_document(request: QueryRequest):

    results = retriever.retrieve(request.question)

    prompt = PromptBuilder.build(
        request.question,
        results
    )

    answer = llm.generate(prompt)

    return {
        "answer": answer
    }