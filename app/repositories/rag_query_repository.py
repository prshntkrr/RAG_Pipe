from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.rag_query_log import RAGQueryLog


class RAGQueryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, log: RAGQueryLog):
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log

    def get_all(self):
        return (
            self.db.query(RAGQueryLog)
            .order_by(RAGQueryLog.created_at.desc())
            .all()
        )

    def count(self):
        return self.db.query(RAGQueryLog).count()

    def count_by_status(self, status: str):
        return (
            self.db.query(RAGQueryLog)
            .filter(RAGQueryLog.status == status)
            .count()
        )

    def average_response_time(self):
        return (
            self.db.query(func.avg(RAGQueryLog.response_time_ms))
            .scalar()
        )