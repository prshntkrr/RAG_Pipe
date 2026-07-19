import uuid

from langchain_openai import OpenAIEmbeddings

from app.core.config import settings
from app.embeddings.base_embedding import BaseEmbedding
from app.models.embedding_record import EmbeddingRecord


class OpenAIEmbedding(BaseEmbedding):

    def __init__(self):

        self.model = OpenAIEmbeddings(
            model=settings.OPENAI_EMBEDDING_MODEL
        )

    def embed_documents(self, documents):

        texts = [
            doc.page_content
            for doc in documents
        ]

        vectors = self.model.embed_documents(texts)

        records = []

        for doc, vector in zip(documents, vectors):

            records.append(
                EmbeddingRecord(
                    id=str(uuid.uuid4()),
                    embedding=vector,
                    document=doc.page_content,
                    metadata=doc.metadata
                )
            )

        return records

    def embed_query(self, query):

        return self.model.embed_query(query)
