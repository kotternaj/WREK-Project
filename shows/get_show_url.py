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

def get_mode7_urls():
    public_urls = list_blobs('wrek-01')
    mode7_urls = []
    week = []
    filename = []
    for url in public_urls:
        filepath  = os.path.join(url)
        filepath = os.path.normpath(filepath)
        filepath = filepath.split(os.sep)
        # remove everything up to /<show name>/<week>/>
        # and then join above items back into a path
        del filepath[0:3]
        week = filepath[1]
        print(filepath)
        if filepath[0] == 'Mode7':
            filename.append(filepath[2])
            print(filename)
            mode7_urls.append(url)
    return(mode7_urls, week, filename)
        # upload_file_path = os.path.join(*filepath).replace("\\","/")


    # for url in public_url:
    #     str(url)
    #     print(url)
    # for k, v in url_dict.items():
    #     if k.startswith(k):
    #         key_list.append(k)
    #         print(key_list)


    # showpath = blob.name
    # show_name = showpath.split('/')
    # show = show_name[0]
    # if show_name[0] == show:
    #     pass
    # print(show_name)
    # print(show)
        # print(public_url)
    # return(two_urls)
    # two_urls = public_url[:2]
    # print(two_urls)

if __name__ == '__main__':
    get_mode7_urls()
