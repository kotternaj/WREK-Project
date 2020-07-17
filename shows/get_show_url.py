from google.cloud import storage
import os
from .current_week import current_week
from .create_m3u import create_m3u
from .upload import upload_to_gcs
from .split_url import split_url

def list_blobs(bucket_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/JSON/WREK-01.json"
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    public_urls = []

    for blob in blobs:
        public_urls.append(blob.public_url)
    return(public_urls)

def find_show_url(showname):
    public_urls = list_blobs('wrek-01')
    show_urls = []

    for url in public_urls:
        filepath, week, file = split_url(url)
        # filepath = os.path.join(url)
        # filepath = os.path.normpath(filepath)
        # filepath = filepath.split(os.sep)
        # del filepath[0:3] #/<showname>/<week>/<mp3>
        # week = filepath[1]
        # file = filepath[2] #ex. Sun1800.mp3

        if filepath[0] == showname and week == str(current_week()):
            local_path = str(filepath[0] + '/' + filepath[1])
            show_urls.append(url)
        else:
            pass
    print(show_urls, local_path)
    return(show_urls, local_path)
