from google.cloud import storage
import os
from collections import defaultdict

bucket_url: 'https://storage.googleapis.com/wrek-01/'
show_dict = defaultdict(list)

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
    # print(public_urls)
    show_urls = []
    mp3_filenames = []
    file = []
    weeks = set()


    for url in public_urls:
        filepath = os.path.join(url)
        filepath = os.path.normpath(filepath)

        filepath = filepath.split(os.sep)

        del filepath[0:3] # results in /<showname>/<week>/<file.mp3>
        week = filepath[1]
        file = filepath[2] # ex. Sun1800.mp3

        if filepath[0] == showname:
            show_urls.append(url)
            show_dict[week].append(url)
            mp3_filenames.append(file)
        else:
            pass

    # print(mp3_filenames)
    # print(show_dict)
    return(show_dict.items(), mp3_filenames)
    # return(show_urls, weeks, filename)
        # upload_file_path = os.path.join(*filepath).replace("\\","/")



    # print(two_urls)

if __name__ == '__main__':
    find_show_url('Mode7')
