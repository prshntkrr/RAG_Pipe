from app.embeddings.embedding_factory import EmbeddingFactory
from app.vectordb.vectordb_factory import VectorDBFactory


class Retriever:

    def __init__(self):

        self.embedding_service = EmbeddingFactory.get_embedding()
        self.vectordb = VectorDBFactory.get_vectordb()

    def retrieve(
        self,
        query: str,
        k: int = 3
    ):

        query_embedding = self.embedding_service.embed_query(query)

        # print(f"Query: {query}")
        # print(f"Embedding dimension: {len(query_embedding)}")

        results = self.vectordb.similarity_search(
            embedding=query_embedding,
            k=k
        )

        # print(results)

        return results