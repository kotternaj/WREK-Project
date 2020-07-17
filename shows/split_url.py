import os

def split_url(url):
    filepath = os.path.join(url)
    filepath = os.path.normpath(filepath)
    filepath = filepath.split(os.sep) # split up each part of the URL
    del filepath[0:3] # results in path of /<showname>/<week>/<mp3>
    week = filepath[1]
    file = filepath[2] # ex. Sun1800.mp3
    return(filepath, week, file)
