from app.embeddings.embedding_factory import EmbeddingFactory
from app.vectordb.vectordb_factory import VectorDBFactory


class Retriever:

    def __init__(self):

        self.embedding_service = (
            EmbeddingFactory.get_embedding()
        )

        self.vectordb = (
            VectorDBFactory.get_vectordb()
        )

    def retrieve(
        self,
        query: str,
        k: int = 3
    ):

        # Step 1: Convert the user's question into an embedding
        query_embedding = self.embedding_service.embed_query(query)

        print(f"Query: {query}")
        print(f"Embedding dimension: {len(query_embedding)}")

        return query_embedding