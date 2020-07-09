from google.cloud import storage
import os

bucket_url: 'https://storage.googleapis.com/wrek-01/'

def list_blobs(bucket_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/JSON/WREK-01.json"

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    public_urls = []
    # url_dict = {}
    # key_list = []

    for blob in blobs:
        # url_dict.update({blob.name : blob.public_url})
        public_urls.append(blob.public_url)
    # print(url_dict)
    return(public_urls)

def find_show_week(showname):
    public_urls = list_blobs('wrek-01')
    mp3_urls = []
    week = []
    filename = []
    for url in public_urls:
        filepath  = os.path.join(url)
        filepath = os.path.normpath(filepath)
        filepath = filepath.split(os.sep)

        del filepath[0:3] #/<showname>/<week>/<mp3>
        week = filepath[1] #grab week
        # print(filepath)

        if filepath[0] == showname: # if /showname/x/x == showname
            for file in filepath:
                filename.append(filepath[2])
                print(filename)
                mp3_urls.append(url)
                print(mp3_urls)
            return(mp3_urls, week, filename)
        # upload_file_path = os.path.join(*filepath).replace("\\","/")



    # print(two_urls)

if __name__ == '__main__':
    find_show_week('Mode7')
