import os
from upload import upload_to_gcs
import urllib
import urllib.request

def download(urls, mp3_filename, complete_path):
    if os.path.exists(complete_path):
        print('Directory "%s" already exists' %complete_path)
    else:
        os.makedirs(complete_path) # create a new directory if one doesn't exist
        print('New directory "%s" was created' %complete_path)
    os.chdir(complete_path) # change into that directory
    try:
        urllib.request.urlretrieve(urls, mp3_filename)
        print('Successfully saved: ', mp3_filename)
        print(complete_path)

        filepath  = os.path.join(complete_path) # split up the local path in prep for uploading to GCS
        filepath = os.path.normpath(filepath)
        filepath = filepath.split(os.sep)
        del filepath[0:7] # remove everything up to /<show name>/<week>/>
        upload_file_path = os.path.join(*filepath).replace("\\","/") # then join above items back into a path
        return(upload_file_path, mp3_filename)

    except(ValueError):
        pass
