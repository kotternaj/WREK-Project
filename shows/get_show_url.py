from google.cloud import storage
import os

def list_blobs(bucket_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/JSON/WREK-01.json"    

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)
        print(blob.public_url)

if __name__ == '__main__':
    list_blobs('wrek-01')
