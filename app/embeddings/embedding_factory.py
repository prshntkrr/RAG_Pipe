from app.core.config import settings

from app.embeddings.openai_embedding import OpenAIEmbedding
from app.embeddings.huggingface_embedding import HuggingFaceEmbedding


class EmbeddingFactory:

    @staticmethod
    def get_embedding():

        provider = settings.EMBEDDING_PROVIDER.lower()

        if provider == "openai":
            return OpenAIEmbedding()

        if provider == "huggingface":
            return HuggingFaceEmbedding()

        raise ValueError(
            f"Unsupported embedding provider: {provider}"
        )
