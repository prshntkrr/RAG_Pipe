from dataclasses import dataclass


@dataclass
class EmbeddingRecord:
    """
    Represents one vector record that will be stored
    in the vector database.
    """

    id: str

    embedding: list[float]

    document: str

    metadata: dict
