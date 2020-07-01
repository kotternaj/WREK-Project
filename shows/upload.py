import os
from google.cloud import storage

def upload_to_gcs(file):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/JSON/WREK-01.json" #Set gloud credentials.
    client = storage.Client() #Set gcloud client.
    bucket = client.get_bucket("wrek-01") #Specify gcloud bucket.
    blob = bucket.blob(file)
    blob.upload_from_filename(file)
    url = blob.public_url
    print(f"Image URL - {url}")

    # gsutil cp -r /show_data gs://wrek-01
if __name__ == '__main__':
    upload_to_gcs('show_data/2020/Mode 7/Week 27/Sun1800_old.mp3')
