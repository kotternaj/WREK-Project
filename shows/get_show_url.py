from google.cloud import storage
import os
from .current_week import current_week
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
        if filepath[0] == showname and week == str(current_week()-2): # compare showname with all items in public_urls
            local_path = str(filepath[0] + '/' + filepath[1])
            show_urls.append(url) # if they match append show_urls
        else:
            pass
    return(show_urls, local_path)
