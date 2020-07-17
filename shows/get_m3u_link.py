import os
from .split_url import split_url

def get_m3u_link(showname):
    m3u_dict = {}
    bucket_contents = list_blobs('wrek-01')
    for url in bucket_contents:
        filepath, week, file = split_url(url)
        # filepath = os.path.join(url)
        # filepath = os.path.normpath(filepath)
        # filepath = filepath.split(os.sep)
        #
        # del filepath[0:3] #/<showname>/<week>/<mp3>
        # print(filepath)
        # week = filepath[1]
        # file = filepath[2] #ex. Sun1800.mp3
        if file == 'playlist.m3u':
            if filepath[0] == showname:
                m3u_dict.update({ week: url })
    return(m3u_dict.items())
