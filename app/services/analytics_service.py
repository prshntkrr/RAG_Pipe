from sqlalchemy.orm import Session

from app.repositories.rag_query_repository import RAGQueryRepository


class AnalyticsService:

    def __init__(self, db: Session):
        self.repository = RAGQueryRepository(db)

    def get_summary(self):
        total = self.repository.count()
        success = self.repository.count_by_status("SUCCESS")
        failed = self.repository.count_by_status("FAILED")
        avg_time = self.repository.average_response_time()

        return {
            "total_queries": total,
            "successful_queries": success,
            "failed_queries": failed,
            "average_response_time_ms": round(avg_time or 0, 2)
        }

    def get_history(self):
        return self.repository.get_all()
