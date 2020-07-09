from google.cloud import storage
import os

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
    filename = []
    file = []
    weeks = set()
    test_dict = {}

    for url in public_urls:
        filepath = os.path.join(url)
        filepath = os.path.normpath(filepath)

        filepath = filepath.split(os.sep)

        del filepath[0:3] #/<showname>/<week>/<mp3>
        week = filepath[1]
        file = filepath[2] #ex. Sun1800.mp3

        if filepath[0] == showname:
            show_urls.append(url)
            for x in show_urls:
                test_dict.update({week : (x)})
            # print('show name DOES match show name in URL')
            # show_urls.append(url)
            # weeks.add(filepath[1]) # grab week number
            filename.append(file)
        else:
            pass
        # print(test_dict)
    # print(weeks)
    return(test_dict.items(), filename)
    # return(show_urls, weeks, filename)
        # upload_file_path = os.path.join(*filepath).replace("\\","/")



    # print(two_urls)

if __name__ == '__main__':
    find_show_url('Mode7')
