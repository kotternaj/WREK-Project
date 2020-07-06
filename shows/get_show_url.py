from google.cloud import storage
import os


def list_blobs(bucket_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/JSON/WREK-01.json"
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)
        print(blob.public_url)

if __name__ == '__main__':
    list_blobs('wrek-01')
