from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    # AWS
    AWS_REGION: str
    S3_BUCKET: str

    # Chunking
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    # Local Storage
    TEMP_DIR: str = "temp"

    # Embedding
    EMBEDDING_PROVIDER: str
    OPENAI_EMBEDDING_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    # Vector Database
    VECTOR_DB: str
    CHROMA_PATH: str
    CHROMA_COLLECTION: str


settings = Settings()
