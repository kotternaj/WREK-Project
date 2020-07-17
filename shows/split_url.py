import os

def split_urls(url):
    filepath = os.path.join(url)
    filepath = os.path.normpath(filepath)
    filepath = filepath.split(os.sep)
    del filepath[0:3] #/<showname>/<week>/<mp3>
    week = filepath[1]
    file = filepath[2] #ex. Sun1800.mp3
    return(filepath, week, file)
