from google.cloud import storage
import os
from current_week import current_week
from create_m3u import create_m3u
from upload import upload_to_gcs

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
    # print(public_urls)
    show_urls = []
    test_dict = {}

    for url in public_urls:
        filepath = os.path.join(url)
        filepath = os.path.normpath(filepath)
        filepath = filepath.split(os.sep)

        del filepath[0:3] #/<showname>/<week>/<mp3>
        local_path = str(filepath[0] + '/' + filepath[1])
        # print(local_path)
        # local_path = os.path.join(*temp_path).replace("\\","/")
        week = filepath[1]
        file = filepath[2] #ex. Sun1800.mp3

        if filepath[0] == showname and week == str(current_week()):
            # test_dict.update({week : url})
            # print('show name DOES match show name in URL')
            show_urls.append(url)

            # weeks.add(filepath[1]) # grab week number
            # filename.append(file)
        else:
            # print('show name does NOT match')
            pass
    print(show_urls, local_path)
    upload_to_gcs(create_m3u(show_urls, local_path))
    # return(show_urls, local_path)

    # print(weeks)
    # return(test_dict.items())
    # return(show_urls, weeks, filename)
        # upload_file_path = os.path.join(*filepath).replace("\\","/")

# def isolate_show_parts(url):


    # print(two_urls)

if __name__ == '__main__':
    find_show_url('Mode7')
