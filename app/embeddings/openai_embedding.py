import uuid

from langchain_openai import OpenAIEmbeddings

from app.core.config import settings
from app.embeddings.base_embedding import BaseEmbedding
from app.models.embedding_record import EmbeddingRecord


class OpenAIEmbedding(BaseEmbedding):

    def __init__(self):

        self.model = OpenAIEmbeddings(
            model=settings.OPENAI_EMBEDDING_MODEL,
            api_key=settings.OPENAI_API_KEY
        )

    def embed_documents(self, documents):

        texts = [
            doc.page_content
            for doc in documents
        ]

        vectors = self.model.embed_documents(texts)

        return vectors

    def embed_query(self, query):

        return self.model.embed_query(query)
