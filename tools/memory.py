from datetime import datetime
from uuid import uuid4
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from app.services.embeddings import create_embedding
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "memories"

client = QdrantClient(host="localhost", port=6333)


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str):
    return model.encode(text).tolist()


def add(memory):
    embedding = create_embedding(memory["text"])
    client.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=[
            PointStruct(
                id=str(uuid4()),
                vector=embedding,
                payload={
                    "text": memory["text"],
                    "category": memory["category"],
                    "importance": memory["importance"],
                    "created_at": datetime.utcnow().isoformat(),
                },
            )
        ],
    )
