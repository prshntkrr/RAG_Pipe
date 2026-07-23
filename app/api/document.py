from pathlib import Path
import shutil
import uuid


from app.core.config import settings
from app.services.s3_service import S3Service
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.ingestion_service import IngestionService
from app.vectordb.vectordb_factory import VectorDBFactory

router = APIRouter(prefix="/documents", tags=["Documents"])

s3_service = S3Service()
ingestion_service = IngestionService()
vectordb = VectorDBFactory.get_vectordb()

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".csv",
    ".xlsx",
    ".docx",
    ".txt"
}

@router.get("/count")
def get_vector_count():

    return {
        "total_vectors": vectordb.count()
    }

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF to S3.
    """

    extension = Path(file.filename).suffix.lower()

    # Validate file type
    if extension not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

    # Create temp directory if it doesn't exist
    Path(settings.TEMP_DIR).mkdir(parents=True, exist_ok=True)

    # Generate a unique filename
    unique_name = f"{uuid.uuid4()}_{file.filename}"

    temp_path = Path(settings.TEMP_DIR) / unique_name

    # Save uploaded file temporarily
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # S3 object key
    s3_key = f"documents/{unique_name}"

    try:
        # Upload to S3
        s3_service.upload_file(
            str(temp_path),
            s3_key
        )

        # Start ingestion
        result = ingestion_service.ingest(s3_key)

        return {
            "message": "Document uploaded and processed successfully.",
            "file_name": file.filename,
            "s3_key": s3_key,
            "pages": result["pages"],
            "chunks": result["chunks"]
        }

    finally:
        # Remove local temp file
        if temp_path.exists():
            temp_path.unlink()
