import os
from google.cloud import storage


def upload_to_gcs(filepath, file):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/JSON/WREK-01.json" #Set gloud credentials.
    client = storage.Client() #Set gcloud client.
    bucket = client.get_bucket("wrek-01") #Specify gcloud bucket.
    blob = bucket.blob(f"{filepath}/{file}")
    blob.upload_from_filename(file)
    url = blob.public_url
    # return(url)
    print(f"MP3 URL - {url}")
    # mp3_urls.append(url)
    # return(mp3_urls)
    # m3u = create_m3u(mp3_urls, filepath)

if __name__ == '__main__':
    upload_to_gcs('Mode7/30', 'playlist.m3u')
