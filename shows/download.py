import os
from upload import upload_to_gcs
import urllib
import urllib.request

def download(urls, mp3_filename, complete_path):
    if os.path.exists(complete_path):
        print('Directory "%s" already exists' %complete_path)
    else:
        os.makedirs(complete_path)
        print('New directory "%s" was created' %complete_path)
    os.chdir(complete_path)
    try:
        urllib.request.urlretrieve(urls, mp3_filename)
        print('Successfully saved: ', mp3_filename)
        print(complete_path)
        # split up the local path in prep for uploading to GCS
        filepath  = os.path.join(complete_path)
        filepath = os.path.normpath(filepath)
        filepath = filepath.split(os.sep)
        # remove everything up to /showdata/<show name>/<week>/>
        # and then join above items back into a path
        del filepath[0:6]
        upload_file_path = os.path.join(*filepath).replace("\\","/")

        mp3_url_dict = upload_to_gcs(upload_file_path, mp3_filename)
        print(mp3_url_dict)

    except(ValueError):
        pass
