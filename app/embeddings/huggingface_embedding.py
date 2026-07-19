from app.embeddings.base_embedding import BaseEmbedding


class HuggingFaceEmbedding(BaseEmbedding):

    def embed_documents(self, documents):
        raise NotImplementedError(
            "HuggingFace embedding is not implemented yet."
        )

    def embed_query(self, query):
        raise NotImplementedError(
            "HuggingFace embedding is not implemented yet."
        )
