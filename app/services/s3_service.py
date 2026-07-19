from pathlib import Path

import boto3

from app.core.config import settings


class S3Service:
    def __init__(self):
        self.client = boto3.client(
            "s3",
            region_name=settings.AWS_REGION
        )

    def upload_file(self, file_path: str, object_key: str) -> str:
        """
        Upload a local file to S3.
        """

        self.client.upload_file(
            Filename=file_path,
            Bucket=settings.S3_BUCKET,
            Key=object_key
        )

        return object_key

    def download_file(self, object_key: str, destination: str):
        """
        Download an S3 object to local storage.
        """

        Path(destination).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.client.download_file(
            settings.S3_BUCKET,
            object_key,
            destination
        )

    def delete_file(self, object_key: str):
        """
        Delete an object from S3.
        """

        self.client.delete_object(
            Bucket=settings.S3_BUCKET,
            Key=object_key
        )

    def file_exists(self, object_key: str) -> bool:
        """
        Check whether an object exists.
        """

        try:
            self.client.head_object(
                Bucket=settings.S3_BUCKET,
                Key=object_key
            )
            return True

        except Exception:
            return False
