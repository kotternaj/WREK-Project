from google.cloud import storage
import os
from .current_week import current_week
from .create_m3u import create_m3u
from .upload import upload_to_gcs

bucket_url: 'https://storage.googleapis.com/wrek-01/'

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
        filepath = os.path.join(url)
        filepath = os.path.normpath(filepath)
        filepath = filepath.split(os.sep)

        del filepath[0:3] #/<showname>/<week>/<mp3>
        week = filepath[1]
        file = filepath[2] #ex. Sun1800.mp3

        if filepath[0] == showname and week == str(current_week()-1):
            local_path = str(filepath[0] + '/' + filepath[1])
            show_urls.append(url)
        else:
            # print('show name does NOT match')
            pass
    print(show_urls, local_path)
    return(show_urls, local_path)
    # upload_to_gcs(create_m3u(show_urls, local_path))


def get_m3u_link(showname):
    m3u_dict = {}
    bucket_contents = list_blobs('wrek-01')
    # print(bucket_contents)
    for url in bucket_contents:
        filepath = os.path.join(url)
        filepath = os.path.normpath(filepath)
        filepath = filepath.split(os.sep)

        del filepath[0:3] #/<showname>/<week>/<mp3>
        print(filepath)
        week = filepath[1]
        file = filepath[2] #ex. Sun1800.mp3
        if file == 'playlist.m3u':
            if filepath[0] == showname:
                m3u_dict.update({ week: url })
    return(m3u_dict.items())

    # print(two_urls)

if __name__ == '__main__':
    find_show_url('Mode7')
