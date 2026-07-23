from fastapi import FastAPI
from app.api.document import router as document_router

app = FastAPI(
    title="RAG API",
    description="Production Ready RAG Pipeline",
    version="1.0.0"
)

app.include_router(document_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to RAG API"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


