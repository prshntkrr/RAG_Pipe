from sqlalchemy.orm import Session
from app.llm.openai_service import OpenAIService
from app.prompts.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever
from app.repositories.rag_query_repository import RAGQueryRepository
from app.models.rag_query_log import RAGQueryLog
import time


class QueryService:

    def __init__(self, db: Session):

        self.retriever = Retriever()
        self.llm = OpenAIService()
        self.repository = RAGQueryRepository(db)

    def ask(self, question: str):
        response_time = 0
        try:

            start_time = time.perf_counter()

            results = self.retriever.retrieve(question)

            prompt = PromptBuilder.build(
                question,
                results
            )

            answer = self.llm.generate(prompt)

            sources = [
                {
                    "file": metadata["source"].split("/")[-1],
                    "page": metadata["page"]
                }
                for metadata in results["metadatas"][0]
            ]

            response_time = int(
                (time.perf_counter() - start_time) * 1000
            )

            log = RAGQueryLog(
                question=question,
                answer=answer,
                status="SUCCESS",
                response_time_ms=response_time
            )

            self.repository.create(log)

            return {
                "question": question,
                "answer": answer,
                "sources": sources
            }

        except Exception:

            log = RAGQueryLog(
                question=question,
                answer=None,
                status="FAILED",
                response_time_ms=response_time
            )

            self.repository.create(log)

            raise
